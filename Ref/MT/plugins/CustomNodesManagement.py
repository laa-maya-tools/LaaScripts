# -*- coding: utf-8 -*-
import NodeID.PluginNodes as PluginNodes 
import maya.api.OpenMaya as OpenMaya
# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

import NodeCustom.Management.Plugins.NodeCollection      as CNNodeCollection
import NodeCustom.Management.Plugins.CustomCollection    as CNCustomCollection

#import importlib
#importlib.reload(CNNodeCollection)
#importlib.reload(CNCustomCollection)

nodeList=[  CNNodeCollection.NodeCollection,
            CNCustomCollection.CustomCollection
        ]

def initializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.registerNodes(mplugin, nodeList)
    
def uninitializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.unregisterNodes(mplugin, nodeList)

