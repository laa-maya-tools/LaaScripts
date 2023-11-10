# -*- coding: utf-8 -*-

import NodeID
import NodeID.PluginNodes as PluginNodes

#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class WeightedLayer(OpenMaya.MPxNode, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName    = "weightedLayer"
    nodeID      = NodeID.ActorManagerWeightedLayerID
    
    animLayer   = OpenMaya.MObject()
    weight      = OpenMaya.MObject()

    @staticmethod
    def creator():
        return WeightedLayer()

    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        
        #animLayer
        WeightedLayer.animLayer = messageAttribute.create("animLayer", "al")
        messageAttribute.writable = True
        messageAttribute.readable = False
        WeightedLayer.addAttribute(WeightedLayer.animLayer)
        
        #weight
        WeightedLayer.weight = numericAttribute.create("weight", "w", OpenMaya.MFnNumericData.kFloat, 1)
        numericAttribute.setMin(0)
        numericAttribute.setMax(1)
        numericAttribute.keyable = False
        WeightedLayer.addAttribute(WeightedLayer.weight)
        
    def postConstructor(self):
        self.setExistWithoutInConnections(False)
        self.setExistWithoutOutConnections(False)


class AnimPreset(OpenMaya.MPxNode, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName    = "animPreset"
    nodeID      = NodeID.ActorManagerAnimPresetID
    
    nameParts       = OpenMaya.MObject()
    enabled         = OpenMaya.MObject()
    active          = OpenMaya.MObject()
    path            = OpenMaya.MObject()
    rangeStart      = OpenMaya.MObject()
    rangeEnd        = OpenMaya.MObject()
    loop            = OpenMaya.MObject()
    mirror          = OpenMaya.MObject()
    pose            = OpenMaya.MObject()
    color           = OpenMaya.MObject()
    actor           = OpenMaya.MObject()
    subActor        = OpenMaya.MObject()
    animLayerList   = OpenMaya.MObject()
    category        = OpenMaya.MObject()
    
    # ~~~ OBSOLETO ~~~
    # Estos atributos ya no se usan y solo son necesarios por retrocompatibilidad.
    start           = OpenMaya.MObject()
    end             = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return AnimPreset()

    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()
        unitAttribute = OpenMaya.MFnUnitAttribute()
        
        #enabled
        AnimPreset.enabled = numericAttribute.create("enabled", "e", OpenMaya.MFnNumericData.kBoolean, True)
        AnimPreset.addAttribute(AnimPreset.enabled)
        
        #active
        AnimPreset.active = numericAttribute.create("active", "a", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = False
        AnimPreset.addAttribute(AnimPreset.active)
        
        #nameParts
        AnimPreset.nameParts = typedAttribute.create("nameParts", "np", OpenMaya.MFnData.kStringArray)
        typedAttribute.default = OpenMaya.MFnStringArrayData().create([""])
        AnimPreset.addAttribute(AnimPreset.nameParts)

        #path
        AnimPreset.path = typedAttribute.create("path", "pth", OpenMaya.MFnData.kString)
        AnimPreset.addAttribute(AnimPreset.path)
        
        #rangeStart
        AnimPreset.rangeStart = unitAttribute.create("rangeStart", "rst", OpenMaya.MFnUnitAttribute.kTime)
        unitAttribute.keyable = False
        AnimPreset.addAttribute(AnimPreset.rangeStart)
        
        #rangeEnd
        AnimPreset.rangeEnd = unitAttribute.create("rangeEnd", "rend", OpenMaya.MFnUnitAttribute.kTime)
        unitAttribute.keyable = False
        AnimPreset.addAttribute(AnimPreset.rangeEnd)
        
        #loop
        AnimPreset.loop = numericAttribute.create("loop", "lp", OpenMaya.MFnNumericData.kBoolean, False)
        AnimPreset.addAttribute(AnimPreset.loop)
        
        #mirror
        AnimPreset.mirror = numericAttribute.create("mirror", "mr", OpenMaya.MFnNumericData.kBoolean, False)
        AnimPreset.addAttribute(AnimPreset.mirror)
        
        #pose
        AnimPreset.pose = numericAttribute.create("pose", "po", OpenMaya.MFnNumericData.kBoolean, False)
        AnimPreset.addAttribute(AnimPreset.pose)
        
        #color
        AnimPreset.color = numericAttribute.createColor("color", "co")
        AnimPreset.addAttribute(AnimPreset.color)
        
        #Actor
        AnimPreset.actor = messageAttribute.create("actor", "ac")
        messageAttribute.writable = False
        messageAttribute.readable = True
        AnimPreset.addAttribute(AnimPreset.actor)
        
        #subActor
        AnimPreset.subActor = messageAttribute.create("subActor", "sac")
        messageAttribute.writable = True
        messageAttribute.readable = False
        AnimPreset.addAttribute(AnimPreset.subActor)
        
        #animLayerList
        AnimPreset.animLayerList = messageAttribute.create("animLayerList", "all")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        AnimPreset.addAttribute(AnimPreset.animLayerList)
        
        #category
        AnimPreset.category = typedAttribute.create("category", "cat", OpenMaya.MFnData.kString)
        typedAttribute.default = OpenMaya.MFnStringData().create("")
        AnimPreset.addAttribute(AnimPreset.category)
        
        # ~~~ OBSOLETO ~~~
        # - start y end son los rangos viejos, que se guardaban como int en vez de MTime. Se conservan para hacer la conversión en archivos viejos.
        
        #start
        AnimPreset.start = numericAttribute.create("start", "st", OpenMaya.MFnNumericData.kInt, 0)
        AnimPreset.addAttribute(AnimPreset.start)
        
        #end
        AnimPreset.end = numericAttribute.create("end", "end", OpenMaya.MFnNumericData.kInt, 0)
        AnimPreset.addAttribute(AnimPreset.end)
    
    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(False)
        
        # ~~~ OBSOLETO ~~~
        # Operaciones que hay que realizar para reinterpretar atributos viejos.
        import maya.cmds
        maya.cmds.evalDeferred(self.updateObsoleteAttributes)
    
    def updateObsoleteAttributes(self):
        dependencyNodeFn = OpenMaya.MFnDependencyNode(self.thisMObject())
        dgModifier = OpenMaya.MDGModifier()
        
        rangeStartPlug = dependencyNodeFn.findPlug(AnimPreset.rangeStart, False)
        rangeEndPlug = dependencyNodeFn.findPlug(AnimPreset.rangeEnd, False)
        if rangeStartPlug.asMTime() == OpenMaya.MTime(0) and rangeEndPlug.asMTime() == OpenMaya.MTime(0):
            dgModifier.newPlugValueMTime(rangeStartPlug, OpenMaya.MTime(dependencyNodeFn.findPlug(AnimPreset.start, False).asInt(), OpenMaya.MTime.uiUnit()))
            dgModifier.newPlugValueMTime(rangeEndPlug, OpenMaya.MTime(dependencyNodeFn.findPlug(AnimPreset.end, False).asInt(), OpenMaya.MTime.uiUnit()))
        
        animLayersPlug = dependencyNodeFn.findPlug(AnimPreset.animLayerList, False)
        arrayIndices = animLayersPlug.getExistingArrayAttributeIndices()
        for i in arrayIndices:
            elementPlug = animLayersPlug.elementByLogicalIndex(i)
            connectedPlug = elementPlug.source()
            if not connectedPlug.isNull and OpenMaya.MFnDependencyNode(connectedPlug.node()).typeId != WeightedLayer.nodeID:
                weightedLayerNode = dgModifier.createNode(WeightedLayer.nodeID)
                weightedLayerFn = OpenMaya.MFnDependencyNode(weightedLayerNode)
                animLayerPlug = weightedLayerFn.findPlug(WeightedLayer.animLayer, False)
                messagePlug = weightedLayerFn.findPlug("message", False)
                dgModifier.disconnect(connectedPlug, elementPlug)
                dgModifier.connect(connectedPlug, animLayerPlug)
                dgModifier.connect(messagePlug, elementPlug)
        
        dgModifier.doIt()
    