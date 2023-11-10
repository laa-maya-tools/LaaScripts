from PySide2 import QtCore, QtWidgets, QtGui

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds

import AnimSystems.KeyingGroup as KG

from Utils.Maya.UndoContext import UndoContext, UndoOff
import TimeSlider

from QtCustomWidgets.QtUtils import BlockSignals

import functools

class KeyingGroupTreeWidgetItemDelegate(QtWidgets.QStyledItemDelegate):
        
    SHOT_TEXT_ENABLED =                     QtGui.QColor.fromHsl(0, 0, 200)
    SHOT_TEXT_ENABLED_HIGHLIFHT =           QtGui.QColor.fromHsl(0, 0, 255)
    SHOT_TEXT_DISABLED =                    QtGui.QColor.fromHsl(0, 0, 128)
    SHOT_TEXT_DISABLED_HIGHLIGHT =          QtGui.QColor.fromHsl(0, 0, 154)
    
    SHOT_TEXT_CAMERA_SELECTED =             QtGui.QColor.fromRgb(126, 230, 126)
    SHOT_TEXT_CAMERA_SELECTED_HIGHLIGHT =   QtGui.QColor.fromRgb(140, 255, 140)
    
    SELECTION_HIGHLIGHT_COLOR =             QtGui.QColor.fromRgb(64, 96, 128)
    
    def __init__(self, treeWidget):
        super().__init__()
        
        self.treeWidget = treeWidget
    
    def paint(self, painter, option, index):
        self.initStyleOption(option, index)
        
        item = self.treeWidget.itemFromIndex(index)
        data = item.data(0, QtCore.Qt.UserRole)
        
        if type(data) == KG.KeyingGroup:
            if data.nodeExists():
                affectedAttributes = data.getAffectedAttributes(includeChildren=True, onlyEnabledChildren=False)
                selection = set(cmds.ls(selection=True))
                for attr in affectedAttributes:
                    node = attr.split(".")[0]
                    if node in selection:
                        painter.fillRect(option.rect, self.SELECTION_HIGHLIGHT_COLOR)
                        break
        else:
            selection = set(cmds.ls(selection=True))
            if data in selection:
                painter.fillRect(option.rect, self.SELECTION_HIGHLIGHT_COLOR)
            
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)

# This class was created late on the development of this tool.
# Many features on KeyingGroupWindow could be moved to this class.
class KeyingGroupTreeWidget(QtWidgets.QTreeWidget):
    
    def __init__(self, keyingGroupWindow):
        super().__init__()
        
        self.keyingGroupWindow = keyingGroupWindow

    def dropEvent(self, event : QtGui.QDropEvent):
        draggedItems = self.selectedItems()
        super().dropEvent(event)
        
        parentItem = draggedItems[0].parent()
        antecesors = []
        if parentItem:
            parentKeyingGroup = parentItem.data(0, QtCore.Qt.UserRole)
            p = parentKeyingGroup.getParentKeyingGroups()
            while p:
                antecesors += p
                p = p[0].getParentKeyingGroups()
        else:
            parentKeyingGroup = None
        
        keyingGroups = []
        affectedAttributes = []
        error = None
        for item in draggedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if type(data) == KG.KeyingGroup:
                if data in antecesors:
                    error = "Unable to reparent Keying Group: {} is already a parent of {}!".format(data, parentKeyingGroup)
                    break
                keyingGroups.append(data)
            elif item.childCount() > 0:
                attrs = [item.child(i).data(0, QtCore.Qt.UserRole) for i in range(item.childCount())]
                affectedAttributes += attrs
            else:
                affectedAttributes.append(data)
        
        if parentKeyingGroup: 
            if error:
                QtWidgets.QMessageBox.warning(self.keyingGroupWindow, "Drag Keying Group", error)
            else:
                with UndoContext("Drag Keying Group"):
                    for kg in keyingGroups:
                        parentKeyingGroup.addChildKeyingGroup(kg)
                    for attr in affectedAttributes:
                        currentKeyingGroup = cmds.listConnections(attr, s=False, d=True, type=KG.KeyingGroup._Type)
                        for kg in currentKeyingGroup:
                            KG.KeyingGroup(kg).removeAffectedAttribute(attr)
                        parentKeyingGroup.addAffectedAttribute(attr)
        
        else:
            with UndoContext("Drag Keying Group"):
                for kg in keyingGroups:
                    kg.clearParentKeyingGroups()
        
        self.keyingGroupWindow.reloadTreeWidget()
        
    def dragMoveEvent(self, event : QtGui.QDragMoveEvent):
        hoverItem = self.itemAt(event.pos())
        if not hoverItem:
            event.accept()
        else:
            data = hoverItem.data(0, QtCore.Qt.UserRole)
            if type(data) == KG.KeyingGroup:
                event.accept()
            else:
                event.ignore()
    
