from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtGui
import QtCustomWidgets.UIFileWidget as UIFileWidget
import maya.cmds as cmds
import os

class AimConstraintWidgetWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\aimConstraintWidget.ui"

    def __init__(self, parent=None, constraintsInputLs=[]):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.constraintsInputLs = constraintsInputLs
        # icons
        self.ui.worldUpObjectQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        # connections
        self.ui.restPositionQCheck.stateChanged.connect(self.restPositionFunc)
        self.ui.restPositionXQSpin.valueChanged.connect(self.restPositionXFunc)
        self.ui.restPositionYQSpin.valueChanged.connect(self.restPositionYFunc)
        self.ui.restPositionZQSpin.valueChanged.connect(self.restPositionZFunc)
        self.ui.offsetXQSpin.valueChanged.connect(self.offsetXFunc)
        self.ui.offsetYQSpin.valueChanged.connect(self.offsetYFunc)
        self.ui.offsetZQSpin.valueChanged.connect(self.offsetZFunc)
        self.ui.aimVectorXQSpin.valueChanged.connect(self.aimVectorXFunc)
        self.ui.aimVectorYQSpin.valueChanged.connect(self.aimVectorYFunc)
        self.ui.aimVectorZQSpin.valueChanged.connect(self.aimVectorZFunc)
        self.ui.upVectorXQSpin.valueChanged.connect(self.upVectorXFunc)
        self.ui.upVectorYQSpin.valueChanged.connect(self.upVectorYFunc)
        self.ui.upVectorZQSpin.valueChanged.connect(self.upVectorZFunc)
        self.ui.worldUpVectorXQSpin.valueChanged.connect(self.worldUpVectorXFunc)
        self.ui.worldUpVectorYQSpin.valueChanged.connect(self.worldUpVectorYFunc)
        self.ui.worldUpVectorZQSpin.valueChanged.connect(self.worldUpVectorZFunc)
        self.ui.worldUpTypeQCombo.currentIndexChanged.connect(self.worldUpTypeFunc)
        self.ui.worldUpObjectQLine.returnPressed.connect(self.worldUpObjectFunc)
        self.ui.worldUpObjectQButton.clicked.connect(self.worldUpObjectSelFunc)
        self.getAttrInfo()

    def worldUpObjectFunc(self):
        val = self.ui.worldUpObjectQLine.text()
        if cmds.ls(val, l=True):
            for cns in self.constraintsInputLs:
                cmds.connectAttr(val + ".wm[0]", cns + ".worldUpMatrix", force=True)
                cmds.setAttr(cns + ".worldUpType", self.ui.worldUpTypeQCombo.currentIndex())
    
    def worldUpObjectSelFunc(self):
        sel = cmds.ls(sl=True)
        if sel:
            self.ui.worldUpObjectQLine.setText(sel[-1])
            self.worldUpObjectFunc()

    def worldUpTypeFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".worldUpType", self.ui.worldUpTypeQCombo.currentIndex())

    def worldUpVectorXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".worldUpVectorX", self.ui.worldUpVectorXQSpin.value())
    
    def worldUpVectorYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".worldUpVectorY", self.ui.worldUpVectorYQSpin.value())
    
    def worldUpVectorZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".worldUpVectorZ", self.ui.worldUpVectorZQSpin.value())

    def upVectorXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".upVectorX", self.ui.upVectorXQSpin.value())
    
    def upVectorYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".upVectorY", self.ui.upVectorYQSpin.value())
    
    def upVectorZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".upVectorZ", self.ui.upVectorZQSpin.value())

    def aimVectorXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".aimVectorX", self.ui.aimVectorXQSpin.value())
    
    def aimVectorYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".aimVectorY", self.ui.aimVectorYQSpin.value())
    
    def aimVectorZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".aimVectorZ", self.ui.aimVectorZQSpin.value())

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
            cmds.setAttr(cns + ".restRotateX", self.ui.restPositionXQSpin.value())
    
    def restPositionYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restRotateY", self.ui.restPositionYQSpin.value())
    
    def restPositionZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restRotateZ", self.ui.restPositionZQSpin.value())
    
    def restPositionFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".enableRestPosition", self.ui.restPositionQCheck.isChecked())

    def getAttrInfo(self):
        self.ui.worldUpTypeQCombo.setCurrentIndex(0)
        self.ui.worldUpVectorXQSpin.setValue(0)
        self.ui.worldUpVectorYQSpin.setValue(0)
        self.ui.worldUpVectorZQSpin.setValue(0)
        self.ui.upVectorXQSpin.setValue(0)
        self.ui.upVectorYQSpin.setValue(0)
        self.ui.upVectorZQSpin.setValue(0)
        self.ui.aimVectorXQSpin.setValue(0)
        self.ui.aimVectorYQSpin.setValue(0)
        self.ui.aimVectorZQSpin.setValue(0)
        self.ui.offsetXQSpin.setValue(0)
        self.ui.offsetYQSpin.setValue(0)
        self.ui.offsetZQSpin.setValue(0)
        self.ui.restPositionQCheck.setChecked(False)
        self.ui.restPositionXQSpin.setValue(0)
        self.ui.restPositionYQSpin.setValue(0)
        self.ui.restPositionZQSpin.setValue(0)
        for cns in self.constraintsInputLs:
            # worldUpType
            self.ui.worldUpTypeQCombo.setCurrentIndex(cmds.getAttr(cns + ".worldUpType"))
            # worldUpObject
            self.ui.worldUpObjectQLine.setText((cmds.listConnections(cns + ".worldUpMatrix") or [""])[0])
            # worldUp vector
            worldUpVector = cmds.getAttr(cns + ".worldUpVector")[0]
            self.ui.worldUpVectorXQSpin.setValue(worldUpVector[0])
            self.ui.worldUpVectorYQSpin.setValue(worldUpVector[1])
            self.ui.worldUpVectorZQSpin.setValue(worldUpVector[2])
            # worldUp vector
            worldUpVector = cmds.getAttr(cns + ".worldUpVector")[0]
            self.ui.worldUpVectorXQSpin.setValue(worldUpVector[0])
            self.ui.worldUpVectorYQSpin.setValue(worldUpVector[1])
            self.ui.worldUpVectorZQSpin.setValue(worldUpVector[2])
            # up vector
            upVector = cmds.getAttr(cns + ".upVector")[0]
            self.ui.upVectorXQSpin.setValue(upVector[0])
            self.ui.upVectorYQSpin.setValue(upVector[1])
            self.ui.upVectorZQSpin.setValue(upVector[2])
            # aim vector
            aimVector = cmds.getAttr(cns + ".aimVector")[0]
            self.ui.aimVectorXQSpin.setValue(aimVector[0])
            self.ui.aimVectorYQSpin.setValue(aimVector[1])
            self.ui.aimVectorZQSpin.setValue(aimVector[2])
            # offset
            offset = cmds.getAttr(cns + ".offset")[0]
            self.ui.offsetXQSpin.setValue(offset[0])
            self.ui.offsetYQSpin.setValue(offset[1])
            self.ui.offsetZQSpin.setValue(offset[2])
            # rest position
            self.ui.restPositionQCheck.setChecked(cmds.getAttr(cns + ".enableRestPosition"))
            restPos = cmds.getAttr(cns + ".restRotate")[0]
            self.ui.restPositionXQSpin.setValue(restPos[0])
            self.ui.restPositionYQSpin.setValue(restPos[1])
            self.ui.restPositionZQSpin.setValue(restPos[2])