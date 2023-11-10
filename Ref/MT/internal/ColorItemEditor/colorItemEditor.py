from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui, QtCore
import QtCustomWidgets.UIFileWidget as UIFileWidget

import maya.cmds as cmds
import maya.mel as mel
import sys
import json
import os

class ColorItemEditorWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ColorItemEditor\colorItemEditor.ui"

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.setObjectName('ColorItemEditor')
        self.setWindowTitle('Color Item Editor')

        for QButtonName, QButtonWidget in self.ui.__dict__.items():
            if "colorQButton" not in QButtonName:
                continue
            QButtonWidget.clicked.connect( self.colorQButtonAction )
        self.ui.colorDisableQButton.clicked.connect( self.colorDisableQButtonAction )
        self.ui.colorRGBQButton.clicked.connect( self.colorRGBQButtonAction )
    
    def colorDisableQButtonAction(self):
        if self._failures_():
            return
        for node in self.getColorTargets():
            if self.ui.colorViewportQCheck.isChecked():
                cmds.setAttr("{}.overrideEnabled".format(node), False)
                cmds.setAttr("{}.overrideRGBColors".format(node), 0)
                cmds.setAttr("{}.overrideColor".format(node), 0)
                cmds.setAttr("{}.overrideColorRGB".format(node), 0,0,0)
            if self.ui.colorOutlinerQCheck.isChecked():
                cmds.setAttr("{}.useOutlinerColor".format(node), False)
                cmds.setAttr('{}.outlinerColor'.format(node), 0,0,0)
    
    def colorRGBQButtonAction(self):
        if self._failures_():
            return
        colorRGB = cmds.colorEditor()
        if colorRGB.endswith("0"):
            return
        colorRGB = [float(channel) for channel in colorRGB[1:-2].split(" ") if channel]
        if self.ui.colorOutlinerQCheck.isChecked():
            self.setOutlinerColor(self.getColorTargets(), colorRGB)
        if self.ui.colorViewportQCheck.isChecked():
            self.setOverrideColorRGB(self.getColorTargets(), colorRGB)
    
    def colorQButtonAction(self):
        if self._failures_():
            return
        colorQButton = self.sender()
        colorIndex = int(colorQButton.objectName().split("_")[1])        
        colorOutliner = [float(channel)/255 for channel in colorQButton.styleSheet()[22:-2].split(", ")]
        if self.ui.colorViewportQCheck.isChecked():
            self.setOverrideColor(self.getColorTargets(), colorIndex)
        if self.ui.colorOutlinerQCheck.isChecked():
            self.setOutlinerColor(self.getColorTargets(), colorOutliner)
    
    def getColorTargets(self):
        sel = cmds.ls(sl=True) if self.ui.colorSelectionQCheck.isChecked() else []
        if self.ui.colorShapesQCheck.isChecked():
            for each in cmds.ls(sl=True):
                sel.extend( cmds.listRelatives(each, shapes=True) or [] )
        return sel

    def setOutlinerColor(self, nodeLs, rgbValue):
        for node in nodeLs:
            cmds.setAttr("{}.useOutlinerColor".format(node), True)
            cmds.setAttr('{}.outlinerColor'.format(node), *rgbValue)

    def setOverrideColor(self, nodeLs, index):
        for node in nodeLs:
            cmds.setAttr("{}.overrideEnabled".format(node), True)
            cmds.setAttr("{}.overrideRGBColors".format(node), 0)
            cmds.setAttr("{}.overrideColor".format(node), index)
    
    def setOverrideColorRGB(self, nodeLs, rgb):
        for node in nodeLs:
            cmds.setAttr("{}.overrideEnabled".format(node), True)
            cmds.setAttr("{}.overrideRGBColors".format(node), 1)
            cmds.setAttr("{}.overrideColorRGB".format(node), *rgb)

    def _failures_(self):
        if not self.ui.colorSelectionQCheck.isChecked() and not self.ui.colorShapesQCheck.isChecked():
            sys.stdout.write('Need at least one True input check in "Colorize"')
            return True
        if not self.ui.colorViewportQCheck.isChecked() and not self.ui.colorOutlinerQCheck.isChecked():
            sys.stdout.write('Need at least one True input check in "Affect To"')
            return True
        return False
        

def show():
    global colorItemEditor
    try:
        if colorItemEditor.isVisible():
            colorItemEditor.close()
    except NameError:
        pass
    colorItemEditor = ColorItemEditorWin()
    colorItemEditor.show()