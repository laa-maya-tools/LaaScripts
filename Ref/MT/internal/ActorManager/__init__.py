# -*- coding: utf-8 -*-

import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext

import ActorManager.Actor as Actor
import ActorManager.CameraSet as CameraSet

import NodeCustom.Management.NodeCollection as NodeCollection

import os
import re

# TODO quizás algunas funciones no deberían estar en NodeWrapper,
#  getSelectionNodes o existNode con el flag sceneNode

def getActors(wrapper=True):
    nodeList = cmds.ls(type=Actor.Actor._Type, ap=True) 
    if wrapper:
        return Actor.Actor.getWrapperList(nodeList)
    else:
        return nodeList

def getCameraSets(wrapper=True):
    nodeList = cmds.ls(type=CameraSet.CameraSet._Type, ap=True) 
    if wrapper:
        return CameraSet.CameraSet.getWrapperList(nodeList)
    else:
        return nodeList
    
def getCameraSetsFromCamera(camera):
    if cmds.nodeType(camera) == "camera":
        camera = cmds.listRelatives(camera, parent=True)[0]
        
    nodeCollections = cmds.listConnections("{}.message".format(camera), s=False, d=True, type=NodeCollection.NodeCollection._Type)
    if not nodeCollections:
        return []
    
    cameraSets = cmds.listConnections(nodeCollections, s=False, d=True, type=CameraSet.CameraSet._Type) or []
    return cameraSets

def getCameraSetByName(cameraSetName):
    cameraSets = getCameraSets()
    for cameraSet in cameraSets:
        if cameraSet.name == cameraSetName:
            return cameraSet
    return None
    
def isExportCamera(camera):
    return len(getCameraSetsFromCamera(camera)) > 0
    
def createActor(actorName):
    with UndoContext("Create Actor"):
        actor = Actor.Actor()
        actor.create()
        actor.name = actorName
        return actor

def getActorByNameSpace(namespace, wrapper=True):
    actorsByNamespace = cmds.ls("{}::*".format(namespace), type="actor")
    if actorsByNamespace:
        actor = actorsByNamespace[0]
        if wrapper:
            return Actor.Actor(actor)
        else: 
            return actor
    return None

def isNamespaceInUse(namespace):
    return cmds.namespace(ex=namespace)

def isActorNameInUse(actorName):
    actors = getActors()
    for actor in actors:
        if actor.getNamespace() == actorName:
            return True
    return False

def isActorLoaded(actor):
    referenceNode = actor.getReferenceNode()
    return cmds.referenceQuery(referenceNode, il=True)

def loadActorReference(actor):
    if not isActorLoaded(actor):
        cmds.file(loadReference=actor.getReferenceNode())

def unloadActorReference(actor):
    if isActorLoaded(actor):
        cmds.file(unloadReference=actor.getReferenceNode())

def duplicateActorReference(actor):
    referenceFile = cmds.referenceQuery(actor.getReferenceNode(), filename=True)
    return createActorReference(referenceFile, namespace=actor.getNamespace(), autoRename=True)

def deleteActorReference(actor):
    cmds.file(removeReference=True, referenceNode=actor.getReferenceNode())
    
def getNextAvailableNamespace(namespace, forceNumber=False):
    if cmds.namespace(ex=namespace) or forceNumber:
        match = re.search(r'\d+$', namespace)
        if match:
            numberStr = match.group(0) or "0"
            name = namespace[:-len(numberStr)]
            number = int(numberStr) + 1
        else:
            name = namespace
            number = 1
    
        while True:
            namespace = "{}{}".format(name, number)
            if not cmds.namespace(ex=namespace):
                break
            number += 1
    
    return namespace
    
