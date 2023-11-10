import NodeManager.NodeWrapper as NodeWrapper

import maya.cmds as cmds

import Utils.Maya.NodeConversion as NodeConversion
import Utils.Maya.AnimLayers as AnimLayerUtils
from Utils.Maya.UndoContext import UndoContext

import itertools

class NoiseFloat(NodeWrapper.NodeWrapper):
        
    _Type = "NoiseFloat"
    
    # Attributes ------------
    
    _time = "time"
    _enabled = "enabled"
    _seed = "seed"
    _seedOffset = "seedOffset"
    _intensity = "intensity"
    _frequency = "frequency"
    _jerk = "jerk"
    _output = "output"
    
    # Properties ------------
        
    @property
    def enabled(self):
        return self.getAttr(self._enabled)
    
    @enabled.setter
    def enabled(self, value):
        with UndoContext("Set Noise Enabled"):
            self.setNumericAttribute(self._enabled, value)

    @property
    def seed(self):
        return self.getAttr(self._seed)
    
    @seed.setter
    def seed(self, value):
        with UndoContext("Set Noise Seed"):
            self.setNumericAttribute(self._seed, value)

    @property
    def seedOffset(self):
        return self.getAttr(self._seedOffset)
    
    @seedOffset.setter
    def seedOffset(self, value):
        with UndoContext("Set Noise Seed Offset"):
            self.setNumericAttribute(self._seedOffset, value)

    @property
    def intensity(self):
        return self.getAttr(self._intensity)
    
    @intensity.setter
    def intensity(self, value):
        with UndoContext("Set Noise Intensity"):
            self.setNumericAttribute(self._intensity, value)

    @property
    def frequency(self):
        return self.getAttr(self._frequency)
    
    @frequency.setter
    def frequency(self, value):
        with UndoContext("Set Noise Frequency"):
            self.setNumericAttribute(self._frequency, value)

    @property
    def jerk(self):
        return self.getAttr(self._jerk)
    
    @jerk.setter
    def jerk(self, value):
        with UndoContext("Set Noise Jerk"):
            self.setNumericAttribute(self._jerk, value)
            
    # Time ------------------
            
    def connectTimePlug(self, timePlug):
        self.connect(self.getPlug(self._time), timePlug)
            
    def connectTimeGlobal(self):
        self.connectTimePlug("time1.outTime")
    
    # Input -----------------
    
    def connectInputs(self, node, connectEnabled=None, connectSeed=None, connectSeedOffset=None, connectIntensity=None, connectFrequency=None, connectJerk=None):
        with UndoContext("Connect Inputs"):
            if connectEnabled != None:
                self.connect(self.getPlug(self._enabled), input="{}.{}".format(node, connectEnabled))
            if connectSeed != None:
                self.connect(self.getPlug(self._seed), input="{}.{}".format(node, connectSeed))
            if connectSeedOffset != None:
                self.connect(self.getPlug(self._seedOffset), input="{}.{}".format(node, connectSeedOffset))
            if connectIntensity != None:
                self.connect(self.getPlug(self._intensity), input="{}.{}".format(node, connectIntensity))
            if connectFrequency != None:
                self.connect(self.getPlug(self._frequency), input="{}.{}".format(node, connectFrequency))
            if connectJerk != None:
                self.connect(self.getPlug(self._jerk), input="{}.{}".format(node, connectJerk))
    
    def disconnectInputs(self, node, connectEnabled=None, connectSeed=None, connectSeedOffset=None, connectIntensity=None, connectFrequency=None, connectJerk=None):
        with UndoContext("Disconnect Inputs"):
            if connectEnabled != None:
                self.removeConnection(self.getPlug(self._enabled), input="{}.{}".format(node, connectEnabled))
            if connectSeed != None:
                self.removeConnection(self.getPlug(self._seed), input="{}.{}".format(node, connectSeed))
            if connectSeedOffset != None:
                self.removeConnection(self.getPlug(self._seedOffset), input="{}.{}".format(node, connectSeedOffset))
            if connectIntensity != None:
                self.removeConnection(self.getPlug(self._intensity), input="{}.{}".format(node, connectIntensity))
            if connectFrequency != None:
                self.removeConnection(self.getPlug(self._frequency), input="{}.{}".format(node, connectFrequency))
            if connectJerk != None:
                self.removeConnection(self.getPlug(self._jerk), input="{}.{}".format(node, connectJerk))
    
    # Output ----------------
    
    def getOutput(self):
        return self.getAttr(self._output)
    
    def getOutputAtTime(self, time):
        return self.getAttrAtTime(self._output, time)
    
    def connectOutput(self, plug):
        self.connect(self.getPlug(self._output), outputList=[plug])
    
    def disconnectOutput(self, plug):
        self.removeConnection(self.getPlug(self._output), outputList=[plug])
    
    def getOutputConnections(self, plugs=True):
        return self.getOutputSingle(self._output, plugs=plugs)


