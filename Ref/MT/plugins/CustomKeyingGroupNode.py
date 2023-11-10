import maya.api.OpenMaya as OpenMaya

import AnimSystems.KeyingGroup as KeyingGroup

import NodeID

import sys

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class CustomKeyingGroup(OpenMaya.MPxNode):
    
    # Plugin data
    nodeName = "customKeyingGroup"
    
    enabled = OpenMaya.MObject()
    affectedAttributes = OpenMaya.MObject()
    parentKeyingGroup = OpenMaya.MObject()
    childKeyingGroups = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return CustomKeyingGroup()

    @staticmethod
    def initializer():
        
        messageAttribute = OpenMaya.MFnMessageAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        genericAttribute = OpenMaya.MFnGenericAttribute()
        
        # Enabled
        CustomKeyingGroup.enabled = numericAttribute.create("enabled", "e", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.keyable = False
        CustomKeyingGroup.addAttribute(CustomKeyingGroup.enabled)
        
        # Affected Attributes
        CustomKeyingGroup.affectedAttributes = genericAttribute.create("affectedAttributes", "at")
        genericAttribute.array = True
        genericAttribute.writable = True
        genericAttribute.readable = False
        genericAttribute.keyable = False
        genericAttribute.disconnectBehavior = genericAttribute.kDelete
        genericAttribute.addDataType(OpenMaya.MFnData.kNumeric)
        CustomKeyingGroup.addAttribute(CustomKeyingGroup.affectedAttributes)
        
        # Parent Keying Group
        CustomKeyingGroup.parentKeyingGroup = messageAttribute.create("parentKeyingGroup", "p")
        messageAttribute.writable = False
        messageAttribute.readable = True
        CustomKeyingGroup.addAttribute(CustomKeyingGroup.parentKeyingGroup)
        
        # Child Keying Groups
        CustomKeyingGroup.childKeyingGroups = messageAttribute.create("childKeyingGroups", "c")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        CustomKeyingGroup.addAttribute(CustomKeyingGroup.childKeyingGroups)


# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    try:
        mplugin.registerNode(CustomKeyingGroup.nodeName, NodeID.CustomKeyingGroupID, CustomKeyingGroup.creator, CustomKeyingGroup.initializer)
    except:
        sys.stderr.write("Failed to register node: " + CustomKeyingGroup.nodeName)
        raise
    
    KeyingGroup.KeyingGroupManager.initialize()

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    KeyingGroup.KeyingGroupManager.uninitialize()
    
    try:
        mplugin.deregisterNode(NodeID.CustomKeyingGroupID)
    except:
        sys.stderr.write("Failed to unregister node: " + CustomKeyingGroup.nodeName)
        raise
