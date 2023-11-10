# coding: utf-8

from PySide2 import QtCore, QtWidgets, QtGui, QtUiTools

import maya.cmds as cmds

import ExporterWindow.ExporterWindowTab as ExporterWindowTab
import ExporterWindow.AnimWidget as AnimWidget
import ExporterWindow.AnimWidgetPanel as AnimWidgetPanel

import ScreenDrawer.CinematicGuides as CinematicGuides

import ActorManager
import ActorManager.AnimPreset as AnimPreset
import ActorManager.SubActor as SubActor
import ActorManager.CameraSet as CameraSet

from Utils.Maya.UndoContext import UndoContext, AutoUndo
import Utils.Maya.AnimLayers as AnimLayerUtils

from QtCustomWidgets.QtUtils import BlockSignals
import QtCustomWidgets.QtUtils as QtUtils

import ProjectPath
import Exporter
import P4.Tools as P4Tools
import Utils.Maya.MayaFBX as MayaFBX

from functools import partial
import sys, traceback, time, math, os, collections

class UIConfigurationOptions():
    SHOW_ANIM_LAYERS                    = "EXPORT_UI_SHOW_ANIM_LAYERS"
    SET_ANIMPRESET_RANGE                = "EXPORT_UI_SET_ANIMPRESET_RANGE"
    SET_ANIMPRESET_FRAME                = "EXPORT_UI_SET_ANIMPRESET_FRAME"
    SET_ANIMPRESET_LAYERS               = "EXPORT_UI_SET_ANIMPRESET_LAYERS"
    SET_ANIMPRESET_SELECT_LAST_LAYER    = "EXPORT_UI_SET_ANIMPRESET_SELECT_LAST_LAYER"


class LayerButtonEventFilter(QtCore.QObject):

    def __init__(self, animationTab):
        QtCore.QObject.__init__(self)

        self.animationTab = animationTab

        self.selectingButton = None

    def mouseButtonPressed(self, source, event):
        if source.isEnabled() and event.buttons() == QtCore.Qt.LeftButton and event.modifiers() == QtCore.Qt.ShiftModifier:
            self.selectingButton = source
            source.setChecked(not source.isChecked())
            return True

        return False

    def mouseMoved(self, source, event):
        if self.selectingButton != None:
            mousePos = self.animationTab.ui.Tbl_AnimList.mapFromGlobal(event.globalPos())
            hoveredItem = self.animationTab.ui.Tbl_AnimList.itemAt(0, mousePos.y())
            if hoveredItem is None:
                return False
                
            column = 1
            if self.animationTab.ui.Tbl_AnimList.columnCount() > 2:
                startX = self.animationTab.ui.Tbl_AnimList.cellWidget(0, 1).pos().x()
                columnWidth = self.animationTab.ui.Tbl_AnimList.cellWidget(0, 2).pos().x() - startX
                column += int((mousePos.x() - startX) / columnWidth)

            hoveredButton = self.animationTab.ui.Tbl_AnimList.cellWidget(hoveredItem.row(), column)
            if hoveredButton is None:
                return False
            
            hoveredButton.setChecked(self.selectingButton.isChecked())

            return True

        return False

    def mouseButtonReleased(self, source, event):
        if self.selectingButton != None:
            self.selectingButton = None
            return True

        return False

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            return self.mouseButtonPressed(source, event)

        if event.type() == QtCore.QEvent.MouseMove:
            return self.mouseMoved(source, event)

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            return self.mouseButtonReleased(source, event)

        return False


class CameraSetDialog(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        
        self._signalsBlocked = False
        
        self.cameraSet = None
        
        uiFilePath = r"ExporterWindow/ui/CameraBrowser.ui"
        self.ui = QtUiTools.QUiLoader().load(os.path.join(ProjectPath.getToolsFolder(), uiFilePath), parent)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.ui)
        
        self.setWindowTitle("CameraSet")
        
        tableHeader = self.ui.Tbl_SceneCameras.horizontalHeader()
        tableHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        tableHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        tableHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        tableHeader.setMinimumSectionSize(1)
        tableHeader.resizeSection(1, 36)
        tableHeader.resizeSection(2, 36)
        
        palette = self.ui.Tbl_SceneCameras.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor.fromHsv(0, 0, 32))
        self.ui.Tbl_SceneCameras.setPalette(palette)
        
        self.ui.BBx_Buttons.accepted.connect(self.accept)
        self.ui.BBx_Buttons.rejected.connect(self.reject)
        
        self.ui.Tbl_SceneCameras.itemChanged.connect(self.onTableItemChecked)
        self.ui.Led_CameraSetPath.editingFinished.connect(self.onPathChanged)
        self.ui.Btn_BrowsePath.clicked.connect(self.browsePath)
        
        self.accepted.connect(self.applyChangesToCameraSet)
    
    def createCameraSet(self):
        cameraSets = ActorManager.getCameraSets()
        cameraSetNames = [cameraSet.name for cameraSet in cameraSets]
        newCameraSetName = "CameraSet"
        idx = 0
        while newCameraSetName in cameraSetNames:
            idx += 1
            newCameraSetName = "CameraSet{}".format(idx)
        
        actors = ActorManager.getActors()
        actor = actors[0] if actors else None
        
        selectedCameras = cmds.ls(selection=True, type="camera")
        
        self.cameraSet = CameraSet.CameraSet().create()
        self.cameraSet.name = newCameraSetName
        self.cameraSet.path = ""
        self.cameraSet.actor = actor
        self.cameraSet.cameras = selectedCameras
        
        result = self.exec_()
        
        if not result:
            self.cameraSet.delete()
            self.cameraSet = None
        
        return self.cameraSet
    
    def editCameraSet(self, cameraSet):        
        self.cameraSet = cameraSet
        self.exec_()
    
    def getSelectedName(self):
        return self.ui.Led_CameraSetName.text()
    
    def getSelectedPath(self):
        pathTokenizer = self.cameraSet.getPathTokenizer()
        return pathTokenizer.Tokenize(self.ui.Led_CameraSetPath.text())
    
    def getSelectedActor(self):
        return ActorManager.getActorByNameSpace(self.ui.Cb_CameraSetActor.currentText())
    
    def getCheckedCameras(self):
        cameras = []
        for i in range(self.ui.Tbl_SceneCameras.rowCount()):
            item = self.ui.Tbl_SceneCameras.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                cameras.append(item.text())
        return cameras
    
    def getCameraLeft(self):
        for i in range(self.ui.Tbl_SceneCameras.rowCount()):
            leftItem = self.ui.Tbl_SceneCameras.item(i, 1)
            if leftItem.checkState() == QtCore.Qt.Checked:
                cameraItem = self.ui.Tbl_SceneCameras.item(i, 0)
                return cameraItem.text()
        return None
    
    def getCameraRight(self):
        for i in range(self.ui.Tbl_SceneCameras.rowCount()):
            rightItem = self.ui.Tbl_SceneCameras.item(i, 2)
            if rightItem.checkState() == QtCore.Qt.Checked:
                cameraItem = self.ui.Tbl_SceneCameras.item(i, 0)
                return cameraItem.text()
        return None
    
    def applyChangesToCameraSet(self):
        self.cameraSet.name = self.getSelectedName()
        self.cameraSet.path = self.getSelectedPath()
        self.cameraSet.actor = self.getSelectedActor()
        self.cameraSet.cameras = self.getCheckedCameras()
        self.cameraSet.cameraLeft = self.getCameraLeft()
        self.cameraSet.cameraRight = self.getCameraRight()
    
    def browsePath(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, caption="Camera Set Path", dir=self.ui.Led_CameraSetPath.text())
        if folder:
            self.ui.Led_CameraSetPath.setText(folder)
            self.onPathChanged()
    
    def onTableItemChecked(self, item):
        if self._signalsBlocked:
            return
        
        if item.column() == 0:
            if item.checkState() == QtCore.Qt.Unchecked:
                with BlockSignals(self):
                    self.ui.Tbl_SceneCameras.item(item.row(), 1).setCheckState(QtCore.Qt.Unchecked)
                    self.ui.Tbl_SceneCameras.item(item.row(), 2).setCheckState(QtCore.Qt.Unchecked)
            else:
                if item.text() == "CameraLeft":
                    self.ui.Tbl_SceneCameras.item(item.row(), 1).setCheckState(QtCore.Qt.Checked)
                elif item.text() == "CameraRight":
                    self.ui.Tbl_SceneCameras.item(item.row(), 2).setCheckState(QtCore.Qt.Checked)
        else:
            if item.checkState() == QtCore.Qt.Checked:
                with BlockSignals(self):
                    cameraItem = self.ui.Tbl_SceneCameras.item(item.row(), 0)
                    if cameraItem.checkState() == QtCore.Qt.Unchecked:
                        cameraItem.setCheckState(QtCore.Qt.Checked)
                    
                    for i in range(self.ui.Tbl_SceneCameras.rowCount()):
                        if i != item.row():
                            self.ui.Tbl_SceneCameras.item(i, item.column()).setCheckState(QtCore.Qt.Unchecked)

    def onPathChanged(self):
        self.ui.Led_CameraSetPath.setToolTip(self.getSelectedPath())
    
    def refresh(self):
        pathTokenizer = self.cameraSet.getPathTokenizer()
        self.ui.Led_CameraSetName.setText(self.cameraSet.name)
        self.ui.Led_CameraSetPath.setText(pathTokenizer.Translate(self.cameraSet.path))
        self.ui.Led_CameraSetPath.setToolTip(self.cameraSet.path)
        self.fillActorList()
        self.fillCameraList()
    
    def fillActorList(self):
        actors = ActorManager.getActors()
        cameraSetActor = self.cameraSet.actor
        self.ui.Cb_CameraSetActor.clear()
        for actor in actors:
            self.ui.Cb_CameraSetActor.addItem(actor.getDisplayName())
            if actor == cameraSetActor:
                self.ui.Cb_CameraSetActor.setCurrentIndex(self.ui.Cb_CameraSetActor.count() - 1)
    
    def fillCameraList(self):
        cameras = cmds.ls(type="camera")
        cameras = [cmds.listRelatives(camera, parent=True)[0] for camera in cameras]
        cameraSetCameras = self.cameraSet.cameras
        cameraLeft = self.cameraSet.cameraLeft
        cameraRight = self.cameraSet.cameraRight
        
        with BlockSignals(self):
            self.ui.Tbl_SceneCameras.setRowCount(len(cameras))
            for row, camera in enumerate(cameras):
                cameraItem = QtWidgets.QTableWidgetItem(camera)
                cameraItem.setCheckState(QtCore.Qt.Checked if camera in cameraSetCameras else QtCore.Qt.Unchecked)
                self.ui.Tbl_SceneCameras.setItem(row, 0, cameraItem)
                
                leftItem = QtWidgets.QTableWidgetItem()
                leftItem.setCheckState(QtCore.Qt.Checked if camera == cameraLeft else QtCore.Qt.Unchecked)
                self.ui.Tbl_SceneCameras.setItem(row, 1, leftItem)
                
                rightItem = QtWidgets.QTableWidgetItem()
                rightItem.setCheckState(QtCore.Qt.Checked if camera == cameraRight else QtCore.Qt.Unchecked)
                self.ui.Tbl_SceneCameras.setItem(row, 2, rightItem)
            
    def accept(self):
        newCameraSetName = self.getSelectedName()
        
        if not newCameraSetName:
            QtWidgets.QMessageBox.warning(self, "CameraSet", "You must specify a name for the CameraSet!")
            return
        
        cameraSets = ActorManager.getCameraSets()
        for cameraSet in cameraSets:
            if cameraSet != self.cameraSet and cameraSet.name == newCameraSetName:
                QtWidgets.QMessageBox.warning(self, "CameraSet", "The name [{}] is already in use by another CameraSet!".format(newCameraSetName))
                return
        
        # All data validated correctly
        QtWidgets.QDialog.accept(self)
    
    def showEvent(self, event):
        if not self.cameraSet:
            QtWidgets.QMessageBox.warning(self, "CameraSet", "No CameraSet assigned to the dialog!")
            QtCore.QTimer.singleShot(0, self.reject)
        else:
            self.refresh()


