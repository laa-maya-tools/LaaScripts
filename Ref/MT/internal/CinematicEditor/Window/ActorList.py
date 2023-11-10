# coding: utf-8

from PySide2 import QtCore, QtWidgets, QtGui

import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window.CinematicExportDialog as CinematicExportDialog

import QtCustomWidgets.QtUtils as QtUtils

import ActorManager
import ActorManager.Actor as Actor

from Utils.Maya.UndoContext import UndoContext, UndoOff

import ActorBrowser

import functools

class ActorListItemDelegate(QtWidgets.QStyledItemDelegate):
    
    NO_SHOT_SELECTED_COLOR =                    QtGui.QColor.fromHsl(0, 0, 200)
    NO_SHOT_SELECTED_COLOR_HIGHLIGHTED =        QtGui.QColor.fromHsl(0, 0, 255)
    ACTOR_DISABLED_COLOR =                      QtGui.QColor.fromRgb(224, 0, 0)
    ACTOR_DISABLED_COLOR_HIGHLIGHTED =          QtGui.QColor.fromRgb(255, 0, 0)
    ACTOR_ENABLED_COLOR =                       QtGui.QColor.fromRgb(0, 224, 0)
    ACTOR_ENABLED_COLOR_HIGHLIGHTED =           QtGui.QColor.fromRgb(0, 255, 0)
    ACTOR_PARTIAL_COLOR =                       QtGui.QColor.fromRgb(192, 192, 0)
    ACTOR_PARTIAL_COLOR_HIGHLIGHTED =           QtGui.QColor.fromRgb(212, 212, 0)
    ACTOR_REMAP_CONFLICT_COLOR =                QtGui.QColor.fromRgb(255, 140, 0)
    ACTOR_REMAP_CONFLICT_COLOR_HIGHLIGHTED =    QtGui.QColor.fromRgb(255, 192, 0)
    
    SEPARATOR_COLOR =                           QtGui.QColor.fromHsl(0, 0, 64)
    
    SELECTION_HIGHLIGHT_COLOR =                 QtGui.QColor.fromRgb(64, 96, 128)
    
    UNLOADED_IMAGE = QtGui.QImage(":/RS_warning.png")
    
    def __init__(self, cinematicEditor):
        QtWidgets.QStyledItemDelegate.__init__(self)
        
        self.cinematicEditor = cinematicEditor
    
    def paint(self, painter, option, index):
        item = self.cinematicEditor.actorList.itemFromIndex(index)
        cutsceneActor = item.data(QtCore.Qt.UserRole)
        selectedShots = self.cinematicEditor.shotTable.getSelectedShots()
        
        if self.cinematicEditor.cachedMasterSlaveFile:
            selectedShots = [shot for shot in selectedShots if self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)]
        
        if len(selectedShots) == 0:
            targetColor = self.NO_SHOT_SELECTED_COLOR
            highlightColor = self.NO_SHOT_SELECTED_COLOR_HIGHLIGHTED
        else:
            remapConflict = False
            for shot in selectedShots:
                shotCutsceneActors = shot.getCutsceneActors()
                if cutsceneActor in shotCutsceneActors:
                    shotCutsceneActors.remove(cutsceneActor)
                    for shotCutsceneActor in shotCutsceneActors:
                        if cutsceneActor.remap == shotCutsceneActor or shotCutsceneActor.remap == cutsceneActor or (shotCutsceneActor.remap == cutsceneActor.remap and cutsceneActor.remap != None):
                            targetColor = self.ACTOR_REMAP_CONFLICT_COLOR
                            highlightColor = self.ACTOR_REMAP_CONFLICT_COLOR_HIGHLIGHTED
                            remapConflict = True
                            break
                
            if not remapConflict:
                actorShots = cutsceneActor.getActorShots()
                intersection = set(actorShots).intersection(selectedShots)
                
                if len(intersection) == 0:
                    targetColor = self.ACTOR_DISABLED_COLOR
                    highlightColor = self.ACTOR_DISABLED_COLOR_HIGHLIGHTED
                elif len (intersection) == len(selectedShots):
                    targetColor = self.ACTOR_ENABLED_COLOR
                    highlightColor = self.ACTOR_ENABLED_COLOR_HIGHLIGHTED
                else:
                    targetColor = self.ACTOR_PARTIAL_COLOR
                    highlightColor = self.ACTOR_PARTIAL_COLOR_HIGHLIGHTED
        
        self.initStyleOption(option, index)
        
        option.palette.setColor(QtGui.QPalette.Text, targetColor)
        option.palette.setColor(QtGui.QPalette.HighlightedText, highlightColor)
        option.palette.setColor(QtGui.QPalette.Highlight, self.SELECTION_HIGHLIGHT_COLOR)
        
        if cutsceneActor.subActor != None:
            option.text += " ({})".format(cutsceneActor.subActor.name)
        
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_ItemViewItem, option, painter)
        
        if not ActorManager.isActorLoaded(cutsceneActor.actor):
            painter.drawImage(option.rect.x() + 2, option.rect.y() + 5, self.UNLOADED_IMAGE)
        
        separatorRect = QtCore.QRect(option.rect.x(), option.rect.y() + option.rect.height() - 1, option.rect.width(), 1)
        painter.fillRect(separatorRect, self.SEPARATOR_COLOR)


