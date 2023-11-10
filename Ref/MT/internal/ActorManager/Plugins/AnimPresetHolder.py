# -*- coding: utf-8 -*-

import maya.api.OpenMaya as OpenMaya

class AnimPresetHolder(OpenMaya.MPxNode):
    
    # Attributes
    animPresetList  = OpenMaya.MObject()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        
        # Anim Presets
        AnimPresetHolder.animPresetList = messageAttribute.create("animPresetList", "apl")
        messageAttribute.array = True
        #messageAttribute.indexMatters = False
        messageAttribute.writable = True
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        messageAttribute.readable = False
        AnimPresetHolder.addAttribute(AnimPresetHolder.animPresetList)
    