from PySide2                    import QtWidgets, QtCore

#import OrganiLayers.Window.lib.MayaBridge as OLMayaBridge
import Utils.Maya.MayaBridge                as OLMayaBridge
import functools

from OrganiLayers.Window.OLIcons        import OLIcons
from OrganiLayers.Window.lib.Classes    import Messages
from OrganiLayers.Window.lib.CustomWidgets import ShowMessage

class OLTreeItem(QtWidgets.QTreeWidgetItem):
    class TreeItemType():
        layer = 0
        item  = 1
    
    columnIcons = [OLIcons.layerInactiveIcon,
                    OLIcons.var_visibilityIcon,
                    OLIcons.var_hideOnPlaybackIcon,
                    OLIcons.var_LodIcon,
                    OLIcons.var_shadingIcon,
                    OLIcons.var_texturedIcon,
                    OLIcons.var_frozenIcon]
    
    def __init__(self, parent, text, dataWrapper, icon=None, itemType=TreeItemType.layer):
        super(OLTreeItem, self).__init__(parent, [text])
        self.itemType       = itemType
        self.dataWrapper    = dataWrapper
        self.__blockCustomSignals = False
        self.__scriptJobIDs = []
        self.__openValues   = [None, 1, 0, 0, 1, 1, 0]
        
        #self.columnWidgets = [None, self.btn_Col1, self.btn_Col2, self.btn_Col3, self.btn_Col4, self.btn_Col5, self.btn_Col6]
        self.columnWidgets = [None]*7
        
        # Set Flags
        if (itemType == self.TreeItemType.layer):
            self.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled) #| QtCore.Qt.ItemIsEditable
        else:
            self.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled) #| QtCore.Qt.ItemIsEditable
            self.__scriptJobIDs = self.registerCallbacks()
        
        # Column 0
        #self.setText(0, text)
        if icon:
            self.setIcon(0, icon)
        
        # Column 1-5
        if (parent):
            self.loadTreeItemWidgets()
    
    # -------------------------------------------------
    # --------------- Custom Behaviour ----------------
    # -------------------------------------------------
    def getChecksStatus(self):
        return[0, self.dataWrapper.visibility, self.dataWrapper.hideOnPlayback, self.dataWrapper.levelOfDetail, self.dataWrapper.shading, self.dataWrapper.texturing, 1 if self.dataWrapper.displayType else 0]
    
    def getChildren(self):
        result = []
        for i in (range(self.childCount())):
            result.append(self.child(i))
        return result
    
    def getSubLayerChildren(self):
        return [item for item in self.getChildren() if item.itemType == self.TreeItemType.layer]
    
    def getSubItemChildren(self):
        return [item for item in self.getChildren() if item.itemType == self.TreeItemType.item]
    
    def createButton(self, icon, value):
        btn = QtWidgets.QToolButton()
        btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        btn.setIcon(icon)
        btn.setCheckable(True)
        btn.setAutoRaise(True)
        btn.setChecked(value)
        btn.setStyleSheet("background-color: rgba(0,0,0,0); border: none;") #QToolButton:checked {background-color: rgba(0,0,0,0); border: none;}
        return btn
    
    def setChildrenColumnEnabled(self, column, value):
        nChildren = self.childCount()
        if (nChildren):
            colWidget = self.child(0).columnWidgets[column]
            if (colWidget and colWidget.isEnabled() != value):
                for i in range(nChildren):
                    child = self.child(i)
                    if (child.columnWidgets[column] != None):
                        child.columnWidgets[column].setEnabled(value)
                        if (child.itemType == self.TreeItemType.layer):
                            child.assertChildrenColumnInheritance(column)
    
    #function in charge of correctly enabling/disabling inheritance in the UI
    def assertChildrenColumnInheritance(self, column):
        value = False
        if (self.columnWidgets[column].isEnabled()):
            value = not (self.columnWidgets[column].isChecked() ^ self.__openValues[column])
        self.setChildrenColumnEnabled(column, value)
    
    def assertColumnsInheritance(self, columns=None):
        parent = self.parent()
        visibleWidgets = columns or self.treeWidget().getVisibleColumnsIndexes()
        
        if (isinstance(parent, OLTreeItem)):
            for i in visibleWidgets:
                value = False
                if (parent.columnWidgets[i].isEnabled()):
                    value = not (parent.columnWidgets[i].isChecked() ^ parent.__openValues[i])
                self.columnWidgets[i].setEnabled(value)
        else:
            for i in visibleWidgets:
                self.columnWidgets[i].setEnabled(True)
    
    def loadTreeItemWidgets(self, columns=None, recursive=False, dirtyLoad=False):
        columnsToLoad = columns or self.treeWidget().getVisibleColumnsIndexes()
        if (dirtyLoad):
            self.columnWidgets = [None]*7
        
        wrapperCheckStatuses = self.getChecksStatus() 
        
        for i in (columnsToLoad):
            if (self.columnWidgets[i] == None):
                self.columnWidgets[i] = self.createButton(self.columnIcons[i], wrapperCheckStatuses[i])
                self.columnWidgets[i].toggled.connect(functools.partial(self.btn_toggled, i))
                self.treeWidget().setItemWidget(self, i, self.columnWidgets[i])
        
        self.assertColumnsInheritance(columnsToLoad)
        
        if (recursive):
            for i in range(self.childCount()):
                self.child(i).loadTreeItemWidgets(columns, recursive, dirtyLoad)
    
    def removeTreeItemWidget(self, column, recursive=False):
        self.treeWidget().removeItemWidget(self, column)
        self.columnWidgets[column] = None
        
        if (recursive):
            for i in range(self.childCount()):
                self.child(i).removeTreeItemWidget(column, recursive)
    
    def blockCustomSignals(self, value):
        previousValue = self.__blockCustomSignals
        self.__blockCustomSignals = value
        return previousValue
    
    def processDropEvent(self, newParent):
        self.dataWrapper.parentLayer = newParent
        self.loadTreeItemWidgets(recursive=True, dirtyLoad=True)
    
    def SelectChildrenItems(self, recursive=False):
        self.setSelected(False)
        if (not self.isExpanded()):
                self.setExpanded(True)
                
        for itm in self.getSubItemChildren():
            itm.setSelected(True)
        
        if (recursive):
            for lyr in self.getSubLayerChildren():
                lyr.SelectChildrenItems(recursive=True)
    
    #       -------------------------------------------------------------------------------
    #region -------------------------------- Callbacks ----------------------------------
    #       -------------------------------------------------------------------------------
    def reloadName(self):
        blockedSignals = self.blockCustomSignals(True)
        self.setText(0, self.dataWrapper.dagNode.node)
        self.blockCustomSignals(blockedSignals)
    
    def registerCallbacks(self):
        result = []
        
        ## There is now another callback when a node is renamed (and reloadName doesn't seem to be working...)
        #if (self.dataWrapper):
        #    dagNode = self.dataWrapper.dagNode.node
        #    if (dagNode):
        #        #Rename
        #        jobID = OLMayaBridge.CreateScriptJob(nnc=[dagNode, self.reloadName])
        #        result.append(jobID)
        
        return result
    
    def unregisterCallbacks(self, arrayIDs):
        for id in arrayIDs:
            OLMayaBridge.KillScriptJob(id)
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region --------------------------------- Overriden -----------------------------------
    #       -------------------------------------------------------------------------------
    def __lt__(self, other):
        if (self.itemType == other.itemType):
            return self.text(0).lower() < other.text(0).lower()
        else:
            if (other.itemType == OLTreeItem.TreeItemType.layer):
                return False
            else:
                return True
    
    def setData(self, column, role, value):
        if (not self.__blockCustomSignals):
            if (column == 0 and role == QtCore.Qt.EditRole and value != self.dataWrapper.name):
                #Editing Item Name
                try:
                    self.dataWrapper.name = value
                    super(OLTreeItem, self).setData(column, role, value)
                except Exception as e:
                    ShowMessage(Messages.errorRenamingItem.format(str(e)))
            else:
                super(OLTreeItem, self).setData(column, role, value)
    
    def __del__(self):
        self.unregisterCallbacks(self.__scriptJobIDs)
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ----------------------------------- Events ------------------------------------
    #       -------------------------------------------------------------------------------    
    def btn_toggled(self, column, val):        
        if (column == 1):
            self.dataWrapper.visibility = val
            
        elif (column == 2):
            self.dataWrapper.hideOnPlayback = val
            
        elif (column == 3):
            self.dataWrapper.levelOfDetail = val
            self.dataWrapper.spreadLevelOfDetail = val
            
        elif (column == 4):
            self.dataWrapper.shading = val
            
        elif (column == 5):
            self.dataWrapper.texturing = val
            
        elif (column == 6):
            if val:
                self.dataWrapper.displayType = 2
            else:
                self.dataWrapper.displayType = 0
            self.dataWrapper.spreadDisplayType = val
        
        enable = val
        if (not self.__openValues[column]):
            enable = not val
        
        self.setChildrenColumnEnabled(column, enable)
        
        if (not self.__blockCustomSignals):
            self.treeWidget().columnClicked.emit(self, column)
    #endregion