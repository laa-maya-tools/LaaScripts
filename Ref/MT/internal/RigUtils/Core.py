import pymel.core as pm
import maya.cmds as cmds

# --------------------------------------------
# -------------- Attributes ------------------
# --------------------------------------------
def listAttrProxies(node):
    '''List userDefined attributes, which set state is on and have an input connection

    Args:
        node (string): nodeName

    Returns: proxy attributes'''
    result = []
    for at in cmds.listAttr(node, s=True, ud=True, k=True) or []:
        if cmds.listConnections("{}.{}".format(node, at), d=False):
            result.append(at)
    return result

def smartSetAttr(nodeAttr, *value, **kwargs):
    '''Try to set the value input if attribute is not connected. Overrides lock state.
    Value input can be whatever type in [list,set,tuple,numeric,string].
    Also allows set other cmds.setAttr arguments

    Args:
        nodeAttr (string): nodeName.attributeName
        *value (whatever, optional): method interpretates input type to set
        **kwargs (dictionary, optional): any flag from cmds.setAttr

    Returns: None'''
    if cmds.listConnections(nodeAttr, d=False, p=True) or []:
        return
    if not value:
        cmds.setAttr(nodeAttr, **kwargs)
        return
    oldValue = cmds.getAttr(nodeAttr)
    if type(oldValue) in [tuple,set,list]:
        oldValue = oldValue[0]
    else:
        oldValue = [oldValue]
    if len(value) == 1:
        value = value[0]
    if type(value) not in [list,set,tuple]:
        value = [value]
    atType = cmds.getAttr(nodeAttr, type=True)
    nodeName, dot, atName = nodeAttr.partition(".")
    atChilds = cmds.attributeQuery(atName, n=nodeName, lc=True)
    if atChilds or atType in ['matrix','string']:
        kwargs["type"] = atType
    if len(value) != len(oldValue):
        cmds.warning("Attribute '´{}' type '{}' does not accept value input '{}'".format(atName, atType, value))
        return
    if atChilds:
        for atC,atVal in zip(atChilds,value):
            smartSetAttr('{}.{}'.format(nodeName, atC.split(".")[-1]), atVal)
        return
    if "l" in kwargs.keys():
        kwargs["lock"] = kwargs["l"]
        kwargs.pop("l")
    else:
        if "lock" not in kwargs.keys():
            kwargs["lock"] = cmds.getAttr(nodeAttr, l=True)
    cmds.setAttr(nodeAttr, l=False)
    cmds.setAttr(nodeAttr, *value, **kwargs)

def GetOrientConstraintWeightAttrib(cns, index):
    return cns.target[index].targetWeight.inputs(p=True)[0]

# --------------------------------------------
# --------------- Grouping -------------------
# --------------------------------------------
def CreateGrpZero(node):
    nodeMat = cmds.xform(node, q=True, matrix=True, ws=True)
    nodeParent = cmds.listRelatives(node, parent=True, fullPath=True)
    
    objShortName = node.split('|')[-1]
    zeroGrp = cmds.group(name="{}Zero".format(objShortName), empty=True)

    cmds.xform(zeroGrp, matrix=nodeMat, ws=True)
    if (nodeParent):
        zeroGrp = cmds.parent(zeroGrp, nodeParent)
    result = cmds.parent(node, zeroGrp)[0]
    return result

# --------------------------------------------
# --------- Constraints operations -----------
# --------------------------------------------
def OptimizedConstraint(master, slave, cType='parent', auxiliar=False):
        sel = cmds.ls(sl=True)
        if type(master) != list:
            master = [master]
        cmds.namespace(set=":")
        if slave.rpartition(":")[0]:
            cmds.namespace(set=slave.rpartition(":")[0])
        cns = cmds.createNode('{}Constraint'.format(cType), p=slave, n="{}Optimized_{}".format(slave, '{}Cns'.format(cType)))
        for ind, mst in enumerate(master):
            if auxiliar:
                cmst = cmds.duplicate(slave, po=True, n=slave + "_mstCns")[0]
                cmds.parent(cmst, mst)
                mst = cmst
            cmds.connectAttr(mst + '.wm[0]', '{}.target[{}].targetParentMatrix'.format(cns, ind))
        cmds.connectAttr(slave + '.pim[0]', cns + '.cpim')
        if cType in ['parent','point']:
            cmds.connectAttr(cns + '.constraintTranslateX', slave + '.tx')
            cmds.connectAttr(cns + '.constraintTranslateY', slave + '.ty')
            cmds.connectAttr(cns + '.constraintTranslateZ', slave + '.tz')
        if cType in ['parent','orient']:
            cmds.connectAttr(cns + '.constraintRotateX', slave + '.rx')
            cmds.connectAttr(cns + '.constraintRotateY', slave + '.ry')
            cmds.connectAttr(cns + '.constraintRotateZ', slave + '.rz')
        if cType == 'scale':
            cmds.connectAttr(cns + '.constraintScaleX', slave + '.rx')
            cmds.connectAttr(cns + '.constraintScaleY', slave + '.ry')
            cmds.connectAttr(cns + '.constraintScaleZ', slave + '.rz')
        cmds.select(sel)
        cmds.namespace(set=":")
        return cns

