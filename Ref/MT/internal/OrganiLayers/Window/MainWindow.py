import QtCustomWidgets.UIFileWidget as UIFileWidget
import WindowDockBase               as wdBase
import OrganiLayers                 as MWraps
import time

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2                    import QtWidgets, QtCore, QtGui

import OrganiLayers.JSONUtils           as JSONUtils
import OrganiLayers.Window.lib.Utils    as Utils
import Utils.Maya.MayaBridge            as OLMayaBridge

from OrganiLayers               import *
from OrganiLayers.OrganiItem    import OrganiItemWrapper    as oItem
from OrganiLayers.OrganiSet     import OrganiSetWrapper     as oSet

from OrganiLayers.Window.OLIcons    import OLIcons
from OrganiLayers.Window.OLTree     import OLTree
from OrganiLayers.Window.OLTreeItem import OLTreeItem

from OrganiLayers.Window.lib.Classes        import CustomRoles, Messages, OrganiNodeTypes
from OrganiLayers.Window.lib.CustomWidgets  import CheckboxDialogInput, ShowMessage

import maya.api.OpenMaya as OpenMaya


class OrganiLayersWindow(wdBase.UIDockManager):
    __pluginName = "LayerManager"
    __typeIconsDict = {
        OrganiNodeTypes.mesh : OLIcons.meshIcon,
        OrganiNodeTypes.joint : OLIcons.jointIcon,
        OrganiNodeTypes.nurbsCurve : OLIcons.curveShapeIcon,
        OrganiNodeTypes.nurbsSurface : OLIcons.nurbsSurfaceIcon,
        OrganiNodeTypes.camera : OLIcons.cameraIcon,
        OrganiNodeTypes.ambientLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.directionalLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.pointLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.spotLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.areaLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.volumeLight : OLIcons.lightAmbientIcon,
        OrganiNodeTypes.locator : OLIcons.locatorIcon
    }
    
    def __init__(self, parent=None):
        self.__isInitialized = False
        if (self.checkPluginLoaded()):
            self.__isInitialized = True
            super(OrganiLayersWindow, self).__init__("OrganiLayers", r"OrganiLayers/Window/ui/MainWindow.ui")
            self.setWindowTitle('OrganiLayers')
            self.setWindowIcon(OLIcons.layerActiveIcon)
            self.__organiSet = None
            self.__currentActiveLayerItem = None
            self.__filtersButtons = [self.ui.btn_ShowMeshes, self.ui.btn_ShowJoints, self.ui.btn_ShowCurves, self.ui.btn_ShowNurbs, self.ui.btn_ShowCameras, self.ui.btn_ShowLights, self.ui.btn_ShowMisc]
            self.__columnsConfig = {
                "Visible"   : True,
                "Hide on Playback"  : True,
                "Display as Box"    : False,
                "Shaded"    : False,
                "Textured"  : False,
                "Frozen"    : True
            }
            self.__columnsOrder = {
                "Visible"   : 1,
                "Hide on Playback"  : 2,
                "Display as Box"    : 3,
                "Shaded"    : 4,
                "Textured"  : 5,
                "Frozen"    : 6}
        
            self.refreshScheduled = False
            
            # Sidebar Icons
            self.ui.btn_ShowMeshes.setIcon(OLIcons.meshIcon)
            self.ui.btn_ShowJoints.setIcon(OLIcons.jointIcon)
            self.ui.btn_ShowCurves.setIcon(OLIcons.curveShapeIcon)
            self.ui.btn_ShowNurbs.setIcon(OLIcons.nurbsSurfaceIcon)
            self.ui.btn_ShowCameras.setIcon(OLIcons.cameraIcon)
            self.ui.btn_ShowLights.setIcon(OLIcons.lightSpotIcon)
            self.ui.btn_ShowMisc.setIcon(OLIcons.miscellaneousIcon)
            self.setFiltersListStatus([True, True, True, True, True, True, True])
            self.setBarOpenedStatus(False)
            
            # Top Menu buttons
            self.ui.btn_CreateLayer.setIcon(OLIcons.newLayerIcon)
            self.ui.btn_CreateLayerWithSelection.setIcon(OLIcons.newLayerSelectedIcon)
            self.ui.btn_DeleteLayer.setIcon(OLIcons.deleteLayerIcon)
            self.ui.btn_SetLayerActive.setIcon(OLIcons.layerActiveIcon)
            self.ui.btn_AddToActiveLayer.setIcon(OLIcons.addNodesIcon)
            self.ui.btn_RemoveFromSet.setIcon(OLIcons.removeNodesIcon)
            
            # Configure list
            self.ui.lyt_Center.removeWidget(self.ui.tree_Layers)
            self.ui.tree_Layers.deleteLater()
            self.ui.tree_Layers = OLTree(self)
            self.ui.lyt_Center.insertWidget(0, self.ui.tree_Layers)
            
            # ********* Events Connections
            self.ui.cbx_Sets.currentIndexChanged.connect(self.cbx_Sets_currentIndexChanged)
            self.ui.btn_CreateLayer.clicked.connect(self.btn_CreateLayer_clicked)
            self.ui.btn_CreateLayerWithSelection.clicked.connect(self.btn_CreateLayerWithSelection_clicked)
            self.ui.btn_DeleteLayer.clicked.connect(self.btn_DeleteLayer_clicked)
            self.ui.btn_SetLayerActive.clicked.connect(self.btn_SetLayerActive_clicked)
            self.ui.btn_AddToActiveLayer.clicked.connect(self.btn_AddToActiveLayer_clicked)
            self.ui.btn_RemoveFromSet.clicked.connect(self.btn_RemoveFromSet_clicked)
            
            #button disabled as currently it is not implemented any filtering:
            self.ui.btn_ToggleBar.clicked.connect(self.btn_ToggleBar_clicked)
            self.ui.btn_ToggleBar.setHidden(True)
            
            # ********* Actions
            self.ui.actionCleanAll.triggered.connect(self.actCleanAll)
            self.ui.actionCustomizeColumns.triggered.connect(self.actCustomizeColumns)
            self.ui.actionNewSet.triggered.connect(self.actNewSet)
            self.ui.actionDeleteSet.triggered.connect(self.actDeleteSet)
            self.ui.actionRenameSet.triggered.connect(self.actRenameSet)
            self.ui.actionExportSets.triggered.connect(self.actExportSets)
            self.ui.actionImportSets.triggered.connect(self.actImportSets)
            self.ui.tree_Layers.ActMakeLayerActive.triggered.connect(self.ActMakeLayerActive_triggered)
            
            # ********* Error Messages
            self.errorDialog = QtWidgets.QErrorMessage(self)
            
            # ********* Register Callbacks
            self.__scriptJobIDs = self.registerCallbacks()
            
            self.refreshUI()
    
    #       -------------------------------------------------------------------------------
    #region -------------------------------- Data Loading ---------------------------------
    #       -------------------------------------------------------------------------------    
    def reloadSetsCombobox(self):
        blockedSignals = self.ui.cbx_Sets.blockSignals(True)
        self.ui.cbx_Sets.clear()
        organiSets = MWraps.GetOrganiSets()
        idx = 0
        
        for s in organiSets:
            name = s.name
            if s.isReferencedNodes:
                name = "{}:{}".format(s.getNamespace(), s.name)
            self.ui.cbx_Sets.addItem(name, userData=s)
            if (s.isActive):
                self.ui.cbx_Sets.setCurrentIndex(idx)
            idx += 1
        self.ui.cbx_Sets.blockSignals(blockedSignals)
    
    def reloadTree(self, createIfNotExists=True):
        updatesEnabled = self.updatesEnabled()
        self.setUpdatesEnabled(False)
        self.ui.tree_Layers.clear()
        self.loadActiveOrganiSet(createIfNotExists)
        self.LoadSavedColumnsVisibility()
        self.ui.tree_Layers.sortItems(0, QtCore.Qt.AscendingOrder)
        self.setUpdatesEnabled(updatesEnabled)
    
    def refreshUI(self, *args, createIfNotExists=False):     # Callbacks may pass additional parameters that are not needed
        updatesEnabled = self.updatesEnabled()
        self.setUpdatesEnabled(False)
        #start = time.time()
        self.reloadTree(createIfNotExists)
        self.reloadSetsCombobox()
        #end = time.time()
        #print("Load in: {}".format(end - start))
        self.setUpdatesEnabled(updatesEnabled)
        
        self.refreshScheduled = False
        
    def scheduleRefresh(self, mObject, oldName, data):
        if not self.refreshScheduled:
            objName = OpenMaya.MFnDependencyNode(mObject).name()
            if cmds.objExists(objName) and cmds.listConnections("{}.message".format(objName), type=oItem._Type):    # Maya will pass a non existing node from time to time
                self.refreshScheduled = True
                cmds.evalDeferred(self.refreshUI)
    
    def loadActiveOrganiSet(self, createIfNotExists=True):
        self.__organiSet = None
        organiSets = MWraps.GetOrganiSets()
        if (organiSets):
            #Get active OrganiSet
            self.__organiSet = organiSets[0]
            for s in organiSets:
                if s.isActive:
                    self.__organiSet = s
                    break
        elif (createIfNotExists):
            #not Organisets in scene, create one.
            self.__organiSet = oSet()
            self.__organiSet.create("Default")
            self.__organiSet.isActive = True
        
        if (self.__organiSet):
            if (len(self.__organiSet.getComponentLayers()) == 0 and createIfNotExists):
                #Create Default Layer if none exists
                defaultLayer = self.__organiSet.createLayer("Default")
                self.__organiSet.activeLayer = defaultLayer

            for layer in self.__organiSet.getRootLayers():
                self.loadTreeLayer(layer)
    
    def loadTreeLayer(self, layerWrapper, parentTreeItem=None, recursive=True):
        isActive = False
        
        if not parentTreeItem:
            parentTreeItem = self.ui.tree_Layers
        
        if layerWrapper == self.__organiSet.activeLayer:
            isActive = True
        
        item = OLTreeItem(parentTreeItem, layerWrapper.name, layerWrapper, OLIcons.layerActiveIcon if isActive else OLIcons.layerInactiveIcon)
        
        if isActive:
            self.__currentActiveLayerItem = item
        
        if recursive:
            for subLayerWrap in layerWrapper.getChildrenLayers():
                self.loadTreeLayer(subLayerWrap, item, recursive)
        
        self.loadTreeLayerItems(item)
        return item
    
    def loadTreeLayerItems(self, treeLayerItem):
        oLayerWrapper = treeLayerItem.dataWrapper
        #In case the dagNode has been deleted from scene, we clean the OrganiLayerItem too
        oLayerWrapper.cleanInvalidItems()
        
        #start = time.time()
        itemWraps = oLayerWrapper.getChildrenItems()
        #end = time.time()
        #print("itemWraps obtained in: {}".format(end - start))
        
        #start = time.time()
        treeLeaves = self.createTreeLeafs(itemWraps)
        treeLayerItem.addChildren(treeLeaves)
        '''for item in (treeLeaves):
            item.loadTreeItemWidgets()'''
        #end = time.time()
        #print("Items loaded in: {}".format(end - start))
    
    def createTreeLeafs(self, itemWrappers):
        result = []
        for itemWrapper in itemWrappers:
            path, name = OLMayaBridge.extractPathName(itemWrapper.name)
            result.append(OLTreeItem(None, name, itemWrapper, self.getIconByWrapper(itemWrapper), OLTreeItem.TreeItemType.item))
        return result
    
    def getIconByWrapper(self, itemWrapper):
        result = OLIcons.questionIcon
        
        nSuperType = OLMayaBridge.typeOf(itemWrapper.dagNode.node)
        
        if nSuperType == OrganiNodeTypes.joint:
            result = OrganiLayersWindow.__typeIconsDict[nSuperType]
        else:
            shapes = itemWrapper.getDagNodeShapes()
            
            if shapes:
                shapeType = OLMayaBridge.typeOf(shapes[0])
                if shapeType in OrganiNodeTypes.listTypes():
                    result = OrganiLayersWindow.__typeIconsDict[shapeType]
                else:
                    result = OLIcons.miscellaneousIcon
        
        return result
    
    def clearTreeLayerChildItems(self, treeLayerItem):
        for i in reversed(range(treeLayerItem.childCount())):
            currchild = treeLayerItem.child(i)
            if (currchild.itemType == OLTreeItem.TreeItemType.item):
                treeLayerItem.takeChild(i)
    
    def createLayer(self, name, parentLayer=None):
        try:
            return self.__organiSet.createLayer(name, parentLayer)
        except Exception as e:
            self.errorDialog.showMessage(Messages.errorNewLayer.format(str(e)))
            return None
    #endregion
    
    def setFiltersListStatus(self, satusList):
        for i in range(len(self.__filtersButtons)):
            self.__filtersButtons[i].setChecked(satusList[i])
    
    def setBarOpenedStatus(self, value):
        if (self.ui.wdg_SideBar.isHidden() == value) :
            self.btn_ToggleBar_clicked()
    
    def LoadSavedColumnsVisibility(self):
        savedConfig = Utils.ReadConfigUI(OLMayaBridge.GetInternalVar(True))
        if savedConfig:
            self.__columnsConfig = savedConfig
        self.checkColumnsVisibility()
        
    def checkColumnsVisibility(self):
        self.ui.tree_Layers.setColumnHidden(1, not self.__columnsConfig["Visible"])
        self.ui.tree_Layers.setColumnHidden(2, not self.__columnsConfig["Hide on Playback"])
        self.ui.tree_Layers.setColumnHidden(3, not self.__columnsConfig["Display as Box"])
        self.ui.tree_Layers.setColumnHidden(4, not self.__columnsConfig["Shaded"])
        self.ui.tree_Layers.setColumnHidden(5, not self.__columnsConfig["Textured"])
        self.ui.tree_Layers.setColumnHidden(6, not self.__columnsConfig["Frozen"])
    
    #       -------------------------------------------------------------------------------
    #region -------------------------------- Commodities ----------------------------------
    #       -------------------------------------------------------------------------------
    def checkPluginLoaded(self):
        result = OLMayaBridge.isPluginLoaded(self.__pluginName)
        if not result:
            try:
                OLMayaBridge.loadPlugin(self.__pluginName)
                return True
            except:
                OLMayaBridge.printWarning("Could not load Plugin '{}'. The tool won't initialize".format(self.__pluginName))
                return False
        return result
    
    def setActiveLayer(self, item):
        try:
            self.__organiSet.activeLayer = item.dataWrapper
        except Exception as e:
            self.errorDialog.showMessage(Messages.errorSetLayerActive.format(str(e)))
            return
        
        #Make previous layer active as inactive
        if (self.__currentActiveLayerItem):
            self.__currentActiveLayerItem.setData(0, CustomRoles.isActiveRole, False)
            self.__currentActiveLayerItem.setIcon(0, OLIcons.layerInactiveIcon)
        
        #Make new layer as active
        item.setData(0, CustomRoles.isActiveRole, True)
        item.setIcon(0, OLIcons.layerActiveIcon)
        self.__currentActiveLayerItem = item
    
    def deleteLayer(self, layerItem):
        allSubLayersDeleted = True
        subLayers = layerItem.getSubLayerChildren()
        for lyrItem in subLayers:
            layerDeleted = self.deleteLayer(lyrItem)
            if (not layerDeleted):
                allSubLayersDeleted = False
        if (layerItem.dataWrapper.isActive()):
            ShowMessage(Messages.warningDelActiveLayer)
        elif (len(layerItem.getSubItemChildren()) > 0 or not allSubLayersDeleted):
            ShowMessage(Messages.warningDelUsedLayer)
        else:
            layerItem.dataWrapper.delete()
            layerParent = layerItem.parent() or layerItem.treeWidget().invisibleRootItem()
            layerParent.removeChild(layerItem)                
            return True
        return False
    
    def addNodesToLayer(self, nodes, layerItem):
        auxList = list(nodes)
        existingItems = self.ui.tree_Layers.findItemsByDagnode(auxList)
        for existingItem in existingItems:
            existingItem.parent().removeChild(existingItem)
            existingItem.dataWrapper.parentLayer = layerItem.dataWrapper
        
        newItems = []
        for n in auxList:
            try:
                item = CreateOrganiItem(n, layerItem.dataWrapper)
                newItems.append(item)
            except Exception as e:
                self.errorDialog.showMessage(Messages.errorNewItem.format(str(e)))
        newLeaves = self.createTreeLeafs(newItems)
        totalToAdd = existingItems + newLeaves
        layerItem.addChildren(totalToAdd)
        for item in (totalToAdd):
            item.loadTreeItemWidgets(dirtyLoad=True)
    
    def setActiveSet(self, setWrapper):
        if (self.__organiSet):
            self.__organiSet.isActive = False
        self.__organiSet = setWrapper
        if (self.__organiSet):
            self.__organiSet.isActive = True
            
        self.reloadTree()
        
    #endregion
    
    
    #       -------------------------------------------------------------------------------
    #region ---------------------------------- Actions ------------------------------------
    #       -------------------------------------------------------------------------------
    def actCleanAll(self):
        organiSets = MWraps.GetOrganiSets()
        for s in organiSets:
            try:
                s.deleteSet()
            except Exception as e:
                self.errorDialog.showMessage("'{}' Set - {}".format(s.name, Messages.errorDeleteSet.format(str(e))))
        self.refreshUI(False)
    
    def actCustomizeColumns(self):
        keys = list(self.__columnsConfig.keys())
        values = list(self.__columnsConfig.values())
        theDialog = CheckboxDialogInput("Visible Columns", keys, values)
        newValues = None
        if (theDialog.exec_() == theDialog.Accepted):
            newValues = theDialog.getValues()
            for i in range(len(keys)):
                self.__columnsConfig[keys[i]] = newValues[i]
        
        if (newValues and newValues != values):
            Utils.SaveConfigUI(self.__columnsConfig, OLMayaBridge.GetInternalVar(True))
            #self.checkColumnsVisibility()
            for i in (range(len(values))):
                if newValues[i] != values[i]:
                    self.ui.tree_Layers.setColumnWidgetVisibility(self.__columnsOrder[keys[i]], newValues[i])
    
    def actNewSet(self):
        text, ok = QtWidgets.QInputDialog().getText(self, "New Set", "New Set Name:", QtWidgets.QLineEdit.Normal)
        if (ok and text):
            try:
                newSet = CreateSet(text)
                newSet.isActive = True
            except Exception as e:
                self.errorDialog.showMessage(Messages.errorNewItem.format(str(e)))
                return
            
            if (self.__organiSet):
                self.__organiSet.isActive = False
            self.__organiSet = newSet
            self.refreshUI()
    
    def actDeleteSet(self):
        setToDelete = self.__organiSet
        organiSets = MWraps.GetOrganiSets()
        organiSets.remove(setToDelete)
        newSet = organiSets[0] if organiSets else None
        
        self.setActiveSet(newSet)
        
        setToDelete.deleteSet()
        self.reloadSetsCombobox()
    
    def actRenameSet(self):
        text, ok = QtWidgets.QInputDialog().getText(self, "Rename Set", "Current Set Name:", QtWidgets.QLineEdit.Normal)
        if (ok and text):
            try:
                self.__organiSet.name = text
                self.reloadSetsCombobox()
            except Exception as e:
                ShowMessage(Messages.errorRenamingItem.format(str(e)))
    
    def actExportSets(self):
        organiSets = MWraps.GetOrganiSets()
        setNames = [x.name for x in organiSets]
        values = [False for i in range(len(setNames))]
        theDialog = CheckboxDialogInput("Sets to Export", setNames, values)
        if (theDialog.exec_() == theDialog.Accepted):
            values = theDialog.getValues()
            
            if (True in values):            
                dir = OLMayaBridge.GetCurrentFilePath()
                folderName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Export Folder", dir, QtWidgets.QFileDialog.ShowDirsOnly)
                if (folderName != ""):
                    setsToExport = []
                    for i in range(len(organiSets)):
                        if values[i] == True:
                            setsToExport.append(organiSets[i])
                    JSONUtils.ExportJSONSets(setsToExport, folderName)
    
    def actImportSets(self):
        dir = OLMayaBridge.GetCurrentFilePath()
        dialog = QtWidgets.QFileDialog(None, "Select Import File", dir)
        dialog.setOptions(QtWidgets.QFileDialog.DontUseNativeDialog)
        dialog.setNameFilter("Json Files(*.json)")
        if (dialog.exec_()):
            for file in dialog.selectedFiles():
                data = JSONUtils.ReadJSON(file)
                try:
                    newSet = RecreateSetData(data)
                except Exception as e:
                    self.errorDialog.showMessage(Messages.errorCreateSet.format(str(e)))
                    return
                self.setActiveSet(newSet)
            self.reloadSetsCombobox()
            ShowMessage("Done!")
    
    def ActMakeLayerActive_triggered(self):
        self.btn_SetLayerActive_clicked()
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region --------------------------------- Callbacks -----------------------------------
    #       -------------------------------------------------------------------------------
    def registerCallbacks(self):
        result = []
        
        jobID = OpenMaya.MEventMessage.addEventCallback("SceneOpened", self.refreshUI)
        result.append(jobID)
        
        jobID = OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.ui.tree_Layers.reloadSelected)
        result.append(jobID)

        jobID = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterUnloadReference, self.refreshUI)
        result.append(jobID)
        
        jobID = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterLoadReference, self.refreshUI)
        result.append(jobID)
        
        jobID = OpenMaya.MNodeMessage.addNameChangedCallback(OpenMaya.MObject(), self.scheduleRefresh)
        result.append(jobID)
        
        return result
    
    def unregisterCallBacks(self, arrayIDs):
        OpenMaya.MMessage.removeCallbacks(arrayIDs)
    
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------------ Slots ------------------------------------
    #       -------------------------------------------------------------------------------
    def cbx_Sets_currentIndexChanged(self, idx):
        self.setActiveSet(self.ui.cbx_Sets.itemData(idx))
    
    def btn_CreateLayer_clicked(self):
        newLayer = None
        text, ok = QtWidgets.QInputDialog().getText(self, "New Layer", "New Layer Name:", QtWidgets.QLineEdit.Normal)
        if (ok and text):
            # Who is the new layer parent
            parentLayerWrap = None
            parentItem = self.ui.tree_Layers.getLastSelectedLayer()
            
            if parentItem:
                parentLayerWrap = parentItem.dataWrapper
            
            newLayer = self.createLayer(text, parentLayerWrap)
            
            if newLayer:
                newLayerItem = self.loadTreeLayer(newLayer,parentItem)
                self.ui.tree_Layers.expandToItem(newLayerItem)
                self.setActiveLayer(newLayerItem)
        return newLayer
    
    def btn_CreateLayerWithSelection_clicked(self):
        selection = OLMayaBridge.getSelectedDAGNodes()
        
        if (selection):
            if (self.btn_CreateLayer_clicked()):
                self.btn_AddToActiveLayer_clicked()
        else:
            ShowMessage(Messages.warningNoDAGNodesSel)
    
    def btn_DeleteLayer_clicked(self):
        for lyrItem in self.ui.tree_Layers.getSelectedLayers():
            self.deleteLayer(lyrItem)
    
    def btn_SetLayerActive_clicked(self):
        layer = self.ui.tree_Layers.getLastSelectedLayer()
        if (layer):
            self.setActiveLayer(layer)
    
    
    
    def btn_AddToActiveLayer_clicked(self):
        selectedNodes = OLMayaBridge.getSelectedDAGNodes()
        
        if (selectedNodes):
            self.addNodesToLayer(selectedNodes, self.__currentActiveLayerItem)
            self.ui.tree_Layers.expandToItem(self.__currentActiveLayerItem)
        else:
            ShowMessage(Messages.warningNoDAGNodesSel)
    
    def btn_RemoveFromSet_clicked(self):
        selectedItems = self.ui.tree_Layers.selectedItems()
        for itm in selectedItems:
            try:
                itm.dataWrapper.delete()
            except Exception as e:
                self.errorDialog.showMessage(Messages.errorRemovingItem.format(str(e)))
                return
            itm.parent().removeChild(itm)
    
    def btn_ToggleBar_clicked(self):
        if (self.ui.wdg_SideBar.isHidden()):
            self.ui.wdg_SideBar.setHidden(False)
            self.ui.btn_ToggleBar.setArrowType(QtCore.Qt.DownArrow)
        else:
            self.ui.wdg_SideBar.setHidden(True)
            self.ui.btn_ToggleBar.setArrowType(QtCore.Qt.UpArrow)
    #endregion
    
    
    #       -------------------------------------------------------------------------------
    #region ---------------------------------- Overriden ----------------------------------
    #       -------------------------------------------------------------------------------
    def close(self):
        self.unregisterCallBacks(self.__scriptJobIDs)
        super(MayaQWidgetBaseMixin, self).close()
    
    def __del__(self):
        if (self.__isInitialized):
            self.unregisterCallBacks(self.__scriptJobIDs)
            super(OrganiLayersWindow, self).__del__()
    #endregion





if __name__ == '__main__':
    try:
        if organiLayersWindow.isVisible():
            organiLayersWindow.close()
    except NameError:
        pass
    organiLayersWindow = OrganiLayersWindow()
    organiLayersWindow.show()