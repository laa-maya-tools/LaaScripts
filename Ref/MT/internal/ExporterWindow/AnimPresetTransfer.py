import ActorManager
import ActorManager.AnimPreset

import ExporterWindow

import json

import maya.cmds as cmds

def exportAnimPresets():
    filePath = cmds.fileDialog2(fileMode=0, fileFilter="Json (*.json);;All Files (*.*)")
    if filePath:
        exportAnimPresetsToFile(filePath[0])

def importAnimPresets():
    filePath = cmds.fileDialog2(fileMode=1, fileFilter="Json (*.json);;All Files (*.*)")
    if filePath:
        importAnimPresetsFromFile(filePath[0])

def exportAnimPresetsToFile(filePath):
    data = {}
    actors = ActorManager.getActors()
    for actor in actors:
        animPresetData = []
        animPresets = actor.getAnimPresets()
        for animPreset in animPresets:
            animPresetData.append(serializeAnimPreset(animPreset))
            
        actorName = actor.getNamespace()
        data[actorName] = animPresetData
    
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def importAnimPresetsFromFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for actorName in data.keys():
        actor = ActorManager.getActorByNameSpace(actorName)
        if actor != None:
            for animPresetData in data[actorName]:
                deserializeAnimPreset(animPresetData, actor)
            actor.normalizeAnimPresetsNameParts()
        else:
            print("WARNING: Actor [{}] not found, skipped.".format(actorName))

def serializeAnimPreset(animPreset):
    color = list(animPreset.color)
    nameParts = animPreset.getNameParts()
    weightedLayers = animPreset.getWeightedLayers()
    subHolder = animPreset.subHolder
    subHolderName = subHolder.getDisplayName() if subHolder else None
    
    data = {
        "enabled" : animPreset.enabled,
        "path" : animPreset.path,
        "category": animPreset.category,
        "start" : animPreset.start,
        "end" : animPreset.end,
        "loop" : animPreset.loop,
        "mirror" : animPreset.mirror,
        "pose" : animPreset.pose,
        "color" : color,
        "nameParts" : nameParts,
        "subHolder" : subHolderName,
        "weightedLayers" : [{
            "animLayer" : weightedLayer.animLayer,
            "weight" : weightedLayer.weight
            } for weightedLayer in weightedLayers]
    }
    
    return data

def deserializeAnimPreset(animPresetData, actor):
    animPreset = ActorManager.AnimPreset.AnimPreset().create()
    actor.addAnimPreset(animPreset)
    
    animPreset.enabled = animPresetData["enabled"]
    animPreset.path = animPresetData["path"]
    animPreset.category = animPresetData["category"]
    animPreset.start = animPresetData["start"]
    animPreset.end = animPresetData["end"]
    animPreset.loop = animPresetData["loop"]
    animPreset.mirror = animPresetData["mirror"]
    animPreset.pose = animPresetData["pose"]
    animPreset.color = animPresetData["color"]
    
    animPreset.setNameParts(animPresetData["nameParts"])
    
    subHolderName = animPresetData["subHolder"]
    if subHolderName != None:
        subHolder = None
        subHolders = actor.getSubHolders()
        for sh in subHolders:
            if sh.getDisplayName() == subHolderName:
                subHolder = sh
        if subHolder != None:
            animPreset.subHolder = subHolder
        else:
            print("WARNING: SubHolder [{}] not found!".format(subHolderName))
    
    animLayers = []
    weights = []
    weightedLayers = animPresetData["weightedLayers"]
    for weightedLayer in weightedLayers:
        animLayers.append(weightedLayer["animLayer"])
        weights.append(weightedLayer["weight"])
    animPreset.setAnimLayers(animLayers, weights)

    refreshExporterWindow()

def refreshExporterWindow():
    if ExporterWindow.isVisible():
        ExporterWindow.instance.refreshCurrentTab()
