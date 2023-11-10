from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import QtCustomWidgets.UIFileWidget as UIFileWidget
from PySide2 import QtGui, QtCore, QtWidgets
from functools import reduce
from QtCustomWidgets.QtUtils import BlockSignals
from ConnectionManager.lib.classes import ConnectionMainWidgetBase

import maya.cmds as cmds
import os

class ConnectionFilterWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\connectionFilterWidget.ui"

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.parentWidget = parent

        self.ui.relatedFilterParentQCheck.stateChanged.connect(self.relatedFilterFunc)
        self.ui.relatedFilterPointQCheck.stateChanged.connect(self.relatedFilterFunc)
        self.ui.relatedFilterOrientQCheck.stateChanged.connect(self.relatedFilterFunc)
        self.ui.relatedFilterScaleQCheck.stateChanged.connect(self.relatedFilterFunc)
        self.ui.relatedFilterAimQCheck.stateChanged.connect(self.relatedFilterFunc)
        self.ui.relatedFilterPoleVectorQCheck.stateChanged.connect(self.relatedFilterFunc)
    
    def relatedFilterFunc(self):
        self.parentWidget.ui.relatedItemsQList.clear()
        self.parentWidget.ui.relatedItemsQList.addItems(self.filterFunc(self.parentWidget.constraintsInputLs))
    
    def filterFunc(self, filterElementsLs):
        filterTypeLs = []
        for checkWidget in self.ui.__dict__.values():
            if type(checkWidget) == QtWidgets.QCheckBox and checkWidget.isChecked():
                filterTypeLs.append( checkWidget.text() )
        result = []
        for elem in filterElementsLs:
            for filter in filterTypeLs:
                if filter.lower() in cmds.nodeType(elem).lower():
                    result.append( elem )
        return result

class MasterQWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ConnectionManager\window\ui\constraint\masterQWidget.ui"

    def __init__(self, parent=None, constraint=None, master=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        
        self.constraint = constraint
        self.master = master
        self._attr = None
        self.ui.masterQLabel.setText(str(master))
        self.getAttrInfo()

        self.ui.masterWeightQSpin.valueChanged.connect(self.masterWeightFunc)
    
    def masterWeightFunc(self):
        cmds.setAttr(self._attr, self.ui.masterWeightQSpin.value())
    
    def getAttrInfo(self):
        value = None
        for ind in cmds.getAttr(self.constraint + ".target", mi=True):
            if self.master not in cmds.listConnections("{}.target[{}].targetParentMatrix".format(self.constraint, ind)):
                continue
            cnn = cmds.listConnections("{}.target[{}].targetWeight".format(self.constraint, ind), p=1)
            if cnn:
                self._attr = cnn[0]
            else:
                self._attr = "{}.target[{}].targetWeight".format(self.constraint, ind)
            value = cmds.getAttr(self._attr)
            break
        self.ui.masterWeightQSpin.setValue(value)

class ConstraintMainWidgetWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget, ConnectionMainWidgetBase):
    __ui_path__        = r"ConnectionManager\window\ui\constraint\constraintMainWidget.ui"
    constraintsInputLs = []

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.parentWidget = parent
        self.filterWidget = None
        self.masterWidget = False
        self._signalsBlocked = False
        # icons
        self.ui.mastersSelQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        self.ui.addMasterQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/ts-add.png").copy(1, 1, 18, 18) )))
        self.ui.delMasterQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/delete.png").copy(1, 1, 18, 18) )))
        self.ui.replaceMasterQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/reloadReference.png").copy(1, 1, 18, 18) )))
        # buttons
        self.ui.mastersSelQButton.clicked.connect(self.mastersSelFunc)
        self.ui.addMasterQButton.clicked.connect(self.addMasterFunc)
        self.ui.delMasterQButton.clicked.connect(self.delMasterFunc)
        self.ui.replaceMasterQButton.clicked.connect(self.replaceMasterFunc)
        self.ui.renameAttrQButton.clicked.connect(self.renameAttrFunc)
        self.ui.normalizeWeightsQButton.clicked.connect(self.normalizeWeightsFunc)
        # check cnn
        self.ui.connectAllXQCheck.stateChanged.connect(self.connectAllXFunc)
        self.ui.connectAllYQCheck.stateChanged.connect(self.connectAllYFunc)
        self.ui.connectAllZQCheck.stateChanged.connect(self.connectAllZFunc)
        # tr
        self.ui.connectAllTrQCheck.stateChanged.connect(self.connectAllTrFunc)
        self.ui.connectTxQCheck.stateChanged.connect(self.connectTxFunc)
        self.ui.connectTyQCheck.stateChanged.connect(self.connectTyFunc)
        self.ui.connectTzQCheck.stateChanged.connect(self.connectTzFunc)
        # rt
        self.ui.connectAllRtQCheck.stateChanged.connect(self.connectAllRtFunc)
        self.ui.connectRxQCheck.stateChanged.connect(self.connectRxFunc)
        self.ui.connectRyQCheck.stateChanged.connect(self.connectRyFunc)
        self.ui.connectRzQCheck.stateChanged.connect(self.connectRzFunc)
        # sz
        self.ui.connectAllScQCheck.stateChanged.connect(self.connectAllScFunc)
        self.ui.connectSxQCheck.stateChanged.connect(self.connectSxFunc)
        self.ui.connectSyQCheck.stateChanged.connect(self.connectSyFunc)
        self.ui.connectSzQCheck.stateChanged.connect(self.connectSzFunc)

        self.ui.lockOutputQCheck.stateChanged.connect(self.lockOutputFunc)
        self.ui.displayOnlySharedQCheck.stateChanged.connect(self.mastersDisplayFunc)
        self.ui.mastersQList.itemSelectionChanged.connect(self.mastersFunc)
        self.addFilterWidget()
        
    def addFilterWidget(self):
        while self.parentWidget.ui.filterQWidget.layout().count():
            child = self.parentWidget.ui.filterQWidget.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.filterWidget = ConnectionFilterWidget(self.parentWidget)
        self.parentWidget.ui.filterQWidget.layout().addWidget(self.filterWidget)
    
    def relatedItemsFilter(self, relatedItemsLs):
        return self.filterWidget.filterFunc(relatedItemsLs)
    
    def normalizeWeightsFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            weightsLs = [cmds.getAttr("{}.target[{}].targetWeight".format(cns, ind)) for ind in cmds.getAttr(cns + ".target", mi=True)]
            for ind,value in enumerate(weightsLs):
                cnn = cmds.listConnections("{}.target[{}].targetWeight".format(cns, ind), p=True)
                if cnn:
                    cmds.setAttr(cnn[0], value/sum(weightsLs))
                else:
                    cmds.setAttr("{}.target[{}].targetWeight".format(cns, ind), value/sum(weightsLs))
        self.mastersDisplayFunc()
        
    def renameAttrFunc(self):
        for cns in self.constraintsInputLs:
            for ind in cmds.getAttr(cns + ".target", mi=True):
                cnn = cmds.listConnections('{}.target[{}].targetParentMatrix'.format(cns, ind))
                weightCnn = cmds.listConnections('{}.target[{}].targetWeight'.format(cns, ind), p=True)
                if cnn and weightCnn:
                    cmds.aliasAttr(cnn[0], weightCnn[0])
        self.mastersDisplayFunc()

    def addMasterFunc(self):
        sel = cmds.ls(sl=True)
        if self._signalsBlocked or not sel:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave:
                continue
            eval('cmds.{}(sel, cnsSlave, mo={})'.format(cnsType, self.ui.addMasterMOQCheck.isChecked()))
        self.mastersDisplayFunc()
    
    def replaceMasterFunc(self):
        sel = cmds.ls(sl=True)
        if self._signalsBlocked or not sel:
            return
        mSelected = self.ui.mastersQList.selectedItems()
        if len(sel) < len(mSelected):
            cmds.warning("Not selection lenght enough to replace")
        elif len(sel) > len(mSelected):
            sel = [elem for elem in sel[:len(mSelected)]]
        for cns in self.constraintsInputLs:
            inCnnLs = cmds.listConnections(cns, c=True, p=True, d=False)[::2]
            outCnnLs = cmds.listConnections(cns, c=True, p=True, d=False)[1::2]
            for master, replaceBy in zip(mSelected, sel):
                if master.text():
                    master = master.text()
                else:
                    master = self.ui.mastersQList.itemWidget(master)
                    master = master.ui.masterQLabel.text()
                for ind, cnn in enumerate(outCnnLs):
                    if master in cnn:
                        if cns in cnn:
                            cmds.aliasAttr(replaceBy, cnn)
                        else:
                            cmds.connectAttr(cnn.replace(master, replaceBy), inCnnLs[ind], force=True)
        self.mastersDisplayFunc()

    def delMasterFunc(self):
        if self._signalsBlocked:
            return
        mSelected = self.ui.mastersQList.selectedItems()
        toDelete = []
        for cns in self.constraintsInputLs:
            for master in mSelected:
                if master.text():
                    master = master.text()
                else:
                    master = self.ui.mastersQList.itemWidget(master)
                    master = master.ui.masterQLabel.text()
                if len(set(cmds.listConnections(cns + ".target", d=False)) - {cns}) == 1:
                    if cmds.confirmDialog(title="Remove Master Warning", message="Remove last master will delete constraint.\nContinue?", button=["Yes", "No"]) == "Yes":
                        toDelete.append(cns)
                        break
                inCnnLs = cmds.listConnections(cns, c=True, p=True, d=False)[::2]
                outCnnLs = cmds.listConnections(cns, c=True, p=True, d=False)[1::2]
                for inCnn, outCnn in zip(inCnnLs, outCnnLs):
                    if master in outCnn and "targetWeight" not in inCnn:
                        cmds.disconnectAttr(outCnn, inCnn)
        for cns in toDelete:
            cmds.delete(cns)
            del self.constraintsInputLs[self.constraintsInputLs.index(cns)]
        self.mastersDisplayFunc()

    def lockOutputFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cmds.setAttr(cns + ".lockOutput", self.ui.lockOutputQCheck.isChecked())

    def connectAllXFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllXQCheck.isChecked():
            if self.ui.connectTxQCheck.isEnabled(): self.ui.connectTxQCheck.setChecked(True)
            if self.ui.connectRxQCheck.isEnabled(): self.ui.connectRxQCheck.setChecked(True)
            if self.ui.connectSxQCheck.isEnabled(): self.ui.connectSxQCheck.setChecked(True)
        else:
            if self.ui.connectTxQCheck.isEnabled(): self.ui.connectTxQCheck.setChecked(False)
            if self.ui.connectRxQCheck.isEnabled(): self.ui.connectRxQCheck.setChecked(False)
            if self.ui.connectSxQCheck.isEnabled(): self.ui.connectSxQCheck.setChecked(False)
        
    def connectAllYFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllYQCheck.isChecked():
            if self.ui.connectTyQCheck.isEnabled(): self.ui.connectTyQCheck.setChecked(True)
            if self.ui.connectRyQCheck.isEnabled(): self.ui.connectRyQCheck.setChecked(True)
            if self.ui.connectSyQCheck.isEnabled(): self.ui.connectSyQCheck.setChecked(True)
        else:
            if self.ui.connectTyQCheck.isEnabled(): self.ui.connectTyQCheck.setChecked(False)
            if self.ui.connectRyQCheck.isEnabled(): self.ui.connectRyQCheck.setChecked(False)
            if self.ui.connectSyQCheck.isEnabled(): self.ui.connectSyQCheck.setChecked(False)
        
    def connectAllZFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllZQCheck.isChecked():
            if self.ui.connectTzQCheck.isEnabled(): self.ui.connectTzQCheck.setChecked(True)
            if self.ui.connectRzQCheck.isEnabled(): self.ui.connectRzQCheck.setChecked(True)
            if self.ui.connectSzQCheck.isEnabled(): self.ui.connectSzQCheck.setChecked(True)
        else:
            if self.ui.connectTzQCheck.isEnabled(): self.ui.connectTzQCheck.setChecked(False)
            if self.ui.connectRzQCheck.isEnabled(): self.ui.connectRzQCheck.setChecked(False)
            if self.ui.connectSzQCheck.isEnabled(): self.ui.connectSzQCheck.setChecked(False)
            
    def connectAllTrFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllTrQCheck.isChecked():
            self.ui.connectTxQCheck.setChecked(True)
            self.ui.connectTyQCheck.setChecked(True)
            self.ui.connectTzQCheck.setChecked(True)
        else:
            self.ui.connectTxQCheck.setChecked(False)
            self.ui.connectTyQCheck.setChecked(False)
            self.ui.connectTzQCheck.setChecked(False)
        
    def connectAllRtFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllRtQCheck.isChecked():
            self.ui.connectRxQCheck.setChecked(True)
            self.ui.connectRyQCheck.setChecked(True)
            self.ui.connectRzQCheck.setChecked(True)
        else:
            self.ui.connectRxQCheck.setChecked(False)
            self.ui.connectRyQCheck.setChecked(False)
            self.ui.connectRzQCheck.setChecked(False)
        
    def connectAllScFunc(self):
        if self._signalsBlocked:
            return
        if self.ui.connectAllScQCheck.isChecked():
            self.ui.connectSxQCheck.setChecked(True)
            self.ui.connectSyQCheck.setChecked(True)
            self.ui.connectSzQCheck.setChecked(True)
        else:
            self.ui.connectSxQCheck.setChecked(False)
            self.ui.connectSyQCheck.setChecked(False)
            self.ui.connectSzQCheck.setChecked(False)
        
    def connectTxFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["pointConstraint","parentConstraint"]:
                continue
            if self.ui.connectTxQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintTranslateX", cnsSlave[0] + ".translateX")
            else:
                cmds.disconnectAttr(cns + ".constraintTranslateX", cnsSlave[0] + ".translateX")
    
    def connectTyFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["pointConstraint","parentConstraint"]:
                continue
            if self.ui.connectTyQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintTranslateY", cnsSlave[0] + ".translateY")
            else:
                cmds.disconnectAttr(cns + ".constraintTranslateY", cnsSlave[0] + ".translateY")
    
    def connectTzFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["pointConstraint","parentConstraint"]:
                continue
            if self.ui.connectTzQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintTranslateZ", cnsSlave[0] + ".translateZ")
            else:
                cmds.disconnectAttr(cns + ".constraintTranslateZ", cnsSlave[0] + ".translateZ")
    
    def connectRxFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["normalConstraint","aimConstraint","orientConstraint","parentConstraint"]:
                continue
            if self.ui.connectRxQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintRotateX", cnsSlave[0] + ".rotateX")
            else:
                cmds.disconnectAttr(cns + ".constraintRotateX", cnsSlave[0] + ".rotateX")
    
    def connectRyFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["normalConstraint","aimConstraint","orientConstraint","parentConstraint"]:
                continue
            if self.ui.connectRyQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintRotateY", cnsSlave[0] + ".rotateY")
            else:
                cmds.disconnectAttr(cns + ".constraintRotateY", cnsSlave[0] + ".rotateY")
    
    def connectRzFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType not in ["normalConstraint","aimConstraint","orientConstraint","parentConstraint"]:
                continue
            if self.ui.connectRzQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintRotateZ", cnsSlave[0] + ".rotateZ")
            else:
                cmds.disconnectAttr(cns + ".constraintRotateZ", cnsSlave[0] + ".rotateZ")
    
    def connectSxFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType != "scaleConstraint":
                continue
            if self.ui.connectSxQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintScaleX", cnsSlave[0] + ".scaleX")
            else:
                cmds.disconnectAttr(cns + ".constraintScaleX", cnsSlave[0] + ".scaleX")
    
    def connectSyFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType != "scaleConstraint":
                continue
            if self.ui.connectSyQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintScaleY", cnsSlave[0] + ".scaleY")
            else:
                cmds.disconnectAttr(cns + ".constraintScaleY", cnsSlave[0] + ".scaleY")
        
    def connectSzFunc(self):
        if self._signalsBlocked:
            return
        for cns in self.constraintsInputLs:
            cnsType = cmds.nodeType(cns)
            cnsSlave = cmds.listConnections(cns + '.constraintParentInverseMatrix')
            if not cnsSlave or cnsType != "scaleConstraint":
                continue
            if self.ui.connectSzQCheck.isChecked():
                cmds.connectAttr(cns + ".constraintScaleZ", cnsSlave[0] + ".scaleZ")
            else:
                cmds.disconnectAttr(cns + ".constraintScaleZ", cnsSlave[0] + ".scaleZ")
    
    def mastersSelFunc(self):
        selectLs = []
        for master in self.ui.mastersQList.selectedItems():
            if master.text():
                selectLs.append( master.text() )
                continue
            else:
                masterWidget = self.ui.mastersQList.itemWidget(master)
                selectLs.append( masterWidget.ui.masterQLabel.text() )
        cmds.select(selectLs)
    
    def mastersFunc(self):
        self.ui.delMasterQButton.setEnabled(False)
        self.ui.replaceMasterQButton.setEnabled(False)
        self.ui.mastersSelQButton.setEnabled(False)
        if self.ui.mastersQList.selectedItems():
            self.ui.delMasterQButton.setEnabled(True)
            self.ui.replaceMasterQButton.setEnabled(True)
            self.ui.mastersSelQButton.setEnabled(True)
        if not self.parentWidget.ui.selectionSyncQButton.isChecked():
            self.mastersSelFunc()

    def mastersDisplayFunc(self):
        self.ui.mastersQList.clear()
        allMasters = []
        result = []
        self.masterWidget = False
        for cns in self.constraintsInputLs:
            allMasters.append( (set(cmds.listConnections(cns + ".target")) - {cns}) or []  )
        if not allMasters:
            return
        [result.extend(x) for x in allMasters]
        shared = list(reduce(lambda i, j: i & j, (x for x in allMasters)))
        if self.ui.displayOnlySharedQCheck.isChecked():
            result = shared[:]
        if len(allMasters) == 1:
            self.masterWidget = True
            for master in sorted(allMasters[0]):
                masterWidget = MasterQWidget(self, self.constraintsInputLs[0], master)
                item = QtWidgets.QListWidgetItem()
                item.setSizeHint(masterWidget.sizeHint())
                self.ui.mastersQList.addItem(item)
                self.ui.mastersQList.setItemWidget( item, masterWidget )
            return
        for master in sorted(set(result)):
            item = QtWidgets.QListWidgetItem(master)
            if master in shared:
                item.setBackground( QtGui.QColor('#b6633c') )
            self.ui.mastersQList.addItem( item )            

    def connectionRelatedItemsSelect(self):
        self.mastersDisplayFunc()
        self.setEnabledWidgets()
        self.getAttrInfo()

    def setEnabledWidgets(self):
        self.ui.addMasterQButton.setEnabled(False)
        self.ui.addMasterMOQCheck.setEnabled(False)
        self.ui.normalizeWeightsQButton.setEnabled(False)
        self.ui.lockOutputQCheck.setEnabled(False)
        self.ui.connectAllXQCheck.setEnabled(False)
        self.ui.connectAllYQCheck.setEnabled(False)
        self.ui.connectAllZQCheck.setEnabled(False)
        self.ui.connectAllTrQCheck.setEnabled(False)
        self.ui.connectAllRtQCheck.setEnabled(False)
        self.ui.connectAllScQCheck.setEnabled(False)
        self.ui.connectTxQCheck.setEnabled(False)
        self.ui.connectTyQCheck.setEnabled(False)
        self.ui.connectTzQCheck.setEnabled(False)
        self.ui.connectRxQCheck.setEnabled(False)
        self.ui.connectRyQCheck.setEnabled(False)
        self.ui.connectRzQCheck.setEnabled(False)
        self.ui.connectSxQCheck.setEnabled(False)
        self.ui.connectSyQCheck.setEnabled(False)
        self.ui.connectSzQCheck.setEnabled(False)
        self.ui.renameAttrQButton.setEnabled(False)
        cSelected = self.parentWidget.ui.relatedItemsQList.selectedItems()
        if not cSelected:
            return
        self.ui.addMasterQButton.setEnabled(True)
        self.ui.addMasterMOQCheck.setEnabled(True)
        self.ui.normalizeWeightsQButton.setEnabled(True)
        self.ui.lockOutputQCheck.setEnabled(True)
        self.ui.renameAttrQButton.setEnabled(True)
        for cns in cSelected:
            cType = cmds.nodeType(cns.text())
            if cType == "scaleConstraint":
                self.ui.connectAllScQCheck.setEnabled(True)
                self.ui.connectSxQCheck.setEnabled(True)
                self.ui.connectSyQCheck.setEnabled(True)
                self.ui.connectSzQCheck.setEnabled(True)
                continue
            if cType in ["pointConstraint","parentConstraint"]:
                self.ui.connectAllTrQCheck.setEnabled(True)
                self.ui.connectTxQCheck.setEnabled(True)
                self.ui.connectTyQCheck.setEnabled(True)
                self.ui.connectTzQCheck.setEnabled(True)
            if cType in ["normalConstraint", "aimConstraint", "orientConstraint","parentConstraint"]:
                self.ui.connectAllRtQCheck.setEnabled(True)
                self.ui.connectRxQCheck.setEnabled(True)
                self.ui.connectRyQCheck.setEnabled(True)
                self.ui.connectRzQCheck.setEnabled(True)
        self.ui.connectAllXQCheck.setEnabled(True)
        self.ui.connectAllYQCheck.setEnabled(True)
        self.ui.connectAllZQCheck.setEnabled(True)

    def getAttrInfo(self):
        cSelected = self.parentWidget.ui.relatedItemsQList.selectedItems()
        with BlockSignals(self):
            self.ui.lockOutputQCheck.setChecked(False)
            self.ui.connectAllXQCheck.setChecked(False)
            self.ui.connectAllYQCheck.setChecked(False)
            self.ui.connectAllZQCheck.setChecked(False)
            self.ui.connectAllTrQCheck.setChecked(False)
            self.ui.connectAllRtQCheck.setChecked(False)
            self.ui.connectAllScQCheck.setChecked(False)
            self.ui.connectTxQCheck.setChecked(False)
            self.ui.connectTyQCheck.setChecked(False)
            self.ui.connectTzQCheck.setChecked(False)
            self.ui.connectRxQCheck.setChecked(False)
            self.ui.connectRyQCheck.setChecked(False)
            self.ui.connectRzQCheck.setChecked(False)
            self.ui.connectSxQCheck.setChecked(False)
            self.ui.connectSyQCheck.setChecked(False)
            self.ui.connectSzQCheck.setChecked(False)
            for cns in cSelected:
                cnsType = cmds.nodeType(cns.text())
                cnsSlave = cmds.listConnections(cns.text() + '.constraintParentInverseMatrix')
                # lock output
                self.ui.lockOutputQCheck.setChecked(cmds.getAttr(cns.text() + ".lockOutput"))
                if not cnsSlave:
                    continue
                # connections
                if cnsType == "scaleConstraint":
                    if cmds.listConnections(cnsSlave[0] + ".scaleX", d=False):
                        self.ui.connectSxQCheck.setChecked(True)
                        self.ui.connectAllXQCheck.setChecked(True)
                        self.ui.connectAllScQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".scaleY", d=False):
                        self.ui.connectSyQCheck.setChecked(True)
                        self.ui.connectAllYQCheck.setChecked(True)
                        self.ui.connectAllScQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".scaleZ", d=False):
                        self.ui.connectSzQCheck.setChecked(True)
                        self.ui.connectAllZQCheck.setChecked(True)
                        self.ui.connectAllScQCheck.setChecked(True)
                    continue
                if cnsType in ["pointConstraint","parentConstraint"]:
                    if cmds.listConnections(cnsSlave[0] + ".translateX", d=False):
                        self.ui.connectTxQCheck.setChecked(True)
                        self.ui.connectAllXQCheck.setChecked(True)
                        self.ui.connectAllTrQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".translateY", d=False):
                        self.ui.connectTyQCheck.setChecked(True)
                        self.ui.connectAllYQCheck.setChecked(True)
                        self.ui.connectAllTrQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".translateZ", d=False):
                        self.ui.connectTzQCheck.setChecked(True)
                        self.ui.connectAllZQCheck.setChecked(True)
                        self.ui.connectAllTrQCheck.setChecked(True)
                if cnsType in ["normalConstraint","aimConstraint","orientConstraint","parentConstraint"]:
                    if cmds.listConnections(cnsSlave[0] + ".rotateX", d=False):
                        self.ui.connectRxQCheck.setChecked(True)
                        self.ui.connectAllXQCheck.setChecked(True)
                        self.ui.connectAllRtQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".rotateY", d=False):
                        self.ui.connectRyQCheck.setChecked(True)
                        self.ui.connectAllYQCheck.setChecked(True)
                        self.ui.connectAllRtQCheck.setChecked(True)
                    if cmds.listConnections(cnsSlave[0] + ".rotateZ", d=False):
                        self.ui.connectRzQCheck.setChecked(True)
                        self.ui.connectAllZQCheck.setChecked(True)
                        self.ui.connectAllRtQCheck.setChecked(True)
