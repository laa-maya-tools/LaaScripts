import maya.cmds as cmds
import ModellingUtils.Core as ModCore

def ResetShapesForm():
    sel = cmds.ls(sl=True, type="transform")
    selWithShapes =  [x for x in sel if (cmds.listRelatives(x, shapes=True) != None)]
    
    for node in selWithShapes:
        ModCore.SetPivotToWorld(node)
        ModCore.CleanShape(node)