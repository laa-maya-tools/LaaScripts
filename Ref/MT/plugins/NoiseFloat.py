import maya.api.OpenMaya as OpenMaya

import NodeID

import sys
import Utils.Python.PerlinNoise as PerlinNoise

maya_useNewAPI = True 

class NoiseFloat(OpenMaya.MPxNode):

    nodeName = "NoiseFloat"

    time = OpenMaya.MObject()
    enabled = OpenMaya.MObject()
    seed = OpenMaya.MObject()
    seedOffset = OpenMaya.MObject()
    intensity = OpenMaya.MObject()
    frequency = OpenMaya.MObject()
    jerk = OpenMaya.MObject()

    output = OpenMaya.MObject()

    @staticmethod
    def creator():
        return NoiseFloat()

    @staticmethod
    def initializer():
        unitFn = OpenMaya.MFnUnitAttribute()
        numFn = OpenMaya.MFnNumericAttribute()

        NoiseFloat.time = unitFn.create("time", "t", OpenMaya.MFnUnitAttribute.kTime, 0)
        unitFn.readable = False
        unitFn.hidden = True
        NoiseFloat.addAttribute(NoiseFloat.time)

        NoiseFloat.enabled = numFn.create("enabled", "e", OpenMaya.MFnNumericData.kBoolean, True)
        NoiseFloat.addAttribute(NoiseFloat.enabled)

        NoiseFloat.seed = numFn.create("seed", "sd", OpenMaya.MFnNumericData.kInt, 0)
        numFn.setMin(0)
        NoiseFloat.addAttribute(NoiseFloat.seed)

        NoiseFloat.seedOffset = numFn.create("seedOffset", "sdo", OpenMaya.MFnNumericData.kInt, 0)
        numFn.setMin(0)
        NoiseFloat.addAttribute(NoiseFloat.seedOffset)
        
        NoiseFloat.intensity = numFn.create("intensity", "in", OpenMaya.MFnNumericData.kFloat, 0)
        NoiseFloat.addAttribute(NoiseFloat.intensity)
        
        NoiseFloat.frequency = numFn.create("frequency", "fq", OpenMaya.MFnNumericData.kFloat, 0)
        numFn.setMin(0)
        NoiseFloat.addAttribute(NoiseFloat.frequency)

        NoiseFloat.jerk = numFn.create("jerk", "jk", OpenMaya.MFnNumericData.kInt, 1)
        numFn.setMin(1)
        NoiseFloat.addAttribute(NoiseFloat.jerk)

        NoiseFloat.output = numFn.create("output", "out", OpenMaya.MFnNumericData.kFloat)
        numFn.writable = False
        numFn.storable = False
        NoiseFloat.addAttribute(NoiseFloat.output)

        NoiseFloat.attributeAffects(NoiseFloat.time, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.enabled, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.seed, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.seedOffset, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.intensity, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.frequency, NoiseFloat.output)
        NoiseFloat.attributeAffects(NoiseFloat.jerk, NoiseFloat.output)

    def compute(self, plug, data):
        if plug == self.output:
            enabled = data.inputValue(self.enabled).asBool()
            time = data.inputValue(self.time).asTime()
            seed = data.inputValue(self.seed).asInt()
            seedOffset = data.inputValue(self.seedOffset).asInt()
            intensity = data.inputValue(self.intensity).asFloat()
            frequency = data.inputValue(self.frequency).asFloat()
            jerk = data.inputValue(self.jerk).asInt()
            
            if enabled:
                context = data.context()
                if context.isNormal():
                    currentTime = time
                else:
                    currentTime = context.getTime()

                pnf = PerlinNoise.PerlinNoiseFactory(1, octaves=jerk, seed=seed+seedOffset, unbias=True)

                timeOffset = frequency * currentTime.asUnits(OpenMaya.MTime.kSeconds)
                noise = pnf(timeOffset) * intensity
                
            else:
                noise = 0
            
            data.outputValue(self.output).setFloat(noise)
            data.setClean(plug)

        OpenMaya.MPxNode.compute(self, plug, data)
        

# initialize the script plug-in
def initializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj, "MSE", "1.0", "Any")

    try:
        plugin.registerNode(NoiseFloat.nodeName, NodeID.NoiseFloatID, NoiseFloat.creator, NoiseFloat.initializer)
    except:
        sys.stderr.write("Failed to register node: " + NoiseFloat.nodeName)
        raise

# uninitialize the script plug-in
def uninitializePlugin(obj):
    plugin = OpenMaya.MFnPlugin(obj)

    try:
        plugin.deregisterNode(NodeID.NoiseFloatID)
    except:
        sys.stderr.write("Failed to unregister node: " + NoiseFloat.nodeName)
        raise   