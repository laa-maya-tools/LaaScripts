import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

import sys

import NodeID

class AttribCollectionBase(object):
    attribsLongNames    = []
    attribsShortNames   = []
    attribsValues       = []
    
    def __init__(self, writable, readable, prefix="", suffix=""):
        # Variations
        self.isWritable = writable
        self.isReadable = readable
        self.__prefix = prefix
        self.__suffix = suffix
    
    def compName(self, name):
        baseVal = name
        if self.__prefix:
            baseVal = name[0].upper() + name[1:]
        return self.__prefix + baseVal + self.__suffix
    
    def setAttrib(self, idx, val):
        pass
    
    def initializer(self, parentCls):
        pass

class DrawInfo(AttribCollectionBase):
    dispTypes   = [["normal", 0], ["template", 1]   , ["reference", 2]]
    lods        = [["full", 0]  , ["boundingBox", 1]]
    
    attribsLongNames    = ["displayType", "levelOfDetail"   , "shading", "texturing"   , "playback", "enabled" , "visibility"  , "hideOnPlayback"  , "overrideRGBColors"]
    attribsShortNames   = ["dt"         , "lod"             , "sh"     , "tex"         , "pb"      , "en"      , "vis"         , "hop"             , "ovRGB"]
    attribsValues       = [dispTypes    , lods              , True     , True          , True      , True      , True          , False             , False]
    
    def __init__(self, writable, readable, prefix="", suffix=""):
        super(DrawInfo, self).__init__(writable, readable, prefix, suffix)
        
        # Attributes
        self.drawInfo            = OpenMaya.MObject()
        self.displayType         = OpenMaya.MObject()
        self.levelOfDetail       = OpenMaya.MObject()
        self.shading             = OpenMaya.MObject()
        self.texturing           = OpenMaya.MObject()
        self.playback            = OpenMaya.MObject()
        self.enabled             = OpenMaya.MObject()
        self.visibility          = OpenMaya.MObject()
        self.hideOnPlayback      = OpenMaya.MObject()
        self.overrideRGBColors   = OpenMaya.MObject()
        self.color               = OpenMaya.MObject()
        self.overrideColorRGB    = OpenMaya.MObject()
    
    def setAttrib(self, idx, val):
        if idx == 0:
            self.displayType = val
        elif idx == 1:
            self.levelOfDetail = val
        elif idx == 2:
            self.shading = val
        elif idx == 3:
            self.texturing = val
        elif idx == 4:
            self.playback = val
        elif idx == 5:
            self.enabled = val
        elif idx == 6:
            self.visibility = val
        elif idx == 7:
            self.hideOnPlayback = val
        elif idx == 8:
            self.overrideRGBColors = val
    
    def initializer(self, parentCls):
        compoundAttribute   = OpenMaya.MFnCompoundAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        enumAtribute        = OpenMaya.MFnEnumAttribute()
        
        #Create compound attribute
        self.drawInfo = compoundAttribute.create(self.compName("drawInfo"), self.compName("di"))
        compoundAttribute.setDisconnectBehavior(OpenMaya.MFnAttribute.kReset)
        compoundAttribute.setCached(False)
        
        #Create Enum Attributes
        for i in range(len(self.attribsLongNames)):
            # Enums
            if i <= 1:
                attr = enumAtribute.create(self.compName(DrawInfo.attribsLongNames[i]), self.compName(DrawInfo.attribsShortNames[i]))
                enumAtribute.setDisconnectBehavior(OpenMaya.MFnAttribute.kReset)
                
                for val in DrawInfo.attribsValues[i]:
                    enumAtribute.addField(val[0], val[1])
            # Booleans
            else:
                attr = numericAttribute.create(self.compName(DrawInfo.attribsLongNames[i]), self.compName(DrawInfo.attribsShortNames[i]), OpenMaya.MFnNumericData.kBoolean, DrawInfo.attribsValues[i])
                numericAttribute.setDisconnectBehavior(OpenMaya.MFnAttribute.kReset)
            
            self.setAttrib(i, attr)
            # Add to Compound
            compoundAttribute.addChild(attr)
        
        #Create Byte Attribute
        self.color = numericAttribute.create(self.compName("color"), self.compName("c"), OpenMaya.MFnNumericData.kInt, 0)
        numericAttribute.setMin(0)
        numericAttribute.setMax(31)
        compoundAttribute.addChild(self.color)
        
        #Create Float3 Attribute
        self.overrideColorRGB = numericAttribute.create(self.compName("overrideColorRGB"), self.compName("RGB"), OpenMaya.MFnNumericData.k3Float)
        numericAttribute.setUsedAsColor(True)
        compoundAttribute.addChild(self.overrideColorRGB)
        
        #Add Compound Attr to node
        compoundAttribute.setWritable(self.isWritable)
        compoundAttribute.setReadable(self.isReadable)
        parentCls.addAttribute(self.drawInfo)

