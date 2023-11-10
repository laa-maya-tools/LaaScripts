# -*- coding: utf-8 -*-
import NodeID.PluginNodes as PluginNodes 
import maya.api.OpenMaya as OpenMaya
# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

import ActorManager.Plugins.Actor           as Actor      
import ActorManager.Plugins.SubActor        as SubActor   
import ActorManager.Plugins.AnimPreset      as AnimPreset 
import ActorManager.Plugins.CameraSet       as CameraSet
#reload(Actor)      
#reload(SubActor)   
#reload(AnimPreset) 
#reload(CameraSet) 

nodeList=  [Actor.Actor,
            SubActor.SubActor,
            AnimPreset.WeightedLayer,
            AnimPreset.AnimPreset,
            CameraSet.CameraSet,
            ]

def initializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.registerNodes(mplugin, nodeList)
    
def uninitializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.unregisterNodes(mplugin, nodeList)
