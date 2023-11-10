# -*- coding: utf-8 -*-
#import math
#import sys
#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class SpaceSwitcher(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName =  "spaceSwitcher"
    nodeID   =  NodeID.SpaceSwitcherID
    #---------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------
    outputMatrix        = OpenMaya.MObject()
    #outputWorldMatrix   = OpenMaya.MObject()
    
    name                = OpenMaya.MObject()
    targetMatrix        = OpenMaya.MObject()
    targetIndex         = OpenMaya.MObject()
    
    offsetMatrix        = OpenMaya.MObject()
    worldInverseParent  = OpenMaya.MObject()
    auxInputParent      = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return SpaceSwitcher()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        #enumAttribute      = OpenMaya.MFnEnumAttribute()
        numericAttribute   = OpenMaya.MFnNumericAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        #CompoundAttribute  = OpenMaya.MFnCompoundAttribute()
        typedAttribute     = OpenMaya.MFnTypedAttribute()
        messageAttribute    = OpenMaya.MFnMessageAttribute()

        #name
        SpaceSwitcher.name = typedAttribute.create("name", "nm", OpenMaya.MFnData.kString )
        SpaceSwitcher.addAttribute(SpaceSwitcher.name)
        
        #---------------------------------------------------------------------------------------
        #targetMatrix
        SpaceSwitcher.targetMatrix = matrixAttribute.create("targetMatrix", "iwm")
        matrixAttribute.writable    = True
        matrixAttribute.readable    = False
        matrixAttribute.storable    = True
        matrixAttribute.keyable     = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        SpaceSwitcher.addAttribute(SpaceSwitcher.targetMatrix)      
        
        #offsetMatrix
        SpaceSwitcher.offsetMatrix = matrixAttribute.create("offsetMatrix", "ow")
        matrixAttribute.writable    = True
        matrixAttribute.readable    = False
        matrixAttribute.storable    = True
        matrixAttribute.keyable     = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        SpaceSwitcher.addAttribute(SpaceSwitcher.offsetMatrix)      
        
        #worldInverseParent
        SpaceSwitcher.worldInverseParent = matrixAttribute.create("worldInverseParent", "iwp")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.storable = True
        matrixAttribute.keyable  = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        SpaceSwitcher.addAttribute(SpaceSwitcher.worldInverseParent)    
      
        
        #auxInputParent
        SpaceSwitcher.auxInputParent = matrixAttribute.create("auxInputParent", "aip")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.storable = True
        matrixAttribute.keyable  = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        SpaceSwitcher.addAttribute(SpaceSwitcher.auxInputParent)      
        
        #scale
        SpaceSwitcher.targetIndex = numericAttribute.create("targetIndex", "ti",OpenMaya.MFnNumericData.kInt ,0)
        numericAttribute.default    = 0
        numericAttribute.writable   = True
        numericAttribute.readable   = True
        numericAttribute.keyable    = True
        numericAttribute.storable   = True
        SpaceSwitcher.addAttribute(SpaceSwitcher.targetIndex)  
        
        #---------------------------------------------------------------------------------------
        #output World
        SpaceSwitcher.outputMatrix = matrixAttribute.create("outputMatrix", "om")
        matrixAttribute.writable    = False
        matrixAttribute.readable    = True
        #matrixAttribute.storable    = True
        #matrixAttribute.keyable    = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset        
        SpaceSwitcher.addAttribute(SpaceSwitcher.outputMatrix)     
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        
        SpaceSwitcher.attributeAffects(SpaceSwitcher.targetMatrix       ,         SpaceSwitcher.outputMatrix)
        SpaceSwitcher.attributeAffects(SpaceSwitcher.targetIndex        ,         SpaceSwitcher.outputMatrix)
        SpaceSwitcher.attributeAffects(SpaceSwitcher.offsetMatrix       ,         SpaceSwitcher.outputMatrix)
        SpaceSwitcher.attributeAffects(SpaceSwitcher.worldInverseParent ,         SpaceSwitcher.outputMatrix)
        SpaceSwitcher.attributeAffects(SpaceSwitcher.auxInputParent     ,         SpaceSwitcher.outputMatrix)
                
        #---------------------------------------------------------------------------------------
    # ______________________________________________________________________________________
    def compute(self, plug, dataBlock):
        
        if (    (plug == self.outputMatrix)
            ):

            # Get Info
            #---------------------------------------------------------------------------------------
            targetMatrix        = (dataBlock.inputValue(self.targetMatrix)).asMatrix() 
            
            offsetMatrix        = (dataBlock.inputValue(self.offsetMatrix)).asMatrix() 
            worldInverseParent  = (dataBlock.inputValue(self.worldInverseParent)).asMatrix()
            
            # Process 
            #---------------------------------------------------------------------------------------
            theOutputMatrix = offsetMatrix * targetMatrix * worldInverseParent
                
            # set values
            #---------------------------------------------------------------------------------------
            dataBlock.outputValue(self.outputMatrix).setMMatrix(theOutputMatrix)
            
            # clean 
            #---------------------------------------------------------------------------------------
            dataBlock.setClean(self.outputMatrix)

