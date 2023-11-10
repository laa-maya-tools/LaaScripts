# coding: utf-8

from PySide2 import QtCore, QtWidgets, QtGui

import maya.api.OpenMaya as OpenMaya
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window.ShotTimeline as ShotTimeline
import CinematicEditor.Window.TimelineSlider as TimelineSlider
import CinematicEditor.Window.CinematicEditorConfiguration as CinematicEditorConfiguration
from CinematicEditor.Shot import Shot

import ScreenDrawer.CinematicGuides as CinematicGuides

#from importlib import reload
#reload(ShotTimeline)
#reload(TimelineSlider)

from QtCustomWidgets.UIFileWidget import UIFileWidget

import ProjectPath

import os
import json
import functools

class TabBarPainter(QtCore.QObject):
    
    def paint(self, widget, event):
        brush = QtGui.QBrush(QtGui.QColor.fromHsv(0, 0, 132), QtCore.Qt.Dense7Pattern)
        offset = 2
        scaleX = 0.74
        scaleY = 0.75
        
        painter = QtGui.QPainter(widget)
        
        painter.fillRect(event.rect(), widget.palette().color(QtGui.QPalette.Button))
        
        transform = painter.transform()
        transform.scale(scaleX, scaleY)
        painter.setTransform(transform)
        
        painter.setBrushOrigin(offset, 0)
        rect = event.rect()
        rect.setX(rect.x() + offset)
        rect.setWidth(rect.width() / scaleX - offset)
        rect.setHeight(rect.height() / scaleY)
        
        painter.fillRect(rect, brush)

    def eventFilter(self, widget, event):
        if event.type() == event.Paint and widget.count() == 1:
            self.paint(widget, event)
            return True
        
        return False


