# -*- coding: utf-8 -*-

import maya.cmds as cmds
#import Exporter
#import ProjectPath
#from Utils.Maya.UndoContext import UndoContext, UndoOff
#import os

#from NodeManager.NodeWrapper import NodeWrapper
import NodeManager.ListWrapperInputs as LWInputs

#from Utils.Maya.UndoContext import UndoContext

class NodeCollection(LWInputs.ListWrapperInputs): 
    _Type           = "nodeCollection"
    _attrConnection = "message"
    _list           = "list"

    def __init__(self, node=None, itemClass = None):
        super().__init__(node, itemClass = itemClass)
        #super(NodeCollection, self).__init__(node, itemClass = itemClass)

        #self._Type           = "nodeCollection"
        #self._attrConnection = "message"
        self.node = node
        self.itemClass = itemClass
        