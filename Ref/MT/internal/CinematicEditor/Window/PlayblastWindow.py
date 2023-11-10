# encoding: utf-8
from PySide2 import QtCore, QtGui, QtWidgets

import QtCustomWidgets.CollapsiblePanel as CollapsiblePanel

import CinematicEditor.Cutscene as Cutscene
import CinematicEditor.MasterSlave as MasterSlave

import ScreenDrawer.CinematicGuides as CinematicGuides

import maya.cmds as cmds
import maya.mel as mel
from maya.api import OpenMaya, OpenMayaRender

import ScreenDrawer
import ProjectPath

from Utils.Maya.OptionVar import OptionVarConfiguration

import copy
import os
import sys
import traceback
import shutil
import datetime

#TODO: Guardar Encoder settings en OptionVars

class PlayblastDrawer(ScreenDrawer.ScreenDrawer):
    
    class Data(object):
        def __init__(self, cameraPath, frameContext):            
            self.dimensions = ScreenDrawer.ScreenDrawerManager.getCameraRect(cameraPath, frameContext)
            
            self.cameraName = OpenMaya.MDagPath.getAPathTo(frameContext.getCurrentCameraPath().transform()).partialPathName()
            
            self.focalLength = OpenMaya.MFnDependencyNode(frameContext.getCurrentCameraPath().node()).findPlug("focalLength", False).asFloat()
    
    def __init__(self):
        super().__init__()
        
        self.currentShot = None
    
    def prepareForDraw(self, objPath, cameraPath, frameContext):
        return PlayblastDrawer.Data(cameraPath, frameContext)
    
    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        currentTime = int(cmds.currentTime(q=True))
        if self.currentShot != None:
            rangeStart = self.currentShot.start
            rangeEnd = self.currentShot.end
        else:
            # Safety measure in case a draw is called before the current shot is set
            rangeStart = 0
            rangeEnd = 1
        
        drawManager.beginDrawable()

        textToWidthFactor = 1.0
        backgroundColor = OpenMaya.MColor((0, 0, 0, 0.5))
        fontSize = max(10, int(10 * data.dimensions[3] / 720.0))

        drawManager.setColor(OpenMaya.MColor((0.7, 0.7, 0.7, 1)))
        drawManager.setFontSize(fontSize)
        drawManager.setFontName("Console")

        fontMetrics = QtGui.QFontMetrics(QtGui.QFont("Console", fontSize))
        textHeight = fontMetrics.height()

        # Camera name
        text = data.cameraName
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + 3 * data.dimensions[2] / 4, data.dimensions[1] + 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)
        
        # Draws FOV
        text = "{}mm".format("%.2f" % round(data.focalLength,2))
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        #drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + data.dimensions[2] / 4, data.dimensions[1] + 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)
        
        # Shot name
        if self.currentShot != None:
            text = self.currentShot.shotName
            textWidth = int(fontMetrics.width(text) * textToWidthFactor)
            drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + data.dimensions[2] / 2, data.dimensions[1] + data.dimensions[3] - textHeight - 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)

        # Cutscene frame
        if self.currentShot != None:
            cutsceneFrame = self.currentShot.getCutscene().getCutsceneFrameFromAnimationFrame(currentTime, preferredShot=self.currentShot)
            text = " {}f ".format(cutsceneFrame)
            textWidth = int(fontMetrics.width(text) * textToWidthFactor)
            drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + data.dimensions[2] / 2, data.dimensions[1] + 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)
        
        # Shot Range
        text = "{} [{} - {}] ({})".format(currentTime, rangeStart, rangeEnd, rangeEnd - rangeStart)
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + data.dimensions[2] - textWidth / 2 - 10, data.dimensions[1] + 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)
        
        # User
        text = os.environ["USER"]
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + textWidth / 2 + 5, data.dimensions[1] + 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)
        
        # Date
        text = datetime.datetime.now().strftime(" %d/%m/%Y ")
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + data.dimensions[2] - textWidth / 2 - 10, data.dimensions[1] + data.dimensions[3] - textHeight - 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)

        # File name
        text, temp = os.path.splitext(os.path.basename(cmds.file(q=True, sn=True)))
        if text == "":
            text = "Untitled"
        textWidth = int(fontMetrics.width(text) * textToWidthFactor)
        drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + textWidth / 2 + 5, data.dimensions[1] + data.dimensions[3] - textHeight - 5), text, alignment=OpenMayaRender.MUIDrawManager.kCenter, backgroundSize=[textWidth, textHeight], backgroundColor=backgroundColor, dynamic=False)

        drawManager.endDrawable()