class InheritInfo(AttribCollectionBase):
    attribsLongNames    = ["spreadDisplayType"  , "spreadLevelOfDetail" , "spreadColor" , "hiddenInView"]
    attribsShortNames   = ["sdt"                , "slod"                , "sc"          , "hiv"]
    attribsValues       = [False                , False                 , False         , False]
    
    def __init__(self, writable, readable, prefix="", suffix=""):
        super(InheritInfo, self).__init__(writable, readable, prefix, suffix)
        
        # Attributes
        self.spreadInfo             = OpenMaya.MObject()
        self.inheritDisplayType     = OpenMaya.MObject()
        self.inheritLevelOfDetail   = OpenMaya.MObject()
        self.inheritColor           = OpenMaya.MObject()
        self.hiddenInView           = OpenMaya.MObject()
                
    def setAttrib(self, idx, val):
        if idx == 0:
            self.inheritDisplayType = val
        elif idx == 1:
            self.inheritLevelOfDetail = val
        elif idx == 2:
            self.inheritColor = val
        elif idx == 3:
            self.hiddenInView = val
    
    def initializer(self, parentCls):
        compoundAttribute   = OpenMaya.MFnCompoundAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        
        #Create compound attribute
        self.spreadInfo = compoundAttribute.create(self.compName("spreadInfo"), self.compName("ii"))
        
        for i in range(len(self.attribsLongNames)):
            attr = numericAttribute.create(self.compName(self.attribsLongNames[i]), self.compName(self.attribsShortNames[i]), OpenMaya.MFnNumericData.kBoolean, InheritInfo.attribsValues[i])
            numericAttribute.setDisconnectBehavior(OpenMaya.MFnAttribute.kReset)
            
            self.setAttrib(i, attr)
            # Add to Compound
            compoundAttribute.addChild(attr)
        
        # Fricking Bug of Maya, is not able to paint a compound attribute of just booleans in the Attribute Editor. Adding another type, renders ok. So stupid, yes.
        auxAttr = numericAttribute.create(self.compName("mayaBugaso"), self.compName("mbug"), OpenMaya.MFnNumericData.kByte, 0)
        numericAttribute.setHidden(True)  
        numericAttribute.setConnectable(False)  
        compoundAttribute.addChild(auxAttr)
        
        #Add Compound Attr to node
        compoundAttribute.setWritable(self.isWritable)
        compoundAttribute.setReadable(self.isReadable)
        parentCls.addAttribute(self.spreadInfo)

