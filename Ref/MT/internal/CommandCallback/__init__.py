import maya.api.OpenMaya as OpenMaya

class CallbacksDisabledContext(object):
    
    def __init__(self):
        self.wereCallbacksEnabled = None
    
    def __enter__(self):
        self.wereCallbacksEnabled = CommandCallbackManager._callbacksEnabled
        CommandCallbackManager._callbacksEnabled = False
    
    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        CommandCallbackManager._callbacksEnabled = self.wereCallbacksEnabled
    

class CommandListener():
    
    _callbacksEnabled = True
    _callbackPriority = 0
    
    @classmethod
    def isCallbacksEnabled(cls):
        return cls._callbacksEnabled and CommandCallbackManager.isCallbacksEnabled()
    
    @classmethod
    def onBeforeCommand(cls, id):
        pass
    
    @classmethod
    def onAfterCommand(cls, id):
        pass


class CommandCallbackManager():
    
    TYPE_PROC = OpenMaya.MCommandMessage.kMELProc
    TYPE_COMMAND = OpenMaya.MCommandMessage.kMELCommand
    
    _initialized = False
    _callbacksEnabled = True
    
    commandCallback = None
    commandCallbackListeners = {}
    
    @classmethod
    def isCallbacksEnabled(cls):
        return cls._callbacksEnabled and not (OpenMaya.MGlobal.isUndoing() or OpenMaya.MGlobal.isRedoing())

    @classmethod
    def setCallbacksEnabled(cls, enabled):
        cls._callbacksEnabled = enabled

    @classmethod
    def initialize(cls):
        cls.commandCallback = OpenMaya.MCommandMessage.addProcCallback(cls.onCommandCallback)
        
        cls._initialized = True
        
    @classmethod
    def uninitialize(cls):
        OpenMaya.MMessage.removeCallback(cls.commandCallback)
        cls.commandCallback = None
        
        cls._initialized = False

    @classmethod
    def addCommandCallbackListener(cls, command, type, listener):
        key = (command, type)
        if key not in cls.commandCallbackListeners:
            commandCallbacks = []
            cls.commandCallbackListeners[key] = commandCallbacks
        else:
            commandCallbacks = cls.commandCallbackListeners[key]
        if listener not in commandCallbacks:
            if not cls._initialized:
                cls.initialize()
                
            commandCallbacks.append(listener)
            commandCallbacks.sort(key=lambda x: x._callbackPriority)
            
    @classmethod
    def removeCommandCallbackListener(cls, command, type, listener):
        key = (command, type)
        if key in cls.commandCallbackListeners:
            commandCallbacks = cls.commandCallbackListeners[key]
            if listener in commandCallbacks:
                commandCallbacks.remove(listener) # No need to sort when removing
            
                if cls._initialized and len(commandCallbacks) == 0:
                    cls.commandCallbackListeners.pop(key)
                    
                    if cls._initialized and len(cls.commandCallbackListeners) == 0:
                        cls.uninitialize()
        
    @classmethod
    def onCommandCallback(cls, command, id, entering, type, data):
        key = (command, type)
        commandCallbacks = cls.commandCallbackListeners.get(key, [])
        if entering:
            for listener in commandCallbacks:
                listener.onBeforeCommand(id)
        else:
            for listener in commandCallbacks:
                listener.onAfterCommand(id)
