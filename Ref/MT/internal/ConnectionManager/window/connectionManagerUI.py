from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui, QtCore
import QtCustomWidgets.UIFileWidget as UIFileWidget
from QtCustomWidgets.QtUtils import BlockSignals
from ConnectionManager import connectionManager
import maya.cmds as cmds
import os

class ConnectionManagerWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__        = r"ConnectionManager\window\ui\connectionManager.ui"
    mainWidget         = None
    subWidget          = None
    inputLs            = []
    constraintsInputLs = []
    relatedItemsDict   = {}

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.setObjectName('ConnectionManager')
        self.setWindowTitle('Connection Manager')

        self._signalsBlocked = False
        # icons
        self.ui.refreshQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/refresh.png").copy(1, 1, 18, 18) )))
        self.ui.selectItemQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        self.ui.selectRelatedItemQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        self.ui.displayHierarchyModeQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/frameHierarchy.png").copy(1, 1, 18, 18) )))
        self.ui.displayListModeQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/out_list.png").copy(1, 1, 16, 16) )))
        self.ui.selectionSyncQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/syncOff.png").copy(1, 1, 16, 16) )))
        #
        self.ui.selectionSyncQButton.clicked.connect(self.selectionSyncFunc)
        self.ui.itemsQTree.itemSelectionChanged.connect(self.displayRelatedItemsConnectionsFunc)
        self.ui.itemsQTree.itemExpanded.connect(self.itemsQTreeExpandFunc)
        self.ui.itemsQTree.itemCollapsed.connect(self.itemsQTreeExpandFunc)
        self.ui.displayHierarchyModeQButton.clicked.connect(self.displayToogleFunc)
        self.ui.displayListModeQButton.clicked.connect(self.displayToogleFunc)
        self.ui.connectionFilterQCombo.addItems(connectionManager.mainWidgetsDict.keys())
        self.ui.connectionFilterQCombo.currentTextChanged.connect(self.addMainWidget)
        self.ui.selectRelatedItemQButton.clicked.connect(self.selectItemFunc)
        self.ui.selectItemQButton.clicked.connect(self.selectItemFunc)
        # related items
        self.ui.relatedItemsQList.itemSelectionChanged.connect(self.connectionRelatedItemsSelect)
        self.ui.displayLevelQSpin.valueChanged.connect(self.displayLevelFunc)
        self.ui.refreshQButton.clicked.connect(self.refreshFunc)
        self.addMainWidget()
        self.refreshFunc()
        
    def selectionSyncFunc(self):
        if self.ui.selectionSyncQButton.isChecked():
            self.ui.selectionSyncQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/syncOff.png").copy(1, 1, 16, 16) )))
            self.ui.selectItemQButton.setEnabled(True)
            self.ui.selectRelatedItemQButton.setEnabled(True)
        else:
            self.ui.selectionSyncQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/syncOn.png").copy(1, 1, 16, 16) )))
            self.ui.selectItemQButton.setEnabled(False)
            self.ui.selectRelatedItemQButton.setEnabled(False)

    def displayItemsFunc(self, asList=True):
        self.ui.itemsQTree.clear()
        if asList:
            for item in sorted(self.relatedItemsDict.keys()):
                if item != "_levels":
                    itemWidget = QtWidgets.QTreeWidgetItem(self.ui.itemsQTree, item.split("|")[-1])
                    itemWidget.setText(0, item.split("|")[-1])
        else:
            itemWidgetDict = {}
            iterableList = [k for k,v in self.relatedItemsDict.items() if k != "_levels" and not v]
            iterableList = sorted(iterableList, key=len)
            toExtend = [k for k,v in self.relatedItemsDict.items() if k != "_levels" and v]
            toExtend = sorted(toExtend, key=len)
            iterableList.extend( toExtend )
            for item in iterableList:
                itemParent = self.relatedItemsDict[item]
                if itemParent:
                    itemParentWidget = itemWidgetDict[ self.relatedItemsDict[item] ]
                else:
                    itemParentWidget = self.ui.itemsQTree
                itemWidgetDict[item] = QtWidgets.QTreeWidgetItem(itemParentWidget, item.split("|")[-1])
                itemWidgetDict[item].setText(0, item.split("|")[-1])

    def displayToogleFunc(self):
        self.ui.displayListModeQButton.setEnabled(False)
        self.ui.displayHierarchyModeQButton.setEnabled(False)
        if "list" in self.sender().objectName().lower():
            self.ui.displayHierarchyModeQButton.setEnabled(True)
            self.displayItemsFunc()
        else:
            self.ui.displayListModeQButton.setEnabled(True)
            self.displayItemsFunc(False)
        
    def selectItemFunc(self):
        cmds.select(clear=True)
        if "Related" in self.sender().objectName():
            widgetSource = self.ui.relatedItemsQList
        else:
            widgetSource = self.ui.itemsQTree
        for item in widgetSource.selectedItems():
            cmds.select(item.text(0) if widgetSource == self.ui.itemsQTree else item.text(), add=True)

    def connectionRelatedItemsSelect(self):
        relatedItemsSelected = [item.text() for item in self.ui.relatedItemsQList.selectedItems()]
        if not self.ui.selectionSyncQButton.isChecked():
            cmds.select( relatedItemsSelected )
        self.mainWidget.constraintsInputLs = relatedItemsSelected
        self.addSubWidget()
        self.mainWidget.connectionRelatedItemsSelect()
        
    def addSubWidget(self):
        while self.ui.subQWidget.layout().count():
            child = self.ui.subQWidget.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        relatedItems = self.ui.relatedItemsQList.selectedItems()
        if not relatedItems:
            return
        filterType = cmds.nodeType(relatedItems[0].text())
        if not all( [filterType == cmds.nodeType(item.text()) for item in relatedItems] ):
            return
        self.subWidget = connectionManager.subWidgetsDict[filterType]['widgetClass'].__call__(self, [item.text() for item in self.ui.relatedItemsQList.selectedItems()])
        self.ui.subQWidget.layout().addWidget(self.subWidget)

    def addMainWidget(self):
        filterValue = self.ui.connectionFilterQCombo.currentText()
        while self.ui.mainQWidget.layout().count():
            child = self.ui.mainQWidget.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.mainWidget = connectionManager.mainWidgetsDict[filterValue]['widgetClass'].__call__(self)
        self.ui.mainQWidget.layout().addWidget(self.mainWidget)
    
    def displayLevelFunc(self):
        if self.ui.displayLevelQSpin.value() == -1:
            displayLevel = 999
        else:
            displayLevel = self.ui.displayLevelQSpin.value()
        self.relatedItemsDict = {"_levels":abs(displayLevel)}
        if displayLevel == 0: # trabajar solo con la seleccion
            for elem in self.inputLs:
                self.relatedItemsDict[elem] = None
                for compare in self.inputLs:
                    if elem == compare:
                        continue
                    if elem in compare:
                        self.relatedItemsDict[compare] = elem
                    elif compare in elem:
                        self.relatedItemsDict[elem] = compare
        else: # ampliar a los padres
            tempLs = self.inputLs[:]
            for step in range(displayLevel):
                iterableList = tempLs[:]
                tempLs = []
                if not iterableList:
                    break
                for addItem in iterableList:
                    addItemParent = cmds.listRelatives(addItem, p=True, f=True)
                    if addItemParent:
                        self.relatedItemsDict[addItem] = addItemParent[0]
                        tempLs.append( addItemParent[0] )
                    else:
                        self.relatedItemsDict[addItem] = None
            for itemParent in tempLs:
                if itemParent not in self.relatedItemsDict.keys():
                    self.relatedItemsDict[itemParent] = None        
        self.displayItemsFunc(not self.ui.displayListModeQButton.isEnabled())
        self.displayRelatedItemsConnectionsFunc()
    
    def refreshFunc(self):
        self.ui.itemsQTree.clear()
        self.ui.relatedItemsQList.clear()
        sel = cmds.ls(sl=True, l=True)
        if not sel:
            return
        self.inputLs = sel
        filterValue = self.ui.connectionFilterQCombo.currentText()
        for elem in self.inputLs:
            if filterValue.lower() in cmds.nodeType(elem).lower():
                self.inputLs.remove(elem)
        self.displayLevelFunc()

    def itemExpandedFunc(self, item, value):
        for ind in range(item.childCount()):
            child = item.child(ind)
            child.setExpanded(value)
            self.itemExpandedFunc(child, value)
    
    def itemsQTreeExpandFunc(self, item):
        if self._signalsBlocked:
            return
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            value = item.isExpanded()
            with BlockSignals(self):
                self.itemExpandedFunc(item, value)
    
    def displayRelatedItemsConnectionsFunc(self):
        self.ui.relatedItemsQList.clear()
        filterValue = self.ui.connectionFilterQCombo.currentText()
        iterableList = []
        self.constraintsInputLs = []
        for item in self.ui.itemsQTree.selectedItems():
            iterableList.append( item.text(0) )
        if iterableList and not self.ui.selectionSyncQButton.isChecked():
                cmds.select( iterableList )
        elif not iterableList:
            iterableList = self.relatedItemsDict.keys()
        for item in iterableList:
            if item == "_levels":
                continue
            toAdd = set(cmds.listConnections(item, type=connectionManager.mainWidgetsDict[filterValue]['mayaNodeTypeFilter'], destination=False) or [])
            self.constraintsInputLs.extend( toAdd )
        result = self.mainWidget.relatedItemsFilter(self.constraintsInputLs)
        self.ui.relatedItemsQList.addItems( result )

def show():
    global connectionManager
    try:
        if connectionManager.isVisible():
            connectionManager.close()
    except NameError:
        pass
    connectionManager = ConnectionManagerWin()
    connectionManager.show()
