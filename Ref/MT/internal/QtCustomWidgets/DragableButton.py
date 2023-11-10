from PySide2 import QtCore, QtWidgets

class DragableButton(QtWidgets.QPushButton):

    moved = QtCore.Signal(QtCore.QPointF)
    cancelled = QtCore.Signal()
    doubleClicked = QtCore.Signal()

    def __init__(self, parent=None):
        super(DragableButton, self).__init__(parent)
        self.pressedPosition = None
        
    def isPressed(self):
        return self.pressedPosition != None

    def mousePressEvent(self, event):
        blockedSignals = self.blockSignals(True)
        super(DragableButton, self).mousePressEvent(event)
        self.blockSignals(blockedSignals)

        if event.button() == QtCore.Qt.LeftButton:
            self.pressedPosition = event.screenPos()
            self.pressed.emit()
            event.accept()
        elif event.button() == QtCore.Qt.RightButton:
            if self.pressedPosition != None:
                self.pressedPosition = None
                self.cancelled.emit()
                event.accept()
                
        return True

    def mouseMoveEvent(self, event):
        blockedSignals = self.blockSignals(True)
        super(DragableButton, self).mouseMoveEvent(event)
        self.blockSignals(blockedSignals)

        if self.pressedPosition != None:
            self.moved.emit(event.screenPos() - self.pressedPosition)
            event.accept()
            
        return True

    def mouseReleaseEvent(self, event):
        blockedSignals = self.blockSignals(True)
        super(DragableButton, self).mouseReleaseEvent(event)
        self.blockSignals(blockedSignals)

        if event.button() == QtCore.Qt.LeftButton:
            if self.pressedPosition != None:
                self.pressedPosition = None
                self.released.emit()
                event.accept()
                
        return True

    def mouseDoubleClickEvent(self, event):
        blockedSignals = self.blockSignals(True)
        super(DragableButton, self).mouseDoubleClickEvent(event)
        self.blockSignals(blockedSignals)

        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClicked.emit()
            event.accept()
            
        return True
