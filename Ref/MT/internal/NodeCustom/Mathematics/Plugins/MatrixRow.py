# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui
#import math

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class MatrixRow(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName        = "matrixRow"
    nodeID          = NodeID.MatrixRowID
    
    row0            = OpenMaya.MObject()
    row00           = OpenMaya.MObject()
    row01           = OpenMaya.MObject()
    row02           = OpenMaya.MObject()
    
    row1            = OpenMaya.MObject()
    row10           = OpenMaya.MObject()
    row11           = OpenMaya.MObject()
    row12           = OpenMaya.MObject()
    
    row2            = OpenMaya.MObject()
    row20           = OpenMaya.MObject()
    row21           = OpenMaya.MObject()
    row22           = OpenMaya.MObject()
    
    row3            = OpenMaya.MObject()
    row30           = OpenMaya.MObject()
    row31           = OpenMaya.MObject()
    row32           = OpenMaya.MObject()
        
    inputMatrix     = OpenMaya.MObject()

    #Method to return an instance    
    @staticmethod
    def creator():
        return MatrixRow()

    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        matrixAttribute     = OpenMaya.MFnMatrixAttribute()
        #enumAttribute      = OpenMaya.MFnEnumAttribute()
        numericAttribute    = OpenMaya.MFnNumericAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        #compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        #messageAttribute   = OpenMaya.MFnMessageAttribute()

        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------

        #inputMatrix
        MatrixRow.inputMatrix = matrixAttribute.create("inputMatrix", "im")
        matrixAttribute.writable = True
        matrixAttribute.readable = False
        matrixAttribute.storable  = True
        matrixAttribute.keyable  = True
        MatrixRow.addAttribute(MatrixRow.inputMatrix)           
        #____________________________________________________________________________________________________
        # row0 ----------------------------------------------------------------------------------------------
        MatrixRow.row00 = numericAttribute.create("row00", "r00",OpenMaya.MFnNumericData.kDouble,1)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row00)   

        MatrixRow.row01 = numericAttribute.create("row01", "r01",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row01)   

        MatrixRow.row02 = numericAttribute.create("row02", "r02",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row02)   

        MatrixRow.row0 = numericAttribute.create("row0", "r0",MatrixRow.row00,MatrixRow.row01,MatrixRow.row02)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row0)   
        #____________________________________________________________________________________________________
        # row1 ----------------------------------------------------------------------------------------------
        MatrixRow.row10 = numericAttribute.create("row10", "r10",OpenMaya.MFnNumericData.kDouble,1)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row10)   

        MatrixRow.row11 = numericAttribute.create("row11", "r11",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row11)   

        MatrixRow.row12 = numericAttribute.create("row12", "r12",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row12)   

        MatrixRow.row1 = numericAttribute.create("row1", "r1",MatrixRow.row10,MatrixRow.row11,MatrixRow.row12)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row1)   
        #____________________________________________________________________________________________________
        # row2 ----------------------------------------------------------------------------------------------
        MatrixRow.row20 = numericAttribute.create("row20", "r20",OpenMaya.MFnNumericData.kDouble,1)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row20)   

        MatrixRow.row21 = numericAttribute.create("row21", "r21",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row21)   

        MatrixRow.row22 = numericAttribute.create("row22", "r22",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row22)   

        MatrixRow.row2 = numericAttribute.create("row2", "r2",MatrixRow.row20,MatrixRow.row21,MatrixRow.row22)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row2)  
        #____________________________________________________________________________________________________
        # row3 ----------------------------------------------------------------------------------------------
        MatrixRow.row30 = numericAttribute.create("row30", "r30",OpenMaya.MFnNumericData.kDouble,1)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row30)   

        MatrixRow.row31 = numericAttribute.create("row31", "r31",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row31)   

        MatrixRow.row32 = numericAttribute.create("row32", "r32",OpenMaya.MFnNumericData.kDouble,0)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row32)   

        MatrixRow.row3 = numericAttribute.create("row3", "r3",MatrixRow.row30,MatrixRow.row31,MatrixRow.row32)
        numericAttribute.writable = False
        numericAttribute.readable = True
        MatrixRow.addAttribute(MatrixRow.row3)   


        #---------------------------------------------------------------------------------------
        # OUTPUTS 
        #---------------------------------------------------------------------------------------
        
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row0)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row00)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row01)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row02)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row02)

        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row1)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row10)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row11)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row12)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row12)

        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row2)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row20)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row21)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row22)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row22)

        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row3)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row30)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row31)
        MatrixRow.attributeAffects(MatrixRow.inputMatrix,         MatrixRow.row32)
    
    @classmethod
    def  fnCompute(cls, plug, row, column, dataBlock):
        MM       = (dataBlock.inputValue(cls.inputMatrix)).asMatrix() 
        dataBlock.outputValue(plug).setDouble(MM.getElement(row, column))
        dataBlock.setClean(plug) 
        
    @classmethod
    def  fnComputeRow(cls, plug, row, dataBlock):
        MM       = (dataBlock.inputValue(cls.inputMatrix)).asMatrix() 
        dataBlock.outputValue(plug).set3Double(MM.getElement(row,0), MM.getElement(row,1), MM.getElement(row,2))
        dataBlock.setClean(plug)    
    
    # la razón de usar el nombre del attributo en vez del propio attributo es que los mObject no pueden ser clave de un diccionario
    optionDict={
        "row0"      :   (lambda dataBlock: (MatrixRow.fnComputeRow( MatrixRow.row0  , 0,    dataBlock))),
        "row00"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row00 , 0, 0, dataBlock))),
        "row01"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row01 , 0, 1, dataBlock))),
        "row02"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row02 , 0, 2, dataBlock))),
        "row1"      :   (lambda dataBlock: (MatrixRow.fnComputeRow( MatrixRow.row1  , 1,    dataBlock))),
        "row10"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row10 , 1, 0, dataBlock))),
        "row11"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row11 , 1, 1, dataBlock))),
        "row12"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row12 , 1, 2, dataBlock))),
        "row2"      :   (lambda dataBlock: (MatrixRow.fnComputeRow( MatrixRow.row2  , 2,    dataBlock))),
        "row20"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row20 , 2, 0, dataBlock))),
        "row21"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row21 , 2, 1, dataBlock))),
        "row22"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row22 , 2, 2, dataBlock))),
        "row3"      :   (lambda dataBlock: (MatrixRow.fnComputeRow( MatrixRow.row3  , 3,    dataBlock))),
        "row30"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row30 , 3, 0, dataBlock))),
        "row31"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row31 , 3, 1, dataBlock))),
        "row32"     :   (lambda dataBlock: (MatrixRow.fnCompute(    MatrixRow.row32 , 3, 2, dataBlock)))
    }    
    
    def compute(self, plug, dataBlock):
        attrName = plug.partialName(useLongNames=True)
        if attrName in self.optionDict:
            self.optionDict[attrName](dataBlock)