# ********************************
# Basic Inheritable Draw Info Node
# ********************************
class InheritableDrawInfo(OpenMayaMPx.MPxNode):
    # Plugin data
    nodeName = "InheritableDrawInfo"
    
    #Attributes
    outDrawInfo     = DrawInfo(False, True, prefix="out")
    drawInfo        = DrawInfo(True, False)
    parentDrawInfo  = DrawInfo(True, False, prefix="parent")
    
    outSpreadInfo     = InheritInfo(False, True, prefix="out")
    spreadInfo        = InheritInfo(True, False)
    parentSpreadInfo  = InheritInfo(True, False, prefix="parent")
    
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(InheritableDrawInfo())
    
    @staticmethod
    def initializer():
        InheritableDrawInfo.outSpreadInfo.initializer(InheritableDrawInfo)
        InheritableDrawInfo.spreadInfo.initializer(InheritableDrawInfo)
        InheritableDrawInfo.parentSpreadInfo.initializer(InheritableDrawInfo)
        
        InheritableDrawInfo.outDrawInfo.initializer(InheritableDrawInfo)
        InheritableDrawInfo.drawInfo.initializer(InheritableDrawInfo)
        InheritableDrawInfo.parentDrawInfo.initializer(InheritableDrawInfo)
        
        # Set Attribute Affects: 'Self' DrawInfo => 'OUT' DrawInfo
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.displayType       , InheritableDrawInfo.outDrawInfo.displayType)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.levelOfDetail     , InheritableDrawInfo.outDrawInfo.levelOfDetail)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.shading           , InheritableDrawInfo.outDrawInfo.shading)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.texturing         , InheritableDrawInfo.outDrawInfo.texturing)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.playback          , InheritableDrawInfo.outDrawInfo.playback)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.enabled           , InheritableDrawInfo.outDrawInfo.enabled)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.visibility        , InheritableDrawInfo.outDrawInfo.visibility)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.hideOnPlayback    , InheritableDrawInfo.outDrawInfo.hideOnPlayback)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.overrideRGBColors , InheritableDrawInfo.outDrawInfo.overrideRGBColors)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.color             , InheritableDrawInfo.outDrawInfo.color)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.drawInfo.overrideColorRGB  , InheritableDrawInfo.outDrawInfo.overrideColorRGB)
        # Set Attribute Affects: 'IN' DrawInfo => 'OUT' DrawInfo
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.displayType       , InheritableDrawInfo.outDrawInfo.displayType)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.levelOfDetail     , InheritableDrawInfo.outDrawInfo.levelOfDetail)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.shading           , InheritableDrawInfo.outDrawInfo.shading)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.texturing         , InheritableDrawInfo.outDrawInfo.texturing)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.playback          , InheritableDrawInfo.outDrawInfo.playback)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.enabled           , InheritableDrawInfo.outDrawInfo.enabled)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.visibility        , InheritableDrawInfo.outDrawInfo.visibility)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.hideOnPlayback    , InheritableDrawInfo.outDrawInfo.hideOnPlayback)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.overrideRGBColors , InheritableDrawInfo.outDrawInfo.overrideRGBColors)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.color             , InheritableDrawInfo.outDrawInfo.color)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentDrawInfo.overrideColorRGB  , InheritableDrawInfo.outDrawInfo.overrideColorRGB)
        # Set Attribute Affects: 'Self' InherintInfo => 'OUT' InherintInfo
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.spreadInfo.inheritDisplayType     , InheritableDrawInfo.outSpreadInfo.inheritDisplayType)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.spreadInfo.inheritLevelOfDetail   , InheritableDrawInfo.outSpreadInfo.inheritLevelOfDetail)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.spreadInfo.inheritColor           , InheritableDrawInfo.outSpreadInfo.inheritColor)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.spreadInfo.hiddenInView           , InheritableDrawInfo.outSpreadInfo.hiddenInView)
        # Set Attribute Affects: 'IN' InherintInfo => 'OUT' InherintInfo
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritDisplayType     , InheritableDrawInfo.outSpreadInfo.inheritDisplayType)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritLevelOfDetail   , InheritableDrawInfo.outSpreadInfo.inheritLevelOfDetail)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritColor           , InheritableDrawInfo.outSpreadInfo.inheritColor)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.hiddenInView           , InheritableDrawInfo.outSpreadInfo.hiddenInView)
        # Set Attribute Affects: 'IN' InherintInfo => 'OUT' DrawInfo
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritDisplayType     , InheritableDrawInfo.outDrawInfo.displayType)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritLevelOfDetail   , InheritableDrawInfo.outDrawInfo.levelOfDetail)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritColor           , InheritableDrawInfo.outDrawInfo.overrideRGBColors)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritColor           , InheritableDrawInfo.outDrawInfo.color)
        InheritableDrawInfo.attributeAffects(InheritableDrawInfo.parentSpreadInfo.inheritColor           , InheritableDrawInfo.outDrawInfo.overrideColorRGB)
    
    def postConstructor(self):
        self.selfDict = {
            self.outDrawInfo.compName("displayType")         : self.drawInfo.displayType,
            self.outDrawInfo.compName("levelOfDetail")       : self.drawInfo.levelOfDetail,
            self.outDrawInfo.compName("shading")             : self.drawInfo.shading,
            self.outDrawInfo.compName("texturing")           : self.drawInfo.texturing,
            self.outDrawInfo.compName("playback")            : self.drawInfo.playback,
            self.outDrawInfo.compName("enabled")             : self.drawInfo.enabled,
            self.outDrawInfo.compName("visibility")          : self.drawInfo.visibility,
            self.outDrawInfo.compName("hideOnPlayback")      : self.drawInfo.hideOnPlayback,
            self.outDrawInfo.compName("overrideRGBColors")   : self.drawInfo.overrideRGBColors,
            self.outDrawInfo.compName("color")               : self.drawInfo.color,
            self.outDrawInfo.compName("overrideColorRGB")    : self.drawInfo.overrideColorRGB,
            self.outSpreadInfo.compName("spreadDisplayType")      : self.spreadInfo.inheritDisplayType,
            self.outSpreadInfo.compName("spreadLevelOfDetail")    : self.spreadInfo.inheritLevelOfDetail,
            self.outSpreadInfo.compName("spreadColor")            : self.spreadInfo.inheritColor,
            self.outSpreadInfo.compName("hiddenInView")           : self.spreadInfo.hiddenInView
        }
        
        self.parentDict = {
            self.outDrawInfo.compName("displayType")         : self.parentDrawInfo.displayType,
            self.outDrawInfo.compName("levelOfDetail")       : self.parentDrawInfo.levelOfDetail,
            self.outDrawInfo.compName("shading")             : self.parentDrawInfo.shading,
            self.outDrawInfo.compName("texturing")           : self.parentDrawInfo.texturing,
            self.outDrawInfo.compName("playback")            : self.parentDrawInfo.playback,
            self.outDrawInfo.compName("enabled")             : self.parentDrawInfo.enabled,
            self.outDrawInfo.compName("visibility")          : self.parentDrawInfo.visibility,
            self.outDrawInfo.compName("hideOnPlayback")      : self.parentDrawInfo.hideOnPlayback,
            self.outDrawInfo.compName("overrideRGBColors")   : self.parentDrawInfo.overrideRGBColors,
            self.outDrawInfo.compName("color")               : self.parentDrawInfo.color,
            self.outDrawInfo.compName("overrideColorRGB")    : self.parentDrawInfo.overrideColorRGB,
            self.outSpreadInfo.compName("spreadDisplayType")      : self.parentSpreadInfo.inheritDisplayType,
            self.outSpreadInfo.compName("spreadLevelOfDetail")    : self.parentSpreadInfo.inheritLevelOfDetail,
            self.outSpreadInfo.compName("spreadColor")            : self.parentSpreadInfo.inheritColor,
            self.outSpreadInfo.compName("hiddenInView")           : self.parentSpreadInfo.hiddenInView
        }
        
        self.inheritParentDict = {
            self.outDrawInfo.compName("displayType")         : self.parentSpreadInfo.inheritDisplayType,
            self.outDrawInfo.compName("levelOfDetail")       : self.parentSpreadInfo.inheritLevelOfDetail,
            self.outDrawInfo.compName("shading")             : None,
            self.outDrawInfo.compName("texturing")           : None,
            self.outDrawInfo.compName("playback")            : None,
            self.outDrawInfo.compName("enabled")             : None,
            self.outDrawInfo.compName("visibility")          : None,
            self.outDrawInfo.compName("hideOnPlayback")      : None,
            self.outDrawInfo.compName("overrideRGBColors")   : self.parentSpreadInfo.inheritColor,
            self.outDrawInfo.compName("color")               : self.parentSpreadInfo.inheritColor,
            self.outDrawInfo.compName("overrideColorRGB")    : self.parentSpreadInfo.inheritColor,
            self.outSpreadInfo.compName("spreadDisplayType")      : None,
            self.outSpreadInfo.compName("spreadLevelOfDetail")    : None,
            self.outSpreadInfo.compName("spreadColor")            : None,
            self.outSpreadInfo.compName("hiddenInView")           : None
        }
        
        self.boolOperatorDict = {
            self.outDrawInfo.compName("shading")             : "&",
            self.outDrawInfo.compName("texturing")           : "&",
            self.outDrawInfo.compName("playback")            : "&",
            self.outDrawInfo.compName("enabled")             : "&",
            self.outDrawInfo.compName("visibility")          : "&",
            self.outDrawInfo.compName("hideOnPlayback")      : "|",
            self.outDrawInfo.compName("overrideRGBColors")   : "&",
            self.outSpreadInfo.compName("spreadDisplayType")      : "|",
            self.outSpreadInfo.compName("spreadLevelOfDetail")    : "|",
            self.outSpreadInfo.compName("spreadColor")            : "|",
            self.outSpreadInfo.compName("hiddenInView")           : "|"
        }
    
    def computePlug(self, plug, data):
        plugName = plug.name().split(".")[1]        
        selfValPlug     = None
        parentValPlug   = None
        inheritParentPlug = None
        
        try:
            selfValPlug     = self.selfDict[plugName]
            parentValPlug   = self.parentDict[plugName]
            inheritParentPlug   = self.inheritParentDict[plugName]
        except Exception:
            #print("Warning: {}".format(plug.name()))
            return
        
        if (selfValPlug and parentValPlug):
            if (not inheritParentPlug):
                # These are the booleans
                selfVal     = data.inputValue(selfValPlug).asBool()
                parentVal   = data.inputValue(parentValPlug).asBool()
                boolOperator = self.boolOperatorDict[plugName]
                if boolOperator == "&":
                    resultVal = selfVal & parentVal
                else:
                    resultVal = selfVal | parentVal
                
                data.outputValue(plug).setBool(resultVal)
            else:
                inheritVal = data.inputValue(inheritParentPlug).asBool()
                valPlug = selfValPlug
                if (inheritVal):
                    valPlug = parentValPlug
                if (plug.isCompound()):
                    values = data.inputValue(valPlug).asFloat3()
                    data.outputValue(plug).set3Float(values[0], values[1], values[2])
                else:
                    data.outputValue(plug).setInt(data.inputValue(valPlug).asInt())
            
            data.setClean(plug)
    
    def compute(self, plug, data):
        #print(plug.partialName(False, False, False, False, True, True))        
        if (plug==self.outDrawInfo.drawInfo
            or plug==self.outSpreadInfo.spreadInfo):
            
            for i in range(plug.numChildren()):
                child = plug.child(i)
                if (not data.isClean(child)):
                    self.computePlug(child, data)
            data.setClean(plug)
        elif (plug==self.outDrawInfo.displayType
            or plug==self.outDrawInfo.levelOfDetail
            or plug==self.outDrawInfo.shading
            or plug==self.outDrawInfo.texturing
            or plug==self.outDrawInfo.playback
            or plug==self.outDrawInfo.enabled
            or plug==self.outDrawInfo.visibility
            or plug==self.outDrawInfo.hideOnPlayback
            or plug==self.outDrawInfo.overrideRGBColors
            or plug==self.outDrawInfo.color
            or plug==self.outDrawInfo.overrideColorRGB
            or plug==self.outSpreadInfo.inheritDisplayType
            or plug==self.outSpreadInfo.inheritLevelOfDetail
            or plug==self.outSpreadInfo.inheritColor
            or plug==self.outSpreadInfo.hiddenInView):
            
            self.computePlug(plug, data)
        else:
            OpenMayaMPx.MPxNode.compute(self, plug, data)

