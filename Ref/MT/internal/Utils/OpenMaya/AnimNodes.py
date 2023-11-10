# coding: utf-8

import maya.api.OpenMaya as OpenMaya

import maya.cmds as cmds

import Utils.Maya.AnimLayers as LayerUtils
import Utils.OpenMaya as OpenMayaUtils

def isAnimNode(node, animCurve=True, blendNode=True, api=OpenMaya):
    nodeFnType = OpenMayaUtils.getNodeType(node, api=api)

    if animCurve:
        if nodeFnType >= api.MFn.kAnimCurve and nodeFnType <= api.MFn.kAnimCurveUnitlessToUnitless:
            return True

    if blendNode:
        if (nodeFnType >= api.MFn.kBlendNodeBase and nodeFnType <= api.MFn.kBlendNodeAdditiveRotation) or nodeFnType == api.MFn.kBlendNodeTime:
            return True

    return False
    
def getTargetPlugsForAnimNode(animNode, plugChildIndex=0, api=OpenMaya):
    # NOTE: Since this method is recursive it won't check if the provided MObject is a valid anim node. That responsability lies on the caller.
    if type(animNode) == api.MFnDependencyNode:
        dependencyNode = animNode
        animNode = dependencyNode.object()
    else:
        dependencyNode = api.MFnDependencyNode(animNode)
    outputPlug = dependencyNode.findPlug("output", False)
    
    # Special case for rotation blend nodes, that features 3 different components
    if OpenMayaUtils.getNodeType(animNode, api=api) == api.MFn.kBlendNodeAdditiveRotation:
        outputPlug = outputPlug.child(plugChildIndex)
    if api == OpenMaya:
        outConnections = outputPlug.connectedTo(False, True)
    else:
        outConnections = api.MPlugArray()
        outputPlug.connectedTo(outConnections, False, True)
        outConnections = [outConnections[i] for i in range(outConnections.length())]
    
    result = []
    for plug in outConnections:
        node = plug.node()
        if isAnimNode(node, api=api):
            plugChildIndex = 0
            isChild = plug.isChild if api == OpenMaya else plug.isChild()
            if isChild:
                plugParent = plug.parent()
                for i in range(plugParent.numChildren()):
                    if plugParent.child(i) == plug:
                        plugChildIndex = i
                        
            result.extend(getTargetPlugsForAnimNode(node, plugChildIndex=plugChildIndex, api=api))
        else:
            result.append(plug)
    
    return result

def getNodeAttributeFromAnimNode(animNode, api=OpenMaya):
    animNodeMObject = OpenMayaUtils.asMObject(animNode, api=api)
    if not isAnimNode(animNodeMObject):
        raise AssertionError("The provided node [{}] is not an animation node!".format(animNode))

    connectedPlugs = getTargetPlugsForAnimNode(animNodeMObject)
    connectedAttributes = [(api.MFnDependencyNode(plug.node()).name(), api.MFnAttribute(plug.attribute()).name) for plug in connectedPlugs]

    # NOTE: Returning just the first element (or just None) and not an array is not correct, but since most of the time there is going to be only one connection, doing this will simplify the code.
    if len(connectedAttributes) == 0:
        return None, None
    elif len(connectedAttributes) == 1:
        return connectedAttributes[0]
    else:
        return connectedAttributes

def getLayerBlendNodes(layer, layersToFilterForBaseLayer=None):
    # Retrieves the base layer to check if any of the provided layers is the base one.
    # Blend nodes for this layer are retrieved in a different way.
    if not LayerUtils.isBaseLayer(layer):
        # We can use the command "animLayer" to directly retrive the blend nodes for all the objects on a specific layer.
        return cmds.animLayer(layer, q=True, blendNodes=True) or []
    else:
        # The base layer doesn't have a blend node of its own. Instead, the curves for this layer are assigned to the the other anim layers' blend nodes.
        baseBlendNodes = []
        if layersToFilterForBaseLayer == None:
            layersToFilterForBaseLayer = cmds.ls(type="animLayer")
        for layer in layersToFilterForBaseLayer:
            blendNodes = cmds.animLayer(layer, q=True, blendNodes=True) or []
            for blendNode in blendNodes:
                inputPlug = "{0}.inputA".format(blendNode)
                if OpenMayaUtils.getNodeType(blendNode) == OpenMaya.MFn.kBlendNodeAdditiveRotation:
                    inputPlug += "X"    # Rotation blend nodes have their output connected to their coordinates. Uses the X one to keep looking for connections. NOTE: This may cause problems if the X coordinate is on a different layer than the other coordinates.
                connections = cmds.listConnections(inputPlug, s=True, d=False)
                if connections == None or not isAnimNode(connections[0], animCurve=False, blendNode=True):
                    baseBlendNodes.append(blendNode)
        return baseBlendNodes
