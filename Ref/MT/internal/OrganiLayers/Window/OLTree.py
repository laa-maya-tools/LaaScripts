import Utils.Maya.MayaBridge as OLMayaBridge
from PySide2                    import QtWidgets, QtCore
from PySide2.QtCore             import Signal

from OrganiLayers.Window.OLIcons import OLIcons
from OrganiLayers.Window.OLTreeItem import OLTreeItem
from QtCustomWidgets.QtUtils import BlockSignals

class OLTree(QtWidgets.QTreeWidget):
    # TODO: Columns yet to add
    # Color
    headerIcons = [OLIcons.layerActiveIcon,
                    OLIcons.eyeIcon,           # visible **
                    OLIcons.playbackIcon,      # visibleOnPlayback **
                    OLIcons.BBoxIcon,          # displayAsBox (levelOfDetail) **
                    OLIcons.wireframeIcon,     # Shaded/Wire **
                    OLIcons.textureIcon,       # Textured **
                    OLIcons.snowFlakeIcon      #Frozen => displayType (Normal, Reference, Template)
                    ]
    
    columnClicked = Signal(OLTreeItem, int)
    
    def __init__(self, mainWindow, parent=None):
        super(OLTree, self).__init__(parent)
        
        self.mainWindow = mainWindow
        
        self.__visibleColumnsDirty = True
        self.__visibleColumns   = []
        self.__shiftKeyPressed  = False
        
        self._signalsBlocked    = False
        self._autoSelecting     = False
        self.sortingOrder       = QtCore.Qt.AscendingOrder
        
        # QAbstractView and QTreeWidget Config
        self.setAlternatingRowColors(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.setIndentation(15)
        self.setUniformRowHeights(True)
        self.setSortingEnabled(False)
        self.setExpandsOnDoubleClick(False)
        self.setColumnCount(5)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        
        # Header Config
        header = self.header()
        '''header.setSortIndicatorShown(True)
        header.setSortIndicator(0, QtCore.Qt.AscendingOrder)'''
        header.setStretchLastSection(False)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setMinimumSectionSize(5)
        header.setSectionsClickable(True)
        #header.resizeSection(1, 5)
        self.headerWidgetItem = QtWidgets.QTreeWidgetItem(["Name"])
        self.headerWidgetItem.setIcon(0, OLIcons.arrowUp)
        for column in range(1,len(self.headerIcons)):
            self.headerWidgetItem.setIcon(column, self.headerIcons[column])
        self.setHeaderItem(self.headerWidgetItem)
        header.sectionClicked.connect(self.headerSectionClicked)
        
        # ********* Signals
        self.itemExpanded.connect(self.treeItemExpanded)
        self.itemCollapsed.connect(self.treeItemCollapsed)
        self.itemDoubleClicked.connect(self.treeItemDoubleClicked)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.itemSelectionChanged.connect(self.treeItemSelectionChanged)
        self.columnClicked.connect(self.tree_Layers_columnClicked)
        
        # ********* Actions
        self.ActAddSelection    = QtWidgets.QAction("Add Selection", None)
        self.ActRemoveSelection = QtWidgets.QAction("Remove Selection", None)
        self.ActRename          = QtWidgets.QAction("Rename Layer", None)
        self.ActSelChildren     = QtWidgets.QAction("Select Children Items", None)
        self.ActSelChildrenRec  = QtWidgets.QAction("Select Children Items Recursively", None)
        self.ActMakeLayerActive = QtWidgets.QAction("Make Layer Active", None)
        
        self.ActAddSelection.triggered.connect(self.ActAddSelection_Triggered)
        self.ActRemoveSelection.triggered.connect(self.ActRemoveSelection_Triggered) 
        self.ActRename.triggered.connect(self.ActRename_Triggered)
        self.ActSelChildren.triggered.connect(self.ActSelChildren_Triggered)
        self.ActSelChildrenRec.triggered.connect(self.ActSelChildrenRec_Triggered)   
    
    # -------------------------------------------------
    # --------------- Custom Behaviour ----------------
    # -------------------------------------------------    
    def getSelectedLayers(self):
        return [item for item in self.selectedItems() if item.itemType == OLTreeItem.TreeItemType.layer]
    
    def getSelectedNodeItems(self):
        return [item for item in self.selectedItems() if item.itemType == OLTreeItem.TreeItemType.item]
    
    def getSelectedNodesFullPath(self):
        return [item.dataWrapper.name for item in self.selectedItems() if item.itemType == OLTreeItem.TreeItemType.item]
    
    def getLastSelectedLayer(self):
        selLayers = self.getSelectedLayers()
        if selLayers:
            return selLayers[len(selLayers)-1]
        else:
            return None
    
    def getLastSelectedItem(self):
        selectedItems = self.selectedItems()
        if (len(selectedItems) > 0):
            return selectedItems[len(selectedItems)-1]
        return None
    
    def getVisibleColumnsIndexes(self):
        if (self.__visibleColumnsDirty):
            self.__visibleColumns = []
            for idx in range(1,self.columnCount()):
                if (not self.isColumnHidden(idx)):
                    self.__visibleColumns.append(idx)
            self.__visibleColumnsDirty = False
        return self.__visibleColumns
    
    def setExpandedRecursive(self, item, value):
        for i in range(item.childCount()):
            child = item.child(i)
            child.setExpanded(value)
            self.setExpandedRecursive(child, value)
    
    def setColumnWidgetVisibility(self, column, value):
        self.setColumnHidden(column, not value)
        if (value):
            for i in range(self.topLevelItemCount()):
                self.topLevelItem(i).loadTreeItemWidgets([column], recursive=True)
        else:
            for i in range(self.topLevelItemCount()):
                self.topLevelItem(i).removeTreeItemWidget(column, recursive=True)
    
    def findLayerItemsByWrapperName(self, searchWrapper):
        matchingNameItems = self.findItems(searchWrapper.name, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 0)
        return [x for x in matchingNameItems if (x.dataWrapper == searchWrapper)]
    
    def findItemsByDagnode(self, arrayNodes, item=None):
        result = []
        
        if (not item):
            item = self.invisibleRootItem()
        
        if (isinstance(item, OLTreeItem) and item.itemType == OLTreeItem.TreeItemType.item and item.dataWrapper.dagNode.node in arrayNodes):
            result.append(item)
            arrayNodes.remove(item.dataWrapper.dagNode.node)
        
        for idx in range(item.childCount()):
            result += (self.findItemsByDagnode(arrayNodes, item.child(idx)))
            
        return result
    
    def expandToItem(self, item):
        self.setItemExpanded(item, True)
        
        parent = item.parent()
        
        if (isinstance(parent, QtWidgets.QTreeWidgetItem)):
            self.expandToItem(parent)
    
    def cleanSelection(self):
        for item in self.selectedItems():
            self.setItemSelected(item, False)
    
    def reloadSelected(self, *args):    # Callbacks may pass additional parameters that are not needed
        if (not self._autoSelecting):
            with (BlockSignals(self)):
                self.cleanSelection()
                selection = OLMayaBridge.getSelectedDAGNodes()
                if (selection):
                    itemsToSelect = self.findItemsByDagnode(selection)
                    for item in itemsToSelect:
                        self.setItemSelected(item, True)
        self._autoSelecting = False
    
    def showContextMenu(self, location):
        selectedItem = self.getLastSelectedItem()
        if selectedItem:
            menu = QtWidgets.QMenu(self)
            menu.addAction(self.ActAddSelection)
            #menu.addAction(self.ActRemoveSelection)
            menu.addSeparator()
            menu.addAction(self.ActRename)
            if (self.getLastSelectedItem().itemType == OLTreeItem.TreeItemType.layer):
                menu.addSeparator()
                menu.addAction(self.ActMakeLayerActive)
                menu.addSeparator()
                menu.addAction(self.ActSelChildren)
                menu.addAction(self.ActSelChildrenRec)
            menu.popup(self.mapToGlobal(location))
    
    # -------------------------------------------------
    # -------------- Override Functions ---------------
    # -------------------------------------------------
    def dropEvent(self, event):
        draggedItems = self.selectedItems()
        super(OLTree, self).dropEvent(event)
        newParentItem = draggedItems[0].parent() or draggedItems[0].treeWidget().invisibleRootItem()
        
        if (isinstance(newParentItem, OLTreeItem)):
            newParentItem = newParentItem.dataWrapper
        else:
            newParentItem = None
        
        for item in draggedItems:
            item.processDropEvent(newParentItem)
        
        self.sortByName(self.sortingOrder)
    
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Shift):
            self.__shiftKeyPressed = True
        elif (event.key() == QtCore.Qt.Key_F):
            selection = OLMayaBridge.getCurrentSelection() or []
            self.clearSelection()
            items = self.findItemsByDagnode(selection)
            for item in items:
                self.expandToItem(item)
                item.setSelected(True)
        else:
            event.ignore()
    
    def keyReleaseEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Shift):
            self.__shiftKeyPressed = False
        else:
            event.ignore()
    
    def setColumnHidden(self, column, value):
        self.__visibleColumnsDirty = True
        return super(OLTree, self).setColumnHidden(column, value)
    
    # -------------------------------------------------
    # --------------- Signals Actions -----------------
    # -------------------------------------------------
    def treeItemExpanded(self, item):
        for child in item.getSubItemChildren():
            child.loadTreeItemWidgets()
            pass
            
        if (self.__shiftKeyPressed):
            self.setExpandedRecursive(item, True)
    
    def treeItemCollapsed(self, item):
        if (self.__shiftKeyPressed):
            self.setExpandedRecursive(item, False)
    
    def treeItemDoubleClicked(self, item, recursive=False):
        if (item.itemType == OLTreeItem.TreeItemType.layer):
            with(BlockSignals(self)):
                item.SelectChildrenItems(recursive)
                self._autoSelecting = True
                OLMayaBridge.selectNodes(self.getSelectedNodesFullPath())
    
    def treeItemSelectionChanged(self):
        if (not self._signalsBlocked):
            selectedNodes = self.getSelectedNodesFullPath()
            with (BlockSignals(self)):
                if selectedNodes:
                    self._autoSelecting = True
                    OLMayaBridge.selectNodes(selectedNodes)
    
    def tree_Layers_columnClicked(self, item, column):
        selectedItems = self.selectedItems()
        if item in selectedItems:
            newValue = item.columnWidgets[column].isChecked()
            
            for l in selectedItems:
                blockedSignals  = l.blockCustomSignals(True)
                if l.columnWidgets[column]:
                    l.columnWidgets[column].setChecked(newValue)
                else:
                    l.btn_toggled(column, newValue)
                l.blockCustomSignals(blockedSignals)
    
    def headerSectionClicked(self, idx):
        #only sort when first header section clicked
        if (idx == 0):
            newOrder = QtCore.Qt.AscendingOrder
            if (self.sortingOrder == QtCore.Qt.AscendingOrder):
                newOrder = QtCore.Qt.DescendingOrder
            
            self.sortByName(newOrder)
    
    def sortByName(self, sortingOrder):
        self.setSortingEnabled(True)
        self.sortByColumn(0, sortingOrder)
        self.setSortingEnabled(False)
        self.header().setSectionsClickable(True)
        
        if (sortingOrder == QtCore.Qt.AscendingOrder):
            self.headerWidgetItem.setIcon(0, OLIcons.arrowUp)
        else:
            self.headerWidgetItem.setIcon(0, OLIcons.arrowDown)
        self.sortingOrder = sortingOrder
        
    # -------------------------------------------------
    # ------------- Actions Definitions ---------------
    # -------------------------------------------------
    def ActAddSelection_Triggered(self):
        lastSelectedItem = self.getLastSelectedItem()
        self.mainWindow.addNodesToLayer(OLMayaBridge.getSelectedDAGNodes(), lastSelectedItem)
    
    def ActRemoveSelection_Triggered(self):
        raise NotImplementedError()
    
    def ActRename_Triggered(self):
        lastSelectedItem = self.getLastSelectedItem()
        itmFlags = lastSelectedItem.flags()
        lastSelectedItem.setFlags(itmFlags | QtCore.Qt.ItemIsEditable)
        self.editItem(lastSelectedItem, 0)
        lastSelectedItem.setFlags(itmFlags)
    
    def ActSelChildren_Triggered(self):
        self.treeItemDoubleClicked(self.getLastSelectedItem())
    
    def ActSelChildrenRec_Triggered(self):
        self.treeItemDoubleClicked(self.getLastSelectedItem(), True)