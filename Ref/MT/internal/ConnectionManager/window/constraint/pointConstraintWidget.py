from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import QtCustomWidgets.UIFileWidget as UIFileWidget
import maya.cmds as cmds
import os

class PointConstraintWidgetWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\pointConstraintWidget.ui"

    def __init__(self, parent=None, constraintsInputLs=[]):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.constraintsInputLs = constraintsInputLs
        
        self.ui.restPositionQCheck.stateChanged.connect(self.restPositionFunc)
        self.ui.restPositionXQSpin.valueChanged.connect(self.restPositionXFunc)
        self.ui.restPositionYQSpin.valueChanged.connect(self.restPositionYFunc)
        self.ui.restPositionZQSpin.valueChanged.connect(self.restPositionZFunc)
        self.ui.offsetXQSpin.valueChanged.connect(self.offsetXFunc)
        self.ui.offsetYQSpin.valueChanged.connect(self.offsetYFunc)
        self.ui.offsetZQSpin.valueChanged.connect(self.offsetZFunc)

        self.getAttrInfo()

    def offsetXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".offsetX", self.ui.offsetXQSpin.value())
    
    def offsetYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".offsetY", self.ui.offsetYQSpin.value())
    
    def offsetZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".offsetZ", self.ui.offsetZQSpin.value())
    
    def restPositionXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateX", self.ui.restPositionXQSpin.value())
    
    def restPositionYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateY", self.ui.restPositionYQSpin.value())
    
    def restPositionZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateZ", self.ui.restPositionZQSpin.value())
    
    def restPositionFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".enableRestPosition", self.ui.restPositionQCheck.isChecked())

    def getAttrInfo(self):
        self.ui.offsetXQSpin.setValue(0)
        self.ui.offsetYQSpin.setValue(0)
        self.ui.offsetZQSpin.setValue(0)
        self.ui.restPositionQCheck.setChecked(False)
        self.ui.restPositionXQSpin.setValue(0)
        self.ui.restPositionYQSpin.setValue(0)
        self.ui.restPositionZQSpin.setValue(0)
        for cns in self.constraintsInputLs:
            offset = cmds.getAttr(cns + ".offset")[0]
            self.ui.offsetXQSpin.setValue(offset[0])
            self.ui.offsetYQSpin.setValue(offset[1])
            self.ui.offsetZQSpin.setValue(offset[2])
            # rest position
            self.ui.restPositionQCheck.setChecked(cmds.getAttr(cns + ".enableRestPosition"))
            restPos = cmds.getAttr(cns + ".restTranslate")[0]
            self.ui.restPositionXQSpin.setValue(restPos[0])
            self.ui.restPositionYQSpin.setValue(restPos[1])
            self.ui.restPositionZQSpin.setValue(restPos[2])