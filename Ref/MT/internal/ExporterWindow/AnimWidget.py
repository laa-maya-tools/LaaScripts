from PySide2 import QtCore, QtWidgets, QtGui

import QtCustomWidgets.UIFileWidget as UIFileWidget
import QtCustomWidgets.QtUtils as Utils
import QtCustomWidgets.DecimalDetectorSpinBox as DecimalDetectorSpinBox
import ProjectPath
from Utils.Maya.UndoContext import UndoContext

import ActorManager
import ActorManager.SubActor as SubActor
import ActorManager.Actor as Actor
import ActorManager.CameraSet as CameraSet
import ActorManager.AnimPreset as AnimPreset

import maya.cmds as cmds

import os
from functools import partial

# This class is used to substitute a SpinBox defined on the UI file with a custom one
class QCustomSpinBox(DecimalDetectorSpinBox.DecimalDetectorSpinBox):
    
    def __init__(self, originalSpinBox : QtWidgets.QSpinBox):
        super().__init__()
        
        layout : QtWidgets.QBoxLayout = originalSpinBox.parent().layout()
        layout.insertWidget(layout.indexOf(originalSpinBox), self)
        layout.removeWidget(originalSpinBox)
        originalSpinBox.deleteLater()
        
        self.setObjectName(originalSpinBox.objectName())
        
        # QWidget Properties (NOTE: These are not all the properties, only the ones relevant to AnimWidget)
        self.setSizePolicy(originalSpinBox.sizePolicy())
        self.setMinimumSize(originalSpinBox.minimumSize())
        self.setMaximumSize(originalSpinBox.maximumSize())
        
        # QSpinBox Properties (NOTE: These are not all the properties, only the ones relevant to AnimWidget)
        self.setMinimum(originalSpinBox.minimum())
        self.setMaximum(originalSpinBox.maximum())
        self.setSingleStep(originalSpinBox.singleStep())


