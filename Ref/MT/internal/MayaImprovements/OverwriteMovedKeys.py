import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

import AnimSystems

import maya.cmds as cmds

from MayaImprovements import MayaImprovement
import Utils.OpenMaya.ApiUndo as ApiUndo

import sys

# Utilizamos esta clase para deshacer a la vez el borrado de las claves sobrescritas y el movimiento de las propias claves.
class UndoOverwrite():
    def __init__(self, change):
        self.change = change

    def undoIt(self):
        OverwriteMovedKeys.callbackEnabled = False

        self.change.undoIt()
        cmds.undo()
        
        OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
        OverwriteMovedKeys.callbackEnabled = True

    def redoIt(self):
        OverwriteMovedKeys.callbackEnabled = False

        cmds.redo()
        self.change.redoIt()

        OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
        OverwriteMovedKeys.callbackEnabled = True
        

class OverwriteMovedKeys(MayaImprovement, AnimSystems.KeyEditedListener):

    initialized = False

    # Constants
    epsilon = 0.0001
    overwriteMovedKeysOptionVar = "overwriteMovedKeysEnabled"
    
    _callbackPriority = 300

    @classmethod
    def isOverwriteMovedKeysEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.overwriteMovedKeysOptionVar):
            default = False  # False by default, AnimBot already provides this functionality
            cls.setOverwriteMovedKeysEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.overwriteMovedKeysOptionVar)

    @classmethod
    def setOverwriteMovedKeysEnabled(cls, enabled, updateOptionVar=True):
        if updateOptionVar:
            cmds.optionVar(iv=(cls.overwriteMovedKeysOptionVar, enabled))

        if enabled:
            AnimSystems.AnimSystemsCallbackManager.addAnimKeyEditedListener(cls)
        else:
            AnimSystems.AnimSystemsCallbackManager.removeAnimKeyEditedListener(cls)

    @classmethod
    def onAnimKeyEdited(cls, keyChanges, data):
        keysToOverwrite = {}
        curves = {}
        for keyChange in keyChanges:
            if keyChange.type == AnimSystems.KeyChange.TYPE_MOVE:
                currentTime = keyChange.currentTime.asUnits(OpenMaya.MTime.uiUnit())
                if not currentTime.is_integer():
                    intTimeValue = round(currentTime)
                    diff = intTimeValue - currentTime
                    if abs(diff) < cls.epsilon:
                        # We edit the time on the KeyChange to the integer value, since we will move the Keyframe there
                        keyChange.currentTime = OpenMaya.MTime(intTimeValue, OpenMaya.MTime.uiUnit())
                        
                        curve = OpenMayaAnim.MFnAnimCurve(keyChange.paramCurve)
                        currentIndex = keyChange.keyIndex
                        targetIndex = currentIndex
                        if diff > 0:
                            targetIndex += 1
                        elif diff < 0:
                            targetIndex -= 1
                        
                        curveName = curve.name()
                        if curveName not in keysToOverwrite:
                            keysToOverwrite[curveName] = []
                            curves[curveName] = curve
                        keysToOverwrite[curveName].append((currentIndex, targetIndex, intTimeValue))

        # We have to return the new changes performed by this call.
        # This tool will result in the deletion of some Keys.
        newKeyChanges = []
        
        if len(keysToOverwrite) > 0:
            curveChange = OpenMayaAnim.MAnimCurveChange()
            for curveName in keysToOverwrite:
                curve = curves[curveName]
                keyIndicesToOverwrite = sorted(keysToOverwrite[curveName])
                for i in range(len(keyIndicesToOverwrite)-1, -1, -1):
                    keyToMoveIndex = keyIndicesToOverwrite[i][0]
                    keyToDeleteIndex = keyIndicesToOverwrite[i][1]
                    
                    keyChange = AnimSystems.KeyChange()
                    keyChange.type = AnimSystems.KeyChange.TYPE_REMOVE
                    
                    keyChange.keyIndex = sys.maxsize   # The usual behaviour for deleting key is that the index is set to a huge number
                    keyChange.paramCurve = curve.object()
                    
                    keyChange.deltaType = OpenMayaAnim.MFnKeyframeDeltaAddRemove.kRemoved
                    keyChange.value = None
                    keyChange.time = curve.time(keyToDeleteIndex)
                    keyChange.replacedValue = None
                    
                    newKeyChanges.append(keyChange)
                    
                    curve.remove(keyToDeleteIndex, curveChange)
                    if keyToMoveIndex > keyToDeleteIndex:
                        keyToMoveIndex -= 1
                    curve.setTime(keyToMoveIndex, OpenMaya.MTime(keyIndicesToOverwrite[i][2], OpenMaya.MTime.uiUnit()), curveChange)

            undo = UndoOverwrite(curveChange)
            
            ApiUndo.commit(undo=undo.undoIt, redo=undo.redoIt)
        
        return keyChanges + newKeyChanges

    @classmethod
    def initialize(cls):
        cls.initialized = True

        cls.setOverwriteMovedKeysEnabled(cls.isOverwriteMovedKeysEnabled(), updateOptionVar=False) # We do this to renable the callback

    @classmethod
    def uninitialize(cls):
        cls.initialized = False

        cls.setOverwriteMovedKeysEnabled(False, updateOptionVar=False)