import QtCustomWidgets.UIFileWidget         as UIFileWidget
import ActorManagerTool.ListGroupWidget     as ListGroupWidget
import ActorManagerTool.SkeletonTabWidget   as SkeletonTabWidget
import ActorManagerTool.GeometryTabWidget   as GeometryTabWidget
import ActorManagerTool.ControlsTabWidget   as ControlsTabWidget
import ActorManagerTool.GeneralTabWidget    as GeneralTabWidget
import Utils.Maya.MayaBridge                as Bridge
import RigManager.Rig                       as Rig
import os, ProjectPath
import ActorManager

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2                    import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets          import QMessageBox
from ActorManagerTool.lib.Utils import Messages, Defaults
from QtCustomWidgets.QtUtils    import BlockSignals

class ActorManagerWindow(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __pluginActorsName      = "ActorManagerPlugin"
    __pluginCollectionsName = "CustomNodesManagement"
    
    greenColor = QtGui.QColor(0,200,50,100)
    yellowColor = QtGui.QColor(255,255,30,100)
    greenTransparentBrush = QtGui.QBrush(greenColor)
    yellowTransparentBrush = QtGui.QBrush(yellowColor)
    transparentBrush = QtGui.QBrush(QtGui.QColor(0,0,0,0))
    
    linearGrad = QtGui.QLinearGradient(0,0,200, 0)
    linearGrad.setSpread(QtGui.QGradient.PadSpread)
    linearGrad.setColorAt(0, greenColor)
    linearGrad.setColorAt(1, yellowColor)
    linearGradBrush = QtGui.QBrush(linearGrad)
    
    def __init__(self, parent=None):
        self.__isInitialized = False
        if (self.checkPluginLoaded()):
            self.__isInitialized = True
            UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/ActorManagerWindow.ui", parent=parent)
            self.setObjectName('ActorManager')
            self.setWindowTitle('Actors Manager')
            self.setWindowIcon(QtGui.QIcon(os.path.join(ProjectPath.getIconsFolder(), r"ActorManagerTool\ActorManager.png")))

            self.__NumActorsSelected = 0

            # ****************** Load SubWidgets ******************
            self.wdg_Actors     = ListGroupWidget.ListGroupWidget("Actor")
            self.wdg_SubActors  = ListGroupWidget.ListGroupWidget("Sub-Actor")
            self.wdg_Controls   = ControlsTabWidget.ControlsTabWidget(self)
            self.wdg_Geometry   = GeometryTabWidget.GeometryTabWidget(self)
            self.wdg_Skeleton   = SkeletonTabWidget.SkeletonTabWidget(self)
            self.wdg_General    = GeneralTabWidget.GeneralTabWidget(self)

            self.ui.wdg_ContainerTop.layout().addWidget(self.wdg_Actors)
            self.ui.wdg_ContainerTop.layout().addWidget(self.wdg_SubActors)
            self.ui.tab_Controls.layout().addWidget(self.wdg_Controls)
            self.ui.tab_Geometry.layout().addWidget(self.wdg_Geometry)
            self.ui.tab_Skeleton.layout().addWidget(self.wdg_Skeleton)
            self.ui.tab_General.layout().addWidget(self.wdg_General)

            # ********* Load Data
            self.refreshActors()
            self.wdg_Actors.SetDeleteEnabled(False)
            self.wdg_Actors.SetSelectEnabled(False)
            self.wdg_Actors.SetDuplicateVisible(False)
            self.wdg_SubActors.SetAddEnabled(False)
            self.wdg_SubActors.SetDeleteEnabled(False)
            self.wdg_SubActors.SetDuplicateEnabled(False)
            self.wdg_SubActors.SetSelectEnabled(False)
            self.wdg_SubActors.SetRefreshVisible(False)
            self.__checkTabsStatus(0, 0)
            self.ui.wdg_footer.setHidden(True)

            # ********* Events Connections
            self.wdg_Actors.addClicked.connect(self.btn_Add_Wdg_Actors_Clicked)
            self.wdg_Actors.deleteClicked.connect(self.btn_Delete_Wdg_Actors_Clicked)
            self.wdg_Actors.selectClicked.connect(self.btn_Select_Wdg_Actors_Clicked)
            self.wdg_Actors.refreshClicked.connect(self.btn_Refresh_Wdg_Actors_Clicked)
            self.wdg_SubActors.addClicked.connect(self.btn_Add_Wdg_SubActors_Clicked)
            self.wdg_SubActors.deleteClicked.connect(self.btn_Delete_Wdg_SubActors_Clicked)
            self.wdg_SubActors.duplicateClicked.connect(self.btn_Duplicate_Wdg_SubActors_Clicked)
            self.wdg_SubActors.selectClicked.connect(self.btn_Select_Wdg_SubActors_Clicked)
            self.wdg_Actors.itemSelectionChanged.connect(self.wdg_Actors_SelectionChanged)
            self.wdg_Actors.lstDataItemDoubleClicked.connect(self.wdg_Actors_ItemDoubleClicked)
            self.wdg_SubActors.itemSelectionChanged.connect(self.wdg_SubActors_SelectionChanged)
            self.wdg_SubActors.lstDataItemDoubleClicked.connect(self.wdg_SubActors_ItemDoubleClicked)
            self.ui.twg_Info.currentChanged.connect(self.twg_Info_CurrentChanged)
            # ********* Error Messages
            self.newActorErrDialog = QtWidgets.QErrorMessage(self)
    
    
    def refreshActors(self):
        self.wdg_Actors.LoadData(ActorManager.getActors())
        
    def refreshSubActors(self):
        selectedActors = self.wdg_Actors.selectedItemsData()
        self.loadSubActors(selectedActors)
    
    def loadSubActors(self, actorsList):
        self.wdg_SubActors.ClearData()
        for actor in actorsList:
            self.wdg_SubActors.AppendData(actor.getSubActors())
        
        # Look for the main subactor and anim subactor to give it another color
        self.reloadSubActorsBackgrounds()
    
    def cleanSubActorBackgrounds(self):
        numSubActors = self.wdg_SubActors.ui.lst_Data.count()
        for idx in range(numSubActors):
            item = self.wdg_SubActors.ui.lst_Data.item(idx)
            item.setBackground(self.transparentBrush)
    
    def reloadSubActorsBackgrounds(self):
        self.cleanSubActorBackgrounds()
        numSubActors = self.wdg_SubActors.ui.lst_Data.count()
        for idx in range(numSubActors):
            item = self.wdg_SubActors.ui.lst_Data.item(idx)
            itemWidget = self.wdg_SubActors.ui.lst_Data.itemWidget(item)
            if (itemWidget.itemData.isMainSubActor()):
                item.setBackground(self.greenTransparentBrush)
                if (itemWidget.itemData.isAnimSubActor()):
                    item.setBackground(self.linearGradBrush)
            elif (itemWidget.itemData.isAnimSubActor()):
                item.setBackground(self.yellowTransparentBrush)
    
    def createActor(self):
        text, ok = QtWidgets.QInputDialog().getText(self, "New Actor", "New Actor Name:", QtWidgets.QLineEdit.Normal)
        text = text.rstrip().lstrip()
        if (ok and text):
            try:
                ActorManager.createActor(text)
            except Exception as e:
                self.newActorErrDialog.showMessage(Messages.errorNewActor.format(str(e)))
            
            self.wdg_Actors.LoadData(ActorManager.getActors())
            self.wdg_Actors.selectByName(text)
    
    def createSubActor(self, actor):
        text, ok = QtWidgets.QInputDialog().getText(self, "New SubActor", "New SubActor Name:", QtWidgets.QLineEdit.Normal)
        text = text.rstrip().lstrip()
        if (ok and text):
            try:
                newSubActor = actor.createSubActor(text)
                newSubActor.exportPath = Defaults.exportPath
                newSubActor.subActorPathToken = Defaults.subActorPath
                newSubActor.modelPath = Defaults.modelPath
                newSubActor.animPath = Defaults.animsPath
                newSubActor.modelName = Defaults.modelName
                # Default Main Subactor if it's first created
                if (not actor.mainSubActor):
                    actor.mainSubActor = newSubActor
                # Default Anim Subactor if it's first created
                if (not actor.animSubActor):
                    actor.animSubActor = newSubActor
            except Exception as e:
                self.newActorErrDialog.showMessage(Messages.errorNewSubActor.format(str(e)))
                
            self.refreshSubActors()
            self.wdg_SubActors.selectByName(text)
    
    def DuplicateSubActor(self, subActor):
        parentActor = subActor.getActor()
        
        newSubActor = parentActor.createSubActor("{}_Copy".format(subActor.name))
        newSubActor.exportPath = subActor.exportPath
        newSubActor.subActorPathToken = subActor.subActorPathToken
        newSubActor.modelPath = subActor.modelPath
        newSubActor.animPath = subActor.animPath
        newSubActor.modelName = subActor.modelName
        newSubActor.isModelExportable = subActor.isModelExportable
        newSubActor.addGeometries(subActor.getGeometryNodes())
        newSubActor.addJoints(subActor.getJointNodes())
        newSubActor.addDcRoot(subActor.getDCRootNode())
    
    def renameItem(self, nameWdgt):
        text, ok = QtWidgets.QInputDialog().getText(self, "Rename", "New Name:", QtWidgets.QLineEdit.Normal, text=nameWdgt.itemData.name)
        if (ok and text):
            try:
                nameWdgt.itemData.name = text
                nameWdgt.setName(text)
            except Exception as e:
                self.newActorErrDialog.showMessage(Messages.errorRename.format(str(e)))
    
    def showMessageBox(self, title, text):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
    
    def checkUIStatus(self, numActorsSelected, numSubActorsSelected):
        actorsStatus = 1
        subActorsStatus = 0
        if (numActorsSelected > 0):
            actorsStatus = 2
            if (numActorsSelected == 1):
                subActorsStatus = 1
        
        if (numSubActorsSelected > 0):
            if (subActorsStatus == 1):
                subActorsStatus = 2
            else:
                subActorsStatus = 3
        
        self.wdg_Actors.SetUIStatus(actorsStatus)
        self.wdg_SubActors.SetUIStatus(subActorsStatus)
        
        self.__checkTabsStatus(numActorsSelected, numSubActorsSelected)
    
    def __checkTabsStatus(self, numActorsSelected, numSubActorsSelected):
        self.ui.tab_Skeleton.setEnabled(False)
        self.ui.tab_Controls.setEnabled(False)
        self.ui.tab_Geometry.setEnabled(False)
        self.ui.tab_General.setEnabled(False)
        if (numActorsSelected > 0):
            self.ui.tab_Controls.setEnabled(True)
            self.ui.tab_General.setEnabled(True)
        if (numSubActorsSelected > 0):
            self.ui.tab_Geometry.setEnabled(True)
            self.ui.tab_Skeleton.setEnabled(True)
    
    def loadTabWidgetData(self, idx, subActor=None, actor=None): #idx of the tab panel opened
        self.ui.wdg_footer.setHidden(True)
        if (actor or subActor):
            wdg = None
            
            if (idx == 0):
                wdg = self.wdg_Controls
                self.ui.wdg_footer.setHidden(False)
            elif (idx == 1):
                wdg = self.wdg_Geometry 
            elif (idx == 2):
                wdg = self.wdg_Skeleton
            elif (idx == 3):
                wdg = self.wdg_General
                pass
            
            if (wdg):
                wdg.setCurrentActor(actor)
                wdg.setCurrentSubActor(subActor)
                if (actor):
                    wdg.loadCurrentActorData()
                if (subActor):
                    wdg.loadCurrentSubActorData()
    
    def cleanTabWidgetData(self):
        self.wdg_Geometry.clearUI()
        self.wdg_Skeleton.clearUI()
        self.wdg_General.clearUI()
        #ToDo: Implement when those widgets are programmed
        #self.wdg_Controls.clearUI()
    
    # ******************************************************
    # ******************** Commodities *********************
    # ******************************************************
    def checkPluginLoaded(self):
        resultActorsPlugin = Bridge.isPluginLoaded(self.__pluginActorsName)
        if not resultActorsPlugin:
            try:
                Bridge.loadPlugin(self.__pluginActorsName)
                print("Plugin loaded: {}".format(self.__pluginActorsName))
                resultActorsPlugin = True
            except:
                Bridge.printWarning("Could not load Plugin '{}'. The tool won't initialize".format(self.__pluginName))
                return False
        
        resultCollectionsPlugin = Bridge.isPluginLoaded(self.__pluginCollectionsName)
        if not resultCollectionsPlugin:
            try:
                Bridge.loadPlugin(self.__pluginCollectionsName)
                print("Plugin loaded: {}".format(self.__pluginCollectionsName))
                resultCollectionsPlugin = True
            except:
                Bridge.printWarning("Could not load Plugin '{}'. The tool won't initialize".format(self.__pluginName))
                return False
        
        return resultActorsPlugin and resultCollectionsPlugin
    # ******************************************************
    # *********************** EVENTS ***********************
    # ******************************************************
    
    #----------------- Actors -----------------
    def btn_Add_Wdg_Actors_Clicked(self):
        self.createActor()
    
    def btn_Delete_Wdg_Actors_Clicked(self):
        selectedActors = self.wdg_Actors.selectedItemsData()
        #Clear data before deleting because QListWidget.clear() launches selectionchanged signal and it is inconsistent while deleting QListWidgetItems.
        self.wdg_Actors.ClearData()
        for actor in selectedActors:
            actor.delete()
        self.refreshActors()
    
    def btn_Refresh_Wdg_Actors_Clicked(self):
        self.refreshActors()
    
    def btn_Select_Wdg_Actors_Clicked(self):
        nodesToSelect = [x.node for x in (self.wdg_Actors.selectedItemsData())]
        Bridge.selectNodes(nodesToSelect)
    
    def wdg_Actors_SelectionChanged(self):
        selectedActors = self.wdg_Actors.selectedItemsData()
        self.loadSubActors(selectedActors)
        
        self.__NumActorsSelected = len(selectedActors)
        self.checkUIStatus(self.__NumActorsSelected, 0)
        self.cleanTabWidgetData()
        if (self.__NumActorsSelected == 1):
            self.loadTabWidgetData(self.ui.twg_Info.currentIndex(), None, selectedActors[0])
        # TODO: We can discern here if there is multiple selection
    
    def wdg_Actors_ItemDoubleClicked(self, item):
        wdgtName = self.wdg_Actors.getItemWidget(item)
        self.renameItem(wdgtName)
    
    #----------------- SubActors -----------------
    def btn_Add_Wdg_SubActors_Clicked(self):
        selectedActors = self.wdg_Actors.selectedItemsData()
        if (len(selectedActors) == 1):
            self.createSubActor(selectedActors[0])
        else:
            self.showMessageBox("Invalid Action", Messages.infoSubActorInMultipleActors)
    
    def btn_Delete_Wdg_SubActors_Clicked(self):
        selectedSubActors =  self.wdg_SubActors.selectedItemsData()
        for subActor in selectedSubActors:
            subActor.delete()
        self.refreshSubActors()
    
    def btn_Duplicate_Wdg_SubActors_Clicked(self):
        selectedSubActors = self.wdg_SubActors.selectedItemsData()
        for subAct in selectedSubActors:
            try:
                self.DuplicateSubActor(subAct)
            except Exception as e:
                self.newActorErrDialog.showMessage(Messages.errorNewActor.format(str(e)))
        self.refreshSubActors()
    
    def btn_Select_Wdg_SubActors_Clicked(self):
        nodesToSelect = [x.node for x in (self.wdg_SubActors.selectedItemsData())]
        Bridge.selectNodes(nodesToSelect)
    
    def wdg_SubActors_SelectionChanged(self):
        selectedActors = self.wdg_Actors.selectedItemsData()
        selectedSubActors = self.wdg_SubActors.selectedItemsData()
        self.checkUIStatus(self.__NumActorsSelected, len(selectedSubActors))
        self.cleanTabWidgetData()
        subActorToLoad = None
        actorToLoad = None
        if (len(selectedSubActors) == 1):
            subActorToLoad = selectedSubActors[0]
        if (len(selectedActors) == 1):
            actorToLoad = selectedActors[0]
        self.loadTabWidgetData(self.ui.twg_Info.currentIndex(), subActorToLoad, actorToLoad)
        # TODO: We can discern here if there is multiple selection
    
    def wdg_SubActors_ItemDoubleClicked(self, item):
        wdgtName = self.wdg_SubActors.getItemWidget(item)
        self.renameItem(wdgtName)
    
    #----------------- Tab Widget -----------------
    def twg_Info_CurrentChanged(self, idx):
        selectedActors      =  self.wdg_Actors.selectedItemsData()
        actor       = None
        subActor    = None
        if (len(selectedActors) == 1):
            actor = selectedActors[0]
        
        selectedSubActors   =  self.wdg_SubActors.selectedItemsData()
        if (len(selectedSubActors) == 1):
            subActor = selectedSubActors[0]
        
        self.loadTabWidgetData(idx, subActor, actor)



if __name__ == '__main__':
    try:
        if actorManagerWindow.isVisible():
            actorManagerWindow.close()
    except NameError:
        pass
    actorManagerWindow = ActorManagerWindow()
    actorManagerWindow.show()