from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from functools import reduce
import QtCustomWidgets.UIFileWidget as UIFileWidget
import maya.cmds as cmds
import os

class ParentConstraintTargetOffsetWidgetWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\parentConstraintTargetOffsetWidget.ui"

    def __init__(self, parent=None, constraintsInputLs=[], masterName=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.parentWidget = parent
        self.constraintsInputLs = constraintsInputLs
        self.masterName = masterName
        self.ui.offsetQBox.setTitle(self.ui.offsetQBox.title().replace("...",masterName))
        
        self.ui.offsetTrXQSpin.valueChanged.connect(self.offsetTrXFunc)
        self.ui.offsetTrYQSpin.valueChanged.connect(self.offsetTrYFunc)
        self.ui.offsetTrZQSpin.valueChanged.connect(self.offsetTrZFunc)
        self.ui.offsetRtXQSpin.valueChanged.connect(self.offsetRtXFunc)
        self.ui.offsetRtYQSpin.valueChanged.connect(self.offsetRtYFunc)
        self.ui.offsetRtZQSpin.valueChanged.connect(self.offsetRtZFunc)

        self.getAttrInfo()

    def getAttrInfo(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName not in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    continue
                self.ui.offsetTrXQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetTranslateX".format(cns, ind)))
                self.ui.offsetTrYQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetTranslateY".format(cns, ind)))
                self.ui.offsetTrZQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetTranslateZ".format(cns, ind)))
                self.ui.offsetRtXQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetRotateX".format(cns, ind)))
                self.ui.offsetRtYQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetRotateY".format(cns, ind)))
                self.ui.offsetRtZQSpin.setValue(cmds.getAttr("{}.target[{}].targetOffsetRotateZ".format(cns, ind)))

    def offsetTrXFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetTranslateX".format(cns, ind), self.ui.offsetTrXQSpin.value())
            
    def offsetTrYFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetTranslateY".format(cns, ind), self.ui.offsetTrYQSpin.value())
            
    def offsetTrZFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetTranslateZ".format(cns, ind), self.ui.offsetTrZQSpin.value())
            
    def offsetRtXFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetRotateX".format(cns, ind), self.ui.offsetRtXQSpin.value())
            
    def offsetRtYFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetRotateY".format(cns, ind), self.ui.offsetRtYQSpin.value())
            
    def offsetRtZFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                if self.masterName in cmds.listConnections("{}.target[{}].targetParentMatrix".format(cns, ind)):
                    cmds.setAttr("{}.target[{}].targetOffsetRotateZ".format(cns, ind), self.ui.offsetRtZQSpin.value())

class ParentConstraintWidgetWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\parentConstraintWidget.ui"

    def __init__(self, parent=None, constraintsInputLs=[]):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.constraintsInputLs = constraintsInputLs

        self.ui.restPositionQCheck.stateChanged.connect(self.restPositionFunc)
        self.ui.restPositionTrXQSpin.valueChanged.connect(self.restPositionTrXFunc)
        self.ui.restPositionTrYQSpin.valueChanged.connect(self.restPositionTrYFunc)
        self.ui.restPositionTrZQSpin.valueChanged.connect(self.restPositionTrZFunc)
        self.ui.restPositionRtXQSpin.valueChanged.connect(self.restPositionRtXFunc)
        self.ui.restPositionRtYQSpin.valueChanged.connect(self.restPositionRtYFunc)
        self.ui.restPositionRtZQSpin.valueChanged.connect(self.restPositionRtZFunc)
        self.ui.interpTypeQCombo.currentIndexChanged.connect(self.interpTypeFunc)

        self.getAttrInfo()
        self.addOffsetWidget()

    def interpTypeFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".interpType", self.ui.interpTypeQCombo.currentIndex())

    def restPositionTrXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateX", self.ui.restPositionTrXQSpin.value())
    
    def restPositionTrYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateY", self.ui.restPositionTrYQSpin.value())
    
    def restPositionTrZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restTranslateZ", self.ui.restPositionTrZQSpin.value())
    
    def restPositionRtXFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restRotateX", self.ui.restPositionRtXQSpin.value())
    
    def restPositionRtYFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restRotateY", self.ui.restPositionRtYQSpin.value())
    
    def restPositionRtZFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".restRotateZ", self.ui.restPositionRtZQSpin.value())
    
    def restPositionFunc(self):
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".enableRestPosition", self.ui.restPositionQCheck.isChecked())

    def getAttrInfo(self):
        self.ui.interpTypeQCombo.setCurrentIndex(0)
        self.ui.restPositionQCheck.setChecked(False)
        self.ui.restPositionTrXQSpin.setValue(0)
        self.ui.restPositionTrYQSpin.setValue(0)
        self.ui.restPositionTrZQSpin.setValue(0)
        self.ui.restPositionRtXQSpin.setValue(0)
        self.ui.restPositionRtYQSpin.setValue(0)
        self.ui.restPositionRtZQSpin.setValue(0)
        if len(self.constraintsInputLs) > 1:
            return
        cns = self.constraintsInputLs[0]
        for cns in self.constraintsInputLs:
            # interpType
            self.ui.interpTypeQCombo.setCurrentIndex(cmds.getAttr(cns + ".interpType"))
            # rest position
            self.ui.restPositionQCheck.setChecked(cmds.getAttr(cns + ".enableRestPosition"))
            restTrPos = cmds.getAttr(cns + ".restTranslate")[0]
            restRtPos = cmds.getAttr(cns + ".restRotate")[0]
            self.ui.restPositionRtXQSpin.setValue(restRtPos[0])
            self.ui.restPositionRtYQSpin.setValue(restRtPos[1])
            self.ui.restPositionRtZQSpin.setValue(restRtPos[2])
            self.ui.restPositionTrXQSpin.setValue(restTrPos[0])
            self.ui.restPositionTrYQSpin.setValue(restTrPos[1])
            self.ui.restPositionTrZQSpin.setValue(restTrPos[2])
    
    def addOffsetWidget(self):
        while self.ui.targetOffsetQWidget.layout().count():
            child = self.ui.targetOffsetQWidget.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        allTargets = []
        masterConstraintDict = {}
        for cns in self.constraintsInputLs:
            for master in list(set(cmds.listConnections(cns + ".target")) - {cns}):
                if master not in masterConstraintDict.keys():
                    masterConstraintDict[master] = [cns]
                else:
                    masterConstraintDict[master].append(cns)
            #allTargets.extend( list(set(cmds.listConnections(cns + ".target")) - {cns}) )
        #for target in set(allTargets):
        for master, cnsRelated in masterConstraintDict.items():
            self.targetOffsetWidget = ParentConstraintTargetOffsetWidgetWin(self, self.constraintsInputLs, master)
            #self.targetOffsetWidget.ui.offsetQBox.title()
            self.ui.targetOffsetQWidget.layout().addWidget(self.targetOffsetWidget)