class AnimWidgetSortState(object):

    _forwardIcon = u"▼"
    _backwardIcon = u"▲"

    def __init__(self, animationTab, sortWidget):
        self.animationTab = animationTab
        self.sortWidget = sortWidget
        
        self.reversed = False
    
    def sortList(self, list):
        if self.isGrouped():
            groups = {}
            for item in list:
                group = self.groupCriteria(item)
                if group not in groups:
                    groups[group] = []
                groups[group].append(item)
            sortedKeys = sorted(groups.keys(), reverse=self.reversed, key=self.sortCriteria)
            sortedGroups = collections.OrderedDict()
            for key in sortedKeys:
                sortedGroups[key] = groups[key]
            if len(groups) == 1:
                key = next(iter(groups.keys()))
                if key == None or key == "" or key == "None":
                    return groups[key]
            return sortedGroups
        else:
            list.sort(reverse=self.reversed, key=self.sortCriteria)
            return list
    
    def updateIcon(self, clear=False):
        text = self.sortWidget.text()
        if text.endswith(self._forwardIcon) or text.endswith(self._backwardIcon):
            text = text[:-1]
        if not clear:
            if self.reversed:
                text += self._backwardIcon
            else:
                text += self._forwardIcon
        self.sortWidget.setText(text)

    # Delegated Methods
    
    def sortCriteria(self, item):
        return item
    
    def isGrouped(self):
        return False
    
    def groupCriteria(self, item):
        return item
    
    def canBeReordered(self, elements):
        return False, None
    
    def canElementsBeReordered(self, elements, target):
        return True
    
    def onReorder(self, elements, target):
        return True
    
    def showGroupContextMenu(self, group, parent, event):
        pass


class BasicSortState(AnimWidgetSortState):
    
    def __init__(self, animationTab, sortWidget, sortFunction):
        super().__init__(animationTab, sortWidget)
        
        self.sortFunction = sortFunction
    
    def sortCriteria(self, item):
        return self.sortFunction(item)


class BasicGroupState(AnimWidgetSortState):
    
    def __init__(self, animationTab, sortWidget, groupFunction):
        super().__init__(animationTab, sortWidget)
        
        self.groupFunction = groupFunction
    
    def isGrouped(self):
        return True
    
    def groupCriteria(self, item):
        return self.groupFunction(item)


class GroupByCategory(AnimWidgetSortState):
    
    def sortCriteria(self, item):
        return "zzzzzzzzz" if not item or item == "None" else item
    
    def isGrouped(self):
        return True
    
    def groupCriteria(self, item):
        return item.animPreset.category or "None"
    
    def canBeReordered(self, elements):
        # NOTE: We wouldn't usually allow to reorder animations from different actors.
        # However we still could want to do this if we want to change thir category BUT not reorder them.
        # For this reason, we will allow the user to begin reordering but block it if necessary on "canElementsBeReordered".
        return True, None
    
    def canElementsBeReordered(self, elements, target):
        targetCategory = target.category
        for element in elements:
            if element.category != targetCategory:
                return True
        
        targetHolder = target.getHolder()  
        for element in elements:
            if element.getHolder() != targetHolder:
                return False
        
        return True
    
    def onReorder(self, elements, target):
        category = target.category                
        for element in elements:
            if element.category != category:
                element.category = category
        
        targetHolder = target.getHolder()  
        for element in elements:
            if element.getHolder() != targetHolder:
                return False
        return True
                
    def showGroupContextMenu(self, group, parent, event):
        if group and group != "None":
            contextMenuOptions = []
            contextMenuOptions.append(QtUtils.MenuOption('renameCategory', 'Rename Category', False, partial(self.onRenameCategoryOptionSelected, group)))
            contextMenuOptions.append(None)
            contextMenuOptions.append(QtUtils.MenuOption('clearCategory', 'Clear Category', False, partial(self.onClearCategoryOptionSelected, group)))
            QtUtils.showContextMenu(contextMenuOptions, parent, event.globalPos())
    
    def onRenameCategoryOptionSelected(self, category):
        newCategory, result = self.animationTab.selectCategory(category)
        if result and newCategory != category:
            with UndoContext("Rename AnimPreset Category"):
                animPresets = AnimPreset.AnimPreset.getInstances()
                for animPreset in animPresets:
                    if animPreset.category == category:
                        animPreset.category = newCategory
            
            self.animationTab.refreshAnimWidgetsList(keepSelection=True)
    
    def onClearCategoryOptionSelected(self, category):
        result = QtWidgets.QMessageBox.question(self.animationTab, "Clear Category", "This will clear the category from all the Animations currently categorized as [{}]. Proceed?".format(category))
        if result == QtWidgets.QMessageBox.Yes:
            with UndoContext("Clear AnimPreset Category"):
                animPresets = AnimPreset.AnimPreset.getInstances()
                for animPreset in animPresets:
                    if animPreset.category == category:
                        animPreset.category = ""
            self.animationTab.refreshAnimWidgetsList(keepSelection=True)


class GroupByActor(AnimWidgetSortState):
    
    def isGrouped(self):
        return True
    
    def groupCriteria(self, item):
        return item.animPreset.getHolder().getDisplayName()
    
    def canBeReordered(self, elements):
        return True, None
    
    def onReorder(self, elements, target):
        holder = target.getHolder()
        for element in elements:
            if element.getHolder() != holder:
                element.changeHolder(holder)
        return True
    
    def showGroupContextMenu(self, group, parent, event):
        if group and group != "None":
            isActor = ActorManager.getActorByNameSpace(group) != None
            isCameraSet = ActorManager.getCameraSetByName(group) != None
            
            contextMenuOptions = []
            if isActor: contextMenuOptions.append(QtUtils.MenuOption('renameActor', 'Rename Actor', False, partial(self.onRenameActorOptionSelected, group)))
            if isCameraSet: contextMenuOptions.append(QtUtils.MenuOption('editCameraSet', 'Edit Camera Set', False, partial(self.onEditCameraSetOptionSelected, group)))
            QtUtils.showContextMenu(contextMenuOptions, parent, event.globalPos())
    
    def onRenameActorOptionSelected(self, actorName):
        newName, result = self.animationTab.selectActorName(actorName)
        if result and newName != actorName:
            with UndoContext("Rename Actor"):
                cmds.namespace(rename=(actorName, newName), parent=":")
        
            self.animationTab.refreshAnimWidgetsList(keepSelection=True)
            
    def onEditCameraSetOptionSelected(self, cameraSetName):
        cameraSet = ActorManager.getCameraSetByName(cameraSetName)
        self.animationTab.showEditCameraSetDialog(cameraSet)
        self.animationTab.refreshAnimWidgetsList(keepSelection=True)


