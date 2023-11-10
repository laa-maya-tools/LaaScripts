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

class TrigonometricInverseAngle(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName = "trigonometricInverseAngle"
    nodeID   = NodeID.TrigonometricInverseAngleID
    
    asin    = OpenMaya.MObject()
    acos    = OpenMaya.MObject()
    atan    = OpenMaya.MObject()

    input   = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return TrigonometricInverseAngle()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute    = OpenMaya.MFnMatrixAttribute()
        #enumAttribute      = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        unitAttribute       = OpenMaya.MFnUnitAttribute()
        #compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()
        
        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------
        #input
        TrigonometricInverseAngle.input = numericAttribute.create("input", "ip", OpenMaya.MFnNumericData.kFloat, 0.0)   
        numericAttribute.writable   = True
        numericAttribute.readable   = False
        numericAttribute.storable   = True
        numericAttribute.keyable    = True

        TrigonometricInverseAngle.addAttribute(TrigonometricInverseAngle.input)   
        
        #asin
        TrigonometricInverseAngle.asin = unitAttribute.create("asin", "as", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        TrigonometricInverseAngle.addAttribute(TrigonometricInverseAngle.asin)   
        
        #acos
        TrigonometricInverseAngle.acos = unitAttribute.create("acos", "ac", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        TrigonometricInverseAngle.addAttribute(TrigonometricInverseAngle.acos)   
        
        #atan
        TrigonometricInverseAngle.atan = unitAttribute.create("atan", "at", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        TrigonometricInverseAngle.addAttribute(TrigonometricInverseAngle.atan)      
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        # outputWorldMatrix
        TrigonometricInverseAngle.attributeAffects(TrigonometricInverseAngle.input, TrigonometricInverseAngle.acos)
        TrigonometricInverseAngle.attributeAffects(TrigonometricInverseAngle.input, TrigonometricInverseAngle.asin)
        TrigonometricInverseAngle.attributeAffects(TrigonometricInverseAngle.input, TrigonometricInverseAngle.atan)
        
    def compute(self, plug, dataBlock):
        if plug == self.asin:
            theInput = (dataBlock.inputValue(self.input)).asFloat()
            #dataBlock.outputValue(self.asin).setFloat(math.asin(theInput))
            dataBlock.outputValue(self.asin).setMAngle(OpenMaya.MAngle(math.asin(theInput)))
            dataBlock.setClean(plug)
    
        elif plug == self.acos:
            theInput = (dataBlock.inputValue(self.input)).asFloat()
            #dataBlock.outputValue(self.acos).setFloat(math.acos(theInput))
            dataBlock.outputValue(self.acos).setMAngle(OpenMaya.MAngle(math.acos(theInput)))
            dataBlock.setClean(plug)
    
        elif plug == self.atan:
            theInput = (dataBlock.inputValue(self.input)).asFloat()
            #dataBlock.outputValue(self.atan).setFloat(math.atan(theInput))
            dataBlock.outputValue(self.atan).setMAngle(OpenMaya.MAngle(math.atan(theInput)))
            dataBlock.setClean(plug)
    

