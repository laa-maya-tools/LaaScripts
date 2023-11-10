import ScreenDrawer

import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

import Utils.Python as PythonUtils
from Utils.Maya.OptionVar import OptionVarConfiguration

import CinematicEditor.Window as CinematicEditorUtils
import ActorManager
import ExporterWindow

import math

phi = (1 + math.sqrt(5)) / 2
iphi = 1 / phi

class GuideMode(object):
    
    def __init__(self, order):
        self.order = order
        
    def getOrder(self):
        return self.order
    
    def getName(self):
        return "None"
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        pass
    
    @staticmethod
    def drawPoints(drawManager, *args):
        if len(args) == 1:
            args = args[0]
        pointArray = OpenMaya.MPointArray()
        for e in args:
            pointArray.append(OpenMaya.MPoint(e[0], e[1]))
        drawManager.lineList(pointArray, True)
        
    @staticmethod
    def mirrorHorizontally(x, y, w, h):
        return x + w, y, -w, h
        
    @staticmethod
    def mirrorVertically(x, y, w, h):
        return x, y + h, w, -h


class CrossMode(GuideMode):
    
    def getName(self):
        return "Cross"
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        self.drawPoints(drawManager,
            (x, y), (x + w, y + h),
            (x + w, y), (x, y + h)
        )
            

class QuadDivisionMode(GuideMode):
    
    def __init__(self, order, divisions):
        GuideMode.__init__(self, order)
        
        self.divisions = divisions
    
    def getName(self):
        if self.divisions == 2:
            return "Rule of Halfs"
        elif self.divisions == 3:
            return "Rule of Thirds"
        elif self.divisions == 4:
            return "Rule of Fourths"
        else:
            return "Rule of {}ths".format(self.divisions)
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        points = []
        for i in range(1, self.divisions):
            points.append((x + i * w / self.divisions, y))
            points.append((x + i * w / self.divisions, y + h))
            points.append((x, y + i * h / self.divisions))
            points.append((x + w, y + i * h / self.divisions))
            
        self.drawPoints(drawManager, points)


class GoldenSectionMode(GuideMode):
    
    def getName(self):
        return "Golden Section"
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        self.drawPoints(drawManager,
            (x + w * iphi, y), (x + w * iphi, y + h),
            (x + w * (1 - iphi), y), (x + w * (1 - iphi), y + h),
            (x, y + h * iphi), (x + w, y + h * iphi),
            (x, y + h * (1 - iphi)), (x + w, y + h * (1 - iphi))
        )


class GoldenTrianglesMode(GuideMode):
    
    def __init__(self, order, inverse=False):
        GuideMode.__init__(self, order)
        
        self.inverse = inverse
    
    def getName(self):
        return "Golden Triangles {}".format("\\" if self.inverse else "/")
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        if self.inverse:
            x, y, w, h = self.mirrorHorizontally(x, y, w, h)
        
        hw2 = h * h / (h * h + w * w)
        self.drawPoints(drawManager,
            (x, y), (x + w, y + h),
            (x, y + h), (x + w * hw2, y + h * hw2),
            (x + w, y), (x + w * (1 - hw2), y + h * (1 - hw2))
        )


class GoldenSpiralMode(GuideMode):
    
    def __init__(self, order, mirrorHorizontal=False, mirrorVertical=False):
        GuideMode.__init__(self, order)
        
        self.mirrorHorizontal = mirrorHorizontal
        self.mirrorVertical = mirrorVertical
    
    def getName(self):
        if self.mirrorVertical:
            if self.mirrorHorizontal:
                d = "↖"
            else:
                d = "↗"
        else:
            if self.mirrorHorizontal:
                d = "↙"
            else:
                d = "↘"
        return "Golden Spiral {}".format(d)
    
    def addUIDrawables(self, drawManager, x, y, w, h):
        if w > h * phi:
            x += (w - h * phi) / 2
            w = h * phi
        else:
            y += (h - w / phi) / 2
            h = w / phi
        
        if self.mirrorHorizontal:
            x, y, w, h = self.mirrorHorizontally(x, y, w, h)
        if self.mirrorVertical:
            x, y, w, h = self.mirrorVertically(x, y, w, h)
        
        self.drawGoldenSpiralSpiral(drawManager, x, y, w, h, 0, 10)
    
    def drawGoldenSpiralSpiral(self, drawManager, x, y, w, h, rotation, iterations):
        if iterations == 0:
            return
        
        wSign = 1 if w > 0 else -1
        hSign = 1 if h > 0 else -1
        sign = wSign * hSign
        r = OpenMaya.MEulerRotation(0, 0, rotation)
        newOrigin = OpenMaya.MPoint(x, y) + OpenMaya.MVector(sign * h, h).rotateBy(r)
        spiralCenter = OpenMaya.MPoint(x, y) + OpenMaya.MVector(sign * h, 0).rotateBy(r)
        
        turns = 0
        if wSign > 0:
            turns = 0 if hSign > 0 else 1
        else:
            turns = -1 if hSign > 0 else 2
        rr = OpenMaya.MEulerRotation(0, 0, rotation + (turns * math.pi / 2))
        
        drawManager.arc2d(spiralCenter, OpenMaya.MVector(0, 1).rotateBy(rr), OpenMaya.MVector(-1, 0).rotateBy(rr), abs(h))
        drawManager.line2d(newOrigin, spiralCenter)
        
        self.drawGoldenSpiralSpiral(drawManager, newOrigin.x, newOrigin.y, sign * h, sign * w - h, rotation - sign * math.pi / 2, iterations - 1)


