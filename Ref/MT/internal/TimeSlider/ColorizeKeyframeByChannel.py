from PySide2 import QtCore, QtGui

import maya.cmds as cmds

import TimeSlider
import TimeSlider.TimeSliderOverlay as TimeSliderOverlay
import Utils.OpenMaya.AnimNodes as AnimNodeUtils

class ColorFilter(object):

    def __init__(self, enabled=True):
        self.enabled = enabled
        
    def onStart(self):
        pass

    def getKeyframeColorAndPriority(self, node, attribute, animCurve, keyTime, displayRange):
        return None, None


class AttributeColorFilter(ColorFilter):

    def __init__(self, attributes, color, priority, enabled=True, enableCoordinateColors=False, coordinateColors=None):
        ColorFilter.__init__(self, enabled=enabled)

        self.attributes = attributes
        self.color = color
        self.priority = priority
        
        self.enableCoordinateColors = enableCoordinateColors
        self.coordinateColors = coordinateColors
        self.useCoordinateColors = False
        
        if self.coordinateColors != None:
            for i, color in enumerate(self.coordinateColors):
                if issubclass(type(color), str):
                    rgb = cmds.displayRGBColor(color, q=True)
                    self.coordinateColors[i] = QtGui.QColor.fromRgb(255 * rgb[0], 255 * rgb[1], 255 * rgb[2])
            
    def shouldUseCoordinateColors(self):
        if self.enableCoordinateColors:
            displayedAnimCurves = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, animCurveNames=True) or []
            for animCurve in displayedAnimCurves:
                node, attr = AnimNodeUtils.getNodeAttributeFromAnimNode(animCurve)
                longName = cmds.attributeQuery(attr, node=node, longName=True)
                if longName not in self.attributes:
                    return False
            return True
        else:
            return False
        
    def onStart(self):
        self.useCoordinateColors = self.shouldUseCoordinateColors()

    def getKeyframeColorAndPriority(self, node, attribute, animCurve, keyTime, displayRange):
        if attribute in self.attributes:
            if self.useCoordinateColors:
                index = self.attributes.index(attribute)
                return self.coordinateColors[index], index
            else:
                return self.color, self.priority
        else:
            return None, None


class IKFKBlendColorFilter(ColorFilter):

    blendAttributes = set(["leg_blend", "arm_blend"])
    fkColor = QtGui.QColor(64, 156, 255)
    ikColor = QtGui.QColor(212, 212, 32)
    intermediateColor = QtGui.QColor(96, 212, 128)
    priority = 50

    def getKeyframeColorAndPriority(self, node, attribute, animCurve, keyTime, displayRange):
        if attribute in self.blendAttributes:
            blendValue = cmds.keyframe(animCurve, q=True, ev=True, t=(keyTime,keyTime))[0]
            if blendValue == 0:
                keyColor = self.fkColor
            elif blendValue == 1:
                keyColor = self.ikColor
            else:
                keyColor = self.intermediateColor
            return keyColor, self.priority
        else:
            return None, None


class DefaultColorFilter(ColorFilter):

    defaultKeyframeColor = QtGui.QColor(64, 64, 64)
    defaultKeyframeColorPriority = 100000000

    def getKeyframeColorAndPriority(self, node, attribute, animCurve, keyTime, displayRange):
        return self.defaultKeyframeColor, self.defaultKeyframeColorPriority