class ActorList(QtWidgets.QListWidget):
    
    def __init__(self, cinematicEditor):
        QtWidgets.QListWidget.__init__(self, parent=None)
        
        self.cinematicEditor = cinematicEditor
        
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setSelectionBehavior(QtWidgets.QListWidget.SelectRows)
        self.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setDragDropMode(QtWidgets.QTableWidget.InternalMove)
                
        self.itemChanged.connect(self.onToggleSelectedActorsActive)
        self.customContextMenuRequested.connect(self.onContextMenuRequested)
        self.itemDoubleClicked.connect(self.onItemDoubleClicked)
        
        self.contextMenuOptions = self.createContextMenuOptions()
        self.unloadedContextMenuOptions = self.createUnloadedContextMenuOptions()
        
        self.setItemDelegate(ActorListItemDelegate(self.cinematicEditor))

    # ------------------------------------
    # | Util Methods                     |
    # ------------------------------------
    
    def isSlave(self):
        return self.cinematicEditor.cachedMasterSlaveFile and not self.cinematicEditor.cachedMasterSlaveFile.isMaster()
    
    # ------------------------------------
    # | Methods                          |
    # ------------------------------------

    def reload(self): 
        signalsBlocked = self.blockSignals(True)
        
        self.clear()
        
        cutscene = CinematicEditor.getCutscene()
        if cutscene != None:        
            cutsceneActors = cutscene.getCutsceneActors()
            for cutsceneActor in cutsceneActors:
                actorItem = QtWidgets.QListWidgetItem()
                actorItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
                actorItem.setData(QtCore.Qt.UserRole, cutsceneActor)
                
                actorItem.setSizeHint(QtCore.QSize(0, 21))
                font = actorItem.font()
                font.setPointSize(9)
                #font.setBold(True)
                actorItem.setFont(font)
                
                self.addItem(actorItem)

        self.blockSignals(signalsBlocked)
            
        self.refresh()

    def refresh(self):
        cutscene = CinematicEditor.getCutscene()
        if cutscene == None:
            return
        
        signalsBlocked = self.blockSignals(True)
        
        cutsceneActors = cutscene.getCutsceneActors()
        for i in range(self.count()):
            actorItem = self.item(i)
            cutsceneActor = actorItem.data(QtCore.Qt.UserRole)
            actorItem.setText("{}{}".format(cutsceneActor.actor.getNamespace(), "*" if cutsceneActor.remap != None else ""))
            actorItem.setCheckState(QtCore.Qt.Checked if cutsceneActor.active and ActorManager.isActorLoaded(cutsceneActor.actor) else QtCore.Qt.Unchecked)
            
            toolTipText = ""
            if cutsceneActor.remap != None:
                toolTipText += "<p>Remapped to: <b>{}</b></p>".format(cutsceneActor.remap.actor.getNamespace())
            else:
                remappedActors = ["<br><b>{}</b>".format(actorRemap.actor.getNamespace()) for actorRemap in cutsceneActors if actorRemap.remap == cutsceneActor]
                if len(remappedActors) > 0:
                    toolTipText += "<p>Remapped from:{}</p>".format("".join(remappedActors))
            if ActorManager.isActorLoaded(cutsceneActor.actor):
                toolTipText += "<p>Cutscene actor. The checkbox indicates if the actor should be exported on the current sesion.</p>"
            else:
                toolTipText += "<p><b>WARNING:</b> The Actor is unloaded, certain features will be disabled. To load the actor select the \"Load Actor\" option on the Right-Click menu.</p>"
            toolTipText += "<p>Double Click: Enables/disables the actor on the selected shots.</p>"
            actorItem.setToolTip(toolTipText)
            
        self.blockSignals(signalsBlocked)
        
        self.viewport().update()

    def getSelectedRows(self):
        selectedRows = self.selectionModel().selectedRows()
        selectedRows = [index.row() for index in selectedRows]
        selectedRows.sort()
        return selectedRows

    def getSelectedCutsceneActors(self):
        selectedRows = self.getSelectedRows()
        return [self.item(row).data(QtCore.Qt.UserRole) for row in selectedRows]

    def selectCutsceneActors(self, cutsceneActors, scrollToLast=False):
        selectionModel = self.selectionModel()
        self.clearSelection()
        lastSelectedItem = None
        for i in range(self.count()):
            item = self.item(i)
            if item.data(QtCore.Qt.UserRole) in cutsceneActors:
                selectionModel.select(self.indexFromItem(item), QtCore.QItemSelectionModel.Rows | QtCore.QItemSelectionModel.Select)
                lastSelectedItem = item
                
        if scrollToLast and lastSelectedItem is not None:
            self.scrollToItem(lastSelectedItem)

    def mergeActor(self, arg=None):
        if self.isSlave():
            result = QtWidgets.QMessageBox.question(self, "Merge Actor", "Slaves cannot add new actors to the cutscene, but you can remap a new actor to an existing one. Do you want to merge an actor and remap it to onether one?")
            if result != QtWidgets.QMessageBox.Yes:
                return
            
            cutscene = CinematicEditor.getCutscene()
            cutsceneActors = cutscene.getCutsceneActors(nonRemapped=True) if cutscene else []
            if not cutsceneActors:
                QtWidgets.QMessageBox.warning(self, "Merge Actor", "There are no actors on the scene to remap to.")
                return
            
            cutsceneActorNames = [actor.getActorName() for actor in cutsceneActors]
            actorToRemap = QtUtils.SelectItemsDialog(self, "Remap Actor", cutsceneActors, labels=cutsceneActorNames, defaultSelection=[cutsceneActors[0]], multiSelection=False, includeNoneOption=False, okButtonText="Remap merged Actor to this").run()
            if actorToRemap:
                ActorBrowser.ActorBrowser(callback=functools.partial(self.mergeActorCallback, remapTo=actorToRemap[0]), addNumberToNamespace=True, parent=self).exec_()
            
        else:
            ActorBrowser.ActorBrowser(callback=self.mergeActorCallback, addNumberToNamespace=True, parent=self).exec_()

    def mergeActorCallback(self, importedNamespace, remapTo=None):
        if importedNamespace:
            with UndoOff(): # File merging cannot be undone
                actor = ActorManager.getActorByNameSpace(importedNamespace)
                
                cutscene = CinematicEditor.getCutscene(createIfNotExists=True)
                cutsceneActor = cutscene.createCutsceneActor(actor)
                
                if remapTo:
                    cutsceneActor.remap = remapTo
                
                self.reload()

    def addActor(self, arg=None, actors=None):
        cutscene = CinematicEditor.getCutscene()
        
        if self.isSlave():
            result = QtWidgets.QMessageBox.question(self, "Register Actor", "Slaves cannot add new actors to the cutscene, but you can remap a new actor to an existing one. Do you want to register an actor and remap it to onether one?")
            if result != QtWidgets.QMessageBox.Yes:
                return
            
            cutsceneActors = cutscene.getCutsceneActors(nonRemapped=True) if cutscene else []
            if not cutsceneActors:
                QtWidgets.QMessageBox.warning(self, "Register Actor", "There are no actors on the scene to remap to.")
                return
            
            cutsceneActorNames = [actor.getActorName() for actor in cutsceneActors]
            actorToRemap = QtUtils.SelectItemsDialog(self, "Remap Actor", cutsceneActors, labels=cutsceneActorNames, defaultSelection=[cutsceneActorNames[0]], multiSelection=False, includeNoneOption=False, okButtonText="Remap registered Actor to this").run()
            if actorToRemap:
                actorToRemap = actorToRemap[0]
            else:
                return
            
        else:
            actorToRemap = None
        
        if actors == None:
            sceneActors = Actor.Actor.getInstances()
            cutsceneActors = [cutsceneActor.actor for cutsceneActor in cutscene.getCutsceneActors()] if cutscene else []
            availableActors = [actor for actor in sceneActors if actor not in cutsceneActors]
            availableActorNames = [actor.getNamespace() for actor in availableActors]
        
            actors = QtUtils.SelectItemsDialog(self, "Add Actor", availableActors, labels=availableActorNames, multiSelection=True, includeNoneOption=False, okButtonText="Add", noItemsText="<No available Actors!>").run()
            if actors == None or actors == []:
                return
        
        if isinstance(actors, Actor.Actor):
            actors = [actors]
        
        with UndoContext("Add Actor"):
            cutscene = CinematicEditor.getCutscene(createIfNotExists=True)
            for actor in actors:
                if isinstance(actor, Actor.Actor):
                    cutsceneActor = cutscene.createCutsceneActor(actor)
                else:
                    cutsceneActor = actor
                    cutscene.addCutsceneActor(cutsceneActor)
                cutsceneActor.remap = actorToRemap
            
        self.reload()

    def renameCutsceneActor(self, cutsceneActor, newName):
        if self.isSlave() and cutsceneActor.remap == None:
            raise AssertionError("Only the Master can rename actors!")
        
        with UndoContext("Rename Actor"):
            cmds.namespace(rename=(cutsceneActor.actor.getNamespace(), newName), parent=":")
        
        self.cinematicEditor.refreshActors()

    def setCutsceneActorsEnabled(self, cutsceneActors, shots, enabled):
        with UndoContext("Set CutsceneActor Enabled"):
            for shot in shots:
                shotCutsceneActors = shot.getCutsceneActors()
                for cutsceneActor in cutsceneActors:
                    if enabled != (cutsceneActor in shotCutsceneActors):
                        if enabled:
                            shot.addCutsceneActor(cutsceneActor)
                        else:
                            shot.removeCutsceneActor(cutsceneActor)
        
        self.cinematicEditor.refreshActors()

    def duplicateCutsceneActors(self, cutsceneActors, sameShots=True, sameRemap=True, sameSubActor=True):
        if self.isSlave() and not sameRemap:
            raise AssertionError("Slaves can only duplicate remaped Actors!")
        
        for cutsceneActor in cutsceneActors:
            newNamespace = ActorManager.duplicateActorReference(cutsceneActor.actor)
            newActor = ActorManager.getActorByNameSpace(newNamespace)
            
            cutscene = cutsceneActor.getCutscene()
            newCutsceneActor = cutscene.createCutsceneActor(newActor, enableInAllShots=not sameShots)
            cutscene.setCutsceneActorIndex(newCutsceneActor, cutscene.getCutsceneActorIndex(cutsceneActor) + 1)
            
            if sameShots:
                actorShots = cutsceneActor.getActorShots()
                for shot in actorShots:
                    shot.addCutsceneActor(newCutsceneActor)
                    
            if sameRemap:
                if self.isSlave() and cutsceneActor.remap == None:
                    newCutsceneActor.remap = cutsceneActor
                else:
                    newCutsceneActor.remap = cutsceneActor.remap
                
            if sameSubActor:
                newCutsceneActor.subActor = cutsceneActor.subActor
        
        self.cinematicEditor.reloadActors()

    def removeCutsceneActors(self, cutsceneActors, delete=False):
        if self.isSlave():
            for cutsceneActor in cutsceneActors:
                if cutsceneActor.remap == None:
                    raise AssertionError("Only the Master can remove Actors!")
        
        with UndoContext("Remove CutsceneActor"):
            cutscene = CinematicEditor.getCutscene()
            for cutsceneActor in cutsceneActors:
                cutscene.removeCutsceneActor(cutsceneActor)
                if delete:
                    ActorManager.deleteActorReference(cutsceneActor.actor)
            
        self.cinematicEditor.reloadActors()

    def remapCutsceneActors(self, remappedCutsceneActors, cutsceneActorToRemap):
        if self.isSlave():
            for cutsceneActor in remappedCutsceneActors:
                if cutsceneActor.remap == None:
                    raise AssertionError("Slaves can't remap the Actors from the Master!")
            if cutsceneActorToRemap == None:
                raise AssertionError("Slaves can't unremap the Actors they have added!")
        
        if cutsceneActorToRemap != None:
            while cutsceneActorToRemap.remap != None:   # WARNING: This might cause an infinite loop if there is already a loop on the remaps.
                if cutsceneActorToRemap.remap in remappedCutsceneActors:
                    raise AssertionError("Remap would cause an infinite loop of remappings!")
                cutsceneActorToRemap = cutsceneActorToRemap.remap

        for cutsceneActor in remappedCutsceneActors:
            cutsceneActor.remap = cutsceneActorToRemap

        cutsceneActors = CinematicEditor.getCutscene().getCutsceneActors()
        for cutsceneActor in cutsceneActors:
            if cutsceneActor.remap != None and cutsceneActor.remap in remappedCutsceneActors:
                cutsceneActor.remap = cutsceneActorToRemap

        self.cinematicEditor.refreshActors()

    # ------------------------------------
    # | Drag & Drop                      |
    # ------------------------------------
    
    def createDragPixmap(self):
        selectedRows = self.getSelectedRows()[:5]
        totalHeight = 0
        for row in selectedRows:
            totalHeight += self.visualItemRect(self.item(row)).height()

        pixmap = QtGui.QPixmap.grabWidget(self)
        selectedShotsPixmap = QtGui.QPixmap(pixmap.width(), totalHeight)
        selectedShotsPixmap.fill(QtGui.QColor(0, 0, 0, 0))

        painter = QtGui.QPainter(selectedShotsPixmap)
        acumulatedHeight = 0
        for i, row in enumerate(selectedRows):
            rect = self.visualItemRect(self.item(row))
            painter.setOpacity(0.1 * (5 - i))
            painter.drawPixmap(0, acumulatedHeight, pixmap, 0, rect.y(), pixmap.width(), rect.height())
            acumulatedHeight += rect.height()
        painter.end()

        return selectedShotsPixmap
    
    # Hay que hacer hacks con mousePressEvent y mouseMoveEvent en vez de usar startDrag porque el drag and drop parace estar roto (similar a lo que le pasa a la tabla de shots, pero en este caso no tenemos columnas así que hay que usar otro enfoque)
    def mousePressEvent(self, event):
        self.pressedPosition = None
        
        if event.button() == QtCore.Qt.LeftButton:
            self.pressedPosition = event.pos()
        
        QtWidgets.QListWidget.mousePressEvent(self, event)
    
    def mouseMoveEvent(self, event):
        if self.pressedPosition != None:
            if (event.pos() - self.pressedPosition).manhattanLength() >= 5:
                self.startDrag(QtCore.Qt.MoveAction)
        else:
            QtWidgets.QTableWidget.mouseMoveEvent(self, event)

    def startDrag(self, supportedActions):
        if supportedActions & QtCore.Qt.MoveAction:
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
        if event.dropAction() == QtCore.Qt.MoveAction:
            selectedCutsceneActors = self.getSelectedCutsceneActors()
            
            targetCutsceneActor = None
            dropPos = event.pos().y()
            for i in range(self.count()):
                item = self.item(i)
                rect = self.visualItemRect(item)
                refPos = rect.y() + rect.height() / 2
                if dropPos < refPos:
                    cutsceneActor = item.data(QtCore.Qt.UserRole)
                    if cutsceneActor not in selectedCutsceneActors:
                        targetCutsceneActor = cutsceneActor
                        break
            
            with UndoContext("Reorder CutsceneActors"):
                cutscene = CinematicEditor.getCutscene()
                for cutsceneActor in selectedCutsceneActors:
                    cutscene.removeCutsceneActor(cutsceneActor, disableInAllShots=False)
                if targetCutsceneActor == None:
                    for cutsceneActor in selectedCutsceneActors:
                        cutscene.addCutsceneActor(cutsceneActor, enableInAllShots=False)
                else:
                    targetIndex = cutscene.getCutsceneActorIndex(targetCutsceneActor)
                    for i, cutsceneActor in enumerate(selectedCutsceneActors):
                        cutscene.insertCutsceneActor(cutsceneActor, targetIndex + i, enableInAllShots=False)
            
            self.cinematicEditor.reloadActors()
            self.selectCutsceneActors(selectedCutsceneActors)

    # ------------------------------------
    # | Events                           |
    # ------------------------------------

    def onToggleSelectedActorsActive(self, changedItem):
        signalsBlocked = self.blockSignals(True)

        if changedItem.isSelected():
            selectedCutsceneActors = self.getSelectedCutsceneActors()
        else:
            selectedCutsceneActors = [changedItem.data(QtCore.Qt.UserRole)]

        with UndoOff(): # We don't actually want to undo this.
            checked = changedItem.checkState() == QtCore.Qt.Checked
            for cutsceneActor in selectedCutsceneActors:
                cutsceneActor.active = checked

        self.refresh()  # No need to call the refreshActors function on the cinematicEditorWindow, since this will only affect the checkboxes on this list

        QtCore.QTimer.singleShot(0, functools.partial(self.selectCutsceneActors, selectedCutsceneActors))

        self.blockSignals(signalsBlocked)

    def onItemDoubleClicked(self, item):
        selectedShots = self.cinematicEditor.shotTable.getSelectedShots()
        if self.cinematicEditor.cachedMasterSlaveFile:
            selectedShots = [shot for shot in selectedShots if self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)]
        if len(selectedShots) == 0:
            return
        
        cutsceneActor = item.data(QtCore.Qt.UserRole)
        cutsceneActorShots = cutsceneActor.getActorShots()
        intersection = set(cutsceneActorShots).intersection(selectedShots)
        isActive = len(intersection) == len(selectedShots)
        
        with UndoContext("Set CutsceneActor Enabled"):
            for shot in selectedShots:
                if isActive:
                    shot.removeCutsceneActor(cutsceneActor)
                else:
                    shot.addCutsceneActor(cutsceneActor)
                
        self.refresh()
        
    def onContextMenuRequested(self, pos):
        clickedItem = self.itemAt(pos)
        if clickedItem is not None:
            if not clickedItem.isSelected():
                self.selectRow(self.indexFromItem(clickedItem).row())
                
            selectedCutsceneActors = self.getSelectedCutsceneActors()
            contextMenuToDisplay = self.contextMenuOptions
            for cutsceneActor in selectedCutsceneActors:
                if not ActorManager.isActorLoaded(cutsceneActor.actor):
                    contextMenuToDisplay = self.unloadedContextMenuOptions
                    break
            
            QtUtils.showContextMenu(contextMenuToDisplay, self, QtGui.QCursor.pos(), multiSelection=len(selectedCutsceneActors) > 1)

    # ------------------------------------
    # | Context Menu                     |
    # ------------------------------------

    def createContextMenuOptions(self):
        return [
            QtUtils.MenuOption("selectActorControl",    "Select Actor Control",         True,  self.onSelectActorControlOptionSelected, "Selects the actor's master control."),
            None,
            QtUtils.MenuOption("renameActor",           "Rename Actor",                 False, self.onRenameActorOptionSelected, "Rename the actor. The name must be unique."),
            None,
            QtUtils.MenuOption("enableActor",           "Enable Selected Actors",       True,  self.onEnableActorOptionSelected, "<p>Enables the selected Actors for export on the selected Shots.</p><p>Whn exporting, Actors marked <span style=\"color: rgb(0,200,0)\">Green</span> on a Shot <b>will be exported</b>.</p>"),
            QtUtils.MenuOption("disableActor",          "Disable Selected Actors",      True,  self.onDisableActorOptionSelected, "<p>Disables the selected Actors for export on the selected Shots.</p><p>Whn exporting, Actors marked <span style=\"color: rgb(200,0,0)\">Red</span> on a Shot <b>will NOT be exported</b>.</p>"),
            None,
            QtUtils.MenuOption("exportActor",           "Export Selected Actors",       True,  subMenus=
            [
                QtUtils.MenuOption("exportActorAll",        "All Shots",                    True,   self.onExportActorForAllShotsOptionSelected, "<p>Export the selected Actors on <b>all Shots</b> (even if their checkmarks are unmarked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                QtUtils.MenuOption("exportActorMarked",     "Marked Shots",                 True,   self.onExportActorForMarkedShotsOptionSelected, "<p>Export the selected Actors on the <b>marked Shots</b> (those whose checkmark is marked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
                QtUtils.MenuOption("exportActorSelected",   "Selected Shots",               True,   self.onExportActorForSelectedShotsOptionSelected, "<p>Export the selected Actors on the <b>selected Shots</b> (even if their checkmarks are unmarked).</p><p>Only the Actors enabled on each Shot will be exported.</p>"),
            ]),
            None,
            QtUtils.MenuOption("loadActor",             "Load Selected Actors",         True,  self.onLoadActorOptionSelected, "Loads the selected Actors Reference (if some of them were already loaded, skips them)."),
            QtUtils.MenuOption("unloadActor",           "Unload Selected Actors",       True,  self.onUnloadActorOptionSelected, "<p>Unloads the selected Actors Reference (if some of them were already unloaded, skips them).</p><p><b>NOTE</b>: If an Actor is asked to be exported, it will be automatically loaded.</p><p><b>WARNING</b>: Some operations cannot be performed when an actor is unloaded.</p>"),
            None,
            QtUtils.MenuOption("selectSubActor",        "Select SubActor",              False, self.onSelectSubActorOptionSelected, "Selects which SubActor will be used by the Actor."),
            None,
            QtUtils.MenuOption("remapActor",            "Remap Selected Actors",        True,  self.onRemapActorOptionSelected, "<p>Remaps the selected Actors to another.</p><p>When an actor is remapped, it will be exported with the name of another. Use this to have multiple copies of the actor to aid you on the animation process.</p><p><b>NOTE</b>: Only one remapped Actor can be marked for export on each Shot at the same time. If there are multiple marked, they will be shown in <span style=\"color: rgb(255,100,0)\">Orange</span> and you won't be able to export them.</p>"),
            None,
            QtUtils.MenuOption("duplicateActor",        "Duplicate Selected Actors",    True,  self.onDuplicateActorOptionSelected, "<p>Duplicates the selected Actors. Their animation will not be copied.</p><p><b>WARNING</b>: Actor duplication cannot be undone, since it involves duplicating a reference.</p>"),
             None,
            QtUtils.MenuOption("unregisterActor",       "Unregister Selected Actors",   True,  self.onUnregisterActorOptionSelected, "<p>Unregisters the selected Actors. These actors will no longer be part of the Cutscene, but they will remain on the scene.</p><p><b>WARNING</b>: You can add the unregistered actors back to the Cutscene, but they will lose their remap information, their SubActor selection and the information regarding which Shots the Actors should be exported on.</p>"),
            #None,
            #QtUtils.MenuOption("deleteActor",           "Delete Selected Actor",        True,  self.onDeleteActorOptionSelected, "<p>Deletes the selected actors. They will be completely deleted from the scene.</p><p><span style=\"font-weight: bold; color: rgb(200, 0, 0);\">EXTREME CAUTION</span>: Deleting an Actor <b>CANNOT BE UNDONE</b>. Make sure you really want to delete the Actor and have previously saved the file.</p>")  # Deleting an actor is not undoable so it's very dangerous. We hide this option son it doesn't cause trouble.
        ]
        
    def createUnloadedContextMenuOptions(self):
        return [
            self.contextMenuOptions[4],  # Enable Selected Actors
            self.contextMenuOptions[5],  # Disable Selected Actors
            None,
            self.contextMenuOptions[7],  # Export Selected Actors
            None,
            self.contextMenuOptions[9],  # Load Selected Actors
            self.contextMenuOptions[10], # Unload Selected Actors
            None,
            self.contextMenuOptions[16], # Unregister Selected Actors
        ]

    def onSelectActorControlOptionSelected(self):
        selectedActors = self.getSelectedCutsceneActors()
        masters = [actor.actor.rig.mainControl for actor in selectedActors]
        cmds.select(masters)
    
    def onRenameActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) != 1:
            raise AssertionError("Unable to rename Actor: You can only rename one actor at a time!")
        
        cutsceneActor = selectedCutsceneActors[0]
        
        if self.isSlave():
            if cutsceneActor.remap == None:
                QtWidgets.QMessageBox.warning(self, "Rename Actor", "Only the Master can rename Actors. You can still rename actors you are using for remapping.")
                return
            
        actorName = cutsceneActor.actor.getNamespace()
        newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor", "Enter new actor name:", text=actorName)
        
        while True:
            if not ok or not newName or newName == actorName:
                return
            elif ActorManager.isActorNameInUse(newName):
                newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor","The actor name [{}] is already in use.\nPlease enter a new one.".format(newName), text=actorName)
            elif ActorManager.isNamespaceInUse(newName):
                newName, ok = QtWidgets.QInputDialog.getText(self, "Rename Actor","There is already a namespace with the name [{}].\nPlease enter a new actor name that doesn't correspond to an existing namespace.".format(newName), text=actorName)
            else:
                break
        
        self.renameCutsceneActor(selectedCutsceneActors[0], newName)

    def onEnableActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to set Actor enabled: At least one actor must be selected!")
        
        shots = self.cinematicEditor.shotTable.getSelectedShots()
        if self.cinematicEditor.cachedMasterSlaveFile:
            shots = [shot for shot in shots if self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)]
        
        if len(shots) == 0:
            QtWidgets.QMessageBox.information(self, "Set Actors Enabled", "You must select at least one shot to enable or disable the actors on it.")
        else:
            self.setCutsceneActorsEnabled(selectedCutsceneActors, shots, True)
    
    def onDisableActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to set Actor enabled: At least one actor must be selected!")
        
        shots = self.cinematicEditor.shotTable.getSelectedShots()
        if self.cinematicEditor.cachedMasterSlaveFile:
            shots = [shot for shot in shots if self.cinematicEditor.cachedMasterSlaveFile.ownsShot(shot)]
        
        if len(shots) == 0:
            QtWidgets.QMessageBox.information(self, "Set Actors Enabled", "You must select at least one shot to enable or disable the actors on it.")
        else:
            self.setCutsceneActorsEnabled(selectedCutsceneActors, shots, False)

    def onExportActorForAllShotsOptionSelected(self):
        selectedActors = self.getSelectedCutsceneActors()
        if selectedActors:
            cutscene = selectedActors[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=cutscene.getShots(), actors=selectedActors, forceShots=True, forceActors=True)
            
    def onExportActorForMarkedShotsOptionSelected(self):
        selectedActors = self.getSelectedCutsceneActors()
        if selectedActors:
            cutscene = selectedActors[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=cutscene.getShots(), actors=selectedActors, forceShots=False, forceActors=True)
            
    def onExportActorForSelectedShotsOptionSelected(self):
        selectedActors = self.getSelectedCutsceneActors()
        selectedShots = self.cinematicEditor.shotTable.getSelectedShots()
        if selectedActors and selectedShots:
            cutscene = selectedActors[0].getCutscene()
            exportDialog = CinematicExportDialog.CinematicExportDialog(self, cutscene)
            exportDialog.export(shots=selectedShots, actors=selectedActors, forceShots=True, forceActors=True)
            
    def onLoadActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to load Actor: At least one actor must be selected!")
        
        for cutsceneActor in selectedCutsceneActors:
            ActorManager.loadActorReference(cutsceneActor.actor) # There is no need to reload the actors, loading or unloading an actor reference will cause this tool to update.

    def onUnloadActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to unload Actor: At least one actor must be selected!")
        
        for cutsceneActor in selectedCutsceneActors:
            ActorManager.unloadActorReference(cutsceneActor.actor) # There is no need to reload the actors, loading or unloading an actor reference will cause this tool to update.

    def onSelectSubActorOptionSelected(self):
        if self.isSlave():
            QtWidgets.QMessageBox.warning(self, "Select Sub Actor", "Only the Master can select the SubActor for an Actor.")
            return
        
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) != 1:
            raise AssertionError("Unable to select SubActor: You can only select the SubActor for one actor at a time!")
        
        cutsceneActor = selectedCutsceneActors[0]
        subActors = cutsceneActor.actor.getSubActors()
        subActors = [subActor for subActor in subActors if subActor.Tags.Model in subActor.tags]
        subActorNames = [subActor.name for subActor in subActors]
        defaultSelection = [cutsceneActor.subActor] if cutsceneActor.subActor != None else None
        
        selectedSubActor = QtUtils.SelectItemsDialog(self, "Select SubActor", subActors, labels=subActorNames, defaultSelection=defaultSelection, multiSelection=False, includeNoneOption=True, okButtonText="Select", noItemsText="<No available SubActors!>", noneItemText="<No SubActor>").run()
        if selectedSubActor != None:
            if len(selectedSubActor) == 1:
                selectedSubActor = selectedSubActor[0]
            else:
                selectedSubActor = None

            cutsceneActor.subActor = selectedSubActor

    def onRemapActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to remap Actor: At least one actor must be selected!")
        
        if self.isSlave():
            for cutsceneActor in selectedCutsceneActors:
                if cutsceneActor.remap == None:
                    QtWidgets.QMessageBox.warning(self, "Remap Actor", "Actors defined by the Master cannot be remapped. You can still remap any Actor local to this file.")
                    return
        
        cutscene = CinematicEditor.getCutscene()
        cutsceneActors = cutscene.getCutsceneActors(nonRemapped=True)
        availableActors = [cutsceneActor.actor for cutsceneActor in cutsceneActors if cutsceneActor not in selectedCutsceneActors]
        availableActorNames = [actor.getNamespace() for actor in availableActors]
        
        defaultSelection = None
        for cutsceneActor in selectedCutsceneActors:
            if cutsceneActor.remap != None:
                defaultSelection = [cutsceneActor.remap.actor]
                break
        
        actorToRemap = QtUtils.SelectItemsDialog(self, "Remap Actor", availableActors, labels=availableActorNames, defaultSelection=defaultSelection, multiSelection=False, includeNoneOption=(not self.isSlave()), okButtonText="Remap", noItemsText="<No available Actors!>", noneItemText="<No Actor>").run()
        if actorToRemap != None:
            if len(actorToRemap) == 1:
                actorToRemap = cutscene.getCutsceneActorFromActor(actorToRemap[0])
            else:
                if not self.isSlave():
                    actorToRemap = None
                else:
                    raise AssertionError("Slaves can't have unremapped actors!")
            
            self.remapCutsceneActors(selectedCutsceneActors, actorToRemap)

    def onDuplicateActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        
        if self.isSlave():
            for cutsceneActor in selectedCutsceneActors:
                if cutsceneActor.remap == None:
                    result = QtWidgets.QMessageBox.question(self, "Duplicate Actor", "You are trying to duplicate an Actor owned by the Master. Slaves can't create new actors, so the copy will be remapped to the original Actor, proceed?")
                    if result != QtWidgets.QMessageBox.Yes:
                        return
                    break
        
        self.duplicateCutsceneActors(selectedCutsceneActors)

    def onUnregisterActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to unregister Actors: At least one actor must be selected!")
        
        if self.isSlave():
            for cutsceneActor in selectedCutsceneActors:
                if cutsceneActor.remap == None:
                    QtWidgets.QMessageBox.warning(self, "Unregister Actors", "Only the Master can unregister the cutscene's Actors. You can still unregister the local Actors you have created.")
                    return
                
        if QtWidgets.QMessageBox.question(self, "Unregister Actors", "By unregistering the actors they will no longer participate on the cutscene but will remain on the file. Are you sure you want to unregister the selected actors?") == QtWidgets.QMessageBox.Yes:
            self.removeCutsceneActors(selectedCutsceneActors, delete=False)
    
    def onDeleteActorOptionSelected(self):
        selectedCutsceneActors = self.getSelectedCutsceneActors()
        if len(selectedCutsceneActors) == 0:
            raise AssertionError("Unable to delete Actors: At least one actor must be selected!")
        
        if self.isSlave():
            for cutsceneActor in selectedCutsceneActors:
                if cutsceneActor.remap == None:
                    QtWidgets.QMessageBox.warning(self, "Delete Actors", "Only the Master can delete the cutscene's Actors. You can still delete the local Actors you have created.")
                    return
                
        actorList = ""
        for cutsceneActor in selectedCutsceneActors:
            actorList += "\n- {}".format(cutsceneActor.actor.getNamespace())
        if QtWidgets.QMessageBox.question(self, "Unregister Actors", "This will delete the actors and all thier nodes from the the file. Are you sure you want to deletes the selected actors?\n\nWARNING: THIS OPERATION CANNOT BE UNDONE.\n{}".format(actorList)) == QtWidgets.QMessageBox.Yes:
            self.removeCutsceneActors(selectedCutsceneActors, delete=True)
