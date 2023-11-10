import pymel.core as pm

def GetModuleControlsRoot(moduleName):
    matches = pm.ls("{}_root".format(moduleName))
    result = None
    for match in matches:
        # If the node has this attribute, it is the root for the module controls
        if (pm.attributeQuery("compCtl", node=match, ex=True)):
            result = match
            break
    return result

def GetGuideRoot(moduleName):
    matches = pm.ls("{}_root".format(moduleName))
    result = None
    for match in matches:
        # If the node has this attribute, it is the root for the module controls
        if (not pm.attributeQuery("compCtl", node=match, ex=True)):
            result = match
            break
    return result

def SetWorldHierarchy(baseCtl="world_C0"):
    baseCtlRoot = GetModuleControlsRoot(baseCtl)
    defaultRoot = baseCtlRoot.getParent()
    rigRoot = defaultRoot.getParent()
    baseCtlRoot.setParent(rigRoot)
    toDeleteShapes = defaultRoot.getShapes()
    pm.delete(toDeleteShapes)

def IsRightSideModule(moduleName):
    spl = moduleName.split("_")
    for part in spl:
        if (len(part)==2 and (part[0]=="R")):
            return True
    return False