def createActorReference(filePath, namespace=None, autoRename=False, forceNumber=False):
    temporalReferenceNamespace = "TEMP_REFERENCE_NAMESPACE"
    temporalReferenceGroupName = "TEMP_REFERENCE_GROUP_NAME"
    
    if namespace != None and cmds.namespace(ex=namespace) and not autoRename:
        raise AssertionError("The provided namespace {} already exists.".format(namespace))
    
    referenceNodeName = "{}_RN".format(os.path.basename(filePath).split(".")[0])
    referenceFile = cmds.file(filePath, reference=True, groupReference=True, groupName=temporalReferenceGroupName, usingNamespaces=True, namespace=temporalReferenceNamespace, referenceNode=referenceNodeName)
    
    if not cmds.namespace(ex=temporalReferenceNamespace):
        # The operation was aborted by the user
        return None
    
    actor = getActorByNameSpace(temporalReferenceNamespace)
    if actor == None:
        cmds.file(referenceFile, removeReference=True)
        raise AssertionError("The referenced file is not an Actor.")
    
    cmds.rename(temporalReferenceGroupName, "{}:{}".format(temporalReferenceNamespace, actor.name))
    
    if namespace == None:
        namespace = actor.name
    namespace = getNextAvailableNamespace(namespace, forceNumber=forceNumber)
    
    cmds.namespace(rename=(temporalReferenceNamespace, namespace), parent=":")
    
    return namespace

def mergeActorAnimFile(filePath, namespace=None, autoRename=False, forceNumber=False):
    temporalReferenceNamespace = "TEMP_REFERENCE_NAMESPACE"
    
    if namespace != None and cmds.namespace(ex=namespace) and not autoRename:
        raise AssertionError("The provided namespace {} already exists.".format(namespace))
    
    mergedNodes = cmds.file(filePath, i=True, namespace=temporalReferenceNamespace, preserveReferences=True, returnNewNodes=True)
    
    if not cmds.namespace(ex=temporalReferenceNamespace):
        # The operation was aborted by the user
        return None
    
    actor = getActorByNameSpace(temporalReferenceNamespace)
    if actor == None:
        for obj in mergedNodes:
            if cmds.nodeType(obj) == "reference":
                cmds.file(removeReference=True, referenceNode=obj)
                break
        cmds.delete([obj for obj in mergedNodes if cmds.objExists(obj)])
        raise AssertionError("The merged file is not an Actor.")
    
    if namespace == None:
        namespace = actor.name
    namespace = getNextAvailableNamespace(namespace, forceNumber=forceNumber)
    
    # If there is a reference in the file, assign the namespace to that reference
    # Multiple references on the merged file are not supported
    referenceNode = actor.getReferenceNode()
    if referenceNode:
        actorNamespace = cmds.referenceQuery(referenceNode, namespace=True)
        
        cmds.lockNode(referenceNode, lock=False)
        referenceNode = cmds.rename(referenceNode, "{}:{}_RN".format(temporalReferenceNamespace, namespace))
        referenceFile = cmds.referenceQuery(referenceNode, filename=True)
        cmds.file(referenceFile, e=True, namespace=namespace)
        
        # Moves the contents of the previous namespace of the reference to the new one.
        # This is done becouse there could be nodes added to a reference's namespace that are not moved when changing the reference's namespace.
        if cmds.namespace(ex=actorNamespace):
            cmds.namespace(moveNamespace=(actorNamespace, namespace))
            cmds.namespace(removeNamespace=actorNamespace)
    else:
        cmds.namespace(add=namespace)
    
    # This lines would be necessary if the merged _anim files wouldn't have their nodes grouped.
    #dagParents = [node for node in mergedNodes if cmds.objectType(node, isAType="transform") and not cmds.listRelatives(node, parent=True)]
    #cmds.group(dagParents, name="{}:{}".format(temporalReferenceNamespace, actor.name), world=True)
    
    # Moves the rest of imported nodes to the namespace from the temporal one and deletes it
    cmds.namespace(moveNamespace=(temporalReferenceNamespace, namespace), force=True)
    cmds.namespace(removeNamespace=temporalReferenceNamespace)
    
    return namespace
