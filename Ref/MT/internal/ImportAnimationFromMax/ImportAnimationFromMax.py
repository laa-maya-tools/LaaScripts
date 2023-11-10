# coding: utf-8
from PySide2 import QtWidgets

import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaAnim as OpenMayaAnim
import maya.cmds as cmds

import Utils.OpenMaya as OpenMayaUtils
import Utils.Maya.AnimLayers as AnimLayerUtils
import MGearExtended.IKFKMatch as IKFKMatch
import ActorManager
import ProjectPath
import Batcher
import AnimSystems

import xml.etree.ElementTree as XML
import math
import os
import re

import logging
logger = logging.getLogger(__name__)

positionComponents = ["PositionX", "PositionY", "PositionZ"]
rotationComponents = ["RotationX", "RotationY", "RotationZ"]
scaleComponents = ["ScaleX", "ScaleY", "ScaleZ"]

class CharacterAnimation():
    
    def __init__(self, characterName, namespace=None):
        self.characterName = characterName
        self.namespace = namespace

        self.nodes = []
        self.layerAnimations = []
        self.animPresets = []
        self.parameters = []
        
        self.ikLimbs = []

    @staticmethod
    def listNodes(collection, removeMissing):
        nodes = set()

        for item in collection:
            nodes.update(item.getAffectedNodes(removeMissing=False))

        if removeMissing:
            existingNodes = set()
            for node in nodes:
                if node.nodeExists():
                    existingNodes.add(node)
            nodes = existingNodes

        return nodes

    def getAffectedNodes(self, removeMissing=False):
        return CharacterAnimation.listNodes(self.layerAnimations, removeMissing)

    def updateIKLimbs(self):
        self.ikLimbs = IKLimb.getIKLimbsFromNodes(self.nodes, self.namespace)

    def applyAnimation(self):
        # Change dafault tangent type to spline to reduce tangent changes.
        # Spline is the same as biped's TCB with default values, making it the most common tangent type.
        defaultInTangentType = cmds.keyTangent(q=True, g=True, inTangentType=True)[0]
        defaultOutTangentType = cmds.keyTangent(q=True, g=True, outTangentType=True)[0]
        cmds.keyTangent(e=True, g=True, inTangentType="spline")
        cmds.keyTangent(e=True, g=True, outTangentType="spline")

        # Enables auto-keyframe
        wasAutoKeyframeEnabled = cmds.autoKeyframe(q=True, state=True)
        cmds.autoKeyframe(state=True)
        
        # Sets Hybrid keying mode
        animLayerSelectionKeyMode = cmds.optionVar(q="animLayerSelectionKey")
        cmds.optionVar(iv=("animLayerSelectionKey", 1))
        
        # Disables the animation systems
        wereAnimSystemsCallbacksEnabled = AnimSystems.AnimSystemsCallbackManager._callbacksEnabled
        AnimSystems.AnimSystemsCallbackManager._callbacksEnabled = False

        try:
            # Links the DC's and Props to the same node they were linked to on max.
            logger.info("Reparenting Nodes...")
            for node in self.nodes:
                node.performReparent()

            # Stores the default transformation of each node. It asumes the character is on T pose.
            for node in self.nodes:
                node.storeBasePose()
                
            # Applies the base transformation for each node.
            cmds.currentTime(0, e=True) # The baseTransform were taken on frame 0
            for node in self.nodes:
                if node.baseTransform != None:
                    node.baseTransform.applyAnimation()
            
            # Applies the animation for each parameter.
            # This is performed before applying the animation just in case the animation depends on them.
            logger.info("Applying Parameters Animation...")
            for parameter in self.parameters:
                parameter.applyParameterAnimation()

            # Nodes that should be on each layer. Includes the IK limbs' nodes.
            nodesInLayer = self.getAffectedNodes(removeMissing=True)
            for ikLimb in self.ikLimbs.values():
                nodesInLayer.update(ikLimb.getAffectedNodes(removeMissing=True))

            # Deletes all the layers if they exist. The layers will be created anew.
            logger.info("Deleting Existing Animation Layers...")
            animLayers = cmds.ls(type="animLayer") or []
            for layer in animLayers:
                if layer != "BaseAnimation":
                    cmds.delete(layer)

            # Applies the animation for each layer.
            for i, layerAnim in enumerate(self.layerAnimations):
                logger.info("Applying Animation to Layer [{} ({}/{})]...".format(layerAnim.layerName, i+1, len(self.layerAnimations)), extra={"color":"white"})
                layerAnim.applyAnimation(self.layerAnimations, self.animPresets, nodesInLayer=nodesInLayer, ikLimbs=self.ikLimbs)

            # Sets the IK state for all the limbs. The IK state is set on the first layer only.
            logger.info("Applying IK Configuration...")
            if len(self.layerAnimations) > 1:
                for layer in self.layerAnimations:
                    cmds.animLayer(layer.layerName, e=True, preferred=(layer == self.layerAnimations[0]))
            previousIKLimbsState = {}
            for animationPosture in self.layerAnimations[0].animationPostures:
                previousIKLimbsState = animationPosture.setIKState(self.ikLimbs, previousIKLimbsState)

            # Creates all the anim presets
            if len(self.animPresets) > 0:
                logger.info("Creating AnimPresets...")
                if self.namespace == None:
                    logger.warning("No namespace was specified! Unable to create AnimPrests.")
                else:
                    actor = ActorManager.getActorByNameSpace(self.namespace)
                    if actor == None:
                        logger.warning("Couldn't find namespace {}! Unable to create AnimPrests.".format(self.namespace))
                    else:
                        for animPreset in self.animPresets:
                            animPreset.createAnimPreset(actor)
                        
        finally:
            # Restores the default tangent type.
            cmds.keyTangent(e=True, g=True, inTangentType=defaultInTangentType)
            cmds.keyTangent(e=True, g=True, outTangentType=defaultOutTangentType)

            # Restores the keying mode
            cmds.optionVar(iv=("animLayerSelectionKey", animLayerSelectionKeyMode))
            
            # Restores the auto-keyframe state
            cmds.autoKeyframe(state=wasAutoKeyframeEnabled)
            
            # Restores the animation systems
            OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
            AnimSystems.AnimSystemsCallbackManager._callbacksEnabled = wereAnimSystemsCallbacksEnabled

