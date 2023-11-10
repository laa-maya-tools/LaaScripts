import Utils.Maya.ToolContext as ToolContextUtils
from Utils.Maya.OptionVar import OptionVarConfiguration

import AnimSystems.IKManipulator as IKManipulator

from QtCustomWidgets.QtUtils import EditItemsDialog

import maya.cmds as cmds

#---------------------------------
#|      Tool Space Commands      |
#---------------------------------

class ManipulatorModeCommands():
    
    @staticmethod
    def toggleWorldLocalSpace():
        currentManipulatorMode = ToolContextUtils.ManipulatorModes.currentContextManipulatorMode()
        if currentManipulatorMode == "World":
            ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode("Object", showPrompt=True)
        else:
            ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode("World", showPrompt=True)

    @staticmethod
    def toggleWorldLocalGimbalSpace():
        currentManipulator = ToolContextUtils.currentContextManipulator()
        currentManipulatorMode = ToolContextUtils.ManipulatorModes.currentContextManipulatorMode()
        if currentManipulatorMode == "World":
            ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode("Object", showPrompt=True)
        elif currentManipulatorMode == "Object" and (currentManipulator == "manipRotate" or currentManipulator == IKManipulator.FKManipulatorController.CONTEXT_CLASS):
            ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode("Gimbal", showPrompt=True)
        else:
            ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode("World", showPrompt=True)

    @staticmethod
    def registerCommands():
        cmds.runTimeCommand("ToggleWorldLocalSpace", cat="MSE Commands.Tool Context.Space", i="Manipulators/ToggleSpaces.png", ann="Toggle Between World and Local Space", c="import CustomCommands.ToolContextCommands as ToolContextCommands; ToolContextCommands.ManipulatorModeCommands.toggleWorldLocalSpace()", default=True)
        cmds.runTimeCommand("ToggleWorldLocalGimbalSpace", cat="MSE Commands.Tool Context.Space", i="Manipulators/ToggleSpaces.png", ann="Toggle Between World, Local and Gimbal Space", c="import CustomCommands.ToolContextCommands as ToolContextCommands; ToolContextCommands.ManipulatorModeCommands.toggleWorldLocalGimbalSpace()", default=True)

        cmds.runTimeCommand("SetWorldSpace", cat="MSE Commands.Tool Context.Space", ann="Set World Space", c="import Utils.Maya.ToolContext as ToolContextUtils; ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode('World', showPrompt=True)", default=True)
        cmds.runTimeCommand("SetLocalSpace", cat="MSE Commands.Tool Context.Space", ann="Set Local Space", c="import Utils.Maya.ToolContext as ToolContextUtils; ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode('Object', showPrompt=True)", default=True)
        cmds.runTimeCommand("SetGimbalSpace", cat="MSE Commands.Tool Context.Space", ann="Set Gimbal Space", c="import Utils.Maya.ToolContext as ToolContextUtils; ToolContextUtils.ManipulatorModes.setCurrentContextManipulatorMode('Gimbal', showPrompt=True)", default=True)

        cmds.runTimeCommand("MoveToolWorld", cat="MSE Commands.Tool Context.Space", ann="Move Tool (World)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Move'); ToolContextUtils.ManipulatorModes.setMoveContextManipulatorMode('World', showPrompt=True)", default=True)
        cmds.runTimeCommand("MoveToolLocal", cat="MSE Commands.Tool Context.Space", ann="Move Tool (Local)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Move'); ToolContextUtils.ManipulatorModes.setMoveContextManipulatorMode('Object', showPrompt=True)", default=True)
        cmds.runTimeCommand("RotateToolWorld", cat="MSE Commands.Tool Context.Space", ann="Rotate Tool (World)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Rotate'); ToolContextUtils.ManipulatorModes.setRotateContextManipulatorMode('World', showPrompt=True)", default=True)
        cmds.runTimeCommand("RotateToolLocal", cat="MSE Commands.Tool Context.Space", ann="Rotate Tool (Local)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Rotate'); ToolContextUtils.ManipulatorModes.setRotateContextManipulatorMode('Object', showPrompt=True)", default=True)
        cmds.runTimeCommand("RotateToolGimbal", cat="MSE Commands.Tool Context.Space", ann="Rotate Tool (Gimbal)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Rotate'); ToolContextUtils.ManipulatorModes.setRotateContextManipulatorMode('Gimbal', showPrompt=True)", default=True)
        cmds.runTimeCommand("ScaleToolWorld", cat="MSE Commands.Tool Context.Space", ann="Scale Tool (World)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Scale'); ToolContextUtils.ManipulatorModes.setScaleContextManipulatorMode('World', showPrompt=True)", default=True)
        cmds.runTimeCommand("ScaleToolLocal", cat="MSE Commands.Tool Context.Space", ann="Scale Tool (Local)", c="import Utils.Maya.ToolContext as ToolContextUtils; maya.cmds.setToolTo('Scale'); ToolContextUtils.ManipulatorModes.setScaleContextManipulatorMode('Object', showPrompt=True)", default=True)


#---------------------------------
#|        Snap Commands          |
#---------------------------------

class SnapCommands():
    
    MOVE_SNAP_VALUES_OPTIONVAR = OptionVarConfiguration("MoveSnapValues", "SnapCommands_MoveSnapValues", OptionVarConfiguration.TYPE_FLOAT, [0, 0.1, 1, 5, 10, 50, 100])
    ROTATE_SNAP_VALUES_OPTIONVAR = OptionVarConfiguration("RotateSnapValues", "SnapCommands_RotateSnapValues", OptionVarConfiguration.TYPE_FLOAT, [0, 0.1, 1, 3, 5, 15, 30, 45, 90])
    SCALE_SNAP_VALUES_OPTIONVAR = OptionVarConfiguration("ScaleSnapValues", "SnapCommands_ScaleSnapValues", OptionVarConfiguration.TYPE_FLOAT, [0, 0.1, 0.2, 0.5, 1, 2, 5, 10])
    
    @classmethod
    def getCurrentToolSnapValues(cls):
        contextClass = ToolContextUtils.currentContextManipulator()
        
        if contextClass == "manipMove":
            return cls.MOVE_SNAP_VALUES_OPTIONVAR.value
        elif contextClass == "manipRotate":
            return cls.ROTATE_SNAP_VALUES_OPTIONVAR.value
        elif contextClass == "manipScale":
            return cls.SCALE_SNAP_VALUES_OPTIONVAR.value
        else:
            return None
    
    @classmethod
    def setCurrentToolSnapValues(cls, snapValues):
        contextClass = ToolContextUtils.currentContextManipulator()
        
        if contextClass == "manipMove":
            cls.MOVE_SNAP_VALUES_OPTIONVAR.value = snapValues
        elif contextClass == "manipRotate":
            cls.ROTATE_SNAP_VALUES_OPTIONVAR.value = snapValues
        elif contextClass == "manipScale":
            cls.SCALE_SNAP_VALUES_OPTIONVAR.value = snapValues
    
    @classmethod
    def editCurrentToolSnapValues(cls):
        snapValues = cls.getCurrentToolSnapValues()
        
        if snapValues:
            contextName = cmds.superCtx(cmds.currentCtx(), q=True)
            newSnapValues = EditItemsDialog(None, "Edit {} Snap Values".format(contextName), snapValues, EditItemsDialog.TYPE_FLOAT).run()
            if newSnapValues != None:
                cls.setCurrentToolSnapValues(newSnapValues)
    
    @classmethod
    def toggleSnap(cls, showMessage=True):
        ToolContextUtils.Snap.setCurrentSnapState(not ToolContextUtils.Snap.getCurrentSnapState(), showMessage=showMessage)
        
    @classmethod
    def toggleSnapValue(cls, toggleSnap=True, showMessage=True):
        snapValues = cls.getCurrentToolSnapValues()
        if snapValues:
            currentSnapValue = ToolContextUtils.Snap.getCurrentSnapValue()
            if currentSnapValue in snapValues:
                value = snapValues[(snapValues.index(currentSnapValue) + 1) % len(snapValues)]
            else:
                value = snapValues[0]
            
            showValueChangeMessage = showMessage
            
            if toggleSnap:
                currentSnapState = ToolContextUtils.Snap.getCurrentSnapState()
                if value == 0 and currentSnapState:
                    ToolContextUtils.Snap.setCurrentSnapState(False, showMessage=showMessage)
                    showValueChangeMessage = False
                elif value > 0 and not currentSnapState:
                    ToolContextUtils.Snap.setCurrentSnapState(True, showMessage=False)
            
            ToolContextUtils.Snap.setCurrentSnapValue(value, showMessage=showValueChangeMessage)
    
    @staticmethod
    def registerCommands():
        cmds.runTimeCommand("ToggleCurrentToolSnap", cat="MSE Commands.Tool Context.Snap", i="teToggleSnapping.png", ann="Toggles Grid Snapping for the current tool.", c="import CustomCommands.ToolContextCommands as ToolContextCommands; ToolContextCommands.SnapCommands.toggleSnap()", default=True)
        cmds.runTimeCommand("ToggleCurrentToolSnapValue", cat="MSE Commands.Tool Context.Snap", i="snapValue.png", ann="Cycles through the predefined Snap values for the current tool.", c="import CustomCommands.ToolContextCommands as ToolContextCommands; ToolContextCommands.SnapCommands.toggleSnapValue()", default=True)
        cmds.runTimeCommand("EditCurrentToolSnapValues", cat="MSE Commands.Tool Context.Snap", i="snapPoint.png", ann="Edits the predefined Snap values for the current tool.", c="import CustomCommands.ToolContextCommands as ToolContextCommands; ToolContextCommands.SnapCommands.editCurrentToolSnapValues()", default=True)
        

#---------------------------------
#|           Commands            |
#---------------------------------

def register():
    ManipulatorModeCommands.registerCommands()
    SnapCommands.registerCommands()