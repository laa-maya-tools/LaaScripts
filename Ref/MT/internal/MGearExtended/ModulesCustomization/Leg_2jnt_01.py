import json
import maya.cmds                                     as cmds
import MGearExtended.PostProUtils                    as PostP
import MGearExtended.ModulesCustomization.Foot_bk_01 as Foot

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

def getRollControl(moduleName, side, checkSet=True):
    # base module does not creates this control
    # available when "addPoleVectorRoll" is called
    return PostP.getControl(moduleName, side, 'roll', checkSet)

def getIkControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ik', checkSet)

def getIkCnsControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ikcns', checkSet)

def getIkControls(moduleName, side, checkSet=True):
    result = [getUpVectorControl(moduleName, side, checkSet),
              getIkControl(moduleName, side, checkSet),
              getIkCnsControl(moduleName, side, checkSet)]
    rollCtl = getRollControl(moduleName, side, checkSet)
    if rollCtl:
        result.append( rollCtl )
    return [member for member in result if member]
#######

def doKeyingGroups(moduleName, side, blend=True, fk=True, ik=True, keyGroupParent=None):
    blendKG,fkKG,ikKG = [None]*3
    toeCtl, footRollCtlLs = PostP.KeyingGroupFootFinder(moduleName, side)
    if blend:
        controlInputLs = [PostP.getUIHostControl(moduleName, side) + ".leg_blend"]
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

def addPoleVectorRoll(moduleName, side):
    '''Creates a control to master the roll behaviour integrated in mGear not quadruped module
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply

    Returns:
        Set(Control's Root, Control itself)'''
    # init
    uiHost = PostP.getUIHostControl(moduleName, side)
    ctlParent = None
    if cmds.objExists('{}_{}_mid_ctl'.format(moduleName, side)):
        ctlParent = '{}_{}_mid_ctl'.format(moduleName, side)
    # ctl
    root = cmds.createNode('transform', n='{}_{}_roll_ctl_npo'.format(moduleName, side), p=ctlParent)
    ctl = cmds.createNode('transform', n='{}_{}_roll_ctl'.format(moduleName, side), p=root)
    cmds.sets(ctl, e=True, forceElement="rig_controllers_grp")
    PostP.ControlBuffer(ctl, 'direction')
    PostP.AttributeLockAndHide(ctl, [at + ax for ax in "xyz" for at in "trs"])
    cmds.setAttr("{}.v".format(ctl), k=False)
    cmds.setAttr("{}.rx".format(ctl), l=False, k=True)
    # operation
    sum = cmds.createNode('addDoubleLinear')
    mult = cmds.createNode('multDoubleLinear')
    cmds.setAttr(mult + ".i2", -1)
    cmds.connectAttr('{}.leg_blend'.format(uiHost), root + ".v")
    cmds.connectAttr("{}.rx".format(ctl), mult + ".i1")
    cmds.connectAttr("{}.o".format(mult), sum + ".input1")
    for cnn in cmds.listConnections("{}.leg_roll".format(uiHost), p=True):
        node,dot,at = cnn.partition(".")
        if at not in cmds.listAttr(uiHost, s=True):
            cmds.connectAttr(sum + ".output", cnn, force=True)
    cmds.connectAttr("{}.leg_roll".format(uiHost), sum + ".input2")
    return root, ctl

def doIKFKChain(moduleName, side):
    # ik limb controls
    npoParent = cmds.listConnections(getIkControl(moduleName, side) + ".compRoot")[0]
    npo = cmds.createNode('transform', n='{}_{}_limbs_npo'.format(moduleName, side), p=npoParent)
    ctlA = cmds.createNode('transform', n='{}_{}_limbA_ctl'.format(moduleName, side), p=npo)
    ctlB = cmds.createNode('transform', n='{}_{}_limbB_ctl'.format(moduleName, side), p=ctlA)
    PostP.ControlBuffer(ctlA)
    PostP.ControlBuffer(ctlB)
    cmds.sets([ctlA, ctlB], forceElement='rig_controllers_grp', e=True)
    # controls connections
    decMtx = cmds.listConnections('{}_{}_div0_loc.t'.format(moduleName, side), p=True)[0]
    ctlRoll = getRollControl(moduleName, side)
    ctlIk = getIkControl(moduleName, side)
    cmds.connectAttr(decMtx, npo + ".t")
    cmds.connectAttr(PostP.getUIHostControl(moduleName, side) + ".leg_blend", npo + ".v")
    if ctlRoll:
        cUpV = ctlRoll
    else:
        cUpV = '{}_{}_div5_loc'.format(moduleName, side)
    cmds.aimConstraint(cUpV, npo, aim=[1,0,0], u=[0,0,1], wut='objectrotation', wuo=cUpV, wu=[0,0,1])
    cmds.aimConstraint(ctlIk, ctlB, aim=[1,0,0], u=[0,0,1], wut='objectrotation', wuo=cUpV, wu=[0,0,1])
    cmds.delete(cmds.pointConstraint('{}_{}_div5_loc'.format(moduleName, side), ctlB))
    # controls attr cleaning
    PostP.AttributeLockAndHide(ctlA, [at+ax for at in "trs" for ax in "xyz"])
    PostP.AttributeLockAndHide(ctlB, [at+ax for at in "ts" for ax in "xyz"])
    PostP.AttributeLockAndHide(ctlB, ['r'+ax for ax in "xyz"], doHide=False)
    PostP.AttributeLockAndHide(ctlA, ['v'], False)
    PostP.AttributeLockAndHide(ctlB, ['v'], False)
    # ikfkNode
    limb = PostP.IKFKChainSetUp(moduleName, side,
                                getFkControls(moduleName, side),
                                [ctlA,ctlB,ctlIk],
                                getUpVectorControl(moduleName, side),
                                PostP.getUIHostControl(moduleName, side) + '.leg_blend',
                                ctlRoll + '.rx' if ctlRoll else None,
                                'z')
    limb.swivelCombineMode = 1
    return limb