import pymel.core as pm

def CreateRotOffsetedRef(ctl, axis, degrees, descripName=""):
    ctl = pm.PyNode(ctl)
    rotationOffset = [0,0,0]
    idxVal = 0
    if (axis == "Y"):
        idxVal = 1
    elif (axis == "Z"):
        idxVal = 2
    rotationOffset[idxVal] = degrees
    
    if descripName:
        descripName = "_{}".format(descripName)
    
    newGrp = pm.group(name="{}{}_swRef".format(ctl, descripName), empty=True)
    newGrp.setParent(ctl)
    newGrp.translate.set([0,0,0])
    newGrp.rotate.set(rotationOffset)
    
    return newGrp

def AddRotationSpaces(rotSpaceNodesList, targetNode, UIAttrName, UIHolder="self", addParentAsSelf=True, maintainOffset=False, trailingChopString="_ctl"):
    """Adds Rotation Space Switches to a node, and lets select the node that will have the enum attribute

    Args:
        rotSpaceNodesList (list of String or PyNodes): List of nodes that will be rotation spaces
        targetNode (String or PyNode): Node that will receive the rotation spaces
        UIAttrName (String): Name of the UI attribute on the channelBox
        UIHolder (str, optional): node that will hold the attribute. Defaults to "self".
        addParentAsSelf (bool, optional): Adds its parent as rotation space named 'self'. Defaults to True.
        maintainOffset (bool, optional): Maintaint offset. Defaults to False.
        trailingChopString (str, optional): Trailing string for the namiing of new nodes. Defaults to "_ctl".
    """
    rotSpaceNodesList = [pm.PyNode(x) for x in rotSpaceNodesList]
    enumList = [x.getName() for x in rotSpaceNodesList]
    targetNode = pm.PyNode(targetNode)
    
    if (addParentAsSelf):
        rotSpaceNodesList.insert(0, targetNode.getParent())
        enumList.insert(0, "self")
    baseName = targetNode.getName()
    if trailingChopString and baseName.endswith(trailingChopString):
        baseName = baseName[:-len(trailingChopString)]
    parentRot = pm.group(name="{}_rotSpace".format(baseName), empty=True)
    parentRot.setParent(targetNode.getParent())
    parentRot.translate.set([0,0,0])
    parentRot.rotate.set([0,0,0])
    targetNode.setParent(parentRot)
    oriCns = pm.orientConstraint(rotSpaceNodesList, parentRot, mo=maintainOffset)
    
    # UI Attribute
    if (UIHolder=="self"):
        UIHolder = targetNode
    else:
        UIHolder = pm.PyNode(UIHolder)
    
    if (not hasattr(UIHolder, UIAttrName)):
        pm.addAttr(UIHolder, ln=UIAttrName, at="enum", en=enumList, k=True)
    else:
        raise(Exception("The attribute '{}' already exists".format(UIAttrName)))
    attr = getattr(UIHolder, UIAttrName)
    
    # Create Conditions
    for i, val in enumerate(rotSpaceNodesList):
        conditionNode = pm.createNode("condition")
        attr.connect(conditionNode.firstTerm)
        conditionNode.secondTerm.set(i)
        conditionNode.operation.set(0)
        conditionNode.colorIfTrueR.set(1)
        conditionNode.colorIfFalseR.set(0)
        realPlug = oriCns.target[i].targetWeight.inputs(p=True)[0]
        conditionNode.outColorR.connect(realPlug)

def AddPositionSpaces(posSpaceNodesList, targetNode, UIAttrName, UIHolder="self", addParentAsSelf=True, maintainOffset=False, trailingChopString="_ctl"):
    """Adds Rotation Space Switches to a node, and lets select the node that will have the enum attribute

    Args:
        posSpaceNodesList (list of String or PyNodes): List of nodes that will be rotation spaces
        targetNode (String or PyNode): Node that will receive the rotation spaces
        UIAttrName (String): Name of the UI attribute on the channelBox
        UIHolder (str, optional): node that will hold the attribute. Defaults to "self".
        addParentAsSelf (bool, optional): Adds its parent as rotation space named 'self'. Defaults to True.
        maintainOffset (bool, optional): Maintaint offset. Defaults to False.
        trailingChopString (str, optional): Trailing string for the namiing of new nodes. Defaults to "_ctl".
    """
    posSpaceNodesList = [pm.PyNode(x) for x in posSpaceNodesList]
    enumList = [x.getName() for x in posSpaceNodesList]
    targetNode = pm.PyNode(targetNode)
    
    if (addParentAsSelf):
        posSpaceNodesList.insert(0, targetNode.getParent())
        enumList.insert(0, "self")
    baseName = targetNode.getName()
    if trailingChopString and baseName.endswith(trailingChopString):
        baseName = baseName[:-len(trailingChopString)]
    parentRot = pm.group(name="{}_rotSpace".format(baseName), empty=True)
    parentRot.setParent(targetNode.getParent())
    parentRot.translate.set([0,0,0])
    parentRot.rotate.set([0,0,0])
    targetNode.setParent(parentRot)
    posCns = pm.pointConstraint(posSpaceNodesList, parentRot, mo=maintainOffset)
    
    # UI Attribute
    if (UIHolder=="self"):
        UIHolder = targetNode
    else:
        UIHolder = pm.PyNode(UIHolder)
    
    if (not hasattr(UIHolder, UIAttrName)):
        pm.addAttr(UIHolder, ln=UIAttrName, at="enum", en=enumList, k=True)
    else:
        raise(Exception("The attribute '{}' already exists".format(UIAttrName)))
    attr = getattr(UIHolder, UIAttrName)
    
    # Create Conditions
    for i, val in enumerate(posSpaceNodesList):
        conditionNode = pm.createNode("condition")
        attr.connect(conditionNode.firstTerm)
        conditionNode.secondTerm.set(i)
        conditionNode.operation.set(0)
        conditionNode.colorIfTrueR.set(1)
        conditionNode.colorIfFalseR.set(0)
        realPlug = posCns.target[i].targetWeight.inputs(p=True)[0]
        conditionNode.outColorR.connect(realPlug)