class AnimPresetInfo():
    
    def __init__(self):
        self.nameParts = []
        self.path = ""
        self.enabled = True
        self.start = 0
        self.end = 0
        self.pose = False
        self.loop = False
        self.color = [0, 0, 0]
        self.activeLayers = []
        
    def setActiveLayers(self, layers):
        self.activeLayers = [layer.replace(" ", "_") for layer in layers]

    def createAnimPreset(self, actor):
        pathTokenizer = actor.animSubActor.getPathTokenizer(branch=None)
        pathTokenizer.Update({ ProjectPath.Tokens.TPrjBranch : "@\\game" })

        animPreset = actor.createAnimPreset()

        animPreset.setNameParts(self.nameParts)
        animPreset.path = pathTokenizer.Tokenize(self.path)
        animPreset.enabled = self.enabled
        animPreset.start = self.start
        animPreset.end = self.end
        animPreset.pose = self.pose
        animPreset.loop = self.loop
        animPreset.color = self.color

        for activeLayer in self.activeLayers:
            if activeLayer != "Original":
                animPreset.addAnimLayer(activeLayer)
                
    def updateAnimLayerName(self, oldLayerName, newLayerName):
        if oldLayerName in self.activeLayers:
            self.activeLayers[self.activeLayers.index(oldLayerName)] = newLayerName

class IKLimb():

    @staticmethod
    def getIKLimbsFromNodes(nodes, namespace):
        if namespace == None:
            namespace = ""
        elif namespace != "":
            namespace = "{}:".format(namespace)
        
        regexString = "^{namespace}(arm|leg)_(R|L)([0-9]+)_fk[0-9]+_ctl$".format(namespace=namespace)
        regex = re.compile(regexString)
        
        ikLimbs = {}
        for node in nodes:
            if type(node) == CharacterNode:
                node = node.node
            match = regex.match(node)
            if match:
                limb = match.group(1)
                side = match.group(2)
                key = "{}{}".format(limb, side)
                if key not in ikLimbs:
                    number = match.group(3)
                    ikLimbs[key] = IKLimb(namespace, limb, side, number)
                    
        return ikLimbs

    @staticmethod
    def copyTangent(sourcePlug, target, time=None):
        if time == None:
            time = cmds.currentTime(q=True)
        inTangentType = cmds.keyTangent(sourcePlug, q=True, inTangentType=True, time=(time, time))[0]
        outTangentType = cmds.keyTangent(sourcePlug, q=True, outTangentType=True, time=(time, time))[0]
        # No support for custom tangents...
        if inTangentType == "fixed":
            inTangentType = "spline"
        if outTangentType == "fixed":
            outTangentType = "spline"
        cmds.setKeyframe(target, inTangentType=inTangentType, outTangentType=outTangentType)

    def __init__(self, namespace, limb, side, number):
        self.namespace = namespace
        self.limb = limb
        self.side = side
        self.number = number

        self.characterRoot = "{}rig".format(namespace)
        self.switchControl = "{}{}UI_{}{}_ctl".format(namespace, limb, side, number)
        self.switchAttribute = "{}_blend".format(limb)
        self.ikControl = "{}{}_{}{}_ik_ctl".format(namespace, limb, side, number)
        self.ikUpVectorControl = "{}{}_{}{}_upv_ctl".format(namespace, limb, side, number)
        self.fkControls = ["{}{}_{}{}_fk{}_ctl".format(namespace, limb, side, number, i) for i in range(3)]
        self.ikControls = [self.ikControl, self.ikUpVectorControl]

    # Returns the nodes that are affected by this IK limb as instances of CharacterNode.
    # These instances are not configured to import animation into them and should not be used this way.
    def getAffectedNodes(self, removeMissing=False):
        nodes = set()

        nodes.add(CharacterNode(self.switchControl))
        nodes.add(CharacterNode(self.ikControl))
        nodes.add(CharacterNode(self.ikUpVectorControl))

        if removeMissing:
            existingNodes = set()
            for node in nodes:
                if node.nodeExists():
                    existingNodes.add(node)
            nodes = existingNodes

        return nodes

    def setIKState(self, state, time=None):
        if time == None:
            time = cmds.currentTime(q=True)
        ikPlug = "{}.{}".format(self.switchControl, self.switchAttribute)
        cmds.setKeyframe(ikPlug, v=state, time=time)
        tangent = "stepnext" if state > 0 else "step"
        cmds.keyTangent(ikPlug, e=True, ott=tangent, time=(time, time))

    def modifyIKToMatchFK(self, copyTangent=True):
        if copyTangent:
            self.copyTangent("{}.rotateX".format(self.fkControls[0]), self.ikControls)
        IKFKMatch.ikMatchFk(self.characterRoot, self.switchAttribute, self.switchControl, self.fkControls, self.ikControl, self.ikUpVectorControl)

    def modifyFKToMatchIK(self, copyTangent=True):
        if copyTangent:
            self.copyTangent("{}.translateX".format(self.ikControl), self.fkControls)
        IKFKMatch.fkMatchIk(self.characterRoot, self.switchAttribute, self.switchControl, self.fkControls, self.ikControl, self.ikUpVectorControl)

