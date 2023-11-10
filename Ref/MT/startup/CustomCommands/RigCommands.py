import maya.cmds as cmds

from RigManager.Rig import Rig
from RigManager.RigChain import RigChain

def selectRigCogControl():
    rigs = Rig.getConnectedWrappers(cmds.ls(selection=True))
    controls = set()
    for rig in rigs:
        controls.add(rig.cogControl)
    if controls:
        cmds.select(controls)

def selectRigMainControl():
    rigs = Rig.getConnectedWrappers(cmds.ls(selection=True))
    controls = set()
    for rig in rigs:
        controls.add(rig.mainControl)
    if controls:
        cmds.select(controls)

def selectAllRigControls():
    rigs = Rig.getConnectedWrappers(cmds.ls(selection=True))
    controls = set()
    for rig in rigs:
        controls.update(rig.controls)
    if controls:
        cmds.select(controls)
        
def selectRigChainControls():
    rigChains = RigChain.getConnectedWrappers(cmds.ls(selection=True))
    controls = set()
    for rigChain in rigChains:
        controls.update(rigChain.getControls())
    if controls:
        cmds.select(controls)

def register():
    cmds.runTimeCommand("SelectRigCogControl", cat="MSE Commands.Rig", ann="Selects the COG Control of the selected rigs.", c="import CustomCommands.RigCommands as RigCommands; RigCommands.selectRigCogControl()", default=True)
    cmds.runTimeCommand("SelectRigMainControl", cat="MSE Commands.Rig", ann="Selects the Main Control of the selected rigs.", c="import CustomCommands.RigCommands as RigCommands; RigCommands.selectRigMainControl()", default=True)
    cmds.runTimeCommand("SelectAllRigControls", cat="MSE Commands.Rig", ann="Selects all the Controls of the selected rigs.", c="import CustomCommands.RigCommands as RigCommands; RigCommands.selectAllRigControls()", default=True)
    cmds.runTimeCommand("SelectRigChainControls", cat="MSE Commands.Rig", ann="Selects the Controls of the selected rig chains.", c="import CustomCommands.RigCommands as RigCommands; RigCommands.selectRigChainControls()", default=True)
