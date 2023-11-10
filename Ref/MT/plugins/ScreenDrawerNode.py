import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaRender as OpenMayaRender

import NodeID
import ScreenDrawer

import sys

## Viewport 2.0 override implementation
def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass

class ScreenDrawerNode(OpenMayaUI.MPxLocatorNode):
    
    drawDbClassification = "drawdb/geometry/ScreenDrawer"
    nodeTypeId = NodeID.ScreenDrawerID
    nodeTypeName = "ScreenDrawer"
    
    @staticmethod
    def creator():
        return ScreenDrawerNode()
    
    @staticmethod
    def initialize():
        pass    # No need for attributes in this node
    
    def excludeAsLocator(self):
        return False    # This will make so the node is not hidden when the locators are hidden
        
    
class ScreenDrawerData(OpenMaya.MUserData):
    
    def __init__(self):
        OpenMaya.MUserData.__init__(self, False)

        self.drawerData = {}
        
    def prepareForDraw(self, objPath, cameraPath, frameContext):
        self.drawerData = ScreenDrawer.ScreenDrawerManager.prepareForDraw(objPath, cameraPath, frameContext)
            
    def addUIDrawables(self, objPath, drawManager, frameContext):
        ScreenDrawer.ScreenDrawerManager.addUIDrawables(self.drawerData, objPath, drawManager, frameContext)
        

class ScreenDrawerDrawOverride(OpenMayaRender.MPxDrawOverride):
        
    @staticmethod
    def creator(obj):
        return ScreenDrawerDrawOverride(obj)

    @staticmethod
    def draw(context, data):
        return  # No UI will be drawn here (addUIDrawables will be used instead)
    
    def __init__(self, obj):
        OpenMayaRender.MPxDrawOverride.__init__(self, obj, ScreenDrawerDrawOverride.draw)

    def supportedDrawAPIs(self):
        ## this plugin supports both GL and DX
        return OpenMayaRender.MRenderer.kOpenGL | OpenMayaRender.MRenderer.kDirectX11 | OpenMayaRender.MRenderer.kOpenGLCoreProfile

    def hasUIDrawables(self):
        return True
    
    def prepareForDraw(self, objPath, cameraPath, frameContext, oldData):
        data = oldData
        if not isinstance(data, ScreenDrawerData):
            data = ScreenDrawerData()
            
        data.prepareForDraw(objPath, cameraPath, frameContext)
        
        return data

    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        if not isinstance(data, ScreenDrawerData):
            return
        
        data.addUIDrawables(objPath, drawManager, frameContext)
        
        
def initializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.registerNode(ScreenDrawerNode.nodeTypeName, ScreenDrawerNode.nodeTypeId, ScreenDrawerNode.creator, ScreenDrawerNode.initialize, OpenMaya.MPxNode.kLocatorNode, ScreenDrawerNode.drawDbClassification)
        OpenMayaRender.MDrawRegistry.registerDrawOverrideCreator(ScreenDrawerNode.drawDbClassification, ScreenDrawerNode.nodeTypeName, ScreenDrawerDrawOverride.creator)
    except:
        sys.stderr.write("Failed to register node: {}\n".format(ScreenDrawerNode.nodeTypeName))
        raise

def uninitializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.deregisterNode(ScreenDrawerNode.nodeTypeId)
        OpenMayaRender.MDrawRegistry.deregisterDrawOverrideCreator(ScreenDrawerNode.drawDbClassification, ScreenDrawerNode.nodeTypeName)
    except:
        sys.stderr.write("Failed to deregister node: {}\n".format(ScreenDrawerNode.nodeTypeName))
        pass