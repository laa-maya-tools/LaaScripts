# -*- coding: utf-8 -*-
import NodeID
import NodeID.PluginNodes as PluginNodes

import maya.api.OpenMaya as OpenMaya

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class Rig(OpenMaya.MPxNode, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName    = "rig"
    nodeID      = NodeID.RigManagerRigID
    
    # Attributes
    actor       = OpenMaya.MObject()
    controls    = OpenMaya.MObject()
    rigChains   = OpenMaya.MObject()
    mainControl = OpenMaya.MObject()
    cogControl  = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return Rig()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        
        # Actor
        Rig.actor = messageAttribute.create("actor", "ac")
        messageAttribute.readable = True
        messageAttribute.writable = False
        Rig.addAttribute(Rig.actor)
        
        # Controls
        Rig.controls = messageAttribute.create("controls", "ctls")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Rig.addAttribute(Rig.controls)
        
        # Rig Chains
        Rig.rigChains = messageAttribute.create("rigChains", "rc")
        messageAttribute.writable = True
        messageAttribute.array = True
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        messageAttribute.readable = False
        Rig.addAttribute(Rig.rigChains)
    
        # Main Control       
        Rig.mainControl = messageAttribute.create("mainControl", "mc")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Rig.addAttribute(Rig.mainControl)
    
        # Main Control       
        Rig.cogControl = messageAttribute.create("cogControl", "cog")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Rig.addAttribute(Rig.cogControl)
        
    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(False)
