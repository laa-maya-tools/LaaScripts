from PySide2 import QtCore

import math
import time

class RepeatCommand():
    
    startTimer = QtCore.QTimer()
    repeatTimer = QtCore.QTimer()
    
    currentCommand = None
    
    timeStamp = None
    
    def __init__(self, callback, startTime=300, toggleRate=30):
        self.callback = callback
        self.startTime = startTime
        self.toggleRate = toggleRate
    
    @classmethod
    def stopTimers(cls):
        cls.startTimer.stop()
        cls.repeatTimer.stop()
        
    @classmethod
    def startRepeatTimer(cls):
        cls.startTimer.stop()
        cls.timeStamp = time.time()
        cls.repeatTimer.start(0)
        
    @classmethod
    def getToggleRate(cls):
        if callable(cls.currentCommand.toggleRate):
            return cls.currentCommand.toggleRate()
        return cls.currentCommand.toggleRate
        
    @classmethod
    def processToggleCount(cls):
        currentTimeStamp = time.time()
        elapsedTime = currentTimeStamp - cls.timeStamp
        timeStep = 1.0 / cls.getToggleRate()
        if elapsedTime >= timeStep:
            cls.timeStamp = currentTimeStamp - elapsedTime % timeStep
            return math.floor(elapsedTime / timeStep)
        else:
            return 0
        
    @classmethod
    def processRepeat(cls):
        toggleCount = cls.processToggleCount()
        if toggleCount > 0:
            cls.currentCommand.callback(toggleCount, True)
            
    @classmethod
    def startStartTimer(cls, command):
        if cls.currentCommand != None:
            cls.stopTimers()
        cls.currentCommand = command
        
        command.callback(1, False)
        
        cls.startTimer.start(command.startTime)
    
    @classmethod
    def initializeTimers(cls):
        cls.startTimer.timeout.connect(cls.startRepeatTimer)
        cls.repeatTimer.timeout.connect(cls.processRepeat)
        
    def onCommandPressed(self):
        RepeatCommand.startStartTimer(self)
    
    def onCommandReleased(self):
        if RepeatCommand.currentCommand == self:
            RepeatCommand.stopTimers()
            RepeatCommand.currentCommand = None
        
RepeatCommand.initializeTimers()