# *******************************************************
# OrganiLayer Node, derived from InheritableDrawInfo Node
# *******************************************************
class OrganiLayer(InheritableDrawInfo):
    # Plugin data
    nodeName = "OrganiLayer"
    
    # Attributes
    name        = OpenMaya.MObject()
    parentLayer = OpenMaya.MObject()
    childLayers = OpenMaya.MObject()
    childItems  = OpenMaya.MObject()
    set         = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(OrganiLayer())
    
    @staticmethod
    def initializer():
        # We must inherit the superclass attributes with "inheritAttributesFrom()" instead of calling the superclass "initializer()" method,
        # as calling the "super" "initializer()" would make Maya to re-create the attributes when we use "registerNode()" and ONLY,
        # and JUST ONLY, the last derived node plugin will work correctly when its "Compute()" method is called.
        OrganiLayer.inheritAttributesFrom("InheritableDrawInfo")
        
        messageAttr = OpenMaya.MFnMessageAttribute()
        typedAttr   = OpenMaya.MFnTypedAttribute()
        
        OrganiLayer.name = typedAttr.create("name", "nm", OpenMaya.MFnData.kString)
        typedAttr.setReadable(False)
        OrganiLayer.addAttribute(OrganiLayer.name)
        
        OrganiLayer.parentLayer = messageAttr.create("parentLayer", "ply")
        messageAttr.setReadable(False)
        OrganiLayer.addAttribute(OrganiLayer.parentLayer)
        
        OrganiLayer.childLayers = messageAttr.create("childLayers", "cly")
        messageAttr.setWritable(False)
        OrganiLayer.addAttribute(OrganiLayer.childLayers)
        
        OrganiLayer.childItems = messageAttr.create("childItems", "chi")
        messageAttr.setWritable(False)
        OrganiLayer.addAttribute(OrganiLayer.childItems)
        
        OrganiLayer.set = messageAttr.create("set", "st")
        messageAttr.setReadable(False)
        OrganiLayer.addAttribute(OrganiLayer.set)
    
    def postConstructor(self):
        super(OrganiLayer, self).postConstructor()
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)
    
    def compute(self, plug, data):
        # If attributes are inherithed with "inheritAttributesFrom()" in this class 's initializer, we 
        # can safely call superclass's compute method here.
        super(OrganiLayer, self).compute(plug, data)