class CharacterNode():
    
    def __init__(self, node, parent=None, rotationParent=None, reparent=False, exportPosition=False, exportRotation=True, exportScale=False, baseTransform=None):
        self.node = node
        self.parent = parent
        self.rotationParent = rotationParent
        self.reparent = reparent
        
        self.exportPosition = exportPosition
        self.exportRotation = exportRotation
        self.exportScale = exportScale
        
        self.baseTransform = baseTransform
        
        self.basePosePosition = None
        self.basePoseRotation = None
        self.basePoseScale = None
        
        self.resetKeyframeFlags()

    def resetKeyframeFlags(self):
        self.keyPosSet = [False, False, False]
        self.keyRotSet = [False, False, False]
        self.keyScaSet = [False, False, False]

    def performReparent(self):
        if self.reparent:
            if self.parent != None and not cmds.objExists(self.parent):
                logger.error("ERROR: Unable to find the node {} while attempting to reparent {}".format(self.parent, self.node))
                return
            if self.rotationParent != None and not cmds.objExists(self.rotationParent):
                logger.error("ERROR: Unable to find the node {} while attempting to reparent {}".format(self.rotationParent, self.node))
                return

            separateRotation = self.rotationParent != self.parent
            constraintNode = "{}_parentCns".format(self.node)
            if not cmds.objExists(constraintNode):
                logger.error("ERROR: Unable to find the node {} while attempting to reparent {}".format(constraintNode, self.node))
                return

            if self.parent != None:
                targets = cmds.parentConstraint(constraintNode, q=True, targetList=True) or []
                if self.parent not in targets:
                    if not separateRotation:
                        cmds.parentConstraint(self.parent, constraintNode, maintainOffset=False)
                    else:
                        cmds.parentConstraint(self.parent, constraintNode, maintainOffset=False, skipRotate=["x","y","z"])
                for target in targets:
                    cmds.parentConstraint(target, constraintNode, e=True, weight=(1 if target == self.parent else 0))

            if self.rotationParent != None and separateRotation:
                targets = cmds.orientConstraint(constraintNode, q=True, targetList=True) or []
                if self.rotationParent not in targets:
                    cmds.orientConstraint(self.rotationParent, constraintNode, maintainOffset=False)
                for target in targets:
                    cmds.orientConstraint(target, constraintNode, e=True, weight=(1 if target == self.rotationParent else 0))

    def nodeExists(self):
        return cmds.objExists(self.node)

    def storeBasePose(self):
        if self.nodeExists():
            sl = OpenMaya.MSelectionList()
            sl.add(self.node)
            nodeDagPath = sl.getDagPath(0)
            worldMatrix = nodeDagPath.inclusiveMatrix()
            worldMatrixForRotation = nodeDagPath.inclusiveMatrix()

            if self.parent != None and cmds.objExists(self.parent):
                sl.add(self.parent)
                parentDagPath = sl.getDagPath(sl.length() - 1)
                parentWorldMatrix = parentDagPath.inclusiveMatrix()
                worldMatrix = worldMatrix * parentWorldMatrix.inverse()

            if self.rotationParent != None and cmds.objExists(self.rotationParent):
                sl.add(self.rotationParent)
                rotationParentDagPath = sl.getDagPath(sl.length() - 1)
                rotationParentWorldMatrix = rotationParentDagPath.inclusiveMatrix()
                worldMatrixForRotation = worldMatrixForRotation * rotationParentWorldMatrix.inverse()

            nodeTransform = OpenMaya.MTransformationMatrix(worldMatrix)
            nodeTransformForRotation = OpenMaya.MTransformationMatrix(worldMatrixForRotation)

            if self.exportPosition:
                nodeTranslation = nodeTransform.translation(OpenMaya.MSpace.kObject)
                self.basePosePosition = nodeTranslation

            if self.exportRotation:
                nodeRotation = nodeTransformForRotation.rotation(asQuaternion=True)
                self.basePoseRotation = nodeRotation

            if self.exportScale:
                nodeScale = nodeTransform.scale(OpenMaya.MSpace.kObject)
                self.basePoseScale = nodeScale

class Parameter():
    
    def __init__(self, attribute, namespace=None):
        if namespace != None:
            attribute = "{}:{}".format(namespace, attribute)
        self.attribute = attribute
        
        self.beforeOutOfRangeType = None
        self.afterOutOfRangeType = None
        
        self.keyframeData = []
        
    def applyParameterAnimation(self):
        if not cmds.objExists(self.attribute):
            logger.warning("Couldn't find attribute to apply parameter: {}".format(self.attribute))
            return
        
        for time, value, tangent in self.keyframeData:
            cmds.setKeyframe(self.attribute, time=time, value=value)
            if tangent != None:
                tangent.applyTangent(self.attribute, time)
                
        if self.beforeOutOfRangeType:
            start = OutOfRangeType.mayaTypes[OutOfRangeType.maxTypes.index(self.beforeOutOfRangeType)]
        else:
            start = OutOfRangeType.mayaTypes[0]
        if self.afterOutOfRangeType:
            end = OutOfRangeType.mayaTypes[OutOfRangeType.maxTypes.index(self.afterOutOfRangeType)]
        else:
            end = OutOfRangeType.mayaTypes[0]
        cmds.setInfinity(self.attribute, preInfinite=start, postInfinite=end)

