import json

import RigUtils.Core                                 as RUtils
import MGearExtended.ModulesCustomization.Foot_bk_01 as Foot
import pymel.core                                    as pm
import maya.cmds                                     as cmds

from ShapeControlEditor.shapeControlEditor       import ShapeControlEditorWin
from RigManager.IKFKChain                        import IKFKChain
from AnimSystems.KeyingGroup                     import KeyingGroup

# ################################################################################
# ----- Space Switching
# ################################################################################
def ResetSpaceConstraint(moduleName, side, skipIndexes=[]):
    '''Reset offset for each master in the input space constraint
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply'''
    spaceCns = '{}_{}_ik_cns_parentConstraint1'.format(moduleName, side)
    if not cmds.objExists(spaceCns):
        cmds.warning("Contraint '{}' does not exists".format(spaceCns))
        return False
    for idx, ind in enumerate(cmds.getAttr(spaceCns + ".target", mi=True)):
        if idx not in skipIndexes:
            cmds.setAttr("{}.target[{}].targetOffsetTranslate".format(spaceCns, ind), 0,0,0)
            cmds.setAttr("{}.target[{}].targetOffsetRotate".format(spaceCns, ind), 0,0,0)
    return True

def CreateSpaceSwitches(moduleName, partName, targets, UIHolder, UIAttrName, useSelf=True, maintainOffset=False, useParentGrp=False):
    """Creates a SpaceSwitch-like setup, with multiple targets. You can define what node will hold the UI dropdown for
    the Space Switching.
    
    Args:
        moduleName (String): Base Name of the module to operate with.
        partName (String): Name of the 'part' inside the module name that will have a parent Space Switch.
        targets (Array(String)): The nodes that will be Space Switches.
        UIHolder (String): Name of the control that will hold the attribute.
        UIAttrName (String): Name of the Enum in the Channel Box.
        useSelf (bool, optional): Add its own parent as "self" Space Switch. Defaults to True.
    """
    # Create New Driver Group
    ctl = pm.PyNode("{}_{}_ctl".format(moduleName, partName))
    if (useParentGrp):
        ctl = ctl.getParent()
    #npo = pm.PyNode("{}_{}_npo".format(moduleName, partName))
    switchName = "{}_{}_switch".format(moduleName, partName)
    if (pm.objExists(switchName)):
        switchNode = pm.PyNode(switchName)
        refNodeParent = switchNode.getParent()
    else:
        switchNode = pm.group(em=True, name=switchName)
        refNodeParent = ctl.getParent()
        if (not useParentGrp):
            pm.matchTransform(switchNode, refNodeParent, pos=True, rot=True)
        else:
            pm.matchTransform(switchNode, ctl, pos=True, rot=True)
        switchNode.setParent(refNodeParent)
        ctl.setParent(switchNode)
    
    # Generate Info
    allTargets = targets
    enumList = targets
    if (useSelf):
        selfRef = pm.group(empty=True, name = "{}_switchPoseRef".format(ctl.getName()))
        pm.matchTransform(selfRef, ctl, pos=True, rot=True)
        selfRef.setParent(refNodeParent)
        allTargets = [selfRef] + targets
        enumList = ["self"] + targets
    
    # Create Constraint
    cns = pm.parentConstraint(allTargets, switchNode, mo=maintainOffset)
    
    # Create UI Attribute
    pm.addAttr(UIHolder, ln=UIAttrName, at="enum", en=enumList, k=True)
    
    # Create Conditions
    for i, val in enumerate(allTargets):
        conditionNode = pm.createNode("condition")
        pm.connectAttr("{}.{}".format(UIHolder, UIAttrName), conditionNode.firstTerm)
        conditionNode.secondTerm.set(i)
        conditionNode.operation.set(0)
        conditionNode.colorIfTrueR.set(1)
        conditionNode.colorIfFalseR.set(0)
        realPlug = cns.target[i].targetWeight.inputs(p=True)[0]
        conditionNode.outColorR.connect(realPlug)
# ################################################################################

