import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

import maya.cmds as cmds

import Utils.OpenMaya.ApiUndo as ApiUndo

import traceback

class CallbacksDisabledContext(object):
    
    def __init__(self, flushCallbacksOnExit=True):
        self.flushCallbacksOnExit = flushCallbacksOnExit
        
        self.wereCallbacksEnabled = None
    
    def __enter__(self):
        OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
            
        self.wereCallbacksEnabled = AnimSystemsCallbackManager._callbacksEnabled
        AnimSystemsCallbackManager._callbacksEnabled = False
    
    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        try:
            if self.flushCallbacksOnExit:
                OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
        finally:
            AnimSystemsCallbackManager._callbacksEnabled = self.wereCallbacksEnabled
    

class AnimSystemsUndo(object):
    
    def __init__(self, commandCount=1):
        self.commandCount = commandCount
    
    def commit(self):
        ApiUndo.commit(self.undoIt, self.redoIt)
        
    def undoIt(self):
        with CallbacksDisabledContext():
            for i in range(self.commandCount):
                cmds.undo()
            cmds.undo()
            OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
        
    def redoIt(self):
        with CallbacksDisabledContext():
            for i in range(self.commandCount):
                cmds.redo()
            cmds.redo()
            OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()


class KeyEditedListener():
    
    _callbacksEnabled = True
    _callbackPriority = 0
    
    @classmethod
    def isCallbacksEnabled(cls, includeManager=True):
        return cls._callbacksEnabled and (not includeManager or AnimSystemsCallbackManager.isCallbacksEnabled())
    
    @classmethod
    def onAnimKeyEdited(cls, keyChanges, data):
        return keyChanges
    
    @staticmethod
    def onReset():
        # Virtual method for refreshing the UI when this listener is resetted by CallbacksDisabledContext
        pass
    

class KeyChange(object):
    
    TYPE_UNKNOWN = -1
    TYPE_ADD = 0
    TYPE_REMOVE = 1
    TYPE_REPLACE = 2
    TYPE_MOVE = 3
    
    @classmethod
    def fromKeyDelta(cls, keyDelta):
        keyChange = cls()
        
        if keyDelta.hasFn(OpenMaya.MFn.kKeyframeDeltaAddRemove):
            fn = OpenMayaAnim.MFnKeyframeDeltaAddRemove(keyDelta)
            
            keyChange.deltaType = fn.deltaType()
            keyChange.value = fn.value()
            keyChange.time = fn.time()
            keyChange.replacedValue = fn.replacedValue()
            
            if keyChange.deltaType == fn.kAdded:
                keyChange.type = KeyChange.TYPE_ADD
            elif keyChange.deltaType == fn.kRemoved:
                keyChange.type = KeyChange.TYPE_REMOVE
            elif keyChange.deltaType == fn.kReplaced:
                keyChange.type = KeyChange.TYPE_REPLACE
            
        elif keyDelta.hasFn(OpenMaya.MFn.kKeyframeDeltaMove):
            fn = OpenMayaAnim.MFnKeyframeDeltaMove(keyDelta)
            
            keyChange.previousTime = fn.previousTime()
            keyChange.currentTime = fn.currentTime()
            keyChange.previousValue = fn.previousValue()
            keyChange.currentValue = fn.currentValue()
            keyChange.previousIndex = fn.previousIndex()
            
            keyChange.type = KeyChange.TYPE_MOVE
            
        else:
            fn = OpenMayaAnim.MFnKeyframeDelta(keyDelta)
            
            keyChange.type = KeyChange.TYPE_UNKNOWN
        
        keyChange.paramCurve = fn.paramCurve()
        keyChange.keyIndex = fn.keyIndex()
        
        return keyChange
    
    def __init__(self):
        self.type = None
        
        self.paramCurve = None
        self.keyIndex = None
        
        self.deltaType = None
        self.value = None
        self.time = None
        self.replacedValue = None
        
        self.previousTime = None
        self.currentTime = None
        self.previousValue = None
        self.currentValue = None
        self.previousIndex = None
        

class AnimSystemsCallbackManager():
    
    _initialized = False
    _callbacksEnabled = True
    
    _undoCallback = None
    _redoCallback = None
    
    keyEditedCallback = None
    keyEditedListeners = []
    
    @classmethod
    def isCallbacksEnabled(cls):
        return cls._callbacksEnabled and not (OpenMaya.MGlobal.isUndoing() or OpenMaya.MGlobal.isRedoing())

    @classmethod
    def setCallbacksEnabled(cls, enabled):
        cls._callbacksEnabled = enabled

    @classmethod
    def initialize(cls):
        cls.keyEditedCallback = OpenMayaAnim.MAnimMessage.addAnimKeyframeEditedCallback(cls.onAnimKeyEdited)
        
        cls._undoCallback = OpenMaya.MEventMessage.addEventCallback("Undo", cls.onUndo)
        cls._redoCallback = OpenMaya.MEventMessage.addEventCallback("Redo", cls.onUndo) # We use the same callback, it's the same behaviour
        
        cls._initialized = True
        
    @classmethod
    def uninitialize(cls):
        OpenMaya.MMessage.removeCallback(cls.keyEditedCallback)
        cls.keyEditedCallback = None
        
        OpenMaya.MMessage.removeCallback(cls._undoCallback)
        OpenMaya.MMessage.removeCallback(cls._redoCallback)
        cls._undoCallback = None
        cls._redoCallback = None
        
        cls._initialized = False
        
    @classmethod
    def addAnimKeyEditedListener(cls, listener):
        if listener not in cls.keyEditedListeners:
            if not cls._initialized:
                cls.initialize()
                
            cls.keyEditedListeners.append(listener)
            cls.keyEditedListeners.sort(key=lambda x: x._callbackPriority)
        
    @classmethod
    def removeAnimKeyEditedListener(cls, listener):
        if listener in cls.keyEditedListeners:
            cls.keyEditedListeners.remove(listener) # No need to sort when removing
            
            if cls._initialized and len(cls.keyEditedListeners) == 0:
                cls.uninitialize()
        
    @classmethod
    def onAnimKeyEdited(cls, keyDeltas, data):
        if cls.isCallbacksEnabled():
            keyChanges = [KeyChange.fromKeyDelta(keyDeltas[i]) for i in range(keyDeltas.length())]
            if keyChanges:
                for listener in cls.keyEditedListeners:
                    try:
                        if listener.isCallbacksEnabled(includeManager=False):
                            keyChanges = listener.onAnimKeyEdited(keyChanges, data)
                    except Exception:
                        traceback.print_exc()
            
    @classmethod
    def onUndo(cls, data):
        if cls._callbacksEnabled:
            cls._callbacksEnabled = False
            try:
                OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
            finally:
                cls._callbacksEnabled = True