# TODO:
# + Deshabiltiar botones no usables? (por ejemplo en referencias?) (el botón de add attr también?)
# + Menú contextual:
#   - Create KeyingGroup
#   - Rename KeyingGroup
#   - Add to KeyingGroup
#   - Delete KeyingGroup
#   - Remove from KeyingGroup
#   - Expand Recursively
#   - Select Affected Attributes
#   - Select Children Recursively
class KeyingGroupWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    
    keyingGroupIcon = QtGui.QIcon(":out_parentConstraint.png")
    nodeItemIcon = QtGui.QIcon(":anisotropic.svg")
    attributeItemIcon = QtGui.QIcon(":dot.png")
    enableIcon = QtGui.QIcon()
    enableIcon.addPixmap(QtGui.QPixmap(":radio-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    enableIcon.addPixmap(QtGui.QPixmap(":precompExportChecked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    addIcon = QtGui.QIcon(":pickHandlesObj.png")
    deleteIcon = QtGui.QIcon(":delete.png")
    removeFromKeyingGroupIcon = QtGui.QIcon(":UVTBRemove.png")
    
    controlName = "KeyingGroupsManager"
    workspaceControlName = controlName + "WorkspaceControl"
    
    @classmethod
    def destroyInstance(cls):
        if cmds.workspaceControl(cls.workspaceControlName, q=True, exists=True):
            cmds.workspaceControl(cls.workspaceControlName, e=True, close=True)
            cmds.deleteUI(cls.workspaceControlName)
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.selectionChangedCallback = None
        self.undoCallback = None
        self.redoCallback = None
        
        self._signalsBlocked = False
        self._ignoreNextSelectionCall = False
        
        self.destroyInstance()
        self.setObjectName(self.controlName)
        self.setWindowTitle("Keying Group Manager")
        self.setWindowIcon(self.keyingGroupIcon)
        
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        
        topLayout = QtWidgets.QHBoxLayout()
        mainLayout.addLayout(topLayout)
        
        headerLabel = QtWidgets.QLabel("Keying Groups")
        topLayout.addWidget(headerLabel)
        
        topLayout.addStretch()
        
        exportKeyingGroupsButton = QtWidgets.QPushButton("Export")
        exportKeyingGroupsButton.setToolTip("Exports the scene's Keying Group configuration into a file so it can be restored or transferred easily.")
        exportKeyingGroupsButton.clicked.connect(self.onExportButtonPressed)
        topLayout.addWidget(exportKeyingGroupsButton)
        
        importKeyingGroupsButton = QtWidgets.QPushButton("Import")
        importKeyingGroupsButton.setToolTip("Imports a Keying Group configuration from a file.")
        importKeyingGroupsButton.clicked.connect(self.onImportButtonPressed)
        topLayout.addWidget(importKeyingGroupsButton)
    
        self.treeWidget = KeyingGroupTreeWidget(self)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setSelectionMode(QtWidgets.QTreeWidget.ExtendedSelection)
        mainLayout.addWidget(self.treeWidget)
        
        treeWidgetHeader : QtWidgets.QHeaderView = self.treeWidget.header()
        treeWidgetHeader.setMinimumSectionSize(1)
        treeWidgetHeader.setStretchLastSection(False)
        treeWidgetHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        treeWidgetHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        
        self.itemDelegate = KeyingGroupTreeWidgetItemDelegate(self.treeWidget)
        self.treeWidget.setItemDelegateForColumn(0, self.itemDelegate)
        
        self.treeWidget.itemSelectionChanged.connect(self.onTreeWidgetSelectionChanged)
        self.treeWidget.itemChanged.connect(self.onTreeWidgetItemChanged)
        
        bottomLayout = QtWidgets.QHBoxLayout()
        mainLayout.addLayout(bottomLayout)
        
        addKeyingGroupButton = QtWidgets.QPushButton("Create Keying Group")
        addKeyingGroupButton.setToolTip("Creates a new Keying Group.\nIf any Keying Group is selected, the new one will be parented to it.\nIf any other nodes are selected, their keyable attributes will be added to the new Keying Group.\nIf an attribute is selected on the Channel Box, only these attributes will be added.")
        addKeyingGroupButton.clicked.connect(self.onAddKeyingGroupButtonPressed)
        bottomLayout.addWidget(addKeyingGroupButton)
        
        bottomLayout.addStretch()
        
        checkDuplicatesButton = QtWidgets.QPushButton("Check Duplicates")
        checkDuplicatesButton.setToolTip("Checks for attributes present on several Keying Groups.")
        checkDuplicatesButton.clicked.connect(self.onCheckDuplicatesButtonPressed)
        bottomLayout.addWidget(checkDuplicatesButton)
        
        frameSelectedButton = QtWidgets.QPushButton("Frame Selected")
        frameSelectedButton.setToolTip("Frames the selected nodes on the list, expanding until they are visible.")
        frameSelectedButton.clicked.connect(self.onFrameSelectedButtonPressed)
        bottomLayout.addWidget(frameSelectedButton)
    
    def createCallbacks(self):
        self.selectionChangedCallback = cmds.scriptJob(e=["SelectionChanged", self.onSelectionChanged])
        self.undoCallback = cmds.scriptJob(e=["Undo", self.onUndo])
        self.redoCallback = cmds.scriptJob(e=["Redo", self.onUndo])
    
    def destroyCallbacks(self):
        cmds.scriptJob(kill=self.selectionChangedCallback)
        cmds.scriptJob(kill=self.undoCallback)
        cmds.scriptJob(kill=self.redoCallback)
    
    def reloadTreeWidget(self, keepExpanded=True, expandToSelection=False):
        if keepExpanded:
            expandedItems = set(self.getExpandedItemsData())
            currentScroll = self.treeWidget.verticalScrollBar().value()
        
        self.treeWidget.clear()
        
        keyingGroups = KG.KeyingGroup.getInstances()
        for kg in keyingGroups:
            parents = kg.getParentKeyingGroups()
            if len(parents) == 0:
                self.createKeyingGroupTreeItem(kg, self.treeWidget.addTopLevelItem, expandToSelection=expandToSelection)
                
        if keepExpanded:
            self.expandItems(expandedItems)
            self.treeWidget.updateGeometries()
            self.treeWidget.verticalScrollBar().setValue(currentScroll)
            
        with UndoOff():
            self.onSelectionChanged()
    
    def getExpandedItemsData(self, parent=None):
        if parent == None:
            items = [self.treeWidget.topLevelItem(i) for i in range(self.treeWidget.topLevelItemCount())]
        else:
            items = [parent.child(i) for i in range(parent.childCount())]
        
        expandedItems = []
        for item in items:
            if item.isExpanded():
                data = item.data(0, QtCore.Qt.UserRole)
                expandedItems.append(data)
            
            expandedItems += self.getExpandedItemsData(parent=item)
                
        return expandedItems
    
    def expandItems(self, expandedItems, parent=None):
        if parent == None:
            items = [self.treeWidget.topLevelItem(i) for i in range(self.treeWidget.topLevelItemCount())]
        else:
            items = [parent.child(i) for i in range(parent.childCount())]
        
        for item in items:
            data = item.data(0, QtCore.Qt.UserRole)
            if data and data in expandedItems:
                item.setExpanded(True)
            self.expandItems(expandedItems, parent=item)
    
    def expandToItems(self, expandedItems, scrollToItem=True, parent=None):
        if parent == None:
            items = [self.treeWidget.topLevelItem(i) for i in range(self.treeWidget.topLevelItemCount())]
        else:
            items = [parent.child(i) for i in range(parent.childCount())]
        
        for item in items:
            shouldBeExpanded = self.expandToItems(expandedItems, parent=item)
            if shouldBeExpanded:
                self.treeWidget.expandItem(item)
                return True
            
            data = item.data(0, QtCore.Qt.UserRole)
            if data and data in expandedItems:
                if scrollToItem:
                    self.treeWidget.scrollToItem(item)
                return True
        
        return False
    
    def createKeyingGroupTreeItem(self, keyingGroup, parentFn, expandToSelection=False):
        selection = cmds.ls(selection=True)
        
        item = QtWidgets.QTreeWidgetItem([keyingGroup.node])
        item.setData(0, QtCore.Qt.UserRole, keyingGroup)
        item.setIcon(0, self.keyingGroupIcon)
        flags = item.flags()
        flags |= QtCore.Qt.ItemIsEditable
        item.setFlags(flags)
        
        parentFn(item)
        
        enableButton = QtWidgets.QPushButton(self.enableIcon, "")
        enableButton.setCheckable(True)
        enableButton.setChecked(not keyingGroup.enabled) # For esthetic reasons the "enabled" state of the KeyingGroup is when the button is not checked
        enableButton.setToolTip("Enables or disables the Keying Group.")
        enableButton.toggled.connect(functools.partial(self.onEnableButtonToggled, item))
        
        addButton = QtWidgets.QPushButton(self.addIcon, "")
        addButton.setToolTip("Adds the selected node's keyable attributes to the KeyingGroup.\nIf an attribute is selected on the Channel Box, only these attributes will be added.")
        addButton.clicked.connect(functools.partial(self.onAddButtonClicked, item))
        
        deleteButton = QtWidgets.QPushButton(self.deleteIcon, "")
        deleteButton.setToolTip("Deletes the Keying Group and all it's children.")
        deleteButton.clicked.connect(functools.partial(self.onDeleteButtonClicked, item))
        
        self.treeWidget.setItemWidget(item, 1, enableButton)
        self.treeWidget.setItemWidget(item, 2, addButton)
        self.treeWidget.setItemWidget(item, 3, deleteButton)
        
        childKeyingGroups = keyingGroup.getChildKeyingGroups()
        for kg in childKeyingGroups:
            self.createKeyingGroupTreeItem(kg, item.addChild, expandToSelection=expandToSelection)
        
        attributes = keyingGroup.getAffectedAttributes(includeChildren=False)
        attributesPerObject = {}
        for attr in attributes:
            split = attr.split(".")
            node = split[0]
            
            if node not in attributesPerObject:
                attributesPerObject[node] = []
            attributesPerObject[node].append(attr)
        
        for node, attrs in attributesPerObject.items():
            nodeItem = QtWidgets.QTreeWidgetItem([node])
            nodeItem.setIcon(0, self.nodeItemIcon)
            nodeItem.setData(0, QtCore.Qt.UserRole, node)
            item.addChild(nodeItem)
            
            removeFromKeyingGroupButton = QtWidgets.QPushButton(self.removeFromKeyingGroupIcon, "")
            removeFromKeyingGroupButton.setToolTip("Removes all the node's attributes from the Keying Group.")
            removeFromKeyingGroupButton.clicked.connect(functools.partial(self.onRemoveFromKeyingGroupButtonClicked, nodeItem))
            
            self.treeWidget.setItemWidget(nodeItem, 3, removeFromKeyingGroupButton)
            
            if expandToSelection and node in selection:
                e = nodeItem.parent()
                while e != None:
                    e.setExpanded(True)
                    e = e.parent()
            
            for attr in attrs:
                attrItem = QtWidgets.QTreeWidgetItem([attr])
                attrItem.setIcon(0, self.attributeItemIcon)
                attrItem.setData(0, QtCore.Qt.UserRole, attr)
                nodeItem.addChild(attrItem)
                
                removeFromKeyingGroupButton = QtWidgets.QPushButton(self.removeFromKeyingGroupIcon, "")
                removeFromKeyingGroupButton.setToolTip("Removes the attribute from the Keying Group.")
                removeFromKeyingGroupButton.clicked.connect(functools.partial(self.onRemoveFromKeyingGroupButtonClicked, attrItem))
                
                self.treeWidget.setItemWidget(attrItem, 3, removeFromKeyingGroupButton)
            
        
        return item
    
    def addKeyingGroup(self, name=None, attributes=[], parentItem=None):
        if name == None:
            name, result = QtWidgets.QInputDialog.getText(self, "Create Keying Group", "Name:", QtWidgets.QLineEdit.Normal, "keyingGroup")
            if not (name and result):
                return
        
        with UndoContext("Create Keying Group"):
            keyingGroup = KG.KeyingGroup().create(nodeName=name, skipSelect=False)
            if attributes:
                for attr in attributes:
                    keyingGroup.addAffectedAttribute(attr)
            
            if parentItem:
                parent = parentItem.data(0, QtCore.Qt.UserRole)
                parent.addChildKeyingGroup(keyingGroup)
                parentFn = parentItem.addChild
            else:
                parentFn = self.treeWidget.addTopLevelItem
                
            item = self.createKeyingGroupTreeItem(keyingGroup, parentFn)
            item.setSelected(True)
            item.setExpanded(True)
            self.treeWidget.scrollToItem(item)
            
        return keyingGroup
    
    def getSelectedAttributes(self):
        selection = cmds.ls(selection=True)
        plugs = []
        selectedChannels = cmds.channelBox(TimeSlider.mainChannelBox, q=True, selectedMainAttributes=True) or []
        selectedChannels += cmds.channelBox(TimeSlider.mainChannelBox, q=True, selectedShapeAttributes=True) or []
        for obj in selection:
            if cmds.nodeType(obj) != KG.KeyingGroup._Type:
                attributes = cmds.listAttr(obj, keyable=True, unlocked=True, visible=True, read=True, connectable=True, sn=True)
                for attr in attributes:
                    if not selectedChannels or attr in selectedChannels:
                        plug = "{}.{}".format(obj, attr)
                        if not cmds.addAttr(plug, q=True, exists=True) or not cmds.addAttr(plug, q=True, usedAsProxy=True):    # Proxy attributes are ignored
                            plugs.append(plug)
        return plugs
    
    def onExportButtonPressed(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(self, "Export Keying Groups", filter="JSON file (*.json)")
        if fileName:
            rootKeyingGroups = [self.treeWidget.topLevelItem(i).data(0, QtCore.Qt.UserRole) for i in range(self.treeWidget.topLevelItemCount())]
            KG.exportKeyingGroupsToFile(rootKeyingGroups, fileName)
    
    def onImportButtonPressed(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(self, "Import Keying Groups", filter="JSON file (*.json)")
        if fileName:
            KG.importKeyingGroupsFromFile(fileName)
            self.reloadTreeWidget()
    
    def onAddKeyingGroupButtonPressed(self):
        selectedItems = self.treeWidget.selectedItems()
        parentItem = None
        for item in selectedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if type(data) == KG.KeyingGroup:
                parentItem = item
                break
            
        attributes = self.getSelectedAttributes()
        
        self.addKeyingGroup(attributes=attributes, parentItem=parentItem)
    
    def onCheckDuplicatesButtonPressed(self):
        conflicts = KG.getConflicts()
        if conflicts:
            message = "There are duplicates on the KeyingGroups!"
            for attr, keyingGroups in conflicts.items():
                message += "\n- {} is present on: {}".format(attr, KG.KeyingGroup.getNodeList(keyingGroups))
        else:
            message = "No conflicts."
        QtWidgets.QMessageBox.information(self, "Check Duplcates", message)
    
    def onFrameSelectedButtonPressed(self):
        self.expandToItems(cmds.ls(selection=True))
    
    def onTreeWidgetSelectionChanged(self):
        if self._signalsBlocked:
            return
        
        selectedItems = self.treeWidget.selectedItems()
        nodesToSelect = []
        for item in selectedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if data != None:
                if type(data) == KG.KeyingGroup:
                    data = data.node
                nodesToSelect.append(data)
        if nodesToSelect:
            self._ignoreNextSelectionCall = True
            cmds.select(nodesToSelect)
            self.treeWidget.viewport().update()
    
    def onTreeWidgetItemChanged(self, item, column):
        data = item.data(column, QtCore.Qt.UserRole)
        if type(data) == KG.KeyingGroup:
            with UndoContext("Rename Keying Group"):
                newName = data.renameNode(item.text(column))
                item.setText(column, newName)
    
    def onEnableButtonToggled(self, item, state):
        if not item.isSelected():
            selectedItems = [item]
        else:
            selectedItems = self.treeWidget.selectedItems()
        
        keyingGroups = []
        for item in selectedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if type(data) == KG.KeyingGroup:
                keyingGroups.append(data)
                
        if keyingGroups:
            with UndoContext("Set KeyingGroup Enabled"):
                for keyingGroup in keyingGroups:
                    keyingGroup.enabled = not state # For esthetic reasons the "enabled" state of the KeyingGroup is when the button is not checked
                self.reloadTreeWidget()
    
    def onAddButtonClicked(self, item):
        keyingGroup = item.data(0, QtCore.Qt.UserRole)
        
        attributes = self.getSelectedAttributes()
        if attributes:
            with UndoContext("Add Attributes to Keying Group"):
                for attr in attributes:
                    keyingGroup.addAffectedAttribute(attr)
                 
            self.reloadTreeWidget()
    
    def onDeleteButtonClicked(self, item):
        if not item.isSelected():
            selectedItems = [item]
        else:
            selectedItems = self.treeWidget.selectedItems()
            
        keyingGroups = []
        for item in selectedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if type(data) == KG.KeyingGroup:
                keyingGroups.append(data)
        
        if keyingGroups:
            keyinGroupsStr = ""
            for kg in keyingGroups:
                keyinGroupsStr += "\n- {}".format(kg.node)
            result = QtWidgets.QMessageBox.question(self, "Delete Keying Group", "Are you sure you want to delete the selected KeyingGroups?\n" + keyinGroupsStr)
            if result == QtWidgets.QMessageBox.Yes:
                with UndoContext("Delete Keying Groups"):
                    cmds.delete(KG.KeyingGroup.getNodeList(keyingGroups))
                
                self.reloadTreeWidget()
    
    def onRemoveFromKeyingGroupButtonClicked(self, item):
        if not item.isSelected():
            selectedItems = [item]
        else:
            selectedItems = self.treeWidget.selectedItems()
        
        keyingGroupAttrs = {}
        for item in selectedItems:
            data = item.data(0, QtCore.Qt.UserRole)
            if type(data) != KG.KeyingGroup:
                if item.childCount() > 0:
                    keyingGroup = item.parent().data(0, QtCore.Qt.UserRole)
                else:
                    keyingGroup = item.parent().parent().data(0, QtCore.Qt.UserRole)
                
                if keyingGroup not in keyingGroupAttrs:
                    keyingGroupAttrs[keyingGroup] = []
                    
                if item.childCount() > 0:
                    for i in range(item.childCount()):
                        keyingGroupAttrs[keyingGroup].append(item.child(i).data(0, QtCore.Qt.UserRole))
                else:
                    keyingGroupAttrs[keyingGroup].append(data)
        
        if keyingGroupAttrs:
            keyinGroupsStr = ""
            for kg in keyingGroupAttrs.keys():
                keyinGroupsStr += "\n- {}".format(kg.node)
                for attr in keyingGroupAttrs[kg]:
                    keyinGroupsStr += "\n    - {}".format(attr)
            result = QtWidgets.QMessageBox.question(self, "Remove Attributes From Keying Group", "Are you sure you want to remove the selected attributes from these KeyingGroups?\n" + keyinGroupsStr)
            if result == QtWidgets.QMessageBox.Yes:
                with UndoContext("Remove Attributes From Keying Group"):
                    for kg, attrs in keyingGroupAttrs.items():
                        for attr in attrs:
                            kg.removeAffectedAttribute(attr)
                
                self.reloadTreeWidget()
    
    def showEvent(self, event):
        self.reloadTreeWidget(keepExpanded=False, expandToSelection=True)
        
        self.createCallbacks()
    
    def hideEvent(self, event):
        self.destroyCallbacks()
    
    def onSelectionChanged(self, selection=None, item=None):
        if self._ignoreNextSelectionCall:
            self._ignoreNextSelectionCall = False
            return
        
        if selection == None:
            selection = cmds.ls(selection=True)
        
        if item == None:
            items = [self.treeWidget.topLevelItem(i) for i in range(self.treeWidget.topLevelItemCount())]
        else:
            items = [item.child(i) for i in range(item.childCount())]
        
        with BlockSignals(self):
            for item in items:
                data = item.data(0, QtCore.Qt.UserRole)
                if type(data) == KG.KeyingGroup:
                    data = data.node
                item.setSelected(data in selection)
                
                self.onSelectionChanged(selection=selection, item=item)
        
        self.treeWidget.viewport().update()
    
    def onUndo(self):
        self.reloadTreeWidget()
    

def show():
    ddd = KeyingGroupWindow()
    ddd.show(dockable=True)

if __name__ == "__main__":
    show()
