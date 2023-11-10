# -*- coding: utf-8 -*-
import NodeID.PluginNodes as PluginNodes

import maya.api.OpenMaya as OpenMaya

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class RigChain(OpenMaya.MPxNode, PluginNodes.PluginNode):
    
    # Attributes
    rig = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return RigChain()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        
        # Rig
        RigChain.rig = messageAttribute.create("rig", "rig")
        messageAttribute.readable = True
        messageAttribute.writable = False
        RigChain.addAttribute(RigChain.rig)
    
    def postConstructor(self):
        self.setExistWithoutInConnections(False)
        self.setExistWithoutOutConnections(False)
