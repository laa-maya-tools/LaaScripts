# -*- coding: utf-8 -*-

import NodeID.PluginNodes as PluginNodes
import maya.api.OpenMaya as OpenMaya

# Maya API 2.Functions required to use

def maya_useNewAPI():
    pass

import NodeCustom.Mathematics.Plugins.TrigonometricAngle           as CNTrigonometricAngle
import NodeCustom.Mathematics.Plugins.TrigonometricInverseAngle    as CNTrigonometricInverseAngle
import NodeCustom.Mathematics.Plugins.Angle3Point                  as CNAngle3Point
import NodeCustom.Mathematics.Plugins.MatrixRow                    as CNMatrixRow
import NodeCustom.Mathematics.Plugins.FloatMathList                as CNFloatMathList
import NodeCustom.Mathematics.Plugins.Point3MathList               as CNPoint3MathList

nodeList=[  
            CNTrigonometricAngle.TrigonometricAngle,
            CNTrigonometricInverseAngle.TrigonometricInverseAngle,
            CNAngle3Point.Angle3Point,
            CNMatrixRow.MatrixRow,
            CNFloatMathList.FloatMathList,
            CNPoint3MathList.Point3MathList
        ]

def initializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.registerNodes(mplugin, nodeList)

def uninitializePlugin(mObject):
    mplugin = OpenMaya.MFnPlugin(mObject)
    PluginNodes.unregisterNodes(mplugin, nodeList)
     