class LayerAnimation():
    
    def __init__(self, layerName):
        self.layerName = layerName.replace(" ", "_")

        self.isBaseLayer = self.layerName == "Original"
        if self.isBaseLayer:
            self.layerName = cmds.animLayer(q=True, r=True) or "BaseAnimation"

        self.requiredLayers = None
        self.outOfRangeTypes = None
        self.animationPostures = []

    def setRequiredLayers(self, requiredLayers):
        if requiredLayers == None:
            self.requiredLayers = None
        else:
            self.requiredLayers = []
            for layer in requiredLayers:
                if layer != "Original":
                    self.requiredLayers.append(layer.replace(" ", "_"))
                
    def updateAnimLayerName(self, oldLayerName, newLayerName):
        if self.requiredLayers != None and oldLayerName in self.requiredLayers:
            self.requiredLayers[self.requiredLayers.index(oldLayerName)] = newLayerName

    def getAffectedNodes(self, removeMissing=False):
        return CharacterAnimation.listNodes(self.animationPostures, removeMissing)
        
    def applyAnimation(self, layerAnimations, animPresets, nodesInLayer=None, ikLimbs=None, eulerFilter=True):
        layerNodes = self.getAffectedNodes(removeMissing=True)
        if nodesInLayer == None:
            nodesInLayer = layerNodes

        if not self.isBaseLayer:
            # Some layers started with a number on Max. Maya doesn't allow it, so preppend a string to the layer name in that case.
            newLayerName = self.layerName
            if not self.layerName[0].isalpha():
                newLayerName = "animLayer" + newLayerName
            
            # There might be a node that already is named like the layer, so we remember the name Maya gives us
            nodesToSelect = [node.node for node in nodesInLayer]
            newLayerName = AnimLayerUtils.createLayer(newLayerName, nodes=nodesToSelect, skipEnumAttributes=True)
            if newLayerName != self.layerName:
                for animPreset in animPresets:
                    animPreset.updateAnimLayerName(self.layerName, newLayerName)
                for layerAnimation in layerAnimations:
                    layerAnimation.updateAnimLayerName(self.layerName, newLayerName)
                self.layerName = newLayerName
                
            cmds.animLayer(self.layerName, e=True, preferred=True, mute=False)
            cmds.setAttr("{}.rotationAccumulationMode".format(self.layerName), 1)

        if self.requiredLayers != None:
            for requiredLayer in self.requiredLayers:
                cmds.animLayer(requiredLayer, e=True, mute=False)
            
        for node in layerNodes:
            node.resetKeyframeFlags()

        logger.info("Applying Postures...")
        for animationPosture in self.animationPostures:
            animationPosture.applyAnimation()

        if eulerFilter:
            logger.info("Applying Euler Filter for FK...")
            for node in layerNodes:
                if node.exportRotation:
                    # There is a bug when applying Euler filter to an object with an unkeyed component on the last frame.
                    # Forces all the rotation component to be keyed on the last frame to avoid it.
                    lastTime = cmds.currentTime(q=True) + 1   # This variable actually hold the last frame plus one, so the findKeyframe with the "previous" option finds the last key
                    lastKeyTime = cmds.findKeyframe(node.node, at=["rotate"], which="previous", time=(lastTime, lastTime))
                    if lastKeyTime < lastTime: # If there are no keys on the object, findKeyframe will return the provided time. In this case, we don't need to do anything.
                        cmds.setKeyframe("{}.rotate".format(node.node), time=lastKeyTime)
                cmds.filterCurve(node.node, filter="euler")

        if ikLimbs != None:
            logger.info("Snapping IK Limbs...")
            for animationPosture in self.animationPostures:
                animationPosture.snapIK(ikLimbs)
                
        if eulerFilter:
            logger.info("Applying Euler Filter for IK...")
            for ikLimb in ikLimbs.values():
                nodes = ikLimb.getAffectedNodes()
                for node in nodes:
                    cmds.filterCurve(node.node, filter="euler")
                
        if self.outOfRangeTypes != None and len(self.outOfRangeTypes) > 0:
            logger.info("Applying Curve Infinities...")
            for outOfRangeType in self.outOfRangeTypes:
                outOfRangeType.applyOutOfRangeType()

        if not self.isBaseLayer:
            cmds.animLayer(self.layerName, e=True, mute=True)

        if self.requiredLayers != None:
            for requiredLayer in self.requiredLayers:
                cmds.animLayer(requiredLayer, e=True, mute=True)

class OutOfRangeType():
    
    maxTypes = ["constant", "linear", "cycle", "loop", "relativeRepeat", "pingPong"]
    mayaTypes = ["constant", "linear", "cycle", "cycle", "cycleRelative", "oscillate"]
    attributes = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scale"]
    
    def __init__(self, characterNode):
        self.characterNode = characterNode
        
        self.types = {}
        
    def applyOutOfRangeType(self):
        if self.characterNode.nodeExists():
            for attr, type in self.types.items():
                cmds.setInfinity(self.characterNode.node, at=attr, preInfinite=type[0], postInfinite=type[1])
        
    @classmethod
    def fromXml(cls, xmlORT, characterNodes, namespace=None):
        nodeName = xmlORT.get("nodeName")
        if namespace != None:
            nodeName = "{}:{}".format(namespace, nodeName)
        characterNode = None
        for charNode in characterNodes:
            if charNode.node == nodeName:
                characterNode = charNode
                break
            
        ort = OutOfRangeType(characterNode)
        
        for attr in cls.attributes:
            capitalizedAttr = attr[0].upper() + attr[1:]
            start = xmlORT.get("start{}".format(capitalizedAttr))
            end = xmlORT.get("end{}".format(capitalizedAttr))
            if start or end:
                if start:
                    start = cls.mayaTypes[cls.maxTypes.index(start)]
                else:
                    start = cls.mayaTypes[0]
                if end:
                    end = cls.mayaTypes[cls.maxTypes.index(end)]
                else:
                    end = cls.mayaTypes[0]
                ort.types[attr] = (start, end)
        
        return ort

