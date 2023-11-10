import maya.cmds as cmds

#---------------------------------
#|        Aux Functions          |
#---------------------------------
def IsVisible(obj, checkShapes=True, checkParents=True):
    if checkShapes:
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
        shapeVisible = False
        for shape in shapes:
            if IsVisible(shape, checkShapes=False, checkParents=False):
                shapeVisible = True
                break
        if not shapeVisible:
            return False
    
    if not cmds.getAttr("{}.visibility".format(obj)):
        return False
    if cmds.getAttr("{}.overrideEnabled".format(obj)) and not cmds.getAttr("{}.overrideVisibility".format(obj)):
        return False
        
    if checkParents:
        parent = cmds.listRelatives(obj, parent=True, fullPath=True)
        if parent:
            return IsVisible(parent[0], checkShapes=False, checkParents=True)
    
    return True

def GetParentsTags(controllerTag):
    return cmds.listConnections("{}.parent".format(controllerTag), type="controller") or []

def GetControllerTag(node):
    ctlTagsConnections = cmds.listConnections("{}.message".format(node), type="controller")
    if (ctlTagsConnections):
        return ctlTagsConnections[0]
    return None

def GetControllerObject(controllerTag):
    ctlObjConnections = cmds.listConnections("{}.controllerObject".format(controllerTag), type="transform")
    if (ctlObjConnections):
        return ctlObjConnections[0]
    return None

def GetConnectedNodes(controllerTag, attribName, checkVisibility=False):
    listNodesTags = cmds.listConnections("{}.{}".format(controllerTag, attribName), type="controller") or []
    result = []
    for cTag in listNodesTags:
        ctlObj = GetControllerObject(cTag)
        if (ctlObj):
            if (checkVisibility and (not IsVisible(ctlObj))):
                continue    
            result.append(ctlObj)
    return result

def GetChildrenNodes(node, recursive=False, checkVisibility=False):
    nodeTag = GetControllerTag(node)
    if nodeTag:
        children = GetConnectedNodes(nodeTag, "children", checkVisibility=checkVisibility)
        if recursive:
            recursiveChildren = []
            for child in children:
                recursiveChildren.append(child)
                recursiveChildren += GetChildrenNodes(child, recursive=True, checkVisibility=checkVisibility)
            return recursiveChildren
        else:
            return children
    return []

def GetParentNodes(node, recursive=False, checkVisibility=False):
    nodeTag = GetControllerTag(node)
    if nodeTag:
        parents = GetConnectedNodes(nodeTag, "parent", checkVisibility=checkVisibility)
        if recursive:
            recursiveParents = []
            for parent in parents:
                recursiveParents.append(parent)
                recursiveParents += GetParentNodes(parent, recursive=True, checkVisibility=checkVisibility)
            return recursiveParents
        else:
            return parents
    return []

def GetSiblings(node, checkVisibility=False):
    parentNodes = GetParentNodes(node)
    result = []
    for parentNode in parentNodes:
        result += GetChildrenNodes(parentNode, checkVisibility=checkVisibility)
    return list(set(result))

def GetListNeighbour(list, value, reverse=False):
    valIdx = list.index(value)
    if (not reverse):
        neighbourIdx = valIdx + 1
        if (neighbourIdx >= len(list)):
            return list[0]
        else:
            return list[neighbourIdx]
    else:
        neighbourIdx = valIdx - 1
        if (neighbourIdx < 0):
            return list[len(list)-1]
        else:
            return list[neighbourIdx]


#---------------------------------
#|     Commands Functions        |
#---------------------------------
def TravelToChildren(additive=False, recursive=False):
    selection = cmds.ls(sl=True)
    newSelection = []
    for node in selection:
        childrenNodes = GetChildrenNodes(node, recursive=recursive, checkVisibility=True)
        if (childrenNodes):
            newSelection += childrenNodes
        else:
            # The node has no children. Keep it selected.
            newSelection.append(node)
    
    if additive:
        newSelection += selection
        
    cmds.select(newSelection)

def TravelToParent(additive=False, recursive=False):
    selection = cmds.ls(sl=True)
    newSelection = []
    for node in selection:
        parentNodes = GetParentNodes(node, recursive=recursive, checkVisibility=True)
        if (parentNodes):
            newSelection += parentNodes
        else:
            # The node has no children. Keep it selected.
            newSelection.append(node)
    
    if additive:
        newSelection += selection
    
    cmds.select(newSelection)

def TravelToSibling(reverse=False, all=False, additive=False, checkVisibility=False):
    selection = cmds.ls(sl=True)
    newSelection = []
    for node in selection:
        siblings = GetSiblings(node, checkVisibility=checkVisibility)
        if (node in siblings):
            if all:
                newSelection += siblings
            else:
                newSelection.append(GetListNeighbour(siblings, node, reverse))
        else:
            # The node has no siblings. Keep it selected.
            newSelection.append(node)
    
    if additive:
        newSelection += selection
    
    cmds.select(newSelection)

def TravelToSiblingUp(additive=False):
    TravelToSibling(reverse=False, additive=additive, checkVisibility=True)

def TravelToSiblingDown(additive=False):
    TravelToSibling(reverse=True, additive=additive, checkVisibility=True)

def TravelToAllSiblings():
    TravelToSibling(all=True, additive=True, checkVisibility=True)

#---------------------------------
#|           Commands            |
#---------------------------------
def register():
    cmds.runTimeCommand("TravelToChildren",             cat="MSE Commands.Travel Hierarchy",    ann="Selects the next custom hierarchy children.",                  c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToChildren()", default=True)
    cmds.runTimeCommand("TravelToChildrenAdditive",     cat="MSE Commands.Travel Hierarchy",    ann="Adds the next custom hierarchy children to the selection.",    c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToChildren(additive=True)", default=True)
    cmds.runTimeCommand("TravelToAllDescendants",       cat="MSE Commands.Travel Hierarchy",    ann="Selects all the custom hierarchy descendants.",                c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToChildren(additive=True, recursive=True)", default=True)
    cmds.runTimeCommand("TravelToParent",               cat="MSE Commands.Travel Hierarchy",    ann="Selects the custom hierarchy parent.",                         c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToParent()", default=True)
    cmds.runTimeCommand("TravelToParentAdditive",       cat="MSE Commands.Travel Hierarchy",    ann="Adds the custom hierarchy parent to the selection.",           c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToParent(additive=True)", default=True)
    cmds.runTimeCommand("TravelToSiblingUp",            cat="MSE Commands.Travel Hierarchy",    ann="Selects the custom hierarchy next sibling.",                   c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToSiblingUp()", default=True)
    cmds.runTimeCommand("TravelToSiblingUpAdditive",    cat="MSE Commands.Travel Hierarchy",    ann="Adds the next custom hierarchy sibling to the selection.",     c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToSiblingUp(additive=True)", default=True)
    cmds.runTimeCommand("TravelToSiblingDown",          cat="MSE Commands.Travel Hierarchy",    ann="Selects the custom hierarchy previous sibling.",               c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToSiblingDown()", default=True)
    cmds.runTimeCommand("TravelToSiblingDownAdditive",  cat="MSE Commands.Travel Hierarchy",    ann="Adds the pewvious custom hierarchy sibling to the selection.", c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToSiblingDown(additive=True)", default=True)
    cmds.runTimeCommand("TravelToAllSiblings",          cat="MSE Commands.Travel Hierarchy",    ann="Selects all the custom hierarchy siblings.",                   c="import CustomCommands.TravelCustomHierarchy as T; T.TravelToAllSiblings()", default=True)
