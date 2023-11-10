from QtCustomWidgets.RangeSlider import RangeSlider

from PySide2 import QtCore

import maya.cmds as cmds

import CinematicEditor

class TimelineSlider(RangeSlider):
    
    def __init__(self, cinematicEditorTimeline):
        RangeSlider.__init__(self)
        
        self.cinematicEditorTimeline = cinematicEditorTimeline
        
        self.rangeMaximum = self.getCutsceneDuration()
        self.rangeStart = self.getRangeMinimum()
        self.rangeEnd = self.getRangeMaximum()
        
        self.setMinimumHeight(18)
        self.rangeStartSlider.setFixedWidth(12)
        self.rangeStartSlider.setFixedHeight(12)
        self.rangeEndSlider.setFixedWidth(12)
        self.rangeEndSlider.setFixedHeight(12)
        
        self.rangeStartSlider.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.rangeEndSlider.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.rangeStartSlider.customContextMenuRequested.connect(self.onRangeStartSliderRightClicked)
        self.rangeEndSlider.customContextMenuRequested.connect(self.onRangeEndSliderRightClicked)
    
    def getRangeStart(self):
        return self.rangeStart
    
    def getRangeEnd(self):
        return self.rangeEnd
    
    def getRangeMinimum(self):
        return 0
    
    def getRangeMaximum(self):
        return self.rangeMaximum
    
    def setRangeStart(self, start):
        self.rangeStart = start
        self.updateRangeSlider()
    
    def setRangeEnd(self, end):
        self.rangeEnd = end
        self.updateRangeSlider()
        
    def setRange(self, start, end):
        self.rangeStart = start
        self.rangeEnd = end
        self.updateRangeSlider()
        
    def shouldDrawRangeLength(self):
        return False
        
    def getCutsceneDuration(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            duration = cutscene.getTotalDuration(shots=self.cinematicEditorTimeline.getShotsToDisplay())
            if duration > 0:
                return duration
        
        return 1
        
    def updateCutsceneDuration(self, emitSignal=True):
        cutsceneDuration = self.getCutsceneDuration()
        
        if self.rangeEnd == self.rangeMaximum:
            self.rangeEnd = cutsceneDuration
        elif self.rangeEnd > cutsceneDuration:
            self.rangeEnd = cutsceneDuration
            
        self.rangeMaximum = cutsceneDuration
        
        self.updateRangeSlider(emitSignal=emitSignal)

    def onRangeStartSliderRightClicked(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            cutsceneFrame = cutscene.getCutsceneFrameFromAnimationFrame(cmds.currentTime(q=True), preferredShot=self.cinematicEditorTimeline.getCurrentShot(), shots=self.cinematicEditorTimeline.getShotsToDisplay())
            if cutsceneFrame != None and cutsceneFrame < self.getRangeEnd():
                self.setRangeStart(cutsceneFrame)
        
    def onRangeEndSliderRightClicked(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            cutsceneFrame = cutscene.getCutsceneFrameFromAnimationFrame(cmds.currentTime(q=True), preferredShot=self.cinematicEditorTimeline.getCurrentShot(), shots=self.cinematicEditorTimeline.getShotsToDisplay())
            if cutsceneFrame != None and cutsceneFrame > self.getRangeStart():
                self.setRangeEnd(cutsceneFrame)
        