# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class AngleReaction(OpenMaya.MPxNode, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName         = "angleReaction"
    nodeID           = NodeID.AngleReactionID
        
    worldOriginMatrix     = OpenMaya.MObject()
    worldTargetMatrix     = OpenMaya.MObject()
    
    angle1pos       = OpenMaya.MObject()
    angle1neg       = OpenMaya.MObject()
    angle2pos       = OpenMaya.MObject()
    angle2neg       = OpenMaya.MObject()
    
    quadrantPP      = OpenMaya.MObject()
    quadrantNP      = OpenMaya.MObject()
    quadrantNN      = OpenMaya.MObject()
    quadrantPN      = OpenMaya.MObject()
    
    output              = OpenMaya.MObject()
    
    correctionAngle1pos       = OpenMaya.MObject()
    correctionAngle1neg       = OpenMaya.MObject()
    correctionAngle2pos       = OpenMaya.MObject()
    correctionAngle2neg       = OpenMaya.MObject()
    
    correctionquadrantPP      = OpenMaya.MObject()
    correctionquadrantNP      = OpenMaya.MObject()
    correctionquadrantNN      = OpenMaya.MObject()
    correctionquadrantPN      = OpenMaya.MObject()
    
    correctionOutput    = OpenMaya.MObject()
    
    originAxis        = OpenMaya.MObject()
    targetAxis        = OpenMaya.MObject()
    
    negativeFirstAxis   = OpenMaya.MObject()
    negativeSecondAxis  = OpenMaya.MObject()
    negativeThirdAxis   = OpenMaya.MObject()
    
    #---------------------------------------------------------------------------------------
    axisOrderDict = {
        "XYZ"     : 0,
        "XZY"     : 1,
        "YXZ"     : 2,
        "YZX"     : 3,
        "ZXY"     : 4,
        "ZYX"     : 5
    }

    indexDict = {
        0     : [0,1,2],
        1     : [0,2,1],
        2     : [1,0,2],
        3     : [1,2,0],
        4     : [2,0,1],
        5     : [2,1,0]
    }    
    
    boolDict = {
        True    : -1,
        False   : 1
    }
    
    #---------------------------------------------------------------------------------------
    #Method to return an instance    
    @staticmethod
    def creator():
        return AngleReaction()

    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        enumAttribute       = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        compoundAttribute   = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()

        # ________________________________________________________________________________________________________________________________________________
        #originAxis
        AngleReaction.originAxis = enumAttribute.create("originAxis", "oa", 0) #The number is the default value (currently: x)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        for t in AngleReaction.axisOrderDict:
            enumAttribute.addField(t, AngleReaction.axisOrderDict[t])
        AngleReaction.addAttribute(AngleReaction.originAxis)     
        
        #targetAxis
        AngleReaction.targetAxis = enumAttribute.create("targetAxis", "ta", 0) #The number is the default value (currently: x)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        for t in AngleReaction.axisOrderDict:
            enumAttribute.addField(t, AngleReaction.axisOrderDict[t])
        AngleReaction.addAttribute(AngleReaction.targetAxis)     
        
        AngleReaction.negativeFirstAxis = numericAttribute.create("negativeFirstAxis", "nfa", OpenMaya.MFnNumericData.kBoolean, False) #The number is the default value (currently: x)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.negativeFirstAxis)  
        
        AngleReaction.negativeSecondAxis = numericAttribute.create("negativeSecondAxis", "nsa", OpenMaya.MFnNumericData.kBoolean, False) #The number is the default value (currently: x)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.negativeSecondAxis)  
        
        AngleReaction.negativeThirdAxis = numericAttribute.create("negativeThirdAxis", "nta", OpenMaya.MFnNumericData.kBoolean, False) #The number is the default value (currently: x)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.negativeThirdAxis)  
        
        #worldTargetMatrix
        AngleReaction.worldTargetMatrix = matrixAttribute.create("worldTargetMatrix", "wtm")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        AngleReaction.addAttribute(AngleReaction.worldTargetMatrix)   
        
        #worldOriginMatrix
        AngleReaction.worldOriginMatrix = matrixAttribute.create("worldOriginMatrix", "wom")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        AngleReaction.addAttribute(AngleReaction.worldOriginMatrix)   
        
        # ________________________________________________________________________________________________________________________________________________
        
        AngleReaction.quadrantPP = numericAttribute.create("quadrantPP", "cpp", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.quadrantPP)  
        
        AngleReaction.quadrantNP = numericAttribute.create("quadrantNP", "cnp", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.quadrantNP)  
        
        AngleReaction.quadrantNN = numericAttribute.create("quadrantNN", "cnn", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.quadrantNN)  
        
        AngleReaction.quadrantPN = numericAttribute.create("quadrantPN", "cpn", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.quadrantPN)  

        AngleReaction.angle1pos = numericAttribute.create("angle1pos", "a1p", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.angle1pos)  
        
        AngleReaction.angle1neg = numericAttribute.create("angle1neg", "a1n", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.angle1neg)  
        
        AngleReaction.angle2pos = numericAttribute.create("angle2pos", "a2p", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.angle2pos)  
        
        AngleReaction.angle2neg = numericAttribute.create("angle2neg", "a2n", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.angle2neg)  
        
        #reference COMPOUND
        AngleReaction.output = compoundAttribute.create("output", "o")
        
        compoundAttribute.addChild(AngleReaction.angle1pos)  
        compoundAttribute.addChild(AngleReaction.angle1neg)  
        compoundAttribute.addChild(AngleReaction.angle2pos)  
        compoundAttribute.addChild(AngleReaction.angle2neg)  
        
        compoundAttribute.addChild(AngleReaction.quadrantPP)  
        compoundAttribute.addChild(AngleReaction.quadrantNP)  
        compoundAttribute.addChild(AngleReaction.quadrantNN)  
        compoundAttribute.addChild(AngleReaction.quadrantPN)  
        compoundAttribute.writable = False
        compoundAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.output)
        
        # ________________________________________________________________________________________________________________________________________________
        
        AngleReaction.correctionquadrantPP = numericAttribute.create("correctionquadrantPP", "ccpp", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionquadrantPP)  
        
        AngleReaction.correctionquadrantNP = numericAttribute.create("correctionquadrantNP", "ccnp", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionquadrantNP)  
        
        AngleReaction.correctionquadrantNN = numericAttribute.create("correctionquadrantNN", "ccnn", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionquadrantNN)  
        
        AngleReaction.correctionquadrantPN = numericAttribute.create("correctionquadrantPN", "ccpn", OpenMaya.MFnNumericData.kFloat,0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionquadrantPN)  

        AngleReaction.correctionAngle1pos = numericAttribute.create("correctionAngle1pos", "ca1p", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionAngle1pos)  
        
        AngleReaction.correctionAngle1neg = numericAttribute.create("correctionAngle1neg", "ca1n", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionAngle1neg)  
        
        AngleReaction.correctionAngle2pos = numericAttribute.create("correctionAngle2pos", "ca2p", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionAngle2pos)  
        
        AngleReaction.correctionAngle2neg = numericAttribute.create("correctionAngle2neg", "ca2n", OpenMaya.MFnNumericData.kFloat, 0.0)
        numericAttribute.writable = True
        numericAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionAngle2neg)  
        
        #reference COMPOUND
        AngleReaction.correctionOutput = compoundAttribute.create("correctionOutput", "co")
        
        compoundAttribute.addChild(AngleReaction.correctionAngle1pos)  
        compoundAttribute.addChild(AngleReaction.correctionAngle1neg)  
        compoundAttribute.addChild(AngleReaction.correctionAngle2pos)  
        compoundAttribute.addChild(AngleReaction.correctionAngle2neg)  
        
        compoundAttribute.addChild(AngleReaction.correctionquadrantPP)  
        compoundAttribute.addChild(AngleReaction.correctionquadrantNP)  
        compoundAttribute.addChild(AngleReaction.correctionquadrantNN)  
        compoundAttribute.addChild(AngleReaction.correctionquadrantPN)  
        compoundAttribute.writable = True
        compoundAttribute.readable = True
        AngleReaction.addAttribute(AngleReaction.correctionOutput)        
        
        ##############################################################################################################################################
        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.worldOriginMatrix, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.worldTargetMatrix, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.originAxis, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.targetAxis, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.negativeFirstAxis, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.negativeSecondAxis, AngleReaction.output)
        
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.angle1pos)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.angle1neg)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.angle2pos)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.angle2neg)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.quadrantPP)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.quadrantNP)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.quadrantNN)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.quadrantPN)
        AngleReaction.attributeAffects(AngleReaction.negativeThirdAxis, AngleReaction.output)
    
    ##############################################################################################################################################
    
    def getLocalLookValue(self, dataBlock):
        worldOMM    = (dataBlock.inputValue(self.worldOriginMatrix)).asMatrix()
        worldTMM    = (dataBlock.inputValue(self.worldTargetMatrix)).asMatrix() #* worldOMM
        nFirstAxis  = (dataBlock.inputValue(self.negativeFirstAxis )).asBool()
        tAxisIndex   = self.indexDict[(dataBlock.inputValue(self.targetAxis)).asShort()]
        mainTargetRow = OpenMaya.MVector(worldTMM.getElement(tAxisIndex[0],0), worldTMM.getElement(tAxisIndex[0],1), worldTMM.getElement(tAxisIndex[0],2)).normalize()   * self.boolDict[nFirstAxis] 
        localMainTargetRow  = mainTargetRow * worldOMM.inverse()
        return localMainTargetRow[tAxisIndex[0]]
    
    def getQuadrantValue(self,firstVal,secondVal,lookVal):
        if (abs(firstVal)<=abs(secondVal)):
            return abs(firstVal)/max(abs(secondVal),0.001)*(1-abs(lookVal))
        else:
            return abs(secondVal)/max(abs(firstVal),0.001)*(1-abs(lookVal))
    
    def getQuadrantResult(self, a, b, dataBlock):
        firstVal    = dataBlock.inputValue(a).asFloat()
        secondVal   = dataBlock.inputValue(b).asFloat()
        LookVal     = self.getLocalLookValue(dataBlock)
        result      = self.getQuadrantValue(firstVal,secondVal,LookVal)
        return result
    
    ##############################################################################################################################################
    def compute(self, plug, dataBlock):
        if  (  (plug == self.angle1pos)
            or (plug == self.angle1neg)
            or (plug == self.angle2pos)
            or (plug == self.angle2neg)
            or (plug == self.output)
            ):
            
            # -------------------------- Inputs
            oAxisIndex   = self.indexDict[(dataBlock.inputValue(self.originAxis)).asShort()]
            tAxisIndex   = self.indexDict[(dataBlock.inputValue(self.targetAxis)).asShort()]
            
            nFirstAxis  = (dataBlock.inputValue(self.negativeFirstAxis )).asBool()
            nSecondAxis = (dataBlock.inputValue(self.negativeSecondAxis)).asBool()
            nThirdAxis  = (dataBlock.inputValue(self.negativeThirdAxis )).asBool()
            
            worldOMM    = (dataBlock.inputValue(self.worldOriginMatrix)).asMatrix()
            worldTMM    = (dataBlock.inputValue(self.worldTargetMatrix)).asMatrix()
            
            # --------------------------  
            mainoriginRow = OpenMaya.MVector(worldOMM.getElement(oAxisIndex[0],0), worldOMM.getElement(oAxisIndex[0],1), worldOMM.getElement(oAxisIndex[0],2)).normalize()
            mainTargetRow = OpenMaya.MVector(worldTMM.getElement(tAxisIndex[0],0), worldTMM.getElement(tAxisIndex[0],1), worldTMM.getElement(tAxisIndex[0],2)).normalize() * self.boolDict[nFirstAxis] 
            
            originRow = OpenMaya.MVector(worldOMM.getElement(oAxisIndex[1],0), worldOMM.getElement(oAxisIndex[1],1), worldOMM.getElement(oAxisIndex[1],2)).normalize() 
            TargetRow = OpenMaya.MVector(worldTMM.getElement(tAxisIndex[2],0), worldTMM.getElement(tAxisIndex[2],1), worldTMM.getElement(tAxisIndex[2],2)).normalize() 

            vResult = (originRow ^ TargetRow ).normalize()
            
            val1 =  mainoriginRow.angle(vResult * self.boolDict[nSecondAxis])
            val2 =  mainTargetRow.angle(vResult * self.boolDict[nThirdAxis]) 
            
            # --------------------------  
            a1pos = 0
            a1neg = 0
            a2pos = 0
            a2neg = 0
            
            localMainTargetRow  = mainTargetRow * worldOMM.inverse()
            
            if ((localMainTargetRow[tAxisIndex[2]])>=0):
                a1pos = val1
            else:
                a1neg = val1  
            
            if ((localMainTargetRow[tAxisIndex[1]])>=0):
                a2pos = val2
            else:
                a2neg = val2     
            
            # --------------------------  
            dataBlock.outputValue(self.angle1pos).setFloat(a1pos)
            dataBlock.outputValue(self.angle1neg).setFloat(a1neg)
            dataBlock.outputValue(self.angle2pos).setFloat(a2pos)
            dataBlock.outputValue(self.angle2neg).setFloat(a2neg)
            # --------------------------  
            dataBlock.setClean(self.angle1pos)  
            dataBlock.setClean(self.angle1neg)  
            dataBlock.setClean(self.angle2pos)  
            dataBlock.setClean(self.angle2neg)  
            
        ##################################################################################################################################################
        # ________________________________________________________________________________________________________________________________________________
        if (plug == self.quadrantPP) or (plug == self.output):
            dataBlock.outputValue(self.quadrantPP).setFloat(self.getQuadrantResult(self.angle1pos, self.angle2pos, dataBlock))
            dataBlock.setClean(self.quadrantPP)   
            dataBlock.setClean(self.output)   
            
        # ________________________________________________________________________________________________________________________________________________
        if (plug == self.quadrantNP) or (plug == self.output):
            dataBlock.outputValue(self.quadrantNP).setFloat(self.getQuadrantResult(self.angle1neg, self.angle2pos, dataBlock))
            dataBlock.setClean(self.quadrantNP)
            dataBlock.setClean(self.output)   
            
        # ________________________________________________________________________________________________________________________________________________
        if (plug == self.quadrantNN) or (plug == self.output):
            dataBlock.outputValue(self.quadrantNN).setFloat(self.getQuadrantResult(self.angle1neg, self.angle2neg, dataBlock))
            dataBlock.setClean(self.quadrantNN)   
            dataBlock.setClean(self.output)   
            
        # ________________________________________________________________________________________________________________________________________________
        if (plug == self.quadrantPN) or (plug == self.output):
            dataBlock.outputValue(self.quadrantPN).setFloat(self.getQuadrantResult(self.angle1pos, self.angle2neg, dataBlock))
            dataBlock.setClean(self.quadrantPN)   
            dataBlock.setClean(self.output)   
            
