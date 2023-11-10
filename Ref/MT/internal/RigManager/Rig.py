# -*- coding: utf-8 -*-
from  NodeManager   import NodeWrapper

import maya.cmds as cmds

from NodeCustom.Management.NodeCollection import NodeCollection

import RigManager.RigChain as RigChain

import Utils.Maya.AnimLayers as AnimLayerUtils
from Utils.Maya.UndoContext import UndoContext

import mutils.mirrortable as StudioLibraryMirror
import mutils.selectionset as StudioLibrarySelectionSet

import ProjectPath

import os

STUDIOLIBRARY_PATH = os.path.join(ProjectPath.Tokens.curled(ProjectPath.Tokens.TSubActorAnimPath), "studiolibrary")
STUDIOLIBRARY_MIRROR_TABLE_PATH = os.path.join(STUDIOLIBRARY_PATH, "MirrorTables", "MirrorTable.mirror", "mirrortable.json")
STUDIOLIBRARY_SELECTION_SET_PATH = os.path.join(STUDIOLIBRARY_PATH, "SelectionSets", "SelectionSet.set", "set.json")

class Rig(NodeWrapper.NodeWrapper):
    
    _Type           = "rig"
    _actor          = "actor"
    _controls       = "controls"
    _rigChains      = "rigChains"
    _mainControl    = "mainControl"
    _cogControl     = "cogControl"
    
    def __init__(self, node=None):
        super(Rig, self).__init__(node)
    
    # Properties ------------
    
    @property
    def controls(self):
        return self.getCollectionAttribute(self._controls, NodeCollection)
    
    @controls.setter
    def controls(self, value):
        with UndoContext("Set Rig Controls"):
            controls = self.controls
            controls.clear()
            if value:
                controls += value
    
    @property
    def mainControl(self):
        return self.getInputSingle(self._mainControl)
    
    @mainControl.setter
    def mainControl(self, value):
        with UndoContext("Set Rig Main Control"):
            if value == None:
                self.clearConnection(self._mainControl)
            else:
                self.connect(self.getPlug(self._mainControl), "{}.message".format(value))
    
    @property
    def cogControl(self):
        return self.getInputSingle(self._cogControl)
    
    @cogControl.setter
    def cogControl(self, value):
        with UndoContext("Set Rig Cog Control"):
            if value == None:
                self.clearConnection(self._cogControl)
            else:
                self.connect(self.getPlug(self._cogControl), "{}.message".format(value))
    
    # Methods ---------------
    
    def getActor(self):
        import ActorManager.Actor as Actor
        ActorWrapperList   = self.getOutputSingle(self._actor, cls=Actor.Actor)
        if ActorWrapperList:
            return ActorWrapperList[0]
        return None
    
    def getControls(self):
        # This methods is used to return a copy of the list so it won't be modified
        #return list(self.controls)
        # The rig are not correctly configured yet, so we use the Actor's SelectionSet (from StudioLibrary) to know which controls to use.
        selectionSet = self.getSelectionSet()
        namespace = self.getActor().getNamespace()
        objects = [object.split(":")[-1] for object in selectionSet.objects()]
        objects = ["{}:{}".format(namespace, object) for object in objects]
        objects = [object for object in objects if cmds.objExists(object)]
        return objects
        
    def getMirrorTable(self):
        pathTokenizer = self.getActor().animSubActor.getPathTokenizer(branch="{3D}")
        mirrorTablePath = pathTokenizer.Translate(STUDIOLIBRARY_MIRROR_TABLE_PATH)
        mirrorTable = StudioLibraryMirror.MirrorTable.fromPath(mirrorTablePath)
        return mirrorTable
    
    def getSelectionSet(self):
        pathTokenizer = self.getActor().animSubActor.getPathTokenizer(branch="{3D}")
        selectionSetPath = pathTokenizer.Translate(STUDIOLIBRARY_SELECTION_SET_PATH)
        selectionSet = StudioLibrarySelectionSet.SelectionSet.fromPath(selectionSetPath)
        return selectionSet
    
    # Rig Chains ------------
    
    def getRigChains(self, wrapper=True):
        if wrapper:
            wrapperCLS = RigChain.RigChain
        else:
            wrapperCLS = None   
        return self.getInputFromListAttribute(self._rigChains, cls=wrapperCLS)
    
    def setRigChains(self, rigChains):
        with UndoContext("Set Rig Chains"):
            self.setInputListNodes(self._rigChains, rigChains, inputAttribute=RigChain.RigChain._rig)
    
    def appendRigChains(self, rigChains):
        with UndoContext("Append Rig Chains"):
            self.appendInputList(self._rigChains, rigChains, inputAttribute=RigChain.RigChain._rig)
    
    def addRigChain(self, rigChain):
        with UndoContext("Add Rig Chain"):
            self.addItem( self._rigChains, rigChain.getPlug(RigChain.RigChain._rig))
    
    def insertRigChain(self, rigChain, index):
        with UndoContext("Insert Rig Chain"):
            self.insertItemList(self._rigChains, index, rigChain.getPlug(RigChain.RigChain._rig))
    
    def removeRigChain(self, rigChain, delete=True):
        with UndoContext("Remove Rig Chain"):
            self.removeItemListByPlug(self._rigChains, rigChain.getPlug(RigChain.RigChain._rig), delete=delete)

    # AnimLayers ------------
    
    def addControlsToLayer(self, animLayer):
        AnimLayerUtils.addNodesToLayer(animLayer, self.getControls(), skipEnumAttributes=True)
    
    def removeControlsFromLayer(self, animLayer):
        AnimLayerUtils.removeNodesFromLayer(animLayer, self.getControls())
    
    def extractControlsFromLayer(self, sourceLayer, targetLayer):
        AnimLayerUtils.extractNodesFromLayer(sourceLayer, targetLayer, self.getControls())
    
    # Mirror ---------------
    
    def mirrorAnimation(self, mirrorTable=None):
        with UndoContext("Mirror Animation"):
            if mirrorTable == None:
                mirrorTable = self.getMirrorTable()
            
            namespace = self.getActor().getNamespace()
            mirrorTableObjects = mirrorTable.objects()
            mirrorTableObjects = ["{}:{}".format(namespace, obj.split(":")[-1]) for obj in mirrorTableObjects]
            
            cmds.delete(cmds.animLayer())
            
            currTime = cmds.currentTime(q=True)
            oldSelection = cmds.ls(selection=True) or []
            
            allAnimLayers = AnimLayerUtils.getAnimLayers()
            animLayers = [animLayer for animLayer in allAnimLayers if not cmds.animLayer(animLayer, q=True, mute=True)]
            for animLayer in allAnimLayers:
                if not AnimLayerUtils.isBaseLayer(animLayer):
                    cmds.animLayer(animLayer, e=True, mute=True, lock=True)
                else:
                    baseLayer = animLayer
                    wasBaseLayerLocked = cmds.animLayer(baseLayer, q=True, lock=True)
                    cmds.animLayer(baseLayer, e=True, lock=False)
                cmds.animLayer(animLayer, e=True, selected=False)
                
            AnimLayerUtils.forceAnimLayerUIUpdate()
            
            for animLayer in animLayers:
                isBaseLayer = animLayer == baseLayer
                if not isBaseLayer:
                    cmds.animLayer(animLayer, e=True, mute=False, lock=False)
                        
                    layerPlugs = AnimLayerUtils.getPlugsOnLayer(animLayer)
                    layerObjects = set(plug.split(".")[0] for plug in layerPlugs)
                    layerObjects = set([obj for obj in layerObjects if obj in mirrorTableObjects])
                else:
                    layerObjects = mirrorTableObjects
                
                cmds.animLayer(animLayer, e=True, selected=True)
                cmds.animLayer(animLayer, e=True, preferred=True)
                
                AnimLayerUtils.forceAnimLayerUIUpdate()
                
                cmds.select(layerObjects)
                
                mirrorTable.load(objects=layerObjects, option=StudioLibraryMirror.MirrorOption.Swap, keysOption=StudioLibraryMirror.KeysOption.All)
                
                cmds.animLayer(animLayer, e=True, selected=False)
                
                if not isBaseLayer:
                    cmds.animLayer(animLayer, e=True, mute=True, lock=True)
                    
            cmds.animLayer(baseLayer, e=True, lock=wasBaseLayerLocked)
                    
            cmds.select(oldSelection)
            cmds.currentTime(currTime, e=True)
