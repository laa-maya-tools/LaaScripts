# -*- coding: utf-8 -*-
import maya.api.OpenMaya as OpenMaya

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

import NodeID.PluginNodes as PluginNodes

import AnimSystems.AutoSnap as AutoSnap

import RigManager.Plugins.Rig as Rig
import RigManager.Plugins.IKFKChain as IKFKChain
#reload(Rig)
#reload(IKFKChain)

nodeList = [
    Rig.Rig,
    IKFKChain.IKFKChainNode,
]

def initializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    
    PluginNodes.registerNodes(mplugin, nodeList)
    
    AutoSnap.AutoSnapManager.initialize()
    
def uninitializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    
    AutoSnap.AutoSnapManager.uninitialize()
        
    PluginNodes.unregisterNodes(mplugin, nodeList)
