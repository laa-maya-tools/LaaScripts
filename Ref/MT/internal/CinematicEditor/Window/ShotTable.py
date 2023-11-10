# coding: utf-8

from PySide2 import QtCore, QtWidgets, QtGui

import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window as CinematicEditorUtils
import CinematicEditor.Window.CinematicExportDialog as CinematicExportDialog

from QtCustomWidgets.ColorPickerButton import ColorPickerButton
import QtCustomWidgets.DecimalDetectorSpinBox as DecimalDetectorSpinBox
import QtCustomWidgets.QtUtils as QtUtils

import Utils.Maya as MayaUtils
from Utils.Maya.UndoContext import UndoContext, UndoOff

import functools

class ShotTableItemDelegate(QtWidgets.QStyledItemDelegate):
    
    SHOT_TEXT_ENABLED =                     QtGui.QColor.fromHsl(0, 0, 200)
    SHOT_TEXT_ENABLED_NOT_OWNED =           QtGui.QColor.fromHsl(0, 128, 180)
    SHOT_TEXT_ENABLED_HIGHLIFHT =           QtGui.QColor.fromHsl(0, 0, 255)
    SHOT_TEXT_DISABLED =                    QtGui.QColor.fromHsl(0, 0, 128)
    SHOT_TEXT_DISABLED_NOT_OWNED =          QtGui.QColor.fromHsl(0, 32, 96)
    SHOT_TEXT_DISABLED_HIGHLIGHT =          QtGui.QColor.fromHsl(0, 0, 154)
    
    SHOT_TEXT_NAME_OVERLAP =                QtGui.QColor.fromRgb(232, 128, 128)
    SHOT_TEXT_NAME_OVERLAP_HIGHLIFHT =      QtGui.QColor.fromRgb(255, 156, 156)
    
    SHOT_TEXT_CAMERA_SELECTED =             QtGui.QColor.fromRgb(126, 230, 126)
    SHOT_TEXT_CAMERA_SELECTED_HIGHLIGHT =   QtGui.QColor.fromRgb(140, 255, 140)
    SHOT_TEXT_CLAIMED =                     QtGui.QColor.fromRgb(212, 0, 0)
    SHOT_TEXT_CAMERA_CLAIMED_HIGHLIGHT =    QtGui.QColor.fromRgb(255, 0, 0)
    SHOT_TEXT_FREE =                        QtGui.QColor.fromRgb(0, 164, 212)
    SHOT_TEXT_CAMERA_FREE_HIGHLIGHT =       QtGui.QColor.fromRgb(0, 212, 255)
    
    SELECTION_HIGHLIGHT_COLOR =             QtGui.QColor.fromRgb(64, 96, 128)
    SELECTION_HIGHLIGHT_NOT_OWNED_COLOR =   QtGui.QColor.fromRgb(128, 64, 64)
    
    BACKGROUND_NOT_OWNED_COLOR =            QtGui.QColor.fromRgb(255, 0, 0)
    
    def __init__(self, cinematicEditor):
        QtWidgets.QStyledItemDelegate.__init__(self)
        
        self.cinematicEditor = cinematicEditor
        
    def getTextColor(self, shot, index, owned, free):
        if index.column() == 4: # Camera column
            if owned:
                selectedShots = self.cinematicEditor.shotTable.getSelectedShots()
                selectedCameras = [shot.camera for shot in selectedShots]
                if shot.camera in selectedCameras:
                    return self.SHOT_TEXT_CAMERA_SELECTED, self.SHOT_TEXT_CAMERA_SELECTED_HIGHLIGHT
            elif free:
                return self.SHOT_TEXT_FREE, self.SHOT_TEXT_CAMERA_FREE_HIGHLIGHT
                
        if shot.enabled:
            if owned:
                if index.column() == 2: # Shot Name column
                    shotOverlaps = shot.getCutscene().getShotOverlaps(shot)
                    if len(shotOverlaps) > 0:
                        return self.SHOT_TEXT_NAME_OVERLAP, self.SHOT_TEXT_NAME_OVERLAP_HIGHLIFHT
                return self.SHOT_TEXT_ENABLED, self.SHOT_TEXT_ENABLED_HIGHLIFHT
            else:
                return self.SHOT_TEXT_ENABLED_NOT_OWNED, self.SHOT_TEXT_ENABLED_HIGHLIFHT
        else:
            if owned:
                return self.SHOT_TEXT_DISABLED, self.SHOT_TEXT_DISABLED_HIGHLIGHT
            else:
                return self.SHOT_TEXT_DISABLED_NOT_OWNED, self.SHOT_TEXT_DISABLED_HIGHLIGHT
    
    def paint(self, painter, option, index):
        item = self.cinematicEditor.shotTable.item(index.row(), 0)
        shot = item.data(QtCore.Qt.UserRole)
        if self.cinematicEditor.cachedMasterSlaveFile:
            owned = self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)
            free = self.cinematicEditor.cachedMasterSlaveFile.isShotDelegated(shot) and not self.cinematicEditor.cachedMasterSlaveFile.isShotClaimed(shot)
        else:
            owned = True
            free = False
        
        targetColor, highlightColor = self.getTextColor(shot, index, owned, free)
        
        self.initStyleOption(option, index)
        
        option.palette.setColor(QtGui.QPalette.Text, targetColor)
        option.palette.setColor(QtGui.QPalette.HighlightedText, highlightColor)
        
        if owned:
            option.palette.setColor(QtGui.QPalette.Highlight, self.SELECTION_HIGHLIGHT_COLOR)
        else:
            option.palette.setColor(QtGui.QPalette.Highlight, self.SELECTION_HIGHLIGHT_NOT_OWNED_COLOR)
            option.palette.setColor(QtGui.QPalette.Window, self.BACKGROUND_NOT_OWNED_COLOR)
        
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)


