import maya.cmds as cmds
import pymel.core as pm

import RigUtils.Core as RigCore
import RigUtils.Shapes as RigShapes
import RigUtils.AutomatedReferences as Automation
import RigUtils.Constraints as RigCns

# ----------------------------------------------
# -------------- Basics -------------
# ----------------------------------------------
def CreateChildNode(theNode, suffix, baseName=""):
    """Creates a child node with a suffix and/or a given name, with 0 transforms on its parent.

    Args:
        theNode (String or PyNode): Node wich to create a children.
        suffix (String): Suffix to append to the new created transform
        baseName (str, optional): Base Name for the new creted transform. Defaults to theNode.getName().

    Returns:
        PyNode: Newly created child.
    """
    theNode = pm.PyNode(theNode)
    if (not baseName):
        baseName = theNode.getName()
    theGrp = pm.group(name="{}_{}".format(baseName, suffix), empty=True)
    theGrp.setParent(theNode)
    theGrp.translate.set([0,0,0])
    theGrp.rotate.set([0,0,0])
    
    return theGrp

def CreateHalfRot(nodeA, nodeB, parent, baseName="", sameInitOrient=True):
    nodeA = pm.PyNode(nodeA)
    nodeB = pm.PyNode(nodeB)
    parent = pm.PyNode(parent)
    
    if not baseName:
        baseName = "{}_{}".format(nodeA.getName(), nodeB.getName())
    
    refA = pm.group(empty=True, name="{}_rotRef".format(nodeA), parent=nodeA)
    refB = pm.group(empty=True, name="{}_rotRef".format(nodeB), parent=nodeB)
    pm.matchTransform(refA, nodeA)
    if (sameInitOrient):
        pm.matchTransform(refB, nodeA)
    else:
        pm.matchTransform(refB, nodeB)
    
    halfRot = pm.group(empty=True, name="{}_halfRot".format(baseName), parent=parent)
    pm.matchTransform(halfRot, parent)
    pm.orientConstraint([refA, refB], halfRot)
    
    return halfRot

