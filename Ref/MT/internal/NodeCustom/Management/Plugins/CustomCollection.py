# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class CustomCollection(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName            = "customCollection"
    nodeID              = NodeID.CustomCollectionID
    
    #TODO no tengo claro como haré el parentesco entre nodosCollection, tener dos attributos me permite poder dejar libre el messege para otros contextos
    id                  = OpenMaya.MObject() 
    parent              = OpenMaya.MObject() 
    children            = OpenMaya.MObject() 
    list                = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return CustomCollection()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute    = OpenMaya.MFnMatrixAttribute()
        #enumAttribute      = OpenMaya.MFnEnumAttribute()
        #numericAttribute   = OpenMaya.MFnNumericAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        #compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        typedAttribute      = OpenMaya.MFnTypedAttribute()
        messageAttribute    = OpenMaya.MFnMessageAttribute()
        genericAttribute    = OpenMaya.MFnGenericAttribute()
        
        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------
        #id
        CustomCollection.id = typedAttribute.create("id", "i", OpenMaya.MFnData.kString )
        typedAttribute.array = True
        typedAttribute.writable = True
        typedAttribute.readable = True
        typedAttribute.storable = True
        CustomCollection.addAttribute(CustomCollection.id)
        
                
        #parent        
        CustomCollection.parent = messageAttribute.create("parent", "p")
        messageAttribute.writable = True
        messageAttribute.readable = False
        CustomCollection.addAttribute(CustomCollection.parent)   
        
        #children        
        CustomCollection.children = messageAttribute.create("children", "c")
        messageAttribute.writable = False
        messageAttribute.readable = True
        CustomCollection.addAttribute(CustomCollection.children)    
        
        ##list        
        #CustomCollection.list = messageAttribute.create("list", "l")
        #messageAttribute.array = True
        #messageAttribute.writable = True
        #messageAttribute.readable = False
        #CustomCollection.addAttribute(CustomCollection.list)    
        
        CustomCollection.list = genericAttribute.create ("list", "l")
        #genericAttribute.addDataType(OpenMaya.MFnData.kComponentList)
        #genericAttribute.addDataType(OpenMaya.MFnData.kDynArrayAttrs)
        genericAttribute.addDataType(OpenMaya.MFnData.kAny) 
        genericAttribute.array = True
        genericAttribute.writable = True
        genericAttribute.readable = True
        genericAttribute.storable = True
        CustomCollection.addAttribute(CustomCollection.list)
        
