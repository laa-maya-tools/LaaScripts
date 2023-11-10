# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as om
#import maya.api.OpenMayaUI as omui

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class Point3MathList(om.MPxNode, PluginNodes.PluginNode):
    
    #---------------------------------------------------------------------------------------
    # Plugin data
    nodeName      = "point3MathList"
    nodeID        = NodeID.Point3MathListID

    operation     = om.MObject()
    list          = om.MObject()
    connectedOnly = om.MObject()
    
    output        = om.MObject()
    outputX       = om.MObject()
    outputY       = om.MObject()
    outputZ       = om.MObject()
       
    #---------------------------------------------------------------------------------------
    #Method to return an instance    
    @staticmethod
    def creator():
        return Point3MathList()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute    = om.MFnMatrixAttribute()
        enumAttribute       = om.MFnEnumAttribute()
        numericAttribute    = om.MFnNumericAttribute()
        #unitAttribute      = om.MFnUnitAttribute()
        #compoundAttribute  = om.MFnCompoundAttribute()
        #typedAttribute     = om.MFnTypedAttribute()
        #messageAttribute   = om.MFnMessageAttribute()

        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------   
        
        #vectors
        Point3MathList.list = numericAttribute.createPoint("list", "l")
        #numericAttribute.dafault       = (0.0,0.0,0.0)
        #numericAttribute.array         = True
        numericAttribute.array          = True
        numericAttribute.writable       = True
        numericAttribute.readable       = True
        numericAttribute.keyable        = False
        numericAttribute.storable       = True
        Point3MathList.addAttribute(Point3MathList.list)  
        
        Point3MathList.operation = enumAttribute.create("operation", "op", defaultValue=0) #The number is the default value (currently: x)
        for t in Point3MathList.operationDict:
            enumAttribute.addField(t, Point3MathList.operationDict[t])
        numericAttribute.writable   = True
        numericAttribute.readable   = True
        numericAttribute.keyable    = False
        numericAttribute.storable   = True
        Point3MathList.addAttribute(Point3MathList.operation)  
        
        Point3MathList.connectedOnly    = numericAttribute.create("connectedOnly", "cb", om.MFnNumericData.kBoolean, False)  
        numericAttribute.writable       = True
        numericAttribute.readable       = True
        numericAttribute.keyable        = False
        numericAttribute.storable       = True
        Point3MathList.addAttribute(Point3MathList.connectedOnly)          
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        
        #outputX 
        Point3MathList.outputX   = numericAttribute.create("outputX", "ox", om.MFnNumericData.kFloat, 0.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #Point3MathList.addAttribute(Point3MathList.outputX)      

        #outputY 
        Point3MathList.outputY   = numericAttribute.create("outputY", "oy", om.MFnNumericData.kFloat, 0.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #Point3MathList.addAttribute(Point3MathList.outputY)      

        #outputZ 
        Point3MathList.outputZ   = numericAttribute.create("outputZ", "oz", om.MFnNumericData.kFloat, 0.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #Point3MathList.addAttribute(Point3MathList.outputZ)      

        #output    
        Point3MathList.output     = numericAttribute.create("output", "o", Point3MathList.outputX, Point3MathList.outputY, Point3MathList.outputZ)  
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        Point3MathList.addAttribute(Point3MathList.output)      
        
              
        Point3MathList.attributeAffects(Point3MathList.operation,   Point3MathList.output)
        Point3MathList.attributeAffects(Point3MathList.list,        Point3MathList.output)
        
        Point3MathList.attributeAffects(Point3MathList.operation,     Point3MathList.output)
        Point3MathList.attributeAffects(Point3MathList.list,          Point3MathList.output)
        Point3MathList.attributeAffects(Point3MathList.connectedOnly, Point3MathList.output)
        
        Point3MathList.attributeAffects(Point3MathList.operation,     Point3MathList.outputX)
        Point3MathList.attributeAffects(Point3MathList.list,          Point3MathList.outputX)
        Point3MathList.attributeAffects(Point3MathList.connectedOnly, Point3MathList.outputX)
        
        Point3MathList.attributeAffects(Point3MathList.operation,     Point3MathList.outputY)
        Point3MathList.attributeAffects(Point3MathList.list,          Point3MathList.outputY)
        Point3MathList.attributeAffects(Point3MathList.connectedOnly, Point3MathList.outputY)
        
        Point3MathList.attributeAffects(Point3MathList.operation,     Point3MathList.outputZ)
        Point3MathList.attributeAffects(Point3MathList.list,          Point3MathList.outputZ)
        Point3MathList.attributeAffects(Point3MathList.connectedOnly, Point3MathList.outputZ)
        
        
    #-------------------------------------------------------------------------------------------------------------------------------
    
    operationDict = {
        "add"       : 0,
        "subtract"  : 1,
        "multiply"  : 2,
        "divide"    : 3
    }
    
    valueInitDict = {
        0  : [0,0,0],
        1  : [0,0,0],
        2  : [1,1,1],
        3  : [1,1,1]
    }
    
    def fnOperation(self, operationIndex, a, b):
        operation = {
            0  : a+b,
            1  : a-b,
            2  : a*b,
            3  : (0 if (a==0 or b==0) else (a/b))
        }
        return operation[operationIndex]

    def fnCompute(self, mPlug, operationIndex):
        indexList = mPlug.getExistingArrayAttributeIndices()
        if indexList:
            result = self.valueInitDict[operationIndex].copy()
            for i in indexList:
                for j in range(3):
                    result[j] = self.fnOperation(operationIndex, result[j], mPlug.elementByPhysicalIndex(i).child(j).asFloat())
        else:
            result = [0,0,0]
        return result

    def fnComputeConnectedOnly(self, mPlug, operationIndex):
        indexList = mPlug.getExistingArrayAttributeIndices()
        if indexList:
            result = self.valueInitDict[operationIndex].copy()
            for i in indexList:
                if not (mPlug.elementByLogicalIndex(i)).isDestination:  
                    continue
                else:
                    for j in range(3):
                        result[j] = self.fnOperation(operationIndex, result[j], mPlug.elementByPhysicalIndex(i).child(j).asFloat())
            return result            
        else:
            return [0,0,0] 

    def compute(self, plug, dataBlock):
        # TODO revisar si cambio el point3 completo o filtro según demanda para optimizar
        if (     
            (plug == self.output),
            (plug == self.outputX),
            (plug == self.outputY),
            (plug == self.outputZ)
        ):

            operationIndex  = (dataBlock.inputValue(self.operation)).asShort()
            listAttr = om.MFnDependencyNode(self.thisMObject()).findPlug(self.list,False)
            connectedOnly = dataBlock.inputValue(self.connectedOnly).asBool() 
            
            if connectedOnly:
                result = self.fnComputeConnectedOnly(listAttr, operationIndex)
            else:
                result = self.fnCompute(listAttr, operationIndex)
                
            ## ______________________________________________________________________________________
            ## set values
             
            output = dataBlock.outputValue(self.output)
            output.set3Float(result[0], result[1], result[2])           
        
            # clean 
            #---------------------------------------------------------------------------------------
            #dataBlock.setClean(plug)
            
            dataBlock.setClean(self.output)
            dataBlock.setClean(self.outputX)
            dataBlock.setClean(self.outputY)
            dataBlock.setClean(self.outputZ)
 

