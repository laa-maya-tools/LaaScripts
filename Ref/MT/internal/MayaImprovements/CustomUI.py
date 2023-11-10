from MayaImprovements import MayaImprovement

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as OpenMayaUI

from PySide2 import QtWidgets

import CustomCommands.CommonCommands as CommonCommands

import ProjectPath

import os
import shiboken2

class HideUI():

    # Constants
    hideHomeButtonOptionVar = "hideHomeButtonEnabled"
    hideCycleWarningsOptionVar = "hideCycleWarningsEnabled"
    
    @classmethod
    def getHomeButtonWidget(cls):
        # Finding the button is not easy.
        # We look for the main window's menu bar, then for an item of type "QWidget" with 2 children, the second one being a button.
        # This is the layout that the home button follows and we trust it's the only one.
        mainWindow = shiboken2.wrapInstance(int(OpenMayaUI.MQtUtil.mainWindow()), QtWidgets.QWidget)
        menuBarChildren = mainWindow.children()[2].children() or []
        for child in menuBarChildren:
            if type(child) == QtWidgets.QWidget:
                widgetChildren = child.children() or []
                if len(widgetChildren) == 2 and type(widgetChildren[1] == QtWidgets.QPushButton):
                    return child
        return None
    
    @classmethod
    def isHideHomeButtonEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.hideHomeButtonOptionVar):
            default = False  # False by default
            cls.setHideHomeButtonEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.hideHomeButtonOptionVar)

    @classmethod
    def setHideHomeButtonEnabled(cls, enabled, updateOptionVar=True):
        homeButtonWidget = cls.getHomeButtonWidget()
        if homeButtonWidget:
            homeButtonWidget.setVisible(not enabled)    # What is "enabled" is the "hiding" of the button
        
        if updateOptionVar:
            cmds.optionVar(iv=(cls.hideHomeButtonOptionVar, enabled))

    @classmethod
    def isHideCycleWarningsEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.hideCycleWarningsOptionVar):
            default = True  # True by default
            cls.setHideCycleWarningsEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.hideCycleWarningsOptionVar)

    @classmethod
    def setHideCycleWarningsEnabled(cls, enabled, updateOptionVar=True):
        cmds.cycleCheck(evaluation=not enabled)    # What is "enabled" is the "hiding" the warnings
        
        if updateOptionVar:
            cmds.optionVar(iv=(cls.hideCycleWarningsOptionVar, enabled))

    @classmethod
    def initialize(cls):
        cls.setHideHomeButtonEnabled(cls.isHideHomeButtonEnabled(), updateOptionVar=False)
        cls.setHideCycleWarningsEnabled(cls.isHideCycleWarningsEnabled(), updateOptionVar=False)

    @classmethod
    def uninitialize(cls):
        cls.setHideHomeButtonEnabled(False, updateOptionVar=False)
        cls.setHideCycleWarningsEnabled(False, updateOptionVar=False)


class FrameOrKeyButtonManager():
    
    frameOrKeyToggleButton = None
    
    frameOrKeyToggledScriptJob = None

    # Constants
    showFrameOrKeyToggleButtonOptionVar = "showFrameOrKeyToggleButtonEnabled"
    
    frameRateLayout = "RangeSlider|MainPlaybackRangeLayout|formLayout9|formLayout14"
    frameRateGroupBox = frameRateLayout + "|optionMenuGrp1"
    playbackLoopButton = frameRateLayout + "|iconTextButton2"
    
    @classmethod
    def onFrameOrKeyButtonPressed(cls):
        CommonCommands.TimeChangeRepeat.onFrameOrKeyToggled()
        #cls.updateFrameOrKeyButtonState()  # No need to call the update function, the change to the option var will trigger the call
    
    @classmethod
    def updateFrameOrKeyButtonState(cls):
        cmds.iconTextButton(cls.frameOrKeyToggleButton, e=True, enableBackground=CommonCommands.TimeChangeRepeat.SWITCH_FRAME_OR_KEY_OPTIONVAR.value)
    
    @classmethod
    def isShowFrameOrKeyToggleButtonEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.showFrameOrKeyToggleButtonOptionVar):
            default = False  # False by default
            cls.setShowFrameOrKeyToggleButtonEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.showFrameOrKeyToggleButtonOptionVar)
    
    @classmethod
    def setShowFrameOrKeyToggleButtonEnabled(cls, enabled, updateOptionVar=True):
        cmds.iconTextButton(cls.frameOrKeyToggleButton, e=True, visible=enabled)
        
        if updateOptionVar:
            cmds.optionVar(iv=(cls.showFrameOrKeyToggleButtonOptionVar, enabled))
    
    @classmethod
    def initialize(cls):
        cls.frameOrKeyToggleButton = cmds.iconTextButton(image1="directKeySmall.png", annotation=cmds.runTimeCommand("FrameOrKeyToggle", q=True, ann=True), backgroundColor=(0.32, 0.52, 0.65), enableBackground=False, c=cls.onFrameOrKeyButtonPressed, parent=cls.frameRateLayout)
        cmds.formLayout(cls.frameRateLayout, edit=True,
                        attachControl=[
                            (cls.frameOrKeyToggleButton, "left", 0, cls.frameRateGroupBox),
                            (cls.frameOrKeyToggleButton, "right", 5, cls.playbackLoopButton)
                        ],
                        attachForm=(cls.frameRateGroupBox, "left", 0),
                        attachNone=(cls.frameRateGroupBox, "right")
                        )
        cls.updateFrameOrKeyButtonState()
        
        cls.frameOrKeyToggledScriptJob = cmds.scriptJob(optionVarChanged=(CommonCommands.TimeChangeRepeat.SWITCH_FRAME_OR_KEY_OPTIONVAR.optionVar, cls.updateFrameOrKeyButtonState))
    
        cls.setShowFrameOrKeyToggleButtonEnabled(cls.isShowFrameOrKeyToggleButtonEnabled(), updateOptionVar=False)
        
    @classmethod
    def uninitialize(cls):
        cls.setShowFrameOrKeyToggleButtonEnabled(False, updateOptionVar=False)
        
        cmds.deleteUI(cls.frameOrKeyToggleButton)
        cls.frameOrKeyToggleButton = None

        cmds.scriptJob(kill=cls.frameOrKeyToggledScriptJob)


class OpenRecentMenuOptionManager():
    
    openLastMenuOption = None
    
    # Constants
    moveMenuOptionUpOptionVar = "OpenRecentMenuOption_MoveMenuOptionUp"
    showOpenLastMenuOptionOptionVar = "OpenRecentMenuOption_ShowOpenLastMenuOption"
    
    fileMenuOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\FileMenu.mel")
    
    openRecentMenu = "FileMenuRecentFileItems"
    fileMenu = "mainFileMenu"
    openFileItem = "openFileOptions"
    
    @classmethod
    def openLastFile(cls, *args):
        recentFiles = cmds.optionVar(q="RecentFilesList")
        if recentFiles:
            lastFile = recentFiles[-1]
            fileType = None
            if cmds.file(lastFile, q=True, ex=True):
                t = cmds.file(lastFile, q=True, type=True)
                if t:
                    fileType = t[0]
            mel.eval("openRecentFile \"{}\" \"{}\"".format(lastFile, fileType)) # We use this mel procedure since it will check if the file exists and remove it from the list if it doesn't. But it needs the file type for some reason...
        else:
            print("No recent files to open.")

    @classmethod
    def isMoveMenuOptionUpEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.moveMenuOptionUpOptionVar):
            default = False  # False by default
            cls.setMoveMenuOptionUpEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.moveMenuOptionUpOptionVar)
    
    @classmethod
    def setMoveMenuOptionUpEnabled(cls, enabled, updateOptionVar=True):
        if cls.openRecentMenu and cmds.menuItem(cls.openRecentMenu, q=True, ex=True):
            if enabled:
                beforeAction = cls.openFileItem
            else:
                actions = cmds.menu(cls.fileMenu, q=True, itemArray=True)
                beforeAction = actions[actions.index("setProjectFileItem") + 1]
            
            label = cmds.menuItem(cls.openRecentMenu, q=True, l=True)
            cmds.deleteUI(cls.openRecentMenu)
            cmds.menuItem(cls.openRecentMenu, subMenu=True, l=label, postMenuCommand="import maya.mel; maya.mel.eval(\"buildRecentFileMenu FileMenuRecentFileItems\")", parent=cls.fileMenu, insertAfter=beforeAction)
        
        else:
            print("Warning: Unable to find Open Recent Menu Option!")
            
        if updateOptionVar:
            cmds.optionVar(iv=(cls.moveMenuOptionUpOptionVar, enabled))

    @classmethod
    def isShowOpenLastMenuOptionEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.showOpenLastMenuOptionOptionVar):
            default = False  # False by default
            cls.setShowOpenLastMenuOptionEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.showOpenLastMenuOptionOptionVar)
    
    @classmethod
    def setShowOpenLastMenuOptionEnabled(cls, enabled, updateOptionVar=True):
        if cls.openLastMenuOption and cmds.menuItem(cls.openLastMenuOption, q=True, ex=True):
            cmds.menuItem(cls.openLastMenuOption, e=True, visible=enabled)
            
        else:
            print("Warning: Unable to find Open Last Menu Option!")
    
        if updateOptionVar:
            cmds.optionVar(iv=(cls.showOpenLastMenuOptionOptionVar, enabled))
      
    @classmethod
    def fixOverrideOpenRecent(cls):
        overridePath = "\"" + cls.fileMenuOverrideScript + "\";"
        overridePath = overridePath.replace("\\", "/")
        mel.eval("source " + overridePath)
       
    @classmethod
    def initializeLate(cls):
        if cls.openLastMenuOption == None:
            if cls.openFileItem and cmds.menuItem(cls.openFileItem, q=True, ex=True):
                cls.openLastMenuOption = cmds.menuItem(label="Open Last File", command=cls.openLastFile, parent=cls.fileMenu, insertAfter=cls.openFileItem)
            else:
                print("ERROR: Unable to find Open File Menu Option! Menu reconfiguration aborted.")
        
        cls.setMoveMenuOptionUpEnabled(cls.isMoveMenuOptionUpEnabled(), updateOptionVar=False)
        cls.setShowOpenLastMenuOptionEnabled(cls.isShowOpenLastMenuOptionEnabled(), updateOptionVar=False)
        
        cmds.evalDeferred(cls.removeCallback)
    
    @classmethod
    def removeCallback(cls):
        cmds.callbacks(clearCallbacks=True, hook="addItemToFileMenu", owner="CustomUI")
    
    @classmethod
    def initialize(cls):
        # The menu might not be created yet, we need to delay the execution
        cmds.callbacks(addCallback=cls.initializeLate, hook="addItemToFileMenu", owner="CustomUI")

        cls.fixOverrideOpenRecent()
        
    @classmethod
    def uninitialize(cls):
        cls.setMoveMenuOptionUpEnabled(False, updateOptionVar=False)
        cls.setShowOpenLastMenuOptionEnabled(False, updateOptionVar=False)
        
        if cls.openLastMenuOption and cmds.menuItem(cls.openLastMenuOption, q=True, ex=True):
            cmds.deleteUI(cls.openLastMenuOption)
            cls.openLastMenuOption = None
        
        cls.removeCallback()
        

class CustomFixes():
    
    restoreMenuSetOptionVar = "CustomFixes_RestoreMenuSet"
    
    savedMenuSetOptionVar = "CustomFixes_RestoreMenuSet_SavedMenuSet"
    
    quitApplicationScriptJob = None
    
    @classmethod
    def isRestoreMenuSetOptionEnabled(cls):
        if not CustomUIManager.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.restoreMenuSetOptionVar):
            default = True  # True by default
            cls.setRestoreMenuSetOptionEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.restoreMenuSetOptionVar)
    
    @classmethod
    def setRestoreMenuSetOptionEnabled(cls, enabled):
        cmds.optionVar(iv=(cls.restoreMenuSetOptionVar, enabled))
        
    @classmethod
    def restoreSavedMenuMode(cls):
        if cls.isRestoreMenuSetOptionEnabled():
            if cmds.optionVar(ex=cls.savedMenuSetOptionVar):
                cmds.setMenuMode(cmds.optionVar(q=cls.savedMenuSetOptionVar))
        
    @classmethod
    def saveCurrentMenuMode(cls):
        currentMenuSet = cmds.menuSet(q=True, cms=True)
        cmds.optionVar(sv=(cls.savedMenuSetOptionVar, currentMenuSet))
      
    @classmethod
    def initialize(cls):
        cls.quitApplicationScriptJob = cmds.scriptJob(e=("quitApplication", cls.saveCurrentMenuMode))
        
        cls.restoreSavedMenuMode()
        
    @classmethod
    def uninitialize(cls):
        cmds.scriptJob(k=cls.quitApplicationScriptJob)


class CustomUIManager(MayaImprovement):

    initialized = False

    @classmethod
    def initialize(cls):
        cls.initialized = True
        
        HideUI.initialize()
        CustomFixes.initialize()
        FrameOrKeyButtonManager.initialize()
        OpenRecentMenuOptionManager.initialize()
        
    @classmethod
    def uninitialize(cls):
        cls.initialized = False
        
        HideUI.uninitialize()
        CustomFixes.uninitialize()
        FrameOrKeyButtonManager.uninitialize()
        OpenRecentMenuOptionManager.uninitialize()
