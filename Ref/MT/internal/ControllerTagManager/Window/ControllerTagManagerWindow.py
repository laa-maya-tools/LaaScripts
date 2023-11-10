import maya.cmds as cmds
import pymel.core as pm

import WindowDockBase as wdBase

from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import QBrush, QColor
from PySide2.QtWidgets import QTreeWidgetItem

import ControllerTagManager as ctm

class ControllerTagManagerWindow(wdBase.UIDockManager):
    def __init__(self, parent=None):
        super(ControllerTagManagerWindow, self).__init__("Controller Tag Manager", r"C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/controllertagmanagerui.ui")
        self.setWindowTitle("Controller Tag Manager")
        
        self.resize(500,500)
        
        addIcon = QtGui.QIcon(":pickHandlesObj.png")
        deleteIcon = QtGui.QIcon(":UVTBRemove.png")
        self.ui.addButton.setText("")
        self.ui.addButton.setIcon(addIcon)
        self.ui.removeButton.setText("")
        self.ui.removeButton.setIcon(deleteIcon)
        
        treeStylesheet = '''QTreeView::branch:has-siblings:!adjoins-item {
            border-image: url(C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/icons/stylesheet-vline.png) 0;
        }

        QTreeView::branch:has-siblings:adjoins-item {
            border-image: url(C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/icons/stylesheet-branch-more.png) 0;
        }

        QTreeView::branch:!has-children:!has-siblings:adjoins-item {
            border-image: url(C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/icons/stylesheet-branch-end.png) 0;
        }

        QTreeView::branch:has-children:!has-siblings:closed,
        QTreeView::branch:closed:has-children:has-siblings {
                border-image: none;
                image: url(C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/icons/stylesheet-branch-closed.png);
        }

        QTreeView::branch:open:has-children:!has-siblings,
        QTreeView::branch:open:has-children:has-siblings  {
                border-image: none;
                image: url(C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/ControllerTagManager/Window/ui/icons/stylesheet-branch-open.png);
        }
        '''
        
        self.ui.tagsTreeWidget.setStyleSheet(treeStylesheet)
        
        self.defaultBrush = QBrush()
        self.selectedBrush = QBrush(QColor(51, 85, 107, 255))
        self.invalidBrush = QBrush(QColor(160, 40, 40, 255))
        
        self.ui.addButton.clicked.connect(self.OnAddElements)
        self.ui.removeButton.clicked.connect(self.OnRemoveElements)
        self.ui.exportButton.clicked.connect(self.OnExport)
        self.ui.importButton.clicked.connect(self.OnImport)
        self.ui.expandButton.clicked.connect(self.OnExpand)
        self.ui.collapseButton.clicked.connect(self.OnCollapse)
        self.ui.deleteTagsButton.clicked.connect(self.DeleteCurrentTags)
        self.ui.deleteInvalidTagsButton.clicked.connect(self.DeleteInvalidTags)
        self.ui.updateButton.clicked.connect(self.UpdateTags)
        self.ui.clearSelectionButton.clicked.connect(self.OnClearSelection)
        
        self.ui.tagsTreeWidget.selectionModel().selectionChanged.connect(self.OnSelectionChange)
        
        self.UpdateTags()

    def SelectionChanged(self):
        selectedItems = self.ui.tagsTreeWidget.selectedItems()
        parentsLabelText = ""
        instancesLabelText = ""
        childrenLabelText = ""
        childrenAmount = 0
        parentAmount = 0
        childrenText = ""
        parentText = ""
        
        itemInstances = 0
        allItems = self.GetAllItems()
        for item in allItems:
            item.setBackground(0, self.defaultBrush)
        # Paint selected tags
        for selectedItem in selectedItems:
            for item in allItems:
                if (item.text(0) == selectedItem.text(0)):
                    itemInstances += 1
                    item.setBackground(0, self.selectedBrush)
        # Paint invalid tags
        for item in allItems:
            if (cmds.objExists(item.text(0))):
                valid = ctm.IsValidTag(item.text(0))
                if (not valid):
                    item.setBackground(0, self.invalidBrush)
        
        for selectedItem in selectedItems:
            tagName = selectedItem.text(0)
            tagNode = pm.PyNode(tagName)
            childrenAmount += len(pm.listConnections(tagNode.children, type="controller"))
            for childTag in pm.listConnections(tagNode.children, type="controller"):
                childrenText += "- " + childTag.getName() + " "
            parentAmount += len(pm.listConnections(tagNode.parent, type="controller"))
            for parentTag in pm.listConnections(tagNode.parent, type="controller"):
                parentText += "- " + parentTag.getName() + " "
        if (len(selectedItems) > 0):
            parentsLabelText = "Parent tags: {} ( {})".format(parentAmount, parentText)
            instancesLabelText = "Hierarchy instances: {}".format(str(itemInstances))
            childrenLabelText = "Children tags: {} ( {})".format(childrenAmount, childrenText)
        self.ui.selectionParentsLabel.setText(parentsLabelText)
        self.ui.selectionInstancesLabel.setText(instancesLabelText)
        self.ui.selectionChildrenLabel.setText(childrenLabelText)
    
    def OnSelectionChange(self, selected, deselected):
        self.SelectionChanged()
    
    def OnClearSelection(self):
        self.ui.tagsTreeWidget.clearSelection()
        self.SelectionChanged()
    
    def CleanTree(self):
        topLevelItemCount = self.ui.tagsTreeWidget.topLevelItemCount()
        for i in reversed(range(topLevelItemCount)):
            self.ui.tagsTreeWidget.takeTopLevelItem(i)
    
    def GetChildrenItems(self, parentItem):
        childrenItems = []
        for i in range(parentItem.childCount()):
            childItem = parentItem.child(i)
            childrenItems.append(childItem)
            childrenItems.extend(self.GetChildrenItems(childItem))
        return childrenItems
    
    def GetAllItems(self):
        allItems = []
        topLevelItemCount = self.ui.tagsTreeWidget.topLevelItemCount()
        for i in range(topLevelItemCount):
            topLevelItem = self.ui.tagsTreeWidget.topLevelItem(i)
            allItems.append(topLevelItem)
            allItems.extend(self.GetChildrenItems(topLevelItem))
        return allItems
    
    def AddChildrenItems(self, parentTag, parentItem):
        childrenTags = pm.listConnections(parentTag.children, type="controller")
        for childTag in childrenTags:
            childItem = QTreeWidgetItem([childTag.getName()])
            parentItem.addChild(childItem)
            # Invalid tag
            if (not ctm.IsValidTag(childTag)):
                childItem.setBackground(0, self.invalidBrush)
            
            self.AddChildrenItems(childTag, childItem)
    
    def AddChildItem(self, childTag, parentItem):
        childItem = QTreeWidgetItem([childTag.getName()])
        parentItem.addChild(childItem)
        # Invalid tag
        if (not ctm.IsValidTag(childTag)):
            childItem.setBackground(0, self.invalidBrush)
            
        self.AddChildrenItems(childTag, childItem)
    
    def UpdateTags(self):
        self.CleanTree()
        
        currentTags = pm.ls(type="controller")
        for currentTag in currentTags:
            parentConns = pm.listConnections(currentTag.parent)
            # If it's a top level tag, add to dict and recursively find children tags
            if (len(parentConns) == 0):
                newItem = QTreeWidgetItem([currentTag.getName()])
                self.ui.tagsTreeWidget.addTopLevelItem(newItem)
                # Invalid tag
                if (not ctm.IsValidTag(currentTag)):
                    newItem.setBackground(0, self.invalidBrush)
                
                self.AddChildrenItems(currentTag, newItem)
        
        self.ui.tagsTreeWidget.expandAll()
    
    def DeleteCurrentTags(self):
        confirmValue = cmds.confirmDialog(title="Delete all tags", message="Do you want to delete all tags in the current scene?", button=["Yes","No"], defaultButton="Yes", cancelButton="No", dismissString="No")
        if (confirmValue.lower() == "yes"):
            ctm.DeleteAllTags()
            self.UpdateTags()
    
    def DeleteInvalidTags(self):
        confirmValue = cmds.confirmDialog(title="Delete invalid tags", message="Do you want to delete all invalid tags in the current scene?", button=["Yes","No"], defaultButton="Yes", cancelButton="No", dismissString="No")
        if (confirmValue.lower() == "yes"):
            invalidTags = ctm.GetInvalidTags()
            pm.delete(invalidTags)
            self.UpdateTags()
    
    def OnExpand(self):
        self.ui.tagsTreeWidget.expandAll()
    
    def OnCollapse(self):
        self.ui.tagsTreeWidget.collapseAll()
    
    def AddElements(self, selectedElements, selectedObjects):
        # Check reduntant relations to avoid them
        redundantChild = False
        if (len(selectedElements) > 0):
            for selectedElement in selectedElements:
                siblings = []
                for i in range(selectedElement.childCount()):
                    childItem = selectedElement.child(i)
                    siblings.append(childItem.text(0))
                for selectedObject in selectedObjects:
                    if (selectedObject.getName() in siblings):
                        redundantChild = True
        else:
            siblings = []
            topLevelItemCount = self.ui.tagsTreeWidget.topLevelItemCount()
            for i in range(topLevelItemCount):
                topLevelItem = self.ui.tagsTreeWidget.topLevelItem(i)
                siblings.append(topLevelItem.text(0))
            for selectedObject in selectedObjects:
                if (selectedObject.getName() in siblings):
                    redundantChild = True
        if (redundantChild):
            pm.confirmDialog(message="Redundant relation. An element can't be its own sibling", button="Close")
            return
        
        # Add tag nodes to scene
        connectionTuples = []
        if (len(selectedElements) > 0):
            for selectedElement in selectedElements:
                for selectedObject in selectedObjects:
                    parentControlTagName = selectedElement.text(0)
                    parentControl = ctm.GetTagNode(parentControlTagName)
                    connTuple = ctm.CreateChildTag(selectedObject, parentControl=parentControl)
                    if (connTuple != None):
                        connectionTuples.append(connTuple)
        else:
            for selectedObject in selectedObjects:
                connTuple = ctm.CreateChildTag(selectedObject, parentControl=None)
                if (connTuple != None):
                    connectionTuples.append(connTuple)
        
        # Check cyclic relations to disconnect connection tuples and avoid them
        cyclicRelation = False
        allTags = pm.ls(type="controller")
        for tag in allTags:
            cyclicRelation = ctm.HasCyclicRelation(tag)
            if (cyclicRelation):
                break
        if (cyclicRelation):
            for connectionTuple in connectionTuples:
                pm.disconnectAttr(connectionTuple[0], connectionTuple[1])
            pm.confirmDialog(message="Cyclic relation. An element can't be in its own hierarchy", button="Close")
            return
        
        # Add to tree
        if (len(selectedElements) > 0):
            for selectedElement in selectedElements:
                selectedElementInstances = []
                allItems = self.GetAllItems()
                for item in allItems:
                    if (item.text(0) == selectedElement.text(0)):
                        selectedElementInstances.append(item)
                for selectedElementInstance in selectedElementInstances:
                    for selectedObject in selectedObjects:
                        objectTag = pm.listConnections(selectedObject.message, type="controller")[0]
                        self.AddChildItem(objectTag, selectedElementInstance)
                # Expand
                selectedElement.setExpanded(True)
        else:
            for selectedObject in selectedObjects:
                newItem = QTreeWidgetItem([selectedObject.getName() + "_tag"])
                self.ui.tagsTreeWidget.addTopLevelItem(newItem)
    
    def OnAddElements(self):
        selectedElements = self.ui.tagsTreeWidget.selectedItems()
        selectedObjects = ctm.GetSelectedObjects()
        if (len(selectedObjects) > 0):
            # Check if elements are valid
            validElements = True
            for element in selectedElements:
                valid = ctm.IsValidTag(element.text(0))
                if (not valid):
                    validElements = False
                    pm.confirmDialog(message="Can't create child on invalid tag", button="Close")
                    break
            
            if (validElements):
                self.AddElements(selectedElements, selectedObjects)
                self.SelectionChanged()
        else:
            pm.confirmDialog(message="No objects selected", button="Close")
    
    def GetTagChildren(self, tag_node):
        nodes = []
        children = pm.listConnections(tag_node.children, type="controller")
        nodes.extend(children)
        for child in children:
            nodes.extend(self.GetTagChildren(child))
        return nodes
    
    def RemoveElements(self, elements):
        for element in reversed(elements):
            tagName = element.text(0)
            
            # Remove tag nodes from scene
            tagNode = pm.PyNode(tagName)
            
            parents = pm.listConnections(tagNode.parent, type="controller")
            parentsAmount = len(parents)
            # 'Try' in case this element was already deleted previously by a parent being removed
            try:
                # If there is a parent, disconnect the child tag
                if (parentsAmount > 0):
                    parentItem = element.parent()
                    parentTag = pm.PyNode(parentItem.text(0))
                    childIndex = ctm.GetChildIndex(tagNode, parentTag)
                    pm.disconnectAttr(tagNode.parent, parentTag.children[childIndex])
                if (parentsAmount <= 1):
                    tagChildren = self.GetTagChildren(tagNode)
                    toDelete = []
                    toDelete.append(tagNode)
                    toDelete.extend(tagChildren)
                    # Unique list
                    toDelete = list(set(toDelete))
                    pm.delete(toDelete)
            except IndexError:
                pass
            
            # Remove from tree
            allItems = self.GetAllItems()
            # If there are multiple parents, remove only this instance of this item
            if (parentsAmount > 1):
                parent = element.parent()
                if (parent != None):
                    parent.removeChild(element)
                else:
                    self.ui.tagsTreeWidget.takeTopLevelItem(self.ui.tagsTreeWidget.indexOfTopLevelItem(element))
            else:
                # If there is one parent or none, remove all instances of this item
                for item in reversed(allItems):
                    if (item.text(0) == tagName):
                        parent = item.parent()
                        if (parent != None):
                            parent.removeChild(item)
                        else:
                            self.ui.tagsTreeWidget.takeTopLevelItem(self.ui.tagsTreeWidget.indexOfTopLevelItem(element))
    
    def OnRemoveElements(self):
        selectedElements = self.ui.tagsTreeWidget.selectedItems()
        if (len(selectedElements) > 0):
            self.RemoveElements(selectedElements)
        self.OnClearSelection()
    
    def OnExport(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(self, "Export Tags", filter="JSON file (*.json)")
        if fileName:
            ctm.ExportControlTagsToFile(fileName)
    
    def OnImport(self):
        fileName, selectedFilter = QtWidgets.QFileDialog.getOpenFileName(self, "Import Tags", filter="JSON file (*.json)")
        if fileName:
            ctm.ImportControlTagsFromFile(fileName)
            self.UpdateTags()

if __name__ == "__main__":
    try:
        if controllerTagManagerWindow.isVisible():
            controllerTagManagerWindow.close()
    except NameError:
        pass
    controllerTagManagerWindow = ControllerTagManagerWindow()
    controllerTagManagerWindow.show()
