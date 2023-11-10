import QtCustomWidgets.UIFileWidget     as UIFileWidget
import Utils.Maya.MayaBridge            as Bridge


from ActorManagerTool.lib.Utils        import Messages, ToolIcons
from PySide2.QtWidgets                 import QMessageBox



class ControlsTabWidget(UIFileWidget.UIFileWidget):    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/ControlsTabWidget.ui", parent=parent)
        self.__currentActor     = None
        self.__currentSubActor  = None
        
        self.ui.btn_SelectAll.setIcon(ToolIcons.allIcon)
        self.ui.btn_SelectNone.setIcon(ToolIcons.noneIcon)
        self.ui.btn_AddToList.setIcon(ToolIcons.addIcon)
        self.ui.btn_DeleteFromList.setIcon(ToolIcons.deleteIcon)
        
        self.ui.btn_AddRoot.setIcon(ToolIcons.addRootIcon)
        self.ui.btn_ClearRoot.setIcon(ToolIcons.deleteIcon)
        self.ui.btn_SelectRoot.setIcon(ToolIcons.selectIcon)
        self.ui.btn_ReadHierarchy.setIcon(ToolIcons.addHierarchyIcon)
        
        # ***************************** Events Connections
        # ----------- Root -----------
        self.ui.btn_AddRoot.clicked.connect(self.btn_AddRoot_clicked)
        self.ui.btn_ClearRoot.clicked.connect(self.btn_ClearRoot_clicked)
        #self.ui.btn_ReadHierarchy.clicked.connect(self.btn_ReadHierarchy_clicked)
        self.ui.btn_SelectRoot.clicked.connect(self.btn_SelectRoot_clicked)
        # Copied from Geometry Widget:
        '''self.ui.lst_Geometry.itemSelectionChanged.connect(self.lst_Geometry_itemSelectionChanged)
        self.ui.btn_SelectAll.clicked.connect(self.btn_SelectAll_clicked)
        self.ui.btn_SelectNone.clicked.connect(self.btn_SelectNone_clicked)
        self.ui.btn_AddToList.clicked.connect(self.btn_AddToList_clicked)
        self.ui.btn_DeleteFromList.clicked.connect(self.btn_DeleteFromList_clicked)'''
    # ********************************************************************************************************************
    # **************************************************** Functions *****************************************************
    # ********************************************************************************************************************
    # -------------------------------------------------
    # -------------- UI Status Handling ---------------
    # -------------------------------------------------
    def clearUI(self):
        blockedSignals  = self.ui.lst_Geometry.blockSignals(True)
        
        self.ui.lst_Geometry.clear()
        
        self.ui.lst_Geometry.blockSignals(blockedSignals)
        
        self.checkUIState()
    
    def checkUIState(self):
        selection = self.ui.lst_Geometry.selectedItems()
        self.ui.lbl_NumSelected.setText(str(len(selection)))
    
    def reloadMainCtlData(self):
        if (self.__currentActor and self.__currentActor.rig):
            self.ui.led_Root.setText(self.__currentActor.rig.mainControl)
        else:
            self.ui.led_Root.setText("")
    # -------------------------------------------------
    # -------------- Data Load Handling ---------------
    # ------------------------------------------------- 
    def setCurrentActor(self, act):
        self.__currentActor = act
    
    def loadCurrentActorData(self):
        self.reloadMainCtlData()
        
    def setCurrentSubActor(self, subAct):
        self.__currentSubActor = subAct    
    
    def loadCurrentSubActorData(self):
        #self.reloadGeometryList() # Not SubActor needed (yet)
        pass
    
    
    
    # Copied from Geometry Widget
    '''def reloadGeometryList(self):
        blockedSignals  = self.ui.lst_Geometry.blockSignals(True)
        
        self.ui.lst_Geometry.clear()
        
        geometrySet = self.__currentSubActor.getGeometryNodes()
        for m in geometrySet:
            path,name = Bridge.extractPathName(m)
            item = QtWidgets.QListWidgetItem(ToolIcons.meshIcon, name)
            item.setData(CustomRoles.fullNamePathRole, m)
            self.ui.lst_Geometry.addItem(item)
        
        self.ui.lbl_NumTotal.setText(str(len(geometrySet)))
        
        self.ui.lst_Geometry.blockSignals(blockedSignals)
        
        def addNodesToGeometrySet(self, nodes):
        print(nodes)
        nodesToAppend = []
        notValidNodes = []
        
        for n in nodes:
            if (Bridge.typeOf(n) == NodeTypes.mesh):
                    nodesToAppend.append(n)
            else:
                notValidNodes.append(n)
        
        if (notValidNodes):
            nodesList = ""
            for n in notValidNodes:
                nodesList += n + "\n"
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Node Types Warning")
            msgBox.setText(Messages.invalidTypeNodes.format(nodesList))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        
        self.__currentSubActor.addGeometries(nodesToAppend)
    
    def getFullPathSelectedNodes(self):
        return [item.data(CustomRoles.fullNamePathRole) for item in self.ui.lst_Geometry.selectedItems()]'''

    
    # ********************************************************************************************************************
    # ****************************************************** EVENTS ******************************************************
    # ********************************************************************************************************************
    # ----------------------------------
    # ----------- Root Group -----------
    # ----------------------------------
    def btn_AddRoot_clicked(self):
        selection = Bridge.getCurrentSelection()
        if (not selection):
            Bridge.printWarning(Messages.warningNoSelection)
        else:
            currentRoot = self.__currentActor.rig.mainControl
            if (currentRoot):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Question)
                msgBox.setText(Messages.existingRoot)
                msgBox.setWindowTitle("Add Main Control")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                if (not msgBox.exec_() == QMessageBox.Ok):
                    return
            self.__currentActor.rig.mainControl = selection[0]
            self.reloadMainCtlData()
    
    def btn_ClearRoot_clicked(self):
        currentRoot = self.__currentActor.rig.mainControl
        if (currentRoot):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(Messages.clearRoot)
            msgBox.setWindowTitle("Clear Main Control")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if (not msgBox.exec_() == QMessageBox.Ok):
                return
            
            self.__currentActor.rig.mainControl = None
            self.loadCurrentActorData()
    
    '''def btn_ReadHierarchy_clicked(self):
        currentRoot = self.__currentSubActor.rig.mainControl
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
            self.__currentSubActor.addJoints(hier)
            self.reloadSkeletonView()
        else:
            Bridge.printWarning(Messages.warningNoRoot)'''
    
    def btn_SelectRoot_clicked(self):
        currentRoot = self.__currentActor.rig.mainControl
        if (currentRoot):
            Bridge.selectNodes([currentRoot])
    # Copied from Geometry Widget
    '''def lst_Geometry_itemSelectionChanged(self):
        self.checkUIState()
        Bridge.selectNodes(self.getFullPathSelectedNodes())
        
    def btn_SelectAll_clicked(self):
        blockedSignals = self.ui.lst_Geometry.blockSignals(True)
        for i in range(self.ui.lst_Geometry.count()):
            self.ui.lst_Geometry.item(i).setSelected(True)
        self.ui.lst_Geometry.blockSignals(blockedSignals)
        self.lst_Geometry_itemSelectionChanged()
    
    def btn_SelectNone_clicked(self):
        blockedSignals = self.ui.lst_Geometry.blockSignals(True)
        for i in range(self.ui.lst_Geometry.count()):
            self.ui.lst_Geometry.item(i).setSelected(False)
        self.ui.lst_Geometry.blockSignals(blockedSignals)
        self.lst_Geometry_itemSelectionChanged()
    
    def btn_AddToList_clicked(self):
        meshesInScene = Bridge.getSceneNodesByType(NodeTypes.mesh)
        if meshesInScene:
            theListItems = []
            currentSet = self.__currentSubActor.getGeometryNodes()
            for m in meshesInScene:
                if (m not in currentSet):
                    path,name = Bridge.extractPathName(m)
                    item = QtWidgets.QListWidgetItem(name)
                    item.setData(CustomRoles.fullNamePathRole, m)
                    theListItems.append(item)
            
            if (theListItems):
                theListWdg = MultiItemDialogInput("Meshes", theListItems)
                if (theListWdg.exec_() == theListWdg.Accepted):
                    nodes = [item.data(CustomRoles.fullNamePathRole) for item in theListWdg.listWidget.selectedItems()]
                    if (nodes):
                        self.addNodesToGeometrySet(nodes)
                        self.reloadGeometryList()
            else:
                Bridge.printWarning(Messages.warningAllMeshesInSet)
        else:
            Bridge.printWarning(Messages.warningNoMeshesInScene)
    
    def btn_DeleteFromList_clicked(self):
        nodes = self.getFullPathSelectedNodes()
        if (nodes):
            self.__currentSubActor.removeGeometries(nodes)
            self.reloadGeometryList()
        else:
            Bridge.printWarning(Messages.warningNoSelection)'''