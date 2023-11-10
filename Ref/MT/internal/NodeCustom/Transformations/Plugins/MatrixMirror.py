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

class MatrixMirror(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName = "MatrixMirror"
    nodeID              = NodeID.MatrixMirrorID
    #---------------------------------------------------------------------------------------
    axisDict = {
        "X (+)"     : 0,
        "Y (+)"     : 1,
        "Z (+)"     : 2,
        "XY"        : 3,
        "YZ"        : 4,
        "XZ"        : 5,
        "XYZ (+)"   : 6,
        "None"      : 7
    }
    scaleDict = {
        0   : [-1, 1, 1],  # reflect in YZ plane
        1   : [ 1,-1, 1],  #         in ZX plane
        2   : [ 1, 1,-1],  #         in XY plane
        3   : [-1,-1, 1],
        4   : [ 1,-1,-1],
        5   : [-1, 1,-1],
        6   : [-1,-1,-1],
        7   : [ 1, 1, 1]
    }    
    
    planeDict = {
        "YZ Plane"     : 0,
        "XZ Plane"     : 1,
        "XY Plane"     : 2
    }
    
    #---------------------------------------------------------------------------------------
    mirrorPlane         = OpenMaya.MObject()
    flipAxis            = OpenMaya.MObject()
    #parameters         = OpenMaya.MObject()
    
    inputMatrix         = OpenMaya.MObject()
    pivotMatrix         = OpenMaya.MObject()
    parentInverseMatrix = OpenMaya.MObject()
    
    outputWorldMatrix   = OpenMaya.MObject()
    
    #localOutputs        = OpenMaya.MObject()
    outputMatrix        = OpenMaya.MObject()
    translate           = OpenMaya.MObject()
    rotate              = OpenMaya.MObject()
    rotateX             = OpenMaya.MObject()
    rotateY             = OpenMaya.MObject()
    rotateZ             = OpenMaya.MObject()
    scale               = OpenMaya.MObject()
    shear               = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return MatrixMirror()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        enumAttribute       = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        unitAttribute       = OpenMaya.MFnUnitAttribute()
        CompoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()
        
        #axis
        MatrixMirror.mirrorPlane = enumAttribute.create("mirrorPlane", "mp", 0) #The number is the default value (currently: x)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        enumAttribute.keyable   = True
        for t in MatrixMirror.planeDict:
            enumAttribute.addField(t, MatrixMirror.planeDict[t])
        MatrixMirror.addAttribute(MatrixMirror.mirrorPlane)     
        
        #flipAxis
        MatrixMirror.flipAxis = enumAttribute.create("flipAxis", "fa", 0) #The number is the default value (currently: x)
        enumAttribute.writable  = True
        enumAttribute.readable  = True
        enumAttribute.storable  = True
        enumAttribute.keyable   = True
        for t in MatrixMirror.axisDict:
            enumAttribute.addField(t, MatrixMirror.axisDict[t])
        MatrixMirror.addAttribute(MatrixMirror.flipAxis)     

        ##parameters
        #MatrixMirror.parameters = CompoundAttribute.create("parameters", "pt")
        #CompoundAttribute.addChild(MatrixMirror.mirrorPlane   )  
        #CompoundAttribute.addChild(MatrixMirror.flipAxis   )  
        #CompoundAttribute.writable = True
        #CompoundAttribute.readable = False
        #MatrixMirror.addAttribute(MatrixMirror.parameters)         
        
        #---------------------------------------------------------------------------------------
        #Matrix
        MatrixMirror.inputMatrix = matrixAttribute.create("inputMatrix", "im")
        matrixAttribute.writable    = True
        matrixAttribute.readable    = False
        matrixAttribute.storable    = True
        matrixAttribute.keyable     = True
        #matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        MatrixMirror.addAttribute(MatrixMirror.inputMatrix)      
        
        #pivotMatrix
        MatrixMirror.pivotMatrix = matrixAttribute.create("pivotMatrix", "pm")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        MatrixMirror.addAttribute(MatrixMirror.pivotMatrix)           
        
        #parentInverseMatrix
        MatrixMirror.parentInverseMatrix = matrixAttribute.create("parentInverseMatrix", "pim")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.disconnectBehavior = matrixAttribute.kReset
        MatrixMirror.addAttribute(MatrixMirror.parentInverseMatrix)  
        
        #---------------------------------------------------------------------------------------
        #output World
        MatrixMirror.outputWorldMatrix = matrixAttribute.create("outputWorldMatrix", "owm")
        matrixAttribute.writable = False
        matrixAttribute.readable = True
        #matrixAttribute.keyable = False
        MatrixMirror.addAttribute(MatrixMirror.outputWorldMatrix)      
        
        #output
        MatrixMirror.outputMatrix = matrixAttribute.create("outputMatrix", "om")
        matrixAttribute.writable = False
        matrixAttribute.readable = True
        #matrixAttribute.keyable = False
        #matrixAttribute.storable = True
        MatrixMirror.addAttribute(MatrixMirror.outputMatrix)      
        
        #translate
        MatrixMirror.translate = numericAttribute.createPoint("translate", "t")
        numericAttribute.default = (0,0,0)
        #numericAttribute.default = OpenMaya.MFnNumericData().create([0,0,0])
        numericAttribute.writable = False
        numericAttribute.readable = True
        #numericAttribute.keyable = False
        #numericAttribute.storable = True
        MatrixMirror.addAttribute(MatrixMirror.translate)        
        
        #rotate angle
        MatrixMirror.rotateX = unitAttribute.create("rotateX", "rx", unitAttribute.kAngle, 0.0)
        unitAttribute.writable = False
        unitAttribute.readable = True
        #unitAttribute.keyable = False
        MatrixMirror.addAttribute(MatrixMirror.rotateX)   
        MatrixMirror.rotateY = unitAttribute.create("rotateY", "ry", unitAttribute.kAngle, 0.0)
        unitAttribute.writable = False  
        unitAttribute.readable = True
        #unitAttribute.keyable = False
        MatrixMirror.addAttribute(MatrixMirror.rotateY)   
        MatrixMirror.rotateZ = unitAttribute.create("rotateZ", "rz", unitAttribute.kAngle, 0.0)
        unitAttribute.writable = False
        unitAttribute.readable = True
        #unitAttribute.keyable = False
        MatrixMirror.addAttribute(MatrixMirror.rotateZ)   
        MatrixMirror.rotate = numericAttribute.create("rotate", "r",MatrixMirror.rotateX,MatrixMirror.rotateY,MatrixMirror.rotateZ)
        numericAttribute.keyable = False
        numericAttribute.writable = False
        #numericAttribute.readable = True
        ##numericAttribute.storable = True
        MatrixMirror.addAttribute(MatrixMirror.rotate)   
        
        #scale
        MatrixMirror.scale = numericAttribute.createPoint("scale", "s")
        numericAttribute.default = (1,1,1)
        numericAttribute.writable = False
        numericAttribute.readable = True
        #numericAttribute.keyable = False
        #numericAttribute.storable = True
        MatrixMirror.addAttribute(MatrixMirror.scale)        
        
        #shear
        MatrixMirror.shear = numericAttribute.createPoint("shear", "sh")
        numericAttribute.default = (0,0,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        #numericAttribute.keyable = False
        #numericAttribute.storable = True
        MatrixMirror.addAttribute(MatrixMirror.shear)        

        #localOutputss
        #MatrixMirror.localOutputs = CompoundAttribute.create("localOutputs", "lo")
        #CompoundAttribute.addChild(MatrixMirror.outputMatrix)
        #CompoundAttribute.addChild(MatrixMirror.translate   )
        #CompoundAttribute.addChild(MatrixMirror.rotate      )
        #CompoundAttribute.addChild(MatrixMirror.scale       )
        #CompoundAttribute.addChild(MatrixMirror.shear       )
        #CompoundAttribute.writable = False
        #CompoundAttribute.readable = True
        #MatrixMirror.addAttribute(MatrixMirror.localOutputs) 

        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        # outputWorldMatrix
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.outputWorldMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.outputWorldMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.outputWorldMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.outputWorldMatrix)        
        
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.outputMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.outputMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.outputMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.outputMatrix)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.outputMatrix)            
        #---------------------------------------------------------------------------------------
        # translate
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.translate)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.translate)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.translate)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.translate)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.translate)
        # rotate
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.rotate)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.rotate)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.rotate)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.rotate)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.rotate)
        # rotateX
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.rotateX)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.rotateX)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.rotateX)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.rotateX)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.rotateX)
        # rotateY
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.rotateY)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.rotateY)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.rotateY)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.rotateY)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.rotateY)
        # rotateZ
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.rotateZ)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.rotateZ)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.rotateZ)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.rotateZ)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.rotateZ)
        # scale
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.scale)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.scale)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.scale)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.scale)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.scale)
        # shear
        MatrixMirror.attributeAffects(MatrixMirror.parentInverseMatrix, MatrixMirror.shear)
        MatrixMirror.attributeAffects(MatrixMirror.mirrorPlane,         MatrixMirror.shear)
        MatrixMirror.attributeAffects(MatrixMirror.flipAxis,            MatrixMirror.shear)
        MatrixMirror.attributeAffects(MatrixMirror.pivotMatrix,         MatrixMirror.shear)
        MatrixMirror.attributeAffects(MatrixMirror.inputMatrix,         MatrixMirror.shear)
        #---------------------------------------------------------------------------------------

    # ______________________________________________________________________________________
    def compute(self, plug, dataBlock):
        
        if (    (plug == self.outputWorldMatrix)
            or  (plug == self.outputMatrix)
            or  (plug == self.translate)
            or  (plug == self.rotate)
            or  (plug == self.rotateX)
            or  (plug == self.rotateY)
            or  (plug == self.rotateZ)
            or  (plug == self.scale)
            or  (plug == self.shear)
            ):
            
            # ______________________________________________________________________________________
            # World Transformation 
            #---------------------------------------------------------------------------------------
            theAxis     = (dataBlock.inputValue(self.mirrorPlane)).asShort() 
            theFlipAxis = (dataBlock.inputValue(self.flipAxis)).asShort() 
            thePivotTM  = (dataBlock.inputValue(self.pivotMatrix)).asMatrix() 
            theTM       = (dataBlock.inputValue(self.inputMatrix)).asMatrix() 
            
            MSpace      = OpenMaya.MSpace.kTransform
            aReflection = OpenMaya.MTransformationMatrix().setScale(self.scaleDict[theAxis],MSpace).asMatrix()
            fReflection = OpenMaya.MTransformationMatrix().setScale(self.scaleDict[theFlipAxis],MSpace).asMatrix()
            
            theOutputWorldMatrix = (fReflection * (theTM * (thePivotTM.inverse())) * aReflection * thePivotTM)
            
            # Local transformation 
            #---------------------------------------------------------------------------------------
            
            theParentInverseMatrix = (dataBlock.inputValue(self.parentInverseMatrix)).asMatrix() 
            theLocalMatrix  = theOutputWorldMatrix * theParentInverseMatrix
            
            theLocalTM      = OpenMaya.MTransformationMatrix(theLocalMatrix)
            
            theTraslation   = theLocalTM.translation(OpenMaya.MSpace.kTransform)
            theRotation     = theLocalTM.rotation(asQuaternion=False)
            theScale        = theLocalTM.scale(OpenMaya.MSpace.kTransform)
            theShear        = theLocalTM.shear(OpenMaya.MSpace.kTransform)
            
            # ______________________________________________________________________________________
            # set values
            dataBlock.outputValue(self.outputWorldMatrix).setMMatrix(theOutputWorldMatrix)
            dataBlock.outputValue(self.outputMatrix).setMMatrix(theLocalMatrix)
            dataBlock.outputValue(self.translate).set3Float(theTraslation.x,theTraslation.y,theTraslation.z)
            dataBlock.outputValue(self.rotateX).setMAngle(OpenMaya.MAngle(theRotation.x))
            dataBlock.outputValue(self.rotateY).setMAngle(OpenMaya.MAngle(theRotation.y))
            dataBlock.outputValue(self.rotateZ).setMAngle(OpenMaya.MAngle(theRotation.z))
            dataBlock.outputValue(self.scale).set3Float(theScale[0],theScale[1],theScale[2])
            dataBlock.outputValue(self.shear).set3Float(theShear[0],theShear[1],theShear[2])
            
            # clean 
            #---------------------------------------------------------------------------------------
            dataBlock.setClean(self.outputWorldMatrix)
            dataBlock.setClean(self.outputMatrix)
            dataBlock.setClean(self.translate)
            dataBlock.setClean(self.rotate)
            dataBlock.setClean(self.rotateX)
            dataBlock.setClean(self.rotateY)
            dataBlock.setClean(self.rotateZ)
            dataBlock.setClean(self.scale)
            dataBlock.setClean(self.shear)
