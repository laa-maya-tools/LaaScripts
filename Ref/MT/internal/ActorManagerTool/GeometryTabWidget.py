import QtCustomWidgets.UIFileWidget     as UIFileWidget
import Utils.Maya.MayaBridge            as Bridge

from ActorManagerTool.lib.Utils        import NodeTypes, CustomRoles, Messages, ToolIcons, MultiItemDialogInput

from PySide2                           import QtWidgets
from PySide2.QtWidgets                 import QMessageBox




class GeometryTabWidget(UIFileWidget.UIFileWidget):    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/GeometryTabWidget.ui", parent=parent)
        self.__currentActor     = None
        self.__currentSubActor  = None
        
        self.ui.btn_SelectAll.setIcon(ToolIcons.allIcon)
        self.ui.btn_SelectNone.setIcon(ToolIcons.noneIcon)
        self.ui.btn_ShowList.setIcon(ToolIcons.meshList)
        self.ui.btn_AddToList.setIcon(ToolIcons.addMultiIcon)
        self.ui.btn_DeleteFromList.setIcon(ToolIcons.deleteIcon)
        
        # ***************************** Events Connections
        self.ui.lst_Geometry.itemSelectionChanged.connect(self.lst_Geometry_itemSelectionChanged)
        self.ui.btn_SelectAll.clicked.connect(self.btn_SelectAll_clicked)
        self.ui.btn_SelectNone.clicked.connect(self.btn_SelectNone_clicked)
        self.ui.btn_ShowList.clicked.connect(self.btn_ShowList_clicked)
        self.ui.btn_AddToList.clicked.connect(self.btn_AddToList_clicked)
        self.ui.btn_DeleteFromList.clicked.connect(self.btn_DeleteFromList_clicked)
    
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
        
    def reloadGeometryList(self):
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
    
    def checkUIState(self):
        selection = self.ui.lst_Geometry.selectedItems()
        self.ui.lbl_NumSelected.setText(str(len(selection)))
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
        self.reloadGeometryList()
    
    def addNodesToGeometrySet(self, nodes):
        print(nodes)
        nodesToAppend = []
        notValidNodes = []
        
        for n in nodes:
            if (len(Bridge.getHierarchy(n, [NodeTypes.mesh], asTree=False, recursive=False)) > 0):
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
    # -------------------------------------------------
    # ------------------ Commodities ------------------
    # -------------------------------------------------
    def getFullPathSelectedNodes(self):
        return [item.data(CustomRoles.fullNamePathRole) for item in self.ui.lst_Geometry.selectedItems()]

    
    # ********************************************************************************************************************
    # ****************************************************** EVENTS ******************************************************
    # ********************************************************************************************************************
    #----------------- Geometry List -----------------
    def lst_Geometry_itemSelectionChanged(self):
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
    
    def btn_ShowList_clicked(self):
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
                theListWdg = MultiItemDialogInput("Available Meshes", theListItems)
                if (theListWdg.exec_() == theListWdg.Accepted):
                    nodes = [item.data(CustomRoles.fullNamePathRole) for item in theListWdg.listWidget.selectedItems()]
                    if (nodes):
                        self.addNodesToGeometrySet(nodes)
                        self.reloadGeometryList()
            else:
                Bridge.printWarning(Messages.warningAllMeshesInSet)
        else:
            Bridge.printWarning(Messages.warningNoMeshesInScene)
    
    def btn_AddToList_clicked(self):
        sel = Bridge.getCurrentSelection()
        if (len(sel) > 0):
            meshNodes = Bridge.getSceneNodesByType(NodeTypes.mesh)
            result = []

            for n in sel:
                if n in meshNodes:
                    result.append(n)

            if result:
                self.addNodesToGeometrySet(result)
                self.reloadGeometryList()
            else:
                Bridge.printWarning(Messages.warningNoValidNodesSelected)
        else:
            Bridge.printWarning(Messages.warningNoSelection)
    
    def btn_DeleteFromList_clicked(self):
        nodes = self.getFullPathSelectedNodes()
        if (nodes):
            self.__currentSubActor.removeGeometries(nodes)
            self.reloadGeometryList()
        else:
            Bridge.printWarning(Messages.warningNoSelection)