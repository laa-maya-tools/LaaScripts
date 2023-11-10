import maya.cmds as cmds

import Utils.Maya as MayaUtils
from Utils.Maya.RepeatCommand import RepeatCommand
from Utils.Maya.OptionVar import OptionVarConfiguration

import TimeSlider

import functools

#---------------------------------
#|      Time Change Repeat       |
#---------------------------------

class TimeChangeRepeat():

    SWITCH_FRAME_OR_KEY_OPTIONVAR = OptionVarConfiguration("SwitchFrameOrKey", "TimeChangeRepeat_SwitchFrameOrKey", OptionVarConfiguration.TYPE_INTEGER, False)
    
    @classmethod
    def onFrameOrKeyToggled(cls):
        cls.SWITCH_FRAME_OR_KEY_OPTIONVAR.value = not cls.SWITCH_FRAME_OR_KEY_OPTIONVAR.value
    
    @staticmethod
    def getTimeIndex(keyTimes, currentTime):
        if keyTimes[0] > currentTime:
            return -1
        count = len(keyTimes)
        for i in range(count):
            if i == count - 1 or keyTimes[i + 1] > currentTime:
                return i
    
    @classmethod
    def nextFrame(cls, offset, repeating, switch=False):
        if cls.SWITCH_FRAME_OR_KEY_OPTIONVAR.value != switch:
            keyTimes = TimeSlider.getTimeSliderKeyTimes()
            if not keyTimes:
                return
            
            currentTime = cmds.currentTime(q=True)
            currentTimeIndex = cls.getTimeIndex(keyTimes, currentTime)
            
            newTimeIndex = (currentTimeIndex + offset) % len(keyTimes)
            frame = keyTimes[newTimeIndex]
            
        else:
            frame = cmds.currentTime(q=True) + offset
            max = cmds.playbackOptions(q=True, max=True)
            if frame > max:
                min = cmds.playbackOptions(q=True, min=True)
                if not repeating:
                    frame = min
                else:
                    frame = min + frame - max
                
        cmds.currentTime(frame, e=True)
        
    @classmethod
    def previousFrame(cls, offset, repeating, switch=False):
        if cls.SWITCH_FRAME_OR_KEY_OPTIONVAR.value != switch:
            keyTimes = TimeSlider.getTimeSliderKeyTimes()
            if not keyTimes:
                return
            
            currentTime = cmds.currentTime(q=True)
            currentTimeIndex = cls.getTimeIndex(keyTimes, currentTime)
            
            if currentTime != keyTimes[currentTimeIndex]:
                currentTimeIndex += 1
            newTimeIndex = (currentTimeIndex - offset) % len(keyTimes)
            frame = keyTimes[newTimeIndex]
            
        else:
            frame = cmds.currentTime(q=True) - offset
            min = cmds.playbackOptions(q=True, min=True)
            if frame < min:
                max = cmds.playbackOptions(q=True, max=True)
                if not repeating:
                    frame = max
                else:
                    frame = max + frame - min
                
        cmds.currentTime(frame, e=True)
    
    repeatStartTime = 300
    
    @classmethod
    def createRepeatCommands(cls):
        cls.nextFrameRepeatCommand = RepeatCommand(cls.nextFrame, startTime=cls.repeatStartTime, toggleRate=MayaUtils.getFrameRate)
        cls.previousFrameRepeatCommand = RepeatCommand(cls.previousFrame, startTime=cls.repeatStartTime, toggleRate=MayaUtils.getFrameRate)
        cls.nextKeyRepeatCommand = RepeatCommand(functools.partial(cls.nextFrame, switch=True), startTime=cls.repeatStartTime, toggleRate=MayaUtils.getFrameRate)
        cls.previousKeyRepeatCommand = RepeatCommand(functools.partial(cls.previousFrame, switch=True), startTime=cls.repeatStartTime, toggleRate=MayaUtils.getFrameRate)
        
    @staticmethod
    def registerCommands():
        TimeChangeRepeat.createRepeatCommands()
        
        cmds.runTimeCommand("NextFrameRepeatPress", cat="MSE Commands.Timeline", ann="Jumps to the next frame. It will keep advancing until you call the NextFrameRepeatRelease command (usually set to the same hotkey on release).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.nextFrameRepeatCommand.onCommandPressed()", default=True)
        cmds.runTimeCommand("NextFrameRepeatRelease", cat="MSE Commands.Timeline", ann="Release command for the NextFrameRepeatPress command (usually set to the same hotkey on press). You need to call this command to stop the repeat.", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.nextFrameRepeatCommand.onCommandReleased()", default=True)
        cmds.runTimeCommand("PreviousFrameRepeatPress", cat="MSE Commands.Timeline", ann="Jumps to the previous frame. It will keep advancing until you call the PreviousFrameRepeatRelease command (usually set to the same hotkey on release).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.previousFrameRepeatCommand.onCommandPressed()", default=True)
        cmds.runTimeCommand("PreviousFrameRepeatRelease", cat="MSE Commands.Timeline", ann="Release command for the NextFrameRepeatPress command (usually set to the same hotkey on press). You need to call this command to stop the repeat.", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.previousFrameRepeatCommand.onCommandReleased()", default=True)
        
        cmds.runTimeCommand("NextKeyRepeatPress", cat="MSE Commands.Timeline", ann="Jumps to the next keyframe. It will keep advancing until you call the NextKeyRepeatRelease command (usually set to the same hotkey on release).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.nextKeyRepeatCommand.onCommandPressed()", default=True)
        cmds.runTimeCommand("NextKeyRepeatRelease", cat="MSE Commands.Timeline", ann="Jumps to the previous keyframe. It will keep advancing until you call the PreviousKeyRepeatRelease command (usually set to the same hotkey on release).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.nextKeyRepeatCommand.onCommandReleased()", default=True)
        cmds.runTimeCommand("PreviousKeyRepeatPress", cat="MSE Commands.Timeline", ann="Release command for the NextKeyRepeatPress command (usually set to the same hotkey on press). You need to call this command to stop the repeat.", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.previousKeyRepeatCommand.onCommandPressed()", default=True)
        cmds.runTimeCommand("PreviousKeyRepeatRelease", cat="MSE Commands.Timeline", ann="Release command for the NextKeyRepeatPress command (usually set to the same hotkey on press). You need to call this command to stop the repeat.", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.previousKeyRepeatCommand.onCommandReleased()", default=True)
        
        cmds.runTimeCommand("FrameOrKeyToggle", cat="MSE Commands.Timeline", ann="Makes the NextFrame and NextKey repeat commands to swap functionallity. The NextFrame will jump through keys and the NextKey will advance a frame (same for the \"Previous\" commands).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.TimeChangeRepeat.onFrameOrKeyToggled()", default=True)


#---------------------------------
#|        Anim Commands          |
#---------------------------------

class AnimCommands():
    
    @staticmethod
    def setSafeKeys(count=1):
        initialTime = cmds.currentTime(q=True)
        start = cmds.playbackOptions(q=True, ast=True)
        end = cmds.playbackOptions(q=True, aet=True)
        
        for i in range(count):
            cmds.currentTime(start - i)
            cmds.TimeEditorSetKey()
    
        for i in range(count):
            cmds.currentTime(end + i)
            cmds.TimeEditorSetKey()
            
        cmds.currentTime(initialTime)
    
    @staticmethod
    def registerCommands():
        cmds.runTimeCommand("SetSafeKeys", cat="MSE Commands.Animation", ann="Sets a key on the selected controls at the beginning and end of the animation range.", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.AnimCommands.setSafeKeys()", default=True)
        cmds.runTimeCommand("SetSafeKeysDouble", cat="MSE Commands.Animation", ann="Sets two keys on the selected controls at the beginning and end of the animation range (the second key is placed outside the animation range).", c="import CustomCommands.CommonCommands as CommonCommands; CommonCommands.AnimCommands.setSafeKeys(count=2)", default=True)


#---------------------------------
#|           Commands            |
#---------------------------------

def register():
    TimeChangeRepeat.registerCommands()
    AnimCommands.registerCommands()
