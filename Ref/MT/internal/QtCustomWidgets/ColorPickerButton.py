from PySide2 import QtCore, QtWidgets, QtGui

class ColorPickerButton(QtWidgets.QPushButton):
    
    colorPicked = QtCore.Signal(QtGui.QColor)
    
    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent=parent)
        
        self.color = None
        self.borderColor = QtGui.QColor(QtCore.Qt.black)
        
        self.styleSheetString = "QPushButton:enabled {{ border: 1px solid rgb({3}, {4}, {5}); border-radius: 2px; background-color: rgb({0}, {1}, {2}); }} QPushButton:disabled {{ border: 1px solid rgb({3}, {4}, {5}); border-radius: 2px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.49 rgb({0}, {1}, {2}), stop:0.5 hsl(0, 0, 64)); }}"
        
        self.setAutoFillBackground(True)
        self.setMinimumWidth(1)
        
        self.clicked.connect(self.browseColor)
        
    def updateStyleSheet(self):
        self.setStyleSheet(self.styleSheetString.format(self.color.red(), self.color.green(), self.color.blue(), self.borderColor.red(), self.borderColor.green(), self.borderColor.blue()))

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        color = QtGui.QColor(color)
        self.color = color
        self.updateStyleSheet()
        self.colorPicked.emit(color)
        
    def setBorderColor(self, color):
        color = QtGui.QColor(color)
        self.borderColor = color
        self.updateStyleSheet()
        
    def browseColor(self):
        pickedColor = QtWidgets.QColorDialog.getColor(self.getColor(), self, "Select Shot Color")
        if pickedColor != None:
            self.setColor(pickedColor)