def ConstraintByMatrix(objects, target, t=False, r=False, s=False):
    if (t or r or s):
        for object in objects:
            objShortName = object.split('|')[-1]
            multMatNode = cmds.createNode("multMatrix", name="{}_matrixCntResult".format(objShortName))
            cmds.connectAttr("{}.worldMatrix[0]".format(target), "{}.matrixIn[0]".format(multMatNode))
            cmds.connectAttr("{}.parentInverseMatrix[0]".format(object), "{}.matrixIn[1]".format(multMatNode))
            decompNode = cmds.createNode("decomposeMatrix", name="{}_matrixCntDecomp".format(objShortName))
            cmds.connectAttr("{}.matrixSum".format(multMatNode), "{}.inputMatrix".format(decompNode))
            if (t):
                cmds.connectAttr("{}.outputTranslate".format(decompNode), "{}.translate".format(object))
            if (r):
                cmds.connectAttr("{}.outputRotate".format(decompNode), "{}.rotate".format(object))
            if (s):
                cmds.connectAttr("{}.outputScale".format(decompNode), "{}.scale".format(object))

def DeleteConstraints(node, recursive=False, type=None, excludeNodes=[]):
    if (type):
        _constraintTypes = type
    else:
        _constraintTypes = ['orientConstraint', 'pointConstraint', 'scaleConstraint', 'parentConstraint']
    
    if (node not in excludeNodes):
        # Get node constraints
        cnts = cmds.listRelatives(node, type=_constraintTypes, fullPath=True)
        
        # Delete node constraints
        if (cnts):
            cmds.delete(cnts)
    else:
        print("{} excluded from deleting constraints.".format(node))
    
    # Recursively deletion
    if (recursive):
        children = cmds.listRelatives(node, type=['transform']) or []
        for child in children:
            DeleteConstraints(child, True, _constraintTypes, excludeNodes)

def ConstraintAll(master, slave):
    pm.pointConstraint(master, slave)
    pm.orientConstraint(master, slave)
    pm.scaleConstraint(master, slave)

# --------------------------------------------
# ------------ Bezier Creation ---------------
# --------------------------------------------
def CreateBezier(numPoints, spacing=10):
    if (numPoints >= 2):
        prevSelection = cmds.ls(sl=True)
        listPositions = []
        for p in list(range(numPoints)):
            listPositions.append((p*spacing,0,0))
        theCurve = cmds.curve(d=1, p=listPositions)
        # I hate Maya commands sometimes. I fricking can't call 'nurbsCurveToBezier' with the curve name...
        cmds.select(theCurve)
        cmds.nurbsCurveToBezier()
        cmds.select(prevSelection)
        return theCurve
    else:
        return None

# --------------------------------------------
# ------------ points on Curves ---------------
# --------------------------------------------
def CreatePointOnCurve(curve, name, uVal=0, locator=False, constantVelocity=True):
    if (locator):
        p = pm.spaceLocator(name=name)
    else:
        p = pm.group(name=name, empty=True)
    
    mPath = pm.pathAnimation(p, curve, name="{}_mPath".format(name))
    mPath = pm.PyNode(mPath)
    
    mPath.fractionMode.set(constantVelocity)
    pm.delete(mPath.uValue.inputs()) # Delete Keys
    mPath.uValue.set(uVal)
    
    return p, mPath

