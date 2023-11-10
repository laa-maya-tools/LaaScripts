import maya.api.OpenMaya as OpenMaya

import maya.cmds as cmds

from Utils.Python.Versions import basestring

def asMObject(node, api=OpenMaya):
    if node is None:
        return None
    
    if type(node) != api.MObject:
        if not isinstance(node, basestring):
            raise TypeError("The provided node name is not a string value! {}".format(node))
        
        if not cmds.objExists(node):
            return None
        
        selectionList = api.MSelectionList()
        selectionList.add(node)
        if api == OpenMaya:
            node = selectionList.getDependNode(0)
        else:
            node = api.MObject()
            selectionList.getDependNode(0, node)
            
    return node

def asMPlug(plug, api=OpenMaya):
    if plug is None:
        return None
    
    if type(plug) != api.MPlug:
        if not isinstance(plug, basestring):
            raise TypeError("The provided plug name is not a string value! {}".format(plug))
        
        if not cmds.objExists(plug):
            return None
        
        selectionList = api.MSelectionList()
        selectionList.add(plug)
        if api == OpenMaya:
            plug = selectionList.getPlug(0)
        else:
            plug = api.MPlug()
            selectionList.getPlug(0, plug)
            
    return plug

def asDagPath(path, api=OpenMaya):
    if type(path) != api.MDagPath:
        path = asMObject(path, api=api)
        
        if path is None:
            return None
        
        nodeFn = api.MFnDagNode(path)
        if api == OpenMaya:
            path = nodeFn.getPath()
        else:
            path = api.MDagPath()
            nodeFn.getPath(path)
        
    return path

def getNodeType(node, api=OpenMaya):
    return asMObject(node, api=api).apiType()

def getDisplayOverrideColorState(node, api=OpenMaya):
    fn = api.MFnDagNode(asDagPath(node))
    
    if fn.findPlug("overrideEnabled", False).asBool() and (fn.findPlug("overrideRGBColors", False).asBool() or fn.findPlug("overrideColor", False).asInt() != 0):
        return True
    
    if fn.parentCount() > 0:
        return getDisplayOverrideColorState(fn.parent(0), api=api)
    
    return False
