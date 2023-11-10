
import traceback

import maya.mel as mel
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

class TimeSliderScrubCallback(object):

    def onTimeSliderPressed(self):
        pass

    def onTimeSliderMoved(self, time):
        pass

    def onTimeSliderReleased(self):
        pass

# Maya already has a Time Slider callback to toggle sound scrubbing. Replicates it so it can be called as well.
class DefaultTimeSliderScrubCallback(TimeSliderScrubCallback):

    def __init__(self):
        self.playBackSlider = mel.eval('$tmpVar=$gPlayBackSlider')

    def onTimeSliderPressed(self):
        cmds.timeControl(self.playBackSlider, edit=True, beginScrub=True)

    def onTimeSliderReleased(self):
        cmds.timeControl(self.playBackSlider, edit=True, endScrub=True)


class TimeSliderScrubCallbackManager():

    callbacks = [DefaultTimeSliderScrubCallback()]   # The list starts with Maya's default time slider callback

    commandRegistered = False

    pressed = False

    @staticmethod
    def registerCommandOnTimeControl():
        if not TimeSliderScrubCallbackManager.commandRegistered:
            playBackSlider = mel.eval('$tmpVar=$gPlayBackSlider')
            cmds.timeControl(playBackSlider, edit=True, pressCommand=TimeSliderScrubCallbackManager.onTimeSliderPressed, releaseCommand=TimeSliderScrubCallbackManager.onTimeSliderReleased)
            OpenMaya.MDGMessage.addTimeChangeCallback(TimeSliderScrubCallbackManager.onTimeSliderMoved)  # This returns an ID to manage the callback, but since right now we don't even remove the callback, we don't need it.

            TimeSliderScrubCallbackManager.commandRegistered = True

    @staticmethod
    def registerCallback(callback):
        if callback in TimeSliderScrubCallbackManager.callbacks:
            raise RuntimeError("Unable to register Time Slider callback: The callback already is registered.")

        TimeSliderScrubCallbackManager.callbacks.append(callback)

        if not TimeSliderScrubCallbackManager.commandRegistered:
            TimeSliderScrubCallbackManager.registerCommandOnTimeControl()

    @staticmethod
    def unregisterCallback(callback):
        if callback not in TimeSliderScrubCallbackManager.callbacks:
            raise RuntimeError("Unable to unregister Time Slider callback: The callback is not registered.")
        
        TimeSliderScrubCallbackManager.callbacks.remove(callback)

        if not TimeSliderScrubCallbackManager.commandRegistered:
            TimeSliderScrubCallbackManager.registerCommandOnTimeControl()

    @staticmethod
    def onTimeSliderPressed(arg):
        TimeSliderScrubCallbackManager.pressed = True
        for callback in TimeSliderScrubCallbackManager.callbacks:
            try:
                callback.onTimeSliderPressed()
            except:
                traceback.print_exc()

    @staticmethod
    def onTimeSliderMoved(time, arg):
        if TimeSliderScrubCallbackManager.pressed:
            for callback in TimeSliderScrubCallbackManager.callbacks:
                try:
                    callback.onTimeSliderMoved(time.value)
                except:
                    traceback.print_exc()

    @staticmethod
    def onTimeSliderReleased(arg):
        TimeSliderScrubCallbackManager.pressed = False
        for callback in TimeSliderScrubCallbackManager.callbacks:
            try:
                callback.onTimeSliderReleased()
            except:
                traceback.print_exc()