class AnimationPosture():
    def __init__(self, time, rightArmIK=None, leftArmIk=None, rightLegIK=None, leftLegIK=None):
        self.time = time

        self.ikStates = {}
        self.ikStates["armR"] = rightArmIK
        self.ikStates["armL"] = leftArmIk
        self.ikStates["legR"] = rightLegIK
        self.ikStates["legL"] = leftLegIK

        self.nodeTransforms = []

    def getAffectedNodes(self, removeMissing=False):
        return CharacterAnimation.listNodes(self.nodeTransforms, removeMissing)

    def applyAnimation(self):
        cmds.currentTime(self.time, e=True)
        for nodeTrf in self.nodeTransforms:
            nodeTrf.applyAnimation()

    def snapIK(self, ikLimbs, changeTime=True, force=True):
        if changeTime:
            cmds.currentTime(self.time, e=True)

        for ikLimb in ikLimbs.keys():
            state = self.ikStates[ikLimb]
            if state != None:
                if force or (state > 0):  # The "force" parameter indicates that the IK must be matched even if the limb is set to FK.
                    ikLimbs[ikLimb].modifyIKToMatchFK()

    def setIKState(self, ikLimbs, previousIKLimbsState={}, force=True):
        for ikLimb in ikLimbs.keys():
            state = self.ikStates[ikLimb]
            if state != None:
                previousState = previousIKLimbsState[ikLimb] if not force and ikLimb in previousIKLimbsState else None  # The "force" parameter indicates that IK/FK blend weight must be keyed even if the IK state has not changed.
                if previousState == None or state != previousState:
                    ikLimbs[ikLimb].setIKState(state, time=self.time)
                previousIKLimbsState[ikLimb] = state

        return previousIKLimbsState

class NodeTransform():
    def __init__(self, characterNode):
        self.characterNode = characterNode
        
        self.position = [None, None, None]
        self.rotation = [None, None, None]
        self.scale = [None, None, None]

        self.positionTangent = [None, None, None]
        self.rotationTangent = [None, None, None]
        self.scaleTangent = [None, None, None]

        self.positionKeyed = [False, False, False]
        self.rotationKeyed = [False, False, False]
        self.scaleKeyed = [False, False, False]

    def getAffectedNodes(self, removeMissing=False):
        nodes = set()
        if not removeMissing or self.characterNode.nodeExists():
            nodes.add(self.characterNode)
        return nodes

    def applyAnimation(self):
        if self.characterNode.nodeExists():
            if self.characterNode.exportPosition and self.position[0] != None:  # La posición vendrá con los tres componentes o con ninguno (si viene sin ningundo significa que no hay clave en ningún eje, se puede ignorar).
                position = OpenMaya.MVector(self.position)
                if self.characterNode.rotationParent is not None and self.characterNode.basePoseRotation is not None:
                    position = position.rotateBy(self.characterNode.basePoseRotation.inverse())
                if self.characterNode.basePosePosition is not None:
                    position -= self.characterNode.basePosePosition
                self.characterNode.keyPosSet = self.applyPosition(self.characterNode.node, position, self.positionKeyed, self.positionTangent, self.characterNode.keyPosSet)
            
            if self.characterNode.exportRotation and self.rotation[0] != None:  # La rotación vendrá con los tres componentes o con ninguno (si viene sin ningundo significa que no hay clave en ningún eje, se puede ignorar).
                rotation = OpenMaya.MEulerRotation(math.radians(self.rotation[0]), math.radians(self.rotation[1]), math.radians(self.rotation[2])).asQuaternion()
                if self.characterNode.basePoseRotation is not None:
                    rotation = rotation * self.characterNode.basePoseRotation.inverse()
                self.characterNode.keyRotSet = self.applyRotation(self.characterNode.node, rotation, self.rotationKeyed, self.rotationTangent, self.characterNode.keyRotSet)
            
            if self.characterNode.exportScale:
                scale = self.scale
                if self.characterNode.basePoseScale is not None:
                    scale = [scale[i] - self.characterNode.basePoseScale[i] for i in range(3)]
                self.characterNode.keyScaSet = self.applyScale(self.characterNode.node, scale, self.scaleKeyed, self.scaleTangent, self.characterNode.keyScaSet)
    
    def applyTransformComponent(self, attr, fn, node, value, keyedComponents, tangents, keySet):
        if True not in keyedComponents:
            return keySet
        
        currentTime = cmds.currentTime(q=True)
        
        cmds.setKeyframe("{}.{}".format(node, attr))  # We set a keyframe here regardless of the keyset parameter since it was creating problems when the values didn't changed.
        for i, coord in enumerate(["X", "Y", "Z"]):
            if keyedComponents[i]:
                plug = "{}.{}{}".format(node, attr, coord)
                if tangents[i] != None:
                    tangents[i].applyTangent(plug, currentTime)
        
        fn(value, OpenMaya.MSpace.kTransform)
        cmds.setKeyframe("{}.{}".format(node, attr))    # If we don't set key here AGAIN sometimes the transformation will not be saved :3
        
        for i, coord in enumerate(["X", "Y", "Z"]):
            if not keyedComponents[i]:
                cmds.cutKey(node, at="{}{}".format(attr, coord), t=(currentTime, currentTime), cl=True)
        
        return [keySet[i] or keyedComponents[i] for i in range(3)]

    def applyPosition(self, node, value, keyedComponents, tangents, keySet):
        nodeTransform = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(node))
        return self.applyTransformComponent("translate", nodeTransform.setTranslation, node, value, keyedComponents, tangents, keySet)

    def applyRotation(self, node, value, keyedComponents, tangents, keySet):
        nodeTransform = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(node))
        return self.applyTransformComponent("rotate", nodeTransform.setRotation, node, value, keyedComponents, tangents, keySet)

    def applyScale(self, node, value, keyedComponents, tangents, keySet):
        nodeTransform = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(node))
        return self.applyTransformComponent("scale", nodeTransform.setScale, node, value, keyedComponents, tangents, keySet)

    @classmethod
    def fromXml(cls, xmlNodeTrf, characterNode=None, characterNodes=None, namespace=None):
        if characterNode == None:
            nodeName = xmlNodeTrf.get("nodeName")
            if namespace != None:
                nodeName = "{}:{}".format(namespace, nodeName)
            for charNode in characterNodes:
                if charNode.node == nodeName:
                    characterNode = charNode
                    break

        nodeTrf = NodeTransform(characterNode)

        if characterNode.exportPosition:
            for i in range(3):
                xmlComponent = xmlNodeTrf.find(positionComponents[i])
                if xmlComponent != None:
                    nodeTrf.position[i] = parseFloatOrNone(xmlComponent.text)
                    nodeTrf.positionKeyed[i] = parseBool(xmlComponent.get("keyed"))
                    inTangentType = xmlComponent.get("inTangentType")
                    if inTangentType != None:
                        nodeTrf.positionTangent[i] = KeyTangent(inTangentType, xmlComponent.get("outTangentType"), parseFloatOrNone(xmlComponent.get("inTangent")), parseFloatOrNone(xmlComponent.get("outTangent")), parseFloatOrNone(xmlComponent.get("inTangentLength")), parseFloatOrNone(xmlComponent.get("outTangentLength")))
        if characterNode.exportRotation:
            for i in range(3):
                xmlComponent = xmlNodeTrf.find(rotationComponents[i])
                if xmlComponent != None:
                    nodeTrf.rotation[i] = parseFloatOrNone(xmlComponent.text)
                    nodeTrf.rotationKeyed[i] = parseBool(xmlComponent.get("keyed"))
                    inTangentType = xmlComponent.get("inTangentType")
                    if inTangentType != None:
                        nodeTrf.rotationTangent[i] = KeyTangent(inTangentType, xmlComponent.get("outTangentType"), parseFloatOrNone(xmlComponent.get("inTangent")), parseFloatOrNone(xmlComponent.get("outTangent")), parseFloatOrNone(xmlComponent.get("inTangentLength")), parseFloatOrNone(xmlComponent.get("outTangentLength")))
        if characterNode.exportScale:
            for i in range(3):
                xmlComponent = xmlNodeTrf.find(scaleComponents[i])
                if xmlComponent != None:
                    nodeTrf.scale[i] = parseFloatOrNone(xmlComponent.text)
                    nodeTrf.scaleKeyed[i] = parseBool(xmlComponent.get("keyed"))
                    inTangentType = xmlComponent.get("inTangentType")
                    if inTangentType != None:
                        nodeTrf.scaleTangent[i] = KeyTangent(inTangentType, xmlComponent.get("outTangentType"), parseFloatOrNone(xmlComponent.get("inTangent")), parseFloatOrNone(xmlComponent.get("outTangent")), parseFloatOrNone(xmlComponent.get("inTangentLength")), parseFloatOrNone(xmlComponent.get("outTangentLength")))

        return nodeTrf

