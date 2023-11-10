import pymel.core as pm
import maya.cmds  as cmds

# #################################################################################
# ################################## Creation #####################################
# #################################################################################
def OffsetCurvePoints(points, axis, value):
    updateIdx = -1
    if (axis == "X"):
        updateIdx = 0
    elif (axis == "Y"):
        updateIdx = 1
    elif (axis == "Z"):
        updateIdx = 2
    else:
        print("Invalid Axis")
        return
    
    result = []
    for point in points:
        point[updateIdx] += value
        result.append(point)
    
    return result

def CreateCircle(axis='X', size=1, offsetAxis=None, offsetValue=0):
    points = [[1,0], [0,1], [-1,0], [0,-1]]
    
    insertPos = -1
    if (axis=='X'):
        insertPos = 0
    elif (axis=='Y'):
        insertPos = 1
    elif (axis=='Z'):
        insertPos = 2
    
    cvs = []
    d3Points = []
    for p in points:
        p.insert(insertPos, 0)
        d3Points.append([p[0]*size, p[1]*size, p[2]*size])
    
    if (offsetAxis):
        d3Points = OffsetCurvePoints(d3Points, offsetAxis, offsetValue)
    
    cvs = d3Points
    
    # Repeat 3 firtst point at the end because yes
    cvs = cvs + cvs[0:3]
    theCurve = cmds.curve(per=True, p=cvs, k=list(range(9)))
    return theCurve

def CreateDiamond(size=1, offsetAxis=None, offsetValue=0):
    p = size/2
    points = [[0,p,0], [0,0,p], [0,-p,0], [0,0,-p], [0,p,0], [p,0,0], [0,-p,0], [-p,0,0], [0,p,0], [0,0,p], [-p,0,0], [0,0,-p], [p,0,0], [0,0,p]]
    if (offsetAxis):
        points = OffsetCurvePoints(points, offsetAxis, offsetValue)
    theCurve = cmds.curve(d=1, p=points)
    return theCurve

def CreatePin(name="pin", axis="X", size=1, length=1):
    """Creates a 'pin' shaped Control, in the direction of Axis, with the given length and given size for the 'diamon'.

    Args:
        name (str, optional): Name of the Control. Defaults to "pin".
        axis (str, optional): Direction where the pin is going to be. Defaults to "X".
        size (int, optional): Size of the diamond. Defaults to 1.
        length (int, optional): Length from the Control Zero to the end. Defaults to 1.

    Returns:
        _type_: _description_
    """
    diamondPoints = [[0,1,0], [0,0,1], [0,-1,0], [0,0,-1], [0,1,0], [1,0,0], [0,-1,0], [-1,0,0], [0,1,0], [0,0,1], [-1,0,0], [0,0,-1], [1,0,0], [0,0,1]]
    linePoints = [[0,0,0], [0,0,0]]
    
    idxPos = -1
    if (axis=='X'):
        idxPos = 0
    elif (axis=='Y'):
        idxPos = 1
    elif (axis=='Z'):
        idxPos = 2
    
    linePoints[1][idxPos] = length
    
    cvs = linePoints
    for p in diamondPoints:
        p = [p[0]*size, p[1]*size, p[2]*size]
        p[idxPos] = p[idxPos]+length
        cvs.append(p)
    
    theCurve = cmds.curve(d=1, p=cvs)
    theCurve = cmds.rename(theCurve, name)
    
    return theCurve

def CreateBall(name='ball', size=1):
    ballTransform = cmds.group(name=name, empty=True)
    
    for axis in ['X', 'Y', 'Z']:
        circle = CreateCircle(axis, size)
        theShape = cmds.listRelatives(circle, shapes=True, fullPath=True)[0]
        cmds.parent(theShape, ballTransform, r=True, s=True)
        cmds.delete(circle)
    
    return ballTransform

def CreateDeg1SplineOverPoints(curveName, DCsList, curveWidth=3):
    DCsList = [pm.PyNode(x) for x in DCsList]
    DCsShapes = [dc.getShape() for dc in DCsList]
    points = [list(x.worldPosition[0].get().get()) for x in DCsShapes]
    knots = list(range(0,len(DCsList)))
    
    theCurve = pm.curve(name=curveName, d=1, p=points, k=knots)
    theShape = theCurve.getShape()
    theShape.lineWidth.set(curveWidth)
    
    for idx, DCShape in enumerate(DCsShapes):
        DCShape.worldPosition[0].connect(theShape.controlPoints[idx])
    
    return theCurve

# #################################################################################
# ############################### Modification ####################################
# #################################################################################
def SetCtlColor(node, indexColor=None, rgbColor=None):
    """Sets the color of all shapes of a given node.
    
    Args:
        node (string): Node name of the desired node.
        indexColor (int, optional): Index value for Maya Default Color indexes. Defaults to None.
        rgbColor ([float, float, float], optional): Array of float values describing a RGB Color. Defaults to None.
    """
    shapes = cmds.listRelatives(node, shapes=True, fullPath=True)
    if (shapes):
        for shape in shapes:
            cmds.setAttr("{}.overrideEnabled".format(shape), 1)
            if (rgbColor):
                cmds.setAttr("{}.overrideRGBColors".format(shape), 1)
                cmds.setAttr("{}.overrideColorRGB".format(shape), *rgbColor)
            elif (indexColor):
                cmds.setAttr("{}.overrideRGBColors".format(shape), 0)
                cmds.setAttr("{}.overrideColor".format(shape), indexColor)

def ScaleShape(node, scaleFactor):
    """Translates a shape's points in 3 axes.

    Args:
        node (String or PyNode): The node to be modified
        scaleFactor ([float, float, float]): The values to be used for scaling
    """
    node = pm.PyNode(node)
    for shape in node.getShapes():
        for idx in range(shape.numCVs()):
            point = shape.getCV(idx)
            newPoint = [point[0]*scaleFactor[0], point[1]*scaleFactor[1], point[2]*scaleFactor[2]]
            shape.setCV(idx, newPoint)
        shape.updateCurve()


def ChangeShapeToPointLocator(nodesList):
    """Change the sape of a node for a Point Locator with the axes turned on.

    Args:
        nodesList ([strings or PyNodes]]): list of nodes to work.
    """
    nodesList = [pm.PyNode(x) for x in nodesList]
    pLocResults = []
    for node in nodesList:
        node = pm.PyNode(node)
        
        pLoc = pm.createNode("PointLocator")
        pLoc.axes.set(1)
        
        pLocParent = pLoc.getParent()
        oldShape = node.getShape()
        
        #Try and set a size similar to bounding box max size
        maxSize = 0
        if (oldShape):
            bbox = oldShape.boundingBox()
            size = [bbox.width(), bbox.height(), bbox.depth()]
            size.sort()
            maxSize = size[-1]
        
        if(maxSize <= 0):
            maxSize = 1
            
        pLoc.size.set(maxSize)
        
        if (oldShape):
            shapeName = oldShape.getName()
            pm.delete(oldShape)
        else:
            shapeName = "{}Shape".format(node.getName())
        
        pLoc.setName(shapeName)
        pm.parent(pLoc,node, r=True, s=True)
        pLocResults.append(pLoc)
        pm.delete(pLocParent)
        
        SetCtlColor(node.getName(), indexColor=14)
    return pLocResults