def CreateSplineDrivenPoints(curve, num, name=None, aim=False, upVectors=[], locator=False, constantVelocity=True, constraintUValue=False):
    """
    Creates points driven by a curve based on motion Paths
    Parameters:
        - curve: The nurbs or bezier curve that will act as master
        - num: The number of points that will be created over the curve
        - name: Base name for the new created points. If not set, it will take the name of the curve by default.
        - aim: If True, the new created points will always be aiming the next point. If False, they will be world oriented.
        - upVectors: Array for the upvectors when 'aim' is True. This array can have less or equal length than the number of points created. If it is shorter, the las upVector will be used for all the remaining points.
        - locator: if True, the points will be created with a locator shape. If False, the points will only be a transform node
        - constantVelocity: Sets the 'fractionMode' of the motion paths
        - constraintUValue: If True, the 'uValue' of the motion path of the last point will drive the 'uValue' of the rest of the points, acting as a 'retracting along the curve' control. If False, every motion path will have its own 'uValue' separated.
    """
    if (num > 0):
        nameBase = "{}_{}_drv".format((name or curve), "{}")
        resultPoints = []
        resultmPaths = []
        p, mPath = CreatePointOnCurve(curve, nameBase.format(0), 0, locator, constantVelocity)
        resultPoints.append(p)
        resultmPaths.append(mPath)
        spacing = 1 / (num-1)
        for i in range(1,num):
            uValue = spacing*i
            p, mPath = CreatePointOnCurve(curve, nameBase.format(i), uValue, locator, constantVelocity)
            resultPoints.append(p)
            resultmPaths.append(mPath)
            
            #Aim constraints if desired
            if (aim):
                target = p
                origin = resultPoints[i-1]
                
                if (upVectors):
                    if (i >= len(upVectors)):
                        thisUpVector = upVectors[-1]
                    else:
                        thisUpVector = upVectors[i-1]
                    oriCns = pm.aimConstraint(target, origin, worldUpType=2, worldUpObject=thisUpVector)
                else:
                    oriCns = pm.aimConstraint(target, origin)
                
                if (i == num-1):
                    pm.orientConstraint(origin, target)
        
        if (constraintUValue):
            for i in range(num-2,0,-1):
                ctrlr = pm.createNode('multiplyDivide', n='multDiv_{}'.format(resultPoints[i]))
                resultmPaths[num-1].uValue.connect(ctrlr.input1X)
                ctrlr.input2X.set(spacing*i)
                ctrlr.outputX.connect(resultmPaths[i].uValue)
        
        return resultPoints, resultmPaths

# --------------------------------------------
# -------------------- DCs -------------------
# --------------------------------------------
def CreateDCs(DCsList, ctlParent, exportParent, usePointLocator=False, size=20, constraint=True):
    result = []
    for DCName in DCsList:
        existingMatches = pm.ls("{}*ctl".format(DCName))
        if (len(existingMatches) == 0):
            # Create Ctl (with root and auto groups)
            rootGroup   = pm.group(empty=True, name="{}_root".format(DCName))
            autoGroup   = pm.group(empty=True, name="{}_auto".format(DCName))
            
            if (usePointLocator):
                ctlShape = pm.createNode("PointLocator", name="{}_ctlShape".format(DCName))
                ctlShape.size.set(size)
                ctlShape.axes.set(True)
            else:
                ctlShape = pm.createNode("renderBox", name="{}_ctlShape".format(DCName))
                ctlShape.sizeX.set(size)
                ctlShape.sizeY.set(size)
                ctlShape.sizeZ.set(size)
            ctlNode = ctlShape.getParent()
            ctlNode.setName("{}_ctl".format(DCName))
            
            ctlNode.setParent(autoGroup)
            autoGroup.setParent(rootGroup)
            rootGroup.setParent(ctlParent)
            
            # create export node if not exists, else use the existing DC
            existingMatches = pm.ls(DCName)
            if (len(existingMatches) == 0):
                
                exportLocator = pm.createNode("locator", name="{}Shape".format(DCName))
                exportNode = exportLocator.getParent()
                exportNode.setName(DCName)
                exportNode.setParent(exportParent)
            else:
                exportNode = existingMatches[0]
                #delete possible existing Constraints
                pm.delete(pm.listRelatives(exportNode, type=['orientConstraint', 'pointConstraint', 'scaleConstraint', 'parentConstraint']))
            if (constraint):
                pm.pointConstraint(ctlNode, exportNode)
                pm.orientConstraint(ctlNode, exportNode)
            
            result.append(autoGroup)
        else:
            pm.warning("{} ctl already exists. Nothing will be done".format(DCName))
        
    return result

def ConstraintDCAutos(dcAutoNodes, targetNodes):
    if (len(dcAutoNodes) == len(targetNodes)):
        for i in range(len(dcAutoNodes)):
            #pm.xform(dcAutoNodes[i], ws=True, matrix=(pm.xform(targetNodes[i], q=True, ws=True, matrix=True)))
            pm.parentConstraint(targetNodes[i], dcAutoNodes[i])