class AnimationTab(ExporterWindowTab.ExporterWindowTab):

    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------

    def __init__(self, exporterWindow):
        ExporterWindowTab.ExporterWindowTab.__init__(self, r"ExporterWindow/ui/AnimationTab.ui", exporterWindow)
        
        # Creates the Sort States
        self._byAnimPresetIndexSortState = BasicSortState(self, None, lambda a : a.animPreset.getHolder().getAnimPresets().index(a.animPreset)) # Used to un-sort the anim presets. Not used on the UI.
        self._byCategorySortState = GroupByCategory(self, None) # Default sort state
        self._byActorSortState = GroupByActor(self, self.ui.Btn_SortActor)
        self._byNameSortState = BasicSortState(self, self.ui.Btn_SortAnimation, lambda a : a.animPreset.getConcatenatedName())
        self._byPathSortState = BasicGroupState(self, self.ui.Btn_SortPath, lambda a : a.animPreset.getPathTokenizer().Translate(a.animPreset.path))
        self._byStartSortState = BasicSortState(self, self.ui.Btn_SortStart, lambda a : a.animPreset.start)
        self._byEndSortState = BasicSortState(self, self.ui.Btn_SortEnd, lambda a : a.animPreset.end)
        self._byLoopSortState = BasicGroupState(self, self.ui.Btn_SortLoop, lambda a : a.animPreset.loop)
        self._byMirrorSortState = BasicGroupState(self, self.ui.Btn_SortMirror, lambda a : a.animPreset.mirror)
        self._byPoseSortState = BasicGroupState(self, self.ui.Btn_SortPose, lambda a : a.animPreset.pose)

        # Properties
        self.lastClickedAnimWidget = None
        self.animWidgetSortState = self._byCategorySortState

        # Signals
        self.ui.Btn_AddAnim.clicked.connect(self.onAddAnimButtonClicked)
        self.ui.Btn_ExportAnims.clicked.connect(self.onExportButtonClicked)
        self.ui.Ckb_ToggleActiveAnims.toggled.connect(self.onToggleActiveAnimsStateChanged)

        self.ui.Btn_GetAnimLayers.clicked.connect(self.onGetAnimLayersButtonClicked)
        self.ui.Btn_SetAnimLayers.clicked.connect(self.onSetAnimLayersButtonClicked)
        self.ui.Btn_ShowLayers.toggled.connect(self.showLayerPanel)
        self.ui.Btn_EditLayers.toggled.connect(self.refreshLayerPanel)
        self.ui.Tbl_AnimList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.Tbl_AnimList.itemDoubleClicked.connect(self.onLayerPanelItemDoubleClicked)
        self.ui.Tbl_AnimList.customContextMenuRequested.connect(self.onLayerPanelContextMenuRequested)

        self.ui.Scr_AnimScrollArea.verticalScrollBar().rangeChanged.connect(self.onAnimPresetScrollAreaResize)
        self.ui.splitter_2.splitterMoved.connect(self.resizeLayerPanel)
        self.ui.Ckb_SetRange.toggled.connect(self.onSetRangeToggled)
        self.ui.Ckb_SetLayers.toggled.connect(self.onSetLayersToggled)

        self.ui.Cbx_RulesMode.insertItems(0, [mode.getName() for mode in self.getCinematicGuidesModes()])
        self.ui.Ckb_ShowRules.toggled.connect(self.setCinematicGuidesEnabled)
        self.ui.Cbx_RulesMode.currentIndexChanged.connect(self.setCinematicGuidesModeIndex)
        
        self.ui.Btn_SortActor.clicked.connect(partial(self.setAnimWidgetSortState, self._byActorSortState))
        self.ui.Btn_SortAnimation.clicked.connect(partial(self.setAnimWidgetSortState, self._byNameSortState))
        self.ui.Btn_SortPath.clicked.connect(partial(self.setAnimWidgetSortState, self._byPathSortState))
        self.ui.Btn_SortStart.clicked.connect(partial(self.setAnimWidgetSortState, self._byStartSortState))
        self.ui.Btn_SortEnd.clicked.connect(partial(self.setAnimWidgetSortState, self._byEndSortState))
        self.ui.Btn_SortLoop.clicked.connect(partial(self.setAnimWidgetSortState, self._byLoopSortState))
        self.ui.Btn_SortMirror.clicked.connect(partial(self.setAnimWidgetSortState, self._byMirrorSortState))
        self.ui.Btn_SortPose.clicked.connect(partial(self.setAnimWidgetSortState, self._byPoseSortState))

        # Event filter
        self.ui.Scr_AnimScrollArea.setAcceptDrops(True)
        self.ui.Scr_AnimScrollArea.installEventFilter(self)
        self.layerbuttonEventFilter = LayerButtonEventFilter(self)

    # ------------------------------------
    # | Tab Methods                      |
    # ------------------------------------
    # Note: Override methods required by the exporter window.

    def isRelevant(self):
        actors = ActorManager.getActors() + ActorManager.getCameraSets()
        if len(actors) == 0:
            return False
        for actor in actors:
            if len(actor.getAnimPresets()) > 0:
                return True
        return False

    def refreshTab(self):
        self.refreshAnimWidgetsList()
        self.refreshCinematicGuides()

    def getTabName(self):
        return "Animation"

    def onExportRootChanged(self, exportRoot):
        animWidgets = self.getAnimWidgets()
        for animWidget in animWidgets:
            animWidget.setPath(animWidget.animPreset.path, updateAnimPreset=False)  # By doing this both the path field and it's tooltip will be refreshed to reflect the new export root

    def loadUIConfiguration(self):
        if cmds.optionVar(exists=UIConfigurationOptions.SHOW_ANIM_LAYERS):
            self.ui.Btn_ShowLayers.setChecked(cmds.optionVar(q=UIConfigurationOptions.SHOW_ANIM_LAYERS))

        if cmds.optionVar(exists=UIConfigurationOptions.SET_ANIMPRESET_RANGE):
            self.ui.Ckb_SetRange.setChecked(cmds.optionVar(q=UIConfigurationOptions.SET_ANIMPRESET_RANGE))

        if cmds.optionVar(exists=UIConfigurationOptions.SET_ANIMPRESET_FRAME):
            self.ui.Cbx_GoTo.setCurrentText(cmds.optionVar(q=UIConfigurationOptions.SET_ANIMPRESET_FRAME))

        if cmds.optionVar(exists=UIConfigurationOptions.SET_ANIMPRESET_LAYERS):
            self.ui.Ckb_SetLayers.setChecked(cmds.optionVar(q=UIConfigurationOptions.SET_ANIMPRESET_LAYERS))

        if cmds.optionVar(exists=UIConfigurationOptions.SET_ANIMPRESET_SELECT_LAST_LAYER):
            self.ui.Ckb_AutoSelectLastLayer.setChecked(cmds.optionVar(q=UIConfigurationOptions.SET_ANIMPRESET_SELECT_LAST_LAYER))

    def saveUIConfiguration(self):
        cmds.optionVar(iv=(UIConfigurationOptions.SHOW_ANIM_LAYERS, self.ui.Btn_ShowLayers.isChecked()))
        cmds.optionVar(iv=(UIConfigurationOptions.SET_ANIMPRESET_RANGE, self.ui.Ckb_SetRange.isChecked()))
        cmds.optionVar(sv=(UIConfigurationOptions.SET_ANIMPRESET_FRAME, self.ui.Cbx_GoTo.currentText()))
        cmds.optionVar(iv=(UIConfigurationOptions.SET_ANIMPRESET_LAYERS, self.ui.Ckb_SetLayers.isChecked()))
        cmds.optionVar(iv=(UIConfigurationOptions.SET_ANIMPRESET_SELECT_LAST_LAYER, self.ui.Ckb_AutoSelectLastLayer.isChecked()))

    def resizeEvent(self, event):
        self.resizeLayerPanel()

    def onUndo(self):
        self.refreshAnimWidgetsList(keepSelection=True)

    # ------------------------------------
    # | Options                          |
    # ------------------------------------

    def isSetRangeOptionEnabled(self):
        return self.ui.Ckb_SetRange.isChecked()
    
    def getGoToOption(self):
        return self.ui.Cbx_GoTo.currentText()

    def isSetLayersOptionEnabled(self):
        return self.ui.Ckb_SetLayers.isChecked()

    def isSelectLastLayerOptionEnabled(self):
        return self.ui.Ckb_AutoSelectLastLayer.isChecked()

    def onSetRangeToggled(self, value):
        self.ui.Cbx_GoTo.setEnabled(value)
        
    def onSetLayersToggled(self, value):
        self.ui.Ckb_AutoSelectLastLayer.setEnabled(value)
        
    # ------------------------------------
    # | Methods                          |
    # ------------------------------------

    def getClosestAnimWidgetToPoint(self, point, margin=5):
        animWidgets = self.getAnimWidgets()
        for animWidget in animWidgets:
            pos = self.ui.Scr_AnimScrollArea.mapFromGlobal(animWidget.mapToGlobal(QtCore.QPoint(0, 0)))
            if pos.y() - margin > point.y():
                return animWidget
        if len(animWidgets) > 0:
            return animWidgets[-1]
        else:
            return None
        
    def applyAnimationConfiguration(self, animWidgets, animRange=None, goTo=None, animLayers=None, selectLastLayer=None):
        if animWidgets:
            with UndoContext("Apply AnimPreset Configuration"):
                animWidgets[0].applyAnimationConfiguration(animRange=animRange, goTo="none", animLayers=animLayers, selectLastLayer=False, combine=False)
                for i in range(1, len(animWidgets) - 1):
                    animWidgets[i].applyAnimationConfiguration(animRange=animRange, goTo="none", animLayers=animLayers, selectLastLayer=False, combine=True)
                animWidgets[-1].applyAnimationConfiguration(animRange=animRange, goTo=goTo, animLayers=animLayers, selectLastLayer=selectLastLayer, combine=True)

    def selectCategory(self, initialCategory=None):
        animPresets = AnimPreset.AnimPreset.getInstances()
        categories = []
        for animPreset in animPresets:
            category = animPreset.category
            if category and category not in categories:
                categories.append(category)
        categories.sort()
        
        initialCategoryIndex = categories.index(initialCategory) if initialCategory else 0
        
        return QtWidgets.QInputDialog.getItem(self, "Set AnimPreset Category", "Category:", categories, current=initialCategoryIndex, editable=True)
    
    def selectActorName(self, initialActorName=None):
        newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor", "Enter new actor name:", text=initialActorName)
        
        while True:
            if not ok or not newName or newName == initialActorName:
                return None, False
            elif ActorManager.isActorNameInUse(newName):
                newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor", "The actor name [{}] is already in use.\nPlease enter a new one.".format(newName), text=newName)
            elif ActorManager.isNamespaceInUse(newName):
                newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor", "There is already a namespace with the name [{}].\nPlease enter a new actor name that doesn't correspond to an existing namespace.".format(newName), text=newName)
            else:
                break
        
        return newName, ok
    
    # ------------------------------------
    # | Layer Panel                      |
    # ------------------------------------

    def isLayerPanelVisible(self):
        return self.ui.Btn_ShowLayers.isChecked()

    def isLayerEditModeEnabled(self):
        return self.ui.Btn_EditLayers.isChecked()

    def showLayerPanel(self, visible):
        self.ui.Frm_LayerEditor.setVisible(visible)
        self.ui.splitter_2.refresh()    # The widget dimensions won't update by this point unless we force the splitter to refresh.
        self.refreshLayerPanel()

    def refreshLayerPanel(self):
        if self.isLayerPanelVisible():
            self.ui.Tbl_AnimList.setRowCount(0)
            self.ui.Tbl_AnimList.setColumnCount(1)

            selectedAnimWidgets = self.getSelectedAnimWidgets()
            if len(selectedAnimWidgets) != 0:
                # TODO: Si cada actor tiene sus propias layers, necesitaríamos una manera de mostrarlo visualmetne en la lista. Por ahora solo mostramos las del primer actor.
                animLayers = selectedAnimWidgets[0].animPreset.getHolder().getAnimLayers(includeBaseLayer=True)
                animLayers.reverse()

                for animLayerIndex, animLayer in enumerate(animLayers):
                    item = QtWidgets.QTableWidgetItem(animLayer)
                    
                    font = QtGui.QFont()
                    font.setUnderline(AnimLayerUtils.isOverrideLayer(animLayer))
                    item.setFont(font)
                    
                    self.ui.Tbl_AnimList.insertRow(animLayerIndex)
                    self.ui.Tbl_AnimList.setItem(animLayerIndex, 0, item)

                for i, animWidget in enumerate(selectedAnimWidgets):
                    hue = 0 if i == 0 else int(255.0 * float(i) / (len(selectedAnimWidgets) - 1))
                    animWidgetLayerColor = QtGui.QColor.fromHsv(hue, 255, 255)
                    animWidget.setLayerColor(animWidgetLayerColor)

                    self.ui.Tbl_AnimList.insertColumn(i + 1)
                    for animLayerIndex, animLayer in enumerate(animLayers):
                        layerButton = self.createLayerPanelButton(animWidgetLayerColor, animWidget, animLayer)
                        self.ui.Tbl_AnimList.setCellWidget(animLayerIndex, i + 1, layerButton)

                self.resizeLayerPanel()

        animWidgets = self.getAnimWidgets()
        for animWidget in animWidgets:
            if not (animWidget.isSelected() and self.isLayerPanelVisible()):
                animWidget.clearLayerColor()
    
    def resizeLayerPanel(self):
        if self.isLayerPanelVisible() and self.ui.Tbl_AnimList.columnCount() > 1:
            self.ui.Tbl_AnimList.resizeColumnToContents(0)
            self.ui.Tbl_AnimList.setColumnWidth(0,  self.ui.Tbl_AnimList.columnWidth(0) + 5)
            columnWidth = self.ui.Tbl_AnimList.width() - self.ui.Tbl_AnimList.columnWidth(0) - 5
            if self.ui.Tbl_AnimList.verticalScrollBar().maximum() != 0:
                columnWidth -= 12
            columnWidth /= self.ui.Tbl_AnimList.columnCount() - 1
            for i in range(1, self.ui.Tbl_AnimList.columnCount()):
                self.ui.Tbl_AnimList.setColumnWidth(i, columnWidth)

    def refreshButtonText(self, layerButton, animWidget, animLayer, state):
        if not state:
            layerButton.setText("")
        else:
            weightedLayer = animWidget.animPreset.getWeightedLayerByAnimLayer(animLayer)
            if weightedLayer and AnimPreset.AnimPreset.shouldUseAnimLayerWeight(animLayer):
                layerButton.setText('{0:.3f}'.format(weightedLayer.weight))
    
    def createLayerPanelButton(self, color, animWidget, animLayer):
        layerButton = QtWidgets.QToolButton()
        
        animPresetLayers = animWidget.animPreset.getAnimLayers()
        isRootLayer = AnimLayerUtils.isBaseLayer(animLayer)
        isOverrideLayer = AnimLayerUtils.isOverrideLayer(animLayer)
        isEnabled = not isRootLayer and (animLayer in animPresetLayers)
        
        layerButton.setCheckable(not isRootLayer)
        layerButton.setChecked(isEnabled)
        layerButton.setEnabled(self.isLayerEditModeEnabled())
        layerButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        layerButton.setAutoFillBackground(True)
        layerButton.setAutoRaise(True)
        layerButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        layerButton.setMinimumWidth(self.ui.Tbl_AnimList.horizontalHeader().minimumSectionSize())
        
        self.refreshButtonText(layerButton, animWidget, animLayer, isEnabled)
        
        borderWidth = 3 if isOverrideLayer else 1
        borderStyle = "dashed" if isOverrideLayer else "solid"
        borderColor = QtGui.QColor.fromHsv(0, 0, 32, 255)
        textColor = QtGui.QColor.fromHsv(0, 0, 32, 255)
        checkedColor = color if not isRootLayer else QtGui.QColor.fromHsv(color.hue(),  0.75 * color.saturation(), 0.75 * color.value(), 255)
        uncheckedColor = checkedColor if isRootLayer else QtGui.QColor.fromHsv(color.hue(), color.saturation(), 0.8 * color.value(), 32)
        hoverCheckedColor = checkedColor if isRootLayer else QtGui.QColor.fromHsv(color.hue(), 0.4 * color.saturation(), color.value(), 255)
        hoverUncheckedColor = checkedColor if isRootLayer else QtGui.QColor.fromHsv(color.hue(), 0.6 * color.saturation(), color.value(), 128)
        disabledCheckedColor = QtGui.QColor.fromHsv(color.hue(), color.saturation(), 0.5 * color.value(), 255)
        disabledUncheckedColor = disabledCheckedColor if isRootLayer else QtGui.QColor.fromHsv(color.hue(), color.saturation(), 0.5 * color.value(), 32)
        
        textColorString = "rgb({}, {}, {}, {})".format(textColor.red(), textColor.green(), textColor.blue(), textColor.alpha())
        borderColorString = "rgb({}, {}, {}, {})".format(borderColor.red(), borderColor.green(), borderColor.blue(), borderColor.alpha())
        uncheckedColorString = "rgb({}, {}, {}, {})".format(uncheckedColor.red(), uncheckedColor.green(), uncheckedColor.blue(), uncheckedColor.alpha())
        checkedColorString = "rgb({}, {}, {}, {})".format(checkedColor.red(), checkedColor.green(), checkedColor.blue(), checkedColor.alpha())
        hoverUncheckedColorString = "rgb({}, {}, {}, {})".format(hoverCheckedColor.red(), hoverUncheckedColor.green(), hoverUncheckedColor.blue(), hoverUncheckedColor.alpha())
        hoverCheckedColorString = "rgb({}, {}, {}, {})".format(hoverUncheckedColor.red(), hoverCheckedColor.green(), hoverCheckedColor.blue(), hoverCheckedColor.alpha())
        disabledUncheckedColorString = "rgb({}, {}, {}, {})".format(disabledUncheckedColor.red(), disabledUncheckedColor.green(), disabledUncheckedColor.blue(), disabledUncheckedColor.alpha())
        disabledCheckedColorString = "rgb({}, {}, {}, {})".format(disabledCheckedColor.red(), disabledCheckedColor.green(), disabledCheckedColor.blue(), disabledCheckedColor.alpha())
        layerButtonStyleSheet = "QToolButton {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {uncheckedColor}; }}\nQToolButton:checked {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {checkedColor}; }}\nQToolButton:hover:!checked {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {hoverUncheckedColor}; }}\nQToolButton:hover:checked {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {hoverCheckedColor}; }}\nQToolButton:disabled:!checked {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {disabledUncheckedColor}; }}\nQToolButton:disabled:checked {{ color: {textColor}; border: 1px solid {borderColor}; border-bottom: {borderWidth}px {borderStyle} {borderColor}; background-color: {disabledCheckedColor}; }}"
        layerButton.setStyleSheet(layerButtonStyleSheet.format(textColor=textColorString, borderWidth=borderWidth, borderStyle=borderStyle, borderColor=borderColorString, uncheckedColor=uncheckedColorString, checkedColor=checkedColorString, hoverUncheckedColor=hoverUncheckedColorString, hoverCheckedColor=hoverCheckedColorString, disabledUncheckedColor=disabledUncheckedColorString, disabledCheckedColor=disabledCheckedColorString))
        
        if not isRootLayer:
            layerButton.toggled.connect(partial(self.onLayerPanelButtonStateChanged, layerButton, animWidget, animLayer))
            layerButton.customContextMenuRequested.connect(partial(self.onLayerPanelButtonContextMenuRequested, animWidget, animLayer))
            layerButton.installEventFilter(self.layerbuttonEventFilter)
        
        return layerButton

    def selectLayerWeight(self, animWidgets, animLayer):
        weightedLayer = animWidgets[0].animPreset.getWeightedLayerByAnimLayer(animLayer)
        if weightedLayer and AnimPreset.AnimPreset.shouldUseAnimLayerWeight(animLayer):
            animLayerWeight = weightedLayer.weight
        else:
            animLayerWeight = cmds.getAttr("{}.weight".format(animLayer))
        
        weight, result = QtWidgets.QInputDialog.getDouble(self, "Select Layer Weight", animLayer, animLayerWeight, 0, 1, 3, QtCore.Qt.Dialog, 0.1)
        
        if result:
            with UndoContext("Set AnimLayer Weight"):
                if weight != 1 and not AnimPreset.AnimPreset.shouldUseAnimLayerWeight(animLayer):
                    QtWidgets.QMessageBox.information(self, "Set AnimLayer Weight", "You have specified a layer weight for the layer [{}] for the first time. All the weights for this layer on the other animations has been set to 1.".format(animLayer))
                
                for animWidget in animWidgets:
                    animWidget.animPreset.setAnimLayerWeight(animLayer, weight, enableInactive=False)
    
    # ------------------------------------
    # | Cinematic Guides                 |
    # ------------------------------------
    
    def getCinematicGuidesModes(self):
        cinematicGuidesModes = CinematicGuides.CinematicGuides.Modes.getValues()
        cinematicGuidesModes.sort(key=CinematicGuides.GuideMode.getOrder)
        return cinematicGuidesModes
    
    def refreshCinematicGuides(self):
        instance = CinematicGuides.CinematicGuides.instance()
        self.ui.Ckb_ShowRules.setChecked(instance.enabled)
        self.ui.Cbx_RulesMode.setCurrentIndex(self.getCinematicGuidesModes().index(instance.mode))
    
    def setCinematicGuidesEnabled(self, enabled, updateUI=False):
        CinematicGuides.CinematicGuides.instance().enabled = enabled
        if updateUI:
            self.ui.Ckb_ShowRules.setChecked(enabled)

    def setCinematicGuidesMode(self, mode, updateUI=False):
        CinematicGuides.CinematicGuides.instance().mode = mode
        if updateUI:
            self.ui.Cbx_RulesMode.setCurrentIndex(self.getCinematicGuidesModes().index(mode))

    def setCinematicGuidesModeIndex(self, index, updateUI=False):
        CinematicGuides.CinematicGuides.instance().mode = self.getCinematicGuidesModes()[index]
        if updateUI:
            self.ui.Cbx_RulesMode.setCurrentIndex(index)

    # ------------------------------------
    # | Anim Widgets                     |
    # ------------------------------------

    def refreshAnimWidgetsList(self, keepSelection=False):
        # Stores the selected anim presets
        if keepSelection:
            selectedAnimWidgets = self.getSelectedAnimWidgets()
            selectedAnimPresets = [animWidget.animPreset for animWidget in selectedAnimWidgets]
            
        # Stores the collapsed anim widget panels (they are expanded by default)
        collapsededGroupPanels = [panel.group for panel in self.getAnimWidgetPanels() if not panel.isExpanded()]
            
        # Clears the animation list
        animWidgetsLayout = self.ui.Frm_Animation.layout()
        while animWidgetsLayout.count() > 0:
            widgetItem = animWidgetsLayout.takeAt(0)
            widgetItem.widget().deleteLater()

        # Creates the anim widgets with all the anim presets
        actors = ActorManager.getActors()
        actors += ActorManager.getCameraSets()
        animWidgets = []
        newSelectedAnimWidgets = []
        for actor in actors:
            animPresets = actor.getAnimPresets()
            for animPreset in animPresets:
                animWidget = AnimWidget.AnimWidget(animPreset, self)
                animWidgets.append(animWidget)
                if keepSelection and animPreset in selectedAnimPresets:
                    newSelectedAnimWidgets.append(animWidget)
        
        # Sorts the widget list based on the sort state
        animWidgets = self.animWidgetSortState.sortList(animWidgets)

        if type(animWidgets) == collections.OrderedDict:
            # Classify the widgets based on their group
            animWidgetPanels = {}
            for group, groupAnimWidgets in animWidgets.items():
                if group not in animWidgetPanels:
                    animWidgetPanels[group] = AnimWidgetPanel.AnimWidgetPanel(group, self, contextMenuCallback=self.animWidgetSortState.showGroupContextMenu)
                    animWidgetPanels[group].setExpanded(group not in collapsededGroupPanels)
                    animWidgetsLayout.addWidget(animWidgetPanels[group])
                for animWidget in groupAnimWidgets:
                    animWidgetPanels[group].addWidget(animWidget)
        else:
            # Adds the widgets to the layout
            for animWidget in animWidgets:
                animWidgetsLayout.addWidget(animWidget)

        # Hides or shows the anim widget icons
        self.updateAnimWidgetIcons()

        # Reselectes the previously selected anim widgets
        if keepSelection:
            self.selectAnimWidgets(newSelectedAnimWidgets)

    def getAnimWidgetSortState(self):
        return self.animWidgetSortState

    def setAnimWidgetSortState(self, state):
        if state == None:
            state = self._byCategorySortState
        if state != self._byCategorySortState and self.animWidgetSortState == state:
            self.animWidgetSortState.reversed = not self.animWidgetSortState.reversed
            if not self.animWidgetSortState.reversed:
                self.animWidgetSortState.updateIcon(clear=True)
                self.animWidgetSortState = self._byCategorySortState
            else:
                self.animWidgetSortState.updateIcon()
        else:
            if self.animWidgetSortState != self._byCategorySortState:
                self.animWidgetSortState.reversed = False
                self.animWidgetSortState.updateIcon(clear=True)
            self.animWidgetSortState = state
            if state != self._byCategorySortState:
                state.updateIcon()
        
        self.refreshAnimWidgetsList(keepSelection=True)

    def updateAnimWidgetIcons(self):
        widgets = self.getAnimWidgets()
        
        # Icons will be visible if there is a camera animation (even if there are only camera animations)
        showIcon = False
        for widget in widgets:
            if widget.animPreset.getHolder()._Type == CameraSet.CameraSet._Type:
                showIcon = True
                break
        
        for widget in widgets:
            widget.setWidgetIconVisibility(showIcon)

    def getAnimWidgets(self, sort=True):
        animWidgetsLayout = self.ui.Frm_Animation.layout()
        animWidgets = []
        for i in range(animWidgetsLayout.count()):
            widget = animWidgetsLayout.itemAt(i).widget()
            if type(widget) == AnimWidgetPanel.AnimWidgetPanel:
                animWidgets += widget.getAnimWidgets()
            else:
                animWidgets.append(widget)
        if not sort:
            # If the anim presets are sorted but we don't want them that way, we have to sort them by index
            self._byAnimPresetIndexSortState.sortList(animWidgets)
        return animWidgets

    def getAnimWidgetPanels(self):
        animWidgetsLayout = self.ui.Frm_Animation.layout()
        animWidgetPanels = []
        for i in range(animWidgetsLayout.count()):
            widget = animWidgetsLayout.itemAt(i).widget()
            if type(widget) == AnimWidgetPanel.AnimWidgetPanel:
                animWidgetPanels.append(widget)
        return animWidgetPanels
    
    def getAnimWidgetsByHolder(self, holder):
        animWidgets = self.getAnimWidgets()
        return [animWidget for animWidget in animWidgets if animWidget.animPreset.getHolder() == holder]

    def getSelectedAnimWidgets(self):
        animWidgets = self.getAnimWidgets()
        return [animWidget for animWidget in animWidgets if animWidget.isSelected()]

    def getSelectedAnimPresets(self):
        selectedAnimWidgets = self.getSelectedAnimWidgets()
        return [animWidget.animPreset for animWidget in selectedAnimWidgets]
    
    def selectAnimWidgets(self, animWidgetsToSelect, replaceSelection=True):
        animWidgets = self.getAnimWidgets()
        for animWidget in animWidgets:
            if animWidget in animWidgetsToSelect:
                animWidget.setSelected(True)
            elif replaceSelection:
                animWidget.setSelected(False)
        self.refreshLayerPanel()

    def addActorAnimation(self, actor, subActor=None, scrollToNewWidget=True):
        if subActor != None and subActor not in actor.getSubActors():
            raise AssertionError("Attempting to create an AnimPreset with a SubActor that doesn't belong to the provided Actor")

        animWidgets = self.getAnimWidgetsByHolder(actor)
        namePartsCount = 1 if len(animWidgets) == 0 else len(animWidgets[0].animPreset.getNameParts())
        
        with UndoContext("Create AnimPreset"):
            animPreset = actor.createAnimPreset()
            if subActor != None:
                animPreset.subActor = subActor
            animPreset.setNameParts([""] * namePartsCount)
            animPreset.path = ""
            animPreset.start = cmds.playbackOptions(q=True, ast=True)
            animPreset.end = cmds.playbackOptions(q=True, aet=True)
            animPreset.color = [128, 128, 128]
            animPreset.loop = False
            animPreset.mirror = False
            animPreset.pose = False

        self.finishEditingWidgets()
        self.refreshAnimWidgetsList()

        if scrollToNewWidget:
            animWidgets = self.getAnimWidgets()
            for animWidget in animWidgets:
                if animWidget.animPreset == animPreset:
                    self.selectAnimWidgets([animWidget])
                    QtCore.QCoreApplication.processEvents() # The ScrollArea geometry is not build yet, so we process a draw so it is calculated
                    QtCore.QCoreApplication.processEvents() # For some reason, if we don't do this twice, the ScrollArea geometry won't include the new row
                    self.ui.Scr_AnimScrollArea.ensureWidgetVisible(animWidget)
    
    def addCameraSetAnimation(self, cameraSet, scrollToNewWidget=True):
        self.addActorAnimation(cameraSet, scrollToNewWidget=scrollToNewWidget)  # We can reuse this method as is
    
    def showCreateCameraSetDialog(self, addNewAnimation=True):
        dialog = CameraSetDialog(self)
        cameraSet = dialog.createCameraSet()
        if cameraSet and addNewAnimation:
            self.addCameraSetAnimation(cameraSet)   # We create a new anim preset for the camera set, seems intuitive
        return cameraSet
        
    def showEditCameraSetDialog(self, cameraSet):
        dialog = CameraSetDialog(self)
        dialog.editCameraSet(cameraSet)
        
    def deleteAnimWidgets(self, animWidgetsToDelete, ask=True, deleteAnimPreset=True):
        if len(animWidgetsToDelete) > 0:
            message = "Are you sure you want to delete these anim presets?\n"
            for animWidget in animWidgetsToDelete:
                message += "\n{}".format(animWidget.animPreset.getConcatenatedName())

            result = QtWidgets.QMessageBox.question(self.exporterWindow, "Delete Anim Presets", message) if ask else QtWidgets.QMessageBox.Yes
            if result == QtWidgets.QMessageBox.Yes:
                with UndoContext("Delete AnimPreset"):
                    for animWidget in animWidgetsToDelete:
                        animWidget.parent().layout().removeWidget(animWidget)
                        animWidget.deleteLater()
                        if deleteAnimPreset:
                            animWidget.animPreset.delete()

                    self.finishEditingWidgets()
                    self.refreshLayerPanel()

    def duplicateAnimWidgets(self, animWidgetsToDuplicate, keepPosition=False):
        with UndoContext("Duplicate AnimPreset"):
            animPresetsToDuplicateByHolder = {}
            for animWidget in animWidgetsToDuplicate:
                animPreset = animWidget.animPreset
                holder = animPreset.getHolder()
                if holder not in animPresetsToDuplicateByHolder:
                    animPresetsToDuplicateByHolder[holder] = []
                animPresetsToDuplicateByHolder[holder].append(animPreset)
            
            newAnimPresets = []
            for holder, animPresetsToDuplicate in animPresetsToDuplicateByHolder.items():
                animPresets = holder.getAnimPresets()
                lastIndex = 0
                clonedAnimPresets = []
                for i, animPreset in enumerate(animPresets):
                    if animPreset in animPresetsToDuplicate:
                        clonedAnimPreset = animPreset.clone()
                        clonedAnimPresets.append((clonedAnimPreset, i))
                        newAnimPresets.append(clonedAnimPreset)
                        lastIndex = i
                
                for i, clonedAnimPreset in enumerate(clonedAnimPresets):
                    indexToInsert = clonedAnimPreset[1] if keepPosition else lastIndex
                    indexToInsert += i + 1
                    holder.insertAnimPreset(clonedAnimPreset[0], indexToInsert)
            
            self.finishEditingWidgets()
            self.refreshAnimWidgetsList()
            
            animWidgets = self.getAnimWidgets()
            newAnimWidgets = [animWidget for animWidget in animWidgets if animWidget.animPreset in newAnimPresets]
            self.selectAnimWidgets(newAnimWidgets)

    def finishEditingWidgets(self):
        animWidgets = self.getAnimWidgets()
        for animWidget in animWidgets:
            animWidget.setNamePartEditMode(False)
    
    def exportAnimWidgets(self, animWidgets, verbose=True, expandLog=True, exportMirror=True, checkout=True, convert=True, compile=True):
        # Exports the anim widgets
        try:
            self.exporterWindow.startExport(expandLog=(verbose and expandLog))

            if verbose:
                totalExportTime = 0
                self.exporterWindow.writePreformatedTextToLog("Commencing Animation Export ({} files selected):".format(len(animWidgets)), bold=True)
                self.exporterWindow.writeHtmlTextToLog("Export Root: <span style=\"color: #aaddff\">{}</span>".format(self.exporterWindow.getSelectedExportRoot()))

            subHoldersToExport = set()
            for animWidget in animWidgets:
                subHoldersToExport.add(animWidget.animPreset.getSubHolder())
                
            QtCore.QCoreApplication.processEvents()
            if verbose and not self.exporterWindow.isExportCancelled():
                self.exporterWindow.writePreformatedTextToLog("Preparing Actors for Export...")
                
                subHoldersToExportDigitCount = int(math.floor(math.log10(len(subHoldersToExport)))) + 1
                maxSubHolderLength = 0
                for subHolder in subHoldersToExport:
                    maxSubHolderLength = max(len(subHolder.getDisplayName()), maxSubHolderLength)
            
            problematicSubHolders = set()
            subHolderExportData = {}
            for i, subHolder in enumerate(subHoldersToExport):
                if verbose:
                    timeStamp = time.time()
                    self.exporterWindow.writeHtmlTextToLog("Preparing actor for export: <span style=\"color: white\">{}</span> ({}/{})...".format(subHolder.getDisplayName(), str(i+1).zfill(subHoldersToExportDigitCount), len(subHoldersToExport)), newLine=False)
                    QtCore.QCoreApplication.processEvents()
                    
                try:
                    subHolderExportData[subHolder] = subHolder.onPreExport()
                    
                    if verbose:
                        exportTime = time.time() - timeStamp
                        totalExportTime += exportTime
                        self.exporterWindow.writePreformatedTextToLog("{} DONE ({:.2f} s)".format("  " * (maxSubHolderLength - len(subHolder.getDisplayName())), exportTime), color="lightgreen", bold=True)
                    
                except:
                    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                    error = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                    problematicSubHolders.add(subHolder)
                    
                    if verbose:
                        self.exporterWindow.writePreformatedTextToLog("{} ERROR".format("  " * (maxSubHolderLength - len(subHolder.getDisplayName()))), color="#ff9999", bold=True)
                        self.exporterWindow.writePreformatedTextToLog("".join(error), color="yellow")
            
            QtCore.QCoreApplication.processEvents()
            if verbose and not self.exporterWindow.isExportCancelled():
                self.exporterWindow.writePreformatedTextToLog("Exporting Animations...")
                
                # Precomputes some data to format the text accordingly
                digitCount = int(math.floor(math.log10(len(animWidgets)))) + 1
                maxAnimNameLength = 0
                exportPaths = []
                exportNames = []
                for animWidget in animWidgets:
                    tokenizer = animWidget.getPathTokenizer()
                    tokenizer.Update({ ProjectPath.Tokens.TPrjBranch : "" })
                    exportName = animWidget.animPreset.getConcatenatedName()
                    exportPath = tokenizer.Translate(animWidget.animPreset.path)
                    if exportPath[-1] != os.path.sep:
                        exportPath += os.path.sep
                    maxAnimNameLength = max(len(exportPath) + len(exportName), maxAnimNameLength)
                    exportNames.append(exportName)
                    exportPaths.append(exportPath)
            
            pathsToCompile = []
            problematicAnimWidgets = {}
            subHoldersToMirror = set()
            for i, animWidget in enumerate(animWidgets):
                QtCore.QCoreApplication.processEvents()
                if self.exporterWindow.isExportCancelled():
                    break

                if verbose:
                    timeStamp = time.time()
                    animName = exportNames[i].format(left="left", right="right")
                    animPresetColor = animWidget.animPreset.color
                    animPresetColor = QtGui.QColor(animPresetColor[0], animPresetColor[1], animPresetColor[2])
                    self.exporterWindow.writeHtmlTextToLog("[{}/{}] Exporting <span style=\"color: white\">{}</span><b style=\"color: {}\">{}</b>...".format(str(i+1).zfill(digitCount), len(animWidgets), exportPaths[i], animPresetColor.name(), animName), newLine=False)
                    QtCore.QCoreApplication.processEvents()
                    
                subHolder = animWidget.animPreset.getSubHolder()
                if subHolder in problematicSubHolders:
                    error = "Animation not exported, Actor produced errors while preparing for export: {}".format(subHolder.getDisplayName())
                    problematicAnimWidgets[animWidget] = error
                    
                    if verbose:
                        self.exporterWindow.writePreformatedTextToLog("{} SKIPPED".format("  " * (maxAnimNameLength - len(exportPaths[i] + animName))), color="yellow", bold=True)
                        self.exporterWindow.writePreformatedTextToLog(problematicAnimWidgets[animWidget], color="yellow")
                        
                    continue
                
                try:
                    exportedFilePaths = animWidget.animPreset.export(pathTokenizer=animWidget.getPathTokenizer(), exportMirror=False, checkout=checkout, convert=convert, compile=False, prepareSubHolderForExport=False, subHolderExportData=subHolderExportData[subHolder]) # The compiling and subHolder preparation are performed manually to improve performance by batching all the files
                    pathsToCompile += exportedFilePaths

                    if verbose:
                        exportTime = time.time() - timeStamp
                        totalExportTime += exportTime
                        self.exporterWindow.writePreformatedTextToLog("{} DONE ({:.2f} s)".format("  " * (maxAnimNameLength - len(exportPaths[i] + animName)), exportTime), color="lightgreen", bold=True)

                    # The mirroring is manually exported later to improve performance
                    if animWidget.animPreset.mirror:
                        subHoldersToMirror.add(animWidget.animPreset.getSubHolder())
                        
                except:
                    exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                    error = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                    problematicAnimWidgets[animWidget] = error

                    if verbose:
                        self.exporterWindow.writePreformatedTextToLog("{} ERROR".format("  " * (maxAnimNameLength - len(exportPaths[i] + animName))), color="#ff9999", bold=True)
                        self.exporterWindow.writePreformatedTextToLog(error[-1], color="yellow")
            
            if len(subHoldersToMirror) > 0:
                with AutoUndo():
                    QtCore.QCoreApplication.processEvents()
                    if verbose and not self.exporterWindow.isExportCancelled():
                        self.exporterWindow.writePreformatedTextToLog("Exporting Mirror Animations...")
                        
                        actorsToMirrorDigitCount = int(math.floor(math.log10(len(subHoldersToMirror)))) + 1
                        maxSubHolderLength = 0
                        for subHolder in subHoldersToMirror:
                            maxSubHolderLength = max(len(subHolder.getDisplayName()), maxSubHolderLength)
                    
                    subHolderExportDataMirror = {}
                    for i, subHolder in enumerate(subHoldersToMirror):
                        QtCore.QCoreApplication.processEvents()
                        if self.exporterWindow.isExportCancelled():
                            break
                        
                        if verbose:
                            timeStamp = time.time()
                            self.exporterWindow.writeHtmlTextToLog("Mirroring actor: <span style=\"color: white\">{}</span> ({}/{})...".format(subHolder.getDisplayName(), str(i+1).zfill(actorsToMirrorDigitCount), len(subHoldersToMirror)), newLine=False)
                            QtCore.QCoreApplication.processEvents()
                        
                        try:
                            AnimLayerUtils.setEnabledAnimLayers(subHolder.getHolder().getAnimLayers()) # mirrorAnimation will mirror only enabled layers
                            subHolderExportDataMirror[subHolder] = subHolder.mirrorAnimation(subHolderExportData[subHolder])
                            
                            if verbose:
                                exportTime = time.time() - timeStamp
                                totalExportTime += exportTime
                                self.exporterWindow.writePreformatedTextToLog("{} DONE ({:.2f} s)".format("  " * (maxSubHolderLength - len(subHolder.getDisplayName())), exportTime), color="lightgreen", bold=True)
                            
                        except:
                            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                            error = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                            problematicSubHolders.add(subHolder)
                            
                            if verbose:
                                self.exporterWindow.writePreformatedTextToLog("{} ERROR".format("  " * (maxSubHolderLength - len(subHolder.getDisplayName()))), color="#ff9999", bold=True)
                                self.exporterWindow.writePreformatedTextToLog("".join(error), color="yellow")
                        
                    for i, animWidget in enumerate(animWidgets):
                        QtCore.QCoreApplication.processEvents()
                        if self.exporterWindow.isExportCancelled():
                            break
                        
                        if animWidget.animPreset.mirror:
                            mirroredAnimName = exportNames[i].format(left="right", right="left")
                            
                            if verbose:
                                timeStamp = time.time()
                                animPresetColor = animWidget.animPreset.color
                                animPresetColor = QtGui.QColor(animPresetColor[0], animPresetColor[1], animPresetColor[2])
                                self.exporterWindow.writeHtmlTextToLog("[{}/{}] Exporting <u>mirror animation</u> <span style=\"color: white\">{}</span><b style=\"color: {}\">{}</b>...".format(str(i+1).zfill(digitCount), len(animWidgets), exportPaths[i], animPresetColor.name(), mirroredAnimName), newLine=False)
                                QtCore.QCoreApplication.processEvents()
                            
                            subHolder = animWidget.animPreset.getSubHolder()
                            if subHolder in problematicSubHolders:
                                if animWidget not in problematicAnimWidgets:
                                    error = "Mirror animation not exported, Actor produced errors while mirroring: {}".format(subHolder.getDisplayName())
                                    problematicAnimWidgets[animWidget] = error
                                
                                if verbose:
                                    self.exporterWindow.writePreformatedTextToLog("{} SKIPPED".format("  " * (maxAnimNameLength - len(exportPaths[i] + mirroredAnimName))), color="yellow", bold=True)
                                    self.exporterWindow.writePreformatedTextToLog(problematicAnimWidgets[animWidget], color="yellow")
                                    
                                continue
                            
                            try:
                                if "{left}" not in exportNames[i] and "{right}" not in exportNames[i]:
                                    raise AssertionError("AnimPreset marked for mirroring but no side was indicated! Use {left} or {right} to indicate the side.")
                                
                                nameParts = animWidget.animPreset.getNameParts()
                                for j in range(len(nameParts)):
                                    nameParts[j] = nameParts[j].format(left="right", right="left")
                                animWidget.animPreset.setNameParts(nameParts)
                                
                                exportedFilePaths = animWidget.animPreset.export(pathTokenizer=animWidget.getPathTokenizer(), exportMirror=False, checkout=checkout, convert=convert, compile=False, prepareSubHolderForExport=False, subHolderExportData=subHolderExportDataMirror[subHolder]) # The compiling and subHolder preparation are performed manually are performed manually to improve performance by batching all the files
                                pathsToCompile += exportedFilePaths
                                
                                if verbose:
                                    exportTime = time.time() - timeStamp
                                    totalExportTime += exportTime
                                    self.exporterWindow.writePreformatedTextToLog("{} DONE ({:.2f} s)".format("  " * (maxAnimNameLength - len(exportPaths[i] + mirroredAnimName)), exportTime), color="lightgreen", bold=True)
                                    
                            except:
                                exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                                error = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                                problematicAnimWidgets[animWidget] = error
                                
                                if verbose:
                                    self.exporterWindow.writePreformatedTextToLog("{} ERROR".format("  " * (maxAnimNameLength - len(exportPaths[i] + mirroredAnimName))), color="#ff9999", bold=True)
                                    self.exporterWindow.writePreformatedTextToLog(error[-1], color="yellow")
                        
                    QtCore.QCoreApplication.processEvents()
                    if verbose and not self.exporterWindow.isExportCancelled():
                        timeStamp = time.time()
                        self.exporterWindow.writePreformatedTextToLog("Undoing Mirrors...", newLine=False)
                        QtCore.QCoreApplication.processEvents()
                        
                if verbose:
                    exportTime = time.time() - timeStamp
                    totalExportTime += exportTime
                    self.exporterWindow.writePreformatedTextToLog(" DONE ({:.2f} s)".format(exportTime), color="lightgreen", bold=True)
            
            for subHolder, exportData in subHolderExportData.items():
                subHolder.onPostExport(exportData)
            
            if convert and compile and len(pathsToCompile) > 0:
                QtCore.QCoreApplication.processEvents()
                if not self.exporterWindow.isExportCancelled():
                    if verbose:
                        timeStamp = time.time()
                        self.exporterWindow.writePreformatedTextToLog("Compiling animations...", newLine=False)
                        QtCore.QCoreApplication.processEvents() # The compile process won't ask the ui to update, so we force it before compiling
                    
                    try:
                        Exporter.compileAssetFiles(pathsToCompile)

                        if verbose:
                            convertTime = time.time() - timeStamp
                            totalExportTime += convertTime
                            if len(problematicAnimWidgets.keys()) == 0:
                                self.exporterWindow.writePreformatedTextToLog(" DONE ({:.2f} s)".format(convertTime), color="lightgreen", bold=True)
                            else:
                                self.exporterWindow.writePreformatedTextToLog(" PARTIAL ({:.2f} s)".format(convertTime), color="yellow", bold=True)

                    except:
                        exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
                        error = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                        problematicAnimWidgets[animWidget] = error

                        if verbose:
                            self.exporterWindow.writePreformatedTextToLog(" ERROR", color="#ff9999", bold=True)
                            self.exporterWindow.writePreformatedTextToLog(error[-1], color="yellow")
                    
            if verbose:
                if len(problematicAnimWidgets) == 0:
                    if self.exporterWindow.isExportCancelled():
                        self.exporterWindow.writePreformatedTextToLog("Export Cancelled ({:.2f} s)".format(totalExportTime), color="#d080ff", bold=True)
                    else:
                        self.exporterWindow.writePreformatedTextToLog("Export Completed Successfully ({:.2f} s)".format(totalExportTime), color="lightgreen", bold=True)
                else:
                    if self.exporterWindow.isExportCancelled():
                        self.exporterWindow.writePreformatedTextToLog("Export Cancelled with Errors. The following files gave problems:", color="#d080ff", bold=True)
                    else:
                        self.exporterWindow.writePreformatedTextToLog("Export Completed with Errors. The following files gave problems:", color="#ff9999", bold=True)
                    for problematicAnimWidget in problematicAnimWidgets:
                        self.exporterWindow.writePreformatedTextToLog("- {}".format(problematicAnimWidget.animPreset.getConcatenatedName()), color="#ff9999")
                        self.exporterWindow.writePreformatedTextToLog("".join(problematicAnimWidgets[problematicAnimWidget]), color="yellow")
                self.exporterWindow.writePreformatedTextToLog("")

        except:
            if verbose:
                self.exporterWindow.writePreformatedTextToLog("ERROR: An error occurred while exporting animations. Export Aborted, check the console for more details.", color="#ff9999")
                traceback.print_exc()

        finally:
            self.exporterWindow.endExport(contractLog=(verbose and expandLog))

    def exportAsFBX(self, animWidgets):
        animPresets = [animWidget.animPreset for animWidget in animWidgets]
        subHolders = set([animPreset.getSubHolder() for animPreset in animPresets])

        try:
            exportData = {}
            exportNodes = {}
            for subHolder in subHolders:
                exportData[subHolder] = subHolder.onPreExport()
                exportNodes[subHolder] = subHolder.getExportNodes(exportData[subHolder])
            
            try:
                currentAnimRange = (cmds.playbackOptions(q=True, ast=True), cmds.playbackOptions(q=True, aet=True), cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
                animLayers = cmds.ls(type="animLayer")
                currentAnimLayers = [animLayer for animLayer in animLayers if not cmds.animLayer(animLayer, q=True, m=True)]
                
                presetFilePath = os.path.join(ProjectPath.getToolsFolder(), "ExporterWindow", "resources", "fbx_anim_export_preset.fbxexportpreset")
                MayaFBX.ClearFBXSettings()
                MayaFBX.LoadExportPresetFile(presetFilePath)
                
                for animPreset in animPresets:
                    with AutoUndo():
                        animPreset.applyAnimRange()
                        animPreset.applyAnimLayers(selectLastLayer=False)
                        
                        subHolder = animPreset.getSubHolder()
                        cmds.bakeResults(exportNodes[subHolder], t=(animPreset.start, animPreset.end), hi="below", simulation=True)

                        if type(subHolder) == SubActor.SubActor:
                            meshes = subHolder.getGeometryNodes()
                            if not meshes:
                                subHolders = subHolder.getActor().getSubActors()
                                for sh in subHolders:
                                    meshes += sh.getGeometryNodes()
                        else:
                            meshes = []
                        
                        folder = animPreset.getPathTokenizer(branch="{FX}").Translate(animPreset.path)
                        name = animPreset.getConcatenatedName().format(left="left", right="right") + ".fbx"
                        exportObjs = exportNodes[subHolder] + meshes
                        exportObjs = exportObjs + cmds.listRelatives(exportObjs, allDescendents=True, path=True, type="transform")
                        
                        path = os.path.join(folder, name)
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                        
                        p4Changelist = P4Tools.P4Changelist.getChangelistByDescription("Animation FBX", createIfNotExists=True)
                        p4File = P4Tools.P4File(path)
                        p4File.smartCheckout(changelist=p4Changelist)
                        
                        MayaFBX.ExportFBX(path, exportObjs=exportObjs)
                        
            finally:
                cmds.playbackOptions(e=True, ast=currentAnimRange[0], aet=currentAnimRange[1], min=currentAnimRange[2], max=currentAnimRange[3])
                for animLayer in animLayers:
                    cmds.animLayer(animLayer, e=True, m=(animLayer not in currentAnimLayers))
            
        finally:
            for subHolder in exportData:
                subHolder.onPostExport(exportData[subHolder])
        
    # ------------------------------------
    # | Widget Callbacks                 |
    # ------------------------------------

    def onAddAnimButtonClicked(self, event):
        addAnimMenu = QtWidgets.QMenu(self.exporterWindow)
        
        actorMenu = QtWidgets.QMenu("Actors", self.exporterWindow)
        actors = ActorManager.getActors()
        for actor in actors:
            subActors = actor.getSubActorsByTags([SubActor.SubActor.Tags.Animatable])
            if len(subActors) > 0:
                subActorMenu = QtWidgets.QMenu(actor.getDisplayName(), self.exporterWindow)
                actorMenu.addMenu(subActorMenu)
            else:
                subActorMenu = actorMenu

            action = QtWidgets.QAction(actor.getDisplayName(), self.exporterWindow)
            action.triggered.connect(partial(self.addActorAnimation, actor))
            subActorMenu.addAction(action)
            subActorMenu.addSeparator()
            for subActor in subActors:
                action = QtWidgets.QAction(subActor.name, self.exporterWindow)
                action.triggered.connect(partial(self.addActorAnimation, actor, subActor))
                subActorMenu.addAction(action)
                
        cameraMenu = QtWidgets.QMenu("Cameras", self.exporterWindow)
        cameraSets = ActorManager.getCameraSets()
        for cameraSet in cameraSets:
            action = QtWidgets.QAction(cameraSet.name, cameraMenu)
            action.triggered.connect(partial(self.addCameraSetAnimation, cameraSet))
            cameraMenu.addAction(action)
            
        cameraMenu.addSeparator()
        createCameraSetAction = QtWidgets.QAction("Create Camera Set...", self.exporterWindow)
        createCameraSetAction.triggered.connect(self.showCreateCameraSetDialog)
        cameraMenu.addAction(createCameraSetAction)

        addAnimMenu.addMenu(actorMenu)
        addAnimMenu.addMenu(cameraMenu)

        addAnimMenu.exec_(QtGui.QCursor.pos())

    def onExportButtonClicked(self, event):
        animWidgets = [animWidget for animWidget in self.getAnimWidgets() if animWidget.isMarkedForExport()]
        self.exportAnimWidgets(animWidgets)

    def onToggleActiveAnimsStateChanged(self, state):
        with UndoContext("Set AnimPreset Active"):
            animWidgets = self.getAnimWidgets()
            for animWidget in animWidgets:
                animWidget.setMarkedForExport(state, updateUI=True)

    def onAnimPresetScrollAreaResize(self, event):
        # Resizes the header of the Animation scroll area to match the width of the scroll area when scroll bar appears/disappears.
        if self.ui.Scr_AnimScrollArea.verticalScrollBar().maximum() == 0:
            self.ui.Frm_AnimSort.layout().setContentsMargins(8, 0, 10, 0)
        else:
            self.ui.Frm_AnimSort.layout().setContentsMargins(8, 0, 22, 0)

    def onLayerPanelButtonStateChanged(self, layerButton, animWidget, animLayer, state):
        animWidget.setLayerState(animLayer, state)
        self.refreshButtonText(layerButton, animWidget, animLayer, state)
    
    def onLayerPanelButtonContextMenuRequested(self, animWidget, animLayer, pos):
        if self.isLayerEditModeEnabled() and not AnimLayerUtils.isBaseLayer(animLayer):
            contextMenu = QtWidgets.QMenu()
            
            editLayerWeightsAction = contextMenu.addAction("Edit Layer Weight", partial(self.onEditLayerWeightOptionSelected, [animWidget], animLayer))
            
            editLayerWeightsAction.setEnabled(animLayer in animWidget.animPreset.getAnimLayers())
            
            contextMenu.exec_(QtGui.QCursor.pos())
    
    def onLayerPanelItemDoubleClicked(self, item):
        if item.column() == 0 and self.isLayerEditModeEnabled():
            selectedAnimWidgets = self.getSelectedAnimWidgets()
            if len(selectedAnimWidgets) > 0:
                animLayer = item.text()
                app = QtGui.QGuiApplication.instance()
                if app.mouseButtons() == QtCore.Qt.LeftButton:
                    if not AnimLayerUtils.isBaseLayer(animLayer):
                        with UndoContext("Toggle AnimPreset Layers"):
                            shouldEnableAnimLayer = animLayer not in selectedAnimWidgets[0].animPreset.getAnimLayers()
                            for i in range(1, self.ui.Tbl_AnimList.columnCount()):
                                self.ui.Tbl_AnimList.cellWidget(item.row(), i).setChecked(shouldEnableAnimLayer)

    def onLayerPanelContextMenuRequested(self, pos):
        item = self.ui.Tbl_AnimList.itemAt(pos)
        if item and item.column() == 0 and self.isLayerEditModeEnabled():
            selectedAnimWidgets = self.getSelectedAnimWidgets()
            if len(selectedAnimWidgets) > 0:
                animLayer = item.text()
                if not AnimLayerUtils.isBaseLayer(animLayer):
                    contextMenu = QtWidgets.QMenu()
                    
                    editLayerWeightsAction = contextMenu.addAction("Edit Layer Weight", partial(self.onEditLayerWeightOptionSelected, selectedAnimWidgets, animLayer))
                    contextMenu.addSeparator()
                    clearLayerWeightsAction = contextMenu.addAction("Clear Layer Weights", partial(self.onClearLayerWeightsOptionSelected, animLayer))
                    
                    isLayerActiveOnSelectedWidgets = False
                    for animWidget in selectedAnimWidgets:
                        if animLayer in animWidget.animPreset.getAnimLayers():
                            isLayerActiveOnSelectedWidgets = True
                            break
                    
                    editLayerWeightsAction.setEnabled(isLayerActiveOnSelectedWidgets)
                    clearLayerWeightsAction.setEnabled(AnimPreset.AnimPreset.shouldUseAnimLayerWeight(animLayer))
                    
                    contextMenu.exec_(self.ui.Tbl_AnimList.mapToGlobal(pos))
    
    def onEditLayerWeightOptionSelected(self, animWidgets, animLayer):
        self.selectLayerWeight(animWidgets, animLayer)
        self.refreshLayerPanel()
    
    def onClearLayerWeightsOptionSelected(self, animLayer):
        if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self, "Clear AnimLayer Weights", "This will remove the weights on all the animations for the layer [{}]. Proceed?".format(animLayer)):
            with UndoContext("Clear AnimLayer Weight"):
                weightedLayers = AnimPreset.WeightedLayer.getConnectedWrappers([animLayer])
                for weightedLayer in weightedLayers:
                    weightedLayer.weight = 1
            self.refreshLayerPanel()
    
    def onGetAnimLayersButtonClicked(self):
        result = QtWidgets.QMessageBox.question(self.exporterWindow, "Get Animation Configuration", "This will replace the selected animations' layer configuration with the scene's current. Proceed?")
        if result == QtWidgets.QMessageBox.Yes:
            selectedAnimWidgets = self.getSelectedAnimWidgets()
            with UndoContext("Set AnimPreset Configuration From Scene"):
                for animWidget in selectedAnimWidgets:
                    animWidget.setAnimationConfigurationFromScene(animRange=False, animLayers=True)
            self.refreshLayerPanel()

    def onSetAnimLayersButtonClicked(self):
        self.applyAnimationConfiguration(self.getSelectedAnimWidgets())

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            self.mouseReleaseEvent(event)
            return True

        if event.type() == QtCore.QEvent.DragEnter:
            self.dragEnterEvent(event)
            return True

        if event.type() == QtCore.QEvent.Drop:
            self.dropEvent(event)
            return True

        return False

    def mouseReleaseEvent(self, event):
        if event.modifiers() == QtCore.Qt.NoModifier:
            self.selectAnimWidgets([])
    
    def dragEnterEvent(self, event):
        closestAnimWidget = self.getClosestAnimWidgetToPoint(event.pos())
        if closestAnimWidget != None:
            closestAnimWidget.dragEnterEvent(event)
    
    def dropEvent(self, event):
        closestAnimWidget = self.getClosestAnimWidgetToPoint(event.pos())
        if closestAnimWidget != None:
            event = QtGui.QDropEvent(closestAnimWidget.mapFromGlobal(self.ui.Scr_AnimScrollArea.mapToGlobal(event.pos())), event.dropAction(), event.mimeData(), event.mouseButtons(), event.keyboardModifiers())
            closestAnimWidget.dropEvent(event)
