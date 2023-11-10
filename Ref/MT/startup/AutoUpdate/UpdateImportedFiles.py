import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

from PySide2 import QtWidgets

import AutoUpdate.Utils as UpdateUtils
import AutoUpdate.UpdateCreatedReferences as UpdateCreatedReferences
import AutoUpdate.UpdateFileReferences as UpdateFileReferences


class UpdateImportedFiles():
    
    filePreImportCallback = None
    
    @classmethod
    def onPreImportFile(cls, fileObject, data):
        file = fileObject.resolvedFullName()
        
        if not UpdateUtils.isFileUpToDate(file):
            if not UpdateUtils.isFileVersionIgnored(file):
                messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Update File", file)
                messageBox.setInformativeText("The file you are trying to import is out of date. Do you want to get the last revision?")
                messageBox.setDetailedText(UpdateUtils.getFileRevisionDescription(file))
                
                updateButton = messageBox.addButton("Update", QtWidgets.QMessageBox.RejectRole)
                dontUpdateButton = messageBox.addButton("Don't Update", QtWidgets.QMessageBox.RejectRole)
                ignoreVersionButton = messageBox.addButton("Ignore this version", QtWidgets.QMessageBox.RejectRole)
                dontimportFileButton = messageBox.addButton("Don't Import", QtWidgets.QMessageBox.RejectRole)
                
                updateButton.setToolTip("Gets the file's Last Revision and imports it.")
                dontUpdateButton.setToolTip("Imports the file without updating it.")
                ignoreVersionButton.setToolTip("Imports the file without updating it and never asks again for this version.")
                dontimportFileButton.setToolTip("Aborts importing the file. The file is not updated.")
                
                messageBox.setDefaultButton(updateButton)
                messageBox.setEscapeButton(dontUpdateButton)
                
                messageBox.exec()
                clickedButton = messageBox.clickedButton()
                if clickedButton == updateButton:
                    UpdateUtils.updateFile(file)
                elif clickedButton == ignoreVersionButton:
                    UpdateUtils.ignoreFileVersion(file)
                elif clickedButton == dontimportFileButton:
                    return False
                
            else:
                cmds.warning("Imported File needed update but was ignored by user: {}".format(file))
        
        UpdateCreatedReferences.UpdateCreatedReferences.enabled = False
        cmds.evalDeferred(cls.updateImportedReferences)
        
        return True
    
    @classmethod
    def updateImportedReferences(cls):
        UpdateCreatedReferences.UpdateCreatedReferences.enabled = True
        UpdateFileReferences.UpdateFileReferences.updateFileReferences()
    
    @classmethod
    def initialize(cls):
        cls.filePreImportCallback = OpenMaya.MSceneMessage.addCheckFileCallback(OpenMaya.MSceneMessage.kBeforeImportCheck, cls.onPreImportFile)
        
    @classmethod
    def uninitialize(cls):
        OpenMaya.MMessage.removeCallback(cls.filePreImportCallback)