# ----------------------------------------------
# --------------- Beziers/Splines --------------
# ----------------------------------------------
def CreateBezierWithControls(numPoints, spacing=10, sysName="bezierSys", useMatrices=True, useDiamonds=False, mirrorTangents=False):
    sysRoot = cmds.group(name="{}_sysGral".format(sysName), empty=True)
    if (useMatrices):
        sysSetup = cmds.group(name="{}_setup".format(sysName), empty=True)
    
    # Create "main" Controls and locator drivers
    mainCtls = []
    mainLocs = []
    for p in list(range(numPoints)):
        ctlSize = spacing/7
        if useDiamonds:
            ctl = RigShapes.CreateDiamond(ctlSize)
            ctl = cmds.rename(ctl, "{}_{}_ctl".format(sysName, p))
        else:
            ctl = RigShapes.CreateBall("{}_{}_ctl".format(sysName, p), ctlSize)
        RigShapes.SetCtlColor(ctl, rgbColor=[0.9,0.3,0.0])
        cmds.xform(ctl, translation = [p*spacing, 0, 0])
        ctl = cmds.parent(ctl, sysRoot)[0]
        ctl = RigCore.CreateGrpZero(ctl)
        
        loc = cmds.spaceLocator(name="{}_{}_driver".format(sysName, p))[0]
        if (useMatrices):
            RigCore.ConstraintByMatrix([loc], ctl, t=True)
            loc = cmds.parent(loc, sysSetup)[0]
        else:
            cmds.matchTransform(loc, ctl)
            loc = cmds.parent(loc, ctl)[0]
        cmds.hide(loc)
        
        mainCtls.append(ctl)
        mainLocs.append(loc)
    
    # Create Tangent Controls
    bezierCtls = [None] #This None is added in order to easily merge all controls later
    bezierLocs = [None]
    tanNames = ['In', 'Out']
    for mainCtl in mainCtls:
        ctlNameParts = mainCtl.split('|')[-1].split('_')
        ctlPos = cmds.xform(mainCtl, q=True, translation=True, ws=True)
        ctlSize = spacing/12
        
        for i in list(range(2)):
            ctlNameParts[-1] = "tan{}".format(tanNames[i])
            bezierCtl = RigShapes.CreateBall("{}_ctl".format("_".join(ctlNameParts)), ctlSize)
            RigShapes.SetCtlColor(bezierCtl, indexColor=17)
            
            localSpacing = spacing/3
            pos = ctlPos[0] - (localSpacing) + (i*localSpacing*2)
            cmds.xform(bezierCtl, translation = [pos, 0, 0])
            bezierCtl = cmds.parent(bezierCtl, mainCtl)[0]
            
            loc = cmds.spaceLocator(name="{}_driver".format("_".join(ctlNameParts)))[0]
            if (useMatrices):
                RigCore.ConstraintByMatrix([loc], bezierCtl, t=True)
                loc = cmds.parent(loc, sysSetup)[0]
            else:
                cmds.matchTransform(loc, bezierCtl)
                loc = cmds.parent(loc, bezierCtl)[0]
            cmds.hide(loc)

            if (mirrorTangents and (i == 0)):
                mirrorGrp = cmds.group(empty=True, parent=mainCtl, name="{}_mirrGrp".format("_".join(ctlNameParts)))
                bezierCtl = cmds.parent(bezierCtl, mirrorGrp)[0]
                cmds.setAttr("{}.tx".format(bezierCtl), -cmds.getAttr("{}.tx".format(bezierCtl)))
                cmds.setAttr("{}.sx".format(mirrorGrp), -1)
            
            
            bezierCtls.append(bezierCtl)
            bezierLocs.append(loc)
            
            #Lock Attribs
            for attr in ['r', 's']:    
                for ax in ['x', 'y', 'z']:
                    cmds.setAttr("{}.{}{}".format(bezierCtl, attr, ax), lock=True)
    
    # sort Ctls and ignore first and last tangents (as they don't exist in the bezier)
    nodesToDelete = [bezierCtls[-1], bezierLocs[1], bezierLocs[-1]]
    if (mirrorTangents):
        nodesToDelete.append(cmds.listRelatives(bezierCtls[1], parent=True)[0])
    else:
        nodesToDelete.append(bezierCtls[1])
    cmds.delete(nodesToDelete)
    allLocs = []
    nPos = 3
    temp_iter = iter(bezierLocs)
    for n in mainLocs:
        allLocs.extend([next(temp_iter) for _ in range(nPos - 1)])
        allLocs.append(n)
    allLocs = allLocs[2:]
    
    # Create Bezier
    theBezCurve = RigCore.CreateBezier(numPoints, spacing=spacing)
    theBezCurve = cmds.parent(theBezCurve, sysRoot)[0]
    
    # Assign Drivers to curve points
    curveShape = cmds.listRelatives(theBezCurve, shapes=True, fullPath=True)[0]
    for i in list(range(len(allLocs))):
        theLocShape = cmds.listRelatives(allLocs[i], shapes=True, fullPath=True)[0]
        cmds.connectAttr("{}.worldPosition[0]".format(theLocShape, i), "{}.controlPoints[{}]".format(curveShape, i))
    
    # Reparent last things and Offset curve parent so we don't hac double transforms
    if (useMatrices):
        cmds.connectAttr("{}.worldInverseMatrix[0]".format(sysSetup), "{}.offsetParentMatrix".format(theBezCurve))
        cmds.parent(theBezCurve, sysSetup)
        cmds.parent(sysSetup, sysRoot)
    else:
        cmds.connectAttr("{}.worldInverseMatrix[0]".format(sysRoot), "{}.offsetParentMatrix".format(theBezCurve))
    
    # Lock Attributes
    for attr in ['t', 'r', 's']:    
        for ax in ['x', 'y', 'z']:
            cmds.setAttr("{}.{}{}".format(theBezCurve, attr, ax), lock=True)
    
    for attr in ['r', 's']:    
        for ax in ['x', 'y', 'z']:
            cmds.setAttr("{}.{}{}".format(theBezCurve, attr, ax), lock=True)
    
    # Rename the curve
    theBezCurve = cmds.rename(theBezCurve, "{}_bezier".format(sysName))
    
    # Sort Ctls for returning
    sortedCtls = []
    temp_iter = iter(bezierCtls)
    for n in mainCtls:
        sortedCtls.extend([next(temp_iter) for _ in range(nPos - 1)])
        sortedCtls.append(n)
    sortedCtls = sortedCtls[2:]
    
    # Select root
    cmds.select(sysRoot)
    
    # Return Ctls
    return sortedCtls

def CreateRetractableChainOnBezier(curve, numJoints, name=None, upVectors=[], locator=False, constantVelocity=True, radius=3):
    if (numJoints > 0):
        nameBase = "{}_{}_joint".format((name or curve), "{}")
        
        drivers, mPaths = RigCore.CreateSplineDrivenPoints(curve, numJoints, name=name or curve, locator=False, aim=True, upVectors=upVectors, constraintUValue=True)
        joints = []
        
        for i in range(numJoints):
            cmds.select(None)
            theJoint = cmds.joint(name=nameBase.format(i), radius=radius)
            cmds.setAttr('{}.segmentScaleCompensate'.format(theJoint), 0)
            #transMatrix = pm.xform(drivers[i], q=True, matrix=True, ws=True)
            #cmds.xform(theJoint, matrix=transMatrix, ws=True)
            RigCore.ConstraintByMatrix([theJoint], drivers[i], t=True, r=True)
            joints.append(theJoint)
            
            #The end bone has no scale
            if (i < numJoints-1):
                #Create refDistance
                distNode = cmds.createNode("distanceBetween", name=theJoint+"_distance")
                cmds.connectAttr("{}.worldMatrix[0]".format(drivers[i]), "{}.inMatrix1".format(distNode))
                cmds.connectAttr("{}.worldMatrix[0]".format(drivers[i+1]), "{}.inMatrix2".format(distNode))
                
                #Create InitLength
                initLenNode = cmds.createNode("floatConstant", name=theJoint+"_initLength")
                dist = cmds.getAttr("{}.distance".format(distNode))
                cmds.setAttr("{}.inFloat".format(initLenNode), dist)
                
                #Create MultDiv
                scaleResultNode = cmds.createNode("multiplyDivide", name=theJoint+"_sclResult")
                cmds.setAttr("{}.operation".format(scaleResultNode), 2)
                cmds.connectAttr("{}.distance".format(distNode), "{}.input1X".format(scaleResultNode))
                cmds.connectAttr("{}.outFloat".format(initLenNode), "{}.input2X".format(scaleResultNode))
                
                #Connect Scale
                cmds.connectAttr("{}.outputX".format(scaleResultNode), "{}.scaleX".format(theJoint))
        
        return joints, drivers, mPaths

