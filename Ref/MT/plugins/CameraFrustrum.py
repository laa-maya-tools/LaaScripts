import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaRender as OpenMayaRender

import maya.cmds as cmds

import NodeID

import CinematicEditor.Window.CinematicEditorConfiguration as CEConfiguration

import Utils.OpenMaya as OpenMayaUtils

import math
import sys

## Viewport 2.0 override implementation
def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass

class CameraFrustrum(OpenMayaUI.MPxLocatorNode):
    
    nodeTypeId = NodeID.CameraFrustrumID
    nodeTypeName = "CameraFrustrum"
    classification = "drawdb/geometry/camera/CameraFrustrum"
    
    cameraFrustrumHeader = OpenMaya.MObject()
    enabled = OpenMaya.MObject()
    coneSize = OpenMaya.MObject()
    
    focalLength = OpenMaya.MObject()
    horizontalFilmAperture = OpenMaya.MObject()
    verticalFilmAperture = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return CameraFrustrum()
    
    @staticmethod
    def initialize():
        extensionAttributeFn = OpenMaya.MFnCompoundAttribute()
        numericAttributeFn = OpenMaya.MFnNumericAttribute()
        
        CameraFrustrum.cameraFrustrumHeader = extensionAttributeFn.create("CameraFrustrum", "cf")
        
        CameraFrustrum.enabled = numericAttributeFn.create("enabled", "en", OpenMaya.MFnNumericData.kBoolean, True)
        extensionAttributeFn.addChild(CameraFrustrum.enabled)
        
        CameraFrustrum.coneSize = numericAttributeFn.create("coneSize", "cs", OpenMaya.MFnNumericData.kFloat, 10.0)
        numericAttributeFn.setMin(0.0)
        numericAttributeFn.setMax(1000.0)
        extensionAttributeFn.addChild(CameraFrustrum.coneSize)
        
        CameraFrustrum.addAttribute(CameraFrustrum.cameraFrustrumHeader)
        
        CameraFrustrum.focalLength = numericAttributeFn.create("focalLength", "fl", OpenMaya.MFnNumericData.kFloat, 2.5)
        numericAttributeFn.setMin(2.5)
        numericAttributeFn.setMax(3500.0)
        CameraFrustrum.addAttribute(CameraFrustrum.focalLength)
        
        CameraFrustrum.horizontalFilmAperture = numericAttributeFn.create("horizontalFilmAperture", "hfa", OpenMaya.MFnNumericData.kFloat)
        numericAttributeFn.setMin(3.937e-05)
        numericAttributeFn.setMax(1200.0)
        CameraFrustrum.addAttribute(CameraFrustrum.horizontalFilmAperture)
        
        CameraFrustrum.verticalFilmAperture = numericAttributeFn.create("verticalFilmAperture", "vfa", OpenMaya.MFnNumericData.kFloat)
        numericAttributeFn.setMin(3.937e-05)
        numericAttributeFn.setMax(1200.0)
        CameraFrustrum.addAttribute(CameraFrustrum.verticalFilmAperture)
    
    def __init__(self):
        OpenMayaUI.MPxLocatorNode.__init__(self)
    
    def excludeAsLocator(self):
        return False    # This will make so the node is not hidden when the locators are hidden
    
    def getShapeSelectionMask(self):
        return OpenMaya.MSelectionMask(OpenMaya.MSelectionMask.kSelectCameras)

    # NOTE: Los métodos de la bounding Box en MPxLocatorNode se usan para la selección y para encuadrar al pulsar la tecla F
    def isBounded(self):
        return True
 
    def boundingBox(self):
        box = OpenMaya.MBoundingBox()
        
        width, height, depth = CameraFrustrumDrawOverride.getFrustrumDimensions(self.thisMObject())
        frustrumPoints = CameraFrustrumDrawOverride.getFrustrumPoints(width, height, depth)
        
        box.expand(OpenMaya.MPoint(0, 0, 0))
        for point in frustrumPoints:
            box.expand(point)
        
        return box


class CameraFrustrumData(OpenMaya.MUserData):
    
    def __init__(self):
        OpenMaya.MUserData.__init__(self, False) ## don't delete after draw

        self.enabled = True
        
        self.color = OpenMaya.MColor()
        
        self.width = 0.0
        self.height = 0.0
        self.depth = 0.0


