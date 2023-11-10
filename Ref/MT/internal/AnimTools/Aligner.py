from PySide2 import QtWidgets, QtGui, QtCore

from QtCustomWidgets.PickButton import QPickButton
import QtCustomWidgets.QtUtils as QtUtils

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.cmds as cmds

import AnimTools.CopyPasteWorld as CopyPasteWorld

from Utils.Maya.UndoContext import UndoContext

import functools

class NodePairList(QtWidgets.QFrame):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setContentsMargins(1, 1, 1, 1)
        self.layout().setSpacing(4)
        
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.setContentsMargins(4, 0, 4, 0)
        self.layout().addLayout(headerLayout)
        
        headerLabel = QtWidgets.QLabel("Node Pairs")
        headerLabel.setAlignment(QtCore.Qt.AlignBottom)
        headerLayout.addWidget(headerLabel)
        
        headerLayout.addStretch()
        
        addNodePairButton = QtWidgets.QPushButton()
        addNodePairButton.setFixedSize(23, 23)
        addNodePairButton.setIcon(QtGui.QIcon(":item_add.png"))
        addNodePairButton.setToolTip("Add Node Pair. If two objects are selected, a pair aligning the first node to the second one will be added.")
        addNodePairButton.clicked.connect(self.onAddNodePairButtonPressed)
        headerLayout.addWidget(addNodePairButton)
        
        self.nodePairTable = QtWidgets.QTableWidget()
        self.nodePairTable.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        self.nodePairTable.setStyleSheet("QHeaderView::section:horizontal { border: 1px solid; border-bottom: 2px solid; background-color: gray; } QTableWidget::item { border: 1px solid; }")
        self.nodePairTable.setColumnCount(5)
        self.nodePairTable.setHorizontalHeaderLabels(["", "Align...", "", "To...", ""])
        self.nodePairTable.verticalHeader().setVisible(False)
        self.nodePairTable.verticalHeader().setDefaultSectionSize(16)
        self.nodePairTable.horizontalHeader().setMinimumSectionSize(0)
        self.nodePairTable.horizontalHeader().setLineWidth(8)
        self.nodePairTable.horizontalHeader().resizeSection(0, 23)
        self.nodePairTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.nodePairTable.horizontalHeader().resizeSection(1, 64)
        self.nodePairTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.nodePairTable.horizontalHeader().resizeSection(2, 23)
        self.nodePairTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.nodePairTable.horizontalHeader().resizeSection(3, 64)
        self.nodePairTable.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.nodePairTable.horizontalHeader().resizeSection(4, 23)
        self.nodePairTable.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        self.nodePairTable.horizontalHeaderItem(0).setData(QtCore.Qt.ToolTipRole, "Click here to check or uncheck all pairs. Only checked pairs will be aligned.")
        self.nodePairTable.horizontalHeaderItem(0).setData(QtCore.Qt.DecorationRole, QtGui.QPixmap(":checkboxOn.png"))
        self.nodePairTable.horizontalHeaderItem(1).setData(QtCore.Qt.ToolTipRole, "The Source object. This node will be aligned to the Target.")
        self.nodePairTable.horizontalHeaderItem(2).setData(QtCore.Qt.ToolTipRole, "Click here to swap all pairs. This will swap the Sources and the Targets.")
        self.nodePairTable.horizontalHeaderItem(2).setData(QtCore.Qt.DecorationRole, QtGui.QPixmap(":cycle.png"))
        self.nodePairTable.horizontalHeaderItem(3).setData(QtCore.Qt.ToolTipRole, "The Target object. Where the Source node will be aligned to.")
        self.nodePairTable.horizontalHeaderItem(4).setData(QtCore.Qt.ToolTipRole, "Click here to remove all the pairs.")
        self.nodePairTable.horizontalHeaderItem(4).setData(QtCore.Qt.DecorationRole, QtGui.QPixmap(":delete.png"))
        self.nodePairTable.horizontalHeader().sectionClicked.connect(self.onHeaderSectionClicked)
        self.nodePairTable.horizontalHeader().sectionDoubleClicked.connect(self.onHeaderSectionClicked)
        self.layout().addWidget(self.nodePairTable)
        
        lowerButtonsWidget = QtWidgets.QWidget()
        lowerButtonsWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        lowerButtonsWidget.setLayout(QtWidgets.QHBoxLayout())
        lowerButtonsWidget.layout().setContentsMargins(0, 0, 0, 0)
        lowerButtonsWidget.layout().setSpacing(4)
        lowerButtonsWidget.layout().addStretch()
        self.layout().addWidget(lowerButtonsWidget)
        
    def isPairEnabled(self, row):
        cellWidget = self.nodePairTable.cellWidget(row, 0)
        checkBox = cellWidget.layout().itemAt(0).widget()
        return checkBox.isChecked()
        
    def setPairEnabled(self, row, enabled):
        cellWidget = self.nodePairTable.cellWidget(row, 0)
        checkBox = cellWidget.layout().itemAt(0).widget()
        checkBox.setChecked(enabled)
        
    def swapNodePair(self, row):
        sourcePickButton = self.nodePairTable.cellWidget(row, 1)
        targetPickButton = self.nodePairTable.cellWidget(row, 3)
        temp = sourcePickButton.getPickedObject()
        sourcePickButton.setPickedObject(targetPickButton.getPickedObject())
        targetPickButton.setPickedObject(temp)
        
    def getNodePairs(self, onlyEnabled=False):
        pairs = []
        for row in range(self.nodePairTable.rowCount()):
            if not onlyEnabled or self.isPairEnabled(row):
                source = self.nodePairTable.cellWidget(row, 1).getPickedObject()
                target = self.nodePairTable.cellWidget(row, 3).getPickedObject()
                if source:
                    source = cmds.ls(source, long=True)[0]
                if target:
                    target = cmds.ls(target, long=True)[0]
                pairs.append((source, target))
        return pairs
            
    def addNodePair(self, source=None, target=None):
        row = self.nodePairTable.rowCount()
        self.nodePairTable.insertRow(row)
        
        enabledWidget = QtWidgets.QWidget()
        enabledWidget.setLayout(QtWidgets.QHBoxLayout())
        enabledWidget.layout().setContentsMargins(0, 0, 0, 0)
        enabledWidget.layout().setAlignment(QtCore.Qt.AlignCenter)
        enabledCheckBox = QtWidgets.QCheckBox()
        enabledCheckBox.setChecked(True)
        enabledCheckBox.setToolTip("Uncheck this box to ignore this pair when aligning.")
        QtUtils.setPaletteColor(enabledCheckBox, QtGui.QPalette.Window, enabledCheckBox.palette().color(QtGui.QPalette.Foreground))
        enabledWidget.layout().addWidget(enabledCheckBox)
        
        sourcePickButton = QPickButton()
        sourcePickButton.setToolTip("Node to align. The Source will be aligned to the Target.")
        sourcePickButton.setPickedObject(source)
        
        targetPickButton = QPickButton()
        sourcePickButton.setToolTip("Where to align to. The Source will be aligned to the Target.")
        targetPickButton.setPickedObject(target)
        
        swapButton = QtWidgets.QPushButton()
        swapButton.setToolTip("Swap the Source and the Target of this pair.")
        swapButton.clicked.connect(functools.partial(self.onSwapButtonPressed, swapButton))
        swapButton.setIcon(QtGui.QIcon(":cycle.png"))
        
        deleteButton = QtWidgets.QPushButton()
        deleteButton.setToolTip("Remove this align pair.")
        deleteButton.clicked.connect(functools.partial(self.onDeleteButtonPressed, deleteButton))
        deleteButton.setIcon(QtGui.QIcon(":delete.png"))
        
        self.nodePairTable.setCellWidget(row, 0, enabledWidget)
        self.nodePairTable.setCellWidget(row, 1, sourcePickButton)
        self.nodePairTable.setCellWidget(row, 2, swapButton)
        self.nodePairTable.setCellWidget(row, 3, targetPickButton)
        self.nodePairTable.setCellWidget(row, 4, deleteButton)
    
    def addNodePairFromSelection(self):
        selection = cmds.ls(selection=True)
        if len(selection) == 2:
            self.addNodePair(source=selection[0], target=selection[1])
        else:
            self.addNodePair()
    
    def clearNodePairs(self):
        self.nodePairTable.setRowCount(0)
    
    def onDeleteButtonPressed(self, deleteButton):
        for row in range(self.nodePairTable.rowCount()):
            widget = self.nodePairTable.cellWidget(row, 4)
            if widget == deleteButton:
                self.nodePairTable.removeRow(row)
                break
            
    def onSwapButtonPressed(self, swapButton):
        for row in range(self.nodePairTable.rowCount()):
            widget = self.nodePairTable.cellWidget(row, 2)
            if widget == swapButton:
                self.swapNodePair(row)
                break
    
    def onHeaderSectionClicked(self, index):
        if index == 0:
            if self.nodePairTable.rowCount() > 0:
                newState = not self.isPairEnabled(0)
                for row in range(self.nodePairTable.rowCount()):
                    self.setPairEnabled(row, newState)
            
        elif index == 2:
            for row in range(self.nodePairTable.rowCount()):
                self.swapNodePair(row)
            
        elif index == 4:
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self, "Aligner", "Are you sure you want to clear the align list?"):
                self.clearNodePairs()
    
    def onAddNodePairButtonPressed(self):
        self.addNodePairFromSelection()
    

class AlignerWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    savedPairs = None
    savedRangeOption = None
    savedAlignAtOption = None
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle("Aligner")

        self.setLayout(QtWidgets.QVBoxLayout())
        
        self.alignList = NodePairList()
        self.layout().addWidget(self.alignList)
        
        rangeGroupBox = QtWidgets.QGroupBox("Range")
        rangeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        rangeGroupBox.layout().setContentsMargins(5, 2, 5, 5)
        rangeGroupBox.layout().setSpacing(1)
        self.layout().addWidget(rangeGroupBox)
        
        self.selectedRangeRadioButton = QtWidgets.QRadioButton("Selected Range")
        self.selectedRangeRadioButton.setToolTip("Aligns on the selected range. If no range is selected, only aligns on the current frame.")
        rangeGroupBox.layout().addWidget(self.selectedRangeRadioButton)
        
        self.animationRangeRadioButton = QtWidgets.QRadioButton("Animation Range")
        self.animationRangeRadioButton.setToolTip("Aligns on the current animation range.")
        rangeGroupBox.layout().addWidget(self.animationRangeRadioButton)
        
        self.allKeysRadioButton = QtWidgets.QRadioButton("All Keys")
        self.allKeysRadioButton.setToolTip("Aligns on the full animated range of the Target object.")
        rangeGroupBox.layout().addWidget(self.allKeysRadioButton)
        
        self.selectedRangeRadioButton.setChecked(True)
    
        alignAtGroupBox = QtWidgets.QGroupBox("Align At...")
        alignAtGroupBox.setLayout(QtWidgets.QVBoxLayout())
        alignAtGroupBox.layout().setContentsMargins(5, 2, 5, 5)
        alignAtGroupBox.layout().setSpacing(1)
        self.layout().addWidget(alignAtGroupBox)
        
        self.bakeRadioButton = QtWidgets.QRadioButton("Every Frame (Bake)")
        self.bakeRadioButton.setToolTip("Aligns on each frame on the range.")
        alignAtGroupBox.layout().addWidget(self.bakeRadioButton)
        
        self.sourceKeysRadioButton = QtWidgets.QRadioButton("Source Object Keys")
        self.sourceKeysRadioButton.setToolTip("Aligns only when the Source object has keys (the node being aligned).")
        alignAtGroupBox.layout().addWidget(self.sourceKeysRadioButton)
        
        self.targetKeysRadioButton = QtWidgets.QRadioButton("Target Object Keys")
        self.targetKeysRadioButton.setToolTip("Aligns only when the Target object has keys (the node defining where to align to).")
        alignAtGroupBox.layout().addWidget(self.targetKeysRadioButton)
        
        self.bothKeysRadioButton = QtWidgets.QRadioButton("Both Objects Keys")
        self.bothKeysRadioButton.setToolTip("Aligns only when either the Source or the Target objects have keys.")
        alignAtGroupBox.layout().addWidget(self.bothKeysRadioButton)
        
        self.bakeRadioButton.setChecked(True)
    
        alignButton = QtWidgets.QPushButton("Align")
        alignButton.setToolTip("Aligns all the pairs on the list. Only the pairs with their checkbox marked will be aligned.")
        alignButton.clicked.connect(self.onAlignButtonPressed)
        self.layout().addWidget(alignButton)
        
    def onAlignButtonPressed(self):
        nodePairs = self.alignList.getNodePairs(onlyEnabled=True)
        remaps = dict(nodePairs)
        sources = list(remaps.keys())
        targets = list(remaps.values())
        
        if None in sources or None in targets:
            QtWidgets.QMessageBox.warning(self, "Aligner", "Empty align field. Please fill it or remove the line.")
            return
        
        if self.selectedRangeRadioButton.isChecked():
            animRange = CopyPasteWorld.getSelectedAnimRange()
        elif self.animationRangeRadioButton.isChecked():
            start = cmds.playbackOptions(q=True, min=True)
            end = cmds.playbackOptions(q=True, max=True)
            animRange = (start, end)
        else:
            animRange = None
        
        bake = self.bakeRadioButton.isChecked() or (animRange and animRange[0] == animRange[1])
        
        if self.sourceKeysRadioButton.isChecked() or self.bothKeysRadioButton.isChecked():
            copyTimes = {}
            for source, target in nodePairs:
                copyTimes[target] = CopyPasteWorld.getTransformKeyTimes(source, animRange)
            if self.bothKeysRadioButton.isChecked():
                for _, target in nodePairs:
                    copyTimes[target] += CopyPasteWorld.getTransformKeyTimes(target, animRange)
        else:
            copyTimes = None
        
        with UndoContext("Align"):
            transformData = CopyPasteWorld.copyWorldTransform(targets, animRange=animRange, bake=bake, copyTimes=copyTimes)
            CopyPasteWorld.pasteWorldTransform(transformData, nodes=sources, remaps=remaps)
        
    def showEvent(self, event):
        if AlignerWindow.savedPairs:
            self.alignList.clearNodePairs()
            for source, target in AlignerWindow.savedPairs:
                if source and target and cmds.objExists(source) and cmds.objExists(target):
                    self.alignList.addNodePair(source=source, target=target)
        
        if AlignerWindow.savedRangeOption:
            self.selectedRangeRadioButton.setChecked(AlignerWindow.savedRangeOption[0])
            self.animationRangeRadioButton.setChecked(AlignerWindow.savedRangeOption[1])
            self.allKeysRadioButton.setChecked(AlignerWindow.savedRangeOption[2])
        
        if AlignerWindow.savedAlignAtOption:
            self.bakeRadioButton.setChecked(AlignerWindow.savedAlignAtOption[0])
            self.sourceKeysRadioButton.setChecked(AlignerWindow.savedAlignAtOption[1])
            self.targetKeysRadioButton.setChecked(AlignerWindow.savedAlignAtOption[2])
            self.bothKeysRadioButton.setChecked(AlignerWindow.savedAlignAtOption[3])
        
        if len(self.alignList.getNodePairs()) == 0:
            self.alignList.addNodePairFromSelection()
        
    def hideEvent(self, event):
        AlignerWindow.savedPairs = self.alignList.getNodePairs()
        AlignerWindow.savedRangeOption = [self.selectedRangeRadioButton.isChecked(), self.animationRangeRadioButton.isChecked(), self.allKeysRadioButton.isChecked()]
        AlignerWindow.savedAlignAtOption = [self.bakeRadioButton.isChecked(), self.sourceKeysRadioButton.isChecked(), self.targetKeysRadioButton.isChecked(), self.bothKeysRadioButton.isChecked()]
        

instance = None

def show():
    global instance
    if instance != None and instance.isVisible():
        instance.close()
    
    instance = AlignerWindow()
    instance.show()

if __name__ == "__main__":
    show()
