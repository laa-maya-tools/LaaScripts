# coding: utf-8

from PySide2 import QtWidgets, QtGui, QtCore

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window.ShotTable as ShotTable
import CinematicEditor.Window.ActorList as ActorList
import CinematicEditor.Window.IgnoreLayersDialog as IgnoreLayersDialog
import CinematicEditor.Window.OverrideSlaveDialog as OverrideSlaveDialog
import CinematicEditor.Window.CinematicEditorTimeline as CinematicEditorTimeline
import CinematicEditor.Window.PlayblastWindow as Playblast
import CinematicEditor.Window.CinematicExportDialog as CinematicExportDialog

import CinematicEditor.MasterSlave as MasterSlave

#from importlib import reload
#reload(CinematicEditor)
#reload(ShotTable)
#reload(ActorList)
#reload(IgnoreLayersDialog)
#reload(CinematicEditorTimeline)
#reload(Playblast)
#reload(CinematicExportDialog)
#reload(MasterSlave)

import QtCustomWidgets.QtUtils as QtUtils
from QtCustomWidgets.UIFileWidget import UIFileWidget

import Utils.Maya as MayaUtils
from Utils.Maya.UndoContext import UndoContext, UndoOff, clearUndo
from Utils.Maya.OptionVar import OptionVarConfiguration
import ProjectPath

import functools
import os

# TODO:
# - Atajos de teclado para funcionalidad del cinematic
    # Opción para framear todos los shots (poner un botón para ello también?)
# - Opciones:
    # Opción para desactivar el sync del timeline
    # Opción para seleccionar o no la cámara al cambiar de plano
    # Opción para colorear los planos en amarillo si comparten la frame actual
    # Opción para colorear los planos en rojo si comparten frames
    # Opción para no colorear los planos en rojo si comparten tan solo 1 frame
    # Opción para solo mostrar coloreados los conflictos de los planos seleccionados
    # Auto clamp al cambiar de plano
    # Camera frustrum (?)
    # Qué tecla usar, Ctrl o Shift, para seleccionar multiples shots o editarlos -> cambiar los tooltips!
    # Qué tecla usar para empezar a reproducir la cinemática desde el principio (?)
    # Opción para que seleccionar un shot en la ShotTable seleccione su cámara
    # Opción para que seleccionar un actor en la ActorList seleccione su master
# - Opción para setear las layers de un plano en click derecho
# - Auto setear las layers de un plano automaticamente al cambiar de plano de alguna manera? Con redraw apagado igual funciona bien incluso en play
# - Zoomear con el ratón en los clips (igual dar una opción de que no funcione esto?)
# - Eliminar reloads de todos los módulos
# - Separar exportador (en un menú? o en una pestaña?)
# - Maestro/Esclavo (menú avanzado?)
# - Subplanos (mismo plano, dividido entre varias personas)

WINDOW_GEOMETRY_OPTIONVAR = OptionVarConfiguration("WindowGeometry", "CINEMATIC_EDITOR_UI_WINDOW_GEOMETRY", OptionVarConfiguration.TYPE_INTEGER, 0)
SPLITTER_POSITION_OPTIONVAR = OptionVarConfiguration("SplitterPosition", "CINEMATIC_EDITOR_UI_SPLITTER_POSITION", OptionVarConfiguration.TYPE_INTEGER, 0)