def CreatePointsOnPath(spline, arraySubDivs, name="pathPoint"):
    resultPoints = []
    resultmPaths = []
    
    numSections = len(arraySubDivs)
    sectionLength = 1 / numSections
    for sectionNumber in range(numSections):
        numSubdivs = arraySubDivs[sectionNumber]
        subdivLength = sectionLength / numSubdivs
        
        initPos = sectionNumber * sectionLength
        for subdivNumber in range(numSubdivs):
            currentPos = initPos + (subdivNumber * subdivLength)
            
            point, mPath = RigCore.CreatePointOnCurve(spline, name, uVal=currentPos, locator=True)
            resultPoints.append(point)
            resultmPaths.append(mPath)
    
    # create last point:
    point, mPath = RigCore.CreatePointOnCurve(spline, name, uVal=1, locator=True)
    resultPoints.append(point)
    resultmPaths.append(mPath)
    
    return resultPoints, resultmPaths

def CreateBlendMatrixRotationsToControls(arrayPoints, arrayControls, distribution):
    numSections = len(distribution)
    currentPointIndex = 0
    
    for sectionNumber in range(numSections):
        refA = arrayControls[sectionNumber]
        refB = arrayControls[sectionNumber + 1]

        numSubdivs = distribution[sectionNumber]
        subdivFactor = 1 / numSubdivs
        for subdivNumber in range(numSubdivs):
            factorB = subdivFactor * subdivNumber
            RigCns.CreateBlendMatrixOri(refA, refB, arrayPoints[currentPointIndex], factorB)
            currentPointIndex += 1
        
    # Last point:
    RigCns.CreateBlendMatrixOri(refA, refB, arrayPoints[currentPointIndex])
# ----------------------------------------------
# ------------------ Scalables -----------------
# ----------------------------------------------
def CreateSimpleMembrane(pointA, pointB, sysName="membrane", centerCtl=None):
    pointA = pm.PyNode(pointA)
    pointB = pm.PyNode(pointB)
    midName = "midPoint"
    if (not centerCtl):
        midPoint = pm.group(name="{}_{}_loc".format(sysName, midName), empty=True)
        pm.pointConstraint([pointA, pointB], midPoint)
        pm.aimConstraint(pointB, midPoint, worldUpType=2, worldUpObject=pointA)
        ctlZero = CreateChildNode(midPoint, "ctlZero", baseName="{}_{}".format(sysName, midName))
        centerCtl = CreateChildNode(ctlZero, "ctl", baseName="{}_{}".format(sysName, midName))
        centerCtl.visibility.setKeyable(False)
        for transf in ["r", "s"]:
            for axis in ["x", "y", "z"]:
                attr = getattr(centerCtl, "{}{}".format(transf, axis))
                attr.setKeyable(False)
                attr.lock(True)
    else:
        centerCtl = pm.PyNode(centerCtl)
    sclA = Automation.CreateScalableRef(pointA, centerCtl, name="{}_sclA_loc".format(sysName))
    sclB = Automation.CreateScalableRef(pointB, centerCtl, name="{}_sclB_loc".format(sysName))
    
    return [sclA, sclB, centerCtl]

# ----------------------------------------------
# -------------- Additive Controls -------------
# ----------------------------------------------
def CreateAdditiveControls(ctlsList, length, size, axis):
    result = []
    for ctlBase in ctlsList:
        ctlName = "{}_ctl".format(ctlBase)
        ctl = pm.PyNode(ctlName)
        additiveCtl = pm.PyNode(RigShapes.CreatePin("{}_additive_ctl".format(ctlBase), length=length, size=size, axis=axis))
        RigShapes.SetCtlColor(additiveCtl.getName(), indexColor=ctl.getShape().overrideColor.get())
        additiveCtl.setParent(ctl)
        pm.matchTransform(additiveCtl, ctl)
        additiveRef = pm.group(name="{}_0_additive_ref".format(ctlBase), empty=True)
        additiveRef.setParent(additiveCtl)
        pm.matchTransform(additiveRef, additiveCtl)
        result.append(additiveCtl)
    return result