class ShotTable(QtWidgets.QTableWidget):
    
    shotTooltipTemplate = "{genericTooltip}{fieldTooltip}{helpTooltip}"
    
    fieldIndexTooltip = "<p>This checkbox indicates if the shot should be exported on the current sesion.\nTo permanently avoid exporting this shot, disable it using the right-click menu.</p>"
    fieldColorTooltip = "<p>Shot color. You can change it using the right click menu.</p>"
    fieldNameTooltip = "<p>Shot name. Use it to identify your shots.</p>"
    fieldDescriptionTooltip = "<p>Shot description. Use it to provide short descriptions of your shots.</p>"
    fieldCameraTooltip = "<p>The camera for this shot. You can change it using the right-click menu.</p>"
    lockCameraTooltip = "<p>Locks the cameras, preventing them from moving.</p>"
    fieldStartTooltip = "<p>Shot start frame.</p>"
    fieldEndTooltip = "<p>Shot end frame.</p>"
    
    helpGenericTooltip = "<p><b>Double Click</b>: Applies the range and camera of this shot.</p>"
    
    lockCameraPixmapOn = QtGui.QPixmap(":Lock_ON.png")
    lockCameraPixmapOff = QtGui.QPixmap(":Lock_OFF_grey.png")
    
    def __init__(self, cinematicEditor):
        QtWidgets.QTableWidget.__init__(self, parent=None)
        
        self.cinematicEditor = cinematicEditor
        
        self.setStyleSheet("QTableWidget::item{ selection-background-color: rgba(0, 0, 0, 0) } QTableWidget::item:disabled{ color: gray; selection-color: hsl(0, 0, 72); }")
        
        self.setMinimumWidth(340)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.setSelectionMode(QtWidgets.QTableWidget.ExtendedSelection)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setDragDropMode(QtWidgets.QTableWidget.InternalMove)
        
        columns = ["Nº", "Color", "Shot", "Description", "Camera", "Lock", "Start", "End", "La mierda más grande de la historia, por cortesía de QT"]
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        # Si no hay una columna vacía, no funciona el Drag & Drop ¯\_(ツ)_/¯
        # Además, si intentamos el mismo enfoque de mouseMoveEvent que la lista de actores, no desaparece el indicador de drop al soltar
        self.setColumnWidth(len(columns) - 1, 0)
        
        horizontalHeader = self.horizontalHeader()
        horizontalHeader.setDefaultAlignment(QtCore.Qt.AlignLeft)
        horizontalHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(4, QtWidgets.QHeaderView.Interactive) # Esto permite redimensionar la sección de las cámaras (la nº3), aunque se hacede una manera bastante contraintuitiva...
        horizontalHeader.setSectionResizeMode(5, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setSectionResizeMode(6, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setSectionResizeMode(7, QtWidgets.QHeaderView.Fixed)
        horizontalHeader.setMinimumSectionSize(1)
        horizontalHeader.resizeSection(0, 38)
        horizontalHeader.resizeSection(1, 36)
        horizontalHeader.resizeSection(2, 78)
        horizontalHeader.resizeSection(4, 78)
        horizontalHeader.resizeSection(5, 24)
        horizontalHeader.resizeSection(6, 58)
        horizontalHeader.resizeSection(7, 58)
        
        lockCameraHeaderItem = QtWidgets.QTableWidgetItem()
        lockCameraHeaderItem.setIcon(QtGui.QIcon(":lock.png"))
        self.setHorizontalHeaderItem(5, lockCameraHeaderItem)
        
        verticalHeader = self.verticalHeader()
        verticalHeader.setVisible(False)
        verticalHeader.setDefaultSectionSize(25)
        
        self.itemChanged.connect(self.onToggleSelectedShotsActive)
        self.customContextMenuRequested.connect(self.onContextMenuRequested)
        self.itemDoubleClicked.connect(self.onItemDoubleClicked)
        
        self.setItemDelegate(ShotTableItemDelegate(self.cinematicEditor))

    # ------------------------------------
    # | Methods                          |
    # ------------------------------------

    def isMaster(self):
        if self.cinematicEditor.cachedMasterSlaveFile:
            return self.cinematicEditor.cachedMasterSlaveFile.isMaster()
        else:
            return True
        
    def canEditShot(self, shot):
        if self.cinematicEditor.cachedMasterSlaveFile:
            return self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)
        else:
            return True
    
    def createEmptyTableWidgetItem(self):
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        return item
    
    def reload(self):
        signalsBlocked = self.blockSignals(True)
        
        self.contextMenuOptions = self.createContextMenuOptions(owned=True)
        self.notOwnedContextMenuOptions = self.createContextMenuOptions(owned=False)
        
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            self.setRowCount(0)
        else:
            shots = cutscene.getShots()
            self.setRowCount(len(shots))
            for i, shot in enumerate(shots):
                shotIndexItem = QtWidgets.QTableWidgetItem()
                shotIndexItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
                shotIndexItem.setData(QtCore.Qt.UserRole, shot)
                
                shotColorItem = ColorPickerButton()
                shotColorItem.colorPicked.connect(functools.partial(self.onShotColorPicked, shot))  # With the WA_TransparentForMouseEvents set, this is useless, but we keep it in case we want this functionality in the future
                shotColorItemContainer = QtWidgets.QWidget()
                shotColorItemLayout = QtWidgets.QHBoxLayout(shotColorItemContainer)
                shotColorItemLayout.setContentsMargins(3, 0, 3, 0)
                shotColorItemLayout.addWidget(shotColorItem)
                
                shotNameItem = QtWidgets.QTableWidgetItem()
                shotNameItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                
                shotDescriptionItem = QtWidgets.QTableWidgetItem()
                shotDescriptionItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                
                shotCameraItem = QtWidgets.QTableWidgetItem()
                shotCameraItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                
                lockCameraItem = QtWidgets.QPushButton()
                lockCameraItem.setCheckable(True)
                lockCameraItem.toggled.connect(functools.partial(self.onLockCameraPressed, shot))
                lockCameraIcon = QtGui.QIcon()
                lockCameraIcon.addPixmap(self.lockCameraPixmapOn, state=QtGui.QIcon.On)
                lockCameraIcon.addPixmap(self.lockCameraPixmapOff, state=QtGui.QIcon.Off)
                lockCameraItem.setIcon(lockCameraIcon)
                lockCameraPalette = QtGui.QPalette()
                lockCameraPalette.setColor(QtGui.QPalette.Button, QtGui.QColor.fromHsl(0, 0, 64))
                lockCameraItem.setPalette(lockCameraPalette)
                
                shotStartItem = DecimalDetectorSpinBox.DecimalDetectorSpinBox()
                shotStartItem.setFixedWidth(self.columnWidth(6))
                shotStartItem.setRange(-99999, 99999)
                shotStartItem.setKeyboardTracking(False)
                shotStartItem.setFocusPolicy(QtCore.Qt.ClickFocus)
                shotStartItem.valueChanged.connect(functools.partial(self.onRangeStartChanged, shot))
                
                shotEndItem = DecimalDetectorSpinBox.DecimalDetectorSpinBox()
                shotEndItem.setFixedWidth(self.columnWidth(7))
                shotEndItem.setRange(-99999, 99999)
                shotEndItem.setKeyboardTracking(False)
                shotEndItem.setFocusPolicy(QtCore.Qt.ClickFocus)
                shotEndItem.valueChanged.connect(functools.partial(self.onRangeEndChanged, shot))
                
                self.setItem(i, 0, shotIndexItem)
                self.setCellWidget(i, 1, shotColorItemContainer)
                self.setItem(i, 1, self.createEmptyTableWidgetItem())   # Sin estos items vacíos, el Drag & Drop intenta dropear en la casilla en sí, en vez de entre líneas.
                self.setItem(i, 2, shotNameItem)
                self.setItem(i, 3, shotDescriptionItem)
                self.setItem(i, 4, shotCameraItem)
                self.setCellWidget(i, 5, lockCameraItem)
                self.setItem(i, 5, self.createEmptyTableWidgetItem())
                self.setCellWidget(i, 6, shotStartItem)
                self.setItem(i, 6, self.createEmptyTableWidgetItem())
                self.setCellWidget(i, 7, shotEndItem)
                self.setItem(i, 7, self.createEmptyTableWidgetItem())
                
                # We actually don't want the user to be able to change the color by clicking it,
                # so we make it transparent for mouse events.
                shotColorItem.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.blockSignals(signalsBlocked)
            
        self.refresh()

    def refresh(self):
        signalsBlocked = self.blockSignals(True)
        
        for i in range(self.rowCount()):
            shotIndexItem = self.item(i, 0)
            shot = shotIndexItem.data(QtCore.Qt.UserRole)
            enabled = shot.enabled
            camera = shot.camera
            color = CinematicEditorUtils.tupleAsColor(shot.color) if shot.color != None else QtCore.Qt.black
            
            shotOverlaps = shot.getCutscene().getShotOverlaps(shot)
            
            if self.cinematicEditor.cachedMasterSlaveFile:
                owned = self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)
                delegated = self.cinematicEditor.cachedMasterSlaveFile.isShotDelegated(shot)
                claimed = delegated and self.cinematicEditor.cachedMasterSlaveFile.isShotClaimed(shot)
                
                shotOverlaps = [s for s in shotOverlaps if self.cinematicEditor.cachedMasterSlaveFile.ownsShot(s)] if owned else []
                
                if not owned:
                    color = QtCore.Qt.darkGray
                    
            else:
                owned = True
                delegated = False
                claimed = False
                
            
            shotGenericTooltip = CinematicEditorUtils.getShotTooltip(shot, shotOverlaps=shotOverlaps, owned=owned)
            
            shotIndexItem.setText(str(i + 1).zfill(3))
            shotIndexItem.setCheckState(QtCore.Qt.Checked if shot.active and enabled and owned else QtCore.Qt.Unchecked)
            shotIndexItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldIndexTooltip, helpTooltip=self.helpGenericTooltip))
            if owned:
                shotIndexItem.setFlags(shotIndexItem.flags() | QtCore.Qt.ItemIsUserCheckable)
            else:
                shotIndexItem.setFlags(shotIndexItem.flags() & ~QtCore.Qt.ItemIsUserCheckable)
            
            shotColorWidget = self.cellWidget(i, 1)
            shotColorItem = shotColorWidget.layout().itemAt(0).widget()
            shotColorItemSignalsBlocked = shotColorItem.blockSignals(True)
            shotColorItem.setColor(color)
            shotColorItem.setBorderColor(QtCore.Qt.black if owned else QtGui.QColor.fromRgb(128, 0, 0))
            shotColorItem.blockSignals(shotColorItemSignalsBlocked)
            shotColorItem.setEnabled(enabled)
            
            # Since the shotColorWidget is transparent to mouse events, we need to
            # set the tooltip on the cell item underneath.
            self.item(i, 1).setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldColorTooltip, helpTooltip=self.helpGenericTooltip))
            
            shotNameItem = self.item(i, 2)
            shotNameItem.setText(shot.shotName)
            shotNameItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldNameTooltip, helpTooltip=self.helpGenericTooltip))
            
            shotDescriptionItem = self.item(i, 3)
            shotDescriptionItem.setText(shot.description)
            shotDescriptionItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldDescriptionTooltip, helpTooltip=self.helpGenericTooltip))
            
            shotCameraItem = self.item(i, 4)
            if owned:
                cameraText = camera if camera else "<No Camera>"
            elif not delegated:
                cameraText = "<MASTER>"
            elif claimed:
                cameraText = "<CLAIMED>"
            else:
                cameraText = "<FREE>"
            shotCameraItem.setText(cameraText)
            shotCameraItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldCameraTooltip, helpTooltip=self.helpGenericTooltip))
            
            lockCameraItem = self.cellWidget(i, 5)
            lockCameraItem.setChecked(cmds.camera(camera, q=True, lt=True) if camera else False)
            lockCameraItem.setEnabled(owned and camera != None)
            lockCameraItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.lockCameraTooltip, helpTooltip=""))
            
            shotStartItem = self.cellWidget(i, 6)
            if owned:
                shotStartItem.setValue(shot.start)
            else:
                shotStartItem.clear()
            shotStartItem.setEnabled(owned)
            shotStartItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldStartTooltip, helpTooltip=""))
            if len(shotOverlaps) == 0:
                QtUtils.restorePaletteColor(shotStartItem, QtGui.QPalette.Window)
                #QtUtils.restorePaletteColor(shotStartItem.lineEdit(), QtGui.QPalette.Text)
            else:
                QtUtils.setPaletteColor(shotStartItem, QtGui.QPalette.Window, QtCore.Qt.red)
                #QtUtils.setPaletteColor(shotStartItem.lineEdit(), QtGui.QPalette.Text, QtCore.Qt.red)
            
            shotEndItem = self.cellWidget(i, 7)
            shotEndItem.setValue(shot.end)
            shotEndItem.setEnabled(owned)
            shotEndItem.setToolTip(self.shotTooltipTemplate.format(genericTooltip=shotGenericTooltip, fieldTooltip=self.fieldEndTooltip, helpTooltip=""))
            if len(shotOverlaps) == 0:
                QtUtils.restorePaletteColor(shotEndItem, QtGui.QPalette.Window)
                #QtUtils.restorePaletteColor(shotEndItem.lineEdit(), QtGui.QPalette.Text)
            else:
                QtUtils.setPaletteColor(shotEndItem, QtGui.QPalette.Window, QtCore.Qt.red)
                #QtUtils.setPaletteColor(shotEndItem.lineEdit(), QtGui.QPalette.Text, QtCore.Qt.red)
            
        self.blockSignals(signalsBlocked)
        
        self.viewport().update()

    def getSelectedRows(self):
        selectedRows = self.selectionModel().selectedRows()
        selectedRows = [index.row() for index in selectedRows]
        selectedRows.sort()
        return selectedRows

    def getSelectedShots(self, onlyOwned=False):
        selectedRows = self.getSelectedRows()
        shots = [self.item(row, 0).data(QtCore.Qt.UserRole) for row in selectedRows]
        if onlyOwned:
            shots = [shot for shot in shots if self.canEditShot(shot)]
        return shots

    def selectShots(self, shots, scrollToLast=False):
        wereSignalsBlocked = self.blockSignals(True)
        
        selectionModel = self.selectionModel()
        self.clearSelection()
        lastSelectedItem = None
        for i in range(self.rowCount()):
            item = self.item(i, 0)
            if item.data(QtCore.Qt.UserRole) in shots:
                selectionModel.select(self.indexFromItem(item), QtCore.QItemSelectionModel.Rows | QtCore.QItemSelectionModel.Select)
                lastSelectedItem = item
                
        if scrollToLast and lastSelectedItem is not None:
            self.scrollToItem(lastSelectedItem)
            
        self.blockSignals(wereSignalsBlocked)
        
        self.viewport().update()

    def addShot(self, arg=None, promptEdit=True, parent=None):   # We receive some useless argument that we need to take in (the arg parameter)
        if not self.isMaster():
            raise AssertionError("Only the Master can Add Shots!")
        
        with UndoContext("Add Shot"):
            cutscene = CinematicEditor.getCutscene(createIfNotExists=True)
        
            shot = cutscene.createShot()
            
            i = cutscene.getShotIndex(shot) + 1
            while True:
                newShotName = "S{}".format(str(i).zfill(3))
                if cutscene.getShotByName(newShotName) == None:
                    break
                i += 1
            
            shot.shotName = newShotName
            shot.start = cmds.playbackOptions(q=True, min=True)
            shot.end = cmds.playbackOptions(q=True, max=True)
            shot.color = CinematicEditorUtils.colorAsTuple(CinematicEditorUtils.getRandomColor(distinctFrom=[CinematicEditorUtils.tupleAsColor(s.color) for s in shot.getSurroundingShots()]))
        
            if promptEdit:
                if parent == None:
                    parent = self
                result = CinematicEditorUtils.EditShotDialog(shot, shotBeingCreated=True, color=True, name=True, description=True, camera=True, start=True, end=True, title="Add Shot", parent=parent).exec_()
                if not result:
                    cutscene.removeShot(shot, delete=True)
                    return
        
        self.cinematicEditor.reloadShots()
        self.selectShots([shot], scrollToLast=True)

    # ------------------------------------
    # | Drag & Drop                      |
    # ------------------------------------
    
    def createDragPixmap(self):
        selectedRows = self.getSelectedRows()[:5]
        totalHeight = 0
        for row in selectedRows:
            totalHeight += self.rowHeight(row)

        pixmap = QtGui.QPixmap.grabWidget(self)
        selectedShotsPixmap = QtGui.QPixmap(pixmap.width(), totalHeight)
        selectedShotsPixmap.fill(QtGui.QColor(0, 0, 0, 0))

        painter = QtGui.QPainter(selectedShotsPixmap)
        acumulatedHeight = 0
        initialRowPosition = self.horizontalHeader().height()
        for i, row in enumerate(selectedRows):
            rowHeight = self.rowHeight(row)
            painter.setOpacity(0.1 * (5 - i))
            painter.drawPixmap(0, acumulatedHeight, pixmap, 0, initialRowPosition + self.rowViewportPosition(row), pixmap.width(), rowHeight)
            acumulatedHeight += rowHeight
        painter.end()

        return selectedShotsPixmap

    def startDrag(self, supportedActions):
        if self.isMaster() and (supportedActions & QtCore.Qt.MoveAction):
            items = self.selectedItems()
            if len(items) == 0:
                return
            drag = QtGui.QDrag(self)
            drag.setPixmap(self.createDragPixmap())
            drag.setMimeData(self.mimeData(items))
            dropAction = drag.exec_(QtCore.Qt.MoveAction)   # We don't need to do anything in particular with the drop action
            
        else:
            QtWidgets.QTableWidget.startDrag(self, supportedActions)

    def dropEvent(self, event):
        if not self.isMaster():
            raise AssertionError("Only the Master can reorder Shots!")
        
        if event.dropAction() == QtCore.Qt.MoveAction:
            selectedShots = self.getSelectedShots()
            
            targetShot = None
            dropPos = event.pos().y()
            for i in range(self.rowCount()):
                refPos = self.rowViewportPosition(i) + self.rowHeight(i) / 2
                if dropPos < refPos:
                    shot = self.item(i, 0).data(QtCore.Qt.UserRole)
                    if shot not in selectedShots:
                        targetShot = shot
                        break
            
            with UndoContext("Reorder Shots"):
                cutscene = CinematicEditor.getCutscene()
                for shot in selectedShots:
                    cutscene.removeShot(shot, disableAllActors=False)
                if targetShot == None:
                    for shot in selectedShots:
                        cutscene.addShot(shot, enableAllActors=False)
                else:
                    targetIndex = cutscene.getShotIndex(targetShot)
                    for i, shot in enumerate(selectedShots):
                        cutscene.insertShot(shot, targetIndex + i, enableAllActors=False)
            
            self.cinematicEditor.reloadShots()
            self.selectShots(selectedShots)

    # ------------------------------------
    # | Events                           |
    # ------------------------------------

    def onToggleSelectedShotsActive(self, changedItem):
        if changedItem.column() == 0:
            signalsBlocked = self.blockSignals(True)

            if changedItem.isSelected():
                selectedShots = self.getSelectedShots()
            else:
                selectedShots = [changedItem.data(QtCore.Qt.UserRole)]

            with UndoOff(): # We don't actually want to undo this.
                checked = changedItem.checkState() == QtCore.Qt.Checked
                for shot in selectedShots:
                    if self.canEditShot(shot):
                        shot.active = checked

            self.cinematicEditor.reloadShots()  # Shots need to be reloaded becouse inactive shots may not appear on the timeline
            
            QtCore.QTimer.singleShot(0, functools.partial(self.selectShots, selectedShots))

            self.blockSignals(signalsBlocked)

    def onShotColorPicked(self, shot, color):
        selectedShots = self.getSelectedShots()
        if shot not in selectedShots:
            selectedShots = [shot]
            self.selectShots(selectedShots)
        
        with UndoContext("Set Shot Color"):
            colorTuple = CinematicEditorUtils.colorAsTuple(color)
            for selectedShot in selectedShots:
                if self.canEditShot(shot):
                    selectedShot.color = colorTuple
        
        self.cinematicEditor.refreshShots()

    def onLockCameraPressed(self, shot, state):
        if self.signalsBlocked():
            return  # Instead of blocking the signals for each specific ShotRange Widget, we block the signals for the table itself and check it here.
        
        selectedShots = self.getSelectedShots()
        if shot not in selectedShots:
            selectedShots = [shot]
            self.selectShots(selectedShots)
        
        with UndoContext("Lock Shot Camera"):
            for selectedShot in selectedShots:
                if selectedShot.camera and self.canEditShot(selectedShot):
                    cmds.camera(selectedShot.camera, e=True, lt=state)
        
        #self.refresh() # There is no need to refresh the table here, changing the lock state of the camera will trigger a callback that will refresh the table

        # The viewport's lock button won't notice the lock change, so we update it (sometimes it will, but it is inconsistent...)
        viewports = cmds.getPanel(type="modelPanel")
        for viewport in viewports:
            camera = cmds.modelPanel(viewport, q=True, camera=True)
            cameraLockedState = cmds.camera(camera, q=True, lt=True)
            
            iconBar = cmds.modelPanel(viewport, q=True, barLayout=True)
            iconBarLayout = cmds.layout(cmds.layout(iconBar, q=True, childArray=True)[0], q=True, fullPathName=True)
            firstLayout = cmds.layout(cmds.layout(iconBarLayout, q=True, childArray=True)[1], q=True, fullPathName=True)
            lockCameraButton = "{}|LockCameraBtn".format(firstLayout)
            
            cmds.iconTextCheckBox(lockCameraButton, e=True, value=cameraLockedState)

    def onRangeStartChanged(self, shot, val):
        if self.signalsBlocked():
            return  # Instead of blocking the signals for each specific ShotRange Widget, we block the signals for the table itself and check it here.
        
        if not self.canEditShot(shot):
            raise AssertionError("Can't edit non-claimed Shot!")
        
        with UndoContext("Set Shot Start"):
            if cmds.playbackOptions(q=True, min=True) == shot.start:
                cmds.playbackOptions(e=True, min=val, ast=val)
            
            shot.start = val
        
        self.cinematicEditor.refreshShots()

    def onRangeEndChanged(self, shot, val):
        if self.signalsBlocked():
            return  # Instead of blocking the signals for each specific ShotRange Widget, we block the signals for the table itself and check it here.
        
        if not self.canEditShot(shot):
            raise AssertionError("Can't edit non-claimed Shot!")
        
        with UndoContext("Set Shot End"):
            if cmds.playbackOptions(q=True, max=True) == shot.end:
                cmds.playbackOptions(e=True, max=val, aet=val)
                
            shot.end = val
        
        self.cinematicEditor.refreshShots()

    def onItemDoubleClicked(self, item):
        shot = self.item(item.row(), 0).data(QtCore.Qt.UserRole)
        self.cinematicEditor.cinematicEditorTimeline.setCurrentShot(shot, applyShotRange=True, applyShotCamera=True)

    def onContextMenuRequested(self, pos):
        clickedItem = self.itemAt(pos)
        if clickedItem is not None:
            if not clickedItem.isSelected():
                self.selectRow(self.indexFromItem(clickedItem).row())
            multiSelection = len(self.selectionModel().selectedRows()) > 1
            
            ownedShotSelected = False
            selectedShots = self.getSelectedShots()
            for shot in selectedShots:
                if self.canEditShot(shot):
                    ownedShotSelected = True
                    break
            
            menu = self.contextMenuOptions if ownedShotSelected else self.notOwnedContextMenuOptions
            QtUtils.showContextMenu(menu, self, QtGui.QCursor.pos(), multiSelection=multiSelection)

    def showContextMenuForShot(self, shot, parent=None, allowMultiSelection=True):
        if parent == None:
            parent = self
        
        multiSelection = False
        if allowMultiSelection:
            selectedShots = self.getSelectedShots()
            if shot not in selectedShots:
                self.selectShots([shot])
            else:
                multiSelection = len(selectedShots) > 1
                
        ownedShotSelected = False
        selectedShots = self.getSelectedShots()
        for shot in selectedShots:
            if self.canEditShot(shot):
                ownedShotSelected = True
                break
        
        menu = self.contextMenuOptions if ownedShotSelected else self.notOwnedContextMenuOptions
        QtUtils.showContextMenu(menu, parent, QtGui.QCursor.pos(), multiSelection=multiSelection)

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def selectionChanged(self, newSelection, oldSelection):
        QtWidgets.QTableView.selectionChanged(self, newSelection, oldSelection)
        
        # The range spinner won't let go of the focus so we manually take it from them.
        for i in range(self.rowCount()):
            startSpinner = self.cellWidget(i, 4)
            if startSpinner != None:
                startSpinner.clearFocus()
            endSpinner = self.cellWidget(i, 5)
            if endSpinner != None:
                endSpinner.clearFocus()
        
        # Refreshes the viewport becouse changing the selection might change the visuals of some unselected items
        self.viewport().update()
                
        self.cinematicEditor.cinematicEditorTimeline.shotTimeline.refreshSelectedShots(self.getSelectedShots())

    # ------------------------------------
    # | Context Menu                     |
    # ------------------------------------

    def createContextMenuOptions(self, owned=True):
        master = self.isMaster()
        
        options = []
        options.append(QtUtils.MenuOption("selectShot",            "Select Shot",              False,  self.onSelectShotOptionSelected, "<p>Selects this shot, applying it's range and camera to the viewport.</p><p>You can also select a Shot by <i>Doublic-Clicking</i> it.</p>"))
        if owned:
            options.append(None)
            options.append(QtUtils.MenuOption("selectCamera",          "Select Camera",            True,   self.onSelectCameraOptionSelected, "Selects the cameras for the selected shots."))
            options.append(QtUtils.MenuOption("setCameraToViewport",   "Set Camera to Viewport",   False,  self.onSetCameraToViewportOptionSelected, "Sets the current viewport camera to this one."))
        options.append(None)
        if owned:
            options.append(QtUtils.MenuOption("frameShot",             "Frame Selected Shots",     True,   self.onFrameShotOptionSelected, "Applies the combined animation range of the selected shots."))
        options.append(QtUtils.MenuOption("zoomShot",              "Zoom Selected Shots",      True,   self.onZoomShotsOptionSelected, "<p>Zooms the timeline so it frames the selected shots.</p><p>When the timeline is zoomed, the playback will loop on the zoomed range.</p>"))
        if owned:
            if master:
                options.append(None)
                options.append(QtUtils.MenuOption("renameShot",            "Rename Shot",              False,  self.onRenameShotOptionSelected, "Renames the Shot."))   # TODO: No sabemos si el nombre de los shots se va a usar como nombre para las carpetas. En ese caso, indicarlo en este tooltip (o indicar que es solo estetico si no)
                options.append(QtUtils.MenuOption("selectShotDescription", "Change Shot Description",  True,  self.onSelectShotDescriptionOptionSelected, "Cahnges the description of the selected Shots.")) 
            options.append(None)
            options.append(QtUtils.MenuOption("selectShotCamera",      "Change Shot Camera",       True,   self.onSelectShotCameraOptionSelected, "<p>Changes the Shot camera.</p><p>You can also use this option to create and assign a new camera.</p>"))
            options.append(QtUtils.MenuOption("selectShotColor",       "Change Shot Color",        True,   self.onSelectShotColorOptionSelected, "<p>Changes the Shot color.</p><p>This color is only esthetic and won't affect the exported cutscene.</p>"))
            options.append(QtUtils.MenuOption("selectShotRange",       "Change Shot Range",        True,   self.onSelectShotRangeOptionSelected, "<p>Changes the Shot range.</p>"))
            if master:
                options.append(None)
                options.append(QtUtils.MenuOption("enableShot",            "Enable Selected Shots",    True,   self.onEnableShotOptionSelected, "<p>Enables the selected Shots.</p><p>If a shot is <b>disabled</b> it won't be part of cutscene and it will never be exported.</p>"))
                options.append(QtUtils.MenuOption("disableShot",           "Disable Selected Shots",   True,   self.onDisableShotOptionSelected, "<p>Disables the selected Shots.</p><p>If a shot is <b>disabled</b> it won't be part of cutscene and it will never be exported.</p>"))
            options.append(None)
            options.append(QtUtils.MenuOption("exportShot",            "Export Selected Shots",    True,   subMenus=
                [
                    QtUtils.MenuOption("exportShotFull",        "Camera and Actors (All)",  True,   self.onExportShotFullOptionSelected, "<p>Exports the selected Shots' <b>camera</b> and their <b>Actors</b> (even if the Actors' checkmarks are unmarked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                    None,
                    QtUtils.MenuOption("exportShotCamera",      "Camera",                   True,   self.onExportShotCameraOptionSelected, "<p>Exports the selected Shots' <b>camera</b>."),
                    None,
                    QtUtils.MenuOption("exportShotAll",         "Actors (All)",             True,   self.onExportShotActorsOptionSelected, "<p>Exports <b>all the Actors</b> for the selected Shots (even if the Actors' checkmarks are unmarked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                    QtUtils.MenuOption("exportShotMarked",      "Actors (Marked)",          True,   self.onExportShotMarkedActorsOptionSelected, "<p>Exports <b>the marked Actors</b> (those whose checkmarks are marked) for the selected Shots.</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                    QtUtils.MenuOption("exportShotSelected",    "Actors (Selected)",        True,   self.onExportShotSelectedActorsOptionSelected, "<p>Exports <b>the selected Actors</b> for the selected Shots (even if the Actors' checkmarks are unmarked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                ]))
            options.append(QtUtils.MenuOption("playblastShot",         "Playblast Selected Shots", True,   self.onPlayblastShotOptionSelected, "Playblasts the selected Shots."))
        if master:
            options.append(None)
            options.append(QtUtils.MenuOption("duplicateShot",         "Duplicate Selected Shots", True,   self.onDuplicateShotOptionSelected, "Duplicates the selected Shots (it won't duplicate their camera)."))
            if owned:
                options.append(None)
                options.append(QtUtils.MenuOption("deleteShot",            "Delete Selected Shots",    True,   self.onDeleteShotOptionSelected, "Deletes the selected Shots."))
        
        return options
    
    def onSelectShotOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) != 1:
            raise AssertionError("Unable to select Shot: You can only select one shot at once!")
        
        self.cinematicEditor.cinematicEditorTimeline.setCurrentShot(selectedShots[0], applyShotRange=True, applyShotCamera=True)
    
    def onFrameShotOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) == 0:
            raise AssertionError("Unable to frame Shot: You must have at least one shot selected!")
        
        start = None
        end = None
        for shot in selectedShots:
            if self.canEditShot(shot):
                if start == None or start > shot.start:
                    start = shot.start
                if end == None or end < shot.end:
                    end = shot.end
        
        cmds.playbackOptions(e=True, min=start, ast=start, max=end, aet=end)            
    
    def onSelectCameraOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) == 0:
            raise AssertionError("Unable to select Camera: You must have at least one shot selected!")
        
        cameras = []
        for shot in selectedShots:
            if self.canEditShot(shot):
                camera = shot.camera
                if camera != None:
                    cameras.append(camera)
                
        cmds.select(cameras)
    
    def onSetCameraToViewportOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) != 1:
            raise AssertionError("Unable to set camera to viewport: You can only select one shot at once!")
        if not self.canEditShot(selectedShots[0]):
            raise AssertionError("Can't apply non-claimed Shots cameras!")
        
        selectedShots[0].applyCamera(applyToCurrent=True)
    
    def onZoomShotsOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) == 0:
            raise AssertionError("Unable to zoom Shot: You must have at least one shot selected!")
        
        cutscene = selectedShots[0].getCutscene()
        start = cutscene.getCutsceneFrameFromShot(selectedShots[0]) # The shots are already ordered, so we just have to retireve the first and last's cutscene frames.
        end = cutscene.getCutsceneFrameFromShot(selectedShots[-1], shotFrame=selectedShots[-1].getDuration())
        
        self.cinematicEditor.cinematicEditorTimeline.timelineSlider.setRange(start, end)
    
    def onRenameShotOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) != 1:
            raise AssertionError("Unable to rename Shot: You can only rename one shot at a time!")
        if not self.isMaster():
            raise AssertionError("Only the Master can rename Shots!")
        
        with UndoContext("Rename Shot"):    # This UndoContext is not really necessary, but will display a more specific message than the one EditShotDialog would.
            CinematicEditorUtils.EditShotDialog(selectedShots[0], name=True, title="Rename Shot", parent=self.sender().parent()).exec_()

        self.cinematicEditor.refreshShots()
    
    def onSelectShotDescriptionOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) == 0:
            raise AssertionError("Unable to change Shot description: You must have at least one shot selected!")
        if not self.isMaster():
            raise AssertionError("Only the Master can change Shot descriptions!")
        
        with UndoContext("Change Shot Description"):    # This UndoContext is not really necessary, but will display a more specific message than the one EditShotDialog would.
            result = CinematicEditorUtils.EditShotDialog(selectedShots[0], description=True, title="Change Shot Description", parent=self.sender().parent()).exec_()
            if result:
                description = selectedShots[0].description
                for i in range(1, len(selectedShots)):
                    if self.canEditShot(selectedShots[i]):
                        selectedShots[i].description = description
                        
        self.cinematicEditor.refreshShots()
    
    def onSelectShotCameraOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if len(selectedShots) == 0:
            raise AssertionError("Unable to change Shot Camera: You must have at least one shot selected!")
        
        if not self.canEditShot(selectedShots[0]):
            raise AssertionError("Can't change non-claimed Shots cameras!")
        
        with UndoContext("Select Shot Camera"):
            result = CinematicEditorUtils.EditShotDialog(selectedShots[0], camera=True, title="Select Shot Camera", parent=self.sender().parent()).exec_()
            if result:
                camera = selectedShots[0].camera
                for i in range(1, len(selectedShots)):
                    if self.canEditShot(selectedShots[i]):
                        selectedShots[i].camera = camera
                selectedShots[0].applyCamera()
        
        self.cinematicEditor.refreshShots()
    
    def onSelectShotColorOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if len(selectedShots) == 0:
            raise AssertionError("Unable to change Shot Color: You must have at least one shot selected!")
        
        color = QtWidgets.QColorDialog.getColor(CinematicEditorUtils.tupleAsColor(selectedShots[0].color), self.sender().parent())
        if color != None:
            with UndoContext("Set Shot Color"):
                color = CinematicEditorUtils.colorAsTuple(color)
                for shot in selectedShots:
                    if self.canEditShot(shot):
                        shot.color = color

            self.cinematicEditor.refreshShots()
    
    def onSelectShotRangeOptionSelected(self):
        selectedShots = self.getSelectedShots()
        if len(selectedShots) == 0:
            raise AssertionError("Unable to change Shot Range: You must have at least one shot selected!")
        if not self.canEditShot(selectedShots[0]):
            raise AssertionError("Can't change non-claimed Shots ranges!")
        
        with UndoContext("Select Shot Range"):    # This UndoContext is not really necessary, but will display a more specific message than the one EditShotDialog would.
            CinematicEditorUtils.EditShotDialog(selectedShots[0], start=True, end=True, title="Select Shot Range", parent=self.sender().parent()).exec_()
        
        self.cinematicEditor.refreshShots()
    
    def onEnableShotOptionSelected(self):
        if not self.isMaster():
            raise AssertionError("Only the Master can enable Shots!")
        
        with UndoContext("Enable Shot"):
            selectedShots = self.getSelectedShots()
            for shot in selectedShots:
                shot.enabled = True
                shot.active = True
            
        self.cinematicEditor.reloadShots()  # Shots need to be reloaded becouse disabled shots won't appear on the timeline
    
    def onDisableShotOptionSelected(self):
        if not self.isMaster():
            raise AssertionError("Only the Master can disable Shots!")
        
        with UndoContext("Disable Shot"):
            selectedShots = self.getSelectedShots()
            for shot in selectedShots:
                shot.enabled = False
                shot.active = False
            
        self.cinematicEditor.reloadShots()  # Shots need to be reloaded becouse disabled shots won't appear on the timeline
    
    def onPlayblastShotOptionSelected(self):
        self.cinematicEditor.performPlayblast(shotOption=2)
    
    def onExportShotFullOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if selectedShots:
            cutscene = selectedShots[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, actors=cutscene.getCutsceneActors(), cameras=True, forceShots=True, forceActors=True)
    
    def onExportShotCameraOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if selectedShots:
            cutscene = selectedShots[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, cameras=True, forceShots=True)
    
    def onExportShotActorsOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if selectedShots:
            cutscene = selectedShots[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, actors=cutscene.getCutsceneActors(), forceShots=True, forceActors=True)
    
    def onExportShotMarkedActorsOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        if selectedShots:
            cutscene = selectedShots[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, actors=cutscene.getCutsceneActors(), forceShots=True, forceActors=False)
    
    def onExportShotSelectedActorsOptionSelected(self):
        selectedShots = self.getSelectedShots(onlyOwned=True)
        selectedActors = self.cinematicEditor.actorList.getSelectedCutsceneActors()
        if selectedShots and selectedActors:
            cutscene = selectedShots[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, actors=selectedActors, forceShots=True, forceActors=True)
    
    def onDuplicateShotOptionSelected(self):
        if not self.isMaster():
            raise AssertionError("Only the Master can duplicate Shots!")
        
        with UndoContext("Duplicate Shot"):
            selectedShots = self.getSelectedShots()
            for shot in selectedShots:
                shot.duplicateShot(rename=True)
            
            self.cinematicEditor.reloadShots()
    
    def onDeleteShotOptionSelected(self):
        if not self.isMaster():
            raise AssertionError("Only the Master can delete Shots!")
        
        with UndoContext("Delete Shot"):
            selectedShots = self.getSelectedShots()
            shotListString = ""
            for shot in selectedShots:
                shotListString += "\n- {}".format(shot.shotName)
            result = QtWidgets.QMessageBox.question(self.sender().parent(), "Delete Shots", "Are you sure you want to delete the selected shots?\n{}".format(shotListString), buttons=QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel), defaultButton=QtWidgets.QMessageBox.Yes)
            if result == QtWidgets.QMessageBox.Cancel:
                return
            
            cutscene = CinematicEditor.getCutscene()
            shots = cutscene.getShots()
            nonSelectedShotsCameras = set(shot.camera for shot in shots if shot not in selectedShots and shot.camera != None)
            unusedCameras = set(shot.camera for shot in selectedShots if shot.camera not in nonSelectedShotsCameras and shot.camera != None)
            
            if unusedCameras:
                cameraListString = ""
                for camera in unusedCameras:
                    cameraListString += "\n- {}".format(camera)
                result = QtWidgets.QMessageBox.question(self.sender().parent(), "Delete Shots", "The following cameras are no longer used, do you want to delete them?\n{}".format(cameraListString), buttons=QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel), defaultButton=QtWidgets.QMessageBox.Yes)
                if result == QtWidgets.QMessageBox.Cancel:
                    return
                elif result == QtWidgets.QMessageBox.Yes:
                    for camera in unusedCameras:
                        MayaUtils.deleteCamera(camera)
                        
            for shot in selectedShots:
                shot.delete()
                    
            self.cinematicEditor.reloadShots()