class ColorizeKeyframeByChannel(TimeSliderOverlay.TimeSliderPainter):

    def __init__(self, enabled=True):
        TimeSliderOverlay.TimeSliderPainter.__init__(self, enabled=enabled)

        self.colorFilters = []

        self.clean = False
        self.pixmap = None
        self.keyframeColors = {}

    def registerColorFilter(self, colorFilter):
        if colorFilter in self.colorFilters:
            return AssertionError("Unable to register filter: The provided filter is already registered! {}".format(colorFilter))

        self.colorFilters.append(colorFilter)

    def unregisterColorFilter(self, colorFilter):
        if colorFilter not in self.colorFilters:
            return AssertionError("Unable to unregister filter: The provided filter is not registered! {}".format(colorFilter))

        self.colorFilters.remove(colorFilter)

    def setDirty(self, dirty=True, update=False):
        self.clean = not dirty
        if update:
            self.overlay.update()
            
    def onOverlayResized(self, size):
        self.pixmap = QtGui.QPixmap(size.width(), size.height())
        self.setDirty()

    def onSelectionChanged(self):
        self.setDirty()

    def onAnimationRangeChanged(self):
        self.setDirty()

    def onChannelBoxLabelSelected(self):
        # We need the timeline to update if it is not synced to the channelbox (to update the previous value)
        update = cmds.optionVar(q="timeSliderShowKeys") != "mainChannelBox"
        self.setDirty(update=update)

    def onSyncTimeSliderOptionChanged(self):
        self.setDirty(update=True)  # We need the timeline to update here

    def onAnimLayerDisplayOptionsChanged(self):
        self.setDirty()

    def onAnimCurveEdited(self, animCurves):
        self.setDirty()
        
    def onConnectionChanged(self, sourcePlug, destinationPlug, connectionMade):
        self.setDirty()

    def getKeyframeColorAndPriority(self, node, attribute, animCurve, keyTime, displayRange):
        finalColor = None
        finalPriority = None
        for colorFilter in self.colorFilters:
            color, priority = colorFilter.getKeyframeColorAndPriority(node, attribute, animCurve, keyTime, displayRange)
            if color != None and (finalPriority == None or finalPriority > priority):
                if colorFilter.enabled: # If the filter is disabled, we still save the priority so other filters don't reclaim the key.
                    finalColor = color
                finalPriority = priority
        return finalColor, finalPriority

    def paint(self, painter, event):
        # If a new scene is being opened, we might retrieve animation curves for objects that no longer exist.
        if cmds.isTrue("opening") or cmds.isTrue("newing"):
            return

        rangeStart = cmds.playbackOptions(q=True, min=True)
        rangeEnd = cmds.playbackOptions(q=True, max=True)
        displayRange = (rangeStart, rangeEnd + 1) # The display range always shows the next to last frame as well
        displayRangeLength = displayRange[1] - displayRange[0]
        if cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeVisible=True):
            selectedRange = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeArray=True)
        else:
            selectedRange = None

        if not self.clean:
            self.keyframeColors = {}
            for colorFilter in self.colorFilters:
                colorFilter.onStart()
            displayedAnimCurves = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, animCurveNames=True) or []
            for animCurve in displayedAnimCurves:
                node, attribute = AnimNodeUtils.getNodeAttributeFromAnimNode(animCurve)
                displayedKeyTimes = cmds.keyframe(animCurve, q=True, time=displayRange) or []
                for keyTime in displayedKeyTimes:
                    if not keyTime in self.keyframeColors:
                        colors = {}
                        self.keyframeColors[keyTime] = colors
                    else:
                        colors = self.keyframeColors[keyTime]
                        
                    keyframeColor, colorPriority = self.getKeyframeColorAndPriority(node, attribute, animCurve, keyTime, displayRange)
                    if colorPriority != None and colorPriority not in colors:   # We check if the color priority is None. The color itself can be None, wich means that the keyframe should not be colored.
                        colors[colorPriority] = keyframeColor
        
        if not self.clean or self.previousSelectedRange != selectedRange:
            timeArea = QtCore.QRectF(self.overlay.rect())
            timeArea.setX(timeArea.x() + ColorizeKeyframeByChannel.TIME_AREA_MARGIN_LEFT)
            timeArea.setY(timeArea.y() + ColorizeKeyframeByChannel.TIME_AREA_MARGIN_UP)
            timeArea.setWidth(timeArea.width() - ColorizeKeyframeByChannel.TIME_AREA_MARGIN_RIGHT)
            timeArea.setHeight(timeArea.height() - ColorizeKeyframeByChannel.TIME_AREA_MARGIN_DOWN)

            timeToPixelFactor = timeArea.width() / displayRangeLength
            paintWidth = max(1, min(timeToPixelFactor - 1, ColorizeKeyframeByChannel.KEY_PAINTER_TICK_WIDTH))
            tickSize = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, tickSize=True)
            tipLength = max(0, min(ColorizeKeyframeByChannel.KEY_PAINTER_TIP_LENGTH, timeArea.height() - 16))

            self.pixmap.fill(QtCore.Qt.transparent)
            
            pixmapPainter = QtGui.QPainter(self.pixmap)
            pixmapPainter.setRenderHint(pixmapPainter.Antialiasing)
            for keyTime, colors in self.keyframeColors.items():
                orderedPriorities = list(colors.keys())
                orderedPriorities.sort()
                colors = [colors[priority] for priority in orderedPriorities if colors[priority] != None]
                if len(colors) == 0:
                    continue

                if selectedRange != None and keyTime >= selectedRange[0] and keyTime < selectedRange[1]:
                    pixmapPainter.setPen(QtCore.Qt.yellow)
                else:
                    pixmapPainter.setPen(QtCore.Qt.black)

                horizontalOffset = timeArea.x() + (keyTime - rangeStart) * timeToPixelFactor + tickSize
                heightPerColor = float(timeArea.height() - tipLength) / len(colors)
                for i, color in enumerate(colors):
                    verticalOffset = timeArea.y() + i * heightPerColor
                    if i < len(colors) - 1:
                        pixmapPainter.fillRect(horizontalOffset + 0.5, verticalOffset, paintWidth, heightPerColor, color)
                        if paintWidth >= 3:
                            pixmapPainter.drawRect(horizontalOffset + 0.5, verticalOffset, paintWidth, heightPerColor)
                    else:
                        path = QtGui.QPainterPath(QtCore.QPointF(horizontalOffset, verticalOffset))
                        path.lineTo(horizontalOffset + paintWidth, verticalOffset)
                        path.lineTo(horizontalOffset + paintWidth, verticalOffset + heightPerColor)
                        path.lineTo(horizontalOffset, timeArea.y() + timeArea.height())
                        path.closeSubpath()
                        pixmapPainter.fillPath(path, color)
                        if paintWidth >= 3:
                            pixmapPainter.strokePath(path, pixmapPainter.pen())
            pixmapPainter.end()
        
        self.previousSelectedRange = selectedRange              
        self.clean = True

        if self.pixmap != None:
            painter.drawPixmap(self.overlay.rect(), self.pixmap)
