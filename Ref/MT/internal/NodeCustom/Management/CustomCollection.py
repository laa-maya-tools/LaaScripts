# -*- coding: utf-8 -*-

#import maya.cmds as cmds
#import Exporter
#import ProjectPath
#from Utils.Maya.UndoContext import UndoContext, UndoOff
#import os

from NodeManager    import NodeWrapper

class CustomCollection(NodeWrapper.NodeWrapper): 
    _Type         = "customCollection"
    _list         = "list"
    _id           = "id"
    
    def __init__(self, node=None):
        super(CustomCollection, self).__init__(node)
    