# ################################################################################
# ----- Arms Utils
# ################################################################################
def AddLegacySnapSupportToArm(armBaseName):
    """Creates a false 'ikRot_ctl' and 'ikRot_mth' in order to be used with the legacy Picker
    
    Args:
        armBaseName (String): base name of the arm limb. Ex: 'arm_L0'
    """
    handRef = "{}_fk_ref".format(armBaseName)
    
    # False ctl
    targetCtl = cmds.duplicate(handRef)
    targetCtl = cmds.rename(targetCtl, "{}_ikRot_ctl".format(armBaseName))
    
    # False mth
    targetMth = cmds.duplicate(handRef)
    targetMth = cmds.rename(targetMth, "{}_ikRot_mth".format(armBaseName))
# ################################################################################

# ################################################################################
# ----- Legs and Feet
# ################################################################################
def GetGroundPlantedOrient(nodeStart, nodeEnd, isMirrored=False, frontAxis=(1,0,0)):
    """Calculates the orientation corresponding to two points projected on the "ground" plane, assuming the "lookAt" axis is X.

    Args:
        nodeStart (String): 'Ankle' or Start Node
        nodeEnd (String): 'Foot tip' or End Node
        isMirrored (bool, optional): If True, returns the orientation of a mirrored Foot. Defaults to False.
        frontAxis (tuple, optional): Axis (X,Y,Z) looking to front. Defaults to (1,0,0).

    Returns:
        EulerAngles Array: World orientation 'planted' to ground.
    """
    p1 = cmds.xform(nodeStart, q=True, translation=True, ws=True)
    p2 = cmds.xform(nodeEnd, q=True, translation=True, ws=True)
    vector2 = (p2[0]-p1[0], 0, p2[2]-p1[2])
    if isMirrored:
        vector2 = (-vector2[0], 0, -vector2[2])
    
    angle = cmds.angleBetween(euler=True, v1=frontAxis, v2=vector2)
    if isMirrored:
        angle[0] = -180
    return angle
# ################################################################################

# ################################################################################
# ----- Shapes and Controls
# ################################################################################
def ControlToNonidentity(control, attrCleaning=True, hideShapes=True, setRemove=True):
    '''Given a control, it can: lock and hide keyable attributes, hide its shapes and/or removes from mGear set "rig_controllers_grp"'''
    if not any([attrCleaning, hideShapes, setRemove]):
        return
    if attrCleaning:
        AttributeLockAndHide(control, cmds.listAttr(control, k=True) or [])
    if hideShapes:
        for shape in cmds.listRelatives(control, s=True) or []:
            if not cmds.getAttr(shape + ".v", l=True) and not cmds.listConnections(shape + ".v"):
                cmds.setAttr(shape + ".v", False)
            elif not cmds.getAttr(shape + ".lodv", l=True) and not cmds.listConnections(shape + ".lodv"):
                cmds.setAttr(shape + ".lodv", False)
            else:
                cmds.warning("Shape '{}' has Visibility and LodVis locked".format(shape))
    if setRemove and cmds.objExists('rig_controllers_grp'):
        cmds.sets(control, rm='rig_controllers_grp', e=True)

def getControl(moduleName, side, name, checkSet=True):
    '''Search control by naming components
    
    Args:
        moduleName (string): component name to search by
        side (string): component side to search by
        name (string): name id to search by
        checkSet (bool, optional): check existence

    Returns:
        control name if checkSet and exists else control name'''
    ctl = '{}_{}_{}_ctl'.format(moduleName, side, name)
    if checkSet:
        if ctl in cmds.sets('rig_controllers_grp', q=True):
            return ctl
    else:
        return ctl

def getUIHostControl(moduleName, side, checkSet=True):
    '''Search control guide and get uiHost attribute value
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply

    Returns:
        uiHost if exists else global control'''
    for ctl in cmds.ls("{}*{}*ctl".format(moduleName, side)) or []:
        if "uiHost_cnx" in (cmds.listAttr(ctl, ud=True) or []):
            cnn = cmds.listConnections(ctl + ".uiHost_cnx")
            msg = [out.split(".")[1] for out in cmds.listConnections(ctl + '.message', p=True)]
            if cnn and 'uiHost_cnx' not in msg:
                return cnn[0]
    for root in cmds.ls("{}_{}*root".format(moduleName, side), l=True):
        if "guide" in root:
            uiHost = cmds.getAttr(root + ".ui_host")
            if cmds.objExists(uiHost):
                uiHost = uiHost.replace("root","ctl")
            elif cmds.objExists("world_ctl"):
                uiHost = "world_ctl"
            else:
                uiHost = "global_C0_ctl"
            if checkSet:
                if uiHost in cmds.sets('rig_controllers_grp', q=True):
                    return uiHost
            return uiHost

