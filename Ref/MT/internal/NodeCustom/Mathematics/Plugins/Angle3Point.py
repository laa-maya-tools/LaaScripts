# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class Angle3Point(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName            = "angle3Point"
    nodeID              = NodeID.Angle3PointID
    
    angleFrom3Matrix    = OpenMaya.MObject()
    origenMatrix        = OpenMaya.MObject()
    target1Matrix       = OpenMaya.MObject()
    target2Matrix       = OpenMaya.MObject()

    angle               = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return Angle3Point()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute    = OpenMaya.MFnMatrixAttribute()
        #enumAttribute     = OpenMaya.MFnEnumAttribute()
        #numericAttribute  = OpenMaya.MFnNumericAttribute()
        unitAttribute      = OpenMaya.MFnUnitAttribute()
        compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute    = OpenMaya.MFnTypedAttribute()
        #messageAttribute  = OpenMaya.MFnMessageAttribute()
        
        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------
        #Matrix
        Angle3Point.origenMatrix = matrixAttribute.create("origenMatrix", "om")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        Angle3Point.addAttribute(Angle3Point.origenMatrix)   
        
        #Matrix
        Angle3Point.target1Matrix = matrixAttribute.create("target1Matrix", "m1")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        Angle3Point.addAttribute(Angle3Point.target1Matrix)   
        
        #Matrix
        Angle3Point.target2Matrix = matrixAttribute.create("target2Matrix", "t2m")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        Angle3Point.addAttribute(Angle3Point.target2Matrix)   
        
        #reference COMPOUND
        Angle3Point.angleFrom3Matrix = compoundAttribute.create("angleFrom3Matrix", "af3m")
        compoundAttribute.addChild(Angle3Point.origenMatrix   )  
        compoundAttribute.addChild(Angle3Point.target1Matrix   )  
        compoundAttribute.addChild(Angle3Point.target2Matrix   )  
        compoundAttribute.writable = True
        compoundAttribute.readable = False
        Angle3Point.addAttribute(Angle3Point.angleFrom3Matrix)
        
        Angle3Point.angle = unitAttribute.create("angle", "a", unitAttribute.kAngle, 0.0)
        unitAttribute.writable = False
        unitAttribute.readable = True
        Angle3Point.addAttribute(Angle3Point.angle)   
        
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        # outputWorldMatrix
        Angle3Point.attributeAffects(Angle3Point.origenMatrix     , Angle3Point.angle)
        Angle3Point.attributeAffects(Angle3Point.target1Matrix    , Angle3Point.angle)
        Angle3Point.attributeAffects(Angle3Point.target2Matrix    , Angle3Point.angle)
        
    def compute(self, plug, dataBlock):
        if plug == self.angle:
            vectorO   = OpenMaya.MTransformationMatrix((dataBlock.inputValue(self.origenMatrix)).asMatrix() ).translation(OpenMaya.MSpace.kWorld)
            vectorA   = OpenMaya.MTransformationMatrix((dataBlock.inputValue(self.target1Matrix)).asMatrix()).translation(OpenMaya.MSpace.kWorld)
            vectorB   = OpenMaya.MTransformationMatrix((dataBlock.inputValue(self.target2Matrix)).asMatrix()).translation(OpenMaya.MSpace.kWorld)
            
            vector1N = (vectorA -vectorO).normalize()
            vector2N = (vectorB -vectorO).normalize()
            
            val = vector1N.angle(vector2N)
            # ______________________________________________________________________________________
            # set values
            dataBlock.outputValue(self.angle).setMAngle(OpenMaya.MAngle(val))
            # clean 
            #---------------------------------------------------------------------------------------
            dataBlock.setClean(plug)
