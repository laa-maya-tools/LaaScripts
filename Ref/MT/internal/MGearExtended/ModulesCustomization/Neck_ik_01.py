import maya.cmds                  as cmds
import MGearExtended.PostProUtils as PostP

# utils
def getAllControls(moduleName, side, checkSet=True):
    return getFkControls(moduleName, side, checkSet) + getIkControls(moduleName, side, checkSet)

def getFkControls(moduleName, side, checkSet=True):
    head = '{}_{}_head_ctl'.format(moduleName, side)
    result = [head]
    if checkSet and head not in cmds.sets('rig_controllers_grp', q=True):
        result = []
    for ctl in cmds.ls("{}_{}_fk*_ctl".format(moduleName, side)):
        result.append(ctl)
        if checkSet and ctl not in cmds.sets('rig_controllers_grp', q=True):
            result.remove(ctl)
    return result

def getIkControls(moduleName, side, checkSet=True):
    ctl = PostP.getControl(moduleName, side, 'ik', checkSet)
    if ctl:
        return [ctl]
    else:
        return None
#######

def doKeyingGroups(moduleName, side, blend=True, fk=True, ik=True, keyGroupParent=None):
    blendKG,fkKG,ikKG = [None]*3
    toeCtl, footRollCtlLs = PostP.KeyingGroupFootFinder(moduleName, side)
    if blend:
        controlInputLs = [PostP.getUIHostControl(moduleName, side) + ".FK_IK_Blend"]
        if toeCtl:
            controlInputLs.append( toeCtl )
        blendKG = PostP.KeyingGroupSetUp(moduleName, side, controlInputLs, keyGroupParent)
    if fk:
        fkKG = PostP.KeyingGroupSetUp(moduleName+'Fk', side, getFkControls(moduleName, side), blendKG if blendKG else keyGroupParent)
    if ik:
        controlInputLs = getIkControls(moduleName, side)
        if footRollCtlLs:
            controlInputLs.extend( footRollCtlLs )
        ikKG = PostP.KeyingGroupSetUp(moduleName+'Ik', side, controlInputLs, blendKG if blendKG else keyGroupParent)
    return blendKG,fkKG,ikKG