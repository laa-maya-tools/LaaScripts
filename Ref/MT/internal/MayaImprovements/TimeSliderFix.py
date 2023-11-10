# encoding: utf-8
import MayaImprovements

import maya.cmds as cmds  

import TimeSlider.TimeSliderScrubCallback as TimeSliderScrubCallback

from Utils.Maya.OptionVar import OptionVarConfiguration

class TimeSliderFixCallback(TimeSliderScrubCallback.TimeSliderScrubCallback):

    def onTimeSliderPressed(self):
        disableUndo = TimeSliderFix.isDisableTimeSliderUndoEnabled()
        
        if disableUndo:
            cmds.undoInfo(swf=False)
            
        if TimeSliderFix.isStopAnimWithTimeSliderEnabled():
            if cmds.play(q=True, st=True):
                if disableUndo:
                    TimeSliderFix.setDisableTimeSliderUndoEnabled(False, updateOptionVar=False)
                    
                cmds.play(st=False)
                
                if disableUndo:
                    TimeSliderFix.setDisableTimeSliderUndoEnabled(True, updateOptionVar=False)

    def onTimeSliderReleased(self):
        if TimeSliderFix.isDisableTimeSliderUndoEnabled():
            cmds.undoInfo(swf=True)

     
class TimeSliderFix(MayaImprovements.MayaImprovement):

    initialized = False

    # Constants
    DISABLE_TIME_SLIDER_UNDO_OPTIONVAR = OptionVarConfiguration("Disable Time Slider Undo", "disableTimeSliderUndoEnabled", OptionVarConfiguration.TYPE_INTEGER, True)
    STOP_ANIMATION_WITH_TIME_SLIDER_OPTIONVAR = OptionVarConfiguration("Stop Animation With Time Slider", "stopAnimWithTimeSliderEnabled", OptionVarConfiguration.TYPE_INTEGER, True)
    IMPROVED_COPY_PASTE_OPTIONVAR = OptionVarConfiguration("Improve Time Slider Copy Paste", "improvedCopyPasteEnabled", OptionVarConfiguration.TYPE_INTEGER, False)
    
    DISABLE_DOUBLE_CLICK_SELECT_OPTIONVAR = OptionVarConfiguration("Disable Double Click Select", "disableDoubleClickSelect", OptionVarConfiguration.TYPE_INTEGER, False)
    DISABLE_DOUBLE_CLICK_SELECT_WITH_SHIFT_OPTIONVAR = OptionVarConfiguration("Disable Double Click Select With Shift", "disableDoubleClickSelectWithShift", OptionVarConfiguration.TYPE_INTEGER, False)
    FIX_SELECT_NEAR_CURRENT_SELECTION_OPTIONVAR = OptionVarConfiguration("Fix Select Near Current Selection", "fixSelectNearCurrentSelection", OptionVarConfiguration.TYPE_INTEGER, False)
    KEEP_SELECTING_IF_SHIFT_IS_RELEASED_OPTIONVAR = OptionVarConfiguration("Keep Selecting If Shift Is Released", "keepSelectingIfShiftIsReleased", OptionVarConfiguration.TYPE_INTEGER, False)
    START_SELECTING_IF_SHIFT_IS_PRESSED_OPTIONVAR = OptionVarConfiguration("Start Selecting If Shift Is Pressed", "startSelectingIfShiftIsPressed", OptionVarConfiguration.TYPE_INTEGER, False)
    MOVE_SELECTED_KEYS_CLICKING_ANYWHERE_OPTIONVAR = OptionVarConfiguration("Move Selected Keys Clicking Anywhere", "moveSelectedKeysClickingAnywhere", OptionVarConfiguration.TYPE_INTEGER, False)
    
    enableUndoOnKeyMoveCondition = "EnableKeyMove"

    # Properties
    timeSliderFixCallback = None
    playbackStopScriptJob = None
    undoScriptJob = None

    # Variables
    undoCallbackEnabled = True
    
    @staticmethod
    def isDisableDoubleClickSelectEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.DISABLE_DOUBLE_CLICK_SELECT_OPTIONVAR.value

    @staticmethod
    def setDisableDoubleClickSelectEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.DISABLE_DOUBLE_CLICK_SELECT_OPTIONVAR.value = enabled

    @staticmethod
    def isDisableDoubleClickSelectWithShiftEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.DISABLE_DOUBLE_CLICK_SELECT_WITH_SHIFT_OPTIONVAR.value

    @staticmethod
    def setDisableDoubleClickSelectWithShiftEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.DISABLE_DOUBLE_CLICK_SELECT_WITH_SHIFT_OPTIONVAR.value = enabled

    @staticmethod
    def isImprovedCopyPasteEnabled():
        return False    # Temporarily disabled, it's not working properly
        return TimeSliderFix.initialized and TimeSliderFix.IMPROVED_COPY_PASTE_OPTIONVAR.value

    @staticmethod
    def setImprovedCopyPasteEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.IMPROVED_COPY_PASTE_OPTIONVAR.value = enabled

    @staticmethod
    def isFixSelectNearCurrentSelectionEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.FIX_SELECT_NEAR_CURRENT_SELECTION_OPTIONVAR.value

    @staticmethod
    def setFixSelectNearCurrentSelectionEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.FIX_SELECT_NEAR_CURRENT_SELECTION_OPTIONVAR.value = enabled

    @staticmethod
    def isKeepSelectingIfShiftIsReleasedEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.KEEP_SELECTING_IF_SHIFT_IS_RELEASED_OPTIONVAR.value

    @staticmethod
    def setKeepSelectingIfShiftIsReleasedEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.KEEP_SELECTING_IF_SHIFT_IS_RELEASED_OPTIONVAR.value = enabled

    @staticmethod
    def isStartSelectingIfShiftIsPressedEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.START_SELECTING_IF_SHIFT_IS_PRESSED_OPTIONVAR.value

    @staticmethod
    def setStartSelectingIfShiftIsPressedEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.START_SELECTING_IF_SHIFT_IS_PRESSED_OPTIONVAR.value = enabled

    @staticmethod
    def isMoveSelectedKeysClickingAnywhereEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.MOVE_SELECTED_KEYS_CLICKING_ANYWHERE_OPTIONVAR.value

    @staticmethod
    def setMoveSelectedKeysClickingAnywhereEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.MOVE_SELECTED_KEYS_CLICKING_ANYWHERE_OPTIONVAR.value = enabled


    @staticmethod
    def isDisableTimeSliderUndoEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.DISABLE_TIME_SLIDER_UNDO_OPTIONVAR.value

    @staticmethod
    def setDisableTimeSliderUndoEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.DISABLE_TIME_SLIDER_UNDO_OPTIONVAR.value = enabled
        
        # This condition is added so the undo is not disable when moving keys
        if enabled:
            # Esta condición utiliza unos cuantos hacks para que ciertas operaciones funcionen. La clave es que se ejecuta justo después de presionar y justo antes de soltar.
            # Lo que hace es activar el undo justo después de presionar y desactivarlo justo antes de soltar, de manera que nunca se llega a hacer undo a los cambios de tiempo pero se puede hacer undo a todo lo que ocurra entre medias.
            # Como su nombre indica, se utiliza para que se puedan deshacer los movientos de keys. Como se mueve el slider, se realiza un cambio de tiempo, pero como el movimiento de la key ocurre antes de que se procese el soltar el slider, el undo está activado.
            # Además, al hacer playback no se llama a ninguna función, pero sí que se ejecuta el código de la condición. Se ejecuta al empezar a reproducir y tras darle a detener, pero antes de que se realice el cambio de tiempo.
            # Como no se ha ejecutado código previamente, la condición haría lo opuesto de lo que queremos: apagar el undo durante la reproducción y encenderlo justo antes de que se produzca el cambio de tiempo.
            # Por ello, si detectamos que se está reproduciendo la animación, no hacemos el cambio, de manera que solo se apaga el undo. Un scriptjob volverá a encender al undo cuando Maya termine por completo de detener la reproducción.
            cmds.condition(TimeSliderFix.enableUndoOnKeyMoveCondition, d="playingBack", s="if (!`play -q -st`) { undoInfo -stateWithoutFlush (!`undoInfo -q -stateWithoutFlush`); }")
        else:
            try:
                cmds.condition(TimeSliderFix.enableUndoOnKeyMoveCondition, delete=True)
            except:
                pass    # No existe una manera de saber si una condición existe o no y da error si intentas borrar una que no existe, así que se usa try catch como último recurso

    @staticmethod
    def isStopAnimWithTimeSliderEnabled():
        return TimeSliderFix.initialized and TimeSliderFix.STOP_ANIMATION_WITH_TIME_SLIDER_OPTIONVAR.value

    @staticmethod
    def setStopAnimWithTimeSliderEnabled(enabled, updateOptionVar=True):
        if updateOptionVar:
            TimeSliderFix.STOP_ANIMATION_WITH_TIME_SLIDER_OPTIONVAR.value = enabled


    @staticmethod
    def initialize():
        TimeSliderFix.initialized = True

        # Registers the callback called when moving the time slider
        TimeSliderFix.timeSliderFixCallback = TimeSliderFixCallback()
        TimeSliderScrubCallback.TimeSliderScrubCallbackManager.registerCallback(TimeSliderFix.timeSliderFixCallback)

        # Registers a scriptjob called when the animation state changes (since this will also change the current time)
        TimeSliderFix.playbackStopScriptJob = cmds.scriptJob(cf=["playingBack", TimeSliderFix.timeSliderFixCallback.onTimeSliderReleased])

        TimeSliderFix.setDisableTimeSliderUndoEnabled(TimeSliderFix.DISABLE_TIME_SLIDER_UNDO_OPTIONVAR.value)
        TimeSliderFix.setStopAnimWithTimeSliderEnabled(TimeSliderFix.STOP_ANIMATION_WITH_TIME_SLIDER_OPTIONVAR.value)
        TimeSliderFix.setImprovedCopyPasteEnabled(TimeSliderFix.IMPROVED_COPY_PASTE_OPTIONVAR.value)

    @staticmethod
    def uninitialize():
        TimeSliderFix.initialized = False
        
        # Disables the systems
        TimeSliderFix.setDisableTimeSliderUndoEnabled(False, updateOptionVar=False)
        TimeSliderFix.setStopAnimWithTimeSliderEnabled(False, updateOptionVar=False)
        TimeSliderFix.setImprovedCopyPasteEnabled(False, updateOptionVar=False)

        # Unregisters the callback called when moving the time slider
        TimeSliderScrubCallback.TimeSliderScrubCallbackManager.unregisterCallback(TimeSliderFix.timeSliderFixCallback)
        TimeSliderFix.timeSliderFixCallback = None

        # Unregisters the scriptjob for the animation state change
        cmds.scriptJob(kill=TimeSliderFix.playbackStopScriptJob)
        