class CinematicPlayblastUI(QtWidgets.QDialog):

    FFMPEG_PATH = "FFMpeg/ffmpeg.exe"
    
    PLAYBLAST_FOLDER_OPTIONVAR = OptionVarConfiguration("Playblast Folder", "CINEMATIC_EDITOR_PLAYBLAST_FOLDER", OptionVarConfiguration.TYPE_STRING, "{userFolder}/Videos/Playblast/{cutsceneName}")
    PLAYBLAST_VIDEO_FORMAT_PRESET_OPTIONVAR = OptionVarConfiguration("Playblast Format Preset", "CINEMATIC_EDITOR_PLAYBLAST_VIDEO_FORMAT_PRESET", OptionVarConfiguration.TYPE_STRING, "mp4")
    PLAYBLAST_VIDEO_CODEC_PRESET_OPTIONVAR = OptionVarConfiguration("Playblast Codec Preset", "CINEMATIC_EDITOR_PLAYBLAST_VIDEO_CODEC_PRESET", OptionVarConfiguration.TYPE_STRING, "h264")
    PLAYBLAST_VIDEO_RESOLUTION_OPTIONVAR = OptionVarConfiguration("Playblast Format", "CINEMATIC_EDITOR_PLAYBLAST_VIDEO_RESOLUTION", OptionVarConfiguration.TYPE_INTEGER, [1280, 720])
    PLAYBLAST_VISIBILITY_OPTIONVAR = OptionVarConfiguration("Playblast Format", "CINEMATIC_EDITOR_PLAYBLAST_VISIBILITY_PRESET", OptionVarConfiguration.TYPE_STRING, "Geometry")
    PLAYBLAST_DRAW_GUIDES_OPTIONVAR = OptionVarConfiguration("Draw Guides on Playblast", "CINEMATIC_EDITOR_PLAYBLAST_DRAW_GUIDES", OptionVarConfiguration.TYPE_INTEGER, False)
    PLAYBLAST_DRAW_INFO_OPTIONVAR = OptionVarConfiguration("Draw Playblast Info", "CINEMATIC_EDITOR_PLAYBLAST_DRAW_INFO", OptionVarConfiguration.TYPE_INTEGER, True)
    PLAYBLAST_PLAY_AFTER_OPTIONVAR = OptionVarConfiguration("Play After Playblast", "CINEMATIC_EDITOR_PLAYBLAST_PLAY_AFTER", OptionVarConfiguration.TYPE_INTEGER, True)
    PLAYBLAST_SAVE_VERSION_OPTIONVAR = OptionVarConfiguration("Save Playblast Version", "CINEMATIC_EDITOR_PLAYBLAST_SAVE_VERSION", OptionVarConfiguration.TYPE_INTEGER, True)
    
    CONTAINER_PRESETS = [
        "mp4",
        "Image"
    ]

    RESOLUTION_PRESETS = [
        "Render",
        "HD 1080",
        "HD 720",
        "HD 540",
    ]

    VISIBILITY_PRESETS = [
        "Geometry",
        "Viewport"
    ]


    def __init__(self, cutscene : Cutscene.Cutscene, parent=None):
        super(CinematicPlayblastUI, self).__init__(parent=parent)
        
        self.cutscene = cutscene

        self.setWindowTitle("Cinematic Playblast")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(390)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        self._playblast = ZurbriggPlayblast(ffmpeg_path=os.path.join(ProjectPath.getExternalFolder(), CinematicPlayblastUI.FFMPEG_PATH), log_to_maya=True)

        self._encoder_settings_dialog = None
        self._visibility_dialog = None

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.output_dir_path_le = QtWidgets.QLineEdit()
        self.output_dir_path_le.setEnabled(False)

        self.path_btn = QtWidgets.QPushButton("Browse")
        self.path_btn.setToolTip("Changes the folder where the playblast will be saved.")
        self.path_btn.setFixedWidth(45)
        self.path_btn.setFixedHeight(19)

        self.output_dir_path_show_folder_btn = QtWidgets.QPushButton(QtGui.QIcon(":fileOpen.png"), "Show in Folder")
        self.output_dir_path_show_folder_btn.setToolTip("Opens the playblast directory on the explorer.")
        self.output_dir_path_show_folder_btn.setFixedHeight(19)

        playblastAllShotsButton = QtWidgets.QRadioButton("All Shots")
        playblastMarkedShotsButton = QtWidgets.QRadioButton("Marked Shots")
        playblastSelectedShotsButton = QtWidgets.QRadioButton("Selected Shots")
        playblastAllShotsButton.setToolTip("Playblasts all the enabled shots.")
        playblastMarkedShotsButton.setToolTip("Only playblasts the shots marked (checkbox to their left).")
        playblastSelectedShotsButton.setToolTip("Playblasts the selected shots.")

        self.playblastShotsOptionsRadiobuttonGroup = QtWidgets.QButtonGroup()
        self.playblastShotsOptionsRadiobuttonGroup.addButton(playblastAllShotsButton, id=0)
        self.playblastShotsOptionsRadiobuttonGroup.addButton(playblastMarkedShotsButton, id=1)
        self.playblastShotsOptionsRadiobuttonGroup.addButton(playblastSelectedShotsButton, id=2)
        self.playblastShotsOptionsRadiobuttonGroup.button(0).setChecked(True)
        
        mergeAllButton = QtWidgets.QRadioButton("All Shots")
        mergeExportedButton = QtWidgets.QRadioButton("Playblasted Shots")
        mergeNoneButton = QtWidgets.QRadioButton("Don't Merge")
        mergeAllButton.setToolTip("After playblast, merge all shots, not only the ones being playblasted.")
        mergeExportedButton.setToolTip("After playblast, merge the shots being playblasted.")
        mergeNoneButton.setToolTip("Don't merge any shots after playblast.")

        self.mergeOptionsRadiobuttonGroup = QtWidgets.QButtonGroup()
        self.mergeOptionsRadiobuttonGroup.addButton(mergeAllButton, id=0)
        self.mergeOptionsRadiobuttonGroup.addButton(mergeExportedButton, id=1)
        self.mergeOptionsRadiobuttonGroup.addButton(mergeNoneButton, id=2)
        self.mergeOptionsRadiobuttonGroup.button(1).setChecked(True)

        self.merge_btn = QtWidgets.QPushButton("Manual Merge")
        self.merge_btn.setToolTip("Merges the already playblasted shots using the selected option.")
        
        self.resolution_select_cmb = QtWidgets.QComboBox()
        self.resolution_select_cmb.addItems(CinematicPlayblastUI.RESOLUTION_PRESETS)
        self.resolution_select_cmb.addItem("Custom")
        self.resolution_select_cmb.setCurrentText("Custom")

        self.resolution_width_sb = QtWidgets.QSpinBox()
        self.resolution_width_sb.setButtonSymbols(QtWidgets.QSpinBox.NoButtons)
        self.resolution_width_sb.setRange(1, 9999)
        self.resolution_width_sb.setMinimumWidth(40)
        self.resolution_width_sb.setAlignment(QtCore.Qt.AlignRight)
        self.resolution_height_sb = QtWidgets.QSpinBox()
        self.resolution_height_sb.setButtonSymbols(QtWidgets.QSpinBox.NoButtons)
        self.resolution_height_sb.setRange(1, 9999)
        self.resolution_height_sb.setMinimumWidth(40)
        self.resolution_height_sb.setAlignment(QtCore.Qt.AlignRight)

        self.encoding_container_cmb = QtWidgets.QComboBox()
        self.encoding_container_cmb.addItems(CinematicPlayblastUI.CONTAINER_PRESETS)
        self.encoding_container_cmb.setCurrentText(CinematicPlayblastUI.PLAYBLAST_VIDEO_FORMAT_PRESET_OPTIONVAR.value)

        self.encoding_video_codec_cmb = QtWidgets.QComboBox()
        self.encoding_video_codec_settings_btn = QtWidgets.QPushButton("Settings...")
        self.encoding_video_codec_settings_btn.setFixedHeight(19)

        self.visibility_cmb = QtWidgets.QComboBox()
        self.visibility_cmb.addItems(CinematicPlayblastUI.VISIBILITY_PRESETS)
        self.visibility_cmb.addItem("Custom")
        self.visibility_cmb.setCurrentText("Custom")
        
        self.visibility_customize_btn = QtWidgets.QPushButton("Customize...")
        self.visibility_customize_btn.setFixedHeight(19)

        self.cinematicGuidesCheckbox = QtWidgets.QCheckBox()
        self.cinematicGuidesCheckbox.setChecked(CinematicPlayblastUI.PLAYBLAST_DRAW_GUIDES_OPTIONVAR.value)

        self.overlayInfoCheckbox = QtWidgets.QCheckBox()
        self.overlayInfoCheckbox.setChecked(CinematicPlayblastUI.PLAYBLAST_DRAW_INFO_OPTIONVAR.value)

        self.saveVersionCheckbox = QtWidgets.QCheckBox("Save playblast version")
        self.saveVersionCheckbox.setToolTip("Saves a copy of the playblasted shots to a folder named after the Maya file.")
        self.saveVersionCheckbox.setChecked(CinematicPlayblastUI.PLAYBLAST_SAVE_VERSION_OPTIONVAR.value)

        self.viewer_cb = QtWidgets.QCheckBox("Play when finished")
        self.viewer_cb.setToolTip("Plays the generated video after finishing the playblast.")
        self.viewer_cb.setChecked(CinematicPlayblastUI.PLAYBLAST_PLAY_AFTER_OPTIONVAR.value)
        
        self.playblast_btn = QtWidgets.QPushButton("Playblast")

    def create_layout(self):
        output_path_layout = QtWidgets.QHBoxLayout()
        output_path_layout.setSpacing(4)
        output_path_layout.addWidget(self.output_dir_path_le)
        output_path_layout.addWidget(self.path_btn)
        output_path_layout.addWidget(self.output_dir_path_show_folder_btn)

        output_grp = QtWidgets.QGroupBox("Folder")
        output_grp.setLayout(output_path_layout)

        shots_layout = QtWidgets.QHBoxLayout()
        for button in self.playblastShotsOptionsRadiobuttonGroup.buttons():
            shots_layout.addWidget(button)

        shots_grp = QtWidgets.QGroupBox("Shots")
        shots_grp.setLayout(shots_layout)

        mergeOptionsLayout = QtWidgets.QHBoxLayout()
        for button in self.mergeOptionsRadiobuttonGroup.buttons():
            mergeOptionsLayout.addWidget(button)
        mergeOptionsLayout.addWidget(self.merge_btn)

        merge_grp = QtWidgets.QGroupBox("Merge")
        merge_grp.setLayout(mergeOptionsLayout)
        
        resolution_layout = QtWidgets.QHBoxLayout()
        resolution_layout.setSpacing(4)
        resolution_layout.addWidget(self.resolution_select_cmb)
        resolution_layout.addWidget(self.resolution_width_sb)
        resolution_layout.addWidget(QtWidgets.QLabel("x"))
        resolution_layout.addWidget(self.resolution_height_sb)

        encoding_layout = QtWidgets.QHBoxLayout()
        encoding_layout.setSpacing(4)
        encoding_layout.addWidget(self.encoding_container_cmb)
        encoding_layout.addWidget(self.encoding_video_codec_cmb)
        encoding_layout.addWidget(self.encoding_video_codec_settings_btn)

        visibility_layout = QtWidgets.QHBoxLayout()
        visibility_layout.setSpacing(4)
        visibility_layout.addWidget(self.visibility_cmb)
        visibility_layout.addWidget(self.visibility_customize_btn)

        options_layout = QtWidgets.QFormLayout()
        options_layout.addRow("Resolution:", resolution_layout)
        options_layout.addRow("Encoding:", encoding_layout)
        options_layout.addRow("Visibility:", visibility_layout)
        options_layout.addRow("Cinematic Guides:", self.cinematicGuidesCheckbox)
        options_layout.addRow("Overlay Info:", self.overlayInfoCheckbox)

        options_panel = CollapsiblePanel.CollapsiblePanel("Options", mainWindow=self)
        options_panel.addLayout(options_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setAlignment(QtCore.Qt.AlignRight)
        button_layout.addWidget(self.saveVersionCheckbox)
        button_layout.addWidget(self.viewer_cb)
        button_layout.addWidget(self.playblast_btn)

        status_bar_layout = QtWidgets.QHBoxLayout()
        status_bar_layout.addStretch()

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(4)
        main_layout.addWidget(output_grp)
        main_layout.addWidget(shots_grp)
        main_layout.addWidget(merge_grp)
        main_layout.addWidget(options_panel)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(status_bar_layout)

    def create_connections(self):
        self.output_dir_path_show_folder_btn.clicked.connect(self.open_output_directory)
        self.path_btn.clicked.connect(self.onPathButtonPressed)

        self.encoding_container_cmb.currentTextChanged.connect(self.onVideoFormatPresetChanged)
        self.encoding_video_codec_cmb.currentTextChanged.connect(self.onVideoCodecPresetChanged)
        self.encoding_video_codec_settings_btn.clicked.connect(self.show_encoder_settings_dialog)

        self.resolution_select_cmb.currentTextChanged.connect(self.onResolutionPresetChanged)
        self.resolution_width_sb.editingFinished.connect(self.onResolutionChanged)
        self.resolution_height_sb.editingFinished.connect(self.onResolutionChanged)

        self.visibility_cmb.currentTextChanged.connect(self.onVisibilityPresetChanged)
        self.visibility_customize_btn.clicked.connect(self.show_visibility_dialog)

        self.cinematicGuidesCheckbox.clicked.connect(self.onDrawCinematicGuidesOptionChanged)
        self.overlayInfoCheckbox.clicked.connect(self.onDrawOverlayInfoOptionChanged)

        self.saveVersionCheckbox.clicked.connect(self.onSaveVersionOptionChanged)
        self.viewer_cb.clicked.connect(self.onPlayAfterPlaybackOptionChanged)

        self.merge_btn.clicked.connect(self.onManualMergeClicked)
        self.playblast_btn.clicked.connect(self.do_playblast)
    
    def onVideoFormatPresetChanged(self, value):
        self.PLAYBLAST_VIDEO_FORMAT_PRESET_OPTIONVAR.value = value
        
        self.refresh_video_encoders()
        
    def onVideoCodecPresetChanged(self, value):
        self.PLAYBLAST_VIDEO_CODEC_PRESET_OPTIONVAR.value = value
        
        container = self.encoding_container_cmb.currentText()
        encoder = self.encoding_video_codec_cmb.currentText()

        if container and encoder:
            self._playblast.set_encoding(container, encoder)
        
    def onResolutionPresetChanged(self, value):
        if value != "Custom":
            self.refresh_resolution()
        
    def onResolutionChanged(self):
        resolution = [self.resolution_width_sb.value(), self.resolution_height_sb.value()]
        self.PLAYBLAST_VIDEO_RESOLUTION_OPTIONVAR.value = resolution

        for key in ZurbriggPlayblast.RESOLUTION_LOOKUP.keys():
            if list(ZurbriggPlayblast.RESOLUTION_LOOKUP[key]) == resolution:
                self.resolution_select_cmb.setCurrentText(key)
                return

        self.resolution_select_cmb.setCurrentText("Custom")

        self._playblast.set_resolution(resolution)

    def onVisibilityPresetChanged(self, value):
        if value != "Custom":
            self.PLAYBLAST_VISIBILITY_OPTIONVAR.value = value
            
            self.refresh_visibility()
            
    def onVisibilityChanged(self):
        visibilityData = self._playblast.visibility_to_preset(self._visibility_dialog.get_visibility_data())
        self.PLAYBLAST_VISIBILITY_OPTIONVAR.value = visibilityData
        
        self.refresh_visibility()

    def onDrawCinematicGuidesOptionChanged(self, state):
        self.PLAYBLAST_DRAW_GUIDES_OPTIONVAR.value = state

    def onDrawOverlayInfoOptionChanged(self, state):
        self.PLAYBLAST_DRAW_INFO_OPTIONVAR.value = state

    def onSaveVersionOptionChanged(self, state):
        self.PLAYBLAST_SAVE_VERSION_OPTIONVAR.value = state

    def onPlayAfterPlaybackOptionChanged(self, state):
        self.PLAYBLAST_PLAY_AFTER_OPTIONVAR.value = state

    def getSelectedShots(self):
        selectedOption = self.playblastShotsOptionsRadiobuttonGroup.checkedId()
        if selectedOption == 0:
            # All Enabled Shots
            shots = self.cutscene.getEnabledShots()
        elif selectedOption == 1:
            # Only Marked Shots
            shots = self.cutscene.getActiveShots()
        elif selectedOption == 2:
            # Selected Shots
            shots = self.parent().shotTable.getSelectedShots()
        
        # Master-Slave: Can only playblast owned shots
        masterSlaveFile = MasterSlave.MasterSlaveFile(self.cutscene)
        if masterSlaveFile.exists():
            masterSlaveFile.load()
            shots = [shot for shot in shots if masterSlaveFile.ownsShot(shot)]
        
        return shots

    def onManualMergeClicked(self):
        if self.mergeOptionsRadiobuttonGroup.checkedId() == 2:
            cmds.confirmDialog(title="Merge", message="The [Don't Merge] option is selected. Please select other merge option.")
            return

        shotsToMerge = []
        if self.mergeOptionsRadiobuttonGroup.checkedId() == 0:
            shotsToMerge = self.cutscene.getEnabledShots()
        elif self.mergeOptionsRadiobuttonGroup.checkedId() == 1:
            shotsToMerge = self.getSelectedShots()
        
        if len(shotsToMerge) == 0:
            cmds.confirmDialog(title="Merge", message="There are no shots to merge.")
            return

        result = self.mergeShots(shotsToMerge)

        if result:
            if self.viewer_cb.isChecked():
                self.openMergedFile()
            else:
                cmds.confirmDialog(title="Merge", message="The shots have been succesfully merged.")

    def getMayaFileName(self):
        filePath = cmds.file(q=True, sn=True)
        fileName = os.path.basename(filePath)
        rawName, extension = os.path.splitext(fileName)
        return rawName

    def getPathTokenizer(self):
        pathTokenizer = ProjectPath.PathTokenizer()
        pathTokenizer.Update({
                              "userFolder" : os.path.dirname(os.path.expanduser("~")),
                              "cutsceneName" : self.cutscene.getCutsceneName()
                              })
        return pathTokenizer

    def mergeShots(self, shotsToMerge):
        outputFolder = self.output_dir_path_le.text()

        fileNames = []
        shotsMissingFile = []
        for shot in shotsToMerge:
            shotFile = os.path.join(outputFolder, shot.shotName + ".mp4")
            if not os.path.exists(shotFile):
                shotsMissingFile.append(shot)
            else:
                fileNames.append(shotFile)
                
        if shotsMissingFile:
            shotText = ""
            for shot in shotsMissingFile:
                shotText += "\n- {}".format(shot.shotName)
            QtWidgets.QMessageBox.warning(self, "Merge Shots", "Missing shots' playblast files, unable to merge playblast!\n" + shotText)
            return False
        
        mergedFileName = self.cutscene.getCutsceneName() + ".mp4"
        self._playblast.merge(outputFolder, mergedFileName, fileNames)

        mayaFileName = self.getMayaFileName()
        if self.saveVersionCheckbox.isChecked() and mayaFileName != "":
            copyFilePath = os.path.join(outputFolder, mayaFileName)
            if not os.path.isdir(copyFilePath):
                os.makedirs(copyFilePath)

            src = os.path.join(outputFolder, mergedFileName)
            dst = os.path.join(copyFilePath, mayaFileName + ".mp4")
            shutil.copyfile(src, dst)
            
        return True

    def openMergedFile(self):
        self._playblast.open_in_viewer(os.path.abspath(os.path.join(self.output_dir_path_le.text(), self.cutscene.getCutsceneName() + ".mp4")))

    def do_playblast(self):
        selectedShots = self.getSelectedShots()
        if not selectedShots:
            QtWidgets.QMessageBox.warning(self, "Playblast", "No Shots selected to Playblast.")
            return
        
        shotsWithoutCamera = []
        for shot in selectedShots:
            if not shot.camera:
                shotsWithoutCamera.append(shot)
        if shotsWithoutCamera:
            shotText = ""
            for shot in shotsWithoutCamera:
                shotText += "\n- {}".format(shot.shotName)
            QtWidgets.QMessageBox.warning(self, "Playblast", "Unable to perform playblast on shots without a camera assigned!\n" + shotText)
            return

        output_dir_path = self.output_dir_path_le.text()
        if not output_dir_path:
            output_dir_path = self.output_dir_path_le.placeholderText()
        output_dir_path = output_dir_path.replace("/", "\\")

        padding = ZurbriggPlayblast.DEFAULT_PADDING

        tempWindow = cmds.window()
        cmds.columnLayout()
        tempReporter = cmds.cmdScrollFieldReporter(width=200, height=100)
        cmds.cmdScrollFieldReporter(tempReporter, e = 1, clear = 1, fst = "", sw = 0)
        self.playblastCanceled = False
        
        if self.overlayInfoCheckbox.isChecked():
            playblastDrawer = PlayblastDrawer()
            ScreenDrawer.ScreenDrawerManager.registerScreenDrawer(playblastDrawer)

        cinematicGuides = CinematicGuides.CinematicGuides.instance()
        guidesEnabled = cinematicGuides.enabled
        if guidesEnabled != self.cinematicGuidesCheckbox.isChecked():
            cinematicGuides.enabled = self.cinematicGuidesCheckbox.isChecked()

        mayaFileName = self.getMayaFileName()
        if self.saveVersionCheckbox.isChecked() and mayaFileName != "":
            copyFilePath = os.path.join(output_dir_path, mayaFileName)
            if not os.path.isdir(copyFilePath):
                os.makedirs(copyFilePath)

        progressDialog = QtWidgets.QProgressDialog("Capturing Playblast...\n(Press the Esc key to cancel)", None, 0, len(selectedShots), self)
        progressDialog.setWindowTitle("Playblast")
        progressDialog.setWindowFlags(progressDialog.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        progressDialog.setWindowModality(QtCore.Qt.WindowModal)
        progressDialog.show()
        
        try:
            for i, shot in enumerate(selectedShots):
                progressDialog.setValue(i)
                QtWidgets.QApplication.processEvents()
                
                displayResolutionAttribute = "{}.displayResolution".format(shot.camera)
                resolutionDisplayed = cmds.getAttr(displayResolutionAttribute)
                cmds.setAttr(displayResolutionAttribute, False)

                shot.applyAnimLayers()
                if self.overlayInfoCheckbox.isChecked():
                    playblastDrawer.currentShot = shot
                    
                self._playblast.set_camera(shot.camera)
                self._playblast.set_frame_range([shot.start, shot.end])
                outputFile = self._playblast.execute(output_dir_path, shot.shotName, padding, False, False, False, True)
                
                if outputFile and self.saveVersionCheckbox.isChecked() and mayaFileName:
                    copyFileName = outputFile.replace(output_dir_path, copyFilePath)
                    shutil.copyfile(outputFile, copyFileName)

                cmds.setAttr(displayResolutionAttribute, resolutionDisplayed)
                
                text = cmds.cmdScrollFieldReporter(tempReporter, q = 1, text = 1)
                if self.playblastCanceled or text.find("Playblast was interrupted. File still created but may be incomplete.") > -1:
                    self.playblastCanceled = True
                    break

            progressDialog.setValue(len(selectedShots))
        
        finally:
            if self.overlayInfoCheckbox.isChecked():
                ScreenDrawer.ScreenDrawerManager.unregisterScreenDrawer(playblastDrawer)
            
            if guidesEnabled != self.cinematicGuidesCheckbox.isChecked():
                cinematicGuides.enabled = guidesEnabled
            

        cmds.deleteUI(tempWindow)
        if self.playblastCanceled:
            self._playblast.log_output("Playblast was interrupted.")
            return

        if self.mergeOptionsRadiobuttonGroup.checkedId() == 0:
            result = self.mergeShots(self.cutscene.getEnabledShots())
        elif self.mergeOptionsRadiobuttonGroup.checkedId() == 1:
            result = self.mergeShots(selectedShots)

        if result:
            if self.viewer_cb.isChecked():
                if self.mergeOptionsRadiobuttonGroup.checkedId() != 2:
                    self.openMergedFile()
                else:
                    cmds.confirmDialog(title="Merge", message="Playblast completed.\n\nThe option [Don't Merge] was selected\nso no video will be opened.")
            else:
                cmds.confirmDialog(title="Merge", message="Playblast completed.")

    def cancelPlayblast(self):
        self.playblastCanceled = True

    def setPlayblastFolder(self, folder, updateOptionVar=True):
        self.output_dir_path_le.setText(folder)
        self.output_dir_path_le.setToolTip(folder)
        
        if updateOptionVar:
            pathTokenizer = self.getPathTokenizer()
            tokenizedPath = pathTokenizer.Tokenize(folder)
            self.PLAYBLAST_FOLDER_OPTIONVAR.value = tokenizedPath

    def open_output_directory(self):
        playblastFolder = self.output_dir_path_le.text()
        if not os.path.isdir(playblastFolder):
            QtWidgets.QMessageBox.warning(self, "Open Folder", "Unable to open the folder: It doesn't exist yet!")
            return
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(playblastFolder))

    def onPathButtonPressed(self):
        selectedPath = cmds.fileDialog2(ds=1, fm=3, dir=self.output_dir_path_le.text())
        if selectedPath:
            self.setPlayblastFolder(selectedPath[0])

    def refresh(self):
        self.refreshPlayblastFolder()
        self.refresh_resolution()
        self.refresh_video_encoders()
        self.refresh_visibility()

    def refreshPlayblastFolder(self):
        pathTokenizer = self.getPathTokenizer()
        savePath = pathTokenizer.Translate(self.PLAYBLAST_FOLDER_OPTIONVAR.value)
        self.setPlayblastFolder(savePath, updateOptionVar=False)

    def refresh_resolution(self):
        resolution_preset = self.resolution_select_cmb.currentText()
        if resolution_preset != "Custom":
            self._playblast.set_resolution(resolution_preset)
            resolution = self._playblast.get_resolution_width_height()
        else:
            resolution = self.PLAYBLAST_VIDEO_RESOLUTION_OPTIONVAR.value
        
        self.resolution_width_sb.setValue(resolution[0])
        self.resolution_height_sb.setValue(resolution[1])
        
        self.onResolutionChanged()  # Won't be triggered by changing the spinners, since it's connected to de editingFinished signal, so we call it manually here

    def refresh_video_encoders(self):
        container = self.encoding_container_cmb.currentText()
        encoders = ZurbriggPlayblast.VIDEO_ENCODER_LOOKUP[container]
        
        signalsBlocked = self.encoding_video_codec_cmb.blockSignals(True)
        self.encoding_video_codec_cmb.clear()
        self.encoding_video_codec_cmb.addItems(encoders)
        self.encoding_video_codec_cmb.blockSignals(signalsBlocked)
        
        currentEncoder = self.PLAYBLAST_VIDEO_CODEC_PRESET_OPTIONVAR.value
        if currentEncoder not in encoders:
            currentEncoder = encoders[0]
            
        self.encoding_video_codec_cmb.setCurrentText(currentEncoder)

    def refresh_visibility(self):
        visibilityData = self.PLAYBLAST_VISIBILITY_OPTIONVAR.value
        self._playblast.set_visibility(visibilityData)
        
        for key in ZurbriggPlayblast.VIEWPORT_VISIBILITY_PRESETS.keys():
            if list(ZurbriggPlayblast.VIEWPORT_VISIBILITY_PRESETS[key]) == visibilityData:
                blockedSignals = self.visibility_cmb.blockSignals(True)
                self.visibility_cmb.setCurrentText(key)
                self.visibility_cmb.blockSignals(blockedSignals)
                return
            
        self.visibility_cmb.setCurrentText("Custom")
    
    def show_encoder_settings_dialog(self):
        if not self._encoder_settings_dialog:
            self._encoder_settings_dialog = ZurbriggPlayblastEncoderSettingsDialog(self)
            self._encoder_settings_dialog.accepted.connect(self.on_encoder_settings_dialog_modified)

        if self.encoding_container_cmb.currentText() == "Image":
            self._encoder_settings_dialog.set_page("Image")

            image_settings = self._playblast.get_image_settings()
            self._encoder_settings_dialog.set_image_settings(image_settings["quality"])

        else:
            encoder = self.encoding_video_codec_cmb.currentText()
            if encoder == "h264":
                self._encoder_settings_dialog.set_page("h264")

                h264_settings = self._playblast.get_h264_settings()
                self._encoder_settings_dialog.set_h264_settings(h264_settings["quality"], h264_settings["preset"])
            else:
                self._playblast.log_error("Settings page not found for encoder: {0}".format(encoder))

        self._encoder_settings_dialog.show()

    def on_encoder_settings_dialog_modified(self):
        if self.encoding_container_cmb.currentText() == "Image":
            image_settings = self._encoder_settings_dialog.get_image_settings()
            self._playblast.set_image_settings(image_settings["quality"])
        else:
            encoder = self.encoding_video_codec_cmb.currentText()
            if encoder == "h264":
                h264_settings = self._encoder_settings_dialog.get_h264_settings()
                self._playblast.set_h264_settings(h264_settings["quality"], h264_settings["preset"])
            else:
                self._playblast.log_error("Failed to set encoder settings. Unknown encoder: {0}".format(encoder))

    def show_visibility_dialog(self):
        if not self._visibility_dialog:
            self._visibility_dialog = ZurbriggPlayblastVisibilityDialog(self)
            self._visibility_dialog.accepted.connect(self.onVisibilityChanged)

        self._visibility_dialog.set_visibility_data(self._playblast.get_visibility())

        self._visibility_dialog.show()

    def save_defaults(self):
        cmds.optionVar(sv=("CinematicPlayblastUiResolutionPreset", self.resolution_select_cmb.currentText()))
        cmds.optionVar(iv=("CinematicPlayblastUiResolutionWidth", self.resolution_width_sb.value()))
        cmds.optionVar(iv=("CinematicPlayblastUiResolutionHeight", self.resolution_height_sb.value()))

        cmds.optionVar(sv=("CinematicPlayblastUiEncodingContainer", self.encoding_container_cmb.currentText()))
        cmds.optionVar(sv=("CinematicPlayblastUiEncodingVideoCodec", self.encoding_video_codec_cmb.currentText()))

        h264_settings = self._playblast.get_h264_settings()
        cmds.optionVar(sv=("CinematicPlayblastUiH264Quality", h264_settings["quality"]))
        cmds.optionVar(sv=("CinematicPlayblastUiH264Preset", h264_settings["preset"]))

        image_settings = self._playblast.get_image_settings()
        cmds.optionVar(iv=("CinematicPlayblastUiImageQuality", image_settings["quality"]))

        cmds.optionVar(sv=("CinematicPlayblastUiVisibilityPreset", self.visibility_cmb.currentText()))

        visibility_data = self._playblast.get_visibility()
        visibility_str = ""
        for item in visibility_data:
            visibility_str = "{0} {1}".format(visibility_str, int(item))
        cmds.optionVar(sv=("CinematicPlayblastUiVisibilityData", visibility_str))

        cmds.optionVar(iv=("CinematicPlayblastUiViewer", self.viewer_cb.isChecked()))

    def load_defaults(self):
        if cmds.optionVar(exists="CinematicPlayblastUiResolutionPreset"):
            self.resolution_select_cmb.setCurrentText(cmds.optionVar(q="CinematicPlayblastUiResolutionPreset"))
        if self.resolution_select_cmb.currentText() == "Custom":
            if cmds.optionVar(exists="CinematicPlayblastUiResolutionWidth"):
                self.resolution_width_sb.setValue(cmds.optionVar(q="CinematicPlayblastUiResolutionWidth"))
            if cmds.optionVar(exists="CinematicPlayblastUiResolutionHeight"):
                self.resolution_height_sb.setValue(cmds.optionVar(q="CinematicPlayblastUiResolutionHeight"))
            self.on_resolution_changed()

        if cmds.optionVar(exists="CinematicPlayblastUiEncodingContainer"):
            self.encoding_container_cmb.setCurrentText(cmds.optionVar(q="CinematicPlayblastUiEncodingContainer"))
        if cmds.optionVar(exists="CinematicPlayblastUiEncodingVideoCodec"):
            self.encoding_video_codec_cmb.setCurrentText(cmds.optionVar(q="CinematicPlayblastUiEncodingVideoCodec"))

        if cmds.optionVar(exists="CinematicPlayblastUiH264Quality") and cmds.optionVar(exists="CinematicPlayblastUiH264Preset"):
            self._playblast.set_h264_settings(cmds.optionVar(q="CinematicPlayblastUiH264Quality"), cmds.optionVar(q="CinematicPlayblastUiH264Preset"))

        if cmds.optionVar(exists="CinematicPlayblastUiImageQuality"):
            self._playblast.set_image_settings(cmds.optionVar(q="CinematicPlayblastUiImageQuality"))

        if cmds.optionVar(exists="CinematicPlayblastUiVisibilityPreset"):
            self.visibility_cmb.setCurrentText(cmds.optionVar(q="CinematicPlayblastUiVisibilityPreset"))
        if self.visibility_cmb.currentText() == "Custom":
            if cmds.optionVar(exists="CinematicPlayblastUiVisibilityData"):
                visibility_str_list = cmds.optionVar(q="CinematicPlayblastUiVisibilityData").split()
                visibility_data = []
                for item in visibility_str_list:
                    if item:
                        visibility_data.append(bool(int(item)))

                self._playblast.set_visibility(visibility_data)

        if cmds.optionVar(exists="CinematicPlayblastUiViewer"):
            self.viewer_cb.setChecked(cmds.optionVar(q="CinematicPlayblastUiViewer"))

    def keyPressEvent(self, event):
        super(CinematicPlayblastUI, self).keyPressEvent(event)

        event.accept()

    def showEvent(self, event):
        self.refresh()


class ZurbriggPlayblastVisibilityDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(ZurbriggPlayblastVisibilityDialog, self).__init__(parent)

        self.setWindowTitle("Customize Visibility")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)

        visibility_layout = QtWidgets.QGridLayout()

        index = 0
        self.visibility_checkboxes = []

        for i in range(len(ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP)):
            checkbox = QtWidgets.QCheckBox(ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP[i][0])

            visibility_layout.addWidget(checkbox, index / 3, index % 3)
            self.visibility_checkboxes.append(checkbox)

            index += 1

        visibility_grp = QtWidgets.QGroupBox("")
        visibility_grp.setLayout(visibility_layout)

        apply_btn = QtWidgets.QPushButton("Apply")
        apply_btn.clicked.connect(self.accept)

        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(4, 4, 4, 4)
        main_layout.setSpacing(4)
        main_layout.addWidget(visibility_grp)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def get_visibility_data(self):
        data = []
        for checkbox in self.visibility_checkboxes:
            data.append(checkbox.isChecked())

        return data

    def set_visibility_data(self, data):
        if len(self.visibility_checkboxes) != len(data):
            raise RuntimeError("Visibility property/data mismatch")

        for i in range(len(data)):
            self.visibility_checkboxes[i].setChecked(data[i])


