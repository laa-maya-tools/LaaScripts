# -*- coding: utf-8 -*-
import NodeID.PluginNodes as PluginNodes 
import maya.api.OpenMaya as OpenMaya

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

import NodeCustom.Transformations.Plugins.MatrixMirror      as CNMatrixMirror
import NodeCustom.Transformations.Plugins.ScaleFactor       as CNScaleFactor
import NodeCustom.Transformations.Plugins.LookQuaternion    as CNLookQuaternion
import NodeCustom.Transformations.Plugins.AngleReaction     as CNAngleReaction
import NodeCustom.Transformations.Plugins.SpaceSwitcher     as CNSpaceSwitcher

# debug mode
# region

#import importlib
#importlib.reload(CNMatrixMirror)
#importlib.reload(CNScaleFactor)
#importlib.reload(CNLookQuaternion)
#importlib.reload(CNAngleReaction)
#importlib.reload(CNSpaceSwitcher)

# endregion

nodeList=  [CNMatrixMirror.MatrixMirror,
            CNScaleFactor.ScaleFactor,
            CNLookQuaternion.LookQuaternion,
            CNAngleReaction.AngleReaction,
            CNSpaceSwitcher.SpaceSwitcher]
            
def initializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.registerNodes(mplugin, nodeList)
    
def uninitializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.unregisterNodes(mplugin, nodeList)

