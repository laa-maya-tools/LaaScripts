# -*- coding: utf-8 -*-
import NodeID
import NodeID.PluginNodes as PluginNodes
#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class SubActor(OpenMaya.MPxNode, PluginNodes.PluginNode):

    # Plugin data
    nodeName = "subActor"
    nodeID      = NodeID.ActorManagerSubActorID
    
    fileTypesDict = {
        '.fbx': 0,
        '.fmdb': 1,
    }

    name = OpenMaya.MObject()
    tags = OpenMaya.MObject()
    
    actor = OpenMaya.MObject()
    animPreset = OpenMaya.MObject()
    
    subActorPathToken  = OpenMaya.MObject()
    exportPath  = OpenMaya.MObject()
    modelPath   = OpenMaya.MObject()
    animPath = OpenMaya.MObject()
    
    modelName = OpenMaya.MObject()
    modelFileType = OpenMaya.MObject()
    modelExportable = OpenMaya.MObject()
    
    cinematicCharclass = OpenMaya.MObject()
    
    parentSet = OpenMaya.MObject()
    dcRootSet = OpenMaya.MObject()
    jointSet = OpenMaya.MObject()
    geometrySet = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return SubActor()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()  
        enumAttribute = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        
        #actor        
        SubActor.actor = messageAttribute.create("actor", "ac")
        messageAttribute.writable = False
        messageAttribute.readable = True
        SubActor.addAttribute(SubActor.actor)    
        
        #tags
        SubActor.tags = typedAttribute.create("tags", "t", OpenMaya.MFnData.kStringArray)
        typedAttribute.default=OpenMaya.MFnStringArrayData().create([])
        SubActor.addAttribute(SubActor.tags)
        
        #parentSet       
        SubActor.parentSet = messageAttribute.create("parentSet", "ps")
        messageAttribute.writable = True
        messageAttribute.readable = False
        SubActor.addAttribute(SubActor.parentSet)  
        
        #dcRootSet       
        SubActor.dcRootSet = messageAttribute.create("dcRootSet", "dcr")
        messageAttribute.writable = True
        messageAttribute.readable = False
        SubActor.addAttribute(SubActor.dcRootSet)    
        
        #jointSet       
        SubActor.jointSet = messageAttribute.create("jointSet", "js")
        messageAttribute.writable = True
        messageAttribute.readable = False
        SubActor.addAttribute(SubActor.jointSet)    
        
        #GeometrySet       
        SubActor.geometrySet = messageAttribute.create("geometrySet", "gs")
        messageAttribute.writable = True
        messageAttribute.readable = False
        SubActor.addAttribute(SubActor.geometrySet)    
        
        #name
        SubActor.name = typedAttribute.create("name", "nm", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.name)
        
        #subActorPathToken
        SubActor.subActorPathToken = typedAttribute.create("subActorPathToken", "saptht", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.subActorPathToken)
        
        #export path
        SubActor.exportPath = typedAttribute.create("exportPath", "epth", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.exportPath)
        
        #model path
        SubActor.modelPath = typedAttribute.create("modelPath", "mpth", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.modelPath)
        
        #anim path
        SubActor.animPath = typedAttribute.create("animPath", "apth", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.animPath)
        
        #export model name
        SubActor.modelName = typedAttribute.create("modelName", "modn", OpenMaya.MFnData.kString )
        SubActor.addAttribute(SubActor.modelName)
        
        SubActor.modelExportable = numericAttribute.create("isModelExportable", "mexp", OpenMaya.MFnNumericData.kBoolean, True)
        SubActor.addAttribute(SubActor.modelExportable)
        
        #cinematic charclass
        SubActor.cinematicCharclass = typedAttribute.create("cinematicCharclass", "cich", OpenMaya.MFnData.kString)
        SubActor.addAttribute(SubActor.cinematicCharclass)
        
        #export file type
        SubActor.modelFileType = enumAttribute.create("modelFileType", "modft", 0)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        for t in SubActor.fileTypesDict:
            enumAttribute.addField(t, SubActor.fileTypesDict[t])
        SubActor.addAttribute(SubActor.modelFileType)
        
        #animPreset
        SubActor.animPreset = messageAttribute.create("animPreset", "ap")
        #messageAttribute.array = True
        messageAttribute.writable = False
        messageAttribute.readable = True
        SubActor.addAttribute(SubActor.animPreset)
        
    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(False)
