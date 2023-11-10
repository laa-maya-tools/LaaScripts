# -*- coding: utf-8 -*-
import ActorManager.Plugins.AnimPresetHolder as AnimPresetHolder

import maya.api.OpenMaya as OpenMaya

import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class CameraSet(AnimPresetHolder.AnimPresetHolder, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName    = "cameraSetActor"
    nodeID      = NodeID.ActorManagerCameraSetID
    
    # Attributes
    name            = OpenMaya.MObject()
    path            = OpenMaya.MObject()
    cameras         = OpenMaya.MObject()
    cameraLeft      = OpenMaya.MObject()
    cameraRight     = OpenMaya.MObject()
    actor           = OpenMaya.MObject()
      
    @staticmethod
    def creator():
        return CameraSet()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()     
        
        # Name
        CameraSet.name = typedAttribute.create("name", "nm", OpenMaya.MFnData.kString)
        CameraSet.addAttribute(CameraSet.name)

        # Path
        CameraSet.path = typedAttribute.create("path", "pth", OpenMaya.MFnData.kString)
        CameraSet.addAttribute(CameraSet.path)

        # Cameras
        CameraSet.cameras = messageAttribute.create("cameras", "cs")
        messageAttribute.array = True
        #messageAttribute.indexMatters = True
        messageAttribute.writable = True
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        messageAttribute.readable = False
        CameraSet.addAttribute(CameraSet.cameras) 

        # CameraLeft
        CameraSet.cameraLeft = messageAttribute.create("cameraLeft", "cl")
        messageAttribute.writable = True
        CameraSet.addAttribute(CameraSet.cameraLeft) 

        # CameraLeft
        CameraSet.cameraRight = messageAttribute.create("cameraRight", "cr")
        messageAttribute.writable = True
        CameraSet.addAttribute(CameraSet.cameraRight) 
        
        # Actor       
        CameraSet.actor = messageAttribute.create("actor", "ac")
        messageAttribute.writable = True
        messageAttribute.readable = False
        CameraSet.addAttribute(CameraSet.actor)
        
        # AnimPresetHolder initializer
        AnimPresetHolder.AnimPresetHolder.initializer()
        
    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)