# *******************************************************
# OrganiItem Node, derived from InheritableDrawInfo Node
# *******************************************************
class OrganiItem(InheritableDrawInfo):
    # Plugin data
    nodeName = "OrganiItem"
    
    # Attributes
    parentLayer = OpenMaya.MObject()
    dagNode     = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(OrganiItem())
    
    @staticmethod
    def initializer():
        OrganiLayer.inheritAttributesFrom("InheritableDrawInfo")
        
        messageAttr = OpenMaya.MFnMessageAttribute()
        
        OrganiItem.parentLayer = messageAttr.create("parentLayer", "pl")
        messageAttr.setReadable(False)
        OrganiItem.addAttribute(OrganiItem.parentLayer)
        
        OrganiItem.dagNode = messageAttr.create("dagNode", "dagn")
        messageAttr.setReadable(False)
        OrganiItem.addAttribute(OrganiItem.dagNode)
    
    def postConstructor(self):
        super(OrganiItem, self).postConstructor()
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)
        
    def compute(self, plug, data):
        super(OrganiItem, self).compute(plug, data)

# *******************************************************
# OrganiSet Node
# *******************************************************
class OrganiSet(OpenMayaMPx.MPxNode):
    # Plugin data
    nodeName = "OrganiSet"
    
    # Attributes
    name            = OpenMaya.MObject()
    componentLayers = OpenMaya.MObject()
    isActive        = OpenMaya.MObject()
    activeLayer     = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(OrganiSet())
    
    @staticmethod
    def initializer():
        messageAttr         = OpenMaya.MFnMessageAttribute()
        typedAttr           = OpenMaya.MFnTypedAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        
        OrganiSet.name = typedAttr.create("name", "nm", OpenMaya.MFnData.kString)
        typedAttr.setReadable(False)
        OrganiSet.addAttribute(OrganiSet.name)
        
        OrganiSet.componentLayers = messageAttr.create("componentLayers", "ly")
        messageAttr.setWritable(False)
        OrganiSet.addAttribute(OrganiSet.componentLayers)
        
        OrganiSet.isActive = numericAttribute.create("isActive", "ac", OpenMaya.MFnNumericData.kBoolean, False)
        typedAttr.setReadable(False)
        OrganiSet.addAttribute(OrganiSet.isActive)
        
        OrganiSet.activeLayer = messageAttr.create("activeLayer", "acly")
        messageAttr.setReadable(False)
        OrganiSet.addAttribute(OrganiSet.activeLayer)
    
    def postConstructor(self):
        super(OrganiSet, self).postConstructor()
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)

