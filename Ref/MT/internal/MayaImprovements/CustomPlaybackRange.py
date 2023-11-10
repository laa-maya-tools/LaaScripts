from PySide2 import QtCore, QtGui, QtWidgets

import maya.cmds as cmds
import maya.app.general.mayaMixin as MayaMixin

from MayaImprovements import MayaImprovement
from QtCustomWidgets.RangeSlider import RangeSlider

class CustomPlaybackRange(MayaMixin.MayaQWidgetBaseMixin, RangeSlider):
    
    def __init__(self, parent=None):
        super(CustomPlaybackRange, self).__init__(parent=parent)
        
        self.layout().setContentsMargins(5,2,5,3)

        self.rangeBar.setMinimumSize(0, 20)
        self.rangeBar.layout().setContentsMargins(4,0,3,0)

        self.rangeStartSlider.setFixedSize(15, 14)
        self.rangeEndSlider.setFixedSize(15, 14)
    
    def showEvent(self, event):
        RangeSlider.showEvent(self, event)
        
        self.playbackRangeChangedScriptJobs = [cmds.scriptJob(event=["playbackRangeChanged", self.updateRangeSlider]), cmds.scriptJob(event=["playbackRangeSliderChanged", self.updateRangeSlider])]

    def hideEvent(self, event):
        for scriptJob in self.playbackRangeChangedScriptJobs:
            cmds.scriptJob(kill=scriptJob)
            
        RangeSlider.hideEvent(self, event)

    def getRangeStart(self):
        return cmds.playbackOptions(q=True, min=True)
    
    def getRangeEnd(self):
        return cmds.playbackOptions(q=True, max=True)
    
    def getRangeMinimum(self):
        return cmds.playbackOptions(q=True, ast=True)
    
    def getRangeMaximum(self):
        return cmds.playbackOptions(q=True, aet=True)
    
    def setRangeStart(self, start):
        cmds.playbackOptions(min=start)
    
    def setRangeEnd(self, end):
        cmds.playbackOptions(max=end)
    
    def setRangeMinimum(self, minimum):
        cmds.playbackOptions(ast=minimum)
    
    def setRangeMaximum(self, maximum):
        cmds.playbackOptions(aet=maximum)
    
    def setRangeAndLimit(self, start, end, minimum, maximum):
        cmds.playbackOptions(min=start, max=end, ast=minimum, aet=maximum)
    
    def setRange(self, start, end):
        cmds.playbackOptions(min=start, max=end)
        
    def setLimit(self, minimum, maximum):
        cmds.playbackOptions(ast=minimum, aet=maximum)
        
    def setRangeStartAndMinimum(self, start, minimum):
        cmds.playbackOptions(min=start, ast=minimum)
        
    def setRangeEndAndMaximum(self, end, maximum):
        cmds.playbackOptions(max=end, aet=maximum)

    def isShiftKeyPressed(self):
        return cmds.getModifiers() & 1

    def isCtrlKeyPressed(self):
        return cmds.getModifiers() & 4
    
    def getFixedPixelToFrameRatio(self):
        return 20
    
    
class CustomPlaybackRangeManager(MayaImprovement):

    initialized = False

    # Constants
    defaultPlaybackRange = "RangeSlider|MainPlaybackRangeLayout|formLayout9|frameLayout3|rangeControl1"
    customPlaybackRangeOptionVar = "customPlaybackRangeEnabled"

    # Variables
    customPlaybackRangeUI = None
    
    @classmethod
    def isCustomPlaybackRangeEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.customPlaybackRangeOptionVar):
            default = True  # True by default
            cls.setCustomPlaybackRangeEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.customPlaybackRangeOptionVar)

    @classmethod
    def setCustomPlaybackRangeEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.customPlaybackRangeOptionVar, enabled))
            
        cmds.control(cls.defaultPlaybackRange, e=True, vis=not enabled)
        cmds.control(cls.customPlaybackRangeUI.objectName(), e=True, vis=enabled)

    @classmethod
    def initialize(cls):
        cls.initialized = True
        
        cls.customPlaybackRangeUI = CustomPlaybackRange()
        parentLayout = cls.defaultPlaybackRange.rsplit("|", 1)[0]
        cmds.control(cls.customPlaybackRangeUI.objectName(), e=True, p=parentLayout)

        cls.setCustomPlaybackRangeEnabled(cls.isCustomPlaybackRangeEnabled())   # We do this to renable the control

    @classmethod
    def uninitialize(cls):
        cls.setCustomPlaybackRangeEnabled(False, setVar=False)

        cmds.deleteUI(cls.customPlaybackRangeUI.objectName())
        cls.customPlaybackRangeUI = None

        cls.initialized = True