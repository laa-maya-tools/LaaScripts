import maya.cmds as cmds
import json
import pymel.core as pm
import MGearExtended.PostProUtils as PostP

from ShapeControlEditor.shapeControlEditor import ShapeControlEditorWin

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
    return PostP.getControl(moduleName, side, 'roll', checkSet)

def getIkControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ik', checkSet)

def getIkCnsControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'ikcns', checkSet)

def getIkControls(moduleName, side, checkSet=True):
    result = [getUpVectorControl(moduleName, side, checkSet),
              getRollControl(moduleName, side, checkSet),
              getIkControl(moduleName, side, checkSet),
              getIkCnsControl(moduleName, side, checkSet)]
    return [member for member in result if member]
#######


# ###############################################
# ############ Commodities ######################
# ###############################################
def GetModuleControlsRoot(moduleName):
    matches = pm.ls("{}_root".format(moduleName))
    result = None
    for match in matches:
        # If the node has this attribute, it is the root for the module controls
        if (pm.attributeQuery("compCtl", node=match, ex=True)):
            result = match
            break
    return result

def GetChildRollRoot(moduleName):
    result = None
    ctlRoot = GetModuleControlsRoot(moduleName)
    if (ctlRoot):
        # The module has a 'footroll' child if the root node has this attribute
        if (pm.attributeQuery("footCnx", node=ctlRoot, ex=True)):
            result = ctlRoot.footCnx.get()
    return result

def GetUIHostRoot(ctlPyNode):
    UIHostRoot  = None
    conns = ctlPyNode.uiHost_cnx.connections()
    if conns:
        UIHost = conns[0]
        UIHostRoot = UIHost.compRoot.connections()[0]
    return UIHostRoot

# #############################################
# ########### Customizations ##################
# #############################################

def RollFollowElbow(moduleName):
    """Makes the Roll Control follow the elbow of the arm insted of the default behaviour that
    follows a point in between the shoulder and the wrist.

    Args:
        moduleName (String): Base Name of the arm module to operate with
    """
    npo = pm.PyNode("{}_roll_ctl_npo".format(moduleName))
    elbowCtl = pm.PyNode("{}_mid_ctl".format(moduleName))
    
    # Delete npo Pparent Constraint
    parentConstraints = npo.getChildren(type='parentConstraint')
    for cns in parentConstraints:
        pm.delete(cns)
        
    # As the ctl will rotate with the same arm it controls, we offset its own transform
    theCtl = npo.getChildren(type='transform')[0]
    pm.connectAttr(theCtl.inverseMatrix, theCtl.offsetParentMatrix)
    
    # Unlock/Relock NPO translation and set it
    PostP.SetAttribLocked([npo.tx, npo.ty, npo.tz, npo.rx, npo.ry, npo.rz], False)
    pm.matchTransform(npo, elbowCtl, position=True)
    pm.parent(npo, elbowCtl)
    PostP.SetAttribLocked([npo.tx, npo.ty, npo.tz, npo.rx, npo.ry, npo.rz], True)

def FixMirroredFKHandOrient(moduleName):
    """When 'Align Wrist to Guide Orientation' is used, the mirroring from one side to another
    will flip the underlying bone structure. This Fixes that problem for the mirrored arm/s

    Args:
        moduleName (String): Base Name of the mirrored module
    """
    npo     = pm.PyNode("{}_fk2_npo".format(moduleName))
    fkCtl   = pm.PyNode("{}_fk2_ctl".format(moduleName))
    ikMth   = pm.PyNode("{}_ik_mth".format(moduleName))
    fkMth   = pm.PyNode("{}_fk2_mth".format(moduleName))
    ikCtlRef= pm.PyNode("{}_ikCtl_ref".format(moduleName))
    
    # ############# Gathering Data #################
    # ##############################################
    tempParent = pm.group(name="temp", empty=True)
    
    #Look for a UI Host Node
    UIHostRoot  = GetUIHostRoot(fkCtl)
    if (UIHostRoot):
        UIHostRootParent = UIHostRoot.getParent()
        UIHostRoot.setParent(tempParent)
    
    #Look for any children on the end of the chain
    chainEnd = pm.PyNode("{}_eff_loc".format(moduleName))
    handChildren = chainEnd.getChildren()
    for child in handChildren:
        child.setParent(tempParent)
    
    # If there is a Roll child, we must regenerate the constraint on '{rollModule}_fk_ref' after the fixing is done
    childRollRoot = GetChildRollRoot(moduleName)
    if (childRollRoot):
        parentCnsTarget = None
        rollModuleName = childRollRoot.getName().replace("_root", "")
        rollFkRef = pm.PyNode("{}_fk_ref".format(rollModuleName))
        pConsts = pm.listRelatives(rollFkRef, allDescendents=False, type="parentConstraint")
        if (pConsts):
            pConst = pConsts[0]
            targets = pConst.getTargetList()
            if (targets):
                parentCnsTarget = targets[0]
            pm.delete(pConst)
    
    # ############ Fix Rotation ##################
    # ############################################
    ikMth.setParent(tempParent)
    PostP.SetAttribLocked([npo.rx, npo.ry, npo.rz], False)
    auxRot = pm.group(empty=True)
    pm.matchTransform(auxRot, npo)
    auxRot.setParent(npo)
    pm.rotate(auxRot, [0,0,180])
    pm.matchTransform(npo, auxRot)
    pm.delete(auxRot)
    PostP.SetAttribLocked([npo.rx, npo.ry, npo.rz], True)
    ikMth.setParent(fkCtl)
    
    pm.matchTransform(fkMth, npo)
    pm.matchTransform(ikCtlRef, npo)
    
    # If the arm has a 'footRoll' child we need to align these two
    if (childRollRoot):
        ikRef = pm.PyNode("{}_ik_ref".format(moduleName))
        fkRef = pm.PyNode("{}_fk_ref".format(moduleName))
        pm.matchTransform(ikRef, fkRef)
        
        pm.parentConstraint(parentCnsTarget, rollFkRef, mo=True)
    
    # ################ Reconstruct neccesary from gathered data ################
    # ##########################################################################
    # Reparent Host UI and other dependants
    if (UIHostRoot):
        UIHostRoot.setParent(UIHostRootParent)
    
    for child in handChildren:
        child.setParent(chainEnd)
        # Update 'self' parent constraints
        pConsts = pm.listRelatives(chainEnd, allDescendents=True, type="parentConstraint")
        for pConst in pConsts:
            numTargets = pConst.target.evaluateNumElements()
            for i in range(numTargets):
                if (pConst.target[i].targetParentMatrix.inputs()[0] == chainEnd):
                    transVector = pm.getAttr("{}.target[{}].targetOffsetTranslate".format(pConst, i))
                    modifVector = [-transVector[0], -transVector[1], transVector[2]]
                    pm.setAttr("{}.target[{}].targetOffsetTranslate".format(pConst, i), modifVector)
                    rotVector = pm.getAttr("{}.target[{}].targetOffsetRotate".format(pConst, i))
                    print(rotVector)
                    # This could be another axis in other circumstances. TODO: Support should be added sometime.
                    rotVector[2] -= 180
                    pm.setAttr("{}.target[{}].targetOffsetRotate".format(pConst, i), rotVector)
                    print(rotVector)
    
    pm.delete(tempParent)

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
    cmds.connectAttr(PostP.getUIHostControl(moduleName, side) + ".arm_blend", npo + ".v")
    cmds.aimConstraint(ctlRoll, npo, aim=[1,0,0], u=[0,0,1], wut='objectrotation', wuo=ctlRoll, wu=[0,0,1])
    cmds.aimConstraint(ctlIk, ctlB, aim=[1,0,0], u=[0,0,1], wut='objectrotation', wuo=ctlRoll, wu=[0,0,1])
    cmds.delete(cmds.pointConstraint(ctlRoll, ctlB))
    # controls attr cleaning
    PostP.AttributeLockAndHide(ctlA, [at+ax for at in "trs" for ax in "xyz"])
    PostP.AttributeLockAndHide(ctlB, [at+ax for at in "ts" for ax in "xyz"])
    PostP.AttributeLockAndHide(ctlB, ['r'+ax for ax in "xyz"], doHide=False)
    PostP.AttributeLockAndHide(ctlA, ['v'], False)
    PostP.AttributeLockAndHide(ctlB, ['v'], False)
    # ikfkNode
    return PostP.IKFKChainSetUp(moduleName, side,
                         getFkControls(moduleName, side),
                         [ctlA,ctlB,ctlIk],
                         getUpVectorControl(moduleName, side),
                         PostP.getUIHostControl(moduleName, side) + '.arm_blend',
                         ctlRoll + '.rx',
                         'z')

def doKeyingGroups(moduleName, side, blend=True, fk=True, ik=True, keyGroupParent=None):
    blendKG,fkKG,ikKG = [None]*3
    toeCtl, footRollCtlLs = PostP.KeyingGroupFootFinder(moduleName, side)
    if blend:
        controlInputLs = [PostP.getUIHostControl(moduleName, side) + ".arm_blend"]
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