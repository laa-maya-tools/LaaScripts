import maya.cmds as cmds
import maya.mel as mel

import TimeSlider

from Utils.Maya.UndoContext import UndoContext

AnimLayerEditor = "AnimLayerTabanimLayerEditor"

def getBaseLayer():
    return cmds.animLayer(q=True, root=True)

def isBaseLayer(layer):
    return layer == getBaseLayer()

def isOverrideLayer(layer, includeBaseLayer=False):
    if not includeBaseLayer and isBaseLayer(layer):
        return False
    return cmds.animLayer(layer, q=True, override=True)

def isLayerOverriden(layer, layers=None):
    if layers == None:
        layers = getActiveAnimLayers()
    
    animLayers = getAnimLayers()
    layerIndex = animLayers.index(layer)
    for i in range(layerIndex + 1, len(animLayers)):
        l = animLayers[i]
        if isOverrideLayer(l) and l in layers:
            return True
    
    return False

def getAnimLayers(sorted=False):
    if sorted:
        return cmds.treeView(AnimLayerEditor, q=True, children=True) or []
    else:
        return cmds.ls(type="animLayer") or []

def sortAnimLayers(animLayers):
    allLayersSorted = getAnimLayers(sorted=True)
    copy = list(animLayers)
    copy.sort(key=lambda x: allLayersSorted.index(x))
    return copy

def createLayer(layerName, autoRename=True, override=False, parentLayer=None, nodes=None, skipEnumAttributes=False):
    if not autoRename and cmds.animLayer(layerName, q=True, ex=True):
        raise NameError("Unable to create AnimLayer with name [{}]: The name is already in use!".format(layerName))
    
    with UndoContext("Create Anim Layer"):
        kwargs = {}
        if parentLayer:
            kwargs["parent"] = parentLayer
        
        if nodes != None:
            oldSelection = cmds.ls(selection=True)
            cmds.select(nodes)
            
        layerName = cmds.animLayer(layerName, override=override, addSelectedObjects=(nodes != None), excludeBoolean=skipEnumAttributes, excludeEnum=skipEnumAttributes, excludeVisibility=skipEnumAttributes, **kwargs)
        
        if nodes != None:
            cmds.select(oldSelection)
    
    return layerName

def addNodesToLayer(layer, nodes, skipEnumAttributes=True):
    if isBaseLayer(layer):
        cmds.warning("Unable to add nodes to the Base Layer!")
        return
    
    with UndoContext("Add Nodes to Anim Layer"):
        oldSelection = cmds.ls(selection=True)
        
        cmds.select(nodes)
        cmds.animLayer(layer, e=True, addSelectedObjects=True, excludeBoolean=skipEnumAttributes, excludeEnum=skipEnumAttributes, excludeVisibility=skipEnumAttributes)

        cmds.select(oldSelection)

def addAttributeToLayer(plug, layer):
    if isBaseLayer(layer):
        cmds.warning("Unable to add attributes to the Base Layer!")
        return
    
    with UndoContext("Add Attribute to Anim Layer"):
        cmds.animLayer(layer, e=True, at=plug)

def removeNodesFromLayer(layer, nodes):
    if isBaseLayer(layer):
        cmds.warning("Unable to remove nodes from the Base Layer!")
        return
    
    with UndoContext("Remove Nodes from Anim Layer"):
        for node in nodes:
            layeredPlugs = getPlugsOnLayer(layer)
            nodeStr = "{}.".format(node)
            for plug in layeredPlugs:
                if plug.startswith(nodeStr):
                    cmds.animLayer(layer, e=True, ra=plug)
    
def removeAttributeFromLayer(plug, layer):
    if isBaseLayer(layer):
        cmds.warning("Unable to remove attributes from the Base Layer!")
        return
    
    with UndoContext("Remove Attribute from Anim Layer"):
        cmds.animLayer(layer, e=True, ra=plug)

def extractNodesFromLayer(sourceLayer, targetLayer, nodes):
    with UndoContext("Extract Node from Anim Layer"):
        layeredPlugs = getPlugsOnLayer(sourceLayer)
        extractedPlugs = []
        for plug in layeredPlugs:
            for node in nodes:
                nodeStr = "{}.".format(node)
                if plug.startswith(nodeStr):
                    extractedPlugs.append(plug)
                    break
                
        extractAttributesFromLayer(sourceLayer, targetLayer, extractedPlugs)

def extractAttributesFromLayer(sourceLayer, targetLayer, extractedPlugs):
    with UndoContext("Extract Attribute from Anim Layer"):
        # Maya's animLayer extractAnimation doesn't work for specific nodes, so we do the extraction manually
        
        # Step 1: Create a temporal layer and only add the extracted plugs
        temporalLayer = cmds.animLayer("TEMPORAL")
        for plug in extractedPlugs:
            cmds.animLayer(temporalLayer, e=True, at=plug)
        
        # Step 2: Extract the plugs from the source layer to the temporal one. Only shared plugs will be extracted
        cmds.animLayer(temporalLayer, e=True, ea=sourceLayer)
        
        # Step 3: Create the target layer if it doesn't exist and add the plugs to it
        if not cmds.animLayer(targetLayer, q=True, ex=True):
            targetLayer = cmds.animLayer(targetLayer)
        for plug in extractedPlugs:
            cmds.animLayer(targetLayer, e=True, at=plug)
        
        # Step 4: Extract the animation from the temporal layer to the target one
        cmds.animLayer(targetLayer, e=True, ea=temporalLayer)

        # Step 5: Finally, delete the temporal layer (it should be empty by now)
        cmds.delete(temporalLayer)