class KeyTangent():

    tangentTypes = ["spline", "linear", "fast", "slow", "flat", "step", "stepnext", "fixed", "clamped", "plateau", "auto"]

    splineTangentType = tangentTypes.index("spline")
    fixedTangentType = tangentTypes.index("fixed")

    def __init__(self, inTangentType, outTangentType, inTangent, outTangent, inTangentLength, outTangentLength):
        self.inTangentType = self.convertTangentType(inTangentType)
        self.outTangentType = self.convertTangentType(outTangentType)
        self.inTangent = inTangent
        self.outTangent = outTangent
        self.inTangentLength = inTangentLength
        self.outTangentLength = outTangentLength

    def convertTangentType(self, tangentType):
        if tangentType[0] == "#":
            tangentType = tangentType[1:]

        if tangentType == "smooth":
            return KeyTangent.splineTangentType
        elif tangentType == "custom":
            return KeyTangent.fixedTangentType
        else:
            return KeyTangent.tangentTypes.index(tangentType)
    
    def applyTangent(self, attribute, time):
        if self.inTangentType != KeyTangent.splineTangentType or self.outTangentType != KeyTangent.splineTangentType:
            cmds.keyTangent(attribute, e=True, t=(time, time), itt=KeyTangent.tangentTypes[self.inTangentType], ott=KeyTangent.tangentTypes[self.outTangentType])
            
            if self.inTangentType == KeyTangent.fixedTangentType:
                cmds.keyTangent(attribute, e=True, t=(time, time), ia=-self.inTangent)
                if self.inTangentLength != None:
                    if not cmds.keyTangent(attribute, q=True, wt=True)[0]:
                        cmds.keyTangent(attribute, e=True, wt=True, wl=False)
                    cmds.keyTangent(attribute, e=True, t=(time, time), iw=self.inTangentLength)
                    
            if self.outTangentType == KeyTangent.fixedTangentType:
                cmds.keyTangent(attribute, e=True, t=(time, time), l=False)
                cmds.keyTangent(attribute, e=True, t=(time, time), oa=self.outTangent)
                if self.outTangentLength != None:
                    if not cmds.keyTangent(attribute, q=True, wt=True)[0]:
                        cmds.keyTangent(attribute, e=True, wt=True, wl=False)
                    cmds.keyTangent(attribute, e=True, t=(time, time), ow=self.outTangentLength)


def parseFloatOrNone(floatString):
    if floatString == None or floatString == "":
        return None
    else:
        return float(floatString)

def parseBool(boolString):
    return boolString == "true"

def parseFloatArray(arrayString):
    array = arrayString.split(",")
    for i in range(len(array)):
        numberStr = array[i].strip()
        if i == 0:
            numberStr = numberStr.replace("[", "")
        if i == len(array) - 1:
            numberStr = numberStr.replace("]", "")
        array[i] = parseFloatOrNone(numberStr)
    return array