def ControlBuffer(controlInput, exceptionShape='cube'):
    '''Creates shape saved as mGear Buffer
    
    Args:
        controlInput (string): control input name
        exceptionShape (string): shape to attach if no buffer finded'''
    if cmds.objExists(controlInput + "_controlBuffer"):
        currentShapes = cmds.listRelatives(controlInput, shapes=True)
        newShapes = [shp for shp in cmds.listRelatives(controlInput + "_controlBuffer", shapes=True)]
        bufferTr = cmds.duplicate(controlInput + "_controlBuffer")[0]
        for ind,shp in enumerate(cmds.listRelatives(bufferTr, shapes=True)):
            cmds.parent(shp, controlInput, r=True, s=True)
            cmds.rename(shp, newShapes[ind])
        cmds.delete(currentShapes, bufferTr)
    else:
        ctlShape = ShapeControlEditorWin()
        with open("{}\{}.json".format(ctlShape.__library_path__, 'cube'), 'r') as f:
            ctlCurveDict = json.load(f)
        ctlShape.__addShapes__(controlInput, ctlCurveDict)

def CreateAxisShapes(theNode, useMaxBBox=False, fixedSize=0, extraPercent=50):
    """creates Axis shapes for a node. Uses the min bounding box size as default. Can use max bounding box size if specified or a fixed size.

    Args:
        theNode (PyNode): Node to create Axis Shapes
        useMaxBBox (bool, optional): Uses Maximum Bounding Box for size. Defaults to False.
        fixedSize (int, optional): Fixed Size of the Shapes. Defaults to 0.
        extraPercent (int, optional): Fine Adjust for "extra" Shape length. Defaults to 50.

    Returns:
        Array: Array of the Curves generated.
    """
    axis = ['x', 'y', 'z']
    shapes = []
    bbox = theNode.getBoundingBox()
    
    finalSize = 0
    if (fixedSize>0):
        finalSize = fixedSize
    elif (useMaxBBox):
        finalSize = max(bbox[1][0], bbox[1][1], bbox[1][2])
    else:
        finalSize = min(bbox[1][0], bbox[1][1], bbox[1][2])
        
    finalSize = finalSize * (1 + (extraPercent/100.0))
    
    xAxis = pm.curve(n='{}_xAxis'.format(theNode), d=1, p=[(0,0,0), (finalSize,0,0)])
    yAxis = pm.curve(n='{}_yAxis'.format(theNode), d=1, p=[(0,0,0), (0,finalSize,0)])
    zAxis = pm.curve(n='{}_zAxis'.format(theNode), d=1, p=[(0,0,0), (0,0,finalSize)])
    
    for axis in (xAxis, yAxis, zAxis):
        axisShape = axis.getChildren()[0]
        pm.setAttr(axisShape + '.overrideEnabled', 1)
        pm.setAttr(axisShape + '.overrideRGBColors', 1)
        pm.setAttr(axisShape + '.lineWidth', 3)
        
        if (axis == xAxis):
            pm.setAttr(axisShape + '.overrideColorR', 1)
        elif (axis == yAxis):
            pm.setAttr(axisShape + '.overrideColorG', 1)
        else:
            pm.setAttr(axisShape + '.overrideColorB', 1)
            
        pm.parent(axisShape, theNode, r=True, s=True)
        shapes.append(axisShape)
        pm.delete(axis)
        
    return shapes
# ################################################################################