ATTRIBUTE_SEPARATOR = "NoiseSeparator"

ATTRIBUTE_NOISE_ENABLED = "NoiseEnabled"
ATTRIBUTE_NOISE_SEED = "NoiseSeed"
ATTRIBUTE_NOISE_INTENSITY = "NoiseIntensity"
ATTRIBUTE_NOISE_FREQUENCY = "NoiseFrequency"
ATTRIBUTE_NOISE_JERK = "NoiseJerk"

ATTRIBUTE_CATEGORY = "Noise"

def addNoiseToNode(node, attributes, layer=None, niceNames=None, sharedLabel="", addSeparator=True, applySeedOffset=True, shareEnabled=True, shareSeed=True, shareIntensity=False, shareFrequency=False, shareJerk=False):
    with UndoContext("Add Noise"):
        if not sharedLabel.endswith("_"):
            sharedLabel += "_"
        
        if addSeparator:
            separatorAttr = "{}{}".format(sharedLabel, ATTRIBUTE_SEPARATOR)
            if not cmds.attributeQuery(separatorAttr, n=node, ex=True):
                cmds.addAttr(node, longName=separatorAttr, niceName="{} Noise".format(sharedLabel[:-1]), at="enum", enumName="------", dv=0, k=False, r=False, category=ATTRIBUTE_CATEGORY)
                cmds.setAttr("{}.{}".format(node, separatorAttr), e=True, channelBox=True)
        
        if shareEnabled:
            enabledAttr = ["{}{}".format(sharedLabel, ATTRIBUTE_NOISE_ENABLED)]
        else:
            enabledAttr = ["{}_{}".format(attribute if niceNames == None else niceNames[i], ATTRIBUTE_NOISE_ENABLED) for i, attribute in enumerate(attributes)]
        for attr in enabledAttr:
            if not cmds.attributeQuery(attr, n=node, ex=True):
                cmds.addAttr(node, longName=attr, at="bool", dv=True, k=True, category=ATTRIBUTE_CATEGORY, disconnectBehaviour=2)
        
        if shareSeed:
            seedAttr = ["{}{}".format(sharedLabel, ATTRIBUTE_NOISE_SEED)]
        else:
            seedAttr = ["{}_{}".format(attribute if niceNames == None else niceNames[i], ATTRIBUTE_NOISE_SEED) for i, attribute in enumerate(attributes)]
        for attr in seedAttr:
            if not cmds.attributeQuery(attr, n=node, ex=True):
                cmds.addAttr(node, longName=attr, at="long", dv=0, k=True, min=0, category=ATTRIBUTE_CATEGORY, disconnectBehaviour=2)
        
        if shareIntensity:
            intensityAttr = ["{}{}".format(sharedLabel, ATTRIBUTE_NOISE_INTENSITY)]
        else:
            intensityAttr = ["{}_{}".format(attribute if niceNames == None else niceNames[i], ATTRIBUTE_NOISE_INTENSITY) for i, attribute in enumerate(attributes)]
        for attr in intensityAttr:
            if not cmds.attributeQuery(attr, n=node, ex=True):
                cmds.addAttr(node, longName=attr, at="float", dv=0, k=True, category=ATTRIBUTE_CATEGORY, disconnectBehaviour=2)
        
        if shareFrequency:
            frequencyAttr = ["{}{}".format(sharedLabel, ATTRIBUTE_NOISE_FREQUENCY)]
        else:
            frequencyAttr = ["{}_{}".format(attribute if niceNames == None else niceNames[i], ATTRIBUTE_NOISE_FREQUENCY) for i, attribute in enumerate(attributes)]
        for attr in frequencyAttr:
            if not cmds.attributeQuery(attr, n=node, ex=True):
                cmds.addAttr(node, longName=attr, at="float", dv=0, k=True, min=0, category=ATTRIBUTE_CATEGORY, disconnectBehaviour=2)
        
        if shareJerk:
            jerkAttr = ["{}{}".format(sharedLabel, ATTRIBUTE_NOISE_JERK)]
        else:
            jerkAttr = ["{}_{}".format(attribute if niceNames == None else niceNames[i], ATTRIBUTE_NOISE_JERK) for i, attribute in enumerate(attributes)]
        for attr in jerkAttr:
            if not cmds.attributeQuery(attr, n=node, ex=True):
                cmds.addAttr(node, longName=attr, at="long", dv=1, k=True, min=1, max=10, defaultValue=1, category=ATTRIBUTE_CATEGORY, disconnectBehaviour=2)
        
        for i, attr in enumerate(attributes):
            noiseNode = NoiseFloat().create(skipSelect=True)
            noiseNode.connectTimeGlobal()
            
            noiseNode.connectInputs(
                node,
                connectEnabled=enabledAttr[0 if shareEnabled else i],
                connectSeed=seedAttr[0 if shareSeed else i],
                connectIntensity=intensityAttr[0 if shareIntensity else i],
                connectFrequency=frequencyAttr[0 if shareFrequency else i],
                connectJerk=jerkAttr[0 if shareJerk else i]
                )
            
            if applySeedOffset:
                noiseNode.seedOffset = i
            
            plug = "{}.{}".format(node, attr)
            if layer != None:
                if layer == "": # An empty string indicates to use the best anim layer for each attribute
                    layer = AnimLayerUtils.getBestAnimLayerForPlug(plug)
                elif layer not in AnimLayerUtils.getAffectedLayersForAttribute(plug):
                    AnimLayerUtils.addAttributeToLayer(plug, layer)
                plug = AnimLayerUtils.getAnimLayerPlugForAttribute(plug, layer)
                
            noiseNode.connectOutput(plug)
        
