# -*- coding: utf-8 -*-
from  NodeManager   import NodeWrapper
import ActorManager.AnimPresetHolder as AnimPresetHolder

import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext
from Utils.Python.Enum import EnumBase

from NodeCustom.Management.NodeCollection import NodeCollection
#from  ActorManager  import  Actor
#from  ActorManager  import  AnimPreset

import ProjectPath
import Exporter

class SubActor(NodeWrapper.NodeWrapper, AnimPresetHolder.AnimPresetSubHolder):
    _Type = "subActor"

    class Tags(EnumBase):
        Animatable  = "animatable"
        Model       = "model"

    #nodeName
    _name               = "name"
    _tags               = "tags"
    _path               = "path"
    _actor              = "actor"
    _animPreset         = "animPreset"
    _subActorPathToken  = "subActorPathToken"
    _exportPath         = "exportPath"
    _animPath           = "animPath"
    _modelPath          = "modelPath"
    _modelName          = "modelName"
    _modelFileType      = "modelFileType"
    _isModelExportable  = "isModelExportable"
    _cinematicCharclass = "cinematicCharclass"
    
    _parentSet          = "parentSet"
    _dcRootSet          = "dcRootSet"
    _jointSet           = "jointSet"
    _geometrySet        = "geometrySet"

    def __init__(self, node=None):
        super(SubActor, self).__init__(node)

    # ____________________________________________________________________
    # PROPERTIES _________________________________________________________

    # name --------------------------------------
    @property
    def name(self):
        return self.getAttr(self._name)

    @name.setter
    def name(self, value):
        split = value.split("_{}".format(self._Type))
        if len(split) > 0:
            value = split[0]
        nodeName = "{}_{}".format(value, self._Type)
        
        if self.nodeExists():
            if self.name != value:
                if not cmds.objExists(nodeName) or self.node == nodeName:
                    with UndoContext("Set SubActor Name"):
                        self.setStringAttribute(self._name, value)
                        self.renameNode(nodeName)
                else:
                    raise AssertionError("Attempting to rename a SubActor with an already existing SubActor name!")
        else:
            raise AssertionError("Attempting to rename an unexisting SubActor!")

    #Export values --------------------------------------
    
    @property
    def subActorPathToken(self):
        return self.getAttr(self._subActorPathToken)
    
    @subActorPathToken.setter
    def subActorPathToken(self, value):
        self.setStringAttribute(self._subActorPathToken, value)
    
    @property
    def exportPath(self):
        return self.getAttr(self._exportPath)
    
    @exportPath.setter
    def exportPath(self, value):
        self.setStringAttribute(self._exportPath, value)
    
    @property
    def animPath(self):
        return self.getAttr(self._animPath)
    
    @animPath.setter
    def animPath(self, value):
        self.setStringAttribute(self._animPath, value)
    
    @property
    def modelPath(self):
        return self.getAttr(self._modelPath)
    
    @modelPath.setter
    def modelPath(self, value):
        self.setStringAttribute(self._modelPath, value)
    
    @property
    def modelName(self):
        return self.getAttr(self._modelName)
    
    @modelName.setter
    def modelName(self, value):
        self.setStringAttribute(self._modelName, value)
    
    @property
    def isModelExportable(self):
        return self.getAttr(self._isModelExportable)
    
    @isModelExportable.setter
    def isModelExportable(self, value):
        self.setNumericAttribute(self._isModelExportable, value)

    @property
    def modelFileType(self):
        return self.getAttr(self._modelFileType)
        
    @modelFileType.setter
    def modelFileType(self, value):
        self.setNumericAttribute(self._modelFileType, value)

    @property
    def modelFileTypeStr(self):
        return self.getEnumerateValue(self._modelFileType, self.modelFileType)
        
    @modelFileTypeStr.setter
    def modelFileTypeStr(self, value): 
        self.modelFileType = self.getEnumerateIndex(self._modelFileType, value)
    
    @property
    def cinematicCharclass(self):
        return self.getAttr(self._cinematicCharclass)
    
    @cinematicCharclass.setter
    def cinematicCharclass(self, value):
        self.setStringAttribute(self._cinematicCharclass, value)
    
    # override ------------------------------------------------------
    def getCollectionName(self):
        return self.name
    
    def getFileTypes(self):
        return self.getEnumerateList(self._modelFileType)

    # tags ---------------------------------------------------------------
    @property
    def tags(self):
        return self.getAttr(self._tags)
    
    @tags.setter
    def tags(self, listValue):
        with UndoContext("Set SubActor Tags"):
            self.setStringArrayAttribute(self._tags, listValue)
            
    # ____________________________________________________________________
    # METHODS ____________________________________________________________
    
    # create/delete ------------------------------------------------------
    # el nombre se añade sin el sufijo subActor, este se compone despues.
    def create(self, name=None):
        if name == None:
            raise NotImplementedError("Creating a SubActor requieres a name for it, but none was specified.")
        
        with UndoContext("Create SubActor"):
            split = name.split("_{}".format(self._Type))
            if len(split) > 0:
                name = split[0]
                
            nodeName = "{}_{}".format(name, self._Type)
            super(self.__class__, self).create(nodeName=nodeName, unique=True)
            
            self.name = name

    def delete(self):
        with UndoContext("Delete SubActor"):
            (self.getCollectionAttribute(self._dcRootSet, NodeCollection)).delete()
            (self.getCollectionAttribute(self._jointSet, NodeCollection)).delete()
            (self.getCollectionAttribute(self._geometrySet, NodeCollection)).delete()

            super(self.__class__,self).delete()
    
    # getNodesBySet ------------------------------------------------------

    def getDCRootNode(self):
        return self.getCollectionAttribute(self._dcRootSet, NodeCollection).first()
    
    def getDCRootControlNode(self):
        dcRoot = self.getDCRootNode()
        
        constraint = cmds.parentConstraint(dcRoot, q=True)
        if constraint:
            return cmds.parentConstraint(constraint, q=True, targetList=True)[0]
        
        constraint = cmds.pointConstraint(dcRoot, q=True)
        if constraint:
            return cmds.pointConstraint(constraint, q=True, targetList=True)[0]
        
        constraint = cmds.orientConstraint(dcRoot, q=True)
        if constraint:
            return cmds.orientConstraint(constraint, q=True, targetList=True)[0]
        
        return None

    def getGeometryNodes(self):
        return list(self.getCollectionAttribute(self._geometrySet, NodeCollection))
    
    def getJointNodes(self):
        return list(self.getCollectionAttribute(self._jointSet, NodeCollection))

    # set ------------------------------------------------------

    def addDcRoot(self, node):
        with UndoContext("Register DC_Root on SubActor"):
            self.getCollectionAttribute(self._dcRootSet, NodeCollection)[0] = node

    def addGeometries(self, nodes):
        with UndoContext("Register Geometries on SubActor"):
            if (len(nodes) > 0):
                aux = self.getCollectionAttribute(self._geometrySet, NodeCollection)
                aux += nodes

    def addJoints(self, nodes):
        with UndoContext("Register Joints on SubActor"):
            if (len(nodes) > 0):
                aux = self.getCollectionAttribute(self._jointSet, NodeCollection)
                aux += nodes

    # remove ------------------------------------------------------

    def removeGeometries( self, theNodes):
        with UndoContext("Unregister Geometries on SubActor"):
            theWrapper = self.getCollectionAttribute(self._geometrySet, NodeCollection)
            theWrapper.reorderMode=False
            for node in theNodes:
                theWrapper.remove(node)
            theWrapper.reorderMode=True
            theWrapper.rebuildList(theWrapper._list)    

    def removeJoints( self, theNodes):
        with UndoContext("Unregister Joints on SubActor"):
            theWrapper = self.getCollectionAttribute(self._jointSet, NodeCollection)
            theWrapper.reorderMode=False
            for node in theNodes:
                theWrapper.remove(node)
            theWrapper.reorderMode=True
            theWrapper.rebuildList(theWrapper._list)

    # clear ------------------------------------------------------
    
    def clearDcRoot(self):
        with UndoContext("Clear SubActor DC_Root Set"):
            self.getCollectionAttribute(self._dcRootSet, NodeCollection).clear()

    def clearJoints(self):
        with UndoContext("Clear SubActor Joint Set"):
            self.getCollectionAttribute(self._jointSet, NodeCollection).clear()

    def clearGeometries(self):
        with UndoContext("Clear SubActor Joint Set"):
            self.getCollectionAttribute(self._geometrySet, NodeCollection).clear()

    # Commodity access to actor (parent) data ------------------------------------------------------
    def getActor(self):
        from  ActorManager  import  Actor
        ActorWrapperList   = self.getOutputSingle(self._actor, cls=Actor.Actor)
        if ActorWrapperList:
            return ActorWrapperList[0]
        return None
    
    def isMainSubActor(self):
        actor = self.getActor()
        if actor and actor.mainSubActor:
            return self.node == actor.mainSubActor.node
        return False
    
    def isAnimSubActor(self):
        actor = self.getActor()
        if actor and actor.animSubActor:
            return self.node == actor.animSubActor.node
        return False

    #--------- OVERRIDE
    
    def getHolder(self):
        return self.getActor()
    
    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = self.getActor().getPathTokenizer(branch=branch)
        pathTokenizer.Update({ ProjectPath.Tokens.TSubActorName : self.name })
        pathTokenizer.Update({ ProjectPath.Tokens.TSubActorPath : self.subActorPathToken })
        pathTokenizer.Update({ ProjectPath.Tokens.TSubActorExportPath : self.exportPath })
        pathTokenizer.Update({ ProjectPath.Tokens.TSubActorAnimPath : self.animPath })
        pathTokenizer.Update({ ProjectPath.Tokens.TSubActorModelPath : self.modelPath })
        return pathTokenizer
    
    def getSubHolderPlug(self):
        return self._actor

    def getAnimPath(self):
        return self.animPath

    def getDisplayName(self):
        if self.isAnimSubActor():
            return self.getActor().getDisplayName()
        else:
            return self.name

    def getExportNodes(self, data):
        return [self.getDCRootNode()]
    
    def mirrorAnimation(self, data):
        self.getActor().rig.mirrorAnimation()
        return data
    
    def getExportFileType(self):
        return Exporter.EXPORTER_ANIMATION_FILE_TYPE
    