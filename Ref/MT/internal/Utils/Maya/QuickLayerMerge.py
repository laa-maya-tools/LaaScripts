# coding: utf8

import Utils.Maya.AnimLayers as LayerUtils
import Utils.OpenMaya as OpenMayaUtils
import Utils.OpenMaya.AnimNodes as AnimNodeUtils
import Utils.OpenMaya.ApiUndo as ApiUndo

from Utils.Maya.UndoContext import UndoContext

import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaAnim as OpenMayaAnim

import maya.cmds as cmds

# Auxiliary class to wrap the list of blendnodes used by an animation layer.
# Precalculates a lot information to speed up the layer merge process.
class LayerBlendInfo():

    def __init__(self, blendNodes, isBaseLayer):
        # Information is stored on a series of arrays with the same size.
        # And index into these arrays indicates data related to the same blend node
        self.blendNodes = blendNodes
        self.isBaseLayer = isBaseLayer

        # Retrieves the type of the blend node. The type is an enum defined in OpenMaya.MFn.
        # The type of the node will be used to combine the layers (additively, multiplicative, boolean...).
        self.blendNodeTypes = [(OpenMayaUtils.getNodeType(blendNode) if blendNode != None else None) for blendNode in self.blendNodes]
        
        # Gets an API reference to the blend nodes so we can use the API methods (which are faster).
        selectionList = OpenMaya.MSelectionList()
        mObjects = []
        for objName in self.blendNodes:
            if objName != None:
                selectionList.add(objName)
                mObjects.append(OpenMaya.MFnDependencyNode(selectionList.getDependNode(selectionList.length() - 1)))
            else:
                mObjects.append(None)
        
        # Retrieves and stores the animation plugs for the weight attribute, so we don't need to find them each time.
        # The weight for each layer is stored on the "weightA" attribute on each blend node.
        # However, the base layer has it's weight stored on the first layer's "weightB" attribute (but it should be useless since the weight of the first layer is always one).
        self.weightPlugs = []
        weightAttribute = "weightA" if self.isBaseLayer else "weightB"
        for mObject in mObjects:
            if mObject != None:
                # The weight plug may not be directly connected to the animation curve, walks through the connections looking for the curve.
                plug = mObject.findPlug(weightAttribute, False)
                while plug.isDestination:
                    plug = plug.connectedTo(True, False)[0]
                self.weightPlugs.append(plug)
            else:
                self.weightPlugs.append(None)

        # We also store the other weight attribute ("weightA"). It should always be 1, but it might be different if the layer is set to override mode (instead of additive).
        # This only has meaning in layers other than the base one, since this layer already checks "weightA" for it's own weight.
        if not self.isBaseLayer:
            self.weightAccumulativePlugs = []
            for mObject in mObjects:
                if mObject != None:
                    # The weight plug may not be directly connected to the animation curve, walks through the connections looking for the curve.
                    plug = mObject.findPlug("weightA", False)
                    while plug.isDestination:
                        plug = plug.connectedTo(True, False)[0]
                    self.weightAccumulativePlugs.append(plug)
                else:
                    self.weightAccumulativePlugs.append(None)
        
        # Retrieves and stores the animation curves for the input attribute, so we don't need to find them each time.
        # The attributes "inputA" and "inputB" behaves in the same way as the weight did, and they store the very animation for the layer.
        # Since the attribute may not be animated, it may not have an anim curve. Stores the value of the attribute instead.
        # We also store the plugs as well, since they might be usefull on the marginal case that there are no animation curves yet we need to change the value.
        self.animCurves = []
        self.animValues = []
        self.animPlugs = []
        valueAttribute = "inputA" if self.isBaseLayer else "inputB"
        for mObject in mObjects:
            if mObject != None:
                # Rotation blend nodes have compound input attributes, which means they have multiple animation curves (that's why we store the plugs and curves as arrays).
                plugs = [mObject.findPlug(valueAttribute, False)]
                if plugs[0].isCompound:
                    plugs = [plugs[0].child(j) for j in range(plugs[0].numChildren())]

                curves = []
                values = []
                for plug in plugs:
                    # The input plug will always be directly connected to the animation curve, but there might not be an animation curve if the attribute is not animated.
                    # If there is not an animation curve, stores the value of the attribute.
                    animCurve = getAnimCurveForPlug(plug)
                    if animCurve != None:
                        curves.append(animCurve)
                        values.append(None)
                    else:
                        curves.append(None)
                        values.append(plug.asDouble())

                self.animCurves.append(curves)
                self.animValues.append(values)
                self.animPlugs.append(plugs)
            else:
                self.animCurves.append([])
                self.animValues.append([])
                self.animPlugs.append([])

        # Retrieve the rotate orders for the rotation blend nodes, so we don't need to find them each time.
        # We also retrieve the accumulation mode for both rotation and scale nodes.
        self.rotateOrders = [None] * len(mObjects)
        self.accumulationModes = [None] * len(mObjects)
        for i in range(len(mObjects)):  # No "None MObject check" is neccesary here due to how it is implemented. The list is already filled with None values.
            if self.blendNodeTypes[i] == OpenMaya.MFn.kBlendNodeAdditiveRotation:
                self.rotateOrders[i] = mObjects[i].findPlug("rotateOrder", False).asInt()
                self.accumulationModes[i] = mObjects[i].findPlug("accumulationMode", False).asInt()
            elif self.blendNodeTypes[i] == OpenMaya.MFn.kBlendNodeAdditiveScale:
                self.accumulationModes[i] = mObjects[i].findPlug("accumulationMode", False).asInt()

    # Gets the value of the indexed blend node, taken the weight into account.
    # If an accumulated value it provides, it combines it with the new value according to the type of the blend node.
    def getValue(self, index, time, accumulatedValue=None):
        if self.blendNodes[index] == None:
            return accumulatedValue # The layer doesn't influence in this attribute, returns the value as it is.
        
        animCurves = self.animCurves[index]
        animValues = self.animValues[index]
        blendNodeType = self.blendNodeTypes[index]
        
        # Retrieves the weight. If it is not animated, takes the precalculated value directly.
        # If the layer is not the base one, retrieves the accumulative weight as well. It will be multiplied to the accumulatedValue.
        # The base layer should never receive an accumulatedValue.
        if self.isBaseLayer:
            blendWeight = 1
        else:
            timeContext = OpenMaya.MDGContext(time)
            blendWeight = self.weightPlugs[index].asDouble(timeContext)
            if accumulatedValue is not None:
                accumulativeBlendWeight = self.weightAccumulativePlugs[index].asDouble(timeContext)

        # Evaluates the animation curves to get the value.
        # If it is not animated, takes the precalculated value directly.
        values = [value for value in animValues]
        for i in range(len(values)):
            if values[i] == None:
                values[i] = animCurves[i].evaluate(time)
            
        # In the case of rotations, there are 3 animation curves representing the x,y and z coordinates of an euler rotation.
        if blendNodeType == OpenMaya.MFn.kBlendNodeAdditiveRotation:
            rotationOrder = self.rotateOrders[index]
            value = OpenMaya.MEulerRotation(values[0], values[1], values[2], order=rotationOrder)
        else:
            value = values[0]

        # Applies the weight to the value according to the type of the blend node.
        # If an accumulated value was provided, combines the values (it assumes the accumulated value was already weighted).

        # Boolean blending:
        if blendNodeType == OpenMaya.MFn.kBlendNodeEnum or blendNodeType == OpenMaya.MFn.kBlendNodeBoolean:
            if self.isBaseLayer and blendWeight != 1:
                blendWeight = 0 # Boolean blending of the top layer is ON if >0, OFF else. Since we are on the Base Layer, it works like this: ON if =1, OFF else
            if blendWeight == 0:
                if accumulatedValue != None:
                    value = accumulatedValue * accumulativeBlendWeight
                else:
                    value = 0

        # Rotation blending:
        elif blendNodeType == OpenMaya.MFn.kBlendNodeAdditiveRotation:
            value *= blendWeight
            if type(accumulatedValue) == OpenMaya.MEulerRotation:
                accumulatedValue *= accumulativeBlendWeight
                accumulationMode = self.accumulationModes[index]
                if accumulationMode == 1: # Multiply Mode
                    value = value * accumulatedValue
                elif accumulationMode == 0: # Additive Mode
                    value.x += accumulatedValue.x
                    value.y += accumulatedValue.y
                    value.z += accumulatedValue.z

        # Scale blending:
        elif blendNodeType == OpenMaya.MFn.kBlendNodeAdditiveScale:
            accumulationMode = self.accumulationModes[index]
            if accumulationMode == 1: # Multiply Mode
                value = pow(value, blendWeight)
                if accumulatedValue != None:
                    value *= pow(accumulatedValue, accumulativeBlendWeight)
            elif accumulationMode == 0: # Additive Mode
                value *= blendWeight
                if accumulatedValue != None:
                    value += accumulatedValue * accumulativeBlendWeight
        
        # Default is additive blending.
        else:
            value *= blendWeight
            if accumulatedValue != None:
                value += accumulatedValue * accumulativeBlendWeight

        return value

    # Creates animation curves on the indexed blend node's input attributes which are not connected to one already.
    def createAnimCurves(self, index, change=None):
        if self.blendNodes[index] == None:
            return

        curves = self.animCurves[index]
        plugs = self.animPlugs[index]

        for i in range(len(curves)):
            if curves[i] == None:
                curves[i] = OpenMayaAnim.MFnAnimCurve()
                curves[i].create(plugs[i], modifier=change)

    # Sets the values for the indexed blend node.
    # It will replace all the existing keys with the times and values provided.
    def setKeyframes(self, index, times, values, change=None):
        curves = self.animCurves[index]

        # Rotation blend nodes have 3 curves, so we need to decompose the values array into one for each component.
        if self.blendNodeTypes[index] == OpenMaya.MFn.kBlendNodeAdditiveRotation:
            listX = [value.x for value in values]
            listY = [value.y for value in values]
            listZ = [value.z for value in values]
            values = [listX, listY, listZ]
        else:
            values = [values]
        
        # Clears the keys from the animation curves and creates the new ones.
        for i in range(len(curves)):
            # We could use the "addKeys" method to do this, but it is bugged when undoing it, so we have to do it manually (which is slower).
            #curves[i].addKeys(times, values[i], keepExistingKeys=False, change=change)

            for j in range(len(times)):
                # If there is already a keyframe there, changes it's value. Creates a new one otherwise.
                keyIndex = curves[i].find(times[j])
                if keyIndex != None:
                    curves[i].setValue(keyIndex, values[i][j], change=change)
                else:
                    curves[i].addKey(times[j], values[i][j], change=change)

    # Sets the value for the indexed blend node.
    # This method sets a single value on the attribute itself, instead of the animation curves.
    # Use this when there is not animation, just a single value.
    def setAttributeValue(self, index, value, change=None):
        plugs = self.animPlugs[index]
        if plugs:
            # We will use an AttributeChange to perform the changes. If none was provided, we will create a provisional one.
            if change == None:
                change = ApiUndo.AttributeChange()

            # Applies the value to the right plug.
            # Rotation blend nodes have 3 value subattributes, so we need to set the right value on each one.
            if self.blendNodeTypes[index] == OpenMaya.MFn.kBlendNodeAdditiveRotation:
                change.performAndRecordChange(plugs[0], value.x)
                change.performAndRecordChange(plugs[1], value.y)
                change.performAndRecordChange(plugs[2], value.z)
            else:
                change.performAndRecordChange(plugs[0], value)


