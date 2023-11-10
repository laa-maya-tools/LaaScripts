import maya.cmds as cmds
import pymel.core as pm
import json
import copy

# Create tags recursively
def CreateTagHierarchy(hierarchyDict, parentTag=None):
    keys = list(hierarchyDict.keys())
    for key in keys:
        tagName = key + "_tag"
        # Create tag if it doesn't exist
        if (not cmds.objExists(tagName)):
            pm.controller(key)
        # Find tag (previous function doesn't return the tag node)
        tag = pm.PyNode(tagName)
        # If this is not the root tag, connect it to its parent
        if (parentTag is not None):
            # Check if tag has parentTag as a parent already
            if (not IsParentTag(tag, parentTag)):
                childIndex = GetAvailableChildrenConnectionIndex(parentTag)
                pm.connectAttr(tag.name() + ".parent", parentTag.name() + ".children[{}]".format(str(childIndex)))
                # pm.connectAttr(parentTag.name() + ".prepopulate", tag.name() + ".prepopulate")
        # Inspect current tag children and repeat the process
        CreateTagHierarchy(hierarchyDict[key], parentTag=tag)

# Get first available connection in children attribute (children[0], children[1]...)
def GetAvailableChildrenConnectionIndex(node):
    nextAvailableIndex = None
    i = 0
    while (nextAvailableIndex is None):
        conn = cmds.listConnections(node.name() + ".children[{}]".format(str(i)))
        if (conn is None):
            nextAvailableIndex = i
        i += 1
    return nextAvailableIndex

# Check if tag is already connected as a parent
def IsParentTag(tag, parentTag):
    isParent = False
    connections = cmds.listConnections(tag.name() + ".parent") or []
    for connection in connections:
        if (parentTag.name() == connection):
            isParent = True
    return isParent

# Create child tag from a control
def CreateChildTag(control, parentControl=None):
    tagName = control.getName() + "_tag"
    # Create tag if it doesn't exist
    if (not cmds.objExists(tagName)):
        pm.controller(control)
    if (parentControl != None):
        # Find tag
        tag = pm.PyNode(tagName)
        # Look for parent tag
        parentCtl = pm.PyNode(parentControl)
        parentTag = pm.listConnections(parentCtl.message, type="controller")[0]
        # Connect
        if (not IsParentTag(tag, parentTag)):
            childIndex = GetAvailableChildrenConnectionIndex(parentTag)
            pm.connectAttr(tag.name() + ".parent", parentTag.name() + ".children[{}]".format(str(childIndex)))
            connectionTuple = (tag.name() + ".parent", parentTag.name() + ".children[{}]".format(str(childIndex)))
            return connectionTuple

def DeleteAllTags():
    currentTags = ListAllTags()
    pm.delete(currentTags)

def GetSelectedObjects():
    selection = pm.ls(sl=True, type="transform")
    return selection

def ReadTagsFile(path):
    data = {}
    with open(path, 'r') as fp:
        data = json.load(fp)
        fp.close()
    return data

def WriteTagsFile(path, tags):
    with open(path, 'w') as fp:
        json.dump(tags, fp, indent=4)
        fp.close()

def AddChildrenTags(parentTag, parentDict):
    childrenTags = pm.listConnections(parentTag.children, type="controller")
    for childTag in childrenTags:
        try:
            controller_object = pm.listConnections(childTag.controllerObject)[0]
            parentDict[controller_object.getName()] = {}
            AddChildrenTags(childTag, parentDict[controller_object.getName()])
        except IndexError:
            pass

def GetSceneTagsDictionary():
    tagsDict = {}
    currentTags = pm.ls(type="controller")
    for currentTag in currentTags:
        parentConns = pm.listConnections(currentTag.parent)
        # If it's a top level tag, add to dict and recursively find children tags
        if (len(parentConns) == 0):
            # Add top level element as tree item, recursively do the same with its children
            try:
                controllerObject = pm.listConnections(currentTag.controllerObject)[0]
                tagsDict[controllerObject.getName()] = {}
                AddChildrenTags(currentTag, tagsDict[controllerObject.getName()])
            except IndexError:
                pass
    return tagsDict

def GetChildIndex(childTag, parentTag):
    childIndex = None
    children = pm.listConnections(parentTag.children)
    childrenAmount = len(children)
    childrenFound = 0
    idx = 0
    while (childrenFound < childrenAmount):
        try:
            current_child = pm.listConnections(parentTag.children[idx])[0]
            childrenFound += 1
            if (current_child == childTag):
                childIndex = idx
                break
        except IndexError:
            pass
        idx += 1
    return childIndex

def IsCyclicTag(tag, ocurrences):
    isCyclic = False
    parentTags = pm.listConnections(tag.parent, type="controller")
    for parentTag in parentTags:
        ocurrencesBranch = copy.deepcopy(ocurrences)
        if (parentTag in ocurrencesBranch):
            isCyclic = True
            break
        else:
            ocurrencesBranch.append(parentTag)
            isCyclic = IsCyclicTag(parentTag, ocurrencesBranch)
    return isCyclic

def HasCyclicRelation(tag):
    ocurrences = [tag]
    isCyclic = IsCyclicTag(tag, ocurrences)
    return isCyclic

def IsValidTag(tag):
    valid = True
    if (GetTagNode(tag) == None):
        valid = False
    return valid

def ImportControlTagsFromFile(fileName):
    data = ReadTagsFile(fileName)
    CreateTagHierarchy(data)

def ExportControlTagsToFile(fileName):
    data = GetSceneTagsDictionary()
    WriteTagsFile(fileName, data)

# ###################################################### Scene Listing ######################################################
def ListAllTags():
    return cmds.ls(type="controller")

def ListAllTagRoots():
    allTags = ListAllTags()
    allRoots = [x for x in allTags if (GetParentTag(x) == None)]
    return allRoots

# ###################################################### Tags Managing ######################################################
def GetControllerTag(node):
    ctlTagsConnections = cmds.listConnections("{}.message".format(node), type="controller")
    if (ctlTagsConnections):
        return ctlTagsConnections[0]
    return None

def GetParentTag(controllerTag):
    listParentTags = cmds.listConnections("{}.parent".format(controllerTag), type="controller")
    if (listParentTags):
        #Force it to have one parent. Maybe we want the ability to have multiple?
        return listParentTags[0]
    return None

def GetChildrenTags(controllerTag):
    return cmds.listConnections("{}.children".format(controllerTag), type="controller") or []

# ###################################################### Nodes Managing ######################################################
def GetTagNode(controllerTag):
    ctlObjConnections = cmds.listConnections("{}.controllerObject".format(controllerTag))
    if (ctlObjConnections):
        return ctlObjConnections[0]
    return None

# ###################################################### Utilities ######################################################
def GetInvalidTags():
    """Returns all tags that has no connected control node
    """
    result = []
    for tag in ListAllTags():
        if (GetTagNode(tag) == None):
            result.append(tag)
    return result