def addNoiseToTransform(transform, translation=False, rotation=False, scale=False):
    with UndoContext("Add Noise"):
        if cmds.nodeType(transform) != "AdditiveTransform":
            transform = NodeConversion.convertToAdditiveTransform(transform)
            
            for attr, coord in itertools.product(["ap", "ar", "as"], ["x","y","z"]):
                cmds.setAttr("{}.{}{}".format(transform, attr, coord), e=True, k=False, cb=False)
        
        if translation:
            addNoiseToNode(transform, ["apx", "apy", "apz"], layer=None, niceNames=["TranslateX", "TranslateY", "TranslateZ"], sharedLabel="Translation", addSeparator=True,
                        shareEnabled=True, shareSeed=True, shareIntensity=False, shareFrequency=False, shareJerk=True)
        
        if rotation:
            addNoiseToNode(transform, ["arx", "ary", "arz"], layer=None, niceNames=["RotateX", "RotateY", "RotateZ"], sharedLabel="Rotation", addSeparator=True,
                        shareEnabled=True, shareSeed=True, shareIntensity=False, shareFrequency=False, shareJerk=True)
        
        if scale:
            addNoiseToNode(transform, ["asx", "asy", "asz"], layer=None, niceNames=["ScaleX", "ScaleY", "ScaleZ"], sharedLabel="Scale", addSeparator=True,
                        shareEnabled=True, shareSeed=True, shareIntensity=False, shareFrequency=False, shareJerk=True)

