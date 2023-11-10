import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

from PySide2 import QtWidgets

import AutoUpdate.Utils as UpdateUtils


class UpdateCreatedReferences():
    
    referencePreCreateCallback = None
    
    enabled = True
    
    @classmethod
    def onPreReferenceCreated(cls, fileObject, data):
        if cls.enabled:
            file = fileObject.resolvedFullName()
            
            if not UpdateUtils.isFileUpToDate(file):
                if not UpdateUtils.isFileVersionIgnored(file):
                    messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Update File", file)
                    messageBox.setInformativeText("The file you are trying to reference is out of date. Do you want to get the last revision?")
                    messageBox.setDetailedText(UpdateUtils.getFileRevisionDescription(file))
                    
                    updateButton = messageBox.addButton("Update", QtWidgets.QMessageBox.RejectRole)
                    dontUpdateButton = messageBox.addButton("Don't Update", QtWidgets.QMessageBox.RejectRole)
                    ignoreVersionButton = messageBox.addButton("Ignore this version", QtWidgets.QMessageBox.RejectRole)
                    dontCreateReferenceButton = messageBox.addButton("Don't Reference", QtWidgets.QMessageBox.RejectRole)
                    
                    updateButton.setToolTip("Gets the file's Last Revision and references it.")
                    dontUpdateButton.setToolTip("References the file without updating it.")
                    ignoreVersionButton.setToolTip("References the file without updating it and never asks again for this version.")
                    dontCreateReferenceButton.setToolTip("Aborts creating the reference. The file is not updated.")
                    
                    messageBox.setDefaultButton(updateButton)
                    messageBox.setEscapeButton(dontUpdateButton)
                    
                    messageBox.exec()
                    clickedButton = messageBox.clickedButton()
                    if clickedButton == updateButton:
                        UpdateUtils.updateFile(file)
                    elif clickedButton == ignoreVersionButton:
                        UpdateUtils.ignoreFileVersion(file)
                    elif clickedButton == dontCreateReferenceButton:
                        return False
                    
                else:
                    cmds.warning("Referenced File needed update but was ignored by user: {}".format(file))
        
        return True
    
    @classmethod
    def initialize(cls):
        cls.referencePreCreateCallback = OpenMaya.MSceneMessage.addCheckFileCallback(OpenMaya.MSceneMessage.kBeforeCreateReferenceCheck, cls.onPreReferenceCreated)
        
    @classmethod
    def uninitialize(cls):
        OpenMaya.MMessage.removeCallback(cls.referencePreCreateCallback)