def getAnimCurveForPlug(plug):
    if not plug.isConnected:
        return None
    else:
        connectedPlug = plug.connectedTo(True, False)[0]
        connectedNode = connectedPlug.node()
        if connectedNode.hasFn(OpenMaya.MFn.kAnimCurve):
            return OpenMayaAnim.MFnAnimCurve(connectedNode)

        dependencyNode = OpenMaya.MFnDependencyNode(connectedNode)
        if AnimNodeUtils.isAnimNode(connectedNode, animCurve=False, blendNode=True):
            return getAnimCurveForPlug(dependencyNode.findPlug("inputB", False))

        if connectedNode.hasFn(OpenMaya.MFn.kPairBlend):
            inputPlugName = connectedPlug.partialName(useLongNames=True).replace("out","in")
            inputPlug1 = dependencyNode.findPlug(inputPlugName + "1", False)
            inputPlug2 = dependencyNode.findPlug(inputPlugName + "2", False)

            if inputPlug2.isConnected:
                inputPlugConnectedNode = inputPlug2.connectedTo(True, False)[0].node()
                if inputPlugConnectedNode.hasFn(OpenMaya.MFn.kAnimCurve):
                    return OpenMayaAnim.MFnAnimCurve(inputPlugConnectedNode)

            return getAnimCurveForPlug(inputPlug1)
        
        raise RuntimeError("Attribute is connected to another node's attribute!: {} -> {}".format(plug.name(), dependencyNode.name()))