# ################################################################################
# ----- Attributes
# ################################################################################
def FixEnumAttrSpace(controlAttrInput, spaceConstraint):
    '''Set enum values according to space constraint targets
    
    Args:
        controlAttrInput (string): nodeInput.attribute
        spaceConstraint (string): constraint name'''
    ###############################################
    # get the enum values and the constraint target
    # list, if target list is greater do reverse
    # iteration difference steps, so insert not
    # listed item in enum list items
    cnsType = cmds.nodeType(spaceConstraint)
    attrCnsLs = eval('cmds.{}(spaceConstraint, tl=True, q=True)'.format(cnsType))
    attrValLs = cmds.addAttr(controlAttrInput, en=True, q=True).split(":")
    if len(attrValLs) == len(attrCnsLs):
        # check
        return
    stepStop = len(attrCnsLs)-len(attrValLs)
    step = 0
    for ind, val in enumerate(attrCnsLs[::-1]):
        if step == stepStop:
            break
        ind = len(attrCnsLs)-ind-1
        if val not in attrValLs:
            attrValLs.insert(ind, val)
            step += 1
    cmds.addAttr(controlAttrInput, en=":".join(attrValLs), e=True)

def AttributeKeyableToNonKeyable(controlInput, attributeLs=['ro']):
    '''Set node input attribute non-keyable only if attribute is keyable
    
    Args:
        nodeInput (string): inpput node name
        attributeLs (list of string): attribute's short/long name list'''
    for at in attributeLs:
        if cmds.getAttr("{}.{}".format(controlInput, at), k=True):
            cmds.setAttr("{}.{}".format(controlInput, at), k=False, cb=True)
    
def AttributeLockAndHide(nodeInput, attributeLs, doLock=True, doHide=True):
    '''Set Lock and Hide in input attribute list only if attribute is already keyable
    
    Args:
        nodeInput (string): inpput node name
        attributeLs (list of string): attribute's short/long name list
        doLock (bool optional)
        doHide (bool optional)'''
    for at in attributeLs:
        if cmds.getAttr("{}.{}".format(nodeInput, at), k=True):
            cmds.setAttr("{}.{}".format(nodeInput, at), k=not doHide, l=doLock)


def GetLockedTransforms(node):
    node = pm.PyNode(node)
    transAttribs = [
        node.tx,
        node.ty,
        node.tz,
        node.rx,
        node.ry,
        node.rz,
        node.sx,
        node.sy,
        node.sz
    ]
    
    lockedAttribs = []
    for attrib in transAttribs:
        if (attrib.isLocked()):
            lockedAttribs.append(attrib)
    
    return lockedAttribs

def SetTransformsLocked(node, value, translate=False, rotation=False, scale=False):
    """Fast Set transformations attributes lock status. By default, all transforms will be set.

    Args:
        node (string or PyNode): Node to work with
        value (bool): Value to be set
        translate (bool, optional): Set Translation attributes locked status. Defaults to False.
        rotation (bool, optional): Set Rotation attributes locked status. Defaults to False.
        scale (bool, optional): Set Scale Attributes locked status. Defaults to False.
    """
    node = pm.PyNode(node)
    if (translate == rotation == scale):
        translate = rotation = scale = True
    
    if (translate):
        SetAttribLocked([node.tx, node.ty, node.tz], value)
    
    if (rotation):
        SetAttribLocked([node.rx, node.ry, node.rz], value)
    
    if (translate):
        SetAttribLocked([node.sx, node.sy, node.sz], value)

def SetAttribLocked(attribList, lockValue):
    """Sets attributes lock value

    Args:
        attribList (Array of 'pymel.core.general.Attribute'): Pymel Attributes to set
        lockValue (bool): Desired Value. If True, attributes will be locked. If False, Attributes will be unlocked."""
    for attrib in attribList:
            attrib.set(lock=lockValue)
# ################################################################################

