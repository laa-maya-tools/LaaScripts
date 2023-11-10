from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

from PySide2 import QtCore, QtWidgets, QtGui

import maya.cmds as cmds

import ActorManager
import ProjectPath

import os

class ActorBrowser(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    ACTOR_ITEM_RIG_TYPE = QtWidgets.QTreeWidgetItem.UserType + 1
    ACTOR_ITEM_ANIM_TYPE = QtWidgets.QTreeWidgetItem.UserType + 2
    ACTOR_ITEM_FONT = QtGui.QFont()
    ACTOR_ITEM_FONT.setBold(True)
    
    FOLDER_FOREGROUND_COLOR = QtGui.QColor.fromHsl(0, 0, 172)
    
    def __init__(self, callback=None, addNumberToNamespace=False, parent=None):
        super().__init__(parent=parent)
        
        self.callback = callback
        self.addNumberToNamespace = addNumberToNamespace
        
        self.importedNamespace = None
        
        self.setWindowTitle("Actor Browser")
        self.setWindowIcon(QtGui.QIcon(":character.svg"))
        
        mainLayout  = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        
        actorTreeGroupBox = QtWidgets.QGroupBox("Actors")
        actorTreeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        actorTreeGroupBox.layout().setContentsMargins(3,2,3,2)
        mainLayout.addWidget(actorTreeGroupBox)
        
        self.actorTree = QtWidgets.QTreeWidget()
        self.actorTree.setHeaderHidden(True)
        self.actorTree.setStyleSheet("QTreeView::branch:!has-children:adjoins-item {border-image: url(:np-head.png) 1;}")
        self.actorTree.itemSelectionChanged.connect(self.onActorTreeSelectionChanged)
        self.actorTree.itemDoubleClicked.connect(self.onActorTreeItemDoubleClicked)
        actorTreeGroupBox.layout().addWidget(self.actorTree)
        
        mergeActorGroupBox = QtWidgets.QGroupBox("Merge")
        mergeActorGroupBox.setLayout(QtWidgets.QGridLayout())
        mainLayout.addWidget(mergeActorGroupBox)
        
        namespaceTextLabel = QtWidgets.QLabel("Namespace")
        self.namespaceTextField = QtWidgets.QLineEdit()
        mergeActorGroupBox.layout().addWidget(namespaceTextLabel)
        mergeActorGroupBox.layout().addWidget(self.namespaceTextField)
        
        self.mergeActorButton = QtWidgets.QPushButton("Merge Actor")
        self.mergeActorButton.setEnabled(False)
        self.mergeActorButton.clicked.connect(self.onMergeActorButtonPressed)
        mergeActorGroupBox.layout().addWidget(self.mergeActorButton)
        
    def getSelectedItem(self):
        selectedItems = self.actorTree.selectedItems()
        if selectedItems:
            return selectedItems[0]
        else:
            return None
        
    def fillActorTree(self):
        self.actorTree.clear()
        
        actorFolderToken = os.path.join(ProjectPath.Tokens.curled(ProjectPath.Tokens.T3DActors))
        pathTokenizer = ProjectPath.PathTokenizer()
        actorFolder = pathTokenizer.Translate(actorFolderToken)
        
        folderItems = os.listdir(actorFolder)
        for folderItem in folderItems:
            subItems, isActor = self.addElementToTree(actorFolder, folderItem)
            for subItem in subItems:
                self.actorTree.addTopLevelItem(subItem)
                
        self.expandDefaultActor()
    
    def getActorItem(self, path, subItem):
        subItemPath = os.path.join(path, subItem)
        if os.path.isfile(subItemPath):
            split = subItem.split(".")
            fileName = split[0]
            extension = split[1].lower()
            if extension == "mb" or extension == "ma":
                fileType = None
                if fileName.lower().endswith("_rig"):
                    fileType = ActorBrowser.ACTOR_ITEM_RIG_TYPE
                    actorName = fileName[:-4]
                elif fileName.lower().endswith("_anim"):
                    fileType = ActorBrowser.ACTOR_ITEM_ANIM_TYPE
                    actorName = fileName[:-5]
                if fileType != None:
                    item = QtWidgets.QTreeWidgetItem(type=fileType)
                    item.setSizeHint(0, QtCore.QSize(0, 18))
                    item.setText(0, actorName.capitalize())
                    item.setData(0, QtCore.Qt.UserRole, subItemPath)
                    item.setFont(0, ActorBrowser.ACTOR_ITEM_FONT)
                    item.setToolTip(0, subItemPath)
                    return item
        return None
    
    def addElementToTree(self, folder, folderItem):
        path = os.path.join(folder, folderItem)
        
        if not os.path.isfile(path):
            subItems = os.listdir(path)
            actorItems = {}
            for subItem in subItems:
                actorItem = self.getActorItem(path, subItem)
                if actorItem != None:
                    actorName = actorItem.text(0)
                    if (actorName not in actorItems) or (actorItem.type() == ActorBrowser.ACTOR_ITEM_ANIM_TYPE):
                        actorItems[actorName] = actorItem
                        
            if actorItems:
                return list(actorItems.values()), True
            
            else:
                item = QtWidgets.QTreeWidgetItem()
                item.setText(0, folderItem)
                item.setForeground(0, ActorBrowser.FOLDER_FOREGROUND_COLOR)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable)
                shouldSimplify = False
                for subItem in subItems:
                    items, isActor = self.addElementToTree(path, subItem)
                    item.addChildren(items)
                    shouldSimplify |= isActor
                if shouldSimplify and item.childCount() == 1:
                    return [item.takeChild(0)], False
                elif item.childCount() > 0:
                    return [item], False
            
        return [], False
    
    def expandDefaultActor(self, items=None, defaultActor="Samus"):
        if items == None:
            items = [self.actorTree.topLevelItem(i) for i in range(self.actorTree.topLevelItemCount())]
        
        for item in items:
            if item.type() == ActorBrowser.ACTOR_ITEM_ANIM_TYPE and item.text(0).lower() == defaultActor.lower():
                return True
            else:
                children = [item.child(i) for i in range(item.childCount())]
                expanded = self.expandDefaultActor(children, defaultActor=defaultActor)
                if expanded:
                    item.setExpanded(True)
                    return True
        return False
    
    def referenceActor(self, filePath, namespace):
        self.importedNamespace = ActorManager.createActorReference(filePath, namespace=namespace)
        if self.importedNamespace:
            self.accept()
            if self.callback:
                self.callback(self.importedNamespace)
        
    def mergeActor(self, filePath, namespace):
        self.importedNamespace = ActorManager.mergeActorAnimFile(filePath, namespace=namespace)
        if self.importedNamespace:
            self.accept()
            if self.callback:
                self.callback(self.importedNamespace)
    
    def onActorTreeSelectionChanged(self):
        selectedItem = self.getSelectedItem()
        if selectedItem:
            actorName = selectedItem.text(0)
            namespace = ActorManager.getNextAvailableNamespace(actorName, forceNumber=self.addNumberToNamespace)
            self.namespaceTextField.setText(namespace)
            
            self.namespaceTextField.setEnabled(True)
            self.mergeActorButton.setEnabled(True)
            
        else:
            self.namespaceTextField.setEnabled(False)
            self.mergeActorButton.setEnabled(False)
            
    def onActorTreeItemDoubleClicked(self, item, column):
        try:
            if item.type() == ActorBrowser.ACTOR_ITEM_RIG_TYPE:
                actorPath = item.data(0, QtCore.Qt.UserRole)
                namespace = ActorManager.getNextAvailableNamespace(item.text(0), forceNumber=self.addNumberToNamespace)
                self.referenceActor(actorPath, namespace)
            elif item.type() == ActorBrowser.ACTOR_ITEM_ANIM_TYPE:
                actorPath = item.data(0, QtCore.Qt.UserRole)
                namespace = ActorManager.getNextAvailableNamespace(item.text(0), forceNumber=self.addNumberToNamespace)
                self.mergeActor(actorPath, namespace)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Actor Browser", str(e))
    
    def onMergeActorButtonPressed(self):
        namespace = self.namespaceTextField.text()
        if not namespace:
            QtWidgets.QMessageBox.warning(self, "Merge Actor", "You must set a namespace for the actor!")
            return
        elif cmds.namespace(ex=namespace):
            result = QtWidgets.QMessageBox.question(self, "Merge Actor", "The namespace {} is already in use, do you want to use the next available number?".format(namespace))
            if result == QtWidgets.QMessageBox.Yes:
                namespace = ActorManager.getNextAvailableNamespace(namespace, forceNumber=self.addNumberToNamespace)
            else:
                return
        
        try:
            selectedItem = self.getSelectedItem()
            if selectedItem:
                actorPath = selectedItem.data(0, QtCore.Qt.UserRole)
                if selectedItem.type() == ActorBrowser.ACTOR_ITEM_RIG_TYPE:
                    self.referenceActor(actorPath, namespace)
                elif selectedItem.type() == ActorBrowser.ACTOR_ITEM_ANIM_TYPE:
                    self.mergeActor(actorPath, namespace)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Actor Browser", str(e))
    
    def showEvent(self, event):
        self.fillActorTree()


def show(addNumberToNamespace=False):
    ActorBrowser(addNumberToNamespace=addNumberToNamespace).show()

if __name__ == "__main__":
    show()