import maya.cmds as cmds

import ActorManager
import Utils.Maya.AnimLayers as AnimLayerUtils

namespace = "Sendojin"
masters = ['global_C0_ctl', 'local_C0_ctl', 'world_ctl']
actor = ActorManager.getActorByNameSpace(namespace)

animPresets = actor.getAnimPresets()
for animPreset in animPresets:
    animPresetName = animPreset.getConcatenatedName()
    if "{left}" in animPresetName or "{right}" in animPresetName:
        animPreset.mirror = True

cmds.delete(cmds.animLayer())
animLayers = AnimLayerUtils.getAnimLayers()
for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=True, mute=True, selected=False)
for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=False, mute=False)
    cmds.animLayer(animLayer, e=True, preferred=True)
    
    times = {}
    for obj in masters:
        plug = "{}:{}.scale".format(namespace, obj)
        keyTimes = cmds.keyframe(plug, q=True) or [0]
        for keyTime in keyTimes:
            if keyTime not in times:
                times[keyTime] = []
            times[keyTime].append(plug)
            
    keyTimes = list(times.keys())
    keyTimes.sort()
    for keyTime in keyTimes:
        cmds.currentTime(keyTime, e=True)
        for plug in times[keyTime]:
            cmds.setAttr(plug, 1, 1, 1)
    
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, lock=True, mute=True)
            
