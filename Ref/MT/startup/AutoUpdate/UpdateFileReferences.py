import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

from PySide2 import QtCore, QtWidgets, QtGui
import QtCustomWidgets.CollapsiblePanel as CollapsiblePanel
import QtCustomWidgets.QtUtils as QtUtils

import AutoUpdate.Utils as UpdateUtils


class ReferenceUpdateDialog(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    def __init__(self, referenceFilesToUpdate, referenceFilesToSkip, parent=None):
        super().__init__(parent=parent)
        
        self.referenceFilesToUpdate = referenceFilesToUpdate
        self.referenceFilesToSkip = referenceFilesToSkip
        
        self.createUI()
        
    def createUI(self):
        self.setWindowTitle("Update References")
        
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        
        headerLabel = QtWidgets.QLabel("Some of the referenced files are out of date:")
        mainLayout.addWidget(headerLabel)

        self.fileList = QtWidgets.QFrame()
        fileListLayout = QtWidgets.QVBoxLayout()
        fileListLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        fileListLayout.setContentsMargins(4, 4, 4, 4)
        self.fileList.setLayout(fileListLayout)
        
        for referenceFile in self.referenceFilesToUpdate:
            referenceFileWidget = self.createReferenceFileWidget(referenceFile, checked=True)
            fileListLayout.addWidget(referenceFileWidget)
        
        for referenceFile in self.referenceFilesToSkip:
            referenceFileWidget = self.createReferenceFileWidget(referenceFile, checked=False)
            fileListLayout.addWidget(referenceFileWidget)
        
        fileListLayout.addStretch()
        
        fileListArea = QtWidgets.QScrollArea()
        fileListArea.setWidgetResizable(True)
        QtUtils.setPaletteColor(fileListArea, QtGui.QPalette.Background, QtGui.QColor.fromHsv(0, 0, 32))
        fileListArea.setWidget(self.fileList)
        mainLayout.addWidget(fileListArea)
        
        lowerButtonsLayout = QtWidgets.QHBoxLayout()
        lowerButtonsLayout.setAlignment(QtCore.Qt.AlignRight)
        mainLayout.addLayout(lowerButtonsLayout)
        
        updateSelectedReferencesButton = QtWidgets.QPushButton("Update Selected References")
        updateSelectedReferencesButton.clicked.connect(self.accept)
        lowerButtonsLayout.addWidget(updateSelectedReferencesButton)
        
        dontUpdateReferencesButton = QtWidgets.QPushButton("Don't Update References")
        dontUpdateReferencesButton.clicked.connect(self.reject)
        lowerButtonsLayout.addWidget(dontUpdateReferencesButton)
        
        self.ignoreSkippedReferencesCheckBox = QtWidgets.QCheckBox("Ignore this version for skipped files")
        self.ignoreSkippedReferencesCheckBox.setChecked(False)
        self.ignoreSkippedReferencesCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        mainLayout.addWidget(self.ignoreSkippedReferencesCheckBox)
        
    def createReferenceFileWidget(self, referenceFile, checked=True):
        widget = CollapsiblePanel.CollapsiblePanel(referenceFile, showCheckBox=True, checked=checked)
        widget.referenceFile = referenceFile
        widget.setBodyBackgroundColor(QtGui.QColor.fromHsv(0, 0, 64))
        widget.main_layout.setSpacing(0)
        widget.bodyLayout.setContentsMargins(4, 4, 4, 0)
        
        revisionLabel = QtWidgets.QLabel(UpdateUtils.getFileRevisionDescription(referenceFile))
        revisionLabel.setWordWrap(True)
        widget.addWidget(revisionLabel)
        
        widget.setExpanded(True)
        return widget
    
    def accept(self):
        for i in range(self.fileList.layout().count() - 1):
            widget = self.fileList.layout().itemAt(i).widget()
            if widget.isChecked():
                UpdateUtils.updateFile(widget.referenceFile)
            elif self.ignoreSkippedReferencesCheckBox.isChecked():
                UpdateUtils.ignoreFileVersion(widget.referenceFile)
        
        super().accept()
        
    def reject(self):
        if self.ignoreSkippedReferencesCheckBox.isChecked():
            for i in range(self.fileList.layout().count() - 1):
                widget = self.fileList.layout().itemAt(i).widget()
                UpdateUtils.ignoreFileVersion(widget.referenceFile)
        
        super().reject()
        

class UpdateFileReferences():
    
    fileOpenCallback = None
    
    @classmethod
    def updateFileReferences(cls, skipIgnored=True):
        references = cmds.ls(type="reference")
        referenceFilesToUpdate = set()
        referenceFilesToSkip = set()
        for reference in references:
            try:
                referenceFile = cmds.referenceQuery(reference, filename=True, withoutCopyNumber=True)
                if not UpdateUtils.isFileUpToDate(referenceFile):
                    if not (skipIgnored and UpdateUtils.isFileVersionIgnored(referenceFile)):
                        referenceFilesToUpdate.add(referenceFile)
                    else:
                        referenceFilesToSkip.add(referenceFile)
            except:
                cmds.warning("Reference node is not associated with a reference file: {}".format(reference))
            
        if referenceFilesToUpdate:
            dialog = ReferenceUpdateDialog(referenceFilesToUpdate, referenceFilesToSkip)
            dialog.setWindowModality(QtCore.Qt.WindowModal)
            dialog.show()
            
        elif referenceFilesToSkip:
            cmds.warning("Referenced Files needed update but where ignored by user: {}".format(referenceFilesToSkip))
    
    @classmethod
    def onSceneOpened(cls):
        cls.updateFileReferences()
        
    @classmethod
    def initialize(cls):
        cls.fileOpenCallback = cmds.scriptJob(e=("SceneOpened", cls.onSceneOpened))
        
    @classmethod
    def uninitialize(cls):
        cmds.scriptJob(k=cls.fileOpenCallback)
