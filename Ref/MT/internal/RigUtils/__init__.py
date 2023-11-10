import maya.cmds    as cmds
import maya.mel     as mel
import pymel.core   as pm
import RigUtils.Skinning as skn
import RigUtils.Shapes   as RigShapes

def ResetBindTMs():
    selection = cmds.ls(sl=True, type="transform")
    if (selection):
        skn.ResetMeshBindTMs(selection)
    else:
        cmds.warning("Select any Mesh/es first")

def RebuildUniqueDagPose():
    selection = cmds.ls(sl=True, type=["transform", "joint"])
    if (len(selection) == 1):
        skn.RebuildHierarchyDagPose(selection[0])
        #cmds.select(selection)
    else:
        cmds.warning("Select one and only one root node for the skeleton")

def RemoveUnusedNodes():
    totalRemoved = mel.eval("MLdeleteUnused()")
    print("\tRemoved {} unused rendering nodes".format(totalRemoved))

def ConvertSelectionToPointLocator():
    selection = pm.selected()
    RigShapes.ChangeShapeToPointLocator(selection)
    pm.select(selection)