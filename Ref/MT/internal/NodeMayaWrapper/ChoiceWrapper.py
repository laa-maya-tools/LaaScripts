# -*- coding: utf-8 -*-

import maya.cmds as cmds
#import Exporter
#import ProjectPath
#from Utils.Maya.UndoContext import UndoContext, UndoOff
#import os

#from NodeManager    import NodeWrapper
#from NodeCustom.Management.NodeCollection   import NodeCollection
#from Utils.Maya.UndoContext import UndoContext
import NodeManager.ListWrapperInputs as LWInputs

class ChoiceWrapper(LWInputs.ListWrapperInputs): 
    _Type               = "choice"
    #_attrConnection     = "worldMatrix[0]" #"worldMatrix"
    _list               = "input"
    
    _selector   = "selector"
    
    def __init__(self, node=None, itemClass = None):
        super().__init__(node, itemClass = itemClass)
        #super(ChoiceWrapper, self).__init__(node, itemClass = itemClass)
        #self._Type           = "choice"
        self._attrConnection = "worldMatrix[0]"
        self.node = node
        self.itemClass = itemClass    
    
    @property
    def selector(self):
        return self.getAttr(self._selector)
    
    @selector.setter
    def selector(self, value):
        self.setNumericAttribute(self._selector, value)    



