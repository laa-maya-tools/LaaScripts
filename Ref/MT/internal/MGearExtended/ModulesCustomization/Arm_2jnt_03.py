import pymel.core as pm

import MGearExtended.ModulesCustomization as  cMod
import MGearExtended.PostProUtils as PostP

# ######################################## Commodities
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

def GetRollSplineKineNode(transformedNode):
    transformedNode = pm.PyNode(transformedNode)
    
    conns = transformedNode.parentMatrix[0].connections(type="mgear_rollSplineKine")
    if conns:
        return conns[0]
    else:
        return None

def GetMatrixConstrainedNode(driverNode):
    driverNode = pm.PyNode(driverNode)
    conns = driverNode.worldMatrix[0].connections(type="mgear_matrixConstraint")
    print(conns)
    if conns:
        drivenConns = conns[0].drivenParentInverseMatrix.connections()
        print(drivenConns)
        if drivenConns:
            return drivenConns[0]
        return None
    else:
        return None
# ############################################################




def OrientHandToGuide(moduleName):    
    # #######################################################Logic
    # Gather data
    fkNpo = pm.PyNode("{}_fk2_npo".format(moduleName)) # This will be aligned to the wrist guide
    wristGuide = pm.PyNode("{}_wrist".format(moduleName))
    
    ikCtl = pm.PyNode("{}_ik_ctl".format(moduleName)) #This will be aligned to the ikMth AFTER th FK npo is aligned
    ikMth = pm.PyNode("{}_ik_mth".format(moduleName))
    
    #fkCtl = pm.PyNode("{}_fk2_ctl".format(moduleName)) # this is currently not needed.
    effLoc = pm.PyNode("{}_eff_loc".format(moduleName)) #Children of this will need to be unparented
    
    # Possible Roll:
    # ## If there is a Roll child, we must regenerate the constraint on '{rollModule}_fk_ref' after the fixing is done
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
    #########################################################
    
    # Unparenting:
    effLocChildren = effLoc.getChildren()
    ikChildren = [x for x in ikCtl.getChildren(type="transform") if ("_ref" not in x.getName())]
    tempParent = pm.group(empty=True, name="TempAuxParent")
    nodeAttribsLocked = []
    for c in effLocChildren + ikChildren:
        attribsLocked = PostP.GetLockedTransforms(c)
        if attribsLocked:
            nodeAttribsLocked.append([c, attribsLocked])
            PostP.SetTransformsLocked(c, False)
        c.setParent(tempParent)
    
    # Orient FK:
    PostP.SetTransformsLocked(fkNpo, False, rotation=True)
    #PostP.SetAttribLocked([fkNpo.rx, fkNpo.ry, fkNpo.rz], False)
    pm.matchTransform(fkNpo, wristGuide, rotation=True, position=True)
    PostP.SetTransformsLocked(fkNpo, True, rotation=True)
    #PostP.SetAttribLocked([fkNpo.rx, fkNpo.ry, fkNpo.rz], True)
    
    # Orient IK (Always after orienting FK, as ikMth would not be correctly orient4ed otherwise):
    pm.matchTransform(ikCtl, ikMth, rotation=True, position=True)
    
    #Reparenting
    lockedNodes = [x[0] for x in nodeAttribsLocked]
    for c in effLocChildren:
        c.setParent(effLoc)
        if c in lockedNodes:
            idx = lockedNodes.index(c)
            PostP.SetAttribLocked(nodeAttribsLocked[idx][1], True)
    for c in ikChildren:
        c.setParent(ikCtl)
        if c in lockedNodes:
            idx = lockedNodes.index(c)
            PostP.SetAttribLocked(nodeAttribsLocked[idx][1], True)
    
    # ## If the arm has a 'footRoll' child we need to align these two
    if (childRollRoot):
        ikRef = pm.PyNode("{}_ik_ref".format(moduleName))
        fkRef = pm.PyNode("{}_fk_ref".format(moduleName))
        pm.matchTransform(ikRef, fkRef)
    
        pm.parentConstraint(parentCnsTarget, rollFkRef, mo=True)
    #########################################################
    
    fkMth = pm.PyNode("{}_fk2_mth".format(moduleName))
    #ikMth = pm.PyNode("{}_ik_mth".format(moduleName))
    pm.matchTransform(fkMth, fkNpo)
    #pm.matchTransform(ikMth, ikCtl)
    
    pm.delete(tempParent)

