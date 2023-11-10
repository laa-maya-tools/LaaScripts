import maya.cmds as cmds

# Scene Listing
def ListAllTags():
    return cmds.ls(type="controller")

def ListAllTagRoots():
    allTags = ListAllTags()
    allRoots = [x for x in allTags if (GetParentTag(x) == None)]
    return allRoots

# Tags Managing
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

# TODO: falta implementar la conexion del nuevo padre
def SetTagParent(controllerTag, parentTag):
    #Disconnect Current Parent
    conns = cmds.listConnections("{}.parent".format(controllerTag), c=True, p=True)
    for c in conns:
        cmds.disconnectAttr(conns[0], conns[1])
    #Disconnect Current Prepopulate
    conns = cmds.listConnections("{}.prepopulate".format(controllerTag), c=True, p=True)
    for c in conns:
        cmds.disconnectAttr(conns[1], conns[0])
    #TODO: Connect New Parent
    
# Nodes Managing
def GetTagNode(controllerTag):
    ctlObjConnections = cmds.listConnections("{}.controllerObject".format(controllerTag))
    if (ctlObjConnections):
        return ctlObjConnections[0]
    return None
    
def GetChildrenNodes(controllerTag):
    listChildrenTags = GetChildrenTags(controllerTag)
    result = []
    for childTag in listChildrenTags:
        childTagNode = GetTagNode(childTag)
        if (childTagNode):
            result.append(childTagNode)
    return result

def GetParentNode(controllerTag):
    parentTag = GetParentTag(controllerTag)
    if (parentTag):
        return GetTagNode(parentTag)
    return None

# Hierarchy Managing
class TagLeaf():
    def __init__(self, nodeName, controllerTag):
        self.printIndent = 0
        self.nodeName = nodeName
        self.controllerTag = controllerTag
        self.children = []
    
    def __str__(self):
        strValue = "{} - {}\n".format(self.nodeName, self.controllerTag)
        for c in self.children:
            c.printIndent = self.printIndent + 1
            strValue += "\t" * self.printIndent
            strValue += str(c)
            c.printIndent = 0
        return strValue
    
    def __iter__(self):
        yield self.nodeName
        for child in self.children:
            yield from child

def GetHierarchyFromTag(controllerTag):
    currentNode = GetTagNode(controllerTag)
    result = TagLeaf(currentNode, controllerTag)
    for childTag in GetChildrenTags(controllerTag):
        result.children.append(GetHierarchyFromTag(childTag))
    return result

# Utilities
def SortByHierarchy(nodes):
    sorted = []
    remaining = set(cmds.ls(nodes, long=True) or [])
    while len(remaining) > 0:
        item = next(iter(remaining))
        controller = GetControllerTag(item)
        
        if controller:
            while True:
                parentController = GetParentTag(controller)
                if parentController:
                    controller = parentController
                else:
                    break
            
            hierarchy = GetHierarchyFromTag(controller)
            hierarchy = [node for node in hierarchy if node != None]
            hierarchy = cmds.ls(hierarchy, long=True) or []
            for i, obj in enumerate(hierarchy):
                if obj in remaining and obj not in hierarchy[i+1:]: # The node might have multiple parents and thus be several times on the list. We check this is the last occurence.
                    sorted.append(obj)
                    remaining.remove(obj)
        
        else:
            hierarchy = cmds.listHistory("{}.worldMatrix".format(item), leaf=False) or []
            if item not in hierarchy:
                hierarchy.insert(0, item)
            hierarchy.reverse()
            for obj in hierarchy:
                if obj in remaining:
                    sorted.append(obj)
                    remaining.remove(obj)
    
    return sorted
