# -*- coding: utf-8 -*-
#import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext
#import Utils.OpenMaya as OpenMayaUtils

import NodeManager.Lib.AttributeWrapperBase as AWB

class ListWrapperInputs(AWB.AttributeWrapperBase): 
    _Type           = None
    _attrConnection = "messege"
    _list           = "list"

    reorderMode     = True

    def __init__(self, node=None, itemClass=None):
        super().__init__(node)
        #super(NodeCollection, self).__init__(node)

        self.node               = node
        self.itemClass          = itemClass

    # TODO valorar si implementar el forzar a definir estos dos atributos o darle un valor por defecto
    #@property
    #def _Type(self):
    #    if self._Type!=None:
    #        return self._Type
    #    else:
    #        raise Exception("_Type is not defined in class {}".format(self))

    #@_Type.setter
    #def _Type(self, value):
    #    self._Type = value

    #@property
    #def _attrConnection(self):
    #    if self._attrConnection!=None:
    #        return self._attrConnection
    #    else:
    #        raise Exception("_attrConnection is not defined in class {}".format(self))
    
    #@_attrConnection.setter
    #def _attrConnection(self, value):
    #    self._attrConnection = value

    def append(self, item):
        with UndoContext("Append Wrapper Connections"):
            if item:
                if self.isNodeWrapper(item):
                    inputPlug = item.getPlug(self._attrConnection)
                else:
                    inputPlug = "{}.{}".format(item, self._attrConnection)
            else:
                inputPlug = input 
            self.appendInputPlug(self._list, inputPlug, unique=True, rebuildList=self.reorderMode)    
    
    def __add__(self, theList):
        return list(self) + theList
    
    def __iadd__(self, theList): 
        with UndoContext("Join Nodes to " + self._Type ):
            for theItem in theList:
                if type(theItem)==str:
                    if ("." in theItem):
                        self.appendInputPlug(self._list, theItem)
                    else:
                        self.appendInputNode(self._list, theItem, inputAttribute=self._attrConnection, unique=True, rebuildList=True)
                else:
                    self.appendInputWrapper(self._list, theItem, inputAttribute=self._attrConnection, unique=True, rebuildList=True)
        return self
    
    def __len__(self):
        thePlug = self.getPlug(self._list)
        theList = cmds.listConnections(thePlug, plugs=False, source=True, destination=False)  or [] 
        return len(theList)
    
    def remove(self, node):
        with UndoContext("Remove Nodes from " + self._Type ):
            if isinstance(node, AWB.AttributeWrapperBase):
                thePlug = node.getPlug(self._attrConnection)
            else:
                thePlug = "{}.{}".format(node, self._attrConnection)
            self.removeItemListByPlug(self._list,thePlug, delete= False, rebuildList=self.reorderMode)   
    
    def __delitem__(self, index):
        with UndoContext("Delete Nodes from " + self._Type ):
            self.removeItemListByIndex(self._list, index, removeInput = True, removeOutput=False, deleteInputNode = True, deleteOutputNode=False) 

    def clear(self):
        self.clearList(self._list, start = 0, removeInput = True, removeOutput = False, deleteInputNode = False, deleteOutputNode=False)
    
    def __getitem__(self, index):
        theList = self.getInputFromListAttribute(self._list, cls=self.itemClass, plugs=False)
        return theList[index]
    
    def first(self, default=None):
        theList = self.getInputFromListAttribute(self._list, cls=self.itemClass, plugs=False)
        if theList:
            return theList[0]
        else:
            return default
    
    def __setitem__(self, index, node):
        self.rebuildList(self._list)
        thePlug = self.getPlug(self._list)
        thePlugindex= "{}[{}]".format(thePlug,index)
        self.setInputNode(thePlugindex, node, inputAttribute=self._attrConnection)
        #self.setInput(thePlugindex, node, inputAttribute=self._attrConnection)  
    
    def __contains__(self, item):
        if isinstance(item, AWB.AttributeWrapperBase):
            item = item.node
        thePlug = self.getPlug(self._list)
        theList = cmds.listConnections(thePlug, plugs=False, source=True, destination=False)  or []
        return item in theList    
    
    def insert(self, index,  item):
        if not self.reorderMode:
            raise Warning("insert is not allowed when reorderMode is disabled.") 
        else:    
            if isinstance(item, AWB.AttributeWrapperBase):
                itemPlug = item.getPlug(self._attrConnection)
            else:
                itemPlug = "{}.{}".format(item,self._attrConnection)
            self.insertItemList(self._list, index, itemPlug, asInput=True, unique=True)
    
    def index(self, item):
        if isinstance(item, AWB.AttributeWrapperBase):
            item = item.node
        thePlug = self.getPlug(self._list)
        theList = cmds.listConnections(thePlug, plugs=False, source=True, destination=False)  or [] 
        return theList.index(item)

    def __iter__(self):
        theList = self.getInputFromListAttribute(self._list, cls=self.itemClass, plugs=False)
        for i in range(len(theList)):
            yield theList[i]
            
    def __bool__(self):
        return len(self) > 0
    
""" #TODO  - WIP -  
    def __reversed__(self):
        theList = self.getListConnections(self._list)
        theReverseList = theList.reverse()
        self.setInputList(self._list, theReverseList, inputAttribute=None)
        
    #def __repr__(self):
    #    thePlug = self.getPlug(self._list)
    #    theList = cmds.listConnections(thePlug, plugs=False, source=True, destination=False)  or [] 
    #    return print(theList)
    def takeAt(self, item):
        pass
    
    def pop(self):
        pass
    
    #def __str__(self): #con repr sería suficienteb
    #    pass
    
    def sorted(self, item):
        pass
"""




