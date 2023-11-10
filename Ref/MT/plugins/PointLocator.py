import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaRender as OpenMayaRender
#import maya.api.OpenMayaAnim as OpenMayaAnim

import maya.cmds as cmds

import Utils.OpenMaya as OpenMayaUtils

import sys
import NodeID

## Viewport 2.0 override implementation

def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass

class PointLocator(OpenMayaUI.MPxLocatorNode):
    # To be recognized as something that can draw geometry for a renderable object, this string is required.
    # https://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=__files_GUID_A1BA2FCE_DACB_4C61_8340_29B6C6D168C4_htm
    drawDbClassification = "drawdb/geometry/PointLocator"
    nodeTypeId = NodeID.PointLocatorID
    nodeTypeName = "PointLocator"
    
    size    = OpenMaya.MObject()
    centerPoint  = OpenMaya.MObject()
    
    axes    = OpenMaya.MObject()
    xAxis   = OpenMaya.MObject()
    yAxis   = OpenMaya.MObject()
    zAxis   = OpenMaya.MObject()
    axesWidth    = OpenMaya.MObject()
    axesTricolor = OpenMaya.MObject()
    axesCharSize = OpenMaya.MObject()
    
    cube    = OpenMaya.MObject()
    sphere  = OpenMaya.MObject()
    cross   = OpenMaya.MObject()
    plane   = OpenMaya.MObject()
    
    planeScaleU = OpenMaya.MObject()
    planeScaleV = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return PointLocator()

    @staticmethod
    def initialize():
        numericAttribute = OpenMaya.MFnNumericAttribute()
        enumAttribute = OpenMaya.MFnEnumAttribute()
        
        separator = enumAttribute.create("locator_properties", "sep1", 0)
        enumAttribute.keyable = True
        enumAttribute.addField('--------------', 0)
        PointLocator.addAttribute(separator)
        
        PointLocator.size = numericAttribute.create("size", "sz", OpenMaya.MFnNumericData.kFloat, 50.0)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        numericAttribute.setMin(0.01)
        PointLocator.addAttribute(PointLocator.size)
        
        PointLocator.centerPoint = numericAttribute.createPoint("centerPoint", "cp")
        numericAttribute.storable = True
        numericAttribute.keyable = True
        numericAttribute.readable = True
        numericAttribute.writable = True
        PointLocator.addAttribute(PointLocator.centerPoint)
        
        PointLocator.axes = numericAttribute.create("axes", "ax", OpenMaya.MFnNumericData.kBoolean, False)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.axes)
        
        PointLocator.cube = numericAttribute.create("cube", "cu", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.cube)
        
        PointLocator.sphere = numericAttribute.create("sphere", "sp", OpenMaya.MFnNumericData.kBoolean, False)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.sphere)
        
        PointLocator.cross = numericAttribute.create("cross", "cr", OpenMaya.MFnNumericData.kBoolean, False)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.cross)
        
        PointLocator.plane = numericAttribute.create("plane", "pl", OpenMaya.MFnNumericData.kBoolean, False)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.plane)
        
        separator = enumAttribute.create("axes_display", "sep2", 0)
        enumAttribute.keyable = True
        enumAttribute.addField('--------------', 0)
        PointLocator.addAttribute(separator)
        
        PointLocator.axesWidth = numericAttribute.create("axes_width", "aw", OpenMaya.MFnNumericData.kInt, 2)
        numericAttribute.setMin(1)
        numericAttribute.setMax(10)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.axesWidth)
        PointLocator.xAxis = numericAttribute.create("x_axis", "xAx", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.xAxis)
        PointLocator.yAxis = numericAttribute.create("y_axis", "yAx", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.yAxis)
        PointLocator.zAxis = numericAttribute.create("z_axis", "zAx", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.zAxis)
        PointLocator.axesTricolor = numericAttribute.create("tricolor", "tri", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.axesTricolor)
        PointLocator.axesCharSize = numericAttribute.create("char_size", "chs", OpenMaya.MFnNumericData.kInt, 10)
        numericAttribute.setMin(1)
        numericAttribute.setMax(25)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        PointLocator.addAttribute(PointLocator.axesCharSize)
        
        separator = enumAttribute.create("plane_display", "sep3", 0)
        enumAttribute.keyable = True
        enumAttribute.addField('--------------', 0)
        PointLocator.addAttribute(separator)
        
        PointLocator.planeScaleU = numericAttribute.create("plane_scale_U", "plsclu", OpenMaya.MFnNumericData.kFloat, 1.0)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        numericAttribute.setMin(0.0)
        numericAttribute.setMax(20)
        PointLocator.addAttribute(PointLocator.planeScaleU)
        PointLocator.planeScaleV = numericAttribute.create("plane_scale_V", "plsclv", OpenMaya.MFnNumericData.kFloat, 1.0)
        numericAttribute.storable = True
        numericAttribute.keyable = True
        numericAttribute.setMin(0.0)
        numericAttribute.setMax(20)
        PointLocator.addAttribute(PointLocator.planeScaleV)

    def __init__(self):
        OpenMayaUI.MPxLocatorNode.__init__(self)

    def compute(self, plug, data):
        return None

    def draw(self, view, path, style, status):
        return None

    # NOTE: Los métodos de la bounding Box en MPxLocatorNode se usan para la selección y para encuadrar al pulsar la tecla F
    def isBounded(self):
        return True
 
    def boundingBox(self):
        pHelper = OpenMaya.MFnDependencyNode(self.thisMObject())
        
        centerPlug = pHelper.findPlug(PointLocator.centerPoint, False)
        
        center = OpenMaya.MPoint(centerPlug.child(0).asFloat(), centerPlug.child(1).asFloat(), centerPlug.child(2).asFloat())
        size = pHelper.findPlug(PointLocator.size, False).asFloat()
        
        p1 = center + 0.5 * size * OpenMaya.MVector.kOneVector
        p2 = center - 0.5 * size * OpenMaya.MVector.kOneVector
        
        box = OpenMaya.MBoundingBox(p1, p2)
        
        return box


