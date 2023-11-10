import maya.cmds                  as cmds
import MGearExtended.PostProUtils as PostP

# utils
def getAllControls(moduleName, side, checkSet=True):
    return getFkControls(moduleName, side, checkSet) + getIkControls(moduleName, side, checkSet)

def getFkControls(moduleName, side, checkSet=True):
    result = []
    for ctl in cmds.ls("{}_{}_fk*_ctl".format(moduleName, side)):
        result.append(ctl)
        if checkSet and ctl not in cmds.sets('rig_controllers_grp', q=True):
            result.remove(ctl)
    return result

def getUpVectorControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'upv', checkSet)

def getIkControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ik', checkSet)

def getIkCnsControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ikcns', checkSet)

def getIkControls(moduleName, side, checkSet=True):
    result = [getUpVectorControl(moduleName, side, checkSet),
              getIkControl(moduleName, side, checkSet),
              getIkCnsControl(moduleName, side, checkSet)]
    return [member for member in result if member]
#######

def doKeyingGroups(moduleName, side, blend=True, fk=True, ik=True, keyGroupParent=None):
    blendKG,fkKG,ikKG = [None]*3
    toeCtl, footRollCtlLs = PostP.KeyingGroupFootFinder(moduleName, side)
    if blend:
        controlInputLs = [PostP.getUIHostControl(moduleName, side) + ".chain_blend"]
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