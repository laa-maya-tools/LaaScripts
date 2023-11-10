import maya.cmds as cmds

from collections.abc import Iterable

from Utils.Python.Versions import basestring

class OptionVarConfiguration(object):
    
    TYPE_INTEGER = 0
    TYPE_FLOAT = 1
    TYPE_STRING = 2
    
    def __init__(self, name, optionVar, type, defaultValue):
        self.name = name
        self.optionVar = optionVar
        self.type = type
        self.defaultValue = defaultValue
        
    # Value
    
    @property
    def value(self):
        if not self.exists():
            self.value = self.defaultValue
            return self.defaultValue
        return cmds.optionVar(q=self.optionVar)
    
    @value.setter
    def value(self, value):
        if isinstance(value, Iterable) and not isinstance(value, basestring):
            self.clearArray()
            for item in value:
                self.addValue(item)
        else:
            if self.type == self.TYPE_INTEGER:
                cmds.optionVar(intValue=(self.optionVar, value))
            elif self.type == self.TYPE_FLOAT:
                cmds.optionVar(floatValue=(self.optionVar, value))
            elif self.type == self.TYPE_STRING:
                cmds.optionVar(stringValue=(self.optionVar, value))
    
    # Option Var Methods
    
    def exists(self):
        return cmds.optionVar(exists=self.optionVar)
    
    # Array Methods
    
    def isArray(self):
        return self.arrayCount() > 2
    
    def arrayCount(self):
        return cmds.optionVar(arraySize=self.optionVar)
    
    def clearArray(self):
        return cmds.optionVar(clearArray=self.optionVar)
    
    def setArrayValue(self, index, value):
        arrayValue = self.value
        arrayValue[index] = value
        self.value = arrayValue
    
    def addValue(self, value):
        if self.type == self.TYPE_INTEGER:
            cmds.optionVar(intValueAppend=(self.optionVar, value))
        elif self.type == self.TYPE_FLOAT:
            cmds.optionVar(floatValueAppend=(self.optionVar, value))
        elif self.type == self.TYPE_STRING:
            cmds.optionVar(stringValueAppend=(self.optionVar, value))
    
    def insertValue(self, index, value):
        arrayValue = self.value
        arrayValue.insert(index, value)
        self.value = arrayValue
        
    def removeValue(self, value):
        arrayValue = self.value
        index = arrayValue.index(value)
        self.takeAt(index)
        
    def takeAt(self, index):
        cmds.optionVar(removeFromArray=(self.optionVar, index))
