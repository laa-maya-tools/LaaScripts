import maya.cmds as cmds

import maya.api.OpenMaya as OpenMaya

import ActorManager
import Utils.Maya.AnimLayers as AnimLayerUtils
import Utils.OpenMaya as OpenMayaUtils

import math

namespace = "Sendojin"
handOffsets = {
    '{}:arm_L0_ik_ctl'.format(namespace): OpenMaya.MEulerRotation(math.pi / 2.0, 0, 0),
    '{}:arm_R0_ik_ctl'.format(namespace): OpenMaya.MEulerRotation(-math.pi / 2.0, 0, math.pi)
}
actor = ActorManager.getActorByNameSpace(namespace)

cmds.delete(cmds.animLayer())
animLayers = AnimLayerUtils.getAnimLayers()
for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=True, mute=True, selected=False)

animLayersNodeTransforms = {}
for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=False, mute=False)
    cmds.animLayer(animLayer, e=True, preferred=True)
    
    nodeTransforms = {}
    
    for obj in handOffsets.keys():
        keyTimes = cmds.keyframe("{}.rotate".format(obj), q=True) or []
        for keyTime in keyTimes:
            if keyTime not in nodeTransforms:
                nodeTransforms[keyTime] = {}
            nodeTransforms[keyTime][obj] = {}
            
    keyTimes = list(nodeTransforms.keys())
    keyTimes.sort()
    for keyTime in keyTimes:
        cmds.currentTime(keyTime, e=True)
        for obj in nodeTransforms[keyTime].keys():
            fn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(obj))
            nodeTransforms[keyTime][obj] = fn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
    
    animLayersNodeTransforms[animLayer] = nodeTransforms
    
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=True, mute=True)

cmds.animLayer(AnimLayerUtils.getBaseLayer(), e=True, preferred=True)
for obj in handOffsets.keys():
    rotateOrderPlug = "{}.rotateOrder".format(obj)
    keyTimes = cmds.keyframe(rotateOrderPlug, q=True) or [0]
    for keyTime in keyTimes:
        cmds.currentTime(keyTime, e=True)
        cmds.setAttr(rotateOrderPlug, 2) #ZXY


for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=False, mute=False)
    cmds.animLayer(animLayer, e=True, preferred=True)
    
    nodeTransforms = animLayersNodeTransforms[animLayer]
    keyTimes = list(nodeTransforms.keys())
    keyTimes.sort()
    for keyTime in keyTimes:
        cmds.currentTime(keyTime, e=True)
        for obj in nodeTransforms[keyTime].keys():
            fn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(obj))
            fn.setRotation(nodeTransforms[keyTime][obj], OpenMaya.MSpace.kWorld)
            fn.rotateBy(handOffsets[obj], OpenMaya.MSpace.kObject)
            
    cmds.filterCurve(list(handOffsets.keys()))
            
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=True, mute=True)
