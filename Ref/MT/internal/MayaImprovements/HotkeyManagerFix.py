import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as OpenMayaUI

from PySide2 import QtWidgets, QtCore, QtGui

from MayaImprovements import MayaImprovement
import ProjectPath

from Utils.Python.Versions import long

import os, shiboken2

class HotkeyManagerFix(MayaImprovement):

    initialized = False

    # Constants
    melOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements", "MelOverride", "hotkeyEditorWindow.mel")
    hotkeyManagerFixOptionVar = "hotkeyManagerFixEnabled"

    @classmethod
    def isHotkeyManagerFixEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.hotkeyManagerFixOptionVar):
            default = True  # True by default
            cls.setHotkeyManagerFixEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.hotkeyManagerFixOptionVar)

    @classmethod
    def setHotkeyManagerFixEnabled(cls, enabled):
        cmds.optionVar(iv=(cls.hotkeyManagerFixOptionVar, enabled))

    @classmethod
    def overrideMelProcedure(cls):
        melScriptPath = "\"" + cls.melOverrideScript + "\";"
        melScriptPath = melScriptPath.replace("\\", "/")
        mel.eval("source " + melScriptPath)
    
    @classmethod
    def fillItemData(cls, parent=None):        
        if parent == None:
            parent = QtCore.QModelIndex()
            
        hotkeyEditor = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl("HotkeyEditor")), QtWidgets.QWidget)
        leftPanel = hotkeyEditor.layout().itemAt(0).widget().layout().itemAt(1).widget()
        commandListPanel = leftPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()
        commandList = commandListPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()
        
        model = commandList.model()
        if not model.hasChildren(parent):
            commandColumn = model.sibling(parent.row(), 1, parent)
            command = model.data(commandColumn)
            toolTip = cmds.runTimeCommand(command, q=True, ann=True)
            image = cmds.runTimeCommand(command, q=True, image=True)
            
            if image:
                if cmds.resourceManager(nameFilter=image):
                    image = ":" + image
                elif not os.path.exists(image):
                    iconFolders = os.environ["XBMLANGPATH"].split(";")
                    for iconFolder in iconFolders:
                        path = os.path.join(iconFolder, image)
                        if os.path.exists(path):
                            image = path
                            break
            
            model.setData(parent, toolTip, QtCore.Qt.ToolTipRole)
            model.setData(parent, QtGui.QIcon(image), QtCore.Qt.DecorationRole)
            model.setData(commandColumn, toolTip, QtCore.Qt.ToolTipRole)
            
        else:
            for i in range(model.rowCount(parent)):
                cls.fillItemData(model.index(i, 0, parent))

    @classmethod
    def updateToolTips(cls, *args):
        cmds.evalDeferred(cls.fillItemData)
        
    @classmethod
    def onCommandClicked(cls, index):
        modifiers = QtGui.QGuiApplication.keyboardModifiers()
        if modifiers != QtCore.Qt.ShiftModifier | QtCore.Qt.ControlModifier:
            return
        
        hotkeyEditor = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl("HotkeyEditor")), QtWidgets.QWidget)
        leftPanel = hotkeyEditor.layout().itemAt(0).widget().layout().itemAt(1).widget()
        commandListPanel = leftPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()
        commandList = commandListPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()
        
        model = commandList.model()
        if model.hasChildren(index):
            return
        
        gShelfTopLevel = mel.eval("$temp = $gShelfTopLevel")
        if not cmds.tabLayout(gShelfTopLevel, q=True, ex=True):
            return
            
        currentShelf = cmds.tabLayout(gShelfTopLevel, q=True, st=True)
        if index.column() != 1:
            index = model.sibling(index.row(), 1, index)
        command = model.data(index)
        toolTip = cmds.runTimeCommand(command, q=True, ann=True) or ""
        image = cmds.runTimeCommand(command, q=True, image=True) or ""
        if image:
            if image.startswith(":"):
                image = image[1:]
            cmds.shelfButton(rpt=True, i=image, l=command, c=command, stp="mel", ann=toolTip, p=currentShelf)
        else:
            cmds.shelfButton(rpt=True, i="commandButton.png", l=command, c=command, stp="mel", ann=toolTip, p=currentShelf)

    @classmethod
    def onHotkeyManagerShown(cls):
        if not cls.isHotkeyManagerFixEnabled():
            return
        
        hotkeyEditor = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl("HotkeyEditor")), QtWidgets.QWidget)
        leftPanel = hotkeyEditor.layout().itemAt(0).widget().layout().itemAt(1).widget()
        commandListPanel = leftPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()
        commandList = commandListPanel.layout().itemAt(4).widget().layout().itemAt(0).widget()

        commandList.model().rowsInserted.connect(cls.updateToolTips)
        commandList.clicked.connect(cls.onCommandClicked)

    @classmethod
    def initialize(cls):
        cls.initialized = True

        cls.overrideMelProcedure()

    @classmethod
    def uninitialize(cls):
        cls.initialized = False

