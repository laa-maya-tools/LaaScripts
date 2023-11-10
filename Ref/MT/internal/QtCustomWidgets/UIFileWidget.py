from PySide2 import QtWidgets, QtUiTools

import ProjectPath

import os

def loadUIWidget(uiFilePath, parent=None):
    return QtUiTools.QUiLoader().load(os.path.join(ProjectPath.getToolsFolder(), uiFilePath), parent)

class UIFileWidget(QtWidgets.QWidget):

    def __init__(self, uiFilePath, parent=None):
        super(UIFileWidget, self).__init__(parent=parent)

        # Load UI file
        self.ui = loadUIWidget(uiFilePath)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.ui)