class CinematicEditorTimeline(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    
    title = "Cinematic Timeline"

    controlName = "CinematicEditorTimeline"
    workspaceControlName = controlName + "WorkspaceControl"
    
    tabBarPainter = TabBarPainter()
    
    PLAYBACK_EXTRA_FRAMES = 30
    
    GO_TO_FRAME_BUTTON_HOLD_DELAY = 300 #Miliseconds
    
    ICON_PATH = os.path.join(ProjectPath.getToolsFolder(), "CinematicEditor", "Window", "icons")
    ICON_CINEMATIC_PLAY = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_play.png"))
    ICON_CINEMATIC_STOP = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_stop.png"))
    ICON_CINEMATIC_NEXT_FRAME = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_next_frame.png"))
    ICON_CINEMATIC_NEXT_SHOT = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_next_shot.png"))
    ICON_CINEMATIC_PREVIOUS_FRAME = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_previous_frame.png"))
    ICON_CINEMATIC_PREVIOUS_SHOT = QtGui.QIcon(os.path.join(ICON_PATH, "cinematic_previous_shot.png"))

    @classmethod
    def destroyInstance(cls):
        if cmds.workspaceControl(cls.workspaceControlName, q=True, exists=True):
            cmds.workspaceControl(cls.workspaceControlName, e=True, close=True)
            cmds.deleteUI(cls.workspaceControlName)
    
    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------

    def __init__(self, mainWindow, parent=None):
        super(CinematicEditorTimeline, self).__init__(parent=parent)
        
        # The timeline depends on the main window and, as such, the timeline will be updated by the main window, and not the other way.
        # The timeline only stores a reference to the main window to close it if this window is closed, and to refresh the main window if the timeline modifies the cutscene.
        self.mainWindow = mainWindow
        
        # We could know which shot is the current one by comparing the current frame with each shot range (or the current camera).
        # But if several shots share the same frames (and camera), we wouldn't know which of them the user would be working on.
        # As such, we store which shot is the current one and update it whenever a user action chages the current time or animation range.
        self._currentShot = None
        
        # This variable is necessary to know if show is being called because of the window being opened or docked.
        self._wasClosed = True
        
        # Whether or not the cutscene is being played back.
        # Used as a control flag to enable a disable certain features.
        self.playingBackCutscene = False
        
        # Timers used for repeat events.
        self.goToFrameButtonHoldTimer = None    # When holding the nextFrameButton or previousFrameButton, after some delay, the cutscene will start playing untile the button is released.

        # Window Configuration
        self.destroyInstance()
        self.setObjectName(self.controlName)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(":/movie.svg"))
        
        # UI Loading
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        uiFileWidget = UIFileWidget(r"CinematicEditor/Window/ui/CinematicEditorTimeline.ui", self)
        layout.addWidget(uiFileWidget)
        self.ui = uiFileWidget.ui
        
        # Timeline Slider
        self.timelineSlider = TimelineSlider.TimelineSlider(self)
        self.ui.timelineSliderContainer.layout().addWidget(self.timelineSlider)
        
        # Shot Timeline
        self.shotTimeline = ShotTimeline.ShotTimeline(self, self.ui.timelineShotsContainer)
        self.timelineSlider.rangeChanged.connect(self.shotTimeline.onRangeChanged)
        
        # Buttons
        self.ui.rulesComboBox.insertItems(0, [mode.getName() for mode in self.getCinematicGuidesModes()])
        self.ui.filterMarkedShotsButton.toggled.connect(self.reloadShots)
        self.ui.showRulesCheckbox.toggled.connect(self.setCinematicGuidesEnabled)
        self.ui.rulesComboBox.currentIndexChanged.connect(self.setCinematicGuidesModeIndex)
        
        self.ui.previousShotButton.setIcon(self.ICON_CINEMATIC_PREVIOUS_SHOT)
        self.ui.previousFrameButton.setIcon(self.ICON_CINEMATIC_PREVIOUS_FRAME)
        self.ui.playbackButton.setIcon(self.ICON_CINEMATIC_PLAY)
        self.ui.nextFrameButton.setIcon(self.ICON_CINEMATIC_NEXT_FRAME)
        self.ui.nextShotButton.setIcon(self.ICON_CINEMATIC_NEXT_SHOT)
        
        self.ui.previousShotButton.clicked.connect(self.goToPreviousShot)
        self.ui.previousFrameButton.pressed.connect(self.onPreviousFrameButtonPressed)
        self.ui.previousFrameButton.released.connect(self.onPreviousFrameButtonReleased)
        self.ui.playbackButton.clicked.connect(functools.partial(self.togglePlayback, forward=True))    # If we don't do this, Qt will do some weird stuff with the kwargs
        self.ui.nextFrameButton.pressed.connect(self.onNextFrameButtonPressed)
        self.ui.nextFrameButton.released.connect(self.onNextFrameButtonReleased)
        self.ui.nextShotButton.clicked.connect(self.goToNextShot)
        
        self.ui.addShotButton.clicked.connect(self.onAddShotButtonPressed)
        self.ui.splitShotButton.clicked.connect(self.onSplitShotButtonPressed)

    def loadUIConfiguration(self):
        pass    # No configuration to load yet, most of it is handled by Maya

    def saveUIConfiguration(self):
        pass    # No configuration to save yet, most of it is handled by Maya

    def registerCallbacks(self):
        self.timeChangeCallback = OpenMaya.MDGMessage.addForceUpdateCallback(self.onTimeChanged)
        self.playbackToggledCallback = OpenMaya.MConditionMessage.addConditionCallback("playingBack", self.onPlaybackToggled)
        
        self.exitCallback = cmds.scriptJob(e=("quitApplication", self.onExit))

    def unregisterCallbacks(self):
        OpenMaya.MMessage.removeCallback(self.timeChangeCallback)
        OpenMaya.MMessage.removeCallback(self.playbackToggledCallback)
        
        cmds.scriptJob(kill=self.exitCallback)

    def reload(self):
        self.reloadShots()
        
        self.refreshCinematicGuides()

    def reloadShots(self):
        self.shotTimeline.reload()
        
        currentShot = self.getCurrentShot()
        if currentShot == None:
            enabledShots = self.getShotsToDisplay()
            if len(enabledShots) > 0:
                currentShot = enabledShots[0]
        self.setCurrentShot(currentShot)

    def refresh(self):
        self.refreshShots()
        self.refreshCinematicGuides()

    def refreshShots(self):
        self.shotTimeline.refresh()

    def refreshCinematicGuides(self):
        instance = CinematicGuides.CinematicGuides.instance()
        self.ui.showRulesCheckbox.setChecked(instance.enabled)
        self.ui.rulesComboBox.setCurrentIndex(self.getCinematicGuidesModes().index(instance.mode))

    def isFloating(self):
        return cmds.workspaceControl(self.workspaceControlName, q=True, floating=True)

    def updateMasterSlaveConfiguration(self):
        isMaster = not self.mainWindow.cachedMasterSlaveFile or self.mainWindow.cachedMasterSlaveFile.isMaster()
        
        self.ui.addShotButton.setEnabled(isMaster)
        self.ui.splitShotButton.setEnabled(isMaster)

    def getShotsToDisplay(self):
        cutscene = CinematicEditor.getCutscene()
        if not cutscene:
            return []
        elif self.ui.filterMarkedShotsButton.isChecked():
            shots = cutscene.getActiveShots()
            if self.mainWindow.cachedMasterSlaveFile:
                shots = [shot for shot in cutscene.getActiveShots() if self.mainWindow.cachedMasterSlaveFile.ownsShot(shot)]
            return shots
        else:
            return cutscene.getEnabledShots()

    # ------------------------------------
    # | Current Shot                     |
    # ------------------------------------

    def getCurrentShot(self):
        if self._currentShot != None and self._currentShot.nodeExists() and self._currentShot.enabled:
            return self._currentShot
        else:
            return None
    
    def setCurrentShot(self, shot, applyShotRange=False, goTo=Shot.goToStart, applyShotCamera=False, selectShotCamera=True, updateUI=True, selectOnTable=True, multiSelection=False):
        oldCurrentShot = self._currentShot
        self._currentShot = shot
        
        # If applyShotRange is None, it means we have to use the user option for Auto Framing
        if applyShotRange == True or (applyShotRange == None and CinematicEditorConfiguration.AUTO_FRAME_ENABLED_OPTIONVAR.value):
            shot.applyAnimRange(goTo=goTo)
        if applyShotCamera:
            selection = cmds.ls(selection=True)
            shot.applyCamera(selectCamera=selectShotCamera and selection == [oldCurrentShot.camera])
        
        if self.mainWindow.cachedMasterSlaveFile:
            self.mainWindow.cachedMasterSlaveFile.displayShotPreview(shot)
        
        if selectOnTable:
            if multiSelection:
                shotsToSelect = self.mainWindow.shotTable.getSelectedShots()
                if shot in shotsToSelect:
                    shotsToSelect.remove(shot)
                else:
                    shotsToSelect.append(shot)
            else:
                shotsToSelect = [shot]
            self.mainWindow.shotTable.selectShots(shotsToSelect)
        
        if updateUI:
            self.shotTimeline.refreshCurrentFrame(shots=[shot, oldCurrentShot])
    
    # ------------------------------------
    # | Playback                         |
    # ------------------------------------

    def togglePlayback(self, forward=True, fromTheBeginning=None):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        if self.playingBackCutscene:
            # Stops the playback
            self.ui.playbackButton.setIcon(self.ICON_CINEMATIC_PLAY)
            cmds.play(state=False)
            self.playingBackCutscene = False
            self.setCurrentShot(self.getCurrentShot(), applyShotRange=True, goTo=Shot.goToClamp, applyShotCamera=True, selectShotCamera=True)
            
        else:
            # Starts the playback
            currentShot = self.getCurrentShot()
            shots = self.getShotsToDisplay()
            if currentShot == None:
                if len(shots) == 0:
                    return
                currentShot = shots[0 if forward else -1]
                
            if fromTheBeginning == None:
                fromTheBeginning = cmds.getModifiers() & 4
                
            nextShot = currentShot
            nextFrame = None
            cutsceneFrame = cutscene.getCutsceneFrameFromShot(currentShot, cmds.currentTime(q=True) - currentShot.start, shots=shots)
            if forward:
                rangeStart = self.timelineSlider.getRangeStart()
                if cutsceneFrame < rangeStart or fromTheBeginning:
                    nextShot, nextFrame = cutscene.getShotAndFrameFromCutsceneFrame(rangeStart, shots=shots)
            else:
                rangeEnd = self.timelineSlider.getRangeEnd()
                if cutsceneFrame > rangeEnd or fromTheBeginning:
                    nextShot, nextFrame = cutscene.getShotAndFrameFromCutsceneFrame(rangeEnd, shots=shots)
            
            self.ui.playbackButton.setIcon(self.ICON_CINEMATIC_STOP)
            self.setPlaybackShot(nextShot, nextFrame) # This step is performed so the right animation range is set.
            self.playingBackCutscene = True
            cmds.play(state=True, forward=forward)
            
    def setPlaybackShot(self, nextShot, nextFrame=None):
        self.setCurrentShot(nextShot, applyShotCamera=True, selectShotCamera=False)
        cmds.playbackOptions(min=nextShot.start - self.PLAYBACK_EXTRA_FRAMES, ast=nextShot.start - self.PLAYBACK_EXTRA_FRAMES, max=nextShot.end + self.PLAYBACK_EXTRA_FRAMES, aet=nextShot.end + self.PLAYBACK_EXTRA_FRAMES)
        if nextFrame != None:
            # Changing the time with update=False makes Maya not to compute any extra information
            cmds.currentTime(nextShot.start + nextFrame, e=True, update=False)

    def goToCinematicFrame(self, cutsceneFrame, shots=None, applyShotRange=None, loopStart=True, loopEnd=True, useZoomedRange=True, stopPlayback=True):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        if stopPlayback and self.playingBackCutscene:
            self.togglePlayback()
        
        if shots == None:
            shots = self.getShotsToDisplay()
        cutsceneDuration = cutscene.getTotalDuration(shots=shots)
        
        if cutsceneFrame < 0:
            cutsceneFrame = cutsceneDuration + cutsceneFrame + 1
        
        rangeStart = self.timelineSlider.getRangeStart() if useZoomedRange else 0
        rangeEnd = self.timelineSlider.getRangeEnd() if useZoomedRange else cutsceneDuration
        if cutsceneFrame < rangeStart:
            cutsceneFrame = rangeEnd if loopStart else rangeStart
        elif cutsceneFrame > rangeEnd:
            cutsceneFrame = rangeStart if loopEnd else rangeEnd
            
        nextShot, nextFrame = cutscene.getShotAndFrameFromCutsceneFrame(cutsceneFrame, shots=shots)
        if nextShot != None:
            if nextShot != self.getCurrentShot():
                self.setCurrentShot(nextShot, applyShotRange=applyShotRange, goTo=Shot.goToNone, applyShotCamera=True)
            cmds.currentTime(nextShot.start + nextFrame, e=True)

    def goToNextCinematicFrame(self, count=1, applyShotRange=None):
        currentShot = self.getCurrentShot()
        if currentShot != None:
            shots = self.getShotsToDisplay()
            cutsceneFrame = currentShot.getCutscene().getCutsceneFrameFromShot(currentShot, cmds.currentTime(q=True) - currentShot.start, shots=shots)
            self.goToCinematicFrame(cutsceneFrame + count, applyShotRange=applyShotRange, shots=shots, loopStart=False)
        else:
            self.goToCinematicFrame(0, applyShotRange=applyShotRange)
            
    def goToPreviousCinematicFrame(self, count=1, applyShotRange=None):
        currentShot = self.getCurrentShot()
        if currentShot != None:
            shots = self.getShotsToDisplay()
            cutsceneFrame = currentShot.getCutscene().getCutsceneFrameFromShot(currentShot, cmds.currentTime(q=True) - currentShot.start, shots=shots)
            self.goToCinematicFrame(cutsceneFrame - count, applyShotRange=applyShotRange, shots=shots, loopEnd=False)
        else:
            self.goToCinematicFrame(-1, applyShotRange=applyShotRange)

    def goToNextShot(self, applyShotRange=None):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        shots = self.getShotsToDisplay()
        if len(shots) == 0:
            return
        
        currentShot = self.getCurrentShot()
        if currentShot != None:
            nextShotIndex = shots.index(currentShot) + 1
            if nextShotIndex == len(shots):
                self.goToCinematicFrame(self.timelineSlider.getRangeEnd(), shots=shots, applyShotRange=applyShotRange)
            else:
                nextShot = shots[nextShotIndex]
                cutsceneFrame = cutscene.getCutsceneFrameFromShot(nextShot, shots=shots)
                self.goToCinematicFrame(cutsceneFrame, shots=shots, applyShotRange=applyShotRange, loopStart=False, loopEnd=False)
            
        else:
            self.setCurrentShot(shots[0], applyShotRange=applyShotRange, goTo=Shot.goToStart, applyShotCamera=True)
        
    def goToPreviousShot(self, applyShotRange=None):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        shots = self.getShotsToDisplay()
        if len(shots) == 0:
            return
        
        currentShot = self.getCurrentShot()
        if currentShot != None:
            nextShotIndex = shots.index(currentShot) - 1
            if nextShotIndex == -1:
                self.goToCinematicFrame(self.timelineSlider.getRangeStart(), shots=shots, applyShotRange=applyShotRange)
            else:
                nextShot = shots[nextShotIndex]
                cutsceneFrame = cutscene.getCutsceneFrameFromShot(nextShot, shots=shots) + nextShot.getDuration() - 1
                self.goToCinematicFrame(cutsceneFrame, shots=shots, applyShotRange=applyShotRange, loopStart=False, loopEnd=False)
            
        else:
            self.setCurrentShot(shots[-1], applyShotRange=applyShotRange, goTo=Shot.goToEnd, applyShotCamera=True)

    # ------------------------------------
    # | Cinematic Guides                 |
    # ------------------------------------
    
    def getCinematicGuidesModes(self):
        cinematicGuidesModes = CinematicGuides.CinematicGuides.Modes.getValues()
        cinematicGuidesModes.sort(key=CinematicGuides.GuideMode.getOrder)
        return cinematicGuidesModes
    
    def setCinematicGuidesEnabled(self, enabled, updateUI=False):
        CinematicGuides.CinematicGuides.instance().enabled = enabled
        if updateUI:
            self.ui.showRulesCheckbox.setChecked(enabled)

    def setCinematicGuidesMode(self, mode, updateUI=False):
        CinematicGuides.CinematicGuides.instance().mode = mode
        if updateUI:
            self.ui.rulesComboBox.setCurrentIndex(self.getCinematicGuidesModes().index(mode))

    def setCinematicGuidesModeIndex(self, index, updateUI=False):
        CinematicGuides.CinematicGuides.instance().mode = self.getCinematicGuidesModes()[index]
        if updateUI:
            self.ui.rulesComboBox.setCurrentIndex(index)

    # ------------------------------------
    # | Buttons Events                   |
    # ------------------------------------

    def onNextFrameButtonPressed(self):
        self.goToNextCinematicFrame()
        
        if self.goToFrameButtonHoldTimer != None:
            self.goToFrameButtonHoldTimer.stop()
            
        self.goToFrameButtonHoldTimer = QtCore.QTimer()
        self.goToFrameButtonHoldTimer.setSingleShot(True)
        self.goToFrameButtonHoldTimer.start(self.GO_TO_FRAME_BUTTON_HOLD_DELAY)
        self.goToFrameButtonHoldTimer.timeout.connect(self.togglePlayback)

    def onNextFrameButtonReleased(self):
        if self.goToFrameButtonHoldTimer != None:
            self.goToFrameButtonHoldTimer.stop()
            
        if self.playingBackCutscene:
            self.togglePlayback()
    
    def onPreviousFrameButtonPressed(self):
        self.goToPreviousCinematicFrame()
        
        if self.goToFrameButtonHoldTimer != None:
            self.goToFrameButtonHoldTimer.stop()
            
        self.goToFrameButtonHoldTimer = QtCore.QTimer()
        self.goToFrameButtonHoldTimer.setSingleShot(True)
        self.goToFrameButtonHoldTimer.start(self.GO_TO_FRAME_BUTTON_HOLD_DELAY)
        self.goToFrameButtonHoldTimer.timeout.connect(functools.partial(self.togglePlayback, forward=False))
    
    def onPreviousFrameButtonReleased(self):
        if self.goToFrameButtonHoldTimer != None:
            self.goToFrameButtonHoldTimer.stop()
            
        if self.playingBackCutscene:
            self.togglePlayback()
    
    def onAddShotButtonPressed(self):
        if self.mainWindow.cachedMasterSlaveFile and not self.mainWindow.cachedMasterSlaveFile.isMaster():
            raise AssertionError("Only the Master can create Shots!")
        
        self.mainWindow.shotTable.addShot(promptEdit=True, parent=self)
    
    def onSplitShotButtonPressed(self):
        if self.mainWindow.cachedMasterSlaveFile and not self.mainWindow.cachedMasterSlaveFile.isMaster():
            raise AssertionError("Only the Master can split Shots!")
        
        currentShot = self.getCurrentShot()
        if currentShot != None:
            currentTime = cmds.currentTime(q=True)
            if currentTime > currentShot.start and currentTime < currentShot.end:
                currentShot.splitShot(currentTime)
                self.mainWindow.reloadShots()

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def lookForWorkspaceControl(self, data, workspaceControlName):
        subControls = []
        if "panels" in data:
            subControls = data["panels"]
        elif "splitter" in data:
            subControls = data["splitter"]["children"]
        elif "tabWidget" in data:
            subControls = data["tabWidget"]["controls"]
            
        for subControl in subControls:
            workspaceControlData = self.lookForWorkspaceControl(subControl, workspaceControlName)
            if workspaceControlData != None:
                return workspaceControlData
        
        if "objectName" in data and data["objectName"] == workspaceControlName:
            return data
            
        return None
    
    def onTimeChanged(self, *args):
        # This function may be called when a new scene is being openend, before we have a chance to unregister the callbacks.
        # It may also be called after the new scene is opened before giving us the change, so we must be sure it will never trigger again.
        if self._wasClosed or cmds.isTrue("opening"):
            self._wasClosed = True
            return
        
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        currentShot = self.getCurrentShot()
        shots = self.getShotsToDisplay()
        currentTime = cmds.currentTime(q=True)
        if self.playingBackCutscene:
            nextShot = None
            nextFrame = None
            
            cutsceneFrame = cutscene.getCutsceneFrameFromShot(currentShot, currentTime - currentShot.start, shots=shots)
            forward = cmds.play(q=True, forward=True)
            if forward:
                if cutsceneFrame >= self.timelineSlider.getRangeEnd():
                    nextShot, nextFrame = cutscene.getShotAndFrameFromCutsceneFrame(self.timelineSlider.getRangeStart(), shots=shots)
                elif currentTime > currentShot.end:
                    currentShotIndex = shots.index(currentShot)
                    nextShot = shots[currentShotIndex + 1]
                    nextFrame = 0
            else:
                if cutsceneFrame <= self.timelineSlider.getRangeStart():
                    nextShot, nextFrame = cutscene.getShotAndFrameFromCutsceneFrame(self.timelineSlider.getRangeEnd(), shots=shots)
                elif currentTime < currentShot.start:
                    currentShotIndex = shots.index(currentShot)
                    nextShot = shots[currentShotIndex - 1]
                    nextFrame = nextShot.getDuration()
            
            if nextShot != None:
                self.setPlaybackShot(nextShot, nextFrame)
                cmds.play(state=True, forward=forward)  # Changing the shot will stop the playback, so we'll have to resume it. This is invisible and won't procude any halt on the playback.
            else:
                self.shotTimeline.refreshCurrentFrame(shots=[currentShot], time=currentTime)
            
        else:
            if currentShot != None:
                if currentTime >= currentShot.start and currentTime <= currentShot.end:
                    self.shotTimeline.refreshCurrentFrame(shots=[currentShot], time=currentTime)
                    return
            
            overlappingShots = []
            for shot in shots:
                if currentTime >= shot.start and currentTime <= shot.end:
                    overlappingShots = cutscene.getShotsAtTime(currentTime) # We don't use the shots to display here, since inactive shots should also count as overlaping
            
            if len(overlappingShots) == 0:
                #self.setCurrentShot(None)
                pass  # We will preserve the previous shot just in case we need it in the future to decide between overlapping shots
            
            elif len(overlappingShots) == 1 or currentShot == None:
                self.setCurrentShot(overlappingShots[0])
            
            else:
                currentShotIndex = shots.index(currentShot)
                preferredShotIndex = None
                for shot in overlappingShots:
                    shotIndex = shots.index(shot)
                    if currentTime < currentShot.start:
                        if shotIndex < currentShotIndex and (preferredShotIndex == None or preferredShotIndex < shotIndex):
                            preferredShotIndex = shotIndex
                    else:
                        if shotIndex > currentShotIndex and (preferredShotIndex == None or preferredShotIndex > shotIndex):
                            preferredShotIndex = shotIndex
                
                if preferredShotIndex == None:
                    self.setCurrentShot(overlappingShots[0])    # This might happen if the shots are ordered weirdly, so we arbitrarily default to the first one
                else:
                    self.setCurrentShot(shots[preferredShotIndex])
    
    def onPlaybackToggled(self, isPlaying, *args):
        self.shotTimeline.refreshCurrentFrame()
        
        if not isPlaying and self.playingBackCutscene:
            self.togglePlayback()
    
    def onExit(self):
        currentWorkspaceLayout = cmds.workspaceLayoutManager(q=True, current=True).replace(" ", "_")
        workspaceFile = os.path.join(cmds.internalVar(userAppDir=True), cmds.about(version=True), "prefs", "workspaces", "{}.json".format(currentWorkspaceLayout))
        with open(workspaceFile, "r+") as f:
            data = json.load(f)
            
            workspaceControlData = self.lookForWorkspaceControl(data, self.workspaceControlName)
            if workspaceControlData == None:
                print("Unable to find the Cinematic Timeline Workspace Control on file: {}".format(workspaceFile))  # No exception is raised here since Maya will be closing and it can cause problems
                return
            
            workspaceControlData["closed"] = True
            
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
    
    def resizeEvent(self, e):
        self.shotTimeline.onResize()
    
    def showEvent(self, e):
        if self._wasClosed:
            self.loadUIConfiguration()
            self.registerCallbacks()
            
            self.refreshCinematicGuides()
            
            self._wasClosed = False
            
        # Moves the tab to the left and overrides it's drawing function to mimic Maya's dockControl
        if not self.isFloating() and self.parent() != None:
            cmds.workspaceControl(self.workspaceControlName, e=True, tabPosition=("west", False))
            tabWidget = self.parent().parent().parent()
            if tabWidget.count() == 1:
                tabBar = tabWidget.tabBar()
                tabBar.setUsesScrollButtons(False)
                tabBar.setTabText(0, "_" * 255) # Ayyyyyyyyyy LMAO (no, la propiedad "expanding" no funciona)
                tabBar.installEventFilter(self.tabBarPainter)
                font = tabBar.font()
                font.setPointSize(4)
                tabBar.setFont(font)
            
        # The resizeEvent won't be called when Maya restores the dimensions when the window is reopened, so we resize the timeline manually.
        self.resizeEvent(None)
    
    def dockCloseEventTriggered(self):
        self._wasClosed = True
        
        self.saveUIConfiguration()
        self.unregisterCallbacks()
        
        if self.mainWindow and not self.mainWindow.isHidden():
            self.mainWindow.close()