def SetRollSplineUValues(moduleName):
    """Sets and creates well aligned twist transforms for a 3+1+3 twists arm:
    3 twist for upperarm
    1 elbow rotation
    3 twist for forearm

    Args:
        moduleName (String): Module Name. Ex: "arm_L0"
    """
    uVals = [0, 0.25,0.5, 0.5, 0.5, 0.75, 0.999]
    isRightSide = cMod.IsRightSideModule(moduleName)
    
    for idx in range(7):
        uVal = uVals[idx]
        aimVectorX = -1
        if (isRightSide):
            uVal = uVals[len(uVals) - 1 - idx]
            aimVectorX = -1
        
        currentLoc = pm.PyNode("{}_div{}_loc".format(moduleName, idx))
        kineNode = GetRollSplineKineNode(currentLoc)
        if (kineNode):
                kineNode.u.set(uVal)
        
        # Third twist of upper arm and first twist of forearm.
        # They are in uValue 0.5 in order to be well aligned in position.
        # Se use an aim constraint (to their previous/next) using the elbow up, in order to have their orientation
        if (idx==2 or idx==4):
            prevLoc = pm.PyNode("{}_div{}_loc".format(moduleName, idx-1))
            nextLoc = pm.PyNode("{}_div{}_loc".format(moduleName, idx+1))
            currentLoc.rotate.disconnect()
            if (idx==2):
                pm.aimConstraint(prevLoc, currentLoc, aimVector=[aimVectorX,0,0], worldUpType="objectrotation", worldUpObject=nextLoc, upVector=[0,0,1], worldUpVector=[0,0,1])
            else:
                pm.aimConstraint(nextLoc, currentLoc, aimVector=[-aimVectorX,0,0], worldUpType="objectrotation", worldUpObject=prevLoc, upVector=[0,0,1], worldUpVector=[0,0,1])
        
        #Third twist of forearm (align to "wrist")
        if (idx==6):
            effLoc = pm.PyNode("{}_eff_loc".format(moduleName))
            pm.pointConstraint(effLoc, currentLoc)

def CreateArmMainRefs(moduleName):
    upperArmMainLoc = pm.group(name="{}_upperArm_main_ref".format(moduleName), empty=True)
    #shoulderTwistRef = pm.PyNode("{}_div0_loc".format(moduleName))
    shoulderTwistRef = GetMatrixConstrainedNode("{}_div0_loc".format(moduleName))
    #elbowTwistRef1 = pm.PyNode("{}_div2_loc".format(moduleName))
    elbowTwistRef1 = GetMatrixConstrainedNode("{}_div2_loc".format(moduleName))
    upperArmMainLoc.setParent(shoulderTwistRef)
    upperArmMainLoc.translate.set([0,0,0])
    pm.orientConstraint(elbowTwistRef1, upperArmMainLoc)
    
    foreArmMainLoc = pm.group(name="{}_foreArm_main_ref".format(moduleName), empty=True)
    #elbowTwistRef2 = pm.PyNode("{}_div4_loc".format(moduleName))
    elbowTwistRef2 = GetMatrixConstrainedNode("{}_div4_loc".format(moduleName))
    foreArmMainLoc.setParent(elbowTwistRef2)
    foreArmMainLoc.translate.set([0,0,0])
    foreArmMainLoc.rotate.set([0,0,0])
    
    result = [upperArmMainLoc, foreArmMainLoc]
    pm.select(result)
    
    return result