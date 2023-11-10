# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class LookQuaternion(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName                = "lookQuaternion"
    nodeID                  = NodeID.LookQuaternionID

    originControlAxis       = OpenMaya.MObject()
    lookAxisVector          = OpenMaya.MObject()
    
    mainVector              = OpenMaya.MObject()
    originControlMatrix     = OpenMaya.MObject()
    aimTargetMatrix         = OpenMaya.MObject()
    inverseParentMatrix     = OpenMaya.MObject()
    
    outputMatrix            = OpenMaya.MObject()

    rotate                  = OpenMaya.MObject()
    rotateX                 = OpenMaya.MObject()
    rotateY                 = OpenMaya.MObject()
    rotateZ                 = OpenMaya.MObject()
    
    direction               = OpenMaya.MObject() 
    
    #---------------------------------------------------------------------------------------
    axisDict = {
        "X"     : 0,
        "Y"     : 1,
        "Z"     : 2
    }
    vectorDict = {
        0     : [1,0,0],
        1     : [0,1,0],
        2     : [0,0,1]
    } 
    
    boolDict = {
        True    : -1,
        False   : 1
    }
    
    #---------------------------------------------------------------------------------------
    #Method to return an instance    
    @staticmethod
    def creator():
        return LookQuaternion()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        enumAttribute       = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        unitAttribute       = OpenMaya.MFnUnitAttribute()
        compoundAttribute   = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()

        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------   
        #direction
        LookQuaternion.direction = numericAttribute.create("direction", "d", OpenMaya.MFnNumericData.kBoolean ,False) 
        numericAttribute.writable = True
        numericAttribute.readable = True
        LookQuaternion.addAttribute(LookQuaternion.direction)  
        
        #axis
        LookQuaternion.originControlAxis = enumAttribute.create("originControlAxis", "oca", 0) #The number is the default value (currently: x)
        enumAttribute.writable = True
        enumAttribute.readable = True
        #enumAttribute.storable = True
        for t in LookQuaternion.axisDict:
            enumAttribute.addField(t, LookQuaternion.axisDict[t])
        LookQuaternion.addAttribute(LookQuaternion.originControlAxis)     
        
        #axis
        LookQuaternion.lookAxisVector = enumAttribute.create("lookAxisVector", "lav", 0) #The number is the default value (currently: x)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        for t in LookQuaternion.axisDict:
            enumAttribute.addField(t, LookQuaternion.axisDict[t])
        LookQuaternion.addAttribute(LookQuaternion.lookAxisVector)     
        
        #originControlMatrix
        LookQuaternion.originControlMatrix = matrixAttribute.create("originControlMatrix", "ocm")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.keyable  = False
        LookQuaternion.addAttribute(LookQuaternion.originControlMatrix)           

        #aimTargetMatrix
        LookQuaternion.aimTargetMatrix = matrixAttribute.create("aimTargetMatrix", "atm")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.keyable  = False
        LookQuaternion.addAttribute(LookQuaternion.aimTargetMatrix)           

        #localOutputss
        LookQuaternion.mainVector = compoundAttribute.create("mainVector", "mv")
        compoundAttribute.addChild(LookQuaternion.originControlAxis     )
        compoundAttribute.addChild(LookQuaternion.lookAxisVector  )
        compoundAttribute.addChild(LookQuaternion.originControlMatrix   )
        compoundAttribute.addChild(LookQuaternion.aimTargetMatrix   )
        compoundAttribute.writable = True
        compoundAttribute.readable = False
        LookQuaternion.addAttribute(LookQuaternion.mainVector)

        #inverseParentMatrix
        LookQuaternion.inverseParentMatrix = matrixAttribute.create("inverseParentMatrix", "ipm")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.keyable  = False
        LookQuaternion.addAttribute(LookQuaternion.inverseParentMatrix)           

        #outputMatrix
        LookQuaternion.outputMatrix = matrixAttribute.create("outputMatrix", "om")
        matrixAttribute.writable = False
        matrixAttribute.readable = True
        matrixAttribute.keyable  = False
        LookQuaternion.addAttribute(LookQuaternion.outputMatrix)           

        #rotate angle
        LookQuaternion.rotateX = unitAttribute.create("rotateX", "rx", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        LookQuaternion.addAttribute(LookQuaternion.rotateX)   
        LookQuaternion.rotateY = unitAttribute.create("rotateY", "ry", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        LookQuaternion.addAttribute(LookQuaternion.rotateY)   
        LookQuaternion.rotateZ = unitAttribute.create("rotateZ", "rz", unitAttribute.kAngle, 0.0)
        unitAttribute.writable  = False
        unitAttribute.readable  = True
        LookQuaternion.addAttribute(LookQuaternion.rotateZ)   

        LookQuaternion.rotate = numericAttribute.create("rotate", "r",LookQuaternion.rotateX,LookQuaternion.rotateY,LookQuaternion.rotateZ)
        numericAttribute.writable = False
        numericAttribute.readable = True
        LookQuaternion.addAttribute(LookQuaternion.rotate)   
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        
        LookQuaternion.attributeAffects(LookQuaternion.originControlMatrix,   LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.originControlMatrix,   LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.originControlMatrix,   LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.originControlMatrix,   LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.originControlMatrix,   LookQuaternion.outputMatrix)  

        LookQuaternion.attributeAffects(LookQuaternion.aimTargetMatrix,       LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.aimTargetMatrix,       LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.aimTargetMatrix,       LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.aimTargetMatrix,       LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.aimTargetMatrix,       LookQuaternion.outputMatrix)
        
        LookQuaternion.attributeAffects(LookQuaternion.inverseParentMatrix,   LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.inverseParentMatrix,   LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.inverseParentMatrix,   LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.inverseParentMatrix,   LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.inverseParentMatrix,   LookQuaternion.outputMatrix)
        
        LookQuaternion.attributeAffects(LookQuaternion.originControlAxis,     LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.originControlAxis,     LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.originControlAxis,     LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.originControlAxis,     LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.originControlAxis,     LookQuaternion.outputMatrix)

        LookQuaternion.attributeAffects(LookQuaternion.lookAxisVector,        LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.lookAxisVector,        LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.lookAxisVector,        LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.lookAxisVector,        LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.lookAxisVector,        LookQuaternion.outputMatrix)

        LookQuaternion.attributeAffects(LookQuaternion.direction,        LookQuaternion.rotate)
        LookQuaternion.attributeAffects(LookQuaternion.direction,        LookQuaternion.rotateX)
        LookQuaternion.attributeAffects(LookQuaternion.direction,        LookQuaternion.rotateY)
        LookQuaternion.attributeAffects(LookQuaternion.direction,        LookQuaternion.rotateZ)
        LookQuaternion.attributeAffects(LookQuaternion.direction,        LookQuaternion.outputMatrix)
    #-------------------------------------------------------------------------------------------------------------------------------
        
    def compute(self, plug, dataBlock):
        if (    (plug == self.rotate)
            or  (plug == self.rotateX)
            or  (plug == self.rotateY)
            or  (plug == self.rotateZ)
            or  (plug == self.outputMatrix)
        ):
        
            direcction =  (dataBlock.inputValue(self.direction)).asBool()  
            
            origenControlMM = (dataBlock.inputValue(self.originControlMatrix)).asMatrix()  
            inverseParentMM = (dataBlock.inputValue(self.inverseParentMatrix)).asMatrix() 
            
            lookAxisVectorIndex    = (dataBlock.inputValue(self.lookAxisVector)).asShort() 
            axisVector   = OpenMaya.MVector(self.vectorDict[lookAxisVectorIndex] )

            # TODO con esta condicion podemos obtener el vector principal de dos posiciones o un eje de la matriz originControlMM (tengo dudas si mantener la opcion eje o menterlo en otro nodo) 
            if OpenMaya.MFnDependencyNode(self.thisMObject()).findPlug(self.aimTargetMatrix, False).isConnected:
                aimTargetTM   = OpenMaya.MTransformationMatrix((dataBlock.inputValue(self.aimTargetMatrix)).asMatrix()  )
                origenControlTM   = OpenMaya.MTransformationMatrix(origenControlMM)
                mainVector = (aimTargetTM.translation(OpenMaya.MSpace.kWorld) - origenControlTM.translation(OpenMaya.MSpace.kWorld))  * inverseParentMM
            else:   
                originControlAxisIndex    = (dataBlock.inputValue(self.originControlAxis)).asShort()
                mainVector = OpenMaya.MVector([origenControlMM.getElement(originControlAxisIndex,0), origenControlMM.getElement(originControlAxisIndex,1), origenControlMM.getElement(originControlAxisIndex,2)])  * inverseParentMM
            
            axis = self.boolDict[direcction] * ((axisVector ^ mainVector).normalize())
            angle = mainVector.angle(axisVector)

            quat = OpenMaya.MQuaternion(angle,axis)
            euler = quat.asEulerRotation()
            matrix = euler.asMatrix()
            
            # ______________________________________________________________________________________
            # set values
            dataBlock.outputValue(self.outputMatrix).setMMatrix(matrix)
            dataBlock.outputValue(self.rotateX).setMAngle(OpenMaya.MAngle(euler.x))
            dataBlock.outputValue(self.rotateY).setMAngle(OpenMaya.MAngle(euler.y))
            dataBlock.outputValue(self.rotateZ).setMAngle(OpenMaya.MAngle(euler.z))            
            # clean 
            #---------------------------------------------------------------------------------------
            dataBlock.setClean(self.rotate)
            dataBlock.setClean(self.rotateX)
            dataBlock.setClean(self.rotateY)
            dataBlock.setClean(self.rotateZ)
            dataBlock.setClean(self.outputMatrix)