def parseAnimationFromMax(path, namespace=None):
    xmlDoc = XML.parse(path)

    xmlCharAnim = xmlDoc.getroot()
    charAnim = CharacterAnimation(xmlCharAnim.get("characterName"), namespace=namespace)

    xmlAnimPresets = xmlCharAnim.find("AnimPresets")
    if xmlAnimPresets != None:
        for xmlAnimPreset in xmlAnimPresets.findall("AnimPreset"):
            animPresetInfo = AnimPresetInfo()

            animPresetInfo.nameParts = xmlAnimPreset.get("nameParts").split(",")[:-1]   # Animations have an extra "," character at the end we don't need
            animPresetInfo.path = xmlAnimPreset.get("path")
            animPresetInfo.enabled = parseBool(xmlAnimPreset.get("enabled"))
            animPresetInfo.start = parseFloatOrNone(xmlAnimPreset.get("start"))
            animPresetInfo.end = parseFloatOrNone(xmlAnimPreset.get("end"))
            animPresetInfo.pose = parseBool(xmlAnimPreset.get("pose"))
            animPresetInfo.loop = parseBool(xmlAnimPreset.get("loop"))
            animPresetInfo.color = parseFloatArray(xmlAnimPreset.get("color"))

            xmlAnimPresetActiveLayers = xmlAnimPreset.find("ActiveLayers")
            animPresetInfo.setActiveLayers([xmlAnimPresetActiveLayer.text for xmlAnimPresetActiveLayer in xmlAnimPresetActiveLayers.findall("ActiveLayer")])

            charAnim.animPresets.append(animPresetInfo)

    xmlCharNodes = xmlCharAnim.find("Nodes")
    for xmlCharNode in xmlCharNodes.findall("Node"):
        nodeName = xmlCharNode.get("nodeName")
        parentName = xmlCharNode.get("parentName")
        rotationParentName = xmlCharNode.get("parentForRotationName")
        if namespace != None:
            nodeName = "{}:{}".format(namespace, nodeName)
            if parentName != None:
                parentName = "{}:{}".format(namespace, parentName)
            if rotationParentName != None:
                rotationParentName = "{}:{}".format(namespace, rotationParentName)
        
        charNode = CharacterNode(nodeName, parentName, rotationParentName, parseBool(xmlCharNode.get("reparent")), parseBool(xmlCharNode.get("exportPosition")), parseBool(xmlCharNode.get("exportRotation")), parseBool(xmlCharNode.get("exportScale")))
        
        xmlBaseTransform = xmlCharNode.find("NodeTransform")
        if xmlBaseTransform != None:
            charNode.baseTransform = NodeTransform.fromXml(xmlBaseTransform, characterNode=charNode)
            
        charAnim.nodes.append(charNode)
        
    charAnim.updateIKLimbs()

    xmlLayerAnims = xmlCharAnim.find("LayerAnimations")
    for xmlLayerAnim in xmlLayerAnims.findall("LayerAnimation"):
        layerAnim = LayerAnimation(xmlLayerAnim.get("layerName"))
        charAnim.layerAnimations.append(layerAnim)

        xmlRequiredLayers = xmlLayerAnim.find("RequiredLayers")
        if xmlRequiredLayers != None:
            requiredLayers = []
            for xmlRequiredLayer in xmlRequiredLayers.findall("RequiredLayer"):
                requiredLayers.append(xmlRequiredLayer.text)
            layerAnim.setRequiredLayers(requiredLayers)

        xmlOutOfRangeTypes = xmlLayerAnim.find("OutOfRangeTypes")
        if xmlOutOfRangeTypes != None:
            layerAnim.outOfRangeTypes = []
            for xmlOutOfRangeType in xmlOutOfRangeTypes.findall("OutOfRangeType"):
                layerAnim.outOfRangeTypes.append(OutOfRangeType.fromXml(xmlOutOfRangeType, charAnim.nodes, namespace=namespace))
            
        xmlAnimationPostures = xmlLayerAnim.find("AnimationPostures")
        for xmlAnimPosture in xmlAnimationPostures.findall("AnimationPosture"):
            animPosture = AnimationPosture(float(xmlAnimPosture.get("time")), parseFloatOrNone(xmlAnimPosture.get("rightArmIK")), parseFloatOrNone(xmlAnimPosture.get("leftArmIK")), parseFloatOrNone(xmlAnimPosture.get("rightLegIK")), parseFloatOrNone(xmlAnimPosture.get("leftLegIK")))
            layerAnim.animationPostures.append(animPosture)

            for xmlNodeTrf in xmlAnimPosture.findall("NodeTransform"):
                animPosture.nodeTransforms.append(NodeTransform.fromXml(xmlNodeTrf, characterNodes=charAnim.nodes, namespace=namespace))
            
    xmlParameters = xmlCharAnim.find("Parameters")
    if xmlParameters != None:
        for xmlParameter in xmlParameters.findall("Parameter"):
            parameter = Parameter(xmlParameter.get("attribute"), namespace=namespace)
            
            parameter.beforeOutOfRangeType = xmlParameter.get("beforeOutOfRangeType")
            parameter.afterOutOfRangeType = xmlParameter.get("afterOutOfRangeType")
            
            for xmlKeyframe in xmlParameter.findall("Keyframe"):
                inTangentType = xmlKeyframe.get("inTangentType")
                if inTangentType != None:
                    tangent = KeyTangent(inTangentType, xmlKeyframe.get("outTangentType"), parseFloatOrNone(xmlKeyframe.get("inTangent")), parseFloatOrNone(xmlKeyframe.get("outTangent")), parseFloatOrNone(xmlKeyframe.get("inTangentLength")), parseFloatOrNone(xmlKeyframe.get("outTangentLength")))
                else:
                    tangent = None
                    
                parameter.keyframeData.append((xmlKeyframe.get("time"), parseFloatOrNone(xmlKeyframe.text), tangent))
                
            charAnim.parameters.append(parameter)
        
    return charAnim

