import MGearExtended.PostProUtils as PostP
import RigUtils.Core              as RUtils
import pymel.core                 as pm
import maya.cmds                  as cmds

###################################
########### leg_3jnt_01 ###########
###################################

# utils
def getSharedControls(limb, side):
    return ['{}_{}_{}_ctl'.format(limb, side, name) for name in ['root', 'knee', 'ankle']] + [PostP.getUIHostControl(limb, side)]

def getFkControls(limb, side):
    return cmds.ls("{}_{}_fk*_ctl".format(limb, side))

def getIkControls(limb, side):
    return ['{}_{}_{}_ctl'.format(limb, side, name) for name in ['upv','roll','ik','ikcns']]
#######


def FixFootJointOrient(moduleName, isMirrored=False):
    endRef = pm.PyNode("{}_end_ref".format(moduleName))
    endRefParent =  endRef.getParent()
    ctl = pm.PyNode("{}_fk3_ctl".format(moduleName))
    
    endRef.scaleX.set(1.0)
    endRefParent.scaleX.set(1.0)
    pm.matchTransform(endRef, ctl, rot=True)
    if (isMirrored):
        currentZRot = endRef.rz.get()
        endRef.rz.set(currentZRot+180)


# #############################################################################################
# #############################################################################################
# #############################################################################################

def kneeStretchAnkleInfluence(limb, side, attributeName="kneeStretchAnkleInfluence"):
    uiHost = PostP.getUIHostControl(limb, side)
    if attributeName not in cmds.listAttr(uiHost):
        cmds.addAttr(uiHost, ln=attributeName, at="double", min=0, max=1, dv=0.5, k=True)
    dist = cmds.createNode("distanceBetween")
    div = cmds.createNode("multDoubleLinear")
    clamp = cmds.createNode("clamp")
    minus = cmds.createNode("plusMinusAverage")
    remap1 = cmds.createNode("remapValue")
    remap2 = cmds.createNode("remapValue")
    pair1 = cmds.listConnections("{}_{}_legBones1_jnt.t".format(limb, side), d=False)[0]
    pair2 = cmds.listConnections("{}_{}_legBones2_jnt.t".format(limb, side), d=False)[0]
    ################
    cmds.setAttr(div + ".i2", 0.5)
    cmds.setAttr(minus + ".operation", 2)
    cmds.setAttr(clamp + ".max", 999,999,999)
    cmds.setAttr(remap1 + ".value[1].value_Position", 0.5)
    cmds.setAttr(remap1 + ".value[2].value_Position", 1)
    cmds.setAttr(remap2 + ".value[1].value_Position", 0.5)
    cmds.setAttr(remap2 + ".value[2].value_Position", 1)
    ################
    cmds.connectAttr("{}_{}_root_ctl.wm[0]".format(limb, side), dist + ".inMatrix1")
    cmds.connectAttr("{}_{}_ik2B_ik_ref.wm[0]".format(limb, side), dist + ".inMatrix2")
    cmds.connectAttr(dist + ".distance", div + ".input1")
    cmds.connectAttr(dist + ".distance", minus + ".input1D[0]")
    cmds.connectAttr("{}_{}_chain2bones2_jnt.tx".format(limb, side), minus + ".input1D[1]")
    cmds.connectAttr(div + ".output", clamp + ".inputR")
    cmds.connectAttr(minus + ".output1D", clamp + ".inputG")
    cmds.connectAttr(div + ".output", clamp + ".inputB")
    cmds.connectAttr("{}_{}_chain2bones1_jnt.tx".format(limb, side), clamp + ".minR")
    cmds.connectAttr("{}_{}_chain2bones1_jnt.tx".format(limb, side), clamp + ".minG")
    cmds.connectAttr("{}_{}_chain2bones2_jnt.tx".format(limb, side), clamp + ".minB")
    cmds.connectAttr("{}.{}".format(uiHost, attributeName), remap1 + ".inputValue")
    cmds.connectAttr("{}.{}".format(uiHost, attributeName), remap2 + ".inputValue")
    cmds.connectAttr("{}_{}_legIK1_jnt.tx".format(limb, side), remap1 + ".value[0].value_FloatValue")
    cmds.connectAttr(clamp + ".outputR", remap1 + ".value[1].value_FloatValue")
    cmds.connectAttr(clamp + ".outputG", remap1 + ".value[2].value_FloatValue")
    cmds.connectAttr(remap1 + ".outValue", pair1 + ".inTranslateX2")
    cmds.connectAttr("{}_{}_legIK1_jnt.ty".format(limb, side), pair1 + ".inTranslateY2")
    cmds.connectAttr("{}_{}_legIK1_jnt.tz".format(limb, side), pair1 + ".inTranslateZ2")
    cmds.connectAttr("{}_{}_legIK2_jnt.tx".format(limb, side), remap2 + ".value[0].value_FloatValue")
    cmds.connectAttr(clamp + ".outputB", remap2 + ".value[1].value_FloatValue")
    cmds.connectAttr("{}_{}_chain2bones2_jnt.tx".format(limb, side), remap2 + ".value[2].value_FloatValue")
    cmds.connectAttr(remap2 + ".outValue", pair2 + ".inTranslateX2")
    cmds.connectAttr("{}_{}_legIK2_jnt.ty".format(limb, side), pair2 + ".inTranslateY2")
    cmds.connectAttr("{}_{}_legIK2_jnt.tz".format(limb, side), pair2 + ".inTranslateZ2")

def poleAddRollControl(limb, side):
    '''Calls MGearExtended.PostProUtils.PoleVectorRollControl with its own config'''
    return PostP.PoleVectorRollControlQuadruped(limb, side, 'x', True)

def fixPoleEnumAttrSpace(limb, side):
    '''Recommend to call always. Compares control.attribute enum switch to associated constraint targets and edits attribute values'''
    uiHost = PostP.getUIHostControl(limb, side)
    if 'leg_upvref' in cmds.listAttr(uiHost):
        PostP.FixEnumAttrSpace("{}.leg_upvref".format(uiHost), "{}_{}_upv_cns_parentConstraint1".format(limb, side))

def poleAddCustomSpace(limb, side, attrCustomName='custom'):
    '''Search space switch attribute "leg_upvref" and add Custom option'''
    uiHost = PostP.getUIHostControl(limb, side)
    if 'leg_upvref' in cmds.listAttr(uiHost):
        PostP.SpaceAutoPoleVector(limb, side, attrCustomName)

def fixDefaultAttributes(limb, side):
    '''Recommend to call always. Lock and hide attribute "leg_fullIK" and connects "ik_cns" control to "leg_blend" ui host attribute'''
    uiHost = PostP.getUIHostControl(limb, side)
    RUtils.smartSetAttr(uiHost + '.leg_fullIK', 0, l=True, k=False)
    RUtils.smartSetAttr("{}_{}_root_ctlShape.lodVisibility".format(limb, side), False)
    RUtils.smartSetAttr("{}_{}_ik_cns.v".format(limb, side), l=False)
    cmds.connectAttr("{}.leg_blend".format(uiHost), "{}_{}_ik_cns.v".format(limb, side))
    RUtils.smartSetAttr("{}_{}_ik_cns.v".format(limb, side), l=True)

def fixRollPlane(limb, side):
    '''Recommend to call always. Edit module behaviour so any leg segment breaks plane'''
    uiHost = PostP.getUIHostControl(limb, side)
    # delete default operation nodes
    to_del = cmds.listConnections('{}.leg_roll'.format(uiHost))
    for to_d in to_del:
        cnn = cmds.listConnections(to_d, s=False) or []
        if "{}_{}_ik2BonesHandle".format(limb, side) not in cnn and "{}_{}_ik3BonesHandle".format(limb, side) not in cnn:
            to_del.extend( cnn )
    cmds.delete(to_del)
    # hierarchy system
    root = cmds.createNode('transform', p="{}_{}_ik_ctl".format(limb, side), n='{}_{}_ik2B_A_root'.format(limb, side))
    rootCns = cmds.aimConstraint('{}_{}_root_ctl'.format(limb, side), root, wuo='{}_{}_legUpvRef0_jnt'.format(limb, side), aim=[0,1,0], u=[0,0,1], wut='objectrotation', wu=[0,1,0])[0]
    poleRoll = cmds.parent(cmds.createNode('transform', p="{}_{}_upv_ctl".format(limb, side), n="{}_{}_upv_pole_roll".format(limb, side)), root)
    ctlRoll = cmds.createNode('transform', p="{}_{}_upv_cns".format(limb, side), n="{}_{}_upv_roll".format(limb, side))
    cmds.parentConstraint(poleRoll, ctlRoll)
    cmds.parent("{}_{}_ik2B_A_ref".format(limb, side), root)
    cmds.parent("{}_{}_upv_ctl".format(limb, side), ctlRoll)
    # attr
    cmds.connectAttr(uiHost + ".leg_roll", rootCns + ".offsetY")
    PostP.AttributeLockAndHide(ctlRoll, ["tx","ty","tz","rx","ry","rz","sx","sy","sz","v"])

def doKeyingGroups(limb, side):
    legKG = PostP.KeyingGroupSetUp(limb, side, getSharedControls(limb, side))
    legFkKG = PostP.KeyingGroupSetUp(limb, side, getFkControls(limb, side), legKG)
    legIkKG = PostP.KeyingGroupSetUp(limb, side, getIkControls(limb, side), legKG)
    return legKG, legFkKG, legIkKG
    
def doIKFKChainConfig(limb, side):
    PostP.IKFKChainSetUp(limb, side, getFkControls(limb, side),
                                     getIkControls(limb, side),
                                     '{}_{}_upv_ctl'.format(limb, side),
                                     PostP.getUIHostControl(limb, side) + ".leg_blend",
                                     '{}_{}_rollCustom_ctl.rx'.format(limb, side) if cmds.objExists('{}_{}_rollCustom_ctl'.format(limb, side)) else None)

def assertAttributeLockAndHide(limb, side):
    '''Sets lock and hide associated to each control in this "leg_3jnt_01" module'''
    # fk
    fkCtlLs = getFkControls(limb, side)
    for fkCtl in fkCtlLs[1:]:
        PostP.AttributeLockAndHide(fkCtl, ["tx","ty","tz","rx","ry","sy","sz"])
        PostP.AttributeLockAndHide(fkCtl, ["v"], False)
        PostP.AttributeKeyableToNonKeyable(fkCtl)
    PostP.AttributeLockAndHide(fkCtlLs[0], ["tx","ty","tz","sy","sz"])
    PostP.AttributeLockAndHide(fkCtlLs[0], ["v"], False)
    # "mid"
    for ctl in ["knee","ankle"]:
        PostP.AttributeLockAndHide('{}_{}_{}_ctl'.format(limb, side, ctl), ['ry','rz'])
    # roll
    PostP.AttributeLockAndHide('{}_{}_roll_ctl'.format(limb, side), ['ry','rz'])

def fixUpVectorSwitchSpace(limb, side):
    '''Changes pole vector logic to fix upvector switch spaces funcitonality'''
    
    # Create new upvector and reparent the old upvector and the new one
    upv_ctl = pm.PyNode("{}_{}_upv_ctl".format(limb,side))
    new_upv_ctl = pm.duplicate(upv_ctl, rr=True, po=True, name="{}_{}_upv_custom_ctl".format(limb,side))[0]
    pm.parent("{}_{}_upv_ctlShape".format(limb,side), new_upv_ctl, r=True, s=True)
    
    ### Change connections from original upv to custom upv just in case, maybe this not ncessary ###
    pm.disconnectAttr("{}UI_{}_ctl.message".format(limb,side), "{}_{}_upv_ctl.uiHost_cnx".format(limb,side))
    pm.connectAttr("{}UI_{}_ctl.message".format(limb,side), "{}.uiHost_cnx".format(new_upv_ctl))

    pm.disconnectAttr("{}Orig_{}_ctl|{}_{}_root.message".format(limb,side,limb,side), "{}_{}_upv_ctl.compRoot".format(limb,side))
    pm.connectAttr("{}Orig_{}_ctl|{}_{}_root.message".format(limb,side,limb,side), "{}.compRoot".format(new_upv_ctl))

    pm.disconnectAttr("{}_{}_upv_ctl.message".format(limb,side), "{}_{}_upv_ctl_tag.controllerObject".format(limb,side))
    pm.connectAttr("{}.message".format(new_upv_ctl), "{}_{}_upv_ctl_tag.controllerObject".format(limb,side))
    
    curve_cns_conn = getTargetConnection("{}_{}_upv_ctl.worldMatrix[0]".format(limb,side), "mgear_curveCns")
    pm.disconnectAttr("{}_{}_upv_ctl.worldMatrix[0]".format(limb,side), curve_cns_conn)
    pm.connectAttr("{}.worldMatrix[0]".format(new_upv_ctl), curve_cns_conn)

    dag_pose_conn = getTargetConnection("{}_{}_upv_ctl.message".format(limb,side), "dagPose")
    pm.disconnectAttr("{}_{}_upv_ctl.message".format(limb,side), dag_pose_conn)
    pm.connectAttr("{}.message".format(new_upv_ctl), dag_pose_conn)
    
    comp_ctl_conn = getTargetConnection("{}_{}_upv_ctl.message".format(limb,side), "compCtl")
    pm.disconnectAttr("{}_{}_upv_ctl.message".format(limb,side), comp_ctl_conn)
    pm.connectAttr("{}.message".format(new_upv_ctl), comp_ctl_conn)
    
    ### Custom upvector matrices logic ###
    pm.parent(upv_ctl, "{}_{}_upv_cns".format(limb,side))
    pm.parent(new_upv_ctl, "{}_{}_upv_cns".format(limb,side))
    upv_ctl_grp = pm.group(upv_ctl, name="{}_{}_upv_ctl_grp".format(limb,side))
    rollCustom_ctl = pm.PyNode("{}_{}_rollCustom_ctl".format(limb,side))

    decMtrx1 = pm.createNode("decomposeMatrix", name="{}_{}_decomposeMatrix1".format(limb,side))
    decMtrx2 = pm.createNode("decomposeMatrix", name="{}_{}_decomposeMatrix2".format(limb,side))
    comMtrx1 = pm.createNode("composeMatrix", name="{}_{}_composeMatrix1".format(limb,side))
    multDiv1 = pm.createNode("multiplyDivide", name="{}_{}_multiplyDivide1".format(limb,side))
    multMtrx1 = pm.createNode("multMatrix", name="{}_{}_multMatrix1".format(limb,side))
    multMtrx2 = pm.createNode("multMatrix", name="{}_{}_multMatrix2".format(limb,side))
    multMtrx3 = pm.createNode("multMatrix", name="{}_{}_multMatrix3".format(limb,side))
    multMtrx4 = pm.createNode("multMatrix", name="{}_{}_multMatrix4".format(limb,side))
    invMtrix1 = pm.createNode("inverseMatrix", name="{}_{}_inverseMatrix1".format(limb,side))

    pm.connectAttr("{}.matrix".format(rollCustom_ctl), "{}.inputMatrix".format(decMtrx1))
    pm.connectAttr("{}.outputRotate".format(decMtrx1), "{}.input1".format(multDiv1))
    pm.setAttr("{}.input2X".format(multDiv1), 0)
    pm.connectAttr("{}.output".format(multDiv1), "{}.inputRotate".format(comMtrx1))
    pm.connectAttr("{}.outputQuat".format(decMtrx1), "{}.inputQuat".format(comMtrx1))
    pm.connectAttr("{}.outputScale".format(decMtrx1), "{}.inputScale".format(comMtrx1))
    pm.connectAttr("{}.outputShear".format(decMtrx1), "{}.inputShear".format(comMtrx1))
    pm.connectAttr("{}.outputTranslate".format(decMtrx1), "{}.inputTranslate".format(comMtrx1))

    pm.connectAttr("{}.outputMatrix".format(comMtrx1), "{}.matrixIn[0]".format(multMtrx1))
    pm.connectAttr("{}.parentMatrix[0]".format(rollCustom_ctl), "{}.matrixIn[1]".format(multMtrx1))
    pm.connectAttr("{}.matrixSum".format(multMtrx1), "{}.inputMatrix".format(invMtrix1))

    pm.connectAttr("{}.worldMatrix[0]".format(new_upv_ctl), "{}.matrixIn[0]".format(multMtrx2))
    pm.connectAttr("{}.outputMatrix".format(invMtrix1), "{}.matrixIn[1]".format(multMtrx2))

    pm.connectAttr("{}.matrixSum".format(multMtrx2), "{}.matrixIn[0]".format(multMtrx3))
    pm.connectAttr("{}.worldMatrix[0]".format(rollCustom_ctl), "{}.matrixIn[1]".format(multMtrx3))

    pm.connectAttr("{}.matrixSum".format(multMtrx3), "{}.matrixIn[0]".format(multMtrx4))
    pm.connectAttr("{}.parentInverseMatrix[0]".format(upv_ctl_grp), "{}.matrixIn[1]".format(multMtrx4))

    pm.connectAttr("{}.matrixSum".format(multMtrx4), "{}.inputMatrix".format(decMtrx2))
    pm.connectAttr("{}.outputTranslate".format(decMtrx2), "{}.translate".format(upv_ctl_grp))
    
    # Reconnect message from original upv to the new custom one
    conns = pm.listConnections("{}UI_{}_ctl.leg_id0_ctl_cnx".format(limb,side), c=True, p=True)
    target_message = None
    for conn in conns:
        # Check if original upv is found, to retrieve is message destination
        if (conn[1].split(".")[0] == upv_ctl.name()):
            target_message = conn[0]
            break
    if (target_message is not None):
        pm.disconnectAttr("{}.message".format(upv_ctl), target_message)
        pm.connectAttr("{}.message".format(new_upv_ctl), target_message)
        # Clean original upv translation
        pm.setAttr("{}.translateX".format(upv_ctl), 0)
        pm.setAttr("{}.translateY".format(upv_ctl), 0)
        pm.setAttr("{}.translateZ".format(upv_ctl), 0)

def getTargetConnection(source, target):
    target_connection = None
    conns = pm.listConnections(source, c=True, p=True)
    for conn in conns:
        if (target in str(conn[1])):
            target_connection = str(conn[1])
            break
    return target_connection

def fixFKIKSwitch(limb, side):
    '''Fix FKIK switch for the ik to fk mGear's snap'''
    
    ### This part fixes the IK to FK switch behaviour ###
    pm.disconnectAttr("{}_{}_upv_mth.message".format(limb,side), "{}_{}_upv_ctl.match_ref".format(limb,side))
    pm.connectAttr("{}_{}_upv_mth.message".format(limb,side), "{}_{}_upv_custom_ctl.match_ref".format(limb,side))

    # Unlock rotations for last fk control
    pm.setAttr("{}_{}_fk2_ctl.rotateX".format(limb,side), k=True)
    pm.setAttr("{}_{}_fk2_ctl.rotateY".format(limb,side), k=True)
    pm.setAttr("{}_{}_fk2_ctl.rotateX".format(limb,side), lock=False)
    pm.setAttr("{}_{}_fk2_ctl.rotateY".format(limb,side), lock=False)
    
    # Parent last fk reference to the previuous one
    pm.parent("{}_{}_fk3_mth".format(limb,side), "{}_{}_fk2_mth".format(limb,side))
    pm.setAttr("{}_{}_fk3_mth.translateX".format(limb,side), 0)
    pm.setAttr("{}_{}_fk3_mth.translateY".format(limb,side), 0)
    pm.setAttr("{}_{}_fk3_mth.translateZ".format(limb,side), 0)
    pm.setAttr("{}_{}_fk3_mth.rotateX".format(limb,side), 0)
    pm.setAttr("{}_{}_fk3_mth.rotateY".format(limb,side), 0)
    pm.setAttr("{}_{}_fk3_mth.rotateZ".format(limb,side), 0)
    
    # Rename current custom roll and create a new one so mGear's fkik switch won't complain
    pm.renameAttr("{}UI_{}_ctl.leg_roll".format(limb,side), "custom_pole_roll")
    pm.addAttr("{}UI_{}_ctl".format(limb,side), longName="leg_roll", niceName="LegRoll", attributeType="float")
    pm.setAttr("{}_{}_roll_ctl.ctl_role".format(limb,side), "leg_end_pivot")
    
    ### Change mth logic so they won't translate if custom roll rotates ###
    mths = ["{}_{}_fk1_mth".format(limb,side), "{}_{}_fk2_mth".format(limb,side)]
    
    rollCustom_ctl = pm.PyNode("{}_{}_rollCustom_ctl".format(limb,side))
    
    for mth in mths:
        # Reorganize hierarchy
        mthZero = pm.group(name="{}_zero".format(mth), em=True)
        srcXform = pm.xform(mth, query=True, worldSpace=True, m=True)
        pm.xform(mthZero, worldSpace=True, m=srcXform)
        mthParent = pm.listRelatives(mth, parent=True)
        pm.parent(mthZero, mthParent)
        pm.parent(mth, mthZero)
        mthGrp = pm.group(mth, name="{}_grp".format(mth))
        # Create necessary nodes for this behaviour and connect them
        multMtrx1 = pm.createNode("multMatrix", name="{}_multMatrix1".format(mth))
        multMtrx2 = pm.createNode("multMatrix", name="{}_multMatrix2".format(mth))
        multMtrx3 = pm.createNode("multMatrix", name="{}_multMatrix3".format(mth))
        decMtrx1 = pm.createNode("decomposeMatrix", name="{}_decomposeMatrix1".format(mth))
        
        pm.connectAttr("{}.worldMatrix[0]".format(mthZero), "{}.matrixIn[0]".format(multMtrx1))
        pm.connectAttr("{}.worldInverseMatrix[0]".format(rollCustom_ctl), "{}.matrixIn[1]".format(multMtrx1))
        
        pm.connectAttr("{}.matrixSum".format(multMtrx1), "{}.matrixIn[0]".format(multMtrx2))
        pm.connectAttr("{}_{}_multMatrix1.matrixSum".format(limb,side), "{}.matrixIn[1]".format(multMtrx2))
        
        pm.connectAttr("{}.matrixSum".format(multMtrx2), "{}.matrixIn[0]".format(multMtrx3))
        pm.connectAttr("{}.parentInverseMatrix[0]".format(mthGrp), "{}.matrixIn[1]".format(multMtrx3))
        
        pm.connectAttr("{}.matrixSum".format(multMtrx3), "{}.inputMatrix".format(decMtrx1))
        pm.connectAttr("{}.outputTranslate".format(decMtrx1), "{}.translate".format(mthGrp))

# set up
def fullSetUp(limb, side, fixDefaultAttrs=True,
                          fixDefaultPoleSpace=True,
                          fixDefaultRollPlane=True,
                          poleCustomSpaceSwitch=True,
                          assertAttributeCleaning=True,
                          poleAddRollCtl=True,
                          kneeStretchInf=True,
                          resetIkSpaceOffset=True,
                          keyingGroups=True):
    '''Set behaviour in this "leg_3jnt_01" module'''
    if fixDefaultAttrs: fixDefaultAttributes(limb, side)
    if fixDefaultPoleSpace: fixPoleEnumAttrSpace(limb, side)
    if fixDefaultRollPlane: fixRollPlane(limb, side)
    if poleCustomSpaceSwitch: poleAddCustomSpace(limb, side)
    if assertAttributeCleaning: assertAttributeLockAndHide(limb, side)
    if poleAddRollCtl: poleAddRollControl(limb, side)
    if kneeStretchInf: kneeStretchAnkleInfluence(limb, side)
    if resetIkSpaceOffset: PostP.ResetSpaceConstraint(limb, side)
    if keyingGroups: doKeyingGroups(limb, side)

def fullSetUpByGuide(**fullSetUpArgs):
    '''Search under "guide" node's "leg_3jnt_01" modules to then call "fullSetUp"'''
    for node in cmds.listRelatives("guide", ad=True, type="transform", f=True):
        if "comp_type" in cmds.listAttr(node) and cmds.getAttr(node + ".comp_type") == "leg_3jnt_01":
            name = cmds.getAttr(node + ".comp_name")
            side = "{}{}".format(cmds.getAttr(node + ".comp_side"), cmds.getAttr(node + ".comp_index"))
            fullSetUp(name, side, **fullSetUpArgs)