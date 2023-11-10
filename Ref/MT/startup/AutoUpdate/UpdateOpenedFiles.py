import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

from PySide2 import QtWidgets

import AutoUpdate.Utils as UpdateUtils
import AutoUpdate.UpdateCreatedReferences as UpdateCreatedReferences


class UpdateOpenedFiles():
    
    filePreOpenCallback = None
    
    @classmethod
    def onPreSceneOpened(cls, fileObject, data, onStartup=False):
        if fileObject:
            file = fileObject.resolvedFullName()
        else:
            file = cmds.file(q=True, sn=True)
        
        if not UpdateUtils.isFileUpToDate(file):
            if not UpdateUtils.isFileVersionIgnored(file):
                messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Update File", file)
                messageBox.setInformativeText("The file you are trying to open is out of date. Do you want to get the last revision?")
                messageBox.setDetailedText(UpdateUtils.getFileRevisionDescription(file))
                
                updateButton = messageBox.addButton("Update", QtWidgets.QMessageBox.RejectRole)
                dontUpdateButton = messageBox.addButton("Don't Update", QtWidgets.QMessageBox.RejectRole)
                ignoreVersionButton = messageBox.addButton("Ignore this version", QtWidgets.QMessageBox.RejectRole)
                dontOpenButton = messageBox.addButton("Don't Open", QtWidgets.QMessageBox.RejectRole) if not onStartup else None
                
                updateButton.setToolTip("Gets the file's Last Revision and opens it.")
                dontUpdateButton.setToolTip("Opens the file without updating it.")
                ignoreVersionButton.setToolTip("Opens the file without updating it and never asks again for this version.")
                if dontOpenButton:
                    dontOpenButton.setToolTip("Aborts opening the file. The file is not updated.")
                
                messageBox.setDefaultButton(updateButton)
                messageBox.setEscapeButton(dontUpdateButton)
                
                messageBox.exec()
                clickedButton = messageBox.clickedButton()
                if clickedButton == updateButton:
                    UpdateUtils.updateFile(file)
                    if onStartup:
                        cmds.file(file, open=True, force=True)
                        return False
                elif clickedButton == ignoreVersionButton:
                    UpdateUtils.ignoreFileVersion(file)
                elif clickedButton == dontOpenButton:
                    return False
                
            else:
                cmds.warning("Opened File needed update but was ignored by user: {}".format(file))
        
        UpdateCreatedReferences.UpdateCreatedReferences.enabled = False
        cmds.evalDeferred(cls.afterSceneOpened)
        
        return True
    
    @classmethod
    def afterSceneOpened(cls):
        UpdateCreatedReferences.UpdateCreatedReferences.enabled = True
    
    @classmethod
    def initialize(cls):
        cls.filePreOpenCallback = OpenMaya.MSceneMessage.addCheckFileCallback(OpenMaya.MSceneMessage.kBeforeOpenCheck, cls.onPreSceneOpened)
        
    @classmethod
    def uninitialize(cls):
        OpenMaya.MMessage.removeCallback(cls.filePreOpenCallback)