# Given a list of blend nodes, returns the index where the provided blend node should be based on the attribute they are connected to.
# Returns None if no matching attribute was found.
def getBlendNodeIndex(blendNode, blendNodeList):
    blendNodeAttribute = AnimNodeUtils.getNodeAttributeFromAnimNode(blendNode)
    for i in range(len(blendNodeList)):
        if blendNodeList[i] != None and blendNodeAttribute == AnimNodeUtils.getNodeAttributeFromAnimNode(blendNodeList[i]):
            return i
    return None

# Checks if the provided layer has any unselected children.
# Then recursively checks for each child's children.
def hasUnselectedChildrenLayers(layer, selectedLayers):
    children = set(cmds.animLayer(layer, q=True, children=True) or [])
    if len(children) == 0:
        return False
    elif len(children.intersection(selectedLayers)) != len(children):
        return True
    else:
        for child in children:
            if hasUnselectedChildrenLayers(child, selectedLayers):
                return True
        return False
    
# Checks if the provided layer has any unselected parent.
# Then recursively checks for the parent's parent.
def hasUnselectedParentLayers(layer, selectedLayers):
    parent = cmds.animLayer(layer, q=True, parent=True)
    if parent == None or parent == "" or parent == cmds.animLayer(q=True, root=True):
        return False
    elif parent not in selectedLayers:
        return True
    else:
         return hasUnselectedParentLayers(parent, selectedLayers)

