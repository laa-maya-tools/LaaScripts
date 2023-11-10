import maya.cmds as cmds

import ProjectPath
import ActorManager

import Utils.Maya.AnimLayers as AnimLayerUtils

from mutils.animation import Animation
from mutils.selectionset import SelectionSet
import studiolibrary

import os

objectsToRealign = ["body_C0_ctl", "spine_C0_ik1_ctl", "arm_L0_ik_ctl", "arm_R0_ik_ctl", "leg_L0_ik_ctl", "leg_R0_ik_ctl", "arm_L0_upv_ctl", "arm_R0_upv_ctl", "leg_L0_upv_ctl", "leg_R0_upv_ctl"]

actor = ActorManager.getActorByNameSpace("Sendojin")
namespace = actor.getNamespace()
subActor = actor.animSubActor
pathTokenizer = subActor.getPathTokenizer()
subPath = pathTokenizer.Translate(subActor.subActorPathToken)

oldRigFile = os.path.join(ProjectPath.get3DFolder(), subPath, "rig", "{}_RIG_old.mb".format(actor.name))
tempNamespace = ActorManager.createActorReference(oldRigFile, namespace="TEMP", autoRename=True)

sceneName = os.path.splitext(os.path.basename(cmds.file(q=True, sn=True)))[0]
studioLibraryPath = os.path.join(ProjectPath.get3DFolder(), subPath, "animations", "studiolibrary")
tempPath = studiolibrary.createTempPath("SendojinRealigner")
animPath = os.path.join(tempPath, "{}.anim".format(sceneName))
selectionSetPath = os.path.join(studioLibraryPath, "SelectionSets", "SelectionSet.set", "set.json")

selectionSet = SelectionSet.fromPath(selectionSetPath)
selectionSetObjects = selectionSet.objects()
selectionSetObjects = [obj if ":" not in obj else obj.split(":")[1] for obj in selectionSetObjects]
selectionSetObjects = [obj for obj in selectionSetObjects if cmds.objExists("{}:{}".format(namespace, obj))]

# An animation layer is created and inmediately destroyed so Maya creates the BaseAnimation layer if there are no other layers
cmds.delete(cmds.animLayer())

animLayers = AnimLayerUtils.getAnimLayers()
for animLayer in animLayers:
    cmds.animLayer(animLayer, e=True, aso=True)
    cmds.animLayer(animLayer, e=True, selected=False)
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, mute=True, lock=True)
    
for animLayer in animLayers:
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, mute=False, lock=False)
        
        layerPlugs = AnimLayerUtils.getPlugsOnLayer(animLayer)
        layerObjects = set()
        for plug in layerPlugs:
            obj = plug.split(":")[-1].split(".")[0]
            if obj in selectionSetObjects:
                layerObjects.add(obj)

    else:
        layerObjects = selectionSetObjects
    
    cmds.animLayer(animLayer, e=True, selected=True)
    cmds.animLayer(animLayer, e=True, preferred=True)
    
    tmpObjects = ["{}:{}".format(tempNamespace, obj) for obj in layerObjects]
    tmpObjects = [obj for obj in tmpObjects if cmds.objExists(obj)]
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.select(tmpObjects)
        cmds.animLayer(animLayer, e=True, aso=True)
    
    animation = Animation.fromObjects(["{}:{}".format(namespace, obj) for obj in layerObjects])
    animation.save(animPath, bakeConnected=False)
    animation.load(tmpObjects, namespaces=None)
    
    for obj in objectsToRealign:
        if obj in layerObjects:
            source = "{}:{}".format(tempNamespace, obj)
            target = "{}:{}".format(namespace, obj)
            
            aligns = {}
            
            keyTimes = set(cmds.keyframe("{}.translate".format(target), q=True) or [])
            for t in keyTimes:
                if t not in aligns:
                    aligns[t] = [False, False]
                aligns[t][0] = True
            
            keyTimes = set(cmds.keyframe("{}.rotate".format(target), q=True) or [])
            for t in keyTimes:
                if t not in aligns:
                    aligns[t] = [False, False]
                aligns[t][1] = True
                
            keyTimes = list(aligns.keys())
            keyTimes.sort()
            for t in keyTimes:
                cmds.currentTime(t, e=True)
                cmds.matchTransform(target, source, position=aligns[t][0], rotation=aligns[t][1])
                
            cmds.filterCurve(target)
            
    if not AnimLayerUtils.isBaseLayer(animLayer):
        cmds.animLayer(animLayer, e=True, mute=True, lock=True)
    cmds.animLayer(animLayer, e=True, selected=False)
    
ActorManager.deleteActorReference(ActorManager.getActorByNameSpace(tempNamespace))
