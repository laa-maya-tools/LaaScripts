import Batcher

from PySide2 import QtCore, QtWidgets, QtGui

import ProjectPath

import maya.cmds as cmds

import os
import collections

import logging
logger = logging.getLogger(__name__)

class ScriptBatcher(Batcher.BatcherUI):
    
    def onGetWindowTitle(self):
        return "Script Batcher"

    def onGetInputUIFilePath(self):
        return ProjectPath.getToolsFolder() + "\\Batcher\\ScriptBatcher.ui"

    def onInitializeUI(self, inputUI):
        self.inputUI.scriptsList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.inputUI.scriptsList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.scriptsListContextMenu = QtWidgets.QMenu(self.inputUI.scriptsList)
        self.scriptsListContextMenu.addAction("Remove", self.removeSelectedScripts)

        self.inputUI.scriptsList.customContextMenuRequested.connect(self.showScriptsListContextMenu)

        self.inputUI.scriptsAddButton.clicked.connect(self.browseAndAddScripts)
        self.inputUI.scriptsRemoveButton.clicked.connect(self.removeSelectedScripts)

    def onBeforeProcess(self):
        # Checks if all the scripts exist.
        scripts = self.getScripts()
        for script in scripts:
            if not os.path.isfile(script):
                raise FileNotFoundError("Couldn't find the specified script! {}".format(script))
            
        self.scriptData = collections.OrderedDict()
        for script in scripts:
            with open(script, "r") as file:
                compiled = compile(file.read(), script, "exec")
                self.scriptData[script] = compiled

        return True

    def onPerformBatchProcess(self, filePath):
        # Checks if the animation file exists.
        if not os.path.isfile(filePath):
            raise FileNotFoundError("Couldn't find the specified Maya File! {}".format(filePath))

        # Opens the animation file.
        logger.info("Opening Maya File...")
        cmds.file(filePath, o=True, force=True)

        # Runs each script on the file
        for i, script in enumerate(self.scriptData):
            logger.info("[{}/{}] Executing script: {}".format(i+1, len(self.scriptData), os.path.basename(script)))
            exec(self.scriptData[script], {})

        # Saves the file
        logger.info("Saving File...")
        cmds.file(save=True)
    
    def getScripts(self):
        scripts = []
        for i in range(self.inputUI.scriptsList.count()):
            item = self.inputUI.scriptsList.item(i)
            scripts.append(item.data(QtCore.Qt.UserRole))
        return scripts
    
    def browseAndAddScripts(self):
        scripts, selectedFilter = QtWidgets.QFileDialog.getOpenFileNames(self, caption="Select Scripts to process", filter="Python Scripts (*.py)", dir=os.path.dirname(__file__))
        if len(scripts) > 0:
            self.addScripts(scripts)
    
    def addScripts(self, scripts):
        for path in scripts:
            name = os.path.basename(path)
            if not self.inputUI.scriptsList.findItems(name, QtCore.Qt.MatchExactly):
                item = QtWidgets.QListWidgetItem(name)
                item.setData(QtCore.Qt.UserRole, path)
                item.setToolTip(path)
                self.inputUI.scriptsList.addItem(item)
    
    def removeSelectedScripts(self):
        selectedItems = self.inputUI.scriptsList.selectedItems()
        rows = [self.inputUI.scriptsList.row(item) for item in selectedItems]
        rows.sort(reverse=True)
        for row in rows:
            self.inputUI.scriptsList.takeItem(row)
            
    def showScriptsListContextMenu(self, pos):
        selectedItem = self.inputUI.scriptsList.itemAt(pos)
        if selectedItem is not None:
            self.scriptsListContextMenu.exec_(QtGui.QCursor.pos())


def showBatchWindow():
    global scriptBatcherWindow
    try:
        if scriptBatcherWindow.isVisible():
            scriptBatcherWindow.close()
    except NameError:
        pass
    scriptBatcherWindow = ScriptBatcher()
    scriptBatcherWindow.show()

if __name__ == "__main__":
    showBatchWindow()