# ################################################################################
# ----- Limb Utils
# ################################################################################
def TriangulateHips(moduleName, side, newControl=False):
    hipsCtl = '{}_{}_ctl'.format(moduleName, side)
    for hipsRoot in cmds.ls('{}_{}_root'.format(moduleName, side), l=True):
        if "rig" in hipsRoot:
            hipsParent = cmds.listRelatives(hipsRoot, p=True, f=True)[0]
            grp = cmds.createNode('transform', n='{}Chils_{}_ctl'.format(moduleName, side), p=hipsCtl)
            cmds.parent(cmds.listRelatives(hipsCtl, type='transform', f=True), grp)
            sourceTr = cmds.createNode('transform', n='{}IsolateSrc_{}_tr'.format(moduleName, side), p=hipsCtl)
            targetTr = cmds.createNode('transform', n='{}IsolateTrg_{}_tr'.format(moduleName, side), p=hipsParent)
            cmds.setAttr(sourceTr + ".tx", -10)
            cmds.pointConstraint(sourceTr, targetTr, sk=['x'])
            cmds.aimConstraint(targetTr, grp, aim=[-1,0,0], u=[0,1,0], wu=[0,1,0],
                            wut='objectrotation', wuo=hipsCtl)
            if newControl:
                root = cmds.createNode('transform', n='{}Main_{}_root'.format(moduleName, side), p=hipsParent)
                ctl = cmds.createNode('transform', n='{}Main_{}_ctl'.format(moduleName, side), p=root)
                cmds.parent(hipsRoot, targetTr, ctl)
                ControlBuffer(ctl)
                return root, ctl
            return

def KeyingGroupSetUp(moduleName, side, controlInputLs, keyGroupParent=None, enabled=True, add=False, remove=False):
    '''Creates customKeyingGroup node to set multi keying system behaviour
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply
        controlInputLs(list of strings): every affected control. If format != "control.attribute" and format == "control": all keyable attributes are affected
        keyGroupParent(string, optional): customKeyingGroup parent of this one
        enabled(bool, optional): customKeyingGroup default state
        add(bool, optional): if True, add "controlInputLs" to "keyGroupParent", so "moduleName" and "side" must be None
        remove(bool, optional): if True, remove "controlInputLs" from "keyGroupParent", so "moduleName" and "side" must be None
        
    Returns: KeyingGroup node created if so'''
    isCreation = True
    if type(controlInputLs) != list:
        controlInputLs = [controlInputLs]
    # set if has to "create", "add" or "remove"
    if add or remove:
        isCreation = False
        if not keyGroupParent:
            cmds.warning("Tu ereh tonnnnnnto")
            return
        elif type(keyGroupParent) != KeyingGroup:
            cmds.warning("Arg 'keyGroupParent' type is not valid")
            return keyGroupParent
        kgrp = keyGroupParent
    else:
        kgrp = KeyingGroup()
        kgrp.create('{}_{}_keyingGroup'.format(moduleName, side))
    # handle connections
    cmds.waitCursor(st=True)
    for ctl in controlInputLs:
        if not ctl:
            # check ctl != None
            continue
        if "." in ctl:
            attrLs = [ctl]
        else:
            kAttrs = cmds.listAttr(ctl, k=True) or []
            prxAttrs = RUtils.listAttrProxies(ctl)
            attrLs = ['{}.{}'.format(ctl,attr) for attr in (list(set(kAttrs) - set(prxAttrs)))]
        for ctlAttr in attrLs:
            proxySource = cmds.listConnections(ctlAttr,d=False,p=True)
            if proxySource:
                ctlAttr = proxySource[0]
            if ctlAttr in kgrp.getAffectedAttributes():
                if remove:
                    kgrp.removeAffectedAttribute(ctlAttr)
            else:
                if not remove:
                    kgrp.addAffectedAttribute(ctlAttr)
    cmds.waitCursor(st=False)
    if isCreation:
        kgrp.enabled = enabled
        if keyGroupParent:
            if type(keyGroupParent) == KeyingGroup:
                keyGroupParent.addChildKeyingGroup(kgrp)
            else:
                for ind in range(999):
                    if not cmds.listConnections("{}.childKeyingGroups[{}]".format(keyGroupParent, ind)):
                        break
                cmds.connectAttr("{}.keyGroupParent".format(kgrp.node), "{}.childKeyingGroups[{}]".format(keyGroupParent, ind))
        return kgrp

def KeyingGroupFootFinder(moduleName, side):
    '''Looks for module attr "footCnx" and returns module Foot_bk_01 controls'''
    root, toeCtl, footCtlLs = [None]*3
    for root in cmds.ls("{}_{}*root".format(moduleName, side), l=True):
        if "rig" in root and cmds.listAttr(root, ud=True): break
    if "footCnx" in cmds.listAttr(root, ud=True) or []:
        foot = cmds.listConnections(root + ".footCnx")
        if foot and cmds.getAttr(foot[0] + ".componentType") == "foot_bk_01":
            toeCtl = Foot.getToeControl(cmds.getAttr(foot[0] + ".componentName"), side, True)
            footCtlLs = Foot.getControlsByFilter(cmds.getAttr(foot[0] + ".componentName"), side, True, toe=False)
    return toeCtl, footCtlLs