class CameraFrustrumDrawOverride(OpenMayaRender.MPxDrawOverride):
    
    @staticmethod
    def creator(obj):
        return CameraFrustrumDrawOverride(obj)
    
    @staticmethod
    def getFrustrumDimensions(node):
        coneSize = OpenMaya.MPlug(node, CameraFrustrum.coneSize).asFloat()
        focalLength = OpenMaya.MPlug(node, CameraFrustrum.focalLength).asFloat()
        horizontalFilmAperture = OpenMaya.MPlug(node, CameraFrustrum.horizontalFilmAperture).asFloat()
        verticalFilmAperture = OpenMaya.MPlug(node, CameraFrustrum.verticalFilmAperture).asFloat()
        
        horizontalFov = 2.0 * math.atan(horizontalFilmAperture * 25.4 / (2.0 * focalLength))
        verticalFov = 2.0 * math.atan(verticalFilmAperture * 25.4 / (2.0 * focalLength))
        
        width = coneSize * math.sin(horizontalFov / 2.0)
        height = coneSize * math.sin(verticalFov / 2.0)
        depth = coneSize * math.cos(horizontalFov / 2.0)
        
        return (width,  height, depth)
    
    @staticmethod
    def getFrustrumPoints(width, height, depth):
        return [
            OpenMaya.MPoint( width,  height, -depth),
            OpenMaya.MPoint(-width,  height, -depth),
            OpenMaya.MPoint( width, -height, -depth),
            OpenMaya.MPoint(-width, -height, -depth)
        ]
    
    def __init__(self, obj):
        OpenMayaRender.MPxDrawOverride.__init__(self, obj, None, isAlwaysDirty=True) # We need the isAlwaysDirty flag set to True to update the frustrums when the cameras are hidden on a viewport
 
    def supportedDrawAPIs(self):
        ## this plugin supports both GL and DX
        return OpenMayaRender.MRenderer.kOpenGL | OpenMayaRender.MRenderer.kDirectX11 | OpenMayaRender.MRenderer.kOpenGLCoreProfile

    def hasUIDrawables(self):
        return True

    # NOTE: Los métodos de la bounding Box en MPxDrawingOverride se usan para el frustrum culling
    def isBounded(self, objPath, cameraPath):
        return True
 
    def boundingBox(self, objPath, cameraPath):
        box = OpenMaya.MBoundingBox()
        
        if cameraPath.transform() != objPath.transform():   # We won't need to draw the shape on it's camera
            width, height, depth = CameraFrustrumDrawOverride.getFrustrumDimensions(objPath.node())
            frustrumPoints = CameraFrustrumDrawOverride.getFrustrumPoints(width, height, depth)
            
            box.expand(OpenMaya.MPoint(0, 0, 0))
            for point in frustrumPoints:
                box.expand(point)
        
        return box
 
    def prepareForDraw(self, objPath, cameraPath, frameContext, oldData):
        data = oldData
        if not isinstance(data, CameraFrustrumData):
            data = CameraFrustrumData()
            
        # Skip drawing if the frustrums are disabled
        if not CEConfiguration.CAMERA_FRUSTRUMS_ENABLED_OPTIONVAR.value:
            data.enabled = False
            return data

        # Skip drawing if the cameras are hidden
        if frameContext.objectTypeExclusions() & frameContext.kExcludeCameras:
            data.enabled = False
            return data

        # No need to draw if the current camera is the frustrum's
        if cameraPath.transform() == objPath.transform():
            data.enabled = False
            return data

        data.enabled = OpenMaya.MPlug(objPath.node(), CameraFrustrum.enabled).asBool()
        if not data.enabled:
            return data
        
        data.width, data.height, data.depth = CameraFrustrumDrawOverride.getFrustrumDimensions(objPath.node())
        
        displayStatus = OpenMayaRender.MGeometryUtilities.displayStatus(objPath)
        if displayStatus == OpenMayaRender.MGeometryUtilities.kDormant and not OpenMayaUtils.getDisplayOverrideColorState(objPath):
            data.color = OpenMayaUI.M3dView.active3dView().colorAtIndex(cmds.displayColor("camera", q=True, dormant=True) - 1)
        else:
            data.color = OpenMayaRender.MGeometryUtilities.wireframeColor(objPath)
        
        return data

    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        if not isinstance(data, CameraFrustrumData):
            return

        if not data.enabled:
            return

        drawManager.beginDrawable()

        drawManager.setColor(data.color)

        frustrumPoints = CameraFrustrumDrawOverride.getFrustrumPoints(data.width, data.height, data.depth)
        for point in frustrumPoints:
            drawManager.line(OpenMaya.MPoint(0, 0, 0), point)

        drawManager.rect(OpenMaya.MPoint(0, 0, -data.depth), OpenMaya.MVector(0, 1, 0), OpenMaya.MVector(0, 0, 1), data.width, data.height, False)

        drawManager.endDrawable()


def initializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)
    
    try:
        plugin.registerNode(CameraFrustrum.nodeTypeName, CameraFrustrum.nodeTypeId, CameraFrustrum.creator, CameraFrustrum.initialize, OpenMaya.MPxNode.kLocatorNode, CameraFrustrum.classification)
        OpenMayaRender.MDrawRegistry.registerDrawOverrideCreator(CameraFrustrum.classification, CameraFrustrum.nodeTypeName, CameraFrustrumDrawOverride.creator)
    except:
        sys.stderr.write("Failed to register node: {}\n".format(CameraFrustrum.nodeTypeName))
        raise
    
def uninitializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.deregisterNode(CameraFrustrum.nodeTypeId)
        OpenMayaRender.MDrawRegistry.deregisterDrawOverrideCreator(CameraFrustrum.classification, CameraFrustrum.nodeTypeName)
    except:
        sys.stderr.write("Failed to deregister node: {}\n".format(CameraFrustrum.nodeTypeName))
        raise