CINEMATIC_GUIDES_ENABLED_OPTIONVAR = OptionVarConfiguration("CinematicGuidesEnabled", "CINEMATIC_EDITOR_CINEMATIC_GUIDES_ENABLED", OptionVarConfiguration.TYPE_INTEGER, True)  # Default is Enabled
CINEMATIC_GUIDES_MODE_OPTIONVAR = OptionVarConfiguration("CinematicGuidesMode", "CINEMATIC_EDITOR_CINEMATIC_GUIDES_MODE", OptionVarConfiguration.TYPE_STRING, "MODE_RULE_OF_THIRDS")  # Default is RuleOfThirds

class CinematicGuides(ScreenDrawer.ScreenDrawer):
    
    class Data(object):
        def __init__(self, cinematicGuides, cameraPath, frameContext):
            self.enabled = cinematicGuides.enabled
            if not self.enabled:
                return
            
            self.enabled = CinematicEditorUtils.isVisible() and CinematicEditorUtils.isCinematicCamera(cameraPath.fullPathName())
            self.enabled |= ExporterWindow.isVisible() and ActorManager.isExportCamera(cameraPath.fullPathName())
            if not self.enabled:
                return
            
            self.mode = cinematicGuides.mode
            
            self.color = cinematicGuides.color
            self.lineWidth = cinematicGuides.lineWidth
            
            self.dimensions = ScreenDrawer.ScreenDrawerManager.getCameraRect(cameraPath, frameContext)
    
    
    class Modes(PythonUtils.Enum.EnumBase):
        MODE_NONE = GuideMode(0)
        MODE_CROSS = CrossMode(1)
        MODE_RULE_OF_HALFS = QuadDivisionMode(2, 2)
        MODE_RULE_OF_THIRDS = QuadDivisionMode(3, 3)
        MODE_RULE_OF_FOURTHS = QuadDivisionMode(4, 4)
        MODE_GOLDEN_SECTION = GoldenSectionMode(5)
        MODE_GOLDEN_TRIANGLES_A = GoldenTrianglesMode(6)
        MODE_GOLDEN_TRIANGLES_B = GoldenTrianglesMode(7, inverse=True)
        MODE_GOLDEN_SPIRAL_BOTTOM_RIGHT = GoldenSpiralMode(8)
        MODE_GOLDEN_SPIRAL_BOTTOM_LEFT = GoldenSpiralMode(9, mirrorHorizontal=True)
        MODE_GOLDEN_SPIRAL_TOP_RIGHT = GoldenSpiralMode(10, mirrorVertical=True)
        MODE_GOLDEN_SPIRAL_TOP_LEFT = GoldenSpiralMode(11, mirrorHorizontal=True, mirrorVertical=True)
        
    
    color = OpenMaya.MColor((1.0, 1.0, 0.0))
    lineWidth = 1
    
    @property
    def enabled(self):
        return CINEMATIC_GUIDES_ENABLED_OPTIONVAR.value
    
    @enabled.setter
    def enabled(self, v):
        CINEMATIC_GUIDES_ENABLED_OPTIONVAR.value = v
        
        cmds.refresh(force=True)
        
    @property
    def mode(self):
        return CinematicGuides.Modes.getDict()[CINEMATIC_GUIDES_MODE_OPTIONVAR.value]
        
    @mode.setter
    def mode(self, v):
        CINEMATIC_GUIDES_MODE_OPTIONVAR.value = CinematicGuides.Modes.getKeyFromValue(v)
        
        if self.enabled:
            cmds.refresh(force=True)
    
    def prepareForDraw(self, objPath, cameraPath, frameContext):
        return CinematicGuides.Data(self, cameraPath, frameContext)
    
    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        if data.enabled:
            drawManager.beginDrawable()
            
            drawManager.setColor(data.color)
            drawManager.setLineWidth(data.lineWidth)
            
            data.mode.addUIDrawables(drawManager, data.dimensions[0], data.dimensions[1], data.dimensions[2], data.dimensions[3])
            
            drawManager.endDrawable()
    
    
if __name__ == "__main__":
    ScreenDrawer.ScreenDrawerManager.clearScreenDrawers()
    reload(ScreenDrawer)
    guides = CinematicGuides()
    ScreenDrawer.ScreenDrawerManager.registerScreenDrawer(guides)
    guides.enabled = True
    guides.mode = guides.Modes.MODE_RULE_OF_THIRDS
    