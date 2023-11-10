# -*- coding: utf-8 -*-

#import sys
import math
#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class TrigonometricAngle(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName            = "trigonometricAngle"
    nodeID              = NodeID.TrigonometricAngleID
    #angleFrom3Matrix   = OpenMaya.MObject()
    #matrix0            = OpenMaya.MObject()
    #matrix1            = OpenMaya.MObject()
    #matrix2            = OpenMaya.MObject()
    angle               = OpenMaya.MObject()
    sin                 = OpenMaya.MObject()
    cos                 = OpenMaya.MObject()
    tan                 = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return TrigonometricAngle()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        #enumAttribute       = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        unitAttribute       = OpenMaya.MFnUnitAttribute()
        #compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()
        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------
        
        TrigonometricAngle.angle = unitAttribute.create("angle", "a", unitAttribute.kAngle, 0.0)
        unitAttribute.writable = True
        unitAttribute.readable = False
        unitAttribute.keyable  = True
        unitAttribute.storable = True
        TrigonometricAngle.addAttribute(TrigonometricAngle.angle)   
        
        TrigonometricAngle.sin = numericAttribute.create("sin", "sn", OpenMaya.MFnNumericData.kFloat)
        numericAttribute.writable = False
        numericAttribute.readable = True
        TrigonometricAngle.addAttribute(TrigonometricAngle.sin)        

        TrigonometricAngle.cos = numericAttribute.create("cos", "cn", OpenMaya.MFnNumericData.kFloat)
        numericAttribute.writable = False
        numericAttribute.readable = True
        TrigonometricAngle.addAttribute(TrigonometricAngle.cos)        

        TrigonometricAngle.tan = numericAttribute.create("tan", "tn", OpenMaya.MFnNumericData.kFloat)
        numericAttribute.writable = False
        numericAttribute.readable = True
        TrigonometricAngle.addAttribute(TrigonometricAngle.tan)        

        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        TrigonometricAngle.attributeAffects(TrigonometricAngle.angle        , TrigonometricAngle.sin)
        TrigonometricAngle.attributeAffects(TrigonometricAngle.angle        , TrigonometricAngle.cos)
        TrigonometricAngle.attributeAffects(TrigonometricAngle.angle        , TrigonometricAngle.tan)

    def compute(self, plug, dataBlock):
        if plug == self.sin:
            theMAngle    = (dataBlock.inputValue(self.angle)).asAngle()
            dataBlock.outputValue(self.sin).setFloat(math.sin(theMAngle.asRadians()))
            dataBlock.setClean(plug)
            
        elif plug == self.cos:
            theMAngle    = (dataBlock.inputValue(self.angle)).asAngle()
            dataBlock.outputValue(self.cos).setFloat(math.cos(theMAngle.asRadians()))
            dataBlock.setClean(plug)
            
        elif plug == self.tan:
            theMAngle    = (dataBlock.inputValue(self.angle)).asAngle()
            dataBlock.outputValue(self.tan).setFloat(math.tan(theMAngle.asRadians()))
            dataBlock.setClean(plug)