class PointLocatorData(OpenMaya.MUserData):
    
    def __init__(self):
        OpenMaya.MUserData.__init__(self, False) ## don't delete after draw
        self.size = 50.0
        self.center = OpenMaya.MVector.kZeroVector
        
        self.axes = False
        self.xAxis = True
        self.yAxis = True
        self.zAxis = True
        self.axesTricolor = True
        self.axesWidth = 2
        self.axesCharSize = 10
        
        self.cube = True
        self.sphere = False
        self.cross = False
        self.plane = False
        
        self.planeScaleU = 1.0
        self.planeScaleV = 1.0
        
        self.color = OpenMaya.MColor()


class PointLocatorDrawOverride(OpenMayaRender.MPxDrawOverride):
    
    RColor = OpenMaya.MColor((1.0, 0.0, 0.0))
    GColor = OpenMaya.MColor((0.0, 1.0, 0.0))
    BColor = OpenMaya.MColor((0.0, 0.0, 1.0))
    
    @staticmethod
    def creator(obj):
        return PointLocatorDrawOverride(obj)

    @staticmethod
    def draw(context, data):
        return

    def __init__(self, obj):
        OpenMayaRender.MPxDrawOverride.__init__(self, obj, PointLocatorDrawOverride.draw)
        self.tipPoint = None

    def supportedDrawAPIs(self):
        ## this plugin supports both GL and DX
        return OpenMayaRender.MRenderer.kOpenGL | OpenMayaRender.MRenderer.kDirectX11 | OpenMayaRender.MRenderer.kOpenGLCoreProfile

    def prepareForDraw(self, objPath, cameraPath, frameContext, oldData):
        ## Retrieve data cache (create if does not exist)
        data = oldData
        if not isinstance(data, PointLocatorData):
            data = PointLocatorData()

        pHelper = OpenMaya.MFnDependencyNode(objPath.node())
        centerPlug = pHelper.findPlug(PointLocator.centerPoint, False)
        
        data.center = OpenMaya.MPoint(centerPlug.child(0).asFloat(), centerPlug.child(1).asFloat(), centerPlug.child(2).asFloat())
        data.size = pHelper.findPlug(PointLocator.size, False).asFloat()
        
        data.axes = pHelper.findPlug(PointLocator.axes, False).asBool()
        data.xAxis = pHelper.findPlug(PointLocator.xAxis, False).asBool()
        data.yAxis = pHelper.findPlug(PointLocator.yAxis, False).asBool()
        data.zAxis = pHelper.findPlug(PointLocator.zAxis, False).asBool()
        data.axesWidth = pHelper.findPlug(PointLocator.axesWidth, False).asInt()
        data.axesTricolor = pHelper.findPlug(PointLocator.axesTricolor, False).asBool()
        data.axesCharSize = pHelper.findPlug(PointLocator.axesCharSize, False).asInt()
        
        data.cube = pHelper.findPlug(PointLocator.cube, False).asBool()
        data.sphere = pHelper.findPlug(PointLocator.sphere, False).asBool()
        data.cross = pHelper.findPlug(PointLocator.cross, False).asBool()
        data.plane = pHelper.findPlug(PointLocator.plane, False).asBool()
        
        data.planeScaleU = pHelper.findPlug(PointLocator.planeScaleU, False).asFloat()
        data.planeScaleV = pHelper.findPlug(PointLocator.planeScaleV, False).asFloat()
        
        displayStatus = OpenMayaRender.MGeometryUtilities.displayStatus(objPath)
        if displayStatus == OpenMayaRender.MGeometryUtilities.kDormant and not OpenMayaUtils.getDisplayOverrideColorState(objPath):
            data.color = OpenMayaUI.M3dView.active3dView().colorAtIndex(cmds.displayColor("locator", q=True, dormant=True) - 1)
        else:
            data.color = OpenMayaRender.MGeometryUtilities.wireframeColor(objPath)
            
        return data

    def hasUIDrawables(self):
        return True

    # Viewport 2.0 addUIDrawables(Draw) Function
    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        locatordata = data
        if not isinstance(locatordata, PointLocatorData):
            return
        
        # ---------- COMPUTE DYNAMIC PARAMS ----------
        hSize = locatordata.size / 2
        axisTip = hSize * 1.3
        axisArrowSide = hSize * 0.2
        charOffset = axisTip + 5
        xColor = PointLocatorDrawOverride.RColor
        yColor = PointLocatorDrawOverride.GColor
        zColor = PointLocatorDrawOverride.BColor
        
        # -------- BEGIN DRAWING ----------
        drawManager.beginDrawable()

        drawManager.setColor(data.color)
        
        if locatordata.cube:
            drawManager.box(data.center, OpenMaya.MVector.kYaxisVector, OpenMaya.MVector.kXaxisVector, hSize, hSize, hSize)
            
        if locatordata.sphere:
            drawManager.sphere(data.center, hSize, 8, 4)
            
        if locatordata.cross:
            drawManager.line(data.center + OpenMaya.MVector(-hSize, 0.0, 0.0), data.center + OpenMaya.MVector(hSize, 0.0, 0.0))
            drawManager.line(data.center + OpenMaya.MVector(0.0, -hSize, 0.0), data.center + OpenMaya.MVector(0.0, hSize, 0.0))
            drawManager.line(data.center + OpenMaya.MVector(0.0, 0.0, -hSize), data.center + OpenMaya.MVector(0.0, 0.0, hSize))
        
        if locatordata.plane:
            #planePoints = OpenMaya.MPointArray([OpenMaya.MPoint(-hSize, 0.0, hSize), OpenMaya.MPoint(hSize, 0.0, hSize), OpenMaya.MPoint(hSize, 0.0, -hSize), OpenMaya.MPoint(-hSize, 0.0, -hSize)])
            #drawManager.mesh(drawManager.kPoints, planePoints)
            drawManager.rect(data.center, OpenMaya.MVector.kYaxisVector, OpenMaya.MVector(0, 0, 1), hSize * locatordata.planeScaleU, hSize * locatordata.planeScaleV, True)
            
        if locatordata.axes:
            drawManager.setLineWidth(locatordata.axesWidth)
            drawManager.setFontSize(locatordata.axesCharSize)
            
            # XArrow
            if (locatordata.xAxis):
                self.tipPoint = data.center + OpenMaya.MVector(axisTip, 0.0, 0.0)
                drawManager.setColor(xColor)
                drawManager.line(data.center, self.tipPoint)
                drawManager.lineStrip(OpenMaya.MPointArray([data.center + OpenMaya.MVector(hSize, -axisArrowSide, 0.0), self.tipPoint, data.center + OpenMaya.MVector(hSize, axisArrowSide, 0.0)]), False)
                drawManager.text(data.center + OpenMaya.MVector(charOffset, 0, 0), "X", OpenMayaRender.MUIDrawManager.kCenter )
            
            #YArrow
            if (locatordata.yAxis):
                self.tipPoint = data.center + OpenMaya.MVector(0.0, axisTip, 0.0)
                drawManager.setColor(yColor)
                drawManager.line(data.center, self.tipPoint)
                drawManager.lineStrip(OpenMaya.MPointArray([data.center + OpenMaya.MVector(-axisArrowSide, hSize, 0.0), self.tipPoint, data.center + OpenMaya.MVector(axisArrowSide, hSize, 0.0)]), False)
                drawManager.text(data.center + OpenMaya.MVector(0, charOffset, 0), "Y", OpenMayaRender.MUIDrawManager.kCenter )
            
            #ZArrow
            if (locatordata.zAxis):
                self.tipPoint = data.center + OpenMaya.MVector(0.0, 0.0, axisTip)
                drawManager.setColor(zColor)
                drawManager.line(data.center, self.tipPoint)
                drawManager.lineStrip(OpenMaya.MPointArray([data.center + OpenMaya.MVector(0.0, -axisArrowSide, hSize), self.tipPoint, data.center + OpenMaya.MVector(0.0, axisArrowSide, hSize)]), False)
                drawManager.text(data.center + OpenMaya.MVector(0, 0, charOffset), "Z", OpenMayaRender.MUIDrawManager.kCenter )

        drawManager.endDrawable()
    
    # NOTE: Los métodos de la bounding Box en MPxDrawingOverride se usan para el frustrum culling
    def isBounded(self, objPath, cameraPath):
        return True
 
    def boundingBox(self, objPath, cameraPath):
        pHelper = OpenMaya.MFnDagNode(objPath)
        
        centerPlug = pHelper.findPlug(PointLocator.centerPoint, False)
        
        center = OpenMaya.MPoint(centerPlug.child(0).asFloat(), centerPlug.child(1).asFloat(), centerPlug.child(2).asFloat())
        size = pHelper.findPlug(PointLocator.size, False).asFloat()
        
        p1 = center + 0.5 * size * OpenMaya.MVector.kOneVector
        p2 = center - 0.5 * size * OpenMaya.MVector.kOneVector
        
        box = OpenMaya.MBoundingBox(p1, p2)
        
        return box

def initializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj, "JCarlos Ramirez", "1.0")

    try:
        plugin.registerNode("PointLocator", PointLocator.nodeTypeId, PointLocator.creator, PointLocator.initialize, OpenMaya.MPxNode.kLocatorNode, PointLocator.drawDbClassification)
    except:
        sys.stderr.write("Failed to register node\n")
        raise

    try:
        OpenMayaRender.MDrawRegistry.registerDrawOverrideCreator(PointLocator.drawDbClassification, PointLocator.nodeTypeName, PointLocatorDrawOverride.creator)
    except:
        sys.stderr.write("Failed to register override\n")
        raise

def uninitializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.deregisterNode(PointLocator.nodeTypeId)
    except:
        sys.stderr.write("Failed to deregister node\n")
        pass

    try:
        OpenMayaRender.MDrawRegistry.deregisterDrawOverrideCreator(PointLocator.drawDbClassification, PointLocator.nodeTypeName)
    except:
        sys.stderr.write("Failed to deregister override\n")
        pass