from PySide2 import QtCore, QtWidgets, QtGui

import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window as CinematicEditorUtils
from CinematicEditor.Shot import Shot

from QtCustomWidgets.DragableButton import DragableButton

from Utils.Maya.UndoContext import UndoContext

class TimelineRangePainter(QtWidgets.QWidget):
    
    frameColor = QtGui.QColor.fromHsl(0, 0, 117)
    selectedRangeColor = QtGui.QColor.fromRgb(128, 0, 0)

    def __init__(self, shotTimeline, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        
        self.shotTimeline = shotTimeline
        
        self.frameStep = None
        self.pixelsPerFrame = None
        
        self.dragging = False
        self.selectedRangeStart = None
        self.selectedRangeEnd = None
        
        self.setFixedHeight(16)
    
    def refreshRange(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            self.frameStep = None
            self.pixelsPerFrame = None
            return
        
        width = self.width()
        minPixelsPerStep = 30
        if width < minPixelsPerStep:
            self.frameStep = 1
            self.pixelsPerFrame = minPixelsPerStep
            return
        
        frameCount = cutscene.getTotalDuration(shots=self.shotTimeline.cinematicEditorTimeline.getShotsToDisplay())
        if frameCount == 0:
            frameCount = 1
            
        step = 1.0
        stepFactor = [2, 2.5]
        stepIndex = 0
        while True:
            pixelsPerStep = width * step / frameCount
            if pixelsPerStep >= minPixelsPerStep:
                self.pixelsPerFrame = pixelsPerStep / step
                self.frameStep = step
                break
            else:
                step *= stepFactor[stepIndex % 2]
                stepIndex += 1
        
        self.frameStep = int(self.frameStep)
        
        self.update()
    
    def getFrameFromPosition(self, pos):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            frame = (cutscene.getTotalDuration(shots=self.shotTimeline.cinematicEditorTimeline.getShotsToDisplay()) * pos) / self.width()
            timelineSlider = self.shotTimeline.cinematicEditorTimeline.timelineSlider
            frame = max(min(int(frame), timelineSlider.getRangeEnd()), timelineSlider.getRangeStart())
            return frame
        else:
            return None
    
    def setCurrentFrame(self, frame):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            shot, shotFrame = cutscene.getShotAndFrameFromCutsceneFrame(frame, shots=self.shotTimeline.cinematicEditorTimeline.getShotsToDisplay())
            if shot != None:
                oldCurrentShot = self.shotTimeline.cinematicEditorTimeline.getCurrentShot()
                if shot != oldCurrentShot:
                    self.shotTimeline.cinematicEditorTimeline.setCurrentShot(shot, applyShotRange=None, goTo=Shot.goToNone, applyShotCamera=True, updateUI=False)
        
                if self.shotTimeline.cinematicEditorTimeline.playingBackCutscene:
                    self.shotTimeline.cinematicEditorTimeline.togglePlayback()
                    
                cmds.currentTime(shot.start + shotFrame, e=True)
    
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if e.modifiers() & QtCore.Qt.ShiftModifier:
                self.selectedRangeStart = self.getFrameFromPosition(e.pos().x())
                self.selectedRangeEnd = None
            else:
                self.dragging = True
                self.mouseMoveEvent(e)
        
        elif e.button() == QtCore.Qt.RightButton:
            if self.selectedRangeStart != None:
                self.selectedRangeStart = None
                self.selectedRangeEnd = None
                self.update()
                
            else:
                cutscene = CinematicEditor.getCutscene()
                if cutscene != None:
                    frame, result = QtWidgets.QInputDialog.getInt(self, "Cinematic Editor", "Jump to Frame:", self.getFrameFromPosition(e.pos().x()), 0, cutscene.getTotalDuration(shots=self.shotTimeline.cinematicEditorTimeline.getShotsToDisplay()))
                    if result:
                        self.setCurrentFrame(frame)
    
    def mouseMoveEvent(self, e):
        if self.dragging or self.selectedRangeStart != None:
            frame = self.getFrameFromPosition(e.pos().x())
            if frame != None:            
                if self.selectedRangeStart != None:
                    self.selectedRangeEnd = frame if frame != self.selectedRangeStart else None
                    self.update()
                self.setCurrentFrame(frame)
                
    def mouseReleaseEvent(self, e):
        if self.dragging:
            self.dragging = False
                
        if self.selectedRangeStart != None:
            if self.selectedRangeEnd != None:
                start = min(self.selectedRangeStart, self.selectedRangeEnd)
                end = max(self.selectedRangeStart, self.selectedRangeEnd)
                self.shotTimeline.cinematicEditorTimeline.timelineSlider.setRange(start, end)
            
            self.selectedRangeStart = None
            self.selectedRangeEnd = None
            
            self.update()
                
    def paintEvent(self, e):
        if self.frameStep == None:
            return
        
        painter = QtGui.QPainter(self)
        rect = e.rect()
        height = self.height()
        
        if self.selectedRangeStart != None and self.selectedRangeEnd != None:
            start = min(self.selectedRangeStart, self.selectedRangeEnd) * self.pixelsPerFrame
            end = max(self.selectedRangeStart, self.selectedRangeEnd) * self.pixelsPerFrame
            painter.fillRect(QtCore.QRect(start, 0, end - start, height), self.selectedRangeColor)
        
        painter.setPen(self.frameColor)
        startFrame = int(rect.x() / self.pixelsPerFrame)
        endFrame = startFrame + rect.width() / self.pixelsPerFrame
        
        frame = startFrame - startFrame % self.frameStep
        width = self.width()
        while True:
            x = frame * self.pixelsPerFrame
            if x >= width:
                x = width - 1
            painter.fillRect(QtCore.QRect(x, 4, 2, height - 4), self.frameColor)
            painter.drawText(QtCore.QRect(x + 3, -2, 30, height), QtCore.Qt.AlignLeft, str(frame))

            if frame > endFrame:
                break
            frame += self.frameStep


class CurrentFrameIndicator(QtWidgets.QWidget):
    
    class CurrentFrameIndicatorDisplayMode(object):
        
        color = QtGui.QColor.fromRgb(192, 0, 0)
        textColor = QtCore.Qt.white
        
        def __init__(self):
            self.indicator = None
            
        def getText(self):
            return str(self.indicator.cutsceneFrame)
        
        def getLineColor(self):
            return self.color
        
        def getBackgroundColor(self):
            return self.color
        
        def getTextColor(self):
            return self.textColor
        
        def isPositionRefreshedByTime(self):
            return True
    
    
    class CurrentTimeIndicatorDisplayMode(CurrentFrameIndicatorDisplayMode):
        
        color = QtGui.QColor.fromRgb(0, 255, 255)
            
        def getText(self):
            return str(int(cmds.currentTime(q=True)))
        
        def isPositionRefreshedByTime(self):
            return False
    
    
    class DraggingShotIndicatorDisplayMode(CurrentFrameIndicatorDisplayMode):
        
        color = QtGui.QColor.fromRgb(0, 255, 255)
        
        def __init__(self, draggingShot):
            CurrentFrameIndicator.CurrentFrameIndicatorDisplayMode.__init__(self)
            
            self.draggingShot = draggingShot
            
        def getText(self):
            return self.draggingShot.shotName
        
        def getBackgroundColor(self):
            return CinematicEditorUtils.tupleAsColor(self.draggingShot.color)
        
        def isPositionRefreshedByTime(self):
            return False
    
    
    def __init__(self, shotTimeline, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        
        self.cinematicFrameMode = CurrentFrameIndicator.CurrentFrameIndicatorDisplayMode()
        self.cinematicFrameMode.indicator = self
        
        self.shotTimeline = shotTimeline
        
        self.cutsceneFrame = 0
        self.displayMode = self.cinematicFrameMode
        
        self.setFixedWidth(120)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)
        
    def setDisplayMode(self, mode):
        if mode == None:
            mode = self.cinematicFrameMode
        self.displayMode = mode
        mode.indicator = self
        self.refreshPosition()
        
    def setIndicatorPosition(self, pos):
        self.move(QtCore.QPoint(pos - self.width() / 2, 0))
        
    def refreshPosition(self, time=None, preferredShot=None):
        if self.displayMode.isPositionRefreshedByTime():
            cutscene = CinematicEditor.getCutscene()
            if cutscene == None:
                duration = 0
            else:
                if time == None:
                    time = cmds.currentTime(q=True)
                if preferredShot == None:
                    preferredShot = self.shotTimeline.cinematicEditorTimeline.getCurrentShot()
                
                shots = self.shotTimeline.cinematicEditorTimeline.getShotsToDisplay()
                cutsceneFrame = cutscene.getCutsceneFrameFromAnimationFrame(time, preferredShot=preferredShot, shots=shots)
                if cutsceneFrame == None:
                    currentShot = self.shotTimeline.cinematicEditorTimeline.getCurrentShot()
                    if currentShot != None:
                        shotCutsceneFrame = currentShot.getCutscene().getCutsceneFrameFromShot(currentShot)
                        if time <= currentShot.start:
                            cutsceneFrame = shotCutsceneFrame
                        else:
                            cutsceneFrame = shotCutsceneFrame + currentShot.getDuration()
                    else:
                        cutsceneFrame = 0
                            
                self.cutsceneFrame = int(cutsceneFrame)
                duration = cutscene.getTotalDuration(shots=shots)
            
            if duration == 0:
                self.move(-self.width() / 2, 0)
            else:
                self.move((self.parent().width() * cutsceneFrame) / duration - self.width() / 2, 0)
            self.update()   # The "move" method will not fire an update if there are so many frames on the cutscene that it doesn't actually move, but we still need it to repaint the right frame
        
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        
        halfWidth = self.width() / 2
        rectEnd = e.rect().right()
        
        indicatorWidth = 4
        if e.rect().left() <= halfWidth + indicatorWidth and rectEnd >= halfWidth - 2:
            painter.fillRect(QtCore.QRect(max(min(halfWidth, rectEnd - 2), halfWidth - 2), 10, indicatorWidth, self.height() - 10), self.displayMode.getLineColor())
        
        textHeight = 14
        if e.rect().y() <= textHeight:  # This paint method will be called when hovering over a Shot Widget. We only need to draw the low part of the widget in that case.
            text = self.displayMode.getText()
            textWidth = 5 + 6 * len(text)
            
            textRect = QtCore.QRect(max(min(halfWidth, rectEnd - textWidth), halfWidth - textWidth), 0, textWidth, textHeight)

            path = QtGui.QPainterPath()
            path.addRoundedRect(textRect, 3, 3)
            painter.fillPath(path, self.displayMode.getBackgroundColor())
            
            painter.setPen(QtCore.Qt.black)
            painter.drawText(textRect.translated(1, -1), QtCore.Qt.AlignCenter, text)
            painter.setPen(self.displayMode.getTextColor())
            painter.drawText(textRect.translated(0, -2), QtCore.Qt.AlignCenter, text)


class ShotWidget(QtWidgets.QPushButton):
    
    class ShotRangeDraggableButton(DragableButton):
        
        def __init__(self, shotWidget, isEnd=False):
            DragableButton.__init__(self)
            
            self.shotWidget = shotWidget
            self.isEnd = isEnd
            
            self.setMinimumWidth(1)
            self.setMaximumWidth(50)
            self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            
            self.moved.connect(self.onMoved)
            self.cancelled.connect(self.onCancelled)
            
        def mousePressEvent(self, e):
            if e.button() == QtCore.Qt.LeftButton:
                if not (e.modifiers() & ShotTimeline.EDIT_MODE_MODIFIER):
                    e.ignore()
                    return False
                    
                self.shotWidget.shotTimeline.currentFrameIndicator.setDisplayMode(CurrentFrameIndicator.CurrentTimeIndicatorDisplayMode())
                self.onMoved(QtCore.QPoint())
                
            return DragableButton.mousePressEvent(self, e)
                
        def onMoved(self, distance):
            shot = self.shotWidget.shot
            frame = shot.end if self.isEnd else shot.start
            frame += int(distance.x() * shot.getDuration() / float(self.shotWidget.width()))
            
            if self.isEnd:
                if frame <= shot.start:
                    frame = shot.start + 1
            else:
                if frame >= shot.end:
                    frame = shot.end - 1
            
            cmds.currentTime(frame, e=True)
            
            pos = self.shotWidget.pos().x() + self.shotWidget.width() * (frame - shot.start) / float(shot.getDuration())
            self.shotWidget.shotTimeline.currentFrameIndicator.setIndicatorPosition(pos)
            
        def onCancelled(self):
            self.shotWidget.shotTimeline.currentFrameIndicator.setDisplayMode(None)
                
        def mouseReleaseEvent(self, e):
            if self.pressedPosition != None:
                self.shotWidget.shotTimeline.currentFrameIndicator.setDisplayMode(None)
                
                currentTime = cmds.currentTime(q=True)
                shotTable = self.shotWidget.shotTimeline.cinematicEditorTimeline.mainWindow.shotTable
                if self.isEnd:
                    shotTable.onRangeEndChanged(self.shotWidget.shot, currentTime)
                else:
                    shotTable.onRangeStartChanged(self.shotWidget.shot, currentTime)
                
            return DragableButton.mouseReleaseEvent(self, e)
    
    labelStyle = "QLabel { foreground-color: white; border-radius: 3px; background-color: rgba(0, 0, 0, 64); }"
    dragButtonLeftActiveStyle = "QPushButton { border: 0px; background-color: rgba(255, 255, 255, 64); } QPushButton:hover{ border-left: 3px solid cyan; background-color: rgba(255, 255, 255, 64); } QPushButton:pressed{ border-left: 3px solid cyan; background-color: rgba(0, 0, 0, 64); }"
    dragButtonRightActiveStyle = "QPushButton { border: 0px; background-color: rgba(255, 255, 255, 64); } QPushButton:hover{ border-right: 3px solid cyan; background-color: rgba(255, 255, 255, 64); } QPushButton:pressed{ border-right: 3px solid cyan; background-color: rgba(0, 0, 0, 64); }"
    dragButtonInactiveStyle = "QPushButton { border: 0px; }"
    
    defaultCursor = QtGui.QCursor()
    reorderCursor = QtGui.QCursor(QtCore.Qt.SizeHorCursor)
    dragLeftCursor = QtGui.QCursor(QtGui.QPixmap(":/scale_left.png"))
    dragRightCursor = QtGui.QCursor(QtGui.QPixmap(":/scale_right.png"))
    
    shotTimelineHelpSuffix = "<p><b>Click</b>: Select Shot<br><b>Ctrl+Click</b>: Multi Selection<br><b>Double-Click</b>: Zoom Shot Timeline on Shot<br><b>Shift+Click</b>: Shot Manipulation (drag to move or resize)</p>"

    overlapWidth = 4
    borderWidth = 2
    
    notOwnedColor = QtGui.QColor.fromRgb(255, 128, 128)
    
    def __init__(self, shotTimeline, shot):
        QtWidgets.QPushButton.__init__(self, parent=None)
        
        self.shotTimeline = shotTimeline
        self.shot = shot
        
        self._pressed = False
        self._hover = False
        
        self.dragging = False
        self.draggingTargetIndex = None
        
        self.hasOverlaps = False
        self.selected = False
        
        self.backgroundColor = None
        self.backgroundColorLight = None
        self.backgroundColorDark = None
        self.borderColor = None
        
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setMinimumWidth(1)
        
        self.tooSmallLabel = QtWidgets.QLabel("...")
        self.tooSmallLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tooSmallLabel.setStyleSheet(self.labelStyle)
        self.tooSmallLabel.setMargin(1)
        
        self.shotNameLabel = QtWidgets.QLabel()
        self.shotNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shotNameLabel.setStyleSheet(self.labelStyle)
        self.shotNameLabel.setMargin(1)
        
        self.shotNameAndCameraLabel = QtWidgets.QLabel()
        self.shotNameAndCameraLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shotNameAndCameraLabel.setStyleSheet(self.labelStyle)
        self.shotNameAndCameraLabel.setMargin(1)
        
        self.startFrameLabel = QtWidgets.QLabel()
        self.startFrameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startFrameLabel.setStyleSheet(self.labelStyle)
        self.startFrameLabel.setMargin(1)
        
        self.endFrameLabel = QtWidgets.QLabel()
        self.endFrameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.endFrameLabel.setStyleSheet(self.labelStyle)
        self.endFrameLabel.setMargin(1)
        
        stackedLayout = QtWidgets.QStackedLayout()
        stackedLayout.setContentsMargins(0, 0, 0, 0)
        stackedLayout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
        
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setSpacing(0)
        
        self.labelLayout = QtWidgets.QHBoxLayout()
        self.labelLayout.setContentsMargins(self.overlapWidth, self.overlapWidth, self.overlapWidth, self.overlapWidth)
        self.labelLayout.setSpacing(3)
        
        self.leftDragButton = ShotWidget.ShotRangeDraggableButton(self)
        self.leftDragButton.setStyleSheet(self.dragButtonInactiveStyle)
        
        self.rightDragButton = ShotWidget.ShotRangeDraggableButton(self, isEnd=True)
        self.rightDragButton.setStyleSheet(self.dragButtonInactiveStyle)
        
        verticalWidget = QtWidgets.QWidget()
        horizontalWidget = QtWidgets.QWidget()
        
        self.setLayout(stackedLayout)
        
        horizontalWidget.setLayout(horizontalLayout)
        verticalWidget.setLayout(verticalLayout)
        stackedLayout.addWidget(horizontalWidget)
        stackedLayout.addWidget(verticalWidget)
        
        horizontalLayout.addWidget(self.leftDragButton, 20)
        horizontalLayout.addStretch(80)
        horizontalLayout.addWidget(self.rightDragButton, 20)
        
        verticalLayout.addStretch()
        verticalLayout.addLayout(self.labelLayout)
        verticalLayout.addStretch()
        
        self.labelLayout.addWidget(self.startFrameLabel)
        self.labelLayout.addStretch()
        self.labelLayout.addWidget(self.tooSmallLabel)
        self.labelLayout.addWidget(self.shotNameLabel)
        self.labelLayout.addWidget(self.shotNameAndCameraLabel)
        self.labelLayout.addStretch()
        self.labelLayout.addWidget(self.endFrameLabel)
        
        self.clicked.connect(self.selectShot)
    
    def refresh(self):
        self.refreshShotData()
    
    def refreshShotData(self):
        shotName = self.shot.shotName
        shotCamera = self.shot.camera or "<No Camera>"
        color = CinematicEditorUtils.tupleAsColor(self.shot.color) if self.shot.color != None else QtCore.Qt.black
            
        shotOverlaps = self.shot.getCutscene().getShotOverlaps(self.shot)
        
        masterFile = self.shotTimeline.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile
        if masterFile:
            self.owned = masterFile.ownsShot(self.shot)
            shotOverlaps = [shot for shot in shotOverlaps if masterFile.ownsShot(shot)] if self.owned else []
            if not self.owned:
                color = QtGui.QColor(QtCore.Qt.gray)
        else:
            self.owned = True
        
        self.hasOverlaps = len(shotOverlaps) > 0
        
        self.backgroundColor = color
        self.backgroundColorLight = self.backgroundColor.lighter(120)
        self.backgroundColorDark = self.backgroundColor.darker(120)
        
        start = float(self.shot.start)  # The conversion to float is unnecessary, but is safer if the shot range becomes an integer eventually
        if start.is_integer():
            start = int(start)
        end = float(self.shot.end)
        if end.is_integer():
            end = int(end)
        
        shotNameText = " {} ".format(shotName)
        shotNameAndCameraText = " {} ({}) ".format(shotName, shotCamera if self.owned else ("<DELEGATED>"))
        startFrameLabelText = " {} ".format(start)
        endFrameLabelText =  " {} ".format(end)
        
        # Changing the range will resize the widget, which will trigger the resizeEvent thus calling the updateDisplayedLabels.
        # But if we change the camera or the shot name, we need to call the funcion manually.
        updateLabels = shotNameAndCameraText != self.shotNameAndCameraLabel.text()
        
        self.shotNameLabel.setText(shotNameText)
        self.shotNameAndCameraLabel.setText(shotNameAndCameraText)
        self.startFrameLabel.setText(startFrameLabelText)
        self.endFrameLabel.setText(endFrameLabelText)
        
        self.setToolTip(CinematicEditorUtils.getShotTooltip(self.shot, suffix=self.shotTimelineHelpSuffix, shotOverlaps=shotOverlaps, owned=self.owned))
        
        if updateLabels:
            self.updateDisplayedLabels()
        
        self.refreshCurrentFrame()
     
    def refreshSelected(self, selectedShots):
        if self.shot in selectedShots:
            self.selected = len(selectedShots) > 1 or self.shot != self.shotTimeline.cinematicEditorTimeline.getCurrentShot()
        else:
            self.selected = False
        
        self.update()
    
    def updateDisplayedLabels(self):
        self.tooSmallLabel.setVisible(False)
        self.shotNameLabel.setVisible(False)
        self.shotNameAndCameraLabel.setVisible(False)
        self.startFrameLabel.setVisible(False)
        self.endFrameLabel.setVisible(False)
        
        margins = self.labelLayout.contentsMargins()
        maxWidth = self.width() - margins.left() - margins.right()
        fontMetrics = self.shotNameLabel.fontMetrics()
        if fontMetrics.width(self.tooSmallLabel.text()) <= maxWidth:
            shotNameTextWidth = fontMetrics.width(self.shotNameLabel.text())
            if shotNameTextWidth <= maxWidth:
                self.shotNameLabel.setVisible(True)
                frameLabelWith = self.startFrameLabel.fontMetrics().width(self.startFrameLabel.text()) + self.endFrameLabel.fontMetrics().width(self.endFrameLabel.text()) + 2 * self.labelLayout.spacing()
                if shotNameTextWidth + frameLabelWith <= maxWidth:
                    self.startFrameLabel.setVisible(self.owned)
                    self.endFrameLabel.setVisible(self.owned)
                    
                    if fontMetrics.width(self.shotNameAndCameraLabel.text()) + frameLabelWith <= maxWidth:
                        self.shotNameLabel.setVisible(False)
                        self.shotNameAndCameraLabel.setVisible(True)
            else:
                self.tooSmallLabel.setVisible(True)
    
    def refreshCurrentFrame(self, frameOverlaps=None):
        if not self.owned:
            self.borderColor = None
        elif frameOverlaps != None and len(frameOverlaps) > 1 and self.shot in frameOverlaps:
            self.borderColor = QtCore.Qt.yellow
        elif self.shot == self.shotTimeline.cinematicEditorTimeline.getCurrentShot():
            self.borderColor = QtCore.Qt.white
        else:
            self.borderColor = None
            
        self.update()
    
    def isMaster(self):
        if self.shotTimeline.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile:
            return self.shotTimeline.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile.isMaster()
        else:
            return True
    
    def canEditShot(self):
        if self.shotTimeline.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile:
            return self.shotTimeline.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile.ownsShot(self.shot)
        else:
            return True
    
    def selectShot(self, applyShotRange=None, applyShotCamera=True, selectOnTable=True, multiSelection=None):
        if selectOnTable and multiSelection == None:
            multiSelection = cmds.getModifiers() & ShotTimeline.SELECT_MODE_MODIFIER_MAYA
        self.shotTimeline.cinematicEditorTimeline.setCurrentShot(self.shot, applyShotRange=applyShotRange, goTo=Shot.goToClamp, applyShotCamera=applyShotCamera, selectOnTable=selectOnTable, multiSelection=multiSelection)
        
    def mousePressEvent(self, e):            
        if e.button() == QtCore.Qt.LeftButton:
            self._pressed = True
            
            if self.isMaster() and (e.modifiers() & ShotTimeline.EDIT_MODE_MODIFIER):
                self.dragging = True
                self.shotTimeline.currentFrameIndicator.setDisplayMode(CurrentFrameIndicator.DraggingShotIndicatorDisplayMode(self.shot))
        
        elif e.button() == QtCore.Qt.RightButton:            
            if self.dragging:
                self.draggingTargetIndex = None
                self.mouseReleaseEvent(e)
            
            else:
                self.selectShot(applyShotRange=None, applyShotCamera=False, selectOnTable=False)
                self.onHoverExit()
                self.shotTimeline.cinematicEditorTimeline.mainWindow.shotTable.showContextMenuForShot(self.shot, parent=self)
                
        QtWidgets.QPushButton.mousePressEvent(self, e)
        
    def mouseMoveEvent(self, e):
        if self._pressed and self.dragging:
            if not self.isMaster():
                raise AssertionError("Only the Master can reorder Shots!")
            
            offset = (self.pos() + e.pos()).x()
            parentLayout = self.parent().layout()
            self.draggingTargetIndex = -1
            prevWidget = None
            for i in range(parentLayout.count()):
                widget = parentLayout.itemAt(i).widget()
                if widget.pos().x() + widget.width() / 2 > offset:
                    self.draggingTargetIndex = i
                    break
                prevWidget = widget
                
            if prevWidget == self:
                self.draggingTargetIndex -= 1
                
            if self.draggingTargetIndex == -2:
                self.draggingTargetIndex = parentLayout.count() - 1
                lastWidget = parentLayout.itemAt(self.draggingTargetIndex).widget()
                targetPos = lastWidget.pos().x()
            elif self.draggingTargetIndex == -1:
                self.draggingTargetIndex = parentLayout.count()
                lastWidget = parentLayout.itemAt(self.draggingTargetIndex - 1).widget()
                targetPos = lastWidget.pos().x() + lastWidget.width()
            else:
                widget = parentLayout.itemAt(self.draggingTargetIndex).widget()
                targetPos = widget.pos().x()
            
            self.shotTimeline.currentFrameIndicator.setIndicatorPosition(targetPos)
            
    def mouseReleaseEvent(self, e):        
        if self._pressed and self.dragging:
            if self.draggingTargetIndex != None:
                with UndoContext("Reorder Shots"):
                    cutscene = CinematicEditor.getCutscene()
                    if self.draggingTargetIndex > cutscene.getShots().index(self.shot):
                        self.draggingTargetIndex -= 1
                    cutscene.removeShot(self.shot, disableAllActors=False)
                    cutscene.insertShot(self.shot, self.draggingTargetIndex, enableAllActors=False)
                        
            self.dragging = False
            self.draggingTargetIndex = None
            
            self.shotTimeline.currentFrameIndicator.setDisplayMode(None)
            self.shotTimeline.cinematicEditorTimeline.mainWindow.reload()
            
        self._pressed = False
        
        QtWidgets.QPushButton.mouseReleaseEvent(self, e)
        
    def mouseDoubleClickEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton and e.modifiers() == QtCore.Qt.NoModifier:
            startCinematicFrame = self.shot.getCutscene().getCutsceneFrameFromShot(self.shot)
            self.shotTimeline.cinematicEditorTimeline.timelineSlider.setRange(startCinematicFrame, startCinematicFrame + self.shot.getDuration())
        
        QtWidgets.QPushButton.mouseDoubleClickEvent(self, e)
        
    def resizeEvent(self, e):
        self.updateDisplayedLabels()
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        rect = self.rect()
        
        # This will add a border on the side of each ShotWidget.
        # Using the layout spacing is not a good idea since it will mess with the layout's stretch.
        rect.adjust(1, 0, -1, 0)
        
        if self._pressed:
            backgroundColor = self.backgroundColorDark
        elif self._hover:
            backgroundColor = self.backgroundColorLight
        else:
            backgroundColor = self.backgroundColor
        
        path = QtGui.QPainterPath()
        path.addRoundedRect(rect, 3, 3)
        
        if self.selected:
            borderColor = QtCore.Qt.blue
        elif self.borderColor != None:
            borderColor = self.borderColor
        else:
            borderColor = None
            
        if borderColor != None:
            painter.fillPath(path, borderColor)
            path = QtGui.QPainterPath()
            path.addRoundedRect(rect.adjusted(self.borderWidth, self.borderWidth, -self.borderWidth, -self.borderWidth), 3, 3)
        
        if self.hasOverlaps:
            painter.fillPath(path, QtCore.Qt.red)
            path = QtGui.QPainterPath()
            path.addRoundedRect(rect.adjusted(self.overlapWidth, self.overlapWidth, -self.overlapWidth, -self.overlapWidth), 3, 3)
        
        elif not self.owned:
            painter.fillPath(path, self.notOwnedColor)
            path = QtGui.QPainterPath()
            path.addRoundedRect(rect.adjusted(self.overlapWidth, self.overlapWidth, -self.overlapWidth, -self.overlapWidth), 3, 3)
        
        painter.fillPath(path, backgroundColor)
        
        if self.hasOverlaps:
            painter.fillPath(path, QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.BDiagPattern))

    def setActiveState(self, active):
        if active and self.isMaster():
            self.setCursor(self.reorderCursor)
        else:
            self.setCursor(self.defaultCursor)
        
        if active and self.canEditShot():
            self.leftDragButton.setCursor(self.dragLeftCursor)
            self.leftDragButton.setStyleSheet(self.dragButtonLeftActiveStyle)
            self.leftDragButton.setVisible(True)
            self.rightDragButton.setCursor(self.dragRightCursor)
            self.rightDragButton.setStyleSheet(self.dragButtonRightActiveStyle)
            self.rightDragButton.setVisible(True)
        else:
            if not self.leftDragButton.isPressed():
                self.leftDragButton.setCursor(self.defaultCursor)
                self.leftDragButton.setStyleSheet(self.dragButtonInactiveStyle)
                self.leftDragButton.setVisible(False)
            if not self.rightDragButton.isPressed():
                self.rightDragButton.setCursor(self.defaultCursor)
                self.rightDragButton.setStyleSheet(self.dragButtonInactiveStyle)
                self.rightDragButton.setVisible(False)
            
        self.leftDragButton.update()
        self.rightDragButton.update()

    def keyPressEvent(self, e):
        if e.key() == ShotTimeline.EDIT_MODE_KEY:
            self.setActiveState(True)
            
        elif e.key() == QtCore.Qt.Key_Escape:   # When grabbing the keyboard, the Esc key will close the window. This will prevent it.
            return True
        
        e.ignore()
        return False

    def keyReleaseEvent(self, e):
        if e.key() == ShotTimeline.EDIT_MODE_KEY:
            self.setActiveState(False)
        
        e.ignore()
        return False

    def onHoverEnter(self, active=False):
        self._hover = True
        self.grabKeyboard()
        self.setActiveState(active)
        
    def onHoverExit(self):
        self._hover = False
        self.releaseKeyboard()
        self.setActiveState(False)

    def event(self, e):
        if e.type() == e.HoverEnter:
            self.onHoverEnter(active=(e.modifiers() & ShotTimeline.EDIT_MODE_MODIFIER))
        elif e.type() == e.HoverLeave:
            self.onHoverExit()
        
        return QtWidgets.QPushButton.event(self, e)


class ShotTimeline(QtWidgets.QWidget):
    
    EDIT_MODE_MODIFIER = QtCore.Qt.ShiftModifier
    EDIT_MODE_KEY = QtCore.Qt.Key_Shift
    
    SELECT_MODE_MODIFIER_MAYA = 4   # Code for the Control Key on Maya
    
    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------
    
    def __init__(self, cinematicEditorTimeline, parent):
        QtWidgets.QWidget.__init__(self, parent=parent)
        
        self.cinematicEditorTimeline = cinematicEditorTimeline
        
        self.shotWidgets = []
        
        self.frameOverlaps = []
        
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
        # Frame Painter
        self.rangePainter = TimelineRangePainter(self)
        layout.addWidget(self.rangePainter)
        
        # Shot Container
        self.shotContainerLayout = QtWidgets.QHBoxLayout()
        self.shotContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.shotContainerLayout.setSpacing(0)
        shotContainer = QtWidgets.QWidget()
        shotContainer.setLayout(self.shotContainerLayout)
        layout.addWidget(shotContainer)
        
        # Current Frame Indicator
        self.currentFrameIndicator = CurrentFrameIndicator(self)
        layout.addChildWidget(self.currentFrameIndicator)
        
        # This widget is floating under it's parent, and not inside a layout, so we set our parent's minimum size instead of ours.
        parent.setMinimumWidth(150)
        parent.setMinimumHeight(25 + self.rangePainter.minimumHeight())
    
    def reload(self):
        while self.shotContainerLayout.count() > 0:
            self.shotContainerLayout.takeAt(0).widget().deleteLater()   # TakeAt removes the widget from the layout and deleteLater deletes it.
        self.shotWidgets = []
        
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            shots = self.cinematicEditorTimeline.getShotsToDisplay()
            for shot in shots:
                shotWidget = ShotWidget(self, shot)
                self.shotContainerLayout.addWidget(shotWidget)
                self.shotWidgets.append(shotWidget)
            
        self.refresh()

    def refresh(self):
        self.refreshTimelinePosition()

    def refreshTimelinePosition(self):
        self.cinematicEditorTimeline.timelineSlider.updateCutsceneDuration(emitSignal=False)
        
        rangeStart = self.cinematicEditorTimeline.timelineSlider.getRangeStart()
        rangeEnd = self.cinematicEditorTimeline.timelineSlider.getRangeEnd()
        rangeMinimum = self.cinematicEditorTimeline.timelineSlider.getRangeMinimum()
        rangeMaximum = self.cinematicEditorTimeline.timelineSlider.getRangeMaximum()
        
        margin = 1
        totalWidth = self.parent().width() - 2 * margin
        totalHeight = self.parent().height() - 2 * margin
        
        duration = float(rangeMaximum - rangeMinimum)
        if duration == 0:
            finalWidth = totalWidth
            offset = 0
        else:
            finalWidth = totalWidth * duration /  (rangeEnd - rangeStart)
            offset = finalWidth * (rangeStart - rangeMinimum) / duration
        
        self.move(margin - offset, margin)
        self.resize(finalWidth, totalHeight)
        
        for i, shotWidget in enumerate(self.shotWidgets):
            self.shotContainerLayout.setStretch(i, shotWidget.shot.getDuration())
            
        self.refreshShotData()
        self.refreshCurrentFrame()

    def refreshShotData(self):
        self.rangePainter.refreshRange()
        
        for shotWidget in self.shotWidgets:
            shotWidget.refreshShotData()

    def refreshCurrentFrame(self, shots=None, time=None):
        if time == None:
            time = cmds.currentTime(q=True)
        
        self.currentFrameIndicator.refreshPosition(time=time)
        
        newFrameOverlaps = []
        if not cmds.isTrue("playingBack"):
            cutscene = CinematicEditor.getCutscene()
            if cutscene != None:
                newFrameOverlaps = cutscene.getShotsAtTime(time)
        
        masterFile = self.cinematicEditorTimeline.mainWindow.cachedMasterSlaveFile
        if masterFile:
            if masterFile.ownsShot(self.cinematicEditorTimeline.getCurrentShot()):
                newFrameOverlaps = [shot for shot in newFrameOverlaps if masterFile.ownsShot(shot)]
            else:
                newFrameOverlaps = []
            
        if shots != None:
            shots = set(shots)
            shots = shots.union(newFrameOverlaps)
            shots = shots.union(self.frameOverlaps)
            shotWidgetsToRefresh = [shotWidget for shotWidget in self.shotWidgets if shotWidget.shot in shots]
        else:
            shotWidgetsToRefresh = self.shotWidgets
            
        self.frameOverlaps = newFrameOverlaps
        
        for shotWidget in shotWidgetsToRefresh:
            shotWidget.refreshCurrentFrame(frameOverlaps=newFrameOverlaps)

    def refreshSelectedShots(self, selectedShots):
        for shotWidget in self.shotWidgets:
            shotWidget.refreshSelected(selectedShots)

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def onResize(self):
        self.refreshTimelinePosition()

    def onRangeChanged(self, rangeStart, rangeEnd, rangeMinimum, rangeMaximum):
        self.refreshTimelinePosition()  # We don't use the values directly, instead we rely on a single method refreshTimelinePosition (which will read them from the timelineSlider)