def IKFKChainSetUp(moduleName, side, fkControls=None, ikControls=None, poleVectorControl=None, blendControlAttr=None, swivelControlAttr=None, planarAxis="z"):
    '''Creates IKFKChain node to set handle system behaviour
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply
        fkControls(list of strings, optional): three sorted parts fk controls
        ikControls(list of strings, optional): three sorted parts ik controls
        poleVectorControl(string, optional): poleVector control name
        blendControlAttr(string, optional): uiHost.blendFkIkAttribute
        swivelControlAttr(string, optional): rollControl.rotationAxisAvailable,
        planarAxis(string, optional): x,y of z
        
    Returns:
        IKFKChain node created if so'''
    ikfkName = '{}_{}_ikfkChain'.format(moduleName, side)
    if cmds.objExists(ikfkName):
        limb = IKFKChain(ikfkName)
    else:
        limb = IKFKChain()
        limb.create(ikfkName)
        limb.ikPlanarAxis = limb.fkPlanarAxis = {'x':0,'y':1,'z':2,'-x':3,'-y':4,'-z':5}[planarAxis.lower()]
    if fkControls:
        limb.fkLimbA = fkControls[0]
        limb.fkLimbB = fkControls[1]
        limb.fkLimbC = fkControls[2]
        if len(fkControls) == 4:
            limb.fkLimbCuadruped = fkControls[3]
    if ikControls:
        limb.ikLimbA = ikControls[0]
        limb.ikLimbB = ikControls[1]
        limb.ikLimbC = ikControls[2]
    if poleVectorControl:
        limb.ikPoleVector = poleVectorControl
    if blendControlAttr:
        limb.ikFkBlendPlug = blendControlAttr
    if swivelControlAttr:
        limb.ikSwivelPlug = swivelControlAttr
    return limb

def SpaceAutoPoleVector(moduleName, side, spaceAttr='custom'):
    '''Creates auxiliar SingleChain ik solver+chain to add as an choice in IK's SwitchSpace system
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply
        spaceAttr(string, optional): attribute custom choice's name'''
    root = cmds.createNode('transform',n='{}_{}_0_root'.format(moduleName, side),p='setup' if cmds.objExists('setup') else None)
    # auxiliar chain
    auxChain = [root]
    auxIk = '{}Aux_{}_0_iksc'.format(moduleName, side)
    modRoot = [root for root in cmds.ls('{}_{}_root'.format(moduleName, side), l=True) if "rig" in root][0]
    end = '{}_{}_ik_ctl'.format(moduleName, side)
    for num in [0,1]:
        aux = '{}Aux_{}_{}_jnt'.format(moduleName, side, num)
        cmds.delete(cmds.parentConstraint(end if num else modRoot, cmds.createNode('joint', n=aux, p=auxChain[-1])))
        auxChain.append( aux )
    auxChain.remove(root)
    cmds.setAttr(root + ".v", False)
    cmds.setAttr(auxChain[-1] + ".r", 0,0,0)
    cmds.setAttr(auxChain[-1] + ".jo", 0,0,0)
    cmds.parent(cmds.ikHandle(sj=auxChain[0], ee=auxChain[-1], ap=True, sol="ikSCsolver", n=auxIk)[0], root)
    cmds.pointConstraint(modRoot, auxChain[0])
    cmds.pointConstraint(end, auxIk)
    # space attr
    switchControl = '{}UI_{}_ctl'.format(moduleName, side)
    if not cmds.objExists(switchControl):
        switchControl = 'global_C0_ctl'
    switchAttr = '{}_upvref'.format(cmds.getAttr(modRoot + ".componentName"))
    newSpaces = ':'.join( cmds.attributeQuery(switchAttr, n=switchControl, le=True) + [spaceAttr] )
    cmds.addAttr('{}.{}'.format(switchControl, switchAttr), en=newSpaces, e=True)
    # space node
    poleControl = '{}_{}_upv_cns'.format(moduleName, side)
    spaceNode = '{}_{}_{}_space'.format(moduleName, side, spaceAttr)
    cmds.parent(cmds.createNode('transform', n=spaceNode, p=poleControl), auxChain[0])
    switchCns = cmds.parentConstraint(spaceNode, poleControl)[0]
    switchCondition = cmds.createNode('condition')
    cmds.setAttr(switchCondition + ".secondTerm", newSpaces.split(":").index(spaceAttr))
    cmds.setAttr(switchCondition + ".colorIfTrueR", 1)
    cmds.setAttr(switchCondition + ".colorIfFalseR", 0)
    cmds.connectAttr("{}.{}".format(switchControl, switchAttr), switchCondition + ".firstTerm")
    cmds.connectAttr(switchCondition + ".outColorR", "{}.{}".format(switchCns, cmds.parentConstraint(switchCns, wal=True, q=True)[-1]))