def importAnimationFromMax(path=None, namespace=None):
    if path == None:
        path = cmds.fileDialog2(caption="Import Animation From Max", fileFilter="Max CharacterAnimation (*.mxca)", fileMode=1, okCaption="Import")
        if path == None:
            return
        path = path[0]
        
    if namespace == None:
        actors = ActorManager.getActors()
        if len(actors) == 1:
            namespace = actors[0].getNamespace()
        
    logger.info("Parsing Animation File...")
    charAnim = parseAnimationFromMax(path, namespace=namespace)

    logger.info("Applying Animation...")
    charAnim.applyAnimation()


class ImportAnimationFromMaxBatch(Batcher.BatcherUI):

    # OVERRIDE

    def onInitializeUI(self, inputUI):
        inputUI.rigFileBrowseButton.clicked.connect(self.browseRigFile)
        inputUI.outputFolderBrowseButton.clicked.connect(self.browseOutputFolder)
        
        namespace, path = self.getSceneActorPathAndNamespace()
            
        rigFilePath = os.path.join(path, "{}_ANIM.mb".format(namespace))
        if not os.path.isfile(rigFilePath):
            rigFilePath = rigFilePath[:-1] + "a"
        outputFolderPath = os.path.join(path, "animations")
            
        self.setNamespace(namespace)
        self.setRigFilePath(rigFilePath)
        self.setOutputFolderPath(outputFolderPath)

        self.baseRigFileAlreadyOpenend = False

    def onBeforeProcess(self):
        # Checks if the base file to import the animation into exists.
        if not os.path.isfile(self.getRigFilePath()):
            raise FileNotFoundError("Couldn't find the Base Anim File to import the animation into! {}".format(self.getRigFilePath()))

        # Opens the animation file and checks if the provided namespace exists.
        cmds.file(self.getRigFilePath(), o=True, force=True)
        namespaces = cmds.namespaceInfo(":", listOnlyNamespaces=True, recurse=True)
        if not self.getNamespace() in namespaces:
            raise NameError("The provided namespace is not present on the Base Anim File! {}".format(self.getNamespace()))

        # Sets this flag so the first file to be processed doesn't need to open the file again.
        self.baseRigFileAlreadyOpenend = True

        # If the output folder doesn't exist, creates it.
        if not os.path.isdir(self.getOutputFolderPath()):
            os.makedirs(self.getOutputFolderPath())

        return True

    def onPerformBatchProcess(self, filePath):
        # Checks if the animation file exists.
        if not os.path.isfile(filePath):
            raise FileNotFoundError("Couldn't find the specified Animation File! {}".format(filePath))

        # Opens the animation file.
        # If the flag from the preparation process is set, skips this step.
        logger.info("Opening Base Anim File...")
        if not self.baseRigFileAlreadyOpenend:
            cmds.file(self.getRigFilePath(), o=True, force=True)
        else:
            self.baseRigFileAlreadyOpenend = False

        # Imports the animation
        logger.info("Importing Animation...")
        importAnimationFromMax(path=filePath, namespace=self.getNamespace())

        # Saves the file
        fileName, extension = os.path.splitext(os.path.basename(filePath))
        savePath = os.path.join(self.getOutputFolderPath(), "{}.mb".format(fileName))
        logger.info("Saving File... {}".format(savePath))
        cmds.file(rename=savePath)
        cmds.file(save=True, type="mayaBinary")

    def onGetFileFilters(self):
        return ["Max Character Animation (*.mxca)"]

    def onGetDefaultSourceFolderPath(self):
        namespace, path = self.getSceneActorPathAndNamespace()
        return path

    def onGetInputUIFilePath(self):
        return ProjectPath.getToolsFolder() + "\\ImportAnimationFromMax\\ImportAnimationFromMax.ui"

    def onGetLoggerName(self):
        return __name__

    def onGetWindowTitle(self):
        return "Import Animation From Max"

    # METHODS
    
    def getSceneActorPathAndNamespace(self):
        actors = ActorManager.getActors()
        if actors:
            actor = actors[0]
            
            namespace = actor.name
            
            subActor = actor.animSubActor
            pathTokenizer = subActor.getPathTokenizer()
            subPath = pathTokenizer.Translate(subActor.subActorPathToken)
            
        else:
            namespace = "Samus"
            subPath = r"Assets\actors\characters\samus"
        
        print(ProjectPath.get3DFolder(), subPath)
        
        path = os.path.join(ProjectPath.get3DFolder(), subPath)
        if not os.path.isdir(path):
            path = path.replace("PRJ_05", "PRJ_04")
            
        print(namespace, path)
        
        return namespace, path
    
    def setRigFilePath(self, filePath):
        self.inputUI.rigFilePath.setText(filePath)
    
    def getRigFilePath(self):
        return self.inputUI.rigFilePath.text()
        
    def setOutputFolderPath(self, folderPath):
        self.inputUI.outputFolderPath.setText(folderPath)
    
    def getOutputFolderPath(self):
        return self.inputUI.outputFolderPath.text()

    def setNamespace(self, namespace):
        self.inputUI.namespaceText.setText(namespace)

    def getNamespace(self):
        return self.inputUI.namespaceText.text()

    def browseRigFile(self):
        filePath, extension = QtWidgets.QFileDialog.getOpenFileName(self, caption="Select Anim File", filter="Maya Scene File (*.mb *.ma)", dir=self.getRigFilePath())
        if filePath != None and filePath != "":
            self.setRigFilePath(filePath)

    def browseOutputFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, caption="Select Output Folder", dir=self.getOutputFolderPath())
        if folderPath != None and folderPath != "":
            self.setOutputFolderPath(folderPath)


def showBatchWindow():
    global importAnimationFromMaxBatchWindow
    try:
        if importAnimationFromMaxBatchWindow.isVisible():
            importAnimationFromMaxBatchWindow.close()
    except NameError:
        pass
    importAnimationFromMaxBatchWindow = ImportAnimationFromMaxBatch()
    importAnimationFromMaxBatchWindow.show()

if __name__ == "__main__":
    showBatchWindow()