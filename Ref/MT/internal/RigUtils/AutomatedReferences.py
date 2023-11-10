import pymel.core as pm

def Create2PointDrivenTranslationLocs(pointA, pointB, numIntermediates, sysName=""):
    pointA = pm.PyNode(pointA)
    pointB = pm.PyNode(pointB)
    
    spacing = 1/(numIntermediates + 1)
    if (not sysName):
        sysName = pointA.getName()
    resultTransforms = []
    
    
    for i in range(numIntermediates):
        trs = pm.group(name="{}_{}_loc".format(sysName, i), empty=True)
        cns = pm.pointConstraint(pointA, pointB, trs, mo=False)
        currentSpacing = spacing * (i + 1)
        cns.target[0].targetWeight.connections(plugs=True)[0].set(1 - currentSpacing)
        cns.target[1].targetWeight.connections(plugs=True)[0].set(currentSpacing)
        
        resultTransforms.append(trs)
    
    return resultTransforms

def CreateDistanceFactor(pointA, pointB):
    """Creates the nodes neccesary to obtain a "distance factor" between two nodes. Taking into account the
    distance between them the moment this is created, and the distance at any moment.

    Args:
        pointA (String or PyNode): First node
        pointB (String or PyNode): Second node

    Returns:
        PyNode: multiplyDivide node that calculates te final factor result
    """
    pointA = pm.PyNode(pointA)
    pointB = pm.PyNode(pointB)
    
    # Live distance
    liveDistance = pm.createNode("distanceBetween")
    pointA.worldMatrix[0].connect(liveDistance.inMatrix1)
    pointB.worldMatrix[0].connect(liveDistance.inMatrix2)
    
    # Initial Distance
    initialDistance = pm.createNode("floatConstant")
    initialDistance.inFloat.set(liveDistance.distance.get())
    
    # Calculate Factor
    scaleFactor = pm.createNode("multiplyDivide")
    scaleFactor.operation.set(2)
    liveDistance.distance.connect(scaleFactor.input1X)
    initialDistance.outFloat.connect(scaleFactor.input2X)
    
    return scaleFactor

def CreateScalableRef(pointA, pointB, midPos=True, worldUpObj=None, name="", sclAxis="X", upVAxis="Y", worldUpObjAxis="Y"):
    """Creates a transform node that automates aun "X" axis scalability and positions it according
    to wo given nodes.

    Args:
        pointA (String or PyNode): First node
        pointB (String or PyNode): Second node
        midPos (bool, optional): The reference will be create in the middle position between A and B. Defaults to True.
        worldUpObj (String or PyNode, optional): Node to have its Node Rotation Up. If not given, PointA will be used. Defaults to None.
        name (str, optional): Name for the ref created. Defaults to "pointA_sclLoc".
        sclAxis (String): X, Y or Z Axis for the scalability
        upVAxis (String): X, Y or Z Axis for the Up Vector.
        worldUpObjAxis (String): X, Y or Z Axis for the vector to take from the WorldUpObj node.

    Returns:
        PyNode: Reference Node that has the "X" Scalability, and position between two points.
    """
    pointA = pm.PyNode(pointA)
    pointB = pm.PyNode(pointB)

    sclAxis = sclAxis.upper()
    upVAxis = upVAxis.upper()
    worldUpObjAxis = worldUpObjAxis.upper()
    
    # Create Ref loc
    if (not name):
        name = "{}_sclLoc".format(pointA)
    refLoc = pm.group(name=name, empty=True)
    # Position Ref Loc
    pointTargets = [pointA]
    if midPos:
        pointTargets.append(pointB)
    pm.pointConstraint(pointTargets, refLoc)
    # Orient Ref Loc
    if not worldUpObj:
        worldUpObj = pointA
    else:
        worldUpObj = pm.PyNode(worldUpObj)
    
    # Aim Configuration
    axesDict = {"X": 0,
                "Y": 1,
                "Z": 2}
    inputAxes = [sclAxis, upVAxis, worldUpObjAxis]
    targetVectors = [[0,0,0], [0,0,0], [0,0,0]]
    
    for idx, val in enumerate(inputAxes):
        targetValue = 1
        if ("-" in val):
            targetValue = -1
            val = val[1]
        targetVectors[idx][axesDict[val]] = targetValue

    pm.aimConstraint(pointB, refLoc, worldUpType=2, worldUpObject=worldUpObj, aimVector=targetVectors[0], upVector=targetVectors[1], worldUpVector=targetVectors[2])
    
    # Create and Connect Scale Factor
    connectionPlug = None
    if ("X" in sclAxis):
        connectionPlug = refLoc.scaleX
    elif ("Y" in sclAxis):
        connectionPlug = refLoc.scaleY
    elif ("Z" in sclAxis):
        connectionPlug = refLoc.scaleZ
    
    scaleFactor = CreateDistanceFactor(pointA, pointB)
    scaleFactor.outputX.connect(connectionPlug)
    
    return refLoc

def ResetScalableRefInitValues(sclRef):
    sclRef = pm.PyNode(sclRef)
    factor = sclRef.sx.inputs()[0]
    constant = factor.input2X.inputs()[0]
    constant.inFloat.set(factor.input1X.get())