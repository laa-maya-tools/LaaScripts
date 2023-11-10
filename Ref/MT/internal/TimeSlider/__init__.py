import maya.cmds as cmds
import maya.mel as mel

import maya.OpenMayaUI as omui

from PySide2 import QtCore, QtGui, QtWidgets

import shiboken2

defaultTimeSlider = "TimeSlider|MainTimeSliderLayout|formLayout8|frameLayout2|timeControl1"
mainChannelBox = "mainChannelBox"

def refresh():
    cmds.timeControl(defaultTimeSlider, e=True, forceRefresh=True)

def getTimeSliderKeyTimes():
    animCurves = cmds.timeControl(defaultTimeSlider, q=True, acn=True)
    if not animCurves:
        return []
    
    start = cmds.playbackOptions(q=True, min=True)
    end = cmds.playbackOptions(q=True, max=True)
    keyTimes = cmds.keyframe(animCurves, q=True, tc=True, t=(start, end)) or []
    
    uniqueTimes = set(keyTimes)
    orederedTimes = list(uniqueTimes)
    orederedTimes.sort()
    
    return orederedTimes

def clearSelectedTimeSliderRange():
    app = QtWidgets.QApplication.instance()
    
    widgetStr = mel.eval('$gPlayBackSlider=$gPlayBackSlider')
    ptr = omui.MQtUtil.findControl(widgetStr)
    slider = shiboken2.wrapInstance(int(ptr), QtWidgets.QWidget)
    
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, 
                              QtCore.QPoint(0, 0), 
                              QtCore.Qt.RightButton, 
                              QtCore.Qt.RightButton, 
                              QtCore.Qt.ShiftModifier)
    app.sendEvent(slider, event)
    
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, 
                              QtCore.QPoint(0, 0), 
                              QtCore.Qt.RightButton, 
                              QtCore.Qt.RightButton, 
                              QtCore.Qt.ShiftModifier)
    app.sendEvent(slider, event)
    
    app.processEvents()

def selectTimeSliderRange(start, end):
    app = QtWidgets.QApplication.instance()
    
    widgetStr = mel.eval('$gPlayBackSlider=$gPlayBackSlider')
    ptr = omui.MQtUtil.findControl(widgetStr)
    slider = shiboken2.wrapInstance(int(ptr), QtWidgets.QWidget)
    
    slider_width = slider.size().width()
    slider_height = slider.size().height()
    
    # Store time slider settings
    min_time = cmds.playbackOptions(query=True, minTime=True)
    max_time = cmds.playbackOptions(query=True, maxTime=True)
    animation_start_time = cmds.playbackOptions(query=True, animationStartTime=True)
    animation_end_time = cmds.playbackOptions(query=True, animationEndTime=True)
    t = cmds.currentTime(query=True)
    
    # Set the time slider to the range we want so we have
    # perfect precision to click at the start and end of the
    # time slider.
    cmds.playbackOptions(minTime=start)
    cmds.playbackOptions(maxTime=end)
    
    a_pos = QtCore.QPoint(0, slider_height / 2.0)         
    b_pos = QtCore.QPoint(slider_width, slider_height / 2.0)
    
    # Trigger some mouse events on the Time Control
    # Somehow we need to have some move events around
    # it so the UI correctly understands it stopped
    # clicking, etc.
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove, 
                              a_pos, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.NoModifier)
    app.sendEvent(slider, event)
    
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, 
                              a_pos, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.ShiftModifier)
    app.sendEvent(slider, event)
   
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove, 
                              b_pos, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.ShiftModifier)
    app.sendEvent(slider, event)

    event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, 
                              b_pos, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.ShiftModifier)
    app.sendEvent(slider, event)
    
    event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove, 
                              b_pos, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.MouseButton.LeftButton, 
                              QtCore.Qt.NoModifier)
    app.sendEvent(slider, event)
    app.processEvents()
    
    # Reset time slider settings
    cmds.playbackOptions(minTime=min_time)
    cmds.playbackOptions(maxTime=max_time)
    cmds.playbackOptions(animationStartTime=animation_start_time)
    cmds.playbackOptions(animationEndTime=animation_end_time)
    cmds.currentTime(t)