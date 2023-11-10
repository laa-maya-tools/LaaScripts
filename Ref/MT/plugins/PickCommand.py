import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

import maya.cmds as cmds
import maya.mel as mel

class PickContextCommand(OpenMayaMPx.MPxContextCommand):
    
    commandName = "pickContext"

    # Flags
    storedSelectionFlag = "-sl"
    storedSelectionFlagLong = "-selection"
    pickCallbackFlag = "-pc"
    pickCallbackFlagLong = "-pickCallback"
    abortCallbackFlag = "-ac"
    abortCallbackFlagLong = "-abortCallback"

    def __init__(self):
        OpenMayaMPx.MPxContextCommand.__init__(self)

        self.context = None

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(PickContextCommand())

    def makeObj(self):
        self.context = PickContext()
        return OpenMayaMPx.asMPxPtr(self.context)

    def doEditFlags(self):
        argData = self._parser()

        if argData.isFlagSet(PickContextCommand.pickCallbackFlag):
            self.context.pickCallback = argData.flagArgumentString(PickContextCommand.pickCallbackFlag, 0)

        if argData.isFlagSet(PickContextCommand.abortCallbackFlag):
            self.context.abortCallback = argData.flagArgumentString(PickContextCommand.abortCallbackFlag, 0)

    def doQueryFlags(self):
        argData = self._parser()

        if argData.isFlagSet(PickContextCommand.storedSelectionFlag):
            if self.context.storedSelection != None:
                self.setResult(self.context.storedSelection[0])

    def appendSyntax(self):
        syntax = self._syntax()

        syntax.addFlag(PickContextCommand.storedSelectionFlag, PickContextCommand.storedSelectionFlagLong, OpenMaya.MSyntax.kString)
        syntax.addFlag(PickContextCommand.pickCallbackFlag, PickContextCommand.pickCallbackFlagLong, OpenMaya.MSyntax.kString)
        syntax.addFlag(PickContextCommand.abortCallbackFlag, PickContextCommand.abortCallbackFlagLong, OpenMaya.MSyntax.kString)

class PickContext(OpenMayaMPx.MPxSelectionContext):

    def __init__(self):
        OpenMayaMPx.MPxSelectionContext.__init__(self)

        self.selectionChangeScriptJob = None
        self.storedSelection = None
        self.pickCallback = None
        self.abortCallback = None

        self.valid = True

    def toolOnSetup(self, event):
        if not self.valid:
            raise AssertionError("The context has already been used and cannot be used again")

        cmds.select(clear=True)
        self.selectionChangeScriptJob = cmds.scriptJob(event=["SelectionChanged", self.onSelectionChanged])

        self._setTitleString("Pick Object")
        self._setHelpString("select an object on the viewport to pick it")
        self._setCursor(OpenMayaUI.MCursor.doubleCrossHairCursor)

        self.setImage("defaultDoubleCrossHair.png", self.kImage1)

    def toolOffCleanup(self):
        cmds.evalDeferred("cmds.scriptJob(kill=" + str(self.selectionChangeScriptJob) + ")")

        if self.abortCallback != None:
            cmds.evalDeferred(self.abortCallback)
        
        self.valid = False

    def abortAction(self):
        cmds.setToolTo("selectSuperContext")

    def onSelectionChanged(self):
        selection = cmds.ls(sl=True)
        if len(selection) > 0:
            self.storedSelection = selection
            self.abortCallback = None   # Para que no se llame al callback de abortar cuando se salga de la herramienta
            cmds.setToolTo("selectSuperContext")
            if self.pickCallback != None:
                cmds.evalDeferred(self.pickCallback)

        
def initializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)
    
    plugin.registerContextCommand(PickContextCommand.commandName, PickContextCommand.creator)
        
def uninitializePlugin(obj):
    plugin = OpenMayaMPx.MFnPlugin(obj)

    plugin.deregisterContextCommand(PickContextCommand.commandName)