import pymel.core as pm
import RigUtils.Maths as RigMaths

ATTRS_TO_HIDE = ["visibility"]
NAME_RULES_HIDE_ATTRS = ["*_ctl", "*_CTL"]

def HideUnwantedAttribs():
    matches = pm.ls(NAME_RULES_HIDE_ATTRS)
    for match in matches:
        for attribute in ATTRS_TO_HIDE:
            match.attr(attribute).showInChannelBox(False)
            # Keyable attributes always show in channlbox, so we have to set it as notnkeyable
            match.attr(attribute).setKeyable(False)

def SetNiceOrient(node, recursive=False, verbose=False):
    """Sets the rotations of the given node in between -180 and 180 degrees, keeping its current visual orientation.
    
    Args:
        node (PyNode): Node to set simplified angles in x, y and z between -180 and 180
        verbose (bool, optional): Prints information on execution. Defaults to False.
    
    Returns:
        int: Sum between 0 and 3 of the number of rotations modified on the node
    """
    totalChanged = 0
    for attr in [node.rx, node.ry, node.rz]:
        currOrient = attr.get()
        niceOrient = RigMaths.CalculateNiceRotation(currOrient)
        if (niceOrient != currOrient):
            attr.set(niceOrient)
            totalChanged += 1
            if (verbose):
                print("{} changed from: {} to: {}".format(attr, currOrient, niceOrient))
    
    if (recursive):
        for child in node.getChildren(type=["joint", "transform"]):
            totalChanged += SetNiceOrient(child, recursive, verbose)
    
    return totalChanged

def SetOrientConstraintNiceOffsets(cns, verbose=False):
    """Sets the rotations of the given orient constraint in between -180 and 180 degrees, keeping its current visual orientation.
    Args:
        cns (PyNode): orient constraint to work with
        verbose (bool, optional): Prints information on execution. Defaults to False.
    """
    for axis in ["X", "Y", "Z"]:
        attr = getattr(cns, "offset{}".format(axis))
        currVal = attr.get()
        niceOrient = RigMaths.CalculateNiceRotation(currVal)
        if (niceOrient != currVal):
            attr.set(currVal)
            if (verbose):
                print("{} changed from: {} to: {}".format(attr, currVal, niceOrient))

def GetHierarchyConstraints(node, orient=False, point=False, parent=False, scale=False):
    """Returns all the desired constraints from a hierarchy
    
    Args:
        node (PyNode): root node of a hierarchy
        orient (bool, optional): return orient constraints. Defaults to False.
        point (bool, optional): return point constraints. Defaults to False.
        parent (bool, optional): return parent constraints. Defaults to False.
        scale (bool, optional): return scale constraints. Defaults to False.
    
    Returns:
        [PyNodes]: List of constraints
    """
    result = []
    types = []
    if orient:
        types.append("orientConstraint")
    if point:
        types.append("pointConstraint")
    if parent:
        types.append("parentConstraint")
    if scale:
        types.append("scaleConstraint")
    
    if types:
        result += node.getChildren(type=types)
        for child in node.getChildren(type=["joint", "transform"]):
            result += GetHierarchyConstraints(child, orient, point, parent, scale)
    return result