def getSelectedAnimLayers(ignoreBaseLayer=False):
    animLayers = getAnimLayers()
    baseLayer = getBaseLayer()
    return [animLayer for animLayer in animLayers if cmds.animLayer(animLayer, q=True, selected=True) and (not ignoreBaseLayer or animLayer != baseLayer)]

def setSelectedAnimLayers(selectedAnimLayers, refreshUI=True):
    animLayers = getAnimLayers()
    for animLayer in animLayers:
        cmds.animLayer(animLayer, e=True, preferred=False, selected=animLayer in selectedAnimLayers)
    
    cmds.animLayer(selectedAnimLayers[0] if selectedAnimLayers else getBaseLayer(), e=True, preferred=True)
        
    if refreshUI:
        forceAnimLayerUIUpdate()

def getActiveAnimLayers(objects=None):
    if objects == None:
        objects = cmds.ls(selection=True) or []
    return cmds.animLayer(objects, q=True, bestAnimLayer=True) or []

def getEnabledAnimLayers():
    animLayers = getAnimLayers()
    return [animLayer for animLayer in animLayers if not cmds.animLayer(animLayer, q=True, m=True)]

def setEnabledAnimLayers(enabledLayers):
    animLayers = getAnimLayers()
    enabledLayers.append(getBaseLayer())
    for animLayer in animLayers:
        shouldBeMuted = animLayer not in enabledLayers
        if cmds.animLayer(animLayer, q=True, m=True) != shouldBeMuted:
            cmds.animLayer(animLayer, e=True, m=shouldBeMuted, l=shouldBeMuted)    

def getDisplayedAnimLayers(objects=None):
    displayedLayers = set()
    displayOption = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, animLayerFilterOptions=True)

    if displayOption == "selected" or displayOption == "activeAndSelected":
        displayedLayers.update(getSelectedAnimLayers())

    if displayOption == "active" or displayOption == "activeAndSelected":
        displayedLayers.update(getActiveAnimLayers(objects))

    if displayOption == "allAffecting" or displayOption == "animLayerEditor":
        displayedLayers.update(getAnimLayers())

    return displayedLayers

def getPlugsOnLayer(layer):
    return cmds.animLayer(layer, q=True, at=True) or []

def getBestAnimLayerForPlug(plug):
    bestAnimLayers = mel.eval("animLayer -at {} -q -bestAnimLayer".format(plug)) or [] # The animLayer command doesn't seem to work properly on cmds with the "at" flag
    if len(bestAnimLayers) > 0:
        return bestAnimLayers[0]
    else:
        return None
    
def getAffectedLayersForAttribute(plug):
    return mel.eval("animLayer -at {} -q -affectedLayers".format(plug)) or [] # The animLayer command doesn't seem to work properly on cmds with the "at" flag

def getAnimLayerPlugForAttribute(plug, layer=None):
    # If no layer is specified, use the preferred one
    if layer == None:
        layer = getBestAnimLayerForPlug(plug)
        if layer == None:
            # The plug has no layers, so return the plug itself
            return plug
        
    if layer == getBaseLayer():
        # The flag layeredPlug doesn't seem to work properly.
        # Instead, we retrieve the plug layers, then find the first one (aside from the base one).
        # From this layer's layeredPlug's blend node we take the inputA plug (which is the base layer's plug).
        affectedAnimLayers = getAffectedLayersForAttribute(plug)
        if len(affectedAnimLayers) <= 1:
            return plug # The plug doesn't actually have layers, so the layeredPlug is the plug itself.
        else:
            otherLayeredPlug = cmds.animLayer(affectedAnimLayers[-2], q=True, layeredPlug=plug)
            if otherLayeredPlug.endswith("inputB"):
                otherLayeredPlug = otherLayeredPlug[:-1] + "A"  # The returned plug should be "inputB", we need the "inputA"
            else:
                otherLayeredPlug = otherLayeredPlug[:-2] + "A" + otherLayeredPlug[-1]  # The returned plug should be "inputBX", we need the "inputAX"
            return otherLayeredPlug
        
    else:
        return cmds.animLayer(layer, q=True, layeredPlug=plug)

def getAnimCurveForAttribute(plug, layer=None):
    animLayerPlug = getAnimLayerPlugForAttribute(plug, layer=layer)
    if animLayerPlug:
        connectedAnimCurves = cmds.listConnections(animLayerPlug, s=True, d=False, type="animCurve")
        if connectedAnimCurves:
            return connectedAnimCurves[0]
    return None

def forceAnimLayerUIUpdate():
    # Función castaña porque a menudo Maya no se entera ni en 50 años de que has hecho algún cambio en las capas.
    mel.eval("\
        updateEditorFeedbackAnimLayers(\"AnimLayerTab\");\
        onAnimLayersAnimationChanged(\"AnimLayerTab\");\
        onAnimLayersLockChanged(\"AnimLayerTab\");\
        doUpdateTangentFeedback;\
        timeField -edit -value `currentTime -query` TimeSlider|MainTimeSliderLayout|formLayout8|timeField1;\
    ")