class ZurbriggPlayblastEncoderSettingsDialog(QtWidgets.QDialog):
    
    ENCODER_PAGES = {
        "h264": 0,
        "Image": 1,
    }

    H264_QUALITIES = [
        "Very High",
        "High",
        "Medium",
        "Low",
    ]


    def __init__(self, parent):
        super(ZurbriggPlayblastEncoderSettingsDialog, self).__init__(parent)

        self.setWindowTitle("Encoder Settings")
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setModal(True)
        self.setMinimumWidth(220)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        # h264
        self.h264_quality_combo = QtWidgets.QComboBox()
        self.h264_quality_combo.addItems(ZurbriggPlayblastEncoderSettingsDialog.H264_QUALITIES)

        self.h264_preset_combo = QtWidgets.QComboBox()
        self.h264_preset_combo.addItems(ZurbriggPlayblast.H264_PRESETS)

        h264_layout = QtWidgets.QFormLayout()
        h264_layout.addRow("Quality:", self.h264_quality_combo)
        h264_layout.addRow("Preset:", self.h264_preset_combo)

        h264_settings_wdg = QtWidgets.QGroupBox("h264 Options")
        h264_settings_wdg.setLayout(h264_layout)

        # image
        self.image_quality_sb = QtWidgets.QSpinBox()
        self.image_quality_sb.setMinimumWidth(40)
        self.image_quality_sb.setButtonSymbols(QtWidgets.QSpinBox.NoButtons)
        self.image_quality_sb.setMinimum(1)
        self.image_quality_sb.setMaximum(100)

        image_layout = QtWidgets.QFormLayout()
        image_layout.addRow("Quality:", self.image_quality_sb)

        image_settings_wdg = QtWidgets.QGroupBox("Image Options")
        image_settings_wdg.setLayout(image_layout)

        self.settings_stacked_wdg = QtWidgets.QStackedWidget()
        self.settings_stacked_wdg.addWidget(h264_settings_wdg)
        self.settings_stacked_wdg.addWidget(image_settings_wdg)

        self.accept_btn = QtWidgets.QPushButton("Accept")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.accept_btn)
        button_layout.addWidget(self.cancel_btn)
        # button_layout.addWidget(self.merge_btn)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(4)
        main_layout.addWidget(self.settings_stacked_wdg)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.accept_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.close)
    
    
    
    def set_page(self, page):
        if not page in ZurbriggPlayblastEncoderSettingsDialog.ENCODER_PAGES:
            return False

        self.settings_stacked_wdg.setCurrentIndex(ZurbriggPlayblastEncoderSettingsDialog.ENCODER_PAGES[page])
        return True

    def set_h264_settings(self, quality, preset):
        self.h264_quality_combo.setCurrentText(quality)
        self.h264_preset_combo.setCurrentText(preset)

    def get_h264_settings(self):
        return {
            "quality": self.h264_quality_combo.currentText(),
            "preset": self.h264_preset_combo.currentText(),
        }

    def set_image_settings(self, quality):
        self.image_quality_sb.setValue(quality)

    def get_image_settings(self):
        return {
            "quality": self.image_quality_sb.value(),
        }