# Merges the selected layers on the Animation Layer interface. The layers will be merged onto the lowest selected layer.
def mergeSelectedLayers():
    selectedLayers = cmds.treeView("AnimLayerTabanimLayerEditor", q=True, selectItem=True)
    if selectedLayers == None or len(selectedLayers) < 2:
        cmds.confirmDialog(t="Merge Layers", m="You must select at least two layers to merge them.")
    else:
        # Checks if any of the layers are muted or locked.
        for layer in selectedLayers:
            if cmds.animLayer(layer, q=True, m=True) or cmds.animLayer(layer, q=True, l=True):
                cmds.confirmDialog(t="Merge Layers", m="Some of the selected layers are muted or locked.")
                return
        
        # Checks if any of the layers have children or parents which are not selected.
        for layer in selectedLayers:
            if not LayerUtils.isBaseLayer(layer) and hasUnselectedChildrenLayers(layer, selectedLayers):
                cmds.confirmDialog(title="Merge Layers", message="Some of the selected layers have children that are not selected. Please select the child layers or unparent them.")
                return
            # Checking for parent layers should be unnecessary
            #if hasUnselectedParentLayers(layer, selectedLayers):
            #    cmds.confirmDialog(title="Merge Layers", message="Some of the selected layers have parents that are not selected. Please select the parent layers or unparent the layers.")
            #    return
            
        mergeLayers(selectedLayers)

