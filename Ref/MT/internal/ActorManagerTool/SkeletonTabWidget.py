import QtCustomWidgets.UIFileWidget     as UIFileWidget
import Utils.Maya.MayaBridge            as Bridge
import Utils.Maya.NCLBridge             as NCLBridge

from ActorManagerTool.lib.JointWrapper  import JointWrapper
from ActorManagerTool.lib.Utils         import NodeTypes, CustomRoles, Messages, ToolIcons

from PySide2                    import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets          import QMessageBox
from NodeManager.NodeWrapper    import NodeWrapper

class SkeletonTabWidget(UIFileWidget.UIFileWidget):
    invisibleColorStyle = "background-color: rgba(0,0,0,0);"
    greenColorStyle     = "background-color: rgb(0,255,0);"
    orangeColorStyle    = "background-color: rgb(255,170,0);"
    redTransparentBrush = QtGui.QBrush(QtGui.QColor(255,0,0,30))
    orangeTransparentBrush = QtGui.QBrush(QtGui.QColor(255,170,0,30))
    
    jointSidesList = [
        "Center",
        "Left",
        "Right",
        "None"
    ]
    
    jointTypesList = [
        "None",
        "Root",
        "Hip",
        "Knee",
        "Foot",
        "Toe",
        "Spine",
        "Neck",
        "Head",
        "Collar",
        "Shoulder",
        "Elbow",
        "Hand",
        "Finger",
        "Thumb",
        "PropA",
        "PropB",
        "PropC",
        "Other",
        "Index Finger",
        "Middle Finger",
        "Ring Finger",
        "Pinky Finger",
        "Extra Finger",
        "Big Toe",
        "Index Toe",
        "Middle Toe",
        "Ring Toe",
        "Pinky Toe",
        "Foot Thumb"
    ]
    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/SkeletonTabWidget.ui", parent=parent)
        self.__currentViewType = 0 #0 for List, 1 for TreeView
        self.__currentActor     = None
        self.__currentSubActor  = None
        self.__shiftKeyPressed = False
        self.__selectedFullNames = []
        
        self.ui.tree_Skeleton.setVisible(False)
        self.ui.btn_List.setChecked(True)
        self.setMultiHintsInvisible()
        self.ui.cbx_LabelSide.addItems(self.jointSidesList)
        self.ui.cbx_LabelType.addItems(self.jointTypesList)
        
        self.ui.btn_AddRoot.setIcon(ToolIcons.addRootIcon)
        self.ui.btn_ClearRoot.setIcon(ToolIcons.deleteIcon)
        self.ui.btn_SelectRoot.setIcon(ToolIcons.selectIcon)
        self.ui.btn_ReadHierarchy.setIcon(ToolIcons.addHierarchyIcon)
        
        self.ui.btn_List.setIcon(ToolIcons.listIcon)
        self.ui.btn_Hierarchy.setIcon(ToolIcons.hierarchyIcon)
        self.ui.btn_AddToList.setIcon(ToolIcons.addJointsIcon)
        self.ui.btn_DeleteFromList.setIcon(ToolIcons.deleteIcon)
        self.ui.btn_SelectAll.setIcon(ToolIcons.allIcon)
        self.ui.btn_SelectNone.setIcon(ToolIcons.noneIcon)
        
        # ***************************** Events Connections
        # ----------- Skeleton List Buttons -----------
        self.ui.btn_List.toggled.connect(self.toggleView)
        self.ui.btn_Hierarchy.toggled.connect(self.toggleView)
        self.ui.btn_SelectAll.clicked.connect(self.btn_SelectAll_clicked)
        self.ui.btn_SelectNone.clicked.connect(self.btn_SelectNone_clicked)
        self.ui.btn_AddToList.clicked.connect(self.btn_AddToList_clicked)
        self.ui.btn_DeleteFromList.clicked.connect(self.btn_DeleteFromList_clicked)
        # ----------- Skeleton List/Tree -----------
        self.ui.lst_Skeleton.itemSelectionChanged.connect(self.skeletonView_itemSelectionChanged)
        self.ui.lst_Skeleton.itemChanged.connect(self.lst_Skeleton_itemChanged)
        self.ui.tree_Skeleton.itemSelectionChanged.connect(self.skeletonView_itemSelectionChanged)
        self.ui.tree_Skeleton.itemDoubleClicked.connect(self.tree_Skeleton_itemDoubleClicked)
        self.ui.tree_Skeleton.itemExpanded.connect(self.tree_Skeleton_itemExpanded)
        self.ui.tree_Skeleton.itemCollapsed.connect(self.tree_Skeleton_itemCollapsed)
        # ----------- Root -----------
        self.ui.btn_AddRoot.clicked.connect(self.btn_AddRoot_clicked)
        self.ui.btn_ClearRoot.clicked.connect(self.btn_ClearRoot_clicked)
        self.ui.btn_ReadHierarchy.clicked.connect(self.btn_ReadHierarchy_clicked)
        self.ui.btn_SelectRoot.clicked.connect(self.btn_SelectRoot_clicked)
        # ----------- Joint Labelling -----------        
        self.ui.cbx_LabelSide.currentIndexChanged.connect(self.cbx_LabelSide_currentIndexChanged)
        self.ui.cbx_LabelType.currentIndexChanged.connect(self.cbx_LabelType_currentIndexChanged)
        self.ui.led_LabelOther.editingFinished.connect(self.led_LabelOther_editingFinished)
        # ----------- Joint Options -----------
        self.ui.chb_SegScaleComp.stateChanged.connect(self.chb_SegScaleComp_stateChanged)
        # ----------- NCL Options -----------
        self.ui.chb_DontCompress.stateChanged.connect(self.chb_DontCompress_stateChanged)
    
    
    # ********************************************************************************************************************
    # **************************************************** Functions *****************************************************
    # ********************************************************************************************************************
    # -------------------------------------------------
    # -------------- Override Functions ---------------
    # -------------------------------------------------
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Shift):
            self.__shiftKeyPressed = True
    
    def keyReleaseEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Shift):
            self.__shiftKeyPressed = False
    # -------------------------------------------------
    # -------------- UI Status Handling ---------------
    # -------------------------------------------------
    def clearUI(self):
        blockedSignalstree  = self.ui.tree_Skeleton.blockSignals(True)
        blockedSignalslst   = self.ui.lst_Skeleton.blockSignals(True)
        
        self.ui.lst_Skeleton.clear()
        self.ui.tree_Skeleton.clear()
        self.ui.led_Root.setText("")
        
        self.ui.tree_Skeleton.blockSignals(blockedSignalstree)
        self.ui.lst_Skeleton.blockSignals(blockedSignalslst)
        
        self.checkUIState()
    
    def reloadDCRootData(self):
        if (self.__currentSubActor):
            self.ui.led_Root.setText(self.__currentSubActor.getDCRootNode())
        else:
            self.ui.led_Root.setText("")
            
    def reloadSkeletonView(self):
        blockedSignalstree  = self.ui.tree_Skeleton.blockSignals(True)
        blockedSignalslst   = self.ui.lst_Skeleton.blockSignals(True)
        self.ui.tree_Skeleton.setUpdatesEnabled(False)
        self.ui.lst_Skeleton.setUpdatesEnabled(False)
        
        self.ui.lbl_NumTotal.setText("0")
        
        jointSet = self.__currentSubActor.getJointNodes()
        dcRoot = self.__currentSubActor.getDCRootNode()
        totalNodes = len(jointSet) + 1
        if (dcRoot):
            if (not self.__currentViewType):
                # ---------------- List Reload ----------------
                self.ui.lst_Skeleton.clear()
                hier = Bridge.getHierarchy(dcRoot, [NodeTypes.joint, NodeTypes.transform], asTree=False)
                hier.append(dcRoot)
                for fullName in (jointSet + [dcRoot]):
                    path,name = Bridge.extractPathName(fullName)
                    #Show only name but save the full name for working with it in Maya
                    listItem = QtWidgets.QListWidgetItem(ToolIcons.jointIcon if (Bridge.typeOf(fullName) == NodeTypes.joint) else ToolIcons.locatorIcon, name)
                    if (not fullName in hier):
                        listItem.setBackground(self.redTransparentBrush)
                    listItem.setData(CustomRoles.nameRole, name)
                    listItem.setData(CustomRoles.fullNamePathRole, fullName)
                    listItem.setData(CustomRoles.nodeTypeRole, NodeTypes.joint if (Bridge.typeOf(fullName) == NodeTypes.joint) else NodeTypes.transform)
                    listItem.setData(CustomRoles.nodeInSet, True)
                    listItem.setFlags(listItem.flags() | QtCore.Qt.ItemIsEditable)
                    self.ui.lst_Skeleton.addItem(listItem)
                    if (fullName in self.__selectedFullNames):
                        listItem.setSelected(True)
                        self.__selectedFullNames.remove(fullName)
                self.ui.lst_Skeleton.sortItems()
            else:
                # ---------------- Tree Reload ----------------
                expandedItems = self.getTreeExpandedItems()
                self.ui.tree_Skeleton.clear()
                rootItem = self.addTreeRootItem(dcRoot)
                self.ui.tree_Skeleton.expandItem(rootItem) #Root expanded by default
                if (dcRoot in self.__selectedFullNames):
                        rootItem.setSelected(True)
                hier = Bridge.getHierarchy(dcRoot, [NodeTypes.joint, NodeTypes.transform])
                self.loadTreeChildren(rootItem, hier[1], jointSet, expandedItems=expandedItems)
                
                #If there are any joints left, it means they are out of the hierarchy
                if (jointSet):
                    for j in jointSet:
                        self.addTreeRootItem(j, self.redTransparentBrush)
                        
                self.ui.tree_Skeleton.sortItems(0, QtCore.Qt.AscendingOrder)
            
            self.ui.lbl_NumTotal.setText(str(totalNodes))
        else:
            self.ui.lst_Skeleton.clear()
            self.ui.tree_Skeleton.clear()
        
        self.ui.tree_Skeleton.setUpdatesEnabled(True)
        self.ui.lst_Skeleton.setUpdatesEnabled(True)
        self.ui.tree_Skeleton.blockSignals(blockedSignalstree)
        self.ui.lst_Skeleton.blockSignals(blockedSignalslst)
    
    def addTreeRootItem(self, node, bckBrush=None):
        path,name = Bridge.extractPathName(node)
        rootItem = QtWidgets.QTreeWidgetItem(self.ui.tree_Skeleton, [name])
        rootItem.setData(0, CustomRoles.nameRole, name)
        rootItem.setData(0, CustomRoles.fullNamePathRole, node)
        rootItem.setData(0, CustomRoles.nodeTypeRole, NodeTypes.joint if (Bridge.typeOf(node) == NodeTypes.joint) else NodeTypes.transform)
        rootItem.setIcon(0, ToolIcons.jointIcon if (Bridge.typeOf(node) == NodeTypes.joint) else ToolIcons.locatorIcon)
        if (bckBrush):
            rootItem.setBackground(0,bckBrush)
        
        return rootItem
    
    def checkUIState(self):
        self.ui.gbx_JointLabelling.setEnabled(False)
        self.ui.gbx_JointOptions.setEnabled(False)
        self.ui.gbx_NCLOptions.setEnabled(False)
        self.setMultiHintsInvisible()
        
        selNodes = self.getFullPathSelectedNodes()
        numSelected = len(selNodes)
        if (numSelected > 0):
            self.ui.gbx_NCLOptions.setEnabled(True)
            self.loadNCLConfig(selNodes)
            selJoints = self.getFullPathSelectedJoints()
            if (selJoints):
                self.ui.gbx_JointLabelling.setEnabled(True)
                self.ui.gbx_JointOptions.setEnabled(True)
                self.loadJointsConfig(selJoints)
        self.ui.lbl_NumSelected.setText(str(numSelected))
    
    def toggleView(self):
        blockedSignalsHier = self.ui.btn_Hierarchy.blockSignals(True)
        blockedSignalsList = self.ui.btn_List.blockSignals(True)
        
        #self.__togglingView = True
        self.__selectedFullNames = self.getFullPathSelectedNodes()
        if (self.__currentViewType):
            self.ui.btn_Hierarchy.setChecked(False)
            self.ui.btn_List.setChecked(True)
            self.ui.lst_Skeleton.setVisible(True)
            self.ui.tree_Skeleton.setVisible(False)
            self.__currentViewType = 0
        else:
            self.ui.btn_List.setChecked(False)
            self.ui.btn_Hierarchy.setChecked(True)
            self.ui.tree_Skeleton.setVisible(True)
            self.ui.lst_Skeleton.setVisible(False)
            self.__currentViewType = 1
        self.reloadSkeletonView()
        self.checkUIState()
        #self.__togglingView = False
        
        self.ui.btn_Hierarchy.blockSignals(blockedSignalsHier)
        self.ui.btn_List.blockSignals(blockedSignalsList)

    
    def setBckColor(self, uiObj, val):
        if (val == 0):
            uiObj.setStyleSheet(self.orangeColorStyle)
        elif (val == 1):
            uiObj.setStyleSheet(self.greenColorStyle)
        else:
            uiObj.setStyleSheet(self.invisibleColorStyle)
    
    def setMultiHintsInvisible(self):
        self.setBckColor(self.ui.tbt_LabelSide, -1)
        self.setBckColor(self.ui.tbt_LabelType, -1)
        self.setBckColor(self.ui.tbt_LabelOther, -1)
        self.setBckColor(self.ui.tbt_SegScaleComp, -1)
        self.setBckColor(self.ui.tbt_NCLNoCompress, -1)
    # -------------------------------------------------
    # -------------- Data Load Handling ---------------
    # -------------------------------------------------
    def setCurrentActor(self, act):
        pass #This widget does not need an actor (yet)
    
    def loadCurrentActorData(self):
        pass #This widget does not need an actor (yet)
    
    def setCurrentSubActor(self, subAct):
        self.__currentSubActor = subAct
    
    def loadCurrentSubActorData(self):
        self.reloadDCRootData()
        self.reloadSkeletonView()    
    
    def loadNCLConfig (self, nodes):
        if len(nodes) > 0:
            blockedSignalsDontCompress = self.ui.chb_DontCompress.blockSignals(True)
            
            # Only 1 node
            val = NCLBridge.getNoCompress(nodes[0])
            self.ui.chb_DontCompress.setChecked(val)
            
            # Multiple Nodes
            if len(nodes) > 1:
                cDontCompress = self.compareNCLConfig(nodes)
                self.setBckColor(self.ui.tbt_NCLNoCompress, cDontCompress)
            
            self.ui.chb_DontCompress.blockSignals(blockedSignalsDontCompress)
    
    def loadJointsConfig(self, joints):
        if len(joints) > 0:
            blockedSignalsSide  = self.ui.cbx_LabelSide.blockSignals(True)
            blockedSignalsType  = self.ui.cbx_LabelType.blockSignals(True)
            blockedSignalsOther  = self.ui.led_LabelOther.blockSignals(True)
            blockedSignalsScale  = self.ui.chb_SegScaleComp.blockSignals(True)
            
            #self.__loadingData = True
            jntWrap = JointWrapper(joints[0])
            self.ui.cbx_LabelSide.setCurrentIndex(jntWrap.side)
            self.ui.cbx_LabelType.setCurrentIndex(jntWrap.type)
            self.ui.led_LabelOther.setText(jntWrap.other)
            self.ui.chb_SegScaleComp.setChecked(jntWrap.segmentScaleCompensate)
            if len(joints) > 1:
                cSide, cType, cOther, cSegScale = self.compareJointsConfig(joints)
                self.setBckColor(self.ui.tbt_LabelSide, cSide)
                self.setBckColor(self.ui.tbt_LabelType, cType)
                self.setBckColor(self.ui.tbt_LabelOther, cOther)
                self.setBckColor(self.ui.tbt_SegScaleComp, cSegScale)
            #self.__loadingData = False
            
            self.ui.cbx_LabelSide.blockSignals(blockedSignalsSide)
            self.ui.cbx_LabelType.blockSignals(blockedSignalsType)
            self.ui.led_LabelOther.blockSignals(blockedSignalsOther)
            self.ui.chb_SegScaleComp.blockSignals(blockedSignalsScale)
    
    def addNodesToJointSet(self, nodes):
        notInHierarchyNodes = []
        notValidNodes = []
        nodesToAppend = []
        dcRoot = self.__currentSubActor.getDCRootNode()
        hierarchyList = Bridge.getHierarchy(dcRoot, [NodeTypes.joint, NodeTypes.transform], asTree=False)
        
        for n in nodes:
            if (Bridge.typeOf(n) in [NodeTypes.joint, NodeTypes.transform]):
                if (n in hierarchyList):
                    nodesToAppend.append(n)
                else:
                    notInHierarchyNodes.append(n)
            else:
                notValidNodes.append(n)
        
        warnings = [notInHierarchyNodes, notValidNodes]        
        for i in range(len(warnings)):
            warningList = warnings[i]
            if (warningList):
                nodesList = ""
                for n in warningList:
                    nodesList += n + "\n"
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                if (i == 0):
                    msgBox.setWindowTitle("Hierarchy Warning")
                    msgBox.setText(Messages.nodesNotInHierarchy.format(nodesList))
                else:
                    msgBox.setWindowTitle("Node Types Warning")
                    msgBox.setText(Messages.invalidTypeNodes.format(nodesList))
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
        
        self.addSkeletalNodesToSubactor(nodesToAppend)
    # -------------------------------------------------
    # ------------------ Commodities ------------------
    # -------------------------------------------------
    # These are for easy use of both QListWidget and QTreeWidget as a single (but not equal) entity
    def getAllItems(self):
        result = []
        if (not self.__currentViewType):
            for i in range(self.ui.lst_Skeleton.count()):
                result.append(self.ui.lst_Skeleton.item(i))
        else:
            for i in range(self.ui.tree_Skeleton.topLevelItemCount()):
                item = self.ui.tree_Skeleton.topLevelItem(i)
                result.append(item)
                result += self.getAllChildrenTreeItems(item)
        return result
    
    def getSelectedItems(self):
        if (not self.__currentViewType):
            return self.ui.lst_Skeleton.selectedItems()
        else: #Tree
            return self.ui.tree_Skeleton.selectedItems()
    
    def getFullPathSelectedJoints(self):
        if (not self.__currentViewType): #List
            return [item.data(CustomRoles.fullNamePathRole) for item in self.ui.lst_Skeleton.selectedItems() if item.data(CustomRoles.nodeTypeRole) == NodeTypes.joint]
        else:
            return [item.data(0, CustomRoles.fullNamePathRole) for item in self.ui.tree_Skeleton.selectedItems() if item.data(0, CustomRoles.nodeTypeRole) == NodeTypes.joint]
    
    def getFullPathSelectedNodes(self):
        if (not self.__currentViewType): #List
            return [item.data(CustomRoles.fullNamePathRole) for item in self.ui.lst_Skeleton.selectedItems()]
        else: #Tree
            return [item.data(0, CustomRoles.fullNamePathRole) for item in self.ui.tree_Skeleton.selectedItems()]
    
    def setAllItemsSelected(self, value):
        wdg = self.ui.lst_Skeleton
        if (self.__currentViewType):
            wdg = self.ui.tree_Skeleton
        
        #self.__AutoSelecting = True
        blockedSignals = wdg.blockSignals(True)
        wdg.setUpdatesEnabled(False)
        for item in self.getAllItems():
            wdg.setItemSelected(item, value)
        #self.__AutoSelecting = False
        wdg.blockSignals(blockedSignals)
        wdg.setUpdatesEnabled(True)
        self.skeletonView_itemSelectionChanged()
    
    # This is for NCL Plugin Export only
    def compareNCLConfig(self, nodes):
        dontCompress = True
        
        idx = 1
        node0Compress = NCLBridge.getNoCompress(nodes[0])
        while (idx<len(nodes)) and dontCompress:
            jointCurrCompress = NCLBridge.getNoCompress(nodes[idx]) 
            dontCompress = node0Compress == jointCurrCompress
            idx += 1
        
        return dontCompress
    
    def compareJointsConfig(self, joints):
        sideComp = True
        typeComp = True
        otherComp = True
        segScaleComp = True
        
        idx = 1
        joint0 = JointWrapper(joints[0])
        while (idx<len(joints)) and (sideComp or typeComp or otherComp or segScaleComp):
            jointCurr = JointWrapper(joints[idx])
            if sideComp:
                sideComp = joint0.side == jointCurr.side
            if typeComp:
                typeComp = joint0.type == jointCurr.type
            if otherComp:
                otherComp = joint0.other == jointCurr.other
            if segScaleComp:
                segScaleComp = joint0.segmentScaleCompensate == jointCurr.segmentScaleCompensate
            idx += 1
        
        return sideComp, typeComp, otherComp, segScaleComp
    
    def loadTreeChildren(self, treeItem, hier, filterList=None, printNonFiltered=True, expandedItems=[]):
        hasSelected = False
        for child in hier:
            current = child[0]
            isFiltered = False
            if (filterList != None):
                if (child[0] in filterList):
                    isFiltered = True
                    filterList.remove(child[0])
            else:
                isFiltered = True
            
            if (isFiltered or printNonFiltered):
                path,name = Bridge.extractPathName(current)
                childItem = QtWidgets.QTreeWidgetItem(treeItem, [name])
                if (not isFiltered):
                    childItem.setBackground(0,self.orangeTransparentBrush)
                childItem.setData(0, CustomRoles.nameRole, name)
                childItem.setData(0, CustomRoles.fullNamePathRole, current)
                childItem.setData(0, CustomRoles.nodeTypeRole, NodeTypes.joint if (Bridge.typeOf(current) == NodeTypes.joint) else NodeTypes.transform)
                childItem.setData(0, CustomRoles.nodeInSet, isFiltered)
                childItem.setIcon(0, ToolIcons.jointIcon if (Bridge.typeOf(current) == NodeTypes.joint) else ToolIcons.locatorIcon)
                hasSelectedAux = self.loadTreeChildren(childItem, child[1], filterList, expandedItems=expandedItems)
                if(hasSelectedAux or current in expandedItems):
                    if (hasSelectedAux):
                        hasSelected = True
                    self.ui.tree_Skeleton.expandItem(childItem)
                if (current in self.__selectedFullNames):
                        childItem.setSelected(True)
                        self.__selectedFullNames.remove(current)
                        hasSelected = True
        return hasSelected
    
    def getTreeExpandedItems(self, item=None):
        result = []
        if (not item):
            for i in range(self.ui.tree_Skeleton.topLevelItemCount()):
                currChild = self.ui.tree_Skeleton.topLevelItem(i)
                result += self.getTreeExpandedItems(currChild)
        else:
            for i in range(item.childCount()):
                currChild = item.child(i)
                if (currChild.childCount() > 0 and currChild.isExpanded()):
                    result.append(currChild.data(0, CustomRoles.fullNamePathRole))
                result += self.getTreeExpandedItems(currChild)
        return result
    
    def getAllChildrenTreeItems(self, item):
        result = []
        for i in range(item.childCount()):
            result.append(item.child(i))
            result += self.getAllChildrenTreeItems(item.child(i))
        return result
    
    def selectTreeItemChildren(self, item, recursive=True):
        for i in range(item.childCount()):
            child = item.child(i)
            if (child.data(0, CustomRoles.nodeInSet)):
                child.setSelected(True)
            child.setExpanded(True)
            if recursive:
                self.selectTreeItemChildren(child)
    
    def setExpandedRecursive(self, item, value):
        for i in range(item.childCount()):
            child = item.child(i)
            child.setExpanded(value)
            self.setExpandedRecursive(child, value)
    
    def addSkeletalNodesToSubactor(self, nodes):
        # Auto-Set NCL Export property
        for n in nodes:
            NCLBridge.setNoCompress(n, 1)
        self.__currentSubActor.addJoints(nodes)
    
    
    
    
    # ********************************************************************************************************************
    # ****************************************************** EVENTS ******************************************************
    # ********************************************************************************************************************
    # -------------------------------------
    # ----------- Skeleton List -----------
    # -------------------------------------    
    def btn_SelectAll_clicked(self):
        self.setAllItemsSelected(True)
    
    def btn_SelectNone_clicked(self):
        self.setAllItemsSelected(False)
    
    def btn_AddToList_clicked(self):
        nodes = Bridge.getCurrentSelection()
        if (nodes):
            self.addNodesToJointSet(nodes)
            self.reloadSkeletonView()
    
    def btn_DeleteFromList_clicked(self):
        nodes = self.getFullPathSelectedJoints()
        if (nodes):
            self.__currentSubActor.removeJoints(nodes)
            self.reloadSkeletonView()
    
    def skeletonView_itemSelectionChanged(self):
        self.checkUIState()
        Bridge.selectNodes(self.getFullPathSelectedNodes())
    
    def lst_Skeleton_itemChanged(self, item):
        oldName = item.data(CustomRoles.nameRole)
        newName = item.text()
        if (oldName != newName):
            wrap = NodeWrapper(item.data(CustomRoles.fullNamePathRole))
            wrap.renameNode(newName)
            item.setData(CustomRoles.fullNamePathRole, wrap.node)
            item.setData(CustomRoles.nameRole, newName)
    
    def tree_Skeleton_itemDoubleClicked(self, item, column):
        signalsblocked = self.ui.tree_Skeleton.blockSignals(True)
        item.setExpanded(True)
        self.selectTreeItemChildren(item)
        self.ui.tree_Skeleton.blockSignals(signalsblocked)
        self.skeletonView_itemSelectionChanged()
    
    def tree_Skeleton_itemExpanded(self, item):
        if (self.__shiftKeyPressed):
            self.setExpandedRecursive(item, True)
    
    def tree_Skeleton_itemCollapsed(self, item):
        if (self.__shiftKeyPressed):
            self.setExpandedRecursive(item, False)
    
    
    # ----------------------------------
    # ----------- Root Group -----------
    # ----------------------------------
    def btn_AddRoot_clicked(self):
        selection = Bridge.getCurrentSelection()
        if (not selection):
            Bridge.printWarning(Messages.warningNoSelection)
        elif (len(selection) > 1):
            Bridge.printWarning("Varios seleccionados")
        else:
            currentRoot = self.__currentSubActor.getDCRootNode()
            if (currentRoot):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText(Messages.existingRoot)
                msgBox.setWindowTitle("Add Root")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                if (not msgBox.exec_() == QMessageBox.Ok):
                    return
            # Auto-Set NCL Export property
            NCLBridge.setNoCompress(selection[0], 1)
            self.__currentSubActor.addDcRoot(selection[0])
            self.reloadDCRootData()
            self.reloadSkeletonView()
    
    def btn_ClearRoot_clicked(self):
        currentRoot = self.__currentSubActor.getDCRootNode()
        if (currentRoot):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(Messages.clearRoot)
            msgBox.setWindowTitle("Clear Root")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if (not msgBox.exec_() == QMessageBox.Ok):
                return
            
            self.__currentSubActor.clearDcRoot()
            self.__currentSubActor.clearJoints()
            self.loadCurrentSubActorData()
    
    def btn_ReadHierarchy_clicked(self):
        currentRoot = self.__currentSubActor.getDCRootNode()
        if (currentRoot):
            if (self.__currentSubActor.getJointNodes()):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText(Messages.existingJointSet)
                msgBox.setWindowTitle("Append Hierarchy")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                if (not msgBox.exec_() == QMessageBox.Ok):
                    return
                
            hier = Bridge.getHierarchy(currentRoot, [NodeTypes.joint, NodeTypes.transform], asTree=False)
            
            self.addSkeletalNodesToSubactor(hier)
            self.reloadSkeletonView()
        else:
            Bridge.printWarning(Messages.warningNoRoot)
    
    def btn_SelectRoot_clicked(self):
        currentRoot = self.__currentSubActor.getDCRootNode()
        if (currentRoot):
            Bridge.selectNodes([currentRoot])
    # ---------------------------------------
    # ----------- Joint Labelling -----------
    # ---------------------------------------
    def cbx_LabelSide_currentIndexChanged(self, current):
        #print("Joint Label Side Set")
        for jointPath in self.getFullPathSelectedJoints():
            wrap = JointWrapper(jointPath)
            wrap.side = current
        self.checkUIState()
    
    def cbx_LabelType_currentIndexChanged(self, current):
        #print("Joint Label Type Set")
        for jointPath in self.getFullPathSelectedJoints():
            wrap = JointWrapper(jointPath)
            wrap.type = current
        self.checkUIState()
    
    def led_LabelOther_editingFinished(self):
        #print("Joint Label Other Set")
        for jointPath in self.getFullPathSelectedJoints():
            wrap = JointWrapper(jointPath)
            wrap.other = self.ui.led_LabelOther.text()
        self.checkUIState()
    
    # -------------------------------------
    # ----------- Joint Options -----------
    # -------------------------------------
    def chb_SegScaleComp_stateChanged(self, value):
        #print("Joint Segment Scale Compensate Set")
        for jointPath in self.getFullPathSelectedJoints():
            wrap = JointWrapper(jointPath)
            wrap.segmentScaleCompensate = bool(value)
        self.checkUIState()
    
    # -------------------------------------
    # ------------ NCL Options ------------
    # -------------------------------------
    def chb_DontCompress_stateChanged(self, value):
        for nodePath in self.getFullPathSelectedNodes():
            NCLBridge.setNoCompress(nodePath, 1 if value else 0)
        self.checkUIState()