class ZurbriggPlayblast():
    RESOLUTION_LOOKUP = {
        "Render": (),
        "HD 1080": (1920, 1080),
        "HD 720": (1280, 720),
        "HD 540": (960, 540),
    }

    FRAME_RANGE_PRESETS = [
        "Render",
        "Playback",
        "Animation",
    ]

    VIDEO_ENCODER_LOOKUP = {
        "mov": ["h264"],
        "mp4": ["h264"],
        "Image": ["jpg", "png", "tif"],
    }

    H264_QUALITIES = {
        "Very High": 18,
        "High": 20,
        "Medium": 23,
        "Low": 26,
    }

    H264_PRESETS = [
        "veryslow",
        "slow",
        "medium",
        "fast",
        "faster",
        "ultrafast",
    ]

    VIEWPORT_VISIBILITY_LOOKUP = [
        ["Controllers", "controllers"],
        ["NURBS Curves", "nurbsCurves"],
        ["NURBS Surfaces", "nurbsSurfaces"],
        ["NURBS CVs", "cv"],
        ["NURBS Hulls", "hulls"],
        ["Polygons", "polymeshes"],
        ["Subdiv Surfaces", "subdivSurfaces"],
        ["Planes", "planes"],
        ["Lights", "lights"],
        ["Cameras", "cameras"],
        ["Image Planes", "imagePlane"],
        ["Joints", "joints"],
        ["IK Handles", "ikHandles"],
        ["Deformers", "deformers"],
        ["Dynamics", "dynamics"],
        ["Particle Instancers", "particleInstancers"],
        ["Fluids", "fluids"],
        ["Hair Systems", "hairSystems"],
        ["Follicles", "follicles"],
        ["nCloths", "nCloths"],
        ["nParticles", "nParticles"],
        ["nRigids", "nRigids"],
        ["Dynamic Constraints", "dynamicConstraints"],
        ["Locators", "locators"],
        ["Dimensions", "dimensions"],
        ["Pivots", "pivots"],
        ["Handles", "handles"],
        ["Texture Placements", "textures"],
        ["Strokes", "strokes"],
        ["Motion Trails", "motionTrails"],
        ["Plugin Shapes", "pluginShapes"],
        ["Clip Ghosts", "clipGhosts"],
        ["Grease Pencil", "greasePencils"],
        ["Grid", "grid"],
        ["HUD", "hud"],
        ["Hold-Outs", "hos"],
        ["Selection Highlighting", "sel"],
    ]

    VIEWPORT_VISIBILITY_PRESETS = {
        "Geometry": ["NURBS Surfaces", "Polygons"],
        "Viewport": [],
        "Dynamics": ["NURBS Surfaces", "Polygons", "Dynamics", "Fluids", "nParticles"],
    }

    DEFAULT_CONTAINER = "mp4"
    DEFAULT_ENCODER = "h264"
    DEFAULT_H264_QUALITY = "High"
    DEFAULT_H264_PRESET = "fast"
    DEFAULT_IMAGE_QUALITY = 100

    DEFAULT_VISIBILITY = "Geometry"

    DEFAULT_PADDING = 4


    def __init__(self, ffmpeg_path=None, log_to_maya=True):
        self.set_ffmpeg_path(ffmpeg_path)
        self.set_maya_logging_enabled(log_to_maya)

        self.set_encoding(ZurbriggPlayblast.DEFAULT_CONTAINER, ZurbriggPlayblast.DEFAULT_ENCODER)
        self.set_h264_settings(ZurbriggPlayblast.DEFAULT_H264_QUALITY, ZurbriggPlayblast.DEFAULT_H264_PRESET)
        self.set_image_settings(ZurbriggPlayblast.DEFAULT_IMAGE_QUALITY)

        self.set_visibility(ZurbriggPlayblast.DEFAULT_VISIBILITY)

        self.initialize_ffmpeg_process()

    def set_ffmpeg_path(self, ffmpeg_path):
        self._ffmpeg_path = ffmpeg_path

    def get_ffmpeg_path(self):
        return self._ffmpeg_path

    def set_maya_logging_enabled(self, enabled):
        self._log_to_maya = enabled

    def set_camera(self, camera):
        self.log_output('Using camera: {}'.format(camera))
        self._camera = camera

    def set_resolution(self, resolution):
        self._resolution_preset = None

        try:
            widthHeight = self.preset_to_resolution(resolution)
            self._resolution_preset = resolution
        except:
            widthHeight = resolution

        valid_resolution = True
        try:
            if not (isinstance(widthHeight[0], int) and isinstance(widthHeight[1], int)):
                valid_resolution = False
        except:
            valid_resolution = False

        if valid_resolution:
            if widthHeight[0] <=0 or widthHeight[1] <= 0:
                self.log_error("Invalid resolution: {0}. Values must be greater than zero.".format(widthHeight))
                return
        else:
            presets = []
            for preset in ZurbriggPlayblast.RESOLUTION_LOOKUP.keys():
                presets.append("'{0}'".format(preset))

            self.log_error("Invalid resoluton: {0}. Expected one of [int, int], {1}".format(widthHeight, ", ".join(presets)))
            return

        self._widthHeight = (widthHeight[0], widthHeight[1])

    def get_resolution_width_height(self):
        if self._resolution_preset:
            return self.preset_to_resolution(self._resolution_preset)

        return self._widthHeight

    def preset_to_resolution(self, resolution_preset):
        if resolution_preset == "Render":
            width = cmds.getAttr("defaultResolution.width")
            height = cmds.getAttr("defaultResolution.height")
            return (width, height)
        elif resolution_preset in ZurbriggPlayblast.RESOLUTION_LOOKUP.keys():
            return ZurbriggPlayblast.RESOLUTION_LOOKUP[resolution_preset]
        else:
            raise RuntimeError("Invalid resolution preset: {0}".format(resolution_preset))

    def set_frame_range(self, frame_range):
        resolved_frame_range = self.resolve_frame_range(frame_range)
        if not resolved_frame_range:
            return

        self._frame_range_preset = None
        if frame_range in ZurbriggPlayblast.FRAME_RANGE_PRESETS:
            self._frame_range_preset = frame_range

        self._start_frame = resolved_frame_range[0]
        self._end_frame = resolved_frame_range[1]

    def get_start_end_frame(self):
        if self._frame_range_preset:
            return self.preset_to_frame_range(self._frame_range_preset)

        return (self._start_frame, self._end_frame)

    def resolve_frame_range(self, frame_range):
        try:
            if type(frame_range) in [list, tuple]:
                start_frame = frame_range[0]
                end_frame = frame_range[1]
            else:
                start_frame, end_frame = self.preset_to_frame_range(frame_range)

            return (start_frame, end_frame)

        except:
            presets = []
            for preset in ZurbriggPlayblast.FRAME_RANGE_PRESETS:
                presets.append("'{0}'".format(preset))
            self.log_error('Invalid frame range. Expected one of (start_frame, end_frame), {0}'.format(", ".join(presets)))

        return None

    def preset_to_frame_range(self, frame_range_preset):
        if frame_range_preset == "Render":
            start_frame = int(cmds.getAttr("defaultRenderGlobals.startFrame"))
            end_frame = int(cmds.getAttr("defaultRenderGlobals.endFrame"))
        elif frame_range_preset == "Playback":
            start_frame = int(cmds.playbackOptions(q=True, minTime=True))
            end_frame = int(cmds.playbackOptions(q=True, maxTime=True))
        elif frame_range_preset == "Animation":
            start_frame = int(cmds.playbackOptions(q=True, animationStartTime=True))
            end_frame = int(cmds.playbackOptions(q=True, animationEndTime=True))
        else:
            raise RuntimeError("Invalid frame range preset: {0}".format(frame_range_preset))

        return (start_frame, end_frame)

    def set_visibility(self, visibility_data):
        if not visibility_data:
            visibility_data = []

        if not type(visibility_data) in [list, tuple]:
            visibility_data = self.preset_to_visibility(visibility_data)
            if visibility_data is None:
                return
            
        elif not visibility_data or type(visibility_data[0]) is not bool:
            visibility_data = [data[0] in visibility_data for data in ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP]

        self._visibility = copy.copy(visibility_data)

    def get_visibility(self):
        if not self._visibility:
            return self.get_viewport_visibility()

        return self._visibility

    def preset_to_visibility(self, visibility_preset):
        if not visibility_preset in ZurbriggPlayblast.VIEWPORT_VISIBILITY_PRESETS.keys():
            self.log_error("Invaild visibility preset: {0}".format(visibility_preset))
            return None

        visibility_data = []

        preset_names = ZurbriggPlayblast.VIEWPORT_VISIBILITY_PRESETS[visibility_preset]
        if preset_names:
            for lookup_item in ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP:
                visibility_data.append(lookup_item[0] in preset_names)

        return visibility_data

    def visibility_to_preset(self, visibility_data):
        visibility_preset = []
        for i, data in enumerate(visibility_data):
            if data:
                visibility_preset.append(ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP[i][0])
        return visibility_preset

    def get_viewport_visibility(self):
        model_panel = self.get_viewport_panel()
        if not model_panel:
            self.log_error("Failed to get viewport visibility. A viewport is not active.")
            return None

        viewport_visibility = []
        try:
            for item in ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP:
                kwargs = {item[1]: True}
                viewport_visibility.append(cmds.modelEditor(model_panel, q=True, **kwargs))
        except:
            traceback.print_exc()
            self.log_error("Failed to get active viewport visibility. See script editor for details.")
            return None

        return viewport_visibility

    def set_viewport_visibility(self, model_editor, visibility_flags):
        cmds.modelEditor(model_editor, e=True, **visibility_flags)

    def create_viewport_visibility_flags(self, visibility_data):
        visibility_flags = {}

        data_index = 0
        for item in ZurbriggPlayblast.VIEWPORT_VISIBILITY_LOOKUP:
            visibility_flags[item[1]] = visibility_data[data_index]
            data_index += 1

        return visibility_flags

    def set_encoding(self, container_format, encoder):
        if container_format not in ZurbriggPlayblast.VIDEO_ENCODER_LOOKUP.keys():
            self.log_error("Invalid container: {0}. Expected one of {1}".format(container_format, ZurbriggPlayblast.VIDEO_ENCODER_LOOKUP.keys()))
            return

        if encoder not in ZurbriggPlayblast.VIDEO_ENCODER_LOOKUP[container_format]:
            self.log_error("Invalid encoder: {0}. Expected one of {1}".format(encoder, ZurbriggPlayblast.VIDEO_ENCODER_LOOKUP[container_format]))
            return

        self._container_format = container_format
        self._encoder = encoder

    def set_h264_settings(self, quality, preset):
        if not quality in ZurbriggPlayblast.H264_QUALITIES.keys():
            self.log_error("Invalid h264 quality: {0}. Expected one of {1}".format(quality, ZurbriggPlayblast.H264_QUALITIES.keys()))
            return

        if not preset in ZurbriggPlayblast.H264_PRESETS:
            self.log_error("Invalid h264 preset: {0}. Expected one of {1}".format(preset, ZurbriggPlayblast.H264_PRESETS))
            return

        self._h264_quality = quality
        self._h264_preset = preset

    def get_h264_settings(self):
        return {
            "quality": self._h264_quality,
            "preset": self._h264_preset,
        }

    def set_image_settings(self, quality):
        if quality > 0 and quality <= 100:
            self._image_quality = quality
        else:
            self.log_error("Invalid image quality: {0}. Expected value between 1-100")

    def get_image_settings(self):
        return {
            "quality": self._image_quality,
        }

    def execute(self, output_dir, filename, padding=4, overscan=False, show_ornaments=True, show_in_viewer=True, overwrite=False):

        if self.requires_ffmpeg() and not self.validate_ffmpeg():
            self.log_error("ffmpeg executable is not configured. See script editor for details.")
            return ""
        viewport_model_panel = self.get_viewport_panel()
        if not viewport_model_panel:
            self.log_error("An active viewport is not selected. Select a viewport and retry.")
            return ""

        if not output_dir:
            self.log_error("Output directory path not set")
            return ""
        if not filename:
            self.log_error("Output file name not set")
            return ""

        output_dir = self.resolve_output_directory_path(output_dir)
        filename = self.resolve_output_filename(filename)

        if padding <= 0:
            padding = ZurbriggPlayblast.DEFAULT_PADDING

        if self.requires_ffmpeg():
            output_path = os.path.normpath(os.path.join(output_dir, "{0}.{1}".format(filename, self._container_format)))
            if not overwrite and os.path.exists(output_path):
                self.log_error("Output file already exists. Eanble overwrite to ignore.")
                return ""

            playblast_output_dir = "{0}/playblast_temp".format(output_dir)
            playblast_output = os.path.normpath(os.path.join(playblast_output_dir, filename))
            force_overwrite = True
            compression = "png"
            image_quality = 100
            index_from_zero = True
            viewer = False
        else:
            playblast_output = os.path.normpath(os.path.join(output_dir, filename))
            force_overwrite = overwrite
            compression = self._encoder
            image_quality = self._image_quality
            index_from_zero = False
            viewer = show_in_viewer

        widthHeight = self.get_resolution_width_height()
        start_frame, end_frame = self.get_start_end_frame()

        options = {
            "filename": playblast_output,
            "widthHeight": widthHeight,
            "percent": 100,
            "startTime": start_frame,
            "endTime": end_frame,
            "clearCache": True,
            "forceOverwrite": force_overwrite,
            "format": "image",
            "compression": compression,
            "quality": image_quality,
            "indexFromZero": index_from_zero,
            "framePadding": padding,
            "showOrnaments": show_ornaments,
            "viewer": viewer,
        }

        self.log_output("Playblast options: {0}".format(options))

        # Store original viewport settings
        orig_camera = self.get_active_camera()

        camera = self._camera
        if not camera:
            camera = orig_camera

        if not camera:
            self.log_error("Camera does not exist: {0}".format(camera))
            return ""

        self.set_active_camera(camera)

        orig_visibility_flags = self.create_viewport_visibility_flags(self.get_viewport_visibility())
        playblast_visibility_flags = self.create_viewport_visibility_flags(self.get_visibility())
            
        model_editor = cmds.modelPanel(viewport_model_panel, q=True, modelEditor=True)
        self.set_viewport_visibility(model_editor, playblast_visibility_flags)
        
        # Store original camera settings
        orig_overscan = None
        if not overscan:
            overscan_attr = "{0}.overscan".format(camera)
            if not cmds.getAttr(overscan_attr, l=True):
                orig_overscan = cmds.getAttr(overscan_attr)
                cmds.setAttr(overscan_attr, 1.0)

        playblast_failed = False
        try:
            cmds.playblast(**options)
        except:
            traceback.print_exc()
            playblast_failed = True
        finally:
            # Restore original camera settings
            if orig_overscan:
                cmds.setAttr(overscan_attr, orig_overscan)
            
            # Restore original viewport settings
            self.set_active_camera(orig_camera)
            self.set_viewport_visibility(model_editor, orig_visibility_flags)

        if playblast_failed:
            raise Exception("Failed to create playblast. See script editor for details.")

        if self.requires_ffmpeg():
            source_path = "{0}/{1}.%0{2}d.png".format(playblast_output_dir, filename, padding)

            if self._encoder == "h264":
                self.encode_h264(source_path, output_path, start_frame)
            else:
                self.remove_temp_dir(playblast_output_dir)
                raise Exception("Encoding failed. Unsupported encoder ({0}) for container ({1}).".format(self._encoder, self._container_format))

            self.remove_temp_dir(playblast_output_dir)

            if show_in_viewer:
                self.open_in_viewer(output_path)

        return output_path

    def remove_temp_dir(self, temp_dir_path):
        playblast_dir = QtCore.QDir(temp_dir_path)
        playblast_dir.setNameFilters(["*.png"])
        playblast_dir.setFilter(QtCore.QDir.Files)
        for f in playblast_dir.entryList():
            playblast_dir.remove(f)

        if not playblast_dir.rmdir(temp_dir_path):
            self.log_warning("Failed to remove temporary directory: {0}".format(temp_dir_path))

    def open_in_viewer(self, path):
        if not os.path.exists(path):
            self.log_error("Failed to open in viewer. File does not exists: {0}".format(path))
            return

        if self._container_format in ("mov", "mp4") and cmds.optionVar(exists="PlayblastCmdQuicktime"):
            executable_path = cmds.optionVar(q="PlayblastCmdQuicktime")
            if executable_path:
                QtCore.QProcess.startDetached(executable_path, [path])
                return

        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(path))

    def requires_ffmpeg(self):
        return self._container_format != "Image"

    def validate_ffmpeg(self):
        if not self._ffmpeg_path:
            self.log_error("ffmpeg executable path not set")
            return False
        elif not os.path.exists(self._ffmpeg_path):
            self.log_error("ffmpeg executable path does not exist: {0}".format(self._ffmpeg_path))
            return False
        elif os.path.isdir(self._ffmpeg_path):
            self.log_error("Invalid ffmpeg path: {0}".format(self._ffmpeg_path))
            return False

        return True

    def initialize_ffmpeg_process(self):
        self._ffmpeg_process = QtCore.QProcess()
        #self._ffmpeg_process.readyReadStandardError.connect(self.process_ffmpeg_output)

    def execute_ffmpeg_command(self, command):
        self._ffmpeg_process.start(command)
        if self._ffmpeg_process.waitForStarted():
            while self._ffmpeg_process.state() != QtCore.QProcess.NotRunning:
                QtCore.QCoreApplication.processEvents()
                QtCore.QThread.usleep(10)

    def process_ffmpeg_output(self):
        byte_array_output = self._ffmpeg_process.readAllStandardError()

        if sys.version_info.major < 3:
            output = str(byte_array_output)
        else:
            output = str(byte_array_output, "utf-8")

        self.log_output(output)

    def encode_h264(self, source_path, output_path, start_frame):
        framerate = self.get_frame_rate()
        #self.log_output('SOURCE PATH IS {}'.format(source_path))
        audio_file_path, audio_frame_offset = self.get_audio_attributes()
        if audio_file_path:
            audio_offset = self.get_audio_offset_in_sec(start_frame, audio_frame_offset, framerate)

        crf = ZurbriggPlayblast.H264_QUALITIES[self._h264_quality]
        preset = self._h264_preset

        ffmpeg_cmd = self._ffmpeg_path
        ffmpeg_cmd += ' -y -framerate {0} -i "{1}"'.format(framerate, source_path)

        if audio_file_path:
            ffmpeg_cmd += ' -ss {0} -i "{1}"'.format(audio_offset, audio_file_path)

        ffmpeg_cmd += ' -c:v libx264 -crf:v {0} -preset:v {1} -profile high -level 4.0 -pix_fmt yuv420p'.format(crf, preset)

        if audio_file_path:
            ffmpeg_cmd += ' -filter_complex "[1:0] apad" -shortest'

        ffmpeg_cmd += ' "{0}"'.format(output_path)

        #self.log_output(ffmpeg_cmd)

        self.execute_ffmpeg_command(ffmpeg_cmd)

    def merge(self, outputFolder, outputFile, fileList):
        self.create_file_list(outputFolder, fileList)
        ffmpeg_cmd = self._ffmpeg_path
        file_list_path = os.path.abspath(os.path.join(outputFolder, 'filelist.txt'))
        output_path = os.path.abspath(os.path.join(outputFolder, outputFile))
        ffmpeg_cmd += ' -y -f concat -safe 0 -i \"{0}\" -c copy \"{1}\"'.format(file_list_path, output_path)
        
        self.log_output(ffmpeg_cmd)

        self.execute_ffmpeg_command(ffmpeg_cmd)

        os.remove(file_list_path)
        
    def create_file_list(self, outputFolder, fileList):    
        toWrite = ""
        for v_s in fileList:
            toWrite += "file \'{}\'".format(os.path.abspath(os.path.join(outputFolder, v_s)))
            toWrite += "\n"

        filePath = os.path.join(outputFolder, "filelist.txt")
        with open(filePath, "w") as file:
            file.write(toWrite)
        
    def get_frame_rate(self):
        rate_str = cmds.currentUnit(q=True, time=True)

        if rate_str == "game":
            frame_rate = 15.0
        elif rate_str == "film":
            frame_rate = 24.0
        elif rate_str == "pal":
            frame_rate = 25.0
        elif rate_str == "ntsc":
            frame_rate = 30.0
        elif rate_str == "show":
            frame_rate = 48.0
        elif rate_str == "palf":
            frame_rate = 50.0
        elif rate_str == "ntscf":
            frame_rate = 60.0
        elif rate_str.endswith("fps"):
            frame_rate = float(rate_str[0:-3])
        else:
            raise RuntimeError("Unsupported frame rate: {0}".format(rate_str))

        return frame_rate

    def get_audio_attributes(self):
        sound_node = mel.eval("timeControl -q -sound $gPlayBackSlider;")
        if sound_node:
            file_path = cmds.getAttr("{0}.filename".format(sound_node))
            file_info = QtCore.QFileInfo(file_path)
            if file_info.exists():
                offset = cmds.getAttr("{0}.offset".format(sound_node))

                return (file_path, offset)

        return (None, None)

    def get_audio_offset_in_sec(self, start_frame, audio_frame_offset, frame_rate):
        return (start_frame - audio_frame_offset) / frame_rate

    def resolve_output_directory_path(self, dir_path):
        if "{project}" in dir_path:
            dir_path = dir_path.replace("{project}", self.get_project_dir_path())

        return dir_path

    def resolve_output_filename(self, filename):
        if "{scene}" in filename:
            filename = filename.replace("{scene}", self.get_scene_name())

        return filename

    def get_project_dir_path(self):
        return cmds.workspace(q=True, rootDirectory=True)

    def get_scene_name(self):
        scene_name = cmds.file(q=True, sceneName=True, shortName=True)
        if scene_name:
            scene_name = os.path.splitext(scene_name)[0]
        else:
            scene_name = "untitled"

        return scene_name

    def get_viewport_panel(self):
        model_panel = cmds.playblast(ae=True)
        if model_panel:
            return model_panel.split("|")[-1]
        return None

    def get_active_camera(self):
        model_panel = self.get_viewport_panel()
        if not model_panel:
            self.log_error("Failed to get active camera. A viewport is not active.")
            return None

        return cmds.modelPanel(model_panel, q=True, camera=True)

    def set_active_camera(self, camera):
        model_panel = self.get_viewport_panel()
        if not model_panel:
            self.log_error("Failed to set active camera. A viewport is not active.")
            return None
        
        return cmds.modelPanel(model_panel, e=True, camera=camera)

    def log_error(self, text):
        if self._log_to_maya:
            OpenMaya.MGlobal.displayError(text)

    def log_warning(self, text):
        if self._log_to_maya:
            OpenMaya.MGlobal.displayWarning(text)

    def log_output(self, text):
        if self._log_to_maya:
            OpenMaya.MGlobal.displayInfo(text)
