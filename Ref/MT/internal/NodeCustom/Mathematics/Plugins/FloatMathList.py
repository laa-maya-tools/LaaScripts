# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as om
#import maya.api.omUI as omui

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class FloatMathList(om.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName        = "floatMathList"
    nodeID          = NodeID.FloatMathListID
    
    output          = om.MObject()
    list            = om.MObject()  
    operation       = om.MObject()
    connectedOnly   = om.MObject()
    
    #---------------------------------------------------------------------------------------
    #Method to return an instance    
    @staticmethod
    def creator():
        return FloatMathList()
    
    @staticmethod
    def initializer():
        
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute     = om.MFnMatrixAttribute()
        enumAttribute       = om.MFnEnumAttribute()
        numericAttribute    = om.MFnNumericAttribute()
        #unitAttribute       = om.MFnUnitAttribute()
        #compoundAttribute   = om.MFnCompoundAttribute()
        #typedAttribute     = om.MFnTypedAttribute()
        #messageAttribute   = om.MFnMessageAttribute()

        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------   
        
        FloatMathList.operation = enumAttribute.create("operation", "op", defaultValue=0)  
        for t in FloatMathList.operationDict:
            enumAttribute.addField(t, FloatMathList.operationDict[t])
        enumAttribute.writable   = True
        enumAttribute.readable   = True
        enumAttribute.keyable    = False
        enumAttribute.storable   = True
        FloatMathList.addAttribute(FloatMathList.operation)           
        
        FloatMathList.connectedOnly = numericAttribute.create("connectedOnly", "cb", om.MFnNumericData.kBoolean, False)  
        numericAttribute.writable   = True
        numericAttribute.readable   = True
        numericAttribute.keyable    = False
        numericAttribute.storable   = True
        FloatMathList.addAttribute(FloatMathList.connectedOnly)  
        
        FloatMathList.list = numericAttribute.create("list", "l", om.MFnNumericData.kFloat, 0.0) 
        numericAttribute.array      = True
        #numericAttribute.usesArrayDataBuilder =True
        numericAttribute.writable   = True
        numericAttribute.readable   = True
        numericAttribute.keyable    = True
        numericAttribute.storable   = True
        FloatMathList.addAttribute(FloatMathList.list)  
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        #outputX 
        FloatMathList.output   = numericAttribute.create("output", "o", om.MFnNumericData.kFloat, 0.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        FloatMathList.addAttribute(FloatMathList.output)      
        
        FloatMathList.attributeAffects(FloatMathList.operation,     FloatMathList.output)
        FloatMathList.attributeAffects(FloatMathList.list,          FloatMathList.output)
        FloatMathList.attributeAffects(FloatMathList.connectedOnly, FloatMathList.output)
        
 
    #-------------------------------------------------------------------------------------------------------------------------------

    operationDict = {
        "add"       : 0,
        "subtract"  : 1,
        "multiply"  : 2,
        "divide"    : 3
    }  
    
    valueInitDict = {
        0  : 0,
        1  : 0,
        2  : 1,
        3  : 1
    }
    
    def fnOperation(self, operationIndex, a, b):
        operation = {
            0  : a+b,
            1  : a-b,
            2  : a*b,
            3  : (0 if (a==0 or b==0) else (a/b) )
        }   
        return operation[operationIndex]
    
    def fnComputeFloatConnectedOnly(self, mPlug, operationIndex):
        indexList = mPlug.getExistingArrayAttributeIndices()
        if indexList:
            result = self.valueInitDict[operationIndex]
            for i in indexList:
                if not (mPlug.elementByLogicalIndex(i)).isDestination:  
                    continue
                else:
                    result = self.fnOperation(operationIndex, result, mPlug.elementByLogicalIndex(i).asFloat() )
            return result            
        else:
            return 0 

    def fnComputeFloat(self, mPlug, operationIndex):
        indexList = mPlug.getExistingArrayAttributeIndices()      
        if indexList:
            result = self.valueInitDict[operationIndex]
            for i in indexList:
                result = self.fnOperation(operationIndex, result, mPlug.elementByPhysicalIndex(i).asFloat())
        else:    
            result = 0
        return result             
                             
    def compute(self, plug, dataBlock):
        if (    
            (plug == self.output)
        ):
            operationIndex  = (dataBlock.inputValue(self.operation)).asShort()
            listAttr = om.MFnDependencyNode(self.thisMObject()).findPlug(self.list,False)
            
            connectedOnly = dataBlock.inputValue(self.connectedOnly).asBool() 
            if connectedOnly:
                result = self.fnComputeFloatConnectedOnly(listAttr, operationIndex)
            else:
                result = self.fnComputeFloat(listAttr, operationIndex)
                
            ## ______________________________________________________________________________________
            ## set values
             
            output = dataBlock.outputValue(plug)
            output.setFloat(result)             
            
            # clean 
            #---------------------------------------------------------------------------------------
            dataBlock.setClean(plug)