# Merges all the layers into the first one on the provided list.
def mergeLayers(layers):
    # Check if the layers are valid
    animLayers = cmds.ls(type="animLayer")
    for layer in layers:
        if layer not in animLayers:
            raise AssertionError("Unable to merge layers: {0} is not a valid layer.".format(layer))
        elif cmds.animLayer(layer, q=True, m=True) or cmds.animLayer(layer, q=True, l=True):
            raise AssertionError("Unable to merge layers: {0} is locked or muted.".format(layer))

    # At least two layers must be provided
    if len(layers) < 2:
        raise AssertionError("Unable to merge layers: At least two layers must be provided.")

    with UndoContext("Quick Layer Merge"):
        # Initializes the change recorders.
        # Operations on the API are recorded into these objects to be able to undo them.
        changes = []

        # Retrieves the blend nodes for all attributes of the objects on the layer for each layer.
        # These are the nodes which the animation curves are connected to, so we will use them to find these curves.
        blendNodesPerLayer = [AnimNodeUtils.getLayerBlendNodes(layers[0], layersToFilterForBaseLayer=layers)]
        for i in range(1, len(layers)):
            layerBlendNodes = AnimNodeUtils.getLayerBlendNodes(layers[i])

            # The blend nodes need to be sorted based on the attribute they are connected to on the layered object.
            # If the blend node is not on any other layer, adds it at the end.
            sortedBlendNodes = [None] * len(blendNodesPerLayer[0])
            for blendNode in layerBlendNodes:
                index = None
                for previousBlendNodes in blendNodesPerLayer:
                    index = getBlendNodeIndex(blendNode, previousBlendNodes)
                    if index != None:
                        break
                if index != None:
                    sortedBlendNodes[index] = blendNode
                else:
                    sortedBlendNodes.append(blendNode)
                    for j in range(len(blendNodesPerLayer)):
                        blendNodesPerLayer[j].append(None)
            blendNodesPerLayer.append(sortedBlendNodes)

        # The first layer will always end having all the merged attributes, so we have to add them to it.
        if not LayerUtils.isBaseLayer(layers[0]):
            for i in range(len(blendNodesPerLayer[0])):
                if blendNodesPerLayer[0][i] == None:
                    for j in range(1, len(blendNodesPerLayer)):
                        if blendNodesPerLayer[j][i] != None:
                            inputPlug = "{0}.inputA".format(blendNodesPerLayer[j][i])
                            nodeAttribute = ".".join(AnimNodeUtils.getNodeAttributeFromAnimNode(blendNodesPerLayer[j][i]))
                            if OpenMayaUtils.getNodeType(blendNodesPerLayer[j][i]) == OpenMaya.MFn.kBlendNodeAdditiveRotation:
                                inputPlug += "X"    # Rotation blend nodes have their output connected to their coordinates. Uses the X one to keep looking for connections. NOTE: This may cause problems if the X coordinate is on a different layer than the other coordinates.
                                nodeAttribute = nodeAttribute[:-1]  # The attribute that will be returned by "getNodeAttributeFromAnimNode" is the rotateX subattribute, we need the rotate parent attribute
                            cmds.animLayer(layers[0], e=True, at=nodeAttribute)
                            blendNodesPerLayer[0][i] = cmds.listConnections(inputPlug, s=True, d=False)[0]
                            break

        # Instead of directly using the list of blend nodes, a custom class is used to encapsulate the list.
        # This class will provide usefull functionality as well as precalculate a lot of information for every blend node on the layer, improving performance.
        layerBlendInfos = []
        for i in range(len(layers)):
            layerBlendInfos.append(LayerBlendInfo(blendNodesPerLayer[i], LayerUtils.isBaseLayer(layers[i])))
        
        # Starts the merging process.
        # For each layer, the blend nodes are registered on the same order, meaning that, for instance, the visibility blend node for the first layer is at the same position as the visibility blend node for the second one.
        # As such, we can iterate through the blend nodes from any of the layers, trusting that an index will allow us to access the blend node for the same attribute on any layer.
        for i in range(len(layerBlendInfos[0].blendNodes)):
            # NOTE: We iterate through the blend nodes first instad of the layers since this will drastically improve the performance, thanks to the precalculated data from the class LayerBlendInfo.
            # Since it might be confusing remember that whenever we are indexing using [i], we are accessing something related to a blend node, not a layer.

            # The merge has three steps:
            # * First collect all the times where there is a key on any of the merged layers.
            # * Then collect and combine the values for each animation curve on the times obtained on the first step.
            # * Lastly, clear all the keys on the lowest layer and create a key with the collected times and values (from the first and second step)

            # Collects the times where there is a key on any of the merged layers.
            # Uses a set to avoid repetitions. The set is later converted to a list and sorted (this shouldn't be necessary, but it's cleaner).
            keyTimes = set()
            for layerBlendInfo in layerBlendInfos:
                # Iterates through the animation curves assigned to the blend node and retrieves their keys.
                # The animation curves where precalculated by the wrapper class LayerBlendInfo.
                for animCurve in layerBlendInfo.animCurves[i]:
                    if animCurve != None:
                        for j in range(animCurve.numKeys):
                            keyTimes.add(animCurve.input(j).asUnits(OpenMaya.MTime.uiUnit()))
            keyTimes = list(keyTimes)
            keyTimes.sort()
            keyTimes = [OpenMaya.MTime(keyTime, OpenMaya.MTime.uiUnit()) for keyTime in keyTimes]

            # It is possible that the attribute is not animated on any of the layers.
            # If that's the case, gets and sets the value using the blend nodes instead of the animation curves.
            if len(keyTimes) == 0:
                # Collects the combined value from each layer on the collected times.
                value = None
                for layerBlendInfo in layerBlendInfos:
                    # The wrapper class LayerBlendInfo provides a "getValue" method which allows to combine values automatically depending on the blend node type.
                    value = layerBlendInfo.getValue(i, OpenMaya.MTime(0, OpenMaya.MTime.uiUnit()), accumulatedValue=value)

                # Creates a recorder for changes on attributes.
                attributeChange = ApiUndo.AttributeChange()
                changes.append(attributeChange)
                
                # Sets the values on the lowest layer.
                layerBlendInfos[0].setAttributeValue(i, value, change=attributeChange)

            else:
                # Creates a recorder for changes on the dependency graph.
                dgChange = OpenMaya.MDGModifier()
                changes.append(dgChange)

                # Since there is animation, we need to make sure there is an animation curve on the lowest layer's blend node.
                # If there isn't, we need to create it.
                layerBlendInfos[0].createAnimCurves(i, change=dgChange)

                # Collects the combined value from each layer on the collected times.
                values = [None] * len(keyTimes)
                for j in range(len(keyTimes)):
                    for layerBlendInfo in layerBlendInfos:
                        # The wrapper class LayerBlendInfo provides a "getValue" method which allows to combine values automatically depending on the blend node type.
                        values[j] = layerBlendInfo.getValue(i, keyTimes[j], accumulatedValue=values[j])

                # Creates a recorder for changes on animation curves.
                curveChange = OpenMayaAnim.MAnimCurveChange()
                changes.append(curveChange)

                # Sets the values on the lowest layer.
                # LayerBlendInfo's "setKeyframes" method takes an array of times and an array of values and uses them to set the keys on the animation curve on one go, improving performance.
                layerBlendInfos[0].setKeyframes(i, keyTimes, values, change=curveChange)

            # Marks the blend node as dirty so the changes to the animation curve may be applied.
            cmds.dgdirty(layerBlendInfos[0].blendNodes[i])

        # Registers the undo command which will be responsible to undo or redo all the operations from the merging.
        undo = ApiUndo.UndoOverwrite(changes)
        undo.commit()

        # If any of the merged layers was on override mode, sets the lowest layer to override mode as well (since it's the layer that will remain).
        # This is only done if the lowest layer is not the base one (since the base layer doesn't have different override modes).
        if not LayerUtils.isBaseLayer(layer[0]):
            for layer in layers:
                if cmds.animLayer(layer, q=True, o=True):
                    cmds.animLayer(layers[0], e=True, o=True)
                    break

        # Finally, deletes the layers.
        for i in range(1, len(layers)):
            cmds.delete(layers[i])
            

if __name__ == "__main__":
    mergeSelectedLayers()