class CinematicEditorMainwindow(MayaQWidgetBaseMixin, UIFileWidget):

    DEFAULT_WINDOW_TITLE = "Cinematic Editor"

    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------

    def __init__(self, parent=None):
        UIFileWidget.__init__(self, r"CinematicEditor/Window/ui/CinematicEditorMainWindow.ui", parent=parent)
        
        self.playbalstWindow = None
        
        self.cachedMasterSlaveFile = None

        # Window Configuration
        self.setWindowIcon(QtGui.QIcon(":/movie.svg"))
        
        # Shot Table
        self.shotTable = ShotTable.ShotTable(self)
        self.ui.shotTableContainer.layout().addWidget(self.shotTable)
        
        # Actor List
        self.actorList = ActorList.ActorList(self)
        self.ui.actorListContainer.layout().addWidget(self.actorList)
        
        # Signals
        self.shotTable.itemSelectionChanged.connect(self.refreshActors)
        self.ui.browseCutscenePathButton.clicked.connect(self.browseCutscenePath)
        self.ui.masterSlaveButton.clicked.connect(self.openMasterSlaveMenu)
        self.ui.addShotButton.clicked.connect(self.shotTable.addShot)
        self.ui.renameShotsButton.clicked.connect(self.renameShots)
        self.ui.renameCamerasButton.clicked.connect(self.renameShotCameras)
        self.ui.mergeActorButton.clicked.connect(self.actorList.mergeActor)
        self.ui.addActorButton.clicked.connect(self.actorList.addActor)
        self.ui.ignoreLayersButton.clicked.connect(self.showIgnoreLayersDialog)
        self.ui.reorderActorsButton.clicked.connect(self.reorderActorsAlfabetically)
        self.ui.exportButton.clicked.connect(self.exportSelectedOptions)
        self.ui.playblastButton.clicked.connect(self.openPlayblastDialog)
        
        self.ui.masterSlaveButton.setMenu(QtWidgets.QMenu(self.ui.masterSlaveButton))
        self.ui.masterSlaveButton.menu().aboutToShow.connect(self.openMasterSlaveMenu)
        
        # Creates the CinematicEditorTimeline
        self.cinematicEditorTimeline = CinematicEditorTimeline.CinematicEditorTimeline(self)
        
        # Refreshes the UI to load the information from the cutscene
        self.updateCutscenePath()
        self.loadMasterSlave()
        self.reload()

    def loadUIConfiguration(self):
        if WINDOW_GEOMETRY_OPTIONVAR.exists():
            geometry = WINDOW_GEOMETRY_OPTIONVAR.value
            if type(geometry) == list:
                self.move(int(geometry[0]), int(geometry[1]))
                self.resize(int(geometry[2]), int(geometry[3]))
                
                if not QtGui.QGuiApplication.instance().desktop().geometry().intersects(self.geometry()):
                    self.move(0, 0)

        if SPLITTER_POSITION_OPTIONVAR.exists():
            sizes = SPLITTER_POSITION_OPTIONVAR.value
            if type(sizes) == list:
                self.ui.shotsActorsSplitter.setSizes(sizes)

    def saveUIConfiguration(self):
        WINDOW_GEOMETRY_OPTIONVAR.value = [self.x(), self.y(), self.width(), self.height()]
        SPLITTER_POSITION_OPTIONVAR.value = self.ui.shotsActorsSplitter.sizes()

    def registerCallbacks(self):
        self.undoCallback = cmds.scriptJob(e=["Undo", self.onUndo])
        self.redoCallback = cmds.scriptJob(e=["Redo", self.onUndo])
        self.lockChangeCallback = cmds.scriptJob(e=["transformLockChange", self.onLockChange])
        self.mayaExitingCallback = cmds.scriptJob(e=["quitApplication", self.onApplicationExit])    # The kMayaExiting callback on the API doesn't seem to work properly
        self.timeUnitChangedScriptJob = cmds.scriptJob(e=["timeUnitChanged", self.onTimeUnitChanged])

        self.fileOpenCallback = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kBeforeOpen, self.onFileOpen)
        self.fileNewCallback = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kBeforeNew, self.onFileOpen)
        
        #self.mayaExitingCallback = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kMayaExiting, self.onApplicationExit)
        
        self.referenceLoadedCallback = OpenMaya.MSceneMessage.addReferenceCallback(OpenMaya.MSceneMessage.kAfterLoadReference, self.onReferenceLoaded)
        self.referenceUnloadedCallback = OpenMaya.MSceneMessage.addReferenceCallback(OpenMaya.MSceneMessage.kAfterUnloadReference, self.onReferenceLoaded)

    def unregisterCallbacks(self):
        cmds.scriptJob(kill=self.undoCallback)
        cmds.scriptJob(kill=self.redoCallback)
        cmds.scriptJob(kill=self.lockChangeCallback)
        cmds.scriptJob(kill=self.mayaExitingCallback)
        cmds.scriptJob(kill=self.timeUnitChangedScriptJob)
        
        cmds.evalDeferred(functools.partial(OpenMaya.MMessage.removeCallback, self.fileOpenCallback))   # When a new file is opened, the CinematicEditor will be closed, which will call this function. We cannot remove this callback when it's being called.
        cmds.evalDeferred(functools.partial(OpenMaya.MMessage.removeCallback, self.fileNewCallback))   # When a new file is opened, the CinematicEditor will be closed, which will call this function. We cannot remove this callback when it's being called.
        
        #OpenMaya.MMessage.removeCallback(self.mayaExitingCallback)
        
        OpenMaya.MMessage.removeCallback(self.referenceLoadedCallback)
        OpenMaya.MMessage.removeCallback(self.referenceUnloadedCallback)

    def reload(self):
        self.reloadShots()
        self.reloadActors()

    def reloadShots(self):
        self.shotTable.reload()
        self.refreshActors()
        self.cinematicEditorTimeline.reloadShots()

    def reloadActors(self):
        self.actorList.reload()

    def refreshShots(self):
        self.shotTable.refresh()
        self.cinematicEditorTimeline.refreshShots()

    def refreshActors(self):
        self.actorList.refresh()

    # ------------------------------------
    # | Path                             |
    # ------------------------------------

    def updateCutscenePath(self):
        windowTitle = self.DEFAULT_WINDOW_TITLE
        cutscenePath = ""
        expandedPath = ""
        
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            cutscenePath = cutscene.path or ""
            if cutscenePath != "":
                windowTitle += " - {}".format(cutscene.getCutsceneName())
                pathTokenizer = cutscene.getPathTokenizer()
                expandedPath = pathTokenizer.Translate(cutscenePath)
                
        self.setWindowTitle(windowTitle)
        
        self.ui.cutscenePathText.setText(expandedPath)
        self.ui.cutscenePathText.setToolTip((cutscenePath + "\n\nExpands to:\n" + expandedPath) if cutscenePath else "")
    
    def browseCutscenePath(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if masterSlaveFile:
            if masterSlaveFile.isMaster():
                result = QtWidgets.QMessageBox.question(self, "Browse Path", "This file is currently the Master of a Cutscene. Changing the path will have these consequences:\n* If the new path you select is not an already existing cutscene or is not a Master-Slave cutscene, all the information of this cutscene will be preserved as if it was never a Master.\n* If the new path you select is already a Master-Slave cutscene, it will become it's slave and all the current information of the file's cutscene will be replace by the new one's.\n\nAre you sure you want to change the Cutscene Path?")
                if result == QtWidgets.QMessageBox.No:
                    return
            elif masterSlaveFile.isSlave():
                result = QtWidgets.QMessageBox.question(self, "Browse Path", "This file is currently the Slave of a Cutscene. Changing the path will remove all the Cutscene data from this file.\n\nAre you sure you want to change the Cutscene Path?")
                if result == QtWidgets.QMessageBox.No:
                    return
                
        folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, caption="Select Cutscene Path", dir=ProjectPath.getCutscenesFolder())
        if folderPath != None and folderPath != "":
            cutscene = CinematicEditor.getCutscene()
            if cutscene and cutscene.path:
                cutscenePath = cutscene.getPathTokenizer().Translate(cutscene.path)
                if os.path.normpath(cutscenePath) == os.path.normpath(folderPath):
                    return  # No path change
            
            with UndoContext("Set Cutscene Path"):
                cutscene = CinematicEditor.getCutscene(createIfNotExists=True)
                pathTokenizer = cutscene.getPathTokenizer()
                folder = pathTokenizer.Tokenize(os.path.dirname(folderPath))
                folderPath = os.path.join(folder, os.path.basename(folderPath))
                cutscene.path = folderPath
                cutscene.masterSlaveID = -1 # In case the cutscene already existed, removes it's ID so it can be restored as an independent Cutscene (or become a Slave to the Cutscene on the new path)
                
            abort = False
            newMasterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
            if newMasterSlaveFile.exists(checkPerforce=True):
                if self.checkMasterSlaveFile(newMasterSlaveFile):
                    result = QtWidgets.QMessageBox.question(self, "Become Slave", "The Cutscene \"{0}\" has a Master defined and can't be edited without becoming it's Slave.\n\nDo you want to become a slave for the Cutscene \"{0}\"?\n\nWARNING: This operation is not undoable!".format(cutscene.getCutsceneName()))
                    if result == QtWidgets.QMessageBox.Yes:
                        newMasterSlaveFile.becomeSlave()
                        newMasterSlaveFile.load(recreate=True, cachePreviews=True)
                        clearUndo()
                    else:
                        QtWidgets.QMessageBox.warning(self, "Select Cutscene Path", "You can't use this Cutscene Path without becoming it's Slave!\n\n{}".format(folderPath))
                        abort = True
                else:
                    abort = True
            
            if abort:
                cmds.undo()
                with UndoContext(""):   # This context will remove the "Set Cutscene Path" that has been undone.
                    cmds.select(cmds.ls(selection=True))
            else:
                self.updateMasterSlaveConfiguration()
                self.updateCutscenePath()
                self.reload()

    # ------------------------------------
    # | Master / Slave                   |
    # ------------------------------------
    
    def getMasterSlaveFile(self, checkExists=True, checkPerforce=True):
        cutscene = CinematicEditor.getCutscene()
        if cutscene and cutscene.path:
            masterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
            if not checkExists or masterSlaveFile.exists(checkPerforce=checkPerforce):
                masterSlaveFile.load()
                self.cachedMasterSlaveFile = masterSlaveFile
                return masterSlaveFile
        self.cachedMasterSlaveFile = None
        return None
    
    def loadMasterSlave(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if masterSlaveFile:
            with UndoContext("Recreate Master-Slave Cutscene"):
                masterSlaveFile.load(recreate=True, cachePreviews=True)
        
        MasterSlave.MasterSlaveScreenDrawer.instance(createIfNotExists=True)
        
        self.updateMasterSlaveConfiguration()
    
    def checkMasterSlaveFile(self, masterSlaveFile):
        updateStatus = masterSlaveFile.getUpdateStatus(masterSlaveFile.getFilePaths())
        if updateStatus == masterSlaveFile.UPDATE_STATUS_NOT_IN_DEPOT:
            return True # If the file is not even on the depot, it will probably be marked for add, so it's valid
        if updateStatus == masterSlaveFile.UPDATE_STATUS_UNSYNC_CHECKOUT:
            QtWidgets.QMessageBox.warning(self, "Master Slave File", "The Cutscene \"{}\" has a Master defined but it's Master-Slave file is out of date and you have it checked out.\n\nPlease sync the file and resolve any conflict before proceeding.\n\n{}".format(masterSlaveFile.cutscene.getCutsceneName(), masterSlaveFile.getMasterFilePath()))
            return False
        if updateStatus == masterSlaveFile.UPDATE_STATUS_UNSYNC:
            result = QtWidgets.QMessageBox.question(self, "Master Slave File", "The Cutscene \"{}\" has a Master defined but it's Master-Slave file is out of date.\n\nDo you want to get the file's latest revision?".format(masterSlaveFile.cutscene.getCutsceneName()))
            if result == QtWidgets.QMessageBox.Yes:
                masterSlaveFile.syncFile()
                return True
            else:
                QtWidgets.QMessageBox(self, "Master Slave File", "You can't use this Cutscene Path without having the last revision of the Master-Slave file!\n\n{}".format(masterSlaveFile.getMasterFilePath()))
                return False
        if updateStatus == masterSlaveFile.UPDATE_STATUS_SYNC:
            return True
        raise AssertionError("Unknown update status: {}".format(updateStatus))
    
    def updateMasterSlaveConfiguration(self):
        masterSlaveFile = self.getMasterSlaveFile()
        
        palette = QtGui.QPalette()
        
        if not masterSlaveFile:
            cutscene = CinematicEditor.getCutscene()
            if cutscene:
                # In case this cutscene was part of a Master-Slave system that no longer exists, we use the "becomeFree" method to clean this file.
                masterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
                with UndoOff():
                    masterSlaveFile.becomeFree()
            
            masterSlaveButtonText = "Options..."
            
            addShotButtonEnabled = True
            renameShotsButtonEnabled = True
            
        else:
            if not self.checkMasterSlaveFile(masterSlaveFile):
                masterSlaveButtonText = "UNSYNC"
                palette.setColor(QtGui.QPalette.Button, QtCore.Qt.yellow)
                palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.yellow)
            
                addShotButtonEnabled = False
                renameShotsButtonEnabled = False
            
            elif masterSlaveFile.isMaster():
                masterSlaveButtonText = "Master"
                palette.setColor(QtGui.QPalette.Button, QtCore.Qt.green)
                palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.green)
            
                addShotButtonEnabled = True
                renameShotsButtonEnabled = True
                
            elif masterSlaveFile.isSlave():
                masterSlaveButtonText = "Slave"
                palette.setColor(QtGui.QPalette.Button, QtCore.Qt.red)
                palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.red)
            
                addShotButtonEnabled = False
                renameShotsButtonEnabled = False
                
            else:
                raise AssertionError("Cutscene has a master but this file is neither a master or a slave!")
        
        self.ui.masterSlaveButton.setText(masterSlaveButtonText)
        self.ui.masterSlaveButton.setPalette(palette)
        
        self.ui.addShotButton.setEnabled(addShotButtonEnabled)
        self.ui.renameShotsButton.setEnabled(renameShotsButtonEnabled)
        
        self.cinematicEditorTimeline.updateMasterSlaveConfiguration()

    def openMasterSlaveMenu(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile:
            options = [
                QtUtils.MenuOption("convertToMaster", "Convert to Master", False, self.onConvertToMasterOptionSelected, "<p>Converts this file into the Master of this cutscene, allowing the user to delegate shots to another files.</p><p>There can only be one Master per cutscene.</p>"),
                QtUtils.MenuOption("convertToSlave", "Convert to Slave", False, self.onConvertToSlaveOptionSelected, "<p>Converts this file into a Slave for another cutscene, allowing the user to take delegated shots.</p><p>A file can only be a Slave for a cutscene with a Master.</p>")
            ]
        else:
            options = []
            if masterSlaveFile.isMaster():
                options += [
                    QtUtils.MenuOption("delegateSelectedShots", "Delegate Selected Shots", False, self.onDelegateSelectedShotsOptionSelected, "<p>Delegates the selected shots, allowing Slave files to work with them.</p><p><b>Warning</b>: You will no longer be able to modify delegated shots until you reclaim them.</p>"),
                    QtUtils.MenuOption("reclaimSelectedShots", "Reclaim Selected Shots", False, self.onReclaimSelectedShotsOptionSelected, "<p>Reclaims the selected shots, so they will be handled by the Master file instead of any Slave file.</p><p><b>Warning</b>: Slave files will no longer be able to modify this shot.</p>"),
                    None,
                    QtUtils.MenuOption("saveMasterFiles", "Save Master Files", False, self.onSaveMasterFilesOptionSelected, "<p>Saves the Master file and creates or destroys any delegated shot's file if necessary.</p><p><b>Note</b>: This operation is usually not necessary since changes are saved automatically. Use it if external changes have been made to the files.</p>"),
                    None,
                    QtUtils.MenuOption("releaseCutscene", "Release Cutscene", False, self.onReleaseOptionSelected, "<p>Releases the cutscene from the Master-Slave System, restoring it to a normal cutscene. It will no longer have any master nor slave files.</p><p><b>Warning</b>: All Master-Slave information will be lost. Any existing file, Master or Slave will become completely free and able to modify and export the full cutscene.</p>"),
                    QtUtils.MenuOption("convertToSlave", "Convert to Slave", False, self.onConvertToSlaveOptionSelected, "<p>Converts this file into a Slave for this same cutscene, allowing the user to take delegated shots.</p><p><b>Warning</b>: The file will no longer be the Master. Please be sure there is another Master file (or a copy of this one).</p>")
                ]
            elif masterSlaveFile.isSlave():
                options += [
                    QtUtils.MenuOption("claimSelectedShots", "Claim Selected Shots", False, self.onClaimSelectedShotsOptionSelected, "<p>Claims the selected shots, allowing this file and none other to modify them.</p>"),
                    QtUtils.MenuOption("releaseSelectedShots", "Release Selected Shots", False, self.onReleaseSelectedShotsOptionSelected, "<p>Releases the selected claimed shots, so the file won't be able to modify them anymore.</p><p><b>Warning</b>: The information about cameras, ranges, and colors of released shots in this file will be lost even if you reclaim them later.</p>"),
                    None,
                    QtUtils.MenuOption("saveSlaveFiles", "Save Slave Files", False, self.onSaveSlaveFilesOptionSelected, "<p>Saves the delegated shots' files claimed by this Slave.</p><p><b>Note</b>: This operation is usually not necessary since changes are saved automatically. Use it if external changes have been made to the files.</p>"),
                    None,
                    QtUtils.MenuOption("overrideMaster", "Override Master", False, self.onOverrideMasterOptionSelected, "<p>Converts this file into the Master of this cutscene, even if it is only a Slave.</p><p><b>Warning</b>: Doing this will cause multiple masters to exist. This will cause conflicts, use with extreme caution.</p>"),
                    QtUtils.MenuOption("overrideSlave", "Override Slave", False, self.onOverrideSlaveOptionSelected, "<p>Becomes a copy of an existing Slave, taking all their delegated Shots.</p><p><b>Warning</b>: Doing this will cause multiple slaves to work on the same shots. This will cause conflicts, use with extreme caution.</p>")
                ]
                
            options += [
                None,
                QtUtils.MenuOption("becomeFree", "Become Free", False, self.onBecomeFreeOptionSelected, "<p>Frees the file, no longer being tied to the Cutscene or the Master-Slave system.</p><p>The file's export path will be cleared, so it won't be able to be exported.<</p>"),
                None,
                QtUtils.MenuOption("syncMasterSlaveFiles", "Sync Master-Slave Files{}".format("" if masterSlaveFile.isUpdated() else " (!!)"), False, self.onSyncMasterSlaveFilesOptionSelected, "<p>Updates the Master-Slave files from Perforce.</p><p>You can't perform any operations related to the Master-Slave system until these files are updated.</p>"),
                QtUtils.MenuOption("syncPlayblastFiles", "Sync Playblast Files{}".format("" if masterSlaveFile.arePreviewsUpdated() else " (!!)"), False, self.onSyncPlayblastFilesOptionSelected, "<p>Updates the Playblast files from Perforce.</p><p>Playblast files allows the Master and Slaves files to visualize the work of the other files.</p>"),
                None,
                QtUtils.MenuOption("performPlayblast", "Perform Playblast", False, self.onPerformPlayblastOptionSelected, "<p>Playblasts the file's shots to the official location so they can be uploaded and shared on Perforce.</p><p>Playblast files allows the Master and Slaves files to visualize the work of the other files.</p>"),
                QtUtils.MenuOption("checkoutlayblastFiles", "Checkout Playblast Files", False, self.onCheckoutPlayblastFilesOptionSelected, "<p>Checks out the playblast files used by this cutscene on Perforce.</p><p>Playblast files allows the Master and Slaves files to visualize the work of the other files.</p>"),
                QtUtils.MenuOption("showOverlay", "Show Viewport Overlay", False, self.onShowMasterSlaveViewportOverlayOptionSelected, "<p>Shows an overlay on the viewport indicating whether the current shot is owned by the file or not.</p>", checkable=True, checked=MasterSlave.MasterSlaveScreenDrawer.instance().enabled)
            ]
        
        QtUtils.showContextMenu(options, self.ui.masterSlaveButton, self.ui.masterSlaveButton.mapToGlobal(QtCore.QPoint(0, self.ui.masterSlaveButton.height())))

    # Menu Options -----------------------
    
    def onConvertToMasterOptionSelected(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None or not cutscene.path:
            QtWidgets.QMessageBox.warning(self, "Convert to Master", "You must specify the cutscene's path first in order to convert into a Master.")
            return
        
        masterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
        if masterSlaveFile.exists(checkPerforce=True):
            raise AssertionError("Attempting to convert a file to a Master when there is already a Master File!")
        
        result = QtWidgets.QMessageBox.question(self, "Become Master", "This operation is not undoable, do you want to become the Master of this Cutscene?")
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.becomeMaster()
        clearUndo()
        
        self.updateMasterSlaveConfiguration()
        
    def onConvertToSlaveOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if masterSlaveFile:
            if not masterSlaveFile.isMaster():
                raise AssertionError("The file is not a Master!")
            
            result = QtWidgets.QMessageBox.question(self, "Become Slave", "This operation is not undoable, do you want to become a Slave for this Cutscene?")
            if result != QtWidgets.QMessageBox.Yes:
                return
            
            masterSlaveFile.becomeSlave()
            clearUndo()
            
            self.updateMasterSlaveConfiguration()
            self.reload()
            
        else:
            # This option should only be reachable when there is not a cutscene yet on the scene or if it's path has not been set yet. As such, it only needs to ask the user for the cutscene's path.
            with UndoContext("Become Slave"):
                cutscene = CinematicEditor.getCutscene()
                currentPath = cutscene.path if cutscene else None
                
                self.browseCutscenePath()
            
                if not self.getMasterSlaveFile():
                    cutscene = CinematicEditor.getCutscene()
                    cutscene.path = currentPath
                    self.updateCutscenePath()
                    
                    QtWidgets.QMessageBox.warning(self, "Become Slave", "The selected cutscene path doesn't have a Master-Slave file defined! You can't become it's slave.")
    
    # Master Options -----------------------
    
    def onDelegateSelectedShotsOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isMaster():
            raise AssertionError("Only Masters can delegate shots!")
        
        selectedShots = self.shotTable.getSelectedShots()
        shotsToDelegate = [shot for shot in selectedShots if shot.enabled and not masterSlaveFile.isShotDelegated(shot)]
        
        if len(shotsToDelegate) == 0:
            QtWidgets.QMessageBox.warning(self, "Delegate Shots", "Please select the Shots to delegate. Only Enabled shots can be delegated.")
            return
        
        message = "This operation is not undoable, are you sure you want to Delegate the following Shots?"
        for shot in shotsToDelegate:
            message += "\n- {}".format(shot.shotName)
        message += "\n\nNOTE: You won't be able to modify these shots anymore unless you reclaim them."
        result = QtWidgets.QMessageBox.question(self, "Delegate Shots", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.delegateShots(shotsToDelegate)
        clearUndo()
        
        self.reload()
    
    def onReclaimSelectedShotsOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isMaster():
            raise AssertionError("Only Masters can reclaim shots!")
        
        selectedShots = self.shotTable.getSelectedShots()
        shotsToReclaim = [shot for shot in selectedShots if masterSlaveFile.isShotDelegated(shot)]
        
        if len(shotsToReclaim) == 0:
            QtWidgets.QMessageBox.warning(self, "Reclaim Shots", "Please select the Shots to reclaim. Only delegated shots can be reclaimed.")
            return
        
        message = "This operation is not undoable, are you sure you want to reclaim the following Shots?"
        for shot in shotsToReclaim:
            message += "\n- {}".format(shot.shotName)
        result = QtWidgets.QMessageBox.question(self, "Reclaim Shots", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
            
        alreadyclaimedShots = [shot for shot in shotsToReclaim if masterSlaveFile.isShotClaimed(shot)]
        if len(alreadyclaimedShots) > 0:
            message = "The following Shots have already been claimed by Slave files, do you want to force the reclaim?\n"
            for shot in alreadyclaimedShots:
                message += "\n- {}".format(shot.shotName)
            message += "\n\WARNING: The Slave files which claimed the Shots won't be able to modify them anymore."
            result = QtWidgets.QMessageBox.question(self, "Reclaim Shots", message, buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Cancel:
                return
            elif result == QtWidgets.QMessageBox.No:
                shotsToReclaim = [shot for shot in shotsToReclaim if shot not in alreadyclaimedShots]
            
        masterSlaveFile.claimShots(shotsToReclaim)
        clearUndo()
        
        self.reload()
    
    def onSaveMasterFilesOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isMaster():
            raise AssertionError("The file is not a Master!")
        
        masterSlaveFile.saveMasterFile()
        masterSlaveFile.saveOrDeleteAllDelegatedShotsFiles()
    
    def onReleaseOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isMaster():
            raise AssertionError("Only the Master can release the Cutscene!")
        
        if len(masterSlaveFile.delegatedShots) != 0:
            QtWidgets.QMessageBox.warning(self, "Release Cutscene", "In order to release the cutscene the Master must own all the shots. No shot may remain delegated.")
            return
        
        message = "You are about to release the cutscene, effectively restoring it to a normal cutscene.\n\
* The cutscene will no longer have any master nor slaves.\n\
* All other master and slave files will be affected and become \"another version\" of the cutscene.\n\
* Any information already present on the file will be preserved.\n\n\
This process cannot be undone, are you sure you want to release the cutscene?\n\n\
WARNING: This will affect every file related to the cutscene. Be sure you have all the information in this file before releasing the cutscene."
        result = QtWidgets.QMessageBox.question(self, "Release Cutscene", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.release()
        clearUndo()
        
        self.updateMasterSlaveConfiguration()
        self.reload()
        
    # Slave Options -----------------------
    
    def onClaimSelectedShotsOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isSlave():
            raise AssertionError("Only Slave files can claim shots!")
        
        selectedShots = self.shotTable.getSelectedShots()
        shotsToClaim = [shot for shot in selectedShots if masterSlaveFile.isShotDelegated(shot) and not masterSlaveFile.ownsShot(shot)]
        
        if len(shotsToClaim) == 0:
            QtWidgets.QMessageBox.warning(self, "Claim Shots", "Please select the Shots to claim. Only delegated shots can be claimed.")
            return
        
        alreadyclaimedShots = [shot for shot in shotsToClaim if masterSlaveFile.isShotClaimed(shot)]
        if len(alreadyclaimedShots) > 0:
            message = "You can't reclaim the following Shots since they have already been claimed by other Slaves:"
            for shot in alreadyclaimedShots:
                message += "\n- {}".format(shot.shotName)
            if len(alreadyclaimedShots) < len(shotsToClaim):
                message += "\n\nDo you still want to claim the remaining Shots?"
                for shot in shotsToClaim:
                    if shot not in alreadyclaimedShots:
                        message += "\n- {}".format(shot.shotName)
                result = QtWidgets.QMessageBox.question(self, "Claim Shots", message)
                if result != QtWidgets.QMessageBox.Yes:
                    return
                
                shotsToClaim = [shot for shot in shotsToClaim if shot not in alreadyclaimedShots]
                
            else:
                QtWidgets.QMessageBox.warning(self, "Claim Shots", message)
                return
                 
        else:
            message = "This operation is not undoable, are you sure want to claim these Shots?"
            for shot in shotsToClaim:
                if shot not in alreadyclaimedShots:
                    message += "\n- {}".format(shot.shotName)
            result = QtWidgets.QMessageBox.question(self, "Claim Shots", message)
            if result != QtWidgets.QMessageBox.Yes:
                return
            
        masterSlaveFile.claimShots(shotsToClaim)
        clearUndo()
        
        self.reload()
    
    def onReleaseSelectedShotsOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isSlave():
            raise AssertionError("Only Slave files can release shots!")
        
        selectedShots = self.shotTable.getSelectedShots()
        shotsToRelease = [shot for shot in selectedShots if masterSlaveFile.ownsShot(shot)]
        
        if len(shotsToRelease) == 0:
            QtWidgets.QMessageBox.warning(self, "Release Shots", "Please select the Shots to release. Only Claimed shots can be released.")
            return
        
        message = "This operation is not undoable, are you sure you want to release the following Shots?"
        for shot in shotsToRelease:
            message += "\n- {}".format(shot.shotName)
        message += "\n\nWARNING: Once you release these shots, all their information on this file will be lost, even if you reclaim them later."
        result = QtWidgets.QMessageBox.question(self, "Release Shots", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.delegateShots(shotsToRelease)
        clearUndo()
        
        self.reload()
    
    def onOverrideMasterOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isSlave():
            raise AssertionError("The file is not a Slave!")
        
        message = "You are about to become the Master of this cutscene.\n\
* You will be able to modify any non-delegated shot.\n\
* You will be responsible to manage the delegated shots and export the general structure of the cutscene.\n\
* Any delegated shot you have already claimed will remain unchanged.\n\n\
This process cannot be undone, are you sure you want to override the Master of the cutscene?\n\n\
WARNING: The previous Master file will still be considered a Master and there might be conflicts, proceed with extreme caution!"
        result = QtWidgets.QMessageBox.question(self, "Override Master", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.overrideMaster()
        clearUndo()
        
        self.updateMasterSlaveConfiguration()
        self.reload()
    
    def onOverrideSlaveOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isSlave():
            raise AssertionError("The file is not a Slave!")
        
        OverrideSlaveDialog.OverrideSlaveDialog(masterSlaveFile).exec_()
        
        self.reload()
    
    def onSaveSlaveFilesOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile or not masterSlaveFile.isSlave():
            raise AssertionError("The file is not a Slave!")
        
        for shot in masterSlaveFile.getOwnedShots():
            masterSlaveFile.saveDelegatedShotFile(shot)
    
    # Common Options -----------------------
    # These options should only be visible when there is a cutscene on the scene, it's path has been set and there's also a Master-Slave file associated to it.
    
    def onBecomeFreeOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile()
        if not masterSlaveFile:
            raise AssertionError("The Cutscene doesn't have a Master!")
        
        message = "You are about to free this file from the cutscene.\n\
* The cutscene path will be cleared, so the file will no longer be associated to that cutscene.\n\
* The file will no longer depend on the Master-Slave system and will be able to change any field on the CinematicEditor.\n\
* Any information already present on the file will be preserved.\n\n\
This process cannot be undone, are you sure you want to become free from the cutscene?\n\n\
WARNING: All the other files will remain unchanged. Other versions of this Slave will still be Slaves and own their claimed Shots."
        result = QtWidgets.QMessageBox.question(self, "Become Free", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.becomeFree(clearPath=True)  # The path must be cleared in order to not interfere with other files.
        clearUndo()
        
        self.updateMasterSlaveConfiguration()
        self.updateCutscenePath()
        self.reload()
        
    def onSyncMasterSlaveFilesOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile(checkExists=False)
        
        #if masterSlaveFile.isUpdated():
        #    QtWidgets.QMessageBox.warning(self, "Sync Files", "All Master-Slave files are up to date.")
        #    return
        
        result = QtWidgets.QMessageBox.question(self, "Sync Files", "Updating the Master-Slave files will conform this cutscene to the data on them, and this process cannot be undone.\nAre you sure you want to update the Master-Slave files?")
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        masterSlaveFile.syncFiles()
        clearUndo()
        
        self.loadMasterSlave()
        self.reload()
    
    def onSyncPlayblastFilesOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile(checkExists=False)
        
        masterSlaveFile.syncPreviewFiles()
        
        masterSlaveFile.load(recreate=False, cachePreviews=True)
    
    def onPerformPlayblastOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile(checkExists=False)
        
        masterSlaveFile.checkoutPlayblastFiles()
        
        playblastFolder = masterSlaveFile.getShotPreviewFolder()
        self.performPlayblast(shotOption=0, path=playblastFolder)
        
        # We need to do this operation twice: The first time already existing Perforce files will be checked out.
        # The second time newly created Playblast files will be marked for add on Perforce.
        masterSlaveFile.checkoutPlayblastFiles()
    
    def onCheckoutPlayblastFilesOptionSelected(self):
        masterSlaveFile = self.getMasterSlaveFile(checkExists=False)
        
        masterSlaveFile.checkoutPlayblastFiles()
        
    def onShowMasterSlaveViewportOverlayOptionSelected(self, state):
        MasterSlave.MasterSlaveScreenDrawer.instance().enabled = state
    
    # ------------------------------------
    # | Methods                          |
    # ------------------------------------

    def renameShots(self):
        if self.cachedMasterSlaveFile:
            if not self.cachedMasterSlaveFile.isMaster():
                raise AssertionError("Only the Master can rename Shots!")
            if len(self.cachedMasterSlaveFile.delegatedShots) > 0:
                QtWidgets.QMessageBox.warning(self, "Auto-Rename Shots", "You can't auto-rename the Shots when there are delegated Shots!")
                return
            
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            result = QtWidgets.QMessageBox.question(self, "Rename Shots", "This will rename the shot to match their index (for instance, the shot number 1 will be renamed to S001).\nProceed?")
            if result == QtWidgets.QMessageBox.Yes:
                with UndoContext("Rename Shots"):
                    shots = cutscene.getShots()                    
                    for i, shot in enumerate(shots):
                        shot.shotName = "S{}".format(str(i + 1).zfill(3))

                    self.refreshShots()

    def renameShotCameras(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:
            result = QtWidgets.QMessageBox.question(self, "Rename Shot Cameras", "This will rename the shots' cameras to match their index (for instance, the camera for shot number 1 will be DC_Cam001).\nProceed?")
            if result == QtWidgets.QMessageBox.Yes:
                with UndoContext("Rename Shot Cameras"):
                    shots = cutscene.getShots()
                    renamedCameras = set()
                    for i, shot in enumerate(shots):
                        camera = shot.camera
                        if camera != None and camera not in renamedCameras:
                            renamedCameras.add(camera)
                            newCameraName = "DC_Cam{}".format(str(i + 1).zfill(3))
                            if camera != newCameraName:
                                if cmds.objExists(newCameraName):
                                    MayaUtils.renameCamera(newCameraName, "{}_duplicated".format(newCameraName), autoRenameDuplicated=True)
                                MayaUtils.renameCamera(camera, newCameraName)

                    self.refreshShots()

    def showIgnoreLayersDialog(self):
        IgnoreLayersDialog.IgnoreLayersDialog(CinematicEditor.getCutscene(), self).exec_()

    def reorderActorsAlfabetically(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            cutsceneActors = []
        else:
            cutsceneActors = cutscene.getCutsceneActors()
        if len(cutsceneActors) == 0:
            QtWidgets.QMessageBox.information(self, "Reorder Actors Alfabetically", "There are no actors to reorder!")
            return
        
        if QtWidgets.QMessageBox.question(self, "Reorder Actors Alfabetically", "This will reorder the actors alfabetically. Proceed?") == QtWidgets.QMessageBox.Yes:
            with UndoContext("Reorder Actors"):
                cutsceneActors.sort(key=lambda x: x.actor.getNamespace().lower())
                
                for cutsceneActor in cutsceneActors:
                    cutscene.removeCutsceneActor(cutsceneActor, disableInAllShots=False)
                    
                for cutsceneActor in cutsceneActors:
                    cutscene.addCutsceneActor(cutsceneActor, enableInAllShots=False)
                    
                self.reloadActors()
    
    # ------------------------------------
    # | Export                           |
    # ------------------------------------

    def exportSelectedOptions(self):
        cutscene = CinematicEditor.getCutscene()
        if not cutscene.path:
            QtWidgets.QMessageBox.warning(self, "Export Cutscene", "You must define the Cutscene Path first!")
            return
        
        exportActors = self.ui.exportActorsCheck.isChecked()
        exportCameras = self.ui.exportCamerasCheck.isChecked()
        exportStructure = self.ui.exportShotInfoCheck.isChecked()
        
        if not (exportActors or exportCameras or exportStructure):
            QtWidgets.QMessageBox.warning(self, "Export Cutscene", "You must select at least one option to export!")
            return
        
        shots = cutscene.getActiveShots()
        actors = cutscene.getActiveCutsceneActors() if exportActors else []
        
        exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
        exportDialog.export(shots=shots, actors=actors, cameras=exportCameras, structure=exportStructure)
        
    # ------------------------------------
    # | Playblast                        |
    # ------------------------------------

    def openPlayblastDialog(self):
        cutscene = CinematicEditor.getCutscene()
        if not cutscene or not cutscene.getEnabledShots():
            QtWidgets.QMessageBox.warning(self, "Playblast", "There are no shots to playblast!")
            return
        if not cutscene.path:
            QtWidgets.QMessageBox.warning(self, "Playblast", "In order to playblast you must first select the cutscene Path!")
            return
        
        if not self.playbalstWindow:
            self.playbalstWindow = Playblast.CinematicPlayblastUI(CinematicEditor.getCutscene(), parent=self)
        self.playbalstWindow.show()
        
    def performPlayblast(self, shotOption=None, mergeOption=None, path=None):
        if not self.playbalstWindow:
            self.playbalstWindow = Playblast.CinematicPlayblastUI(CinematicEditor.getCutscene(), parent=self)
        
        self.playbalstWindow.refresh()
        
        if shotOption != None:
            oldShotOption = self.playbalstWindow.playblastShotsOptionsRadiobuttonGroup.checkedId()
            self.playbalstWindow.playblastShotsOptionsRadiobuttonGroup.button(shotOption).setChecked(True)
        if mergeOption != None:
            oldMergeOption = self.playbalstWindow.mergeOptionsRadiobuttonGroup.checkedId()
            self.playbalstWindow.mergeOptionsRadiobuttonGroup.button(mergeOption).setChecked(True)
        if path != None:
            oldPath = self.playbalstWindow.output_dir_path_le.text()
            self.playbalstWindow.output_dir_path_le.setText(path)
        
        self.playbalstWindow.do_playblast()
        
        if shotOption != None:
            self.playbalstWindow.playblastShotsOptionsRadiobuttonGroup.button(oldShotOption).setChecked(True)
        if mergeOption != None:
            self.playbalstWindow.mergeOptionsRadiobuttonGroup.button(oldMergeOption).setChecked(True)
        if path != None:
            self.playbalstWindow.output_dir_path_le.setText(oldPath)

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------
    
    def onUndo(self, *args):
        self.reload()
    
    def onLockChange(self):
        # Triggered when an object lock state is changed
        # This object might be a camera, so we refresh the shot table
        self.shotTable.refresh()
    
    def onReferenceLoaded(self, referenceNode, referenceFile, *args):
        # When a reference is loaded or unloaded, the wrappers pointing to its' nodes will break. Recreate them.
        self.reloadActors()
    
    def onApplicationExit(self, *args):
        self.saveUIConfiguration()
        self.cinematicEditorTimeline.saveUIConfiguration()
    
    def onFileOpen(self, *args):
        self.close()
        
    def onTimeUnitChanged(self, *args):
        self.refreshShots()
    
    def showEvent(self, e):
        self.loadUIConfiguration()
        self.registerCallbacks()
        
        if self.cinematicEditorTimeline and self.cinematicEditorTimeline.isHidden():
            self.cinematicEditorTimeline.show(dockable=True, uiScript="None")
    
    def closeEvent(self, e):
        self.saveUIConfiguration()
        self.unregisterCallbacks()
        
        if self.cinematicEditorTimeline and not self.cinematicEditorTimeline.isHidden():
            cmds.workspaceControl(self.cinematicEditorTimeline.workspaceControlName, e=True, close=True)
