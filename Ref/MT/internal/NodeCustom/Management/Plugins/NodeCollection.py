# -*- coding: utf-8 -*-

#Maya API 2 
import maya.api.OpenMaya as OpenMaya

# Archivo dende se registran los IDs para el proyecto
import NodeID
import NodeID.PluginNodes as PluginNodes

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class NodeCollection(OpenMaya.MPxNode, PluginNodes.PluginNode):
    # Plugin data
    nodeName            = "nodeCollection"
    nodeID              = NodeID.NodeCollectionID
    
    #TODO no tengo claro como haré el parentesco entre nodosCollection, tener dos attributos me permite poder dejar libre el messege para otros contextos
    parent              = OpenMaya.MObject() 
    children               = OpenMaya.MObject() 
    list                = OpenMaya.MObject()
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return NodeCollection()
    
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        #matrixAttribute    = OpenMaya.MFnMatrixAttribute()
        #enumAttribute      = OpenMaya.MFnEnumAttribute()
        #numericAttribute   = OpenMaya.MFnNumericAttribute()
        #unitAttribute      = OpenMaya.MFnUnitAttribute()
        #compoundAttribute  = OpenMaya.MFnCompoundAttribute()
        #typedAttribute     = OpenMaya.MFnTypedAttribute()
        messageAttribute    = OpenMaya.MFnMessageAttribute()
        #genericAttribute    = OpenMaya.MFnGenericAttribute()
        
        #---------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------
        #parent        
        NodeCollection.parent = messageAttribute.create("parent", "p")
        messageAttribute.writable = True
        messageAttribute.readable = False
        NodeCollection.addAttribute(NodeCollection.parent)   
        
        #children        
        NodeCollection.children = messageAttribute.create("children", "c")
        messageAttribute.writable = False
        messageAttribute.readable = True
        NodeCollection.addAttribute(NodeCollection.children)    
        
        #list        
        NodeCollection.list = messageAttribute.create("list", "l")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        NodeCollection.addAttribute(NodeCollection.list)    
        
        #NodeCollection.list = genericAttribute.create("list", "l")
        ##genericAttribute.addDataType(OpenMaya.MFnData.kComponentList)
        ##genericAttribute.addDataType(OpenMaya.MFnData.kDynArrayAttrs)
        #genericAttribute.addDataType(OpenMaya.MFnData.kAny) 
        #genericAttribute.array = True
        #genericAttribute.writable = True
        #genericAttribute.readable = True
        #genericAttribute.storable = True
        #NodeCollection.addAttribute(NodeCollection.list)