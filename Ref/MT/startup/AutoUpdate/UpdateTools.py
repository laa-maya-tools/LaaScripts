import maya.cmds as cmds

from PySide2 import QtWidgets

import AutoUpdate.Utils as UpdateUtils

import ProjectPath


class UpdateTools():
    
    @classmethod
    def updateTools(cls, skipIgnored=True, mayRequireRestart=True):
        folder = ProjectPath.getCodeFolder()
        if not UpdateUtils.isFolderUpToDate(folder):
            if not (skipIgnored and UpdateUtils.isFolderVersionIgnored(folder)):
                messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Update Tools", "There seems to be tools out of date.")
                restartMessage = "May require you to restart Maya" if mayRequireRestart else "You won't need to restart Maya"
                messageBox.setInformativeText("Do you want to get the last revision? ({})".format(restartMessage))
                messageBox.setDetailedText(UpdateUtils.getFolderRevisionDescription(folder))
                
                updateButton = messageBox.addButton("Update", QtWidgets.QMessageBox.RejectRole)
                dontUpdateButton = messageBox.addButton("Don't Update", QtWidgets.QMessageBox.RejectRole)
                ignoreVersionButton = messageBox.addButton("Ignore this version", QtWidgets.QMessageBox.RejectRole)
                
                updateButton.setToolTip("Gets the Tools' Last Revision.")
                dontUpdateButton.setToolTip("Doesn't update the Tools.")
                ignoreVersionButton.setToolTip("Doesn't update the Tools and never asks again for this version.")
                
                messageBox.setDefaultButton(updateButton)
                messageBox.setEscapeButton(dontUpdateButton)
                
                messageBox.exec()
                clickedButton = messageBox.clickedButton()
                if clickedButton == updateButton:
                    UpdateUtils.updateFolder(folder)
                elif clickedButton == ignoreVersionButton:
                    UpdateUtils.ignoreFolderVersion(folder)
                
            else:
                cmds.warning("Tools needed update but was ignored by user: {}".format(folder))