class AnimWidget(UIFileWidget.UIFileWidget):

    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------
    
    def __init__(self, animPreset, animationTab, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ExporterWindow/ui/animWidget.ui", parent=parent)

        # Stores the exporter window
        self.animationTab = animationTab

        # Sets the widget icon. It must be set here and not on the UI file since the icon path may change.
        self.ui.Lbl_CharIcon.setPixmap(QtGui.QPixmap(os.path.join(ProjectPath.getToolsFolder(), r"ExporterWindow/images/animation-icon.png")))
        self.ui.Lbl_CamIcon.setPixmap(QtGui.QPixmap(os.path.join(ProjectPath.getToolsFolder(), r"ExporterWindow/images/camera-icon.png")))

        # Properties for the selection state
        self._selected = False
        self._basePalette = self.ui.palette()
        self._selectedPalette = self.createSelectedPalette(self._basePalette)
        self._baseLayerPalette = self.ui.Btn_Layers.palette()

        # Adittional Configuration
        self.namePartValidator = QtGui.QRegExpValidator(QtCore.QRegExp("^[0-9a-z_-{}]*$"), self)
        
        # SPAGUETTI: We need to override the WheelEvent of the SpinBox so they don't catch wheel events.
        # But we can't do that if they were created on QtDesigner, so we have to  override them.
        self.ui.Spn_Start = QCustomSpinBox(self.ui.Spn_Start)
        self.ui.Spn_End = QCustomSpinBox(self.ui.Spn_End)

        # Widget event configuration
        self.setAcceptDrops(True)
        #self.ui.Spn_Start.setAttribute(QtCore.Qt.WA_NoMousePropagation)
        self.ui.Spn_Start.setFocusPolicy(QtCore.Qt.ClickFocus)
        #self.ui.Spn_End.setAttribute(QtCore.Qt.WA_NoMousePropagation)
        self.ui.Spn_End.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ui.Obj_ObjName.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.ui.Btn_Layers.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # Signals
        self._signalsBlocked = False
        self.ui.Ckb_Export.toggled.connect(self.onMarkedForExportToggled)
        self.ui.Btn_EditName.clicked.connect(self.onNameButtonClicked)
        self.ui.Btn_BrowseExport.clicked.connect(self.onBrowseExportPathClicked)
        self.ui.Spn_Start.valueChanged.connect(self.onStartChanged)
        self.ui.Spn_End.valueChanged.connect(self.onEndChanged)
        self.ui.Chk_Loop.toggled.connect(self.onLoopToggled)
        self.ui.Chk_Mirror.toggled.connect(self.onMirrorToggled)
        self.ui.Chk_Pose.toggled.connect(self.onPoseToggled)
        self.ui.Btn_Delete.clicked.connect(self.onDeleteButtonClicked)

        # Loads the information from the anim preset
        self.setAnimPreset(animPreset)

    def createSelectedPalette(self, basePalette):
        selectedPalette = QtGui.QPalette(basePalette)
        selectedPalette.setColor(QtGui.QPalette.Window, QtGui.QColor.fromRgb(130,155,155))
        return selectedPalette

    def createNamePartWidget(self, namePart):
        namePartWidget = QtWidgets.QLineEdit()
        namePartWidget.setText(namePart)
        namePartWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        namePartWidget.setValidator(self.namePartValidator)
        namePartWidget.customContextMenuRequested.connect(self.showNamePartContextMenu)
        namePartWidget.returnPressed.connect(self.onNamePartReturnPressed)
        namePartWidget.textEdited.connect(self.onNamePartTextEdited)
        return namePartWidget

    # ------------------------------------
    # | Widget Utils                     |
    # ------------------------------------

    def setWidgetIconVisibility(self, visible):
        actorType = self.animPreset.getHolder()._Type
        self.ui.Lbl_CharIcon.setVisible(visible and (actorType == Actor.Actor._Type))
        self.ui.Lbl_CamIcon.setVisible(visible and (actorType == CameraSet.CameraSet._Type))

    def setLayerColor(self, color):
        newPalette = QtGui.QPalette(self._baseLayerPalette)
        newPalette.setColor(QtGui.QPalette.Button, color)
        self.ui.Btn_Layers.setPalette(newPalette)

    def clearLayerColor(self):
        self.ui.Btn_Layers.setPalette(self._baseLayerPalette)

    def getNamePartWidgetIndex(self, namePartWidget):
        namePartsLayout =  self.ui.Stk_EditName.widget(1).layout()
        for i in range(namePartsLayout.count()):
            if namePartWidget == namePartsLayout.itemAt(i).widget():
                return i
        return -1

    def refreshAnimWidget(self):
        with Utils.BlockSignals(self):
            self.ui.Ckb_Export.setChecked(self.animPreset.active)
            self.ui.Btn_EditName.setText(self.animPreset.getConcatenatedName())
            self.ui.Spn_Start.setValue(self.animPreset.start)
            self.ui.Spn_End.setValue(self.animPreset.end)
            self.ui.Chk_Loop.setChecked(self.animPreset.loop)
            self.ui.Chk_Mirror.setChecked(self.animPreset.mirror)
            self.ui.Chk_Pose.setChecked(self.animPreset.pose)

        self.setEnabled(self.animPreset.enabled, updateAnimPreset=False)
        self.setPath(self.animPreset.path, updateAnimPreset=False)
        self.setSubHolder(self.animPreset.subHolder, updateAnimPreset=False)
        
        # Creates the context menus
        self._normalContextMenuOptions = self.createNormalContextMenuOptions()
        self._namePartContextMenuOptions = self.createNamePartContextMenuOptions()
        
    def refreshNameParts(self):
        # Clears the widgets
        namePartsLayout =  self.ui.Stk_EditName.widget(1).layout()
        while namePartsLayout.count() > 0:
            namePartsLayout.takeAt(0)

        # Creates a widget for every name part
        nameParts = self.animPreset.getNameParts()
        for namePart in nameParts:
            self.insertNamePart(text=namePart, updateAnimPreset=False, propagateToSameHolder=False)

    def createDragPixmap(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()

        pixmap = QtGui.QPixmap.grabWidget(self)
        lineCount = min(5, len(selectedAnimWidgets))
        selectedAnimWidgetsPixmap = QtGui.QPixmap(pixmap.width(), pixmap.height() * lineCount)
        selectedAnimWidgetsPixmap.fill(QtGui.QColor(0, 0, 0, 0))

        painter = QtGui.QPainter(selectedAnimWidgetsPixmap)
        for i, animWidget in enumerate(selectedAnimWidgets):
            tempPixmap = pixmap if animWidget == self else QtGui.QPixmap.grabWidget(animWidget)
            painter.setOpacity(0.1 * (5 - i))
            painter.drawPixmap(0, i * pixmap.height(), tempPixmap)
        painter.end()

        return selectedAnimWidgetsPixmap

    def getPathTokenizer(self):
        pathTokenizer = self.animPreset.getPathTokenizer(branch=None)
        pathTokenizer = self.animationTab.exporterWindow.getPathTokenizer(pathTokenizer=pathTokenizer)
        return pathTokenizer

    # ------------------------------------
    # | Methods                          |
    # ------------------------------------

    def setAnimPreset(self, animPreset, refreshAnimWidget=True):
        self.animPreset = animPreset
        if refreshAnimWidget:
            self.refreshAnimWidget()

    def setSubHolder(self, subHolder, updateAnimPreset=True):
        if subHolder != None:
            self.ui.Obj_ObjName.setText(subHolder.getDisplayName())
            #self.ui.Obj_ObjName.setText("{1} -> {0}".format(subHolder.getDisplayName(), self.animPreset.getHolder().getDisplayName()))   # TODO: A way to represent both the holder and subHolder could be usefull, but currently there is not enough space on the UI for this
        else:
            self.ui.Obj_ObjName.setText(self.animPreset.getHolder().getDisplayName())

        if updateAnimPreset:
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animPreset.subHolder = subHolder

        self.setColor(self.animPreset.color, updateAnimPreset=False)    # Used to update the background color

    def isEnabled(self):
        return self.animPreset.enabled

    def setEnabled(self, enabled, updateAnimPreset=True):
        with Utils.BlockSignals(self):
            self.ui.Ckb_Export.setEnabled(enabled)
            if not enabled or not self.animPreset.enabled:
                self.ui.Ckb_Export.setChecked(enabled)
        if updateAnimPreset:
            with UndoContext("Set Anim Preset Enabled"):
                self.animPreset.enabled = enabled
                self.animPreset.active = enabled    # We purposefully override the active state (marked for export) on enable/disable to avoid confusion
        self.setColor(self.animPreset.color, updateAnimPreset=False)

    def isMarkedForExport(self):
        return self.isEnabled() and self.animPreset.active

    def setMarkedForExport(self, markedForExport, updateUI=True):
        if self.isEnabled():
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animPreset.active = markedForExport
            if updateUI:
                with Utils.BlockSignals(self):
                    self.ui.Ckb_Export.setChecked(markedForExport)

    def setPath(self, path, updateAnimPreset=True):
        if path and not path.endswith(os.path.sep):
            path += os.path.sep
        if updateAnimPreset:
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animPreset.path = path
            path = self.animPreset.path # If the path is empty, this will make the animpreset return the default path
        self.ui.Led_Path.setText(self.getPathTokenizer().Translate(path))
        self.ui.Led_Path.setToolTip(path + "\n\nExpands to:\n" + self.ui.Led_Path.text())

    def setColor(self, color, updateAnimPreset=True):
        if type(color) is tuple:
            color = QtGui.QColor(color[0], color[1], color[2])

        baseColor = None
        textColor = None
        backgroundColor = None
        if self.animPreset.enabled:
            baseColor = color
            if self.animPreset.subHolder == None:
                backgroundColor = QtGui.QColor(32, 64, 128)
            else:
                backgroundColor = QtGui.QColor(192, 32, 64)
            if 0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue() > 150:
                textColor = QtGui.QColor(0 ,0, 0)
            else:
                textColor = QtGui.QColor(255, 255, 255)
        else:
            hslColor = color.getHsl()
            baseColor = QtGui.QColor()
            baseColor.setHsl(hslColor[0], 0.5 * hslColor[1],  0.8 * hslColor[2], hslColor[3])
            backgroundColor = QtGui.QColor(32, 32, 32)
            if 0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue() > 150:
                textColor = QtGui.QColor(92 ,92, 92)
            else:
                textColor = QtGui.QColor(154, 154, 154)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Base, baseColor)
        palette.setColor(QtGui.QPalette.Background, backgroundColor)
        palette.setColor(QtGui.QPalette.Text, textColor)
        self.ui.Obj_ObjName.setPalette(palette)

        if updateAnimPreset:
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animPreset.color = [color.red(), color.green(), color.blue()]

    def setLayerState(self, animLayer, active, updateUI=False):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        if active:
            self.animPreset.addAnimLayer(animLayer)
        else:
            self.animPreset.removeAnimLayer(animLayer)
        
        if updateUI:
            self.animationTab.refreshLayerPanel()
        else:
            self.animationTab.ui.Tbl_AnimList.viewport().update()

    def setStart(self, start, updateUI=True):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.start = start
        if updateUI:
            with Utils.BlockSignals(self):
                self.ui.Spn_Start.setValue(start)

    def setEnd(self, end, updateUI=True):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.end = end
        if updateUI:
            with Utils.BlockSignals(self):
                self.ui.Spn_End.setValue(end)

    def setLoop(self, loop, updateUI=True):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.loop = loop
        if updateUI:
            with Utils.BlockSignals(self):
                self.ui.Chk_Loop.setChecked(loop)

    def setMirror(self, mirror, updateUI=True):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.mirror = mirror
        if updateUI:
            with Utils.BlockSignals(self):
                self.ui.Chk_Mirror.setChecked(mirror)

    def setPose(self, pose, updateUI=True):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.pose = pose
        if updateUI:
            with Utils.BlockSignals(self):
                self.ui.Chk_Pose.setChecked(pose)

    # Selection --------------------------

    def isSelected(self):
        return self._selected

    def setSelected(self, selected):
        if selected != self._selected:
            self._selected = selected
            self.ui.setPalette(self._selectedPalette if selected else self._basePalette)

        if not selected:
            self.ui.Led_Path.deselect()
            self.ui.Led_Path.setCursorPosition(len(self.ui.Led_Path.text()))

    # Name Parts -------------------------

    def getNamePartEditMode(self):
        return self.ui.Stk_EditName.currentIndex() == 1

    def setNamePartEditMode(self, editMode, propagateToSameHolder=True):
        self.ui.Stk_EditName.setCurrentIndex(1 if editMode else 0)
        if editMode:
            self.refreshNameParts()
        else:
            self.ui.Btn_EditName.setText(self.animPreset.getConcatenatedName())
        
        if propagateToSameHolder:
            animWidgets = self.animationTab.getAnimWidgets()
            for animWidget in animWidgets:
                if animWidget != self:
                    animWidget.setNamePartEditMode(editMode and (animWidget.animPreset.getHolder() == self.animPreset.getHolder()), propagateToSameHolder=False)

    def setNamePart(self, namePart, index, updateAnimPreset=True, keepCursorPosition=False):
        namePartsLayout = self.ui.Stk_EditName.widget(1).layout()
        namePartWidget = namePartsLayout.itemAt(index).widget()
        
        if keepCursorPosition:
            cursorPosition = namePartWidget.cursorPosition()
            
        namePartWidget.setText(namePart)
        
        if keepCursorPosition:
            namePartWidget.setCursorPosition(cursorPosition)
        
        if updateAnimPreset:
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animPreset.setNamePartByIndex(namePart, index)

    def deleteNamePart(self, index, updateAnimPreset=True, propagateToSameHolder=True):
        with UndoContext("Delete Name Part"):
            namePartsLayout = self.ui.Stk_EditName.widget(1).layout()
            namePartWidget = namePartsLayout.takeAt(index).widget()
            #namePartWidget.setVisible(False)   # This causes the area to scroll to the last item, so we avoid doing it
            namePartWidget.deleteLater()
            if updateAnimPreset:
                nameParts = self.animPreset.getNameParts()
                nameParts.pop(index)
                self.animPreset.setNameParts(nameParts)

            if propagateToSameHolder:
                animWidgets = self.animationTab.getAnimWidgetsByHolder(self.animPreset.getHolder())
                for animWidget in animWidgets:
                    if animWidget != self:
                        animWidget.deleteNamePart(index, updateAnimPreset=updateAnimPreset, propagateToSameHolder=False)

    def insertNamePart(self, index=-1, text="", updateAnimPreset=True, propagateToSameHolder=True):
        with UndoContext("Insert Name Part"):
            namePartsLayout = self.ui.Stk_EditName.widget(1).layout()
            namePartsLayout.insertWidget(index, self.createNamePartWidget(text))
            if updateAnimPreset:
                nameParts = self.animPreset.getNameParts()
                nameParts.insert(index, text)
                self.animPreset.setNameParts(nameParts)

            if propagateToSameHolder:
                animWidgets = self.animationTab.getAnimWidgetsByHolder(self.animPreset.getHolder())
                for animWidget in animWidgets:
                    if animWidget != self:
                        animWidget.insertNamePart(index, updateAnimPreset=updateAnimPreset, propagateToSameHolder=False)

    # Other ------------------------------

    def applyAnimationConfiguration(self, animRange=None, goTo=None, animLayers=None, selectLastLayer=None, combine=False):
        if animRange == None:
            animRange = self.animationTab.isSetRangeOptionEnabled()
        if goTo == None:
            goTo = self.animationTab.getGoToOption().lower()
        if animLayers == None:
            animLayers = self.animationTab.isSetLayersOptionEnabled()
        if selectLastLayer == None:
            selectLastLayer = self.animationTab.isSelectLastLayerOptionEnabled()
            
        with UndoContext("Apply AnimPreset Configuration"):
            if animRange:
                self.animPreset.applyAnimRange(goTo=goTo, combine=combine)
            if animLayers:
                self.animPreset.applyAnimLayers(selectLastLayer=selectLastLayer, combine=combine)

    def setAnimationConfigurationFromScene(self, animRange=True, animLayers=True):
        with UndoContext("Set AnimPreset Configuration From Scene"):
            if animRange:
                self.animPreset.start = cmds.playbackOptions(q=True, ast=True)
                self.animPreset.end = cmds.playbackOptions(q=True, aet=True)
            if animLayers:
                animLayers = self.animPreset.getHolder().getAnimLayers()
                activeAnimLayers = [animLayer for animLayer in animLayers if not cmds.animLayer(animLayer, q=True, m=True)]
                layerWeights = [cmds.getAttr("{}.weight".format(animLayer)) for animLayer in activeAnimLayers]
                self.animPreset.setAnimLayers(activeAnimLayers, layerWeights)

    # ------------------------------------
    # | Widget Callbacks                 |
    # ------------------------------------

    def onMarkedForExportToggled(self, state):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset Active"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setMarkedForExport(state, updateUI=(animWidget != self))
                else:
                    self.setMarkedForExport(state, updateUI=False)

    def onNameButtonClicked(self):
        if not self._signalsBlocked:
            if not self.isSelected():
                self.animationTab.selectAnimWidgets([self])
            self.animationTab.lastClickedAnimWidget = self

            self.setNamePartEditMode(True)

    def onNamePartReturnPressed(self):
        if not self._signalsBlocked:
            scrollBar = self.animationTab.ui.Scr_AnimScrollArea.verticalScrollBar()
            currentScroll = scrollBar.value()
            
            self.setNamePartEditMode(False)
            
            scrollBar.setValue(currentScroll)

    def onNamePartTextEdited(self, text):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset NameParts"):  # Needed if there are multiple animations selected
                namePartIndex = self.getNamePartWidgetIndex(self.sender())
                widgetsToChange = [self] if not self.isSelected() else [widget for widget in self.animationTab.getAnimWidgetsByHolder(self.animPreset.getHolder()) if widget.isSelected()]
                for animWidget in widgetsToChange:
                    animWidget.setNamePart(text, namePartIndex, keepCursorPosition=True)

    def onBrowseExportPathClicked(self):
        if not self._signalsBlocked:
            tokenizer = self.getPathTokenizer()
            path = QtWidgets.QFileDialog.getExistingDirectory(self, "Chose Folder", dir=tokenizer.Translate(self.animPreset.path)).lower()
            if path != None and path != "" and os.path.exists(path):
                with UndoContext("Set AnimPreset Path"):  # Needed if there are multiple animations selected
                    path = self.animationTab.exporterWindow.tokenizeExportRoot(os.path.normpath(path))
                    path = tokenizer.Tokenize(path)
                    affectedWidgets = [self] if not self.isSelected() else self.animationTab.getSelectedAnimWidgets()
                    for animWidget in affectedWidgets:
                        animWidget.setPath(path)

    def onStartChanged(self, value):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset Start"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setStart(value, updateUI=(animWidget != self))
                else:
                    self.setStart(value, updateUI=False)

    def onEndChanged(self, value):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset End"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setEnd(value, updateUI=(animWidget != self))
                else:
                    self.setEnd(value, updateUI=False)

    def onLoopToggled(self, state):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset Loop"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setLoop(state, updateUI=(animWidget != self))
                else:
                    self.setLoop(state, updateUI=False)

    def onMirrorToggled(self, state):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset Mirror"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setMirror(state, updateUI=(animWidget != self))
                else:
                    self.setMirror(state, updateUI=False)

    def onPoseToggled(self, state):
        if not self._signalsBlocked:
            with UndoContext("Set AnimPreset Pose"):  # Needed if there are multiple animations selected
                if self.isSelected():
                    selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
                    for animWidget in selectedAnimWidgets:
                        animWidget.setPose(state, updateUI=(animWidget != self))
                else:
                    self.setPose(state, updateUI=False)

    def onDeleteButtonClicked(self):
        if not self._signalsBlocked:
            selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
            if self not in selectedAnimWidgets:
                selectedAnimWidgets = [self]
                self.animationTab.selectAnimWidgets(selectedAnimWidgets)
            
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.animationTab.deleteAnimWidgets(selectedAnimWidgets)

    # ------------------------------------
    # | Context Menu                     |
    # ------------------------------------

    def createNormalContextMenuOptions(self):
        contextMenuOptions = []
        
        holder = self.animPreset.getHolder()
        isActor = holder._Type == Actor.Actor._Type
        isCameraSet = holder._Type == CameraSet.CameraSet._Type
        
        selectHolderMenuOption = Utils.MenuOption('selectActor', 'Change Actor', True)
        selectHolderMenuOption.subMenus = []
        actors = ActorManager.getActors()
        cameraSets = ActorManager.getCameraSets()
        for actor in actors:
            selectHolderMenuOption.subMenus.append(Utils.MenuOption(actor.getNamespace(), actor.getNamespace(), True, partial(self.onSelectHolderOptionSelected, actor)))
        if actors:
            selectHolderMenuOption.subMenus.append(None)
        for cameraSet in cameraSets:
            selectHolderMenuOption.subMenus.append(Utils.MenuOption(cameraSet.name, cameraSet.name, True, partial(self.onSelectHolderOptionSelected, cameraSet)))
        if cameraSets:
            selectHolderMenuOption.subMenus.append(None)
        selectHolderMenuOption.subMenus.append(Utils.MenuOption("newCameraSet", "New Camera Set...", True, self.onSelectNewCameraSetOptionSelected))
        
        if isActor:
            selectSubActorMenuOption = Utils.MenuOption('selectSubActor', 'Change Sub Actor', True)
            subActors = holder.getSubActorsByTags([SubActor.SubActor.Tags.Animatable])
            if len(subActors) > 0:
                selectSubActorMenuOption.subMenus = [Utils.MenuOption(holder.getDisplayName(), holder.getDisplayName(), True, partial(self.onSelectSubActorOptionSelected, None))]
                selectSubActorMenuOption.subMenus.append(None)
                for subActor in subActors:
                    selectSubActorMenuOption.subMenus.append(Utils.MenuOption(subActor.name, subActor.name, True, partial(self.onSelectSubActorOptionSelected, subActor)))
        
        contextMenuOptions.append(Utils.MenuOption('exportSelected',  'Export Selected Animations',                   True,     self.onExportSelectedActorsOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('exportFBX',       'Export as FBX',                                True,     self.onExportAsFBXOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(selectHolderMenuOption)
        if isActor:     contextMenuOptions.append(selectSubActorMenuOption)
        if isActor:     contextMenuOptions.append(Utils.MenuOption('renameActor', 'Rename Actor', False, self.onRenameActorOptionSelected))
        if isCameraSet: contextMenuOptions.append(Utils.MenuOption('editCameraSet', 'Edit Camera Set', False, self.onEditCameraSetOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('setRange',        'Apply Animation Configuration',                True,     self.onApplyAnimationConfigurationOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('enableWidget',    'Enable Selected Presets',                      True,     self.onEnableSelectedActorsOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('disableWidget',   'Disable Selected Presets',                     True,     self.onDisableSelectedActorsOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('copyNameSegment', 'Copy Name (Segmented)',                        False,    self.onCopyNamePartsOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('copyName',        'Copy Name',                                    False,    self.onCopyNameOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('pasteName',       'Paste Name',                                   False,    self.onPasteNameOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('copyPath',        'Copy Path',                                    False,    self.onCopyPathOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('pastePath',       'Paste Path',                                   True,     self.onPastePathOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('openFolder',      'Open Folder',                                  False,    self.onOpenFolderOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('restoreFolder',   'Restore Default Path',                         True,     self.onRestoreDefaultPathOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('setColor',        'Select Color',                                 True,     self.onSetColorOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('setCategory',     'Select Category',                              True,     self.onSetCategoryOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('copyLayerSet',    'Copy Layer Set',                               False,    self.onCopyLayerSetOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('pasteLayerSet',   'Paste Layer Set',                              True,     self.onPasteLayerSetOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('duplicateWidget', 'Duplicate Selected Presets',                   True,     self.onDuplicateSelectedActorsOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('duplicateWidget', 'Duplicate Selected Presets (Keep position)',   True,     self.onDuplicateSelectedActorsKeepPositionOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('deleteWidget',    'Delete Selected Presets',                      True,     self.onDeleteSelectedAnimationsOptionSelected))

        return contextMenuOptions

    def createNamePartContextMenuOptions(self):
        contextMenuOptions = []

        contextMenuOptions.append(Utils.MenuOption('finishEdit',    'Finish Editing',       callback=self.onFinishEditingOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('insertAfter',   'Insert Column After',  callback=self.onInsertColumAfterOptionSelected))
        contextMenuOptions.append(Utils.MenuOption('insertBefore',  'Insert Column Before', callback=self.onInsertColumBeforeOptionSelected))
        contextMenuOptions.append(None)
        contextMenuOptions.append(Utils.MenuOption('remove',        'Remove Column',        callback=self.onRemoveColumnOptionSelected))

        return contextMenuOptions

    def showNamePartContextMenu(self):
        Utils.showContextMenu(self._namePartContextMenuOptions, self.sender(), QtGui.QCursor.pos())

    # Normal Context Menu Callbacks ------

    def onExportSelectedActorsOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        self.animationTab.exportAnimWidgets(selectedAnimWidgets)

    def onExportAsFBXOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        self.animationTab.exportAsFBX(selectedAnimWidgets)
    
    def onSelectHolderOptionSelected(self, holder):
        with UndoContext("Select Actor"):
            selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
            for animWidget in selectedAnimWidgets:
                animWidget.animPreset.changeHolder(holder)
        
        self.animationTab.refreshAnimWidgetsList(keepSelection=True)
        
        QtCore.QCoreApplication.processEvents() # The ScrollArea geometry is not build yet, so we process a draw so it is calculated
        QtCore.QCoreApplication.processEvents() # For some reason, if we don't do this twice, the ScrollArea geometry won't include the new row
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()    # Previous widgets have been destroyed, get the new selected ones
        for animWidget in selectedAnimWidgets:
            self.animationTab.ui.Scr_AnimScrollArea.ensureWidgetVisible(animWidget)
    
    def onSelectNewCameraSetOptionSelected(self):
        with UndoContext("Select New Camera Set"):
            cameraSet = self.animationTab.showCreateCameraSetDialog(addNewAnimation=False)
            if cameraSet:
                self.onSelectHolderOptionSelected(cameraSet)
    
    def onSelectSubActorOptionSelected(self, subActor):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()

        # Only Allow it if all the selected anim widgets belong to the same actor
        actor = None
        for animWidget in selectedAnimWidgets:
            a = animWidget.animPreset.getHolder()
            if actor == None:
                actor = a
            elif actor != a:
                QtWidgets.QMessageBox.warning(self.animationTab.exporterWindow, "Set AnimPreset SubActor", "Unable to change the selected animations' subactor, since they belong to different actors. Please select animations from a single actor.")
                return

        with UndoContext("Set AnimPreset SubActor"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.setSubHolder(subActor)

    def onRenameActorOptionSelected(self):
        actorName = self.animPreset.getHolder().getNamespace()
        newName, result = self.animationTab.selectActorName(actorName)
        if result and newName != actorName:
            with UndoContext("Rename Actor"):
                cmds.namespace(rename=(actorName, newName), parent=":")
        
            self.animationTab.refreshAnimWidgetsList(keepSelection=True)
    
    def onEditCameraSetOptionSelected(self):
        self.animationTab.showEditCameraSetDialog(self.animPreset.getHolder())
        self.animationTab.refreshAnimWidgetsList(keepSelection=True)

    def onEnableSelectedActorsOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        with UndoContext("Set AnimPreset Enabled"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.setEnabled(True)

    def onDisableSelectedActorsOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        with UndoContext("Set AnimPreset Enabled"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.setEnabled(False)

    def onApplyAnimationConfigurationOptionSelected(self):
        self.animationTab.applyAnimationConfiguration(self.animationTab.getSelectedAnimWidgets())

    def onCopyNamePartsOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        app.clipboard().setText(",".join(self.animPreset.getNameParts()))   # Since the clipboard can only store strings, we use the "," separator to indicate the segments.

    def onCopyNameOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        app.clipboard().setText(self.animPreset.getConcatenatedName())

    def onPasteNameOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        name = app.clipboard().text().split(",")
        nameParts = self.animPreset.getNameParts()

        if len(name) <= 1 and len(nameParts) != 1:
            result = QtWidgets.QMessageBox.warning(self, "Paste Name", "Warning: The name you are trying to paste is not segmented. It will be pasted just on the first cell, do you want to continue?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if result != QtWidgets.QMessageBox.Yes:
                return

        for i in range(len(name)):
            if i >= len(nameParts):
                self.insertNamePart()
                nameParts.append(name[i])
            else:
                nameParts[i] = name[i]
        for i in range(len(name), len(nameParts)):
            nameParts[i] = ""
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animPreset.setNameParts(nameParts)

        if self.getNamePartEditMode():
            self.refreshNameParts()
        else:
            self.ui.Btn_EditName.setText(self.animPreset.getConcatenatedName())

    def onCopyPathOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        path = self.getPathTokenizer().Translate(self.animPreset.path)
        app.clipboard().setText(path)

    def onPastePathOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        path = self.getPathTokenizer().Tokenize(app.clipboard().text())
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        with UndoContext("Set AnimPreset Path"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.setPath(path)

    def onOpenFolderOptionSelected(self):
        path = self.getPathTokenizer().Translate(self.animPreset.path)
        if os.path.exists(path):
            os.startfile(path)

    def onRestoreDefaultPathOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        with UndoContext("Restore AnimPreset Path"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.setPath("")

    def onCopyLayerSetOptionSelected(self):
        weightedLayers = self.animPreset.getWeightedLayers()
        weightedLayersData = ["{},{}".format(weightedLayer.animLayer, weightedLayer.weight) for weightedLayer in weightedLayers]
        
        app = QtWidgets.QApplication.instance()
        app.clipboard().setText(";".join(weightedLayersData))   # Since the clipboard can only store strings, we use the ";" separator to separate each layer.

    def onPasteLayerSetOptionSelected(self):
        app = QtWidgets.QApplication.instance()
        weightedLayers = app.clipboard().text().split(";")
        
        animLayers = []
        weights = []
        for weightedLayer in weightedLayers:
            if weightedLayer:
                weightedLayerData = weightedLayer.split(",")
                animLayers.append(weightedLayerData[0])
                weights.append(float(weightedLayerData[1]))
            
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        with UndoContext("Paste AnimPreset Layers"):  # Needed if there are multiple animations selected
            for animWidget in selectedAnimWidgets:
                animWidget.animPreset.setAnimLayers(animLayers, weights)
        self.animationTab.refreshLayerPanel()

    def onDuplicateSelectedActorsOptionSelected(self):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animationTab.duplicateAnimWidgets(self.animationTab.getSelectedAnimWidgets(), keepPosition=False)            

    def onDuplicateSelectedActorsKeepPositionOptionSelected(self):
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animationTab.duplicateAnimWidgets(self.animationTab.getSelectedAnimWidgets(), keepPosition=True)

    def onDeleteSelectedAnimationsOptionSelected(self):
        selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.animationTab.deleteAnimWidgets(selectedAnimWidgets)

    def onSetColorOptionSelected(self):
        initialColor = self.animPreset.color
        initialColor = QtGui.QColor(initialColor[0], initialColor[1], initialColor[2])
        colorPicker = QtWidgets.QColorDialog(initialColor, self)
        if colorPicker.exec_() ==  QtWidgets.QDialog.Accepted:
            selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
            with UndoContext("Set AnimPreset Colors"):  # Needed if there are multiple animations selected
                for animWidget in selectedAnimWidgets:
                    animWidget.setColor(colorPicker.currentColor())

    def onSetCategoryOptionSelected(self):
        newCategory, result = self.animationTab.selectCategory(self.animPreset.category)
        if result:
            selectedAnimWidgets = self.animationTab.getSelectedAnimWidgets()
            with UndoContext("Set AnimPreset Category"):  # Needed if there are multiple animations selected
                for animWidget in selectedAnimWidgets:
                    animWidget.animPreset.category = newCategory
            
            self.animationTab.refreshAnimWidgetsList(keepSelection=True)

    # Name Part Context Menu Callbacks ---

    def onFinishEditingOptionSelected(self):
        self.setNamePartEditMode(False)
    
    def onInsertColumAfterOptionSelected(self):
        namePartIndex = self.getNamePartWidgetIndex(self.sender().parentWidget())
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.insertNamePart(namePartIndex + 1)

    def onInsertColumBeforeOptionSelected(self):
        namePartIndex = self.getNamePartWidgetIndex(self.sender().parentWidget())
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.insertNamePart(namePartIndex)

    def onRemoveColumnOptionSelected(self):
        namePartIndex = self.getNamePartWidgetIndex(self.sender().parentWidget())
        # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
        self.deleteNamePart(namePartIndex)

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._dragStartPosition = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if (event.pos() - self._dragStartPosition).manhattanLength() >= QtWidgets.QApplication.startDragDistance():
                if not self.isSelected():
                    self.animationTab.selectAnimWidgets([self])
                    
                selectedAnimPresets = self.animationTab.getSelectedAnimPresets()
                canBeReordered, reason = self.animationTab.getAnimWidgetSortState().canBeReordered(selectedAnimPresets)
                if not canBeReordered:
                    QtWidgets.QMessageBox.warning(self, "Reorder Animations", reason)
                    return

                dragPixmap = self.createDragPixmap()

                mimeData = QtCore.QMimeData()
                mimeData.setObjectName("moveAnimWidgetMimeData")
                mimeData.setText(",".join([animPreset.node for animPreset in selectedAnimPresets]))

                drag = QtGui.QDrag(self)
                drag.setMimeData(mimeData)
                drag.setHotSpot(event.pos())
                drag.setPixmap(dragPixmap)
                dropAction = drag.start(QtCore.Qt.MoveAction) # We don't do anything else regardless of the dropAction

    def dragEnterEvent(self, event):
        if event.mimeData().objectName() == "moveAnimWidgetMimeData" and not self.isSelected():
            nodes = event.mimeData().text().split(",")
            targets = [AnimPreset.AnimPreset(node) for node in nodes]
            if self.animationTab.getAnimWidgetSortState().canElementsBeReordered(targets, self.animPreset):
                event.setDropAction(QtCore.Qt.MoveAction)
                event.accept()

    def dropEvent(self, event):
        event.acceptProposedAction()
        
        selectedAnimPresets = self.animationTab.getSelectedAnimPresets()
        isTargetSelected = self.animPreset in selectedAnimPresets
        if isTargetSelected:
            selectedAnimPresets.remove(self.animPreset)
        
        with UndoContext("Reorder AnimPreset"):
            doReorder = self.animationTab.getAnimWidgetSortState().onReorder(selectedAnimPresets, self.animPreset)
            if doReorder:
                holder = self.animPreset.getHolder()
                animPresets = holder.getAnimPresets()
                
                for animPreset in selectedAnimPresets:
                    animPresets.remove(animPreset)
                    
                index = animPresets.index(self.animPreset)
                if isTargetSelected or event.pos().y() > self.height() / 2:
                    index += 1
                
                for i, animPreset in enumerate(selectedAnimPresets):
                    animPresets.insert(index + i, animPreset)
        
                holder.setAnimPresets(animPresets)
        
        self.animationTab.refreshAnimWidgetsList(keepSelection=True)

    def mouseReleaseEvent(self, mouseEvent):
        if self.geometry().contains(self.parent().mapFromGlobal(mouseEvent.globalPos())):
            # Left mouse button => Selection
            if mouseEvent.button() == QtCore.Qt.LeftButton:
                # No modifier => Selects the widget, deselecting any other widget
                if mouseEvent.modifiers() == QtCore.Qt.NoModifier:
                    self.animationTab.selectAnimWidgets([self], replaceSelection=True)

                # Ctrl modifier => Selects of deselects the widget, toggling
                elif mouseEvent.modifiers() == QtCore.Qt.ControlModifier:
                    self.setSelected(not self.isSelected())
                    self.animationTab.refreshLayerPanel()

                # Shift modifier => Selects multiple widgets from the position of the last one selected
                elif mouseEvent.modifiers() & QtCore.Qt.ShiftModifier or mouseEvent.modifiers() == (QtCore.Qt.ShiftModifier | QtCore.Qt.ControlModifier):
                    animWidgets = self.animationTab.getAnimWidgets()
                    widgetIndex = animWidgets.index(self)
                    if self.animationTab.lastClickedAnimWidget in animWidgets:
                        lastClickedWidgetIndex = animWidgets.index(self.animationTab.lastClickedAnimWidget)
                        for i in range(widgetIndex, lastClickedWidgetIndex, 1 if widgetIndex <= lastClickedWidgetIndex else -1):
                            animWidgets[i].setSelected(True)
                    else:
                        self.setSelected(True)
                    self.animationTab.refreshLayerPanel()
        
        self.animationTab.lastClickedAnimWidget = self

    def mouseDoubleClickEvent(self, mouseEvent):
        if mouseEvent.button() == QtCore.Qt.LeftButton and mouseEvent.modifiers() == QtCore.Qt.NoModifier:
            # No need to create an undo context here, since only one action will be performed (and it already creates a context on its own)
            self.applyAnimationConfiguration()

    def contextMenuEvent(self, event):
        if not self.isSelected():
            self.animationTab.selectAnimWidgets([self], replaceSelection=True)
        multiSelection = len(self.animationTab.getSelectedAnimWidgets()) > 1
        Utils.showContextMenu(self._normalContextMenuOptions, self, QtGui.QCursor.pos(), multiSelection=multiSelection)
        
        self.animationTab.lastClickedAnimWidget = self
