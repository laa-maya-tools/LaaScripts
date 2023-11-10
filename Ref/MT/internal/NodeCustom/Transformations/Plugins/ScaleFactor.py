# -*- coding: utf-8 -*-

# DISTANCIAS: 
# Ante la duda de si este nodo debía ser o no responsable de la medición de distancias hemos decidido sacarlo del nodo,
# y que el wrapper gestione que usa como input de currentLength e initialLengt

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

class ScaleFactor(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName                = "ScaleFactor"
    nodeID                  = NodeID.ScaleFactorID
       
    axisBehavior            = OpenMaya.MObject()
    axisBehaviorX           = OpenMaya.MObject()
    axisBehaviorY           = OpenMaya.MObject()
    axisBehaviorZ           = OpenMaya.MObject()
    axisBehaviorUnused      = OpenMaya.MObject() # Solución para que maya muestre bien los enumerados hijos de un compound.

    limits                  = OpenMaya.MObject() 
    compressLimit           = OpenMaya.MObject() 
    extendLimit             = OpenMaya.MObject() 
    
    weights                 = OpenMaya.MObject() 
    compressWeight          = OpenMaya.MObject() 
    extendWeight            = OpenMaya.MObject() 
    
    currentLength           = OpenMaya.MObject() 
    initialLength           = OpenMaya.MObject()
    
    factor                  = OpenMaya.MObject()
     
    scale                   = OpenMaya.MObject()
    scaleX                  = OpenMaya.MObject()
    scaleY                  = OpenMaya.MObject()
    scaleZ                  = OpenMaya.MObject()

    # DISTANCIAS: comentado en el inicio
    # region
    #currentLength               = OpenMaya.MObject()
    #currentLengthMatrixStart    = OpenMaya.MObject()
    #currentLengthMatrixEnd      = OpenMaya.MObject()
    #currentLengthStartPos       = OpenMaya.MObject()
    #currentLengthEndPos         = OpenMaya.MObject()
    
    #initialLength               = OpenMaya.MObject()
    #initialLengthMatrixStart    = OpenMaya.MObject()
    #initialLengthMatrixEnd      = OpenMaya.MObject()    
    #initialLengthStartPos       = OpenMaya.MObject()
    #initialLengthEndPos         = OpenMaya.MObject()
    # endregion
    
    scaleOptionDict = {
        "Ignore"            : 0,
        "Factor"            : 1,
        "inverse Factor"    : 2,
    }
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return ScaleFactor()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute    = OpenMaya.MFnMatrixAttribute()
        enumAttribute       = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        CompoundAttribute   = OpenMaya.MFnCompoundAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        genericAttribute    = OpenMaya.MFnGenericAttribute()
        
        #__________________________ AXISBehavior BEHAVIOR
               
        #axisBehaviorX
        ScaleFactor.axisBehaviorX = enumAttribute.create("axisBehaviorX", "abx", defaultValue=0) #The number is the default value (currently: x)
        for t in ScaleFactor.scaleOptionDict:
            enumAttribute.addField(t, ScaleFactor.scaleOptionDict[t])
        #ScaleFactor.addAttribute(ScaleFactor.axisBehaviorX)  #hijo del compound axisBehavior
         
        #axisBehaviorY
        ScaleFactor.axisBehaviorY = enumAttribute.create("axisBehaviorY", "aby", defaultValue=0) #The number is the default value (currently: x)
        for t in ScaleFactor.scaleOptionDict:
            enumAttribute.addField(t, ScaleFactor.scaleOptionDict[t])
        #ScaleFactor.addAttribute(ScaleFactor.axisBehaviorY)  #hijo del compound axisBehavior
        
        #axisBehaviorZ
        ScaleFactor.axisBehaviorZ = enumAttribute.create("axisBehaviorZ", "abz", defaultValue=0) #The number is the default value (currently: x)
        for t in ScaleFactor.scaleOptionDict:
            enumAttribute.addField(t, ScaleFactor.scaleOptionDict[t])
        #ScaleFactor.addAttribute(ScaleFactor.axisBehaviorZ)  #hijo del compound axisBehavior
            
        ScaleFactor.axisBehaviorUnused      = genericAttribute.create("axisBehaviorUnused", "abu")
        genericAttribute.hidden             = True
        genericAttribute.connectable        = False
        #genericAttribute.writable           = True
        genericAttribute.readable           = False
        genericAttribute.keyable            = False
        genericAttribute.storable           = False
        #ScaleFactor.addAttribute(ScaleFactor.axisBehaviorUnused) #hijo del compound axisBehavior        
        
        ScaleFactor.axisBehavior = CompoundAttribute.create("axisBehavior", "ab") 
        CompoundAttribute.addChild(ScaleFactor.axisBehaviorX)
        CompoundAttribute.addChild(ScaleFactor.axisBehaviorY)
        CompoundAttribute.addChild(ScaleFactor.axisBehaviorZ)
        CompoundAttribute.addChild(ScaleFactor.axisBehaviorUnused)
        CompoundAttribute.writable = True
        CompoundAttribute.readable = True
        CompoundAttribute.keyable  = True
        CompoundAttribute.storable = True
        ScaleFactor.addAttribute(ScaleFactor.axisBehavior) 
                   
                        
        ##__________________________ LIMIT   
        ScaleFactor.compressLimit = numericAttribute.createPoint("compressLimit", "cl")
        numericAttribute.default    = (0.01,0.01,0.01)
        #ScaleFactor.addAttribute(ScaleFactor.compressLimit) #hijo del compound limits  
        
        ScaleFactor.extendLimit = numericAttribute.createPoint("extendLimit", "el")
        numericAttribute.default    = (10,10,10)
        #ScaleFactor.addAttribute(ScaleFactor.extendLimit)   #hijo del compound limits
        
        ScaleFactor.limits = CompoundAttribute.create("limits", "l") 
        CompoundAttribute.addChild(ScaleFactor.compressLimit)  
        CompoundAttribute.addChild(ScaleFactor.extendLimit)
        CompoundAttribute.writable = True
        CompoundAttribute.readable = True
        CompoundAttribute.keyable  = True
        CompoundAttribute.storable = True
        ScaleFactor.addAttribute(ScaleFactor.limits) 
        
        ##__________________________ Weight
        ScaleFactor.compressWeight = numericAttribute.createPoint("compressWeight", "cw")
        numericAttribute.default    = (1,1,1)
        #ScaleFactor.addAttribute(ScaleFactor.compressWeight)  #hijo del compound weights 
        
        ScaleFactor.extendWeight = numericAttribute.createPoint("extendWeight", "sw")
        numericAttribute.default    = (1,1,1)
        #ScaleFactor.addAttribute(ScaleFactor.extendWeight)  #hijo del compound weights  
        
        ScaleFactor.weights = CompoundAttribute.create("weights", "w") 
        CompoundAttribute.addChild(ScaleFactor.compressWeight)  
        CompoundAttribute.addChild(ScaleFactor.extendWeight)
        CompoundAttribute.writable = True
        CompoundAttribute.readable = True
        CompoundAttribute.keyable  = True
        CompoundAttribute.storable = True
        ScaleFactor.addAttribute(ScaleFactor.weights) 
        
        ##__________________________ Length
        #currentLength   
        ScaleFactor.currentLength = numericAttribute.create("currentLength", "c", OpenMaya.MFnNumericData.kFloat, 0.0)   
        numericAttribute.writable = True
        numericAttribute.readable = True
        numericAttribute.keyable  = True
        numericAttribute.storable = True
        ScaleFactor.addAttribute(ScaleFactor.currentLength)      
        
        #initialLength   
        ScaleFactor.initialLength = numericAttribute.create("initialLength", "i", OpenMaya.MFnNumericData.kFloat, 0.0)  
        numericAttribute.writable = True
        numericAttribute.readable = True
        numericAttribute.keyable  = True
        numericAttribute.storable = True
        ScaleFactor.addAttribute(ScaleFactor.initialLength)   
        
        # DISTANCIAS: comentado en el inicio
        #region
               
        ##currentLengthMatrixStart
        #ScaleFactor.currentLengthMatrixStart = matrixAttribute.create("currentLengthMatrixStart", "clsm")
        #matrixAttribute.writable = True
        #matrixAttribute.readable = False 
        #matrixAttribute.keyable  = True
        #matrixAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.currentLengthMatrixStart)      
        
        ##currentLengthMatrixEnd
        #ScaleFactor.currentLengthMatrixEnd = matrixAttribute.create("currentLengthMatrixEnd", "clem")
        #matrixAttribute.writable = True
        #matrixAttribute.readable = False
        #matrixAttribute.keyable  = True
        #matrixAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.currentLengthMatrixEnd)      
        
        
        ##current
        #ScaleFactor.current = CompoundAttribute.create("current", "c")
        #CompoundAttribute.addChild(ScaleFactor.currentLength)
        #CompoundAttribute.addChild(ScaleFactor.currentLengthMatrixStart)
        #CompoundAttribute.addChild(ScaleFactor.currentLengthMatrixEnd)
        #CompoundAttribute.writable = True
        #CompoundAttribute.readable = False
        #CompoundAttribute.keyable  = True
        #CompoundAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.current)   
        
        ##initialLengthMatrixStart
        #ScaleFactor.initialLengthMatrixStart = matrixAttribute.create("initialLengthMatrixStart", "ilsm")
        #matrixAttribute.writable = True
        #matrixAttribute.readable = False
        #matrixAttribute.keyable  = True
        #matrixAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.initialLengthMatrixStart)      
        
        ##initialLengthMatrixEnd
        #ScaleFactor.initialLengthMatrixEnd = matrixAttribute.create("initialLengthMatrixEnd", "ilem")
        #matrixAttribute.writable = True
        #matrixAttribute.readable = False
        #matrixAttribute.keyable  = True
        #matrixAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.initialLengthMatrixEnd)      
        
        ##initial
        #ScaleFactor.initial = CompoundAttribute.create("initial", "i")
        #CompoundAttribute.addChild(ScaleFactor.initialLength)
        #CompoundAttribute.addChild(ScaleFactor.initialLengthMatrixStart)
        #CompoundAttribute.addChild(ScaleFactor.initialLengthMatrixEnd)
        #CompoundAttribute.writable = True
        #CompoundAttribute.readable = False
        #CompoundAttribute.keyable  = True
        #CompoundAttribute.storable = True
        #ScaleFactor.addAttribute(ScaleFactor.initial)   
        # endregion

        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        # DISTANCIAS: comentado en el inicio
        # region
        # outputWorldMatrix
        #ScaleFactor.attributeAffects(ScaleFactor.currentLengthMatrixStart   , ScaleFactor.scale)
        #ScaleFactor.attributeAffects(ScaleFactor.currentLengthMatrixEnd     , ScaleFactor.scale)
        #ScaleFactor.attributeAffects(ScaleFactor.initialLengthMatrixStart   , ScaleFactor.scale)
        #ScaleFactor.attributeAffects(ScaleFactor.initialLengthMatrixEnd     , ScaleFactor.scale)   
        # endregion     
        
        #scaleX 
        ScaleFactor.scaleX   = numericAttribute.create("scaleX", "sX", OpenMaya.MFnNumericData.kFloat, 1.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #ScaleFactor.addAttribute(ScaleFactor.scaleX)      

        #scaleY 
        ScaleFactor.scaleY   = numericAttribute.create("scaleY", "sY", OpenMaya.MFnNumericData.kFloat, 1.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #ScaleFactor.addAttribute(ScaleFactor.scaleY)      

        #scaleZ 
        ScaleFactor.scaleZ   = numericAttribute.create("scaleZ", "sZ", OpenMaya.MFnNumericData.kFloat, 1.0)
        numericAttribute.array      = False
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        #ScaleFactor.addAttribute(ScaleFactor.scaleZ)      

        #scale    
        ScaleFactor.scale     = numericAttribute.create("scale", "s", ScaleFactor.scaleX ,ScaleFactor.scaleY ,ScaleFactor.scaleZ)  
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        ScaleFactor.addAttribute(ScaleFactor.scale)      

        ScaleFactor.factor     = numericAttribute.create("factor", "f", OpenMaya.MFnNumericData.kFloat, 0.0)  
        numericAttribute.writable   = False
        numericAttribute.readable   = True
        ScaleFactor.addAttribute(ScaleFactor.factor)      

        ScaleFactor.attributeAffects(ScaleFactor.currentLength      , ScaleFactor.factor)
        ScaleFactor.attributeAffects(ScaleFactor.initialLength      , ScaleFactor.factor)    
        ScaleFactor.attributeAffects(ScaleFactor.currentLength      , ScaleFactor.scale)
        ScaleFactor.attributeAffects(ScaleFactor.initialLength      , ScaleFactor.scale)    
        ScaleFactor.attributeAffects(ScaleFactor.axisBehavior       , ScaleFactor.scale)    
        ScaleFactor.attributeAffects(ScaleFactor.limits             , ScaleFactor.scale)    
        ScaleFactor.attributeAffects(ScaleFactor.weights            , ScaleFactor.scale)    

    # DISTANCIAS: funciones descartadas para medir
    # region
    def getLength(self, start, end, dataBlock):
        startPosition      = OpenMaya.MTransformationMatrix((dataBlock.inputValue(start)).asMatrix() ).translation(OpenMaya.MSpace.kWorld)
        endPosition        = OpenMaya.MTransformationMatrix((dataBlock.inputValue(end)).asMatrix()   ).translation(OpenMaya.MSpace.kWorld)
        return (endPosition-startPosition).length()
        # ----------------------------------------------------
        # calculo alternativo para obtener la distancia
        #lStartMPoint      = OpenMaya.MPoint(startPosition   )
        #lEndMPoint        = OpenMaya.MPoint(endPosition     )   
        #currentLength         = lStartMPoint.distanceTo(lEndMPoint) 

    def getInputLength(self, attr, start, end, dataBlock):
        if OpenMaya.MFnDependencyNode(self.thisMObject()).findPlug(attr, False).isConnected:
            return dataBlock.inputValue(attr).asFloat() 
        else:
            return self.getLength( start, end, dataBlock)
    
    # endregion        

    def compute(self, plug, dataBlock):           
        if (    (plug == self.scale)
            or  (plug == self.scaleX)
            or  (plug == self.scaleY)
            or  (plug == self.scaleZ)
            or  (plug == self.factor)
        ):
            
            # VARIABLES
            #______________________________________________________
            # DISTANCIAS: comentado en el inicio
            # region
            #currentLength   = self.getInputLength(self.currentLength , self.currentLengthMatrixStart, self.currentLengthMatrixEnd, dataBlock)
            #initialLength   = self.getInputLength(self.initialLength , self.initialLengthMatrixStart, self.initialLengthMatrixEnd, dataBlock)
            # endregion
            
            currentLength    = dataBlock.inputValue(self.currentLength).asFloat()
            initialLength    = dataBlock.inputValue(self.initialLength).asFloat()           

            xBehavior  = (dataBlock.inputValue(self.axisBehaviorX)).asShort() 
            yBehavior  = (dataBlock.inputValue(self.axisBehaviorY)).asShort() 
            zBehavior  = (dataBlock.inputValue(self.axisBehaviorZ)).asShort() 
            
            limitTuple = [(dataBlock.inputValue(self.compressLimit )).asFloat3(), ((dataBlock.inputValue(self.extendLimit  )).asFloat3()) ]
            
            # CALCULATE
            #______________________________________________________
            theFactor = currentLength/initialLength
            theInverseFactor = initialLength/currentLength
            
            factorValue = [ 1, theFactor, theInverseFactor ]   
            
            if theFactor>=1:
                weight = dataBlock.inputValue(self.extendWeight).asFloat3()
            else:
                weight = dataBlock.inputValue(self.compressWeight).asFloat3()
                
            xFactor     = 1 + ((factorValue[xBehavior] - 1) * weight[0])
            yFactor     = 1 + ((factorValue[yBehavior] - 1) * weight[1])
            zFactor     = 1 + ((factorValue[zBehavior] - 1) * weight[2])
            
            valX = min(max(limitTuple[0][0],xFactor),limitTuple[1][0])
            valY = min(max(limitTuple[0][1],yFactor),limitTuple[1][1])
            valZ = min(max(limitTuple[0][2],zFactor),limitTuple[1][2])
                       
            # OUTPUT    
            #______________________________________________________
            outputScale = dataBlock.outputValue(self.scale)
            outputScale.set3Float(valX, valY, valZ)
            
            outputFactor = dataBlock.outputValue(self.factor)
            outputFactor.setFloat(theFactor)
            #______________________________________________________
            dataBlock.setClean(self.scale)
            dataBlock.setClean(self.scaleX)
            dataBlock.setClean(self.scaleY)
            dataBlock.setClean(self.scaleZ)
            dataBlock.setClean(self.factor)