from PySide2 import QtCore, QtWidgets, QtGui

from QtCustomWidgets.DragableButton import DragableButton

class RangeSlider(QtWidgets.QWidget):
    
    rangeBarStyle = "QPushButton { border-style: solid; border-width: 1px; border-radius:3px; border-color: #5d5d5d; background-color: #5d5d5d; }"
    rangeSliderStyle = "QPushButton { border-style: solid; border-width: 1px; border-radius:3px; border-color: #919191; background-color: #919191; } QPushButton:pressed { background-color: #373737; }"
    rangeLabelStyle = "QLabel { color: #c6c6c6; background-color: #5d5d5d; }"
    
    rangeChanged = QtCore.Signal(int, int, int, int)
        
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        
        self.initialLimit = None
        self.initialRange = None
        self.storedRange = None
        
        self.setMinimumHeight(3)
        self.setMinimumWidth(5)
        
        backgroundPalette = QtGui.QPalette()
        backgroundPalette.setColor(QtGui.QPalette.Background, QtGui.QColor(55, 55, 55))
        self.setAutoFillBackground(True)
        self.setPalette(backgroundPalette)
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(1,1,1,1)

        self.rangeBar = DragableButton()
        self.rangeBar.setStyleSheet(self.rangeBarStyle)
        layout.addChildWidget(self.rangeBar)

        rangeBarLayout = QtWidgets.QHBoxLayout(self.rangeBar)
        rangeBarLayout.setContentsMargins(3,0,3,0)
        rangeBarLayout.setSpacing(0)

        self.rangeStartLayout = QtWidgets.QHBoxLayout()
        self.rangeStartLayout.setContentsMargins(0,0,0,0)
        self.rangeStartLayout.setSpacing(3)
        rangeBarLayout.addLayout(self.rangeStartLayout, alignment=QtCore.Qt.AlignLeft)

        self.rangeStartSlider = DragableButton()
        self.rangeStartSlider.setStyleSheet(self.rangeSliderStyle)
        self.rangeStartLayout.addWidget(self.rangeStartSlider)

        self.rangeStartLabel = QtWidgets.QLabel("0")
        self.rangeStartLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.rangeStartLabel.setStyleSheet(self.rangeLabelStyle)
        self.rangeStartLayout.addWidget(self.rangeStartLabel)
        
        self.rangeLengthLabel = QtWidgets.QLabel("-1-")
        self.rangeLengthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeLengthLabel.setStyleSheet(self.rangeLabelStyle)
        rangeBarLayout.addWidget(self.rangeLengthLabel, alignment=QtCore.Qt.AlignCenter)

        self.rangeEndLayout = QtWidgets.QHBoxLayout()
        self.rangeEndLayout.setContentsMargins(0,0,0,0)
        self.rangeEndLayout.setSpacing(5)
        rangeBarLayout.addLayout(self.rangeEndLayout, alignment=QtCore.Qt.AlignRight)

        self.rangeEndLabel = QtWidgets.QLabel("100")
        self.rangeEndLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.rangeEndLabel.setStyleSheet(self.rangeLabelStyle)
        self.rangeEndLayout.addWidget(self.rangeEndLabel)

        self.rangeEndSlider = DragableButton()
        self.rangeEndSlider.setStyleSheet(self.rangeSliderStyle)
        self.rangeEndLayout.addWidget(self.rangeEndSlider)

        self.rangeBar.pressed.connect(self.onRangeBarPressed)
        self.rangeBar.moved.connect(self.onRangeBarMoved)
        self.rangeBar.released.connect(self.onRangeButtonReleased)
        self.rangeBar.cancelled.connect(self.onRangeButtonCancelled)
        self.rangeBar.doubleClicked.connect(self.onRangeBarDoubleClicked)

        self.rangeStartSlider.pressed.connect(self.onRangeStartSliderPressed)
        self.rangeStartSlider.moved.connect(self.onRangeStartSliderMoved)
        self.rangeStartSlider.released.connect(self.onRangeButtonReleased)
        self.rangeStartSlider.cancelled.connect(self.onRangeButtonCancelled)
        self.rangeStartSlider.doubleClicked.connect(self.onRangeStartSliderDoubleClicked)

        self.rangeEndSlider.pressed.connect(self.onRangeEndSliderPressed)
        self.rangeEndSlider.moved.connect(self.onRangeEndSliderMoved)
        self.rangeEndSlider.released.connect(self.onRangeButtonReleased)
        self.rangeEndSlider.cancelled.connect(self.onRangeButtonCancelled)
        self.rangeEndSlider.doubleClicked.connect(self.onRangeEndSliderDoubleClicked)
    
    def showEvent(self, event):
        self.updateRangeSlider()

    def resizeEvent(self, event):
        self.updateRangeSlider()
    
    def getRangeStart(self):
        raise NotImplementedError()
    
    def getRangeEnd(self):
        raise NotImplementedError()
    
    def getRangeMinimum(self):
        raise NotImplementedError()
    
    def getRangeMaximum(self):
        raise NotImplementedError()
    
    def setRangeStart(self, start):
        raise NotImplementedError()
    
    def setRangeEnd(self, end):
        raise NotImplementedError()
    
    def setRangeMinimum(self, minimum):
        raise NotImplementedError()
    
    def setRangeMaximum(self, maximum):
        raise NotImplementedError()
    
    def setRangeAndLimit(self, start, end, minimum, maximum):
        self.setRange(start, end)
        self.setLimit(minimum, maximum)
    
    def setRange(self, start, end):
        self.setRangeStart(start)
        self.setRangeEnd(end)
        
    def setLimit(self, minimum, maximum):
        self.setRangeMinimum(minimum)
        self.setRangeMaximum(maximum)
        
    def setRangeStartAndMinimum(self, start, minimum):
        self.setRangeStart(start)
        self.setRangeMinimum(minimum)
        
    def setRangeEndAndMaximum(self, end, maximum):
        self.setRangeEnd(end)
        self.setRangeMaximum(maximum)

    def isShiftKeyPressed(self):
        # The Shift key allows to modify the maximum and minimum ranges
        return False

    def isCtrlKeyPressed(self):
        # Ctrl key allows to move the range on a fixed step, regardless of the length of the range
        return False
    
    def getFixedPixelToFrameRatio(self):
        raise NotImplementedError()
    
    def shouldDrawRangeLength(self):
        return True
    
    def updateRangeSlider(self, emitSignal=True):
        rangeStart = self.getRangeStart()
        rangeEnd = self.getRangeEnd()
        rangeMinimum = self.getRangeMinimum()
        rangeMaximum = self.getRangeMaximum()
        
        self.rangeStartLabel.setText(str(int(rangeStart)))
        self.rangeEndLabel.setText(str(int(rangeEnd)))
        self.rangeLengthLabel.setText("-{}-".format(int(rangeEnd - rangeStart)))
        
        margins = self.layout().contentsMargins()
        width = self.width() - margins.right() - margins.left()
        height = self.height() - margins.top() - margins.bottom()

        pixelToFrameRatio = width / float(rangeMaximum - rangeMinimum)
        position = (rangeStart - rangeMinimum) * pixelToFrameRatio
        size = (rangeEnd - rangeStart) * pixelToFrameRatio

        rangeStartLabelTextWidth = self.rangeStartLabel.fontMetrics().width(self.rangeStartLabel.text()) + self.rangeStartLayout.spacing()
        rangeEndLabelTextWidth = self.rangeEndLabel.fontMetrics().width(self.rangeEndLabel.text()) + self.rangeEndLayout.spacing()
        rangeLengthLabelTextWidth = self.rangeLengthLabel.fontMetrics().width(self.rangeLengthLabel.text())
        
        self.rangeStartLabel.setVisible(size >= rangeStartLabelTextWidth + 5)
        self.rangeEndLabel.setVisible(size >= rangeStartLabelTextWidth + rangeEndLabelTextWidth + 5)
        self.rangeLengthLabel.setVisible(self.shouldDrawRangeLength() and (size >= rangeStartLabelTextWidth + rangeEndLabelTextWidth + rangeLengthLabelTextWidth + 10))
        
        buttonWidth = self.rangeStartSlider.width() + self.rangeEndSlider.width()
        position -= buttonWidth * (rangeStart - rangeMinimum) / (rangeMaximum - rangeMinimum)
        size += buttonWidth * (1 - (rangeEnd - rangeStart) / (rangeMaximum - rangeMinimum))

        self.rangeBar.move(margins.left() + round(position), margins.top())
        self.rangeBar.resize(round(size), height)
        
        if emitSignal:
            self.rangeChanged.emit(rangeStart, rangeEnd, rangeMinimum, rangeMaximum)

    def onRangeButtonReleased(self):
        self.initialLimit = None
        self.initialRange = None

    def onRangeButtonCancelled(self):
        self.setRangeAndLimit(self.initialRange[0], self.initialRange[1], self.initialLimit[0], self.initialLimit[1])
        self.onRangeButtonReleased()

    def onRangeBarPressed(self):
        self.initialRange = (self.getRangeStart(), self.getRangeEnd())
        self.initialLimit = (self.getRangeMinimum(), self.getRangeMaximum())

        if self.isShiftKeyPressed():
            self.setLimit(self.initialRange[0], self.initialRange[1])

    def onRangeBarMoved(self, translation):
        rangeMinimum = self.initialLimit[0]
        rangeMaximum = self.initialLimit[1]

        if self.isCtrlKeyPressed():
            pixelToFrameRatio = self.getFixedPixelToFrameRatio()
        else:
            margins = self.layout().contentsMargins()
            width = self.width() - margins.left() - margins.right()
            pixelToFrameRatio = width / float(rangeMaximum - rangeMinimum)

        duration = self.initialRange[1] - self.initialRange[0]
        rangeStart = self.initialRange[0] + round(translation.x() / pixelToFrameRatio)

        if self.isShiftKeyPressed():
            rangeMinimum = rangeStart
            rangeMaximum = rangeStart + duration
            rangeEnd = rangeMaximum
            
            self.setRangeAndLimit(rangeStart, rangeEnd, rangeMinimum, rangeMaximum)
        else:
            if rangeStart < rangeMinimum:
                rangeStart = rangeMinimum
            elif rangeStart + duration > rangeMaximum:
                rangeStart = rangeMaximum - duration
            rangeEnd = rangeStart + duration
            
            self.setRange(rangeStart, rangeEnd)

    def onRangeBarDoubleClicked(self):
        rangeStart = self.getRangeStart()
        rangeEnd = self.getRangeEnd()
        rangeMinimum = self.getRangeMinimum()
        rangeMaximum = self.getRangeMaximum()

        if self.storedRange and rangeStart == rangeMinimum and rangeEnd == rangeMaximum:
            newStart = min(max(self.storedRange[0], rangeMinimum), rangeMaximum - 1, self.storedRange[1] - 1)
            newEnd = max(min(self.storedRange[1], rangeMaximum), rangeMinimum + 1, self.storedRange[0] + 1)
            self.setRange(newStart, newEnd)
        else:
            self.storedRange = (rangeStart, rangeEnd)
            self.setRange(rangeMinimum, rangeMaximum)

    def onRangeStartSliderPressed(self):
        self.initialRange = (self.getRangeStart(), self.getRangeEnd())
        self.initialLimit = (self.getRangeMinimum(), self.getRangeMaximum())

        if self.isShiftKeyPressed():
            self.setRangeMinimum(self.initialRange[0])

    def onRangeStartSliderMoved(self, translation):
        rangeMinimum = self.initialLimit[0]
        rangeMaximum = self.initialLimit[1]

        if self.isCtrlKeyPressed():
            pixelToFrameRatio = self.getFixedPixelToFrameRatio()
        else:
            margins = self.layout().contentsMargins()
            width = self.width() - margins.left() - margins.right()
            pixelToFrameRatio = width / float(rangeMaximum - rangeMinimum)

        rangeStart = self.initialRange[0] + round(translation.x() / pixelToFrameRatio)

        rangeEnd = self.getRangeEnd()
        if rangeStart >= rangeEnd:
            rangeStart = rangeEnd - 1

        if self.isShiftKeyPressed():
            rangeMinimum = rangeStart
            self.setRangeStartAndMinimum(rangeStart, rangeMinimum)
        else:
            if rangeStart < rangeMinimum:
                rangeStart = rangeMinimum
            self.setRangeStart(rangeStart)
        
    def onRangeStartSliderDoubleClicked(self):
        rangeStart = self.getRangeStart()
        rangeMinimum = self.getRangeMinimum()
        rangeMaximum = self.getRangeMaximum()

        if self.storedRange and rangeStart == rangeMinimum:
            newStart = min(max(self.storedRange[0], rangeMinimum), rangeMaximum - 1, self.storedRange[1] - 1)
            self.setRangeStart(newStart)
        else:
            if self.storedRange:
                storedEnd = self.storedRange[1]
            else:
                storedEnd = rangeMaximum
            self.storedRange = (rangeStart, storedEnd)
            self.setRangeStart(rangeMinimum)

    def onRangeEndSliderPressed(self):
        self.initialRange = (self.getRangeStart(), self.getRangeEnd())
        self.initialLimit = (self.getRangeMinimum(), self.getRangeMaximum())

        if self.isShiftKeyPressed():
            self.setRangeMaximum(self.getRangeEnd())

    def onRangeEndSliderMoved(self, translation):
        rangeMinimum = self.initialLimit[0]
        rangeMaximum = self.initialLimit[1]

        if self.isCtrlKeyPressed():
            pixelToFrameRatio = self.getFixedPixelToFrameRatio()
        else:
            margins = self.layout().contentsMargins()
            width = self.width() - margins.left() - margins.right()
            pixelToFrameRatio = width / float(rangeMaximum - rangeMinimum)

        rangeEnd = self.initialRange[1] + round(translation.x() / pixelToFrameRatio)

        rangeStart = self.getRangeStart()
        if rangeEnd <= rangeStart:
            rangeEnd = rangeStart + 1

        if self.isShiftKeyPressed():
            rangeMaximum = rangeEnd
            self.setRangeEndAndMaximum(rangeEnd, rangeMaximum)
        else:
            if rangeEnd > rangeMaximum:
                rangeEnd = rangeMaximum
            self.setRangeEnd(rangeEnd)

    def onRangeEndSliderDoubleClicked(self):
        rangeEnd = self.getRangeEnd()
        rangeMinimum = self.getRangeMinimum()
        rangeMaximum = self.getRangeMaximum()

        if self.storedRange and rangeEnd == rangeMaximum:
            newEnd = max(min(self.storedRange[1], rangeMaximum), rangeMinimum + 1, self.storedRange[0] + 1)
            self.setRangeEnd(newEnd)
        else:
            if self.storedRange:
                storedStart = self.storedRange[0]
            else:
                storedStart = rangeMinimum
            self.storedRange = (storedStart, rangeEnd)
            self.setRangeEnd(rangeMaximum)