# ***************************************************************************************************************************
# ***************************************************************************************************************************
# Register and de-register
# ***************************************************************************************************************************
# ***************************************************************************************************************************

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    
    try:
        mplugin.registerNode(InheritableDrawInfo.nodeName, NodeID.InheritableDrawInfoID, InheritableDrawInfo.creator, InheritableDrawInfo.initializer)
    except:
        sys.stderr.write("Failed to register node: " + InheritableDrawInfo.nodeName)
        raise
    
    try:
        mplugin.registerNode(OrganiLayer.nodeName, NodeID.OrganiLayerID, OrganiLayer.creator, OrganiLayer.initializer)
    except:
        sys.stderr.write("Failed to register node: " + OrganiLayer.nodeName)
        raise
    
    try:
        mplugin.registerNode(OrganiItem.nodeName, NodeID.OrganiItemID, OrganiItem.creator, OrganiItem.initializer)
    except:
        sys.stderr.write("Failed to register node: " + OrganiItem.nodeName)
        raise
    
    try:
        mplugin.registerNode(OrganiSet.nodeName, NodeID.OrganiSetID, OrganiSet.creator, OrganiSet.initializer)
    except:
        sys.stderr.write("Failed to register node: " + OrganiSet.nodeName)
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    
    try:
        mplugin.deregisterNode(NodeID.InheritableDrawInfoID)
    except:
        sys.stderr.write("Failed to unregister node: " + InheritableDrawInfo.nodeName)
        raise
    
    try:
        mplugin.deregisterNode(NodeID.OrganiLayerID)
    except:
        sys.stderr.write("Failed to unregister node: " + OrganiLayer.nodeName)
        raise
    
    try:
        mplugin.deregisterNode(NodeID.OrganiItemID)
    except:
        sys.stderr.write("Failed to unregister node: " + OrganiItem.nodeName)
        raise
    
    try:
        mplugin.deregisterNode(NodeID.OrganiSetID)
    except:
        sys.stderr.write("Failed to unregister node: " + OrganiSet.nodeName)
        raise