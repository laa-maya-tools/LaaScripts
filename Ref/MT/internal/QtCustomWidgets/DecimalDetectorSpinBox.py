from PySide2 import QtCore, QtWidgets, QtGui

from QtCustomWidgets import QtUtils

class DecimalDetectorSpinBox(QtWidgets.QDoubleSpinBox):
    
    def __init__(self):
        super().__init__()
        
        self.valueChanged.connect(self.updateColor)
    
    def textFromValue(self, value):
        if value.is_integer():
            return str(int(value))
        else:
            return super().textFromValue(value)
    
    def updateColor(self, value):
        if value.is_integer():
            #QtUtils.restorePaletteColor(self, QtGui.QPalette.Window)
            QtUtils.restorePaletteColor(self, QtGui.QPalette.Text)
            QtUtils.restorePaletteColor(self.lineEdit(), QtGui.QPalette.Text)
        else:
            #QtUtils.setPaletteColor(self, QtGui.QPalette.Window, QtCore.Qt.red)
            QtUtils.setPaletteColor(self, QtGui.QPalette.Text, QtCore.Qt.red)
            QtUtils.setPaletteColor(self.lineEdit(), QtGui.QPalette.Text, QtCore.Qt.red)
    
    def wheelEvent(self, event):
        event.ignore()