def removeNoiseFromNode(node, attributes, layer=None, restoreValue=True, removeNoiseAttributes=True):
    with UndoContext("Remove Noise"):
        for attr in attributes:
            plug = "{}.{}".format(node, attr)
            if layer != None:
                if layer == "": # An empty string indicates to use the best anim layer for each attribute
                    layer = AnimLayerUtils.getBestAnimLayerForPlug(plug)
                plug = AnimLayerUtils.getAnimLayerPlugForAttribute(plug, layer)
                
            noiseNode = cmds.listConnections(plug, s=True, d=False, type=NoiseFloat._Type, skipConversionNodes=True) or []
            if len(noiseNode) == 0:
                raise AssertionError("The attribute [{}] is not connected to any Noise node!".format(plug))
            noiseNode = NoiseFloat(noiseNode[0])
            
            # Disconnects the node from the attribute.
            noiseNode.disconnectOutput(plug)
            if restoreValue:
                defaultValues = cmds.attributeQuery(attr, node=node, listDefault=True) or []
                if len(defaultValues) == 0:
                    defaultValues = [0]
                cmds.setAttr(plug, defaultValues[0])
            
            if removeNoiseAttributes:
                # Checks if the node is still connected to anything. If not, removes it and attempts to remove the attributes connected to it.
                outConnections = cmds.listConnections(noiseNode.getPlug(NoiseFloat._output), s=False, d=True, skipConversionNodes=True) or []
                if len(outConnections) == 0:
                    # Looks for the artificial attributes (created by this tool, they belong to the category "Noise").
                    connectedPlugs = cmds.listConnections(noiseNode.node, s=True, d=False, plugs=True, skipConversionNodes=True) or []
                    noiseNode.delete()
                    for connectedPlug in connectedPlugs:
                        if cmds.addAttr(connectedPlug, q=True, exists=True) and ATTRIBUTE_CATEGORY in cmds.addAttr(connectedPlug, q=True, category=True):
                            # With the noise node deleted, if the attribute is not connected to anything else, deletes it.
                            outConnections = cmds.listConnections(connectedPlug, s=False, d=True, skipConversionNodes=True) or []
                            if len(outConnections) == 0:
                                cmds.deleteAttr(connectedPlug)
                                
                            # Lastly, there is a "separator" attribute that is not connected to anything.
                            # If we detect this is the only Noise attribute left on the node, deletes it too.
                            connectedNode = connectedPlug.split(".")[0]
                            noiseAttributes = cmds.listAttr(connectedNode, category=ATTRIBUTE_CATEGORY)
                            for noiseAttr in noiseAttributes:
                                if noiseAttr.endswith(ATTRIBUTE_SEPARATOR):
                                    sharedLabel = noiseAttr.split("_")[0]
                                    mustRemove = True
                                    for otherAttr in noiseAttributes:
                                        if otherAttr != noiseAttr and otherAttr.startswith(sharedLabel):
                                            mustRemove = False
                                            break
                                    if mustRemove:
                                        cmds.deleteAttr("{}.{}".format(node, noiseAttr))
        
def removeNoiseFromTransform(transform, removeNoiseAttributes=True, translation=True, rotation=True, scale=True, restoreToNormalTransform=False):
    with UndoContext("Remove Noise"):
        attributesWithNoise = getAttributesWithNoise(transform, plugs=False)
        attributesWithNoise = set([cmds.attributeQuery(attr, node=transform, shortName=True) for attr in attributesWithNoise])
         
        translationAttrs = attributesWithNoise.intersection(["apx", "apy", "apz"])
        rotationAttrs = attributesWithNoise.intersection(["arx", "ary", "arz"])
        scaleAttrs = attributesWithNoise.intersection(["asx", "asy", "asz"])
        
        if restoreToNormalTransform and ((not translation and len(translationAttrs) > 0) or (not rotation and len(rotationAttrs) > 0) or (not scale and len(scaleAttrs) > 0)):
            raise AssertionError("Restoring the transform to a normal one requieres to remove all translation, rotation and scale noises.")
    
        if translation:
            removeNoiseFromNode(transform, translationAttrs, layer=None, removeNoiseAttributes=removeNoiseAttributes)
        
        if rotation:
            removeNoiseFromNode(transform, rotationAttrs, layer=None, removeNoiseAttributes=removeNoiseAttributes)
        
        if scale:
            removeNoiseFromNode(transform, scaleAttrs, layer=None, removeNoiseAttributes=removeNoiseAttributes)
            
        if restoreToNormalTransform:
            NodeConversion.convertToBasicTransform(transform)

def getAttributesWithNoise(node, layer=None, plugs=True):
    if layer == None:
        connections = cmds.listConnections(node, s=True, d=False, type=NoiseFloat._Type, skipConversionNodes=True, connections=True) or []
        attributesWithNoise = [connections[i] for i in range(0, len(connections), 2)]
        if not plugs:
            attributesWithNoise = [attr.split(".")[-1] for attr in attributesWithNoise]
        return attributesWithNoise
    else:
        attributesWithNoise = []
        attributes = cmds.listAttr(node, k=True)
        for attribute in attributes:
            plug = "{}.{}".format(node, attribute)
            layerPlug = AnimLayerUtils.getAnimLayerPlugForAttribute(plug, layer if layer != "" else AnimLayerUtils.getBestAnimLayerForPlug(plug))
            if layerPlug != None and layerPlug != "":
                connections = cmds.listConnections(layerPlug, s=True, d=False, type=NoiseFloat._Type, skipConversionNodes=True) or []
                if len(connections) > 0:
                    attributesWithNoise.append(plug if plugs else attribute)
        return attributesWithNoise
