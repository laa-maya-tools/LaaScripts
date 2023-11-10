import os
import PySide2.QtGui as QtGui

import QtCustomWidgets.UIFileWidget     as UIFileWidget
import ExporterActor.ActorExportWidget  as ActorExportWidget
import ExporterActor.lib.utils          as utils
import ProjectPath
import Utils.Maya.MayaBridge            as Bridge
import Utils.Maya.MayaFBX               as MayaFBX

from ProjectPath                import PathTokenizer, Tokens
import ActorManager

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2                    import QtWidgets, QtCore
from PySide2.QtWidgets          import QLabel, QMenu, QMessageBox
from PySide2.QtCore             import Signal
from ActorManagerTool.lib.Utils import Defaults

class ClickableLabel(QLabel):
    clicked = Signal()
    
    def __init__(self, *args):
        QLabel.__init__(self, *args)
        
    def mouseReleaseEvent(self, ev):
        self.clicked.emit()

class ActorExporterWindow(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    maxOverridePaths = 10
    maxVisibleOverridePaths = 5
    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ExporterActor/ui/ActorExporterWindow.ui", parent=parent)
        self.setObjectName('ActorExporter')
        self.setWindowTitle('Actor Exporter')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ProjectPath.getIconsFolder(), r"ExporterActor\ExporterActor.png")))
        self.__tempExportActorName = "Temp_3D_Export"
        self.__tempExportActor = None
        
        # ********* Callbacks
        self.undoScriptJob = None
        self.redoScriptJob = None
        
        # ********* Override Paths
        self.ui.cbx_ExportDir.setMaxCount(ActorExporterWindow.maxOverridePaths)
        self.ui.cbx_ExportDir.setMaxVisibleItems(ActorExporterWindow.maxVisibleOverridePaths)
        self.ui.cbx_ExportDir.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        ovPaths = utils.ReadLastUsedPaths()
        if (len(ovPaths) > 0):
            self.ui.cbx_ExportDir.addItems(ovPaths)
            self.ui.ckb_OverridePaths.setEnabled(True)
        
        # ********* Branches
        branches = ProjectPath.GetBranches(ProjectPath.getProjectFolder(), recursive=True, fullPath=False)
        #Force the 'GAME' branch
        gameBranch = "GAME"
        self.ui.cbx_Branch.addItem(gameBranch)
        if (len(branches) > 0):
            try:
                branches.remove(gameBranch)
            except:
                pass
            self.ui.cbx_Branch.addItems(branches)
        
        # ********* Help Label 
        lyt = self.ui.lyt_header.layout()
        newlbl_Help = ClickableLabel()
        newlbl_Help.setPixmap(QtGui.QPixmap(os.path.join(ProjectPath.getToolsFolder(), r"ExporterActor/images/help.png")))
        #lyt.removeWidget(self.ui.lbl_Help)
        self.ui.lbl_Help = newlbl_Help
        lyt.insertWidget(6, self.ui.lbl_Help)
        
        # ********* Progress Bar
        self.ui.pgb_ExportProgress.setHidden(True)
        
        # ********* Refresh Button 
        self.ui.btn_Refresh.setIcon(QtGui.QIcon(os.path.join(ProjectPath.getToolsFolder(), r"ExporterActor/images/refresh.png")))
        
        # ****************** Load SubWidgets ******************
        self.actorWidgs = self.LoadActors(ActorManager.getActors())
        
        # ********* Events Connections
        self.ui.lbl_Help.clicked.connect(self.label_clicked)
        self.ui.btn_BrowseExport.clicked.connect(self.btn_BrowseExport_Clicked)
        self.ui.ckb_OverridePaths.stateChanged.connect(self.ckb_OverridePaths_StateChanged)
        self.ui.cbx_ExportDir.currentIndexChanged.connect(self.cbx_ExportDir_CurrentIndexChanged)
        self.ui.cbx_Branch.currentIndexChanged.connect(self.cbx_Branch_CurrentIndexChanged)
        self.ui.btn_AllNone.clicked.connect(self.btn_AllNone_Clicked)
        self.ui.btn_CreateFromSelection.clicked.connect(self.btn_CreateFromSelection_Clicked)
        self.ui.cbx_ExportDir.customContextMenuRequested.connect(self.__cbx_ExportDir_ContextMenu)
        self.ui.btn_Refresh.clicked.connect(self.btn_Refresh_Clicked)
        self.ui.btn_ExportCharacters.clicked.connect(self.btn_ExportCharacters_Clicked)
        
        # ********* Actions 
        self.clearOverridePathsAction =  QtWidgets.QAction("Clear", None)
        self.clearOverridePathsAction.triggered.connect(self.clearOverridePathsActionn_Triggered)
    
    def onUndo(self):
        self.btn_Refresh_Clicked()
    
    def LoadActors(self, ActorNodes=[]):
        result = []
        
        actorsListLayout = self.ui.frm_Characters.layout()
        for actor in ActorNodes:
            actWidg = ActorExportWidget.ActorExportWidget(actor, self, self.ui.cbx_Branch.currentText())
            actorsListLayout.addWidget(actWidg)
            result.append(actWidg)
        
        return result
    
    def setPathsOverriden(self, overridenStatus):
        ovPath = None
        if (overridenStatus > 0):
            ovPath = self.ui.cbx_ExportDir.currentText()
        
        for actorWidg in self.actorWidgs:
            actorWidg.setPathOverride(ovPath)
    
    def GetSelectedIdxs(self):
        result = []
        
        for i in range(len(self.actorWidgs)):
            if (self.actorWidgs[i].ui.gbx_Actor.isChecked()):
                result.append(i)
        
        return result
    
    def saveOverridenPaths(self):
        paths = []
        currCount = self.ui.cbx_ExportDir.count()
        for idx in range(0,currCount):
            paths.append(self.ui.cbx_ExportDir.itemText(idx))
        
        utils.SaveLastUsedPaths(paths)
    
    def registerCallbacks(self):
        self.undoScriptJob = Bridge.CreateScriptJob(e=["Undo", self.onUndo])
        self.redoScriptJob = Bridge.CreateScriptJob(e=["Redo", self.onUndo])

    def deregisterCallbacks(self):
        Bridge.KillScriptJob(self.undoScriptJob)
        Bridge.KillScriptJob(self.redoScriptJob)
    
    def GetSubactorsToExport(self):
        result = []
        for actorWdg in self.actorWidgs:
            result += actorWdg.GetSubactorsToExport()
        return result
    
    def __cbx_ExportDir_ContextMenu(self, location):
        menu = QMenu(self.ui.cbx_ExportDir)
        menu.addAction(self.clearOverridePathsAction)
        menu.popup(self.ui.cbx_ExportDir.mapToGlobal(location))
    
    # ******************************************************
    # *********************** EVENTS ***********************
    # ******************************************************
    def showEvent(self, event):
        self.registerCallbacks()
    
    def closeEvent(self, event):
        Bridge.EvalDeferred(self.deregisterCallbacks)
    
    def label_clicked(self):
        custDict = {Tokens.TActorName : None, Tokens.TSubActorName : None, Tokens.TActorType : None}
        tkzr = PathTokenizer(custDict)
        fullDict = tkzr.GetFullDictionary()
        
        title = "Info"
        message = "Actor Exporter.\n\
            \n\
            \nAvailable tokens:\n"
        
        for t in sorted(fullDict):
            message += "\n{{{}}}\t: {}".format(t, fullDict[t] if (fullDict[t] != None) else "** Asset Specific **")
        
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
    
    def btn_BrowseExport_Clicked(self):
        dir = self.ui.cbx_ExportDir.currentText()
        if (dir == ""):
            dir = Bridge.GetCurrentFilePath()
        
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Export Folder", dir, QtWidgets.QFileDialog.ShowDirsOnly)
        if (fileName != ""):
            currCount = self.ui.cbx_ExportDir.count()
            idx = 0
            exists = False
            for idx in range(0,currCount):
                if (self.ui.cbx_ExportDir.itemText(idx) == fileName):
                    exists = True
                    break
            
            if (not exists):
                if (self.ui.cbx_ExportDir.count() >= ActorExporterWindow.maxOverridePaths):
                    self.ui.cbx_ExportDir.removeItem(1)
                self.ui.cbx_ExportDir.addItem(fileName)
                self.ui.cbx_ExportDir.setCurrentIndex(self.ui.cbx_ExportDir.count()-1)
            else:
                self.ui.cbx_ExportDir.setCurrentIndex(idx)
            
            self.ui.ckb_OverridePaths.setEnabled(True)
            self.ui.ckb_OverridePaths.setChecked(True)
            self.saveOverridenPaths()
    
    def ckb_OverridePaths_StateChanged(self, status):
        self.ui.cbx_ExportDir.setEnabled(status)
        self.setPathsOverriden(status)
    
    def cbx_ExportDir_CurrentIndexChanged(self, arg):
        if (self.ui.ckb_OverridePaths.isChecked()):
            for actorWid in self.actorWidgs:
                actorWid.setPathOverride(self.ui.cbx_ExportDir.currentText())
                actorWid.updateExportPaths()
    
    def cbx_Branch_CurrentIndexChanged(self, arg):
        for actorWid in self.actorWidgs:
            for subActorWid in actorWid.subActorWidgs:
                subActorWid.SetBranch(self.ui.cbx_Branch.currentText())
    
    def btn_AllNone_Clicked(self):
        seldIdxs = self.GetSelectedIdxs()
        newState = False
        
        if (len(seldIdxs) != len (self.actorWidgs)):
            newState = True
            
        for actWidg in self.actorWidgs:
            actWidg.ui.gbx_Actor.setChecked(newState)
    
    # This shit has been implemented on a rush in order to give the modellears "easy" access
    # to creating a temp export subactor
    def btn_CreateFromSelection_Clicked(self):
        dcRootName = 'DC_Root'
        sel = Bridge.getCurrentSelection()
        if (not dcRootName in sel):
            Bridge.printWarning("No 'DC_Root' node in selection")
        else:
            selMeshes = []
            sceneMeshes = Bridge.getSceneNodesByType("mesh")
            if sceneMeshes:
                selMeshes = [x for x in sceneMeshes if (x in sel)]
            
            if (not selMeshes):
                Bridge.printWarning("No Meshes selected")
            else:
                invalidParent = [x for x in selMeshes if (Bridge.GetParentNode(x) != dcRootName)]
                if (invalidParent):
                    Bridge.printWarning("Some meshes are not direct children of 'DC_Root'")
                else:
                    sceneActors = ActorManager.getActors()
                    tempActorExists = False
                    for actor in sceneActors:
                        if actor.name == self.__tempExportActorName:
                            self.__tempExportActor = actor
                            tempActorExists = True
                    if (not tempActorExists):
                        self.__tempExportActor = ActorManager.createActor(self.__tempExportActorName)
                    
                    text, ok = QtWidgets.QInputDialog().getText(self, "New Subactor", "New subactor Name:", QtWidgets.QLineEdit.Normal)
                    text = text.rstrip().lstrip()
                    if (ok and text):
                        try:
                            newSubActor = self.__tempExportActor.createSubActor(text)
                            newSubActor.exportPath = Defaults.exportPath
                            newSubActor.subActorPathToken = Defaults.subActorPath
                            newSubActor.modelPath = Defaults.modelPath
                            newSubActor.animPath = Defaults.animsPath
                            newSubActor.modelName = Defaults.modelName
                            if (not self.__tempExportActor.mainSubActor):
                                self.__tempExportActor.mainSubActor = newSubActor
                            newSubActor.addGeometries(selMeshes)
                            newSubActor.addDcRoot('DC_Root')
                        except Exception as e:
                            Bridge.printWarning("Error creating SubActor: {}\n{}".format(text, e))
                        self.btn_Refresh_Clicked()
    
    def btn_Refresh_Clicked(self):
        actorsListLayout = self.ui.frm_Characters.layout()
        for i in reversed(range(actorsListLayout.count())): 
            actorsListLayout.itemAt(i).widget().setParent(None)
        
        self.actorWidgs = self.LoadActors(ActorManager.getActors())
    
    def btn_ExportCharacters_Clicked(self):
        subactorsToExport = self.GetSubactorsToExport()
        totalExportNumber = len(subactorsToExport)
        if (totalExportNumber > 0):
            # Init FBX settings only once if there are any
            numFBX = len([x for x in subactorsToExport if x[2]=='.fbx'])
            if (numFBX):
                utils.InitFBXSettings()
            
            totalExported = 0
            self.ui.pgb_ExportProgress.setMinimum(0)
            self.ui.pgb_ExportProgress.setMaximum(totalExportNumber)
            self.ui.pgb_ExportProgress.setHidden(False)
            self.ui.pgb_ExportProgress.setValue(0)
            
            for (subactor, exportPath, fileExtension, asciiMode) in subactorsToExport:
                try:
                    if (fileExtension == '.fbx'):
                        if (asciiMode):
                            MayaFBX.SetProperty(MayaFBX.FBXSettings.Export.AdvancedOptions.FBXFileFormat.fileType, MayaFBX.FBXSettings.Export.AdvancedOptions.FBXFileFormat.FileType.kASCII, verbose=True)
                        else:
                            MayaFBX.SetProperty(MayaFBX.FBXSettings.Export.AdvancedOptions.FBXFileFormat.fileType, MayaFBX.FBXSettings.Export.AdvancedOptions.FBXFileFormat.FileType.kBinary, verbose=True)
                        
                        utils.ExportModelFBX(exportPath, subactor)
                except Exception as err:
                    Bridge.printError("EXPORT ERROR: {}".format(err))
                totalExported +=1
                self.ui.pgb_ExportProgress.setValue(totalExported)
    
    def clearOverridePathsActionn_Triggered(self):
        for idx in range(self.ui.cbx_ExportDir.count()-1, -1, -1):
            self.ui.cbx_ExportDir.removeItem(idx)
        
        self.ui.ckb_OverridePaths.setEnabled(False)
        self.saveOverridenPaths()


if __name__ == '__main__':
    try:
        if exporterActorWindow.isVisible():
            exporterActorWindow.close()
    except NameError:
        pass
    exporterActorWindow = ActorExporterWindow()
    exporterActorWindow.show()