import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext

class ScreenDrawer(object):
    
    @classmethod
    def instance(cls, createIfNotExists=True):
        for screenDrawer in ScreenDrawerManager.screenDrawers:
            if type(screenDrawer) == cls:
                return screenDrawer
        
        if createIfNotExists:
            instance = cls()
            ScreenDrawerManager.registerScreenDrawer(instance)
            return instance
        else:
            return None

    
    def prepareForDraw(self, objPath, cameraPath, frameContext):
        return None
    
    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        raise NotImplementedError()


class ScreenDrawerManager():
    
    screenDrawerNodeType = "ScreenDrawer"
    
    screenDrawers = []
    
    cameraRectCache = None  # Cache for the camera rect so multiple drawers can reuse it.
    
    @staticmethod
    def createScreenDrawerNode():
        screenDrawerNode = cmds.ls(type=ScreenDrawerManager.screenDrawerNodeType)
        if screenDrawerNode == None or len(screenDrawerNode) == 0:
            with UndoContext("Create Screen Drawer Node"):
                screenDrawerNode = cmds.createNode(ScreenDrawerManager.screenDrawerNodeType, name="{}Shape".format(ScreenDrawerManager.screenDrawerNodeType))
                parent = cmds.listRelatives(screenDrawerNode, parent=True)[0]
                parent = cmds.rename(parent, ScreenDrawerManager.screenDrawerNodeType)
                
                cmds.setAttr("{}.template".format(parent), True)            # Unselectable
                cmds.setAttr("{}.hiddenInOutliner".format(parent), True)    # Hidden in the Outliner
                
                return screenDrawerNode
        else:
            return screenDrawerNode[0]
    
    @classmethod
    def getScreenDrawers(cls):
        return cls.screenDrawers
    
    @classmethod
    def registerScreenDrawer(cls, screenDrawer):
        if screenDrawer in cls.screenDrawers:
            raise AssertionError("Unable to register ScreenDrawer: The drawer is already registered.")
        
        cls.screenDrawers.append(screenDrawer)
        
        cls.createScreenDrawerNode()
        
        cmds.refresh()
    
    @classmethod
    def unregisterScreenDrawer(cls, screenDrawer):
        if screenDrawer not in cls.screenDrawers:
            raise AssertionError("Unable to unregister ScreenDrawer: The drawer is not registered yet.")
        
        cls.screenDrawers.remove(screenDrawer)
        
        cmds.refresh()
    
    @classmethod
    def clearScreenDrawers(cls):
        cls.screenDrawers = []
        
        cmds.refresh()
        
    @classmethod
    def prepareForDraw(cls, objPath, cameraPath, frameContext):
        cls.cameraRectCache = None  # Clears the cached camera rect becouse it's no longer valid
        
        drawerData = {}
        for drawer in cls.screenDrawers:
            drawerData[drawer] = drawer.prepareForDraw(objPath, cameraPath, frameContext)
        return drawerData
    
    @classmethod
    def addUIDrawables(cls, drawerData, objPath, drawManager, frameContext):
        for drawer, data in drawerData.items():
            drawer.addUIDrawables(objPath, drawManager, frameContext, data)

    @classmethod
    def getCameraRect(cls, cameraPath, frameContext):
        if cls.cameraRectCache == None:        
            cameraFn = OpenMaya.MFnCamera(cameraPath.node())
            
            viewportDimensions = frameContext.getViewportDimensions()
            viewportAspectRatio = float(viewportDimensions[2]) / viewportDimensions[3]
            
            resolutionWidth = cmds.getAttr("defaultResolution.width")
            resolutionHeight = cmds.getAttr("defaultResolution.height")
            resolutionAspectRatio = float(resolutionWidth) / resolutionHeight
            
            offsetX = 0
            offsetY = 0
            if cameraFn.filmFit == 0:
                useVertical = viewportAspectRatio <= resolutionAspectRatio
            elif cameraFn.filmFit == 1:
                useVertical = False
            elif cameraFn.filmFit == 2:
                useVertical = True
            elif cameraFn.filmFit == 3:
                useVertical = viewportAspectRatio >= resolutionAspectRatio
                
            if useVertical:
                trueHeight = viewportDimensions[3] / cameraFn.overscan if cameraFn.overscan != 0 else 0
                trueWidth = trueHeight * resolutionAspectRatio
            else:                    
                trueWidth = viewportDimensions[2] / cameraFn.overscan if cameraFn.overscan != 0 else 0
                trueHeight = trueWidth / resolutionAspectRatio
                
            trueWidth *= cameraFn.lensSqueezeRatio
            trueHeight *= cameraFn.lensSqueezeRatio
            
            if cameraFn.panZoomEnabled and not cameraFn.renderPanZoom:
                zoom = cameraFn.zoom if cameraFn.zoom != 0 else 1
                trueWidth /= zoom
                trueHeight /= zoom
                apertureFactor = trueHeight / cameraFn.verticalFilmAperture if useVertical else trueWidth / cameraFn.horizontalFilmAperture
                offsetX -= apertureFactor * cameraFn.horizontalPan
                offsetY -= apertureFactor * cameraFn.verticalPan
            
            cls.cameraRectCache = (
                offsetX + (viewportDimensions[2] - trueWidth) / 2,
                offsetY + (viewportDimensions[3] - trueHeight) / 2,
                trueWidth,
                trueHeight
            )
        
        return cls.cameraRectCache
    