from PySide2 import QtWidgets, QtGui, QtCore

import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaAnim as OpenMayaAnim

import maya.OpenMayaUI as OpenMayaUI    # The MQtUtil class seems to be present only on the 1.0 version of the API.

import TimeSlider
import TimeSlider.TimeSliderScrubCallback as TimeSliderScrubCallback

from Utils.Python.Versions import long

from shiboken2 import wrapInstance

import traceback

class TimeSliderPainter(object):

    TIME_AREA_MARGIN_LEFT = 6
    TIME_AREA_MARGIN_RIGHT = 10
    TIME_AREA_MARGIN_UP = 14
    TIME_AREA_MARGIN_DOWN = 16

    KEY_PAINTER_TICK_WIDTH = 8
    KEY_PAINTER_TIP_LENGTH = 8

    def __init__(self, enabled=True, overlay=None):
        self.overlay = overlay
        self.enabled = enabled

    def paint(self, painter, paintEvent):
        raise NotImplementedError()
    
    def onOverlayResized(self, size):
        pass

    def onSelectionChanged(self):
        pass

    def onAnimationRangeChanged(self):
        pass

    def onChannelBoxLabelSelected(self):
        pass
    
    def onSyncTimeSliderOptionChanged(self):
        pass

    def onAnimLayerDisplayOptionsChanged(self):
        pass

    def onAnimCurveEdited(self, animCurves):
        pass

    def onConnectionChanged(self, sourcePlug, destinationPlug, connectionMade):
        pass

    def onTimeSliderPressed(self):
        pass

    def onTimeSliderMoved(self, time):
        pass

    def onTimeSliderReleased(self):
        pass


class TimeSliderOverlay(QtWidgets.QWidget, TimeSliderScrubCallback.TimeSliderScrubCallback):
    
    @staticmethod
    def getTimeSliderWidget():
        timeSliderPointer = OpenMayaUI.MQtUtil.findControl(TimeSlider.defaultTimeSlider)
        return wrapInstance(long(timeSliderPointer), QtWidgets.QWidget)
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.timeSliderPainters = []
        
        self.isSelecting = False
        self.draggingOffset = None

    def registerTimeSliderPainter(self, timeSliderPainter):
        if timeSliderPainter in self.timeSliderPainters:
            return AssertionError("Unable to register painter: The provided painter is already registered! {}".format(timeSliderPainter))

        timeSliderPainter.overlay = self
        self.timeSliderPainters.append(timeSliderPainter)
        
        timeSliderPainter.onOverlayResized(self.size())

    def unregisterTimeSliderPainter(self, timeSliderPainter):
        if timeSliderPainter not in self.timeSliderPainters:
            return AssertionError("Unable to unregister painter: The provided painter is not registered! {}".format(timeSliderPainter))

        self.timeSliderPainters.remove(timeSliderPainter)
        timeSliderPainter.overlay = None
        
    def clearTimeSliderPainters(self):
        while len(self.timeSliderPainters) > 0:
            self.unregisterTimeSliderPainter(self.timeSliderPainters[-1])

    def paintEvent(self, event):
        try:
            painter = QtGui.QPainter(self)
            for timeSliderPainter in self.timeSliderPainters:
                if timeSliderPainter.enabled:
                    painter.save()
                    timeSliderPainter.paint(painter, event)
                    painter.restore()
        except:
            traceback.print_exc()
        finally:
            painter.end()

    def showEvent(self, event):
        self.registerCallbacks()

    def hideEvent(self, event):
        self.unregisterCallbacks()
    
    #region Mouse Events
    
    def getTimeFromPosition(self, x):
        start = cmds.playbackOptions(q=True, min=True)
        end = cmds.playbackOptions(q=True, max=True)
        p = (x - TimeSliderPainter.TIME_AREA_MARGIN_LEFT) / (self.width() - (TimeSliderPainter.TIME_AREA_MARGIN_LEFT + TimeSliderPainter.TIME_AREA_MARGIN_RIGHT))
        return int(start + (end - start + 1) * p)
        
    def getPositionFromTime(self, t):
        start = cmds.playbackOptions(q=True, min=True)
        end = cmds.playbackOptions(q=True, max=True)
        p = (t - start) / (end - start + 1)
        return  int(TimeSliderPainter.TIME_AREA_MARGIN_LEFT + (self.width() - (TimeSliderPainter.TIME_AREA_MARGIN_LEFT + TimeSliderPainter.TIME_AREA_MARGIN_RIGHT)) * p)
        
    def mouseDoubleClickEvent(self, event : QtGui.QMouseEvent):
        import MayaImprovements.TimeSliderFix as TimeSliderFix
        cancelDoubleClick = False
        if event.button() == QtCore.Qt.LeftButton:
            if event.modifiers() & QtCore.Qt.ShiftModifier:
                if TimeSliderFix.TimeSliderFix.isDisableDoubleClickSelectWithShiftEnabled():
                    cancelDoubleClick = True
            else:
                if TimeSliderFix.TimeSliderFix.isDisableDoubleClickSelectEnabled():
                    cancelDoubleClick = True
        
        if cancelDoubleClick:
            event.accept()
            
            app = QtWidgets.QApplication.instance()
            timeSliderWidget = self.getTimeSliderWidget()
            event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, event.pos(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, event.modifiers())
            app.sendEvent(timeSliderWidget, event)
            app.processEvents()
            
            return
        
        event.ignore()
        
    def mousePressEvent(self, event : QtGui.QMouseEvent):
        import MayaImprovements.TimeSliderFix as TimeSliderFix
        if event.button() == QtCore.Qt.LeftButton:
            if event.modifiers() & QtCore.Qt.ShiftModifier:
                self.isSelecting = True
                
                if TimeSliderFix.TimeSliderFix.isFixSelectNearCurrentSelectionEnabled():
                    TimeSlider.clearSelectedTimeSliderRange()
                    
            elif TimeSliderFix.TimeSliderFix.isMoveSelectedKeysClickingAnywhereEnabled() and cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeVisible=True):
                selectedRange = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeArray=True)
                clickedFrame = self.getTimeFromPosition(event.pos().x())
                if clickedFrame > selectedRange[0] and clickedFrame < selectedRange[1]:
                    middle = self.getPositionFromTime(selectedRange[0] + (selectedRange[1] - selectedRange[0]) / 2.0)
                    self.draggingOffset = middle - event.pos().x()
                
                    app = QtWidgets.QApplication.instance()
                    timeSliderWidget = self.getTimeSliderWidget()
                    event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, QtCore.QPoint(middle, event.pos().y()), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, event.modifiers())
                    app.postEvent(timeSliderWidget, event)
                    
                    event.accept()
                    return
                    
        event.ignore()
        
    def mouseMoveEvent(self, event : QtGui.QMouseEvent):
        import MayaImprovements.TimeSliderFix as TimeSliderFix
        if self.isSelecting:
            if TimeSliderFix.TimeSliderFix.isKeepSelectingIfShiftIsReleasedEnabled() and not (event.modifiers() & QtCore.Qt.ShiftModifier):
                event.setModifiers(event.modifiers() | QtCore.Qt.ShiftModifier)
                
        elif self.draggingOffset != None:
            app = QtWidgets.QApplication.instance()
            timeSliderWidget = self.getTimeSliderWidget()
            event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove, event.pos() + QtCore.QPoint(self.draggingOffset, 0), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, event.modifiers())
            app.sendEvent(timeSliderWidget, event)
            app.processEvents()
            
            event.accept()
            return
        
        else:
            if TimeSliderFix.TimeSliderFix.isStartSelectingIfShiftIsPressedEnabled() and (event.buttons() & QtCore.Qt.LeftButton) and (event.modifiers() & QtCore.Qt.ShiftModifier):
                self.isSelecting = True
                
                app = QtWidgets.QApplication.instance()
                timeSliderWidget = self.getTimeSliderWidget()
                event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, event.pos(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
                app.sendEvent(timeSliderWidget, event)
                event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, event.pos(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.ShiftModifier)
                app.sendEvent(timeSliderWidget, event)
                app.processEvents()
                
                event.accept()
                return
        
        event.ignore()
           
    def mouseReleaseEvent(self, event : QtGui.QMouseEvent):
        import MayaImprovements.TimeSliderFix as TimeSliderFix
        if self.isSelecting:
            if TimeSliderFix.TimeSliderFix.isKeepSelectingIfShiftIsReleasedEnabled() and not (event.modifiers() & QtCore.Qt.ShiftModifier):
                event.setModifiers(event.modifiers() | QtCore.Qt.ShiftModifier)
            
            self.isSelecting = False
            
        if self.draggingOffset != None:
            self.draggingOffset = None
        
        event.ignore()
        
    #endregion
        
    def resizeEvent(self, event):
        for timeSliderPainter in self.timeSliderPainters:
            timeSliderPainter.onOverlayResized(event.size())

    def registerCallbacks(self):
        self.selectionChangedCallback = cmds.scriptJob(e=("SelectionChanged", self.onSelectionChanged)) # The SelectionChanged callback doesn't seem to work properly on the API
        self.timelineSyncChangedCallback = cmds.scriptJob(ovc=("timeSliderShowKeys", self.onSyncTimeSliderOptionChanged))
        self.animLayerDisplayOptionsChangedCallback = cmds.scriptJob(ovc=("timeSliderAnimLayerOptions", self.onAnimLayerDisplayOptionsChanged))

        self.animationRangeChangedCallback = OpenMaya.MEventMessage.addEventCallback("playbackRangeChanged", self.onAnimationRangeChanged)
        self.channelBoxLabelSelectedCallback = OpenMaya.MEventMessage.addEventCallback("ChannelBoxLabelSelected", self.onChannelBoxLabelSelected)
        
        self.keyframeEditedCallback = OpenMayaAnim.MAnimMessage.addAnimCurveEditedCallback(self.onAnimCurveEdited)
        self.connectionChangedCallback = OpenMaya.MDGMessage.addConnectionCallback(self.onConnectionChanged)

        TimeSliderScrubCallback.TimeSliderScrubCallbackManager.registerCallback(self)

    def unregisterCallbacks(self):
        cmds.scriptJob(kill=self.selectionChangedCallback)
        cmds.scriptJob(kill=self.timelineSyncChangedCallback)
        cmds.scriptJob(kill=self.animLayerDisplayOptionsChangedCallback)

        OpenMaya.MMessage.removeCallback(self.animationRangeChangedCallback)
        OpenMaya.MMessage.removeCallback(self.channelBoxLabelSelectedCallback)

        OpenMaya.MMessage.removeCallback(self.keyframeEditedCallback)
        OpenMaya.MMessage.removeCallback(self.connectionChangedCallback)

        TimeSliderScrubCallback.TimeSliderScrubCallbackManager.unregisterCallback(self)

    def onSelectionChanged(self):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onSelectionChanged()

    def onAnimationRangeChanged(self, arg):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onAnimationRangeChanged()

    def onChannelBoxLabelSelected(self, arg):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onChannelBoxLabelSelected()
                
    def onSyncTimeSliderOptionChanged(self):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onSyncTimeSliderOptionChanged()

    def onAnimLayerDisplayOptionsChanged(self):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onAnimLayerDisplayOptionsChanged()

    def onAnimCurveEdited(self, animCurves, arg):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onAnimCurveEdited(animCurves)
                
    def onConnectionChanged(self, sourcePlug, destinationPlug, connectionMade, arg):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onConnectionChanged(sourcePlug, destinationPlug, connectionMade)

    def onTimeSliderPressed(self):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onTimeSliderPressed()

    def onTimeSliderMoved(self, time):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onTimeSliderMoved(time)

    def onTimeSliderReleased(self):
        for timeSliderPainter in self.timeSliderPainters:
            if timeSliderPainter.enabled:
                timeSliderPainter.onTimeSliderReleased()