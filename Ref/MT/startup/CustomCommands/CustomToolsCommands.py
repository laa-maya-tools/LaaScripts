import maya.cmds as cmds

from AnimSystems.IKManipulator import IKManipulatorController, FKManipulatorController

MANIP_MOVE_CONTEXT_NAME = "moveSuperContext"
MANIP_ROTATE_CONTEXT_NAME = "RotateSuperContext"

def toggleMoveTool():
    currentContext = cmds.currentCtx()
    if currentContext == MANIP_MOVE_CONTEXT_NAME:
        cmds.setToolTo(IKManipulatorController.CONTEXT_NAME)
    else:
        cmds.setToolTo(MANIP_MOVE_CONTEXT_NAME)

def toggleRotateTool():
    currentContext = cmds.currentCtx()
    if currentContext == MANIP_ROTATE_CONTEXT_NAME:
        cmds.setToolTo(FKManipulatorController.CONTEXT_NAME)
    else:
        cmds.setToolTo(MANIP_ROTATE_CONTEXT_NAME)

def register():
    cmds.runTimeCommand("IKMoveManipulator", cat="MSE Commands.Cutom Tools", i="Manipulators/IKManipulator.png", ann="Tool that allows to manipulate FK chains like they were IK and viceversa. It also allows normal node move manipulation. It is recomended you replace your \"Move Tool\" shortcut with this one.", c="import AnimSystems.IKManipulator; cmds.setToolTo(AnimSystems.IKManipulator.IKManipulatorController.CONTEXT_NAME)", default=True)
    cmds.runTimeCommand("ToggleMoveManipulator", cat="MSE Commands.Cutom Tools", i="Manipulators/IKManipulator.png", ann="Toggles between Move Tools. The tools are: normal Move manipulation, IK Manipulator.", c="import CustomCommands.CustomToolsCommands; CustomCommands.CustomToolsCommands.toggleMoveTool()", default=True)
    
    cmds.runTimeCommand("FKRotateManipulator", cat="MSE Commands.Cutom Tools", i="Manipulators/FKManipulator.png", ann="Tool that allows to manipulate IK chains like they were FK and viceversa. It also allows normal node rotate manipulation. It is recomended you replace your \"Rotate Tool\" shortcut with this one.", c="import AnimSystems.IKManipulator; cmds.setToolTo(AnimSystems.IKManipulator.FKManipulatorController.CONTEXT_NAME)", default=True)
    cmds.runTimeCommand("ToggleRotateManipulator", cat="MSE Commands.Cutom Tools", i="Manipulators/FKManipulator.png", ann="Toggles between Rotate Tools. The tools are: normal Rotate manipulation, FK Manipulator.", c="import CustomCommands.CustomToolsCommands; CustomCommands.CustomToolsCommands.toggleRotateTool()", default=True)