def PoleVectorRollControlQuadruped(moduleName, side, rollRotateAxis='x', connectNegative=True):
    '''Creates a control to master the roll behaviour integrated in mGear quadruped module
    
    Args:
        moduleName (string): component name to search and apply
        side (string): component side to search and apply
        rollRptateAxis(string, optional): rotation axis available in control
        connectNegative(bool, optional): will control rotation output multiply by -1?

    Returns:
        Set(Control's Root, Control itself)'''
    # error
    if rollRotateAxis not in "xyz":
        raise
    # curve shape
    ctlShape = ShapeControlEditorWin()
    with open("{}\{}.json".format(ctlShape.__library_path__, 'direction'), 'r') as f:
        ctlCurveDict = json.load(f)
    # node
    root = cmds.createNode('transform', n='{}_{}_rollCustom_ctl_npo'.format(moduleName, side), p=[ctl for ctl in cmds.ls('{}_{}_root'.format(moduleName, side), l=True) if "rig" in ctl][0])
    ctl = cmds.createNode('transform', n='{}_{}_rollCustom_ctl'.format(moduleName, side), p=root)
    ctlShape.__addShapes__(ctl, ctlCurveDict)
    cmds.sets(ctl, e=True, forceElement="rig_controllers_grp")
    ControlBuffer(ctl)
    for at in "trs":
        AttributeLockAndHide(ctl, [at + ax for ax in "xyz"])
    cmds.setAttr("{}.v".format(ctl), k=False)
    cmds.setAttr("{}.r{}".format(ctl, rollRotateAxis), l=False, k=True)
    # position
    cmds.pointConstraint('{}_{}_*UpvRef0_jnt'.format(moduleName, side), '{}_{}_ik_ctl'.format(moduleName, side), root)
    cmds.orientConstraint('{}_{}_*UpvRef0_jnt'.format(moduleName, side), root)
    # connections
    modRoot = [root for root in cmds.ls('{}_{}_root'.format(moduleName, side), l=True) if "rig" in root][0]
    modName = cmds.getAttr(modRoot + ".componentName")
    uiHost = getUIHostControl(moduleName, side)
    mult = cmds.createNode('multDoubleLinear')
    cmds.addAttr(uiHost, ln="custom_{}_roll".format(modName), nn="Roll", proxy='{}.r{}'.format(ctl, rollRotateAxis))
    cmds.connectAttr('{}.{}_blend'.format(uiHost, modName), root + ".v")
    cmds.connectAttr("{}.r{}".format(ctl, rollRotateAxis), mult + ".i1")
    cmds.connectAttr("{}.o".format(mult), '{}.{}_roll'.format(uiHost, modName))
    cmds.setAttr(mult + ".i2", -1 if connectNegative else 1)
    cmds.setAttr('{}.{}_roll'.format(uiHost, modName), k=False)
    return root, ctl
# ################################################################################
    
# ################################################################################
# ----- Common Finish Process
# ################################################################################
def FinishProcess(rigName="rig"):
    # Visibility Options
    pm.setAttr('{}.ctl_vis_on_playback'.format(rigName), 0)
    pm.setAttr('{}.jnt_vis'.format(rigName), 0)
    # Clear Selection
    pm.select(cl=True)
