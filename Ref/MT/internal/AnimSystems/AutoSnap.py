import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

import maya.cmds as cmds

import AnimSystems

from RigManager.IKFKChain import IKFKChain

from Utils.Maya.UndoContext import UndoContext

class AutoSnapManager(AnimSystems.KeyEditedListener):
    
    _callbacksEnabled = False   # Disabled by default
    _callbackPriority = 200
    
    CALLBACKS_ENABLED_OPTION_VAR = "AUTO_SNAP_CALLBACKS_ENABLED"
    
    @classmethod
    def initialize(cls):
        AnimSystems.AnimSystemsCallbackManager.addAnimKeyEditedListener(cls)
        
        if cmds.optionVar(exists=cls.CALLBACKS_ENABLED_OPTION_VAR):
            cls._callbacksEnabled = cmds.optionVar(q=cls.CALLBACKS_ENABLED_OPTION_VAR)
    
    @classmethod
    def uninitialize(cls):
        AnimSystems.AnimSystemsCallbackManager.removeAnimKeyEditedListener(cls)
        
    @classmethod
    def setCallbacksEnabled(cls, enabled, saveOptionVar=True):
        cls._callbacksEnabled = enabled
        if saveOptionVar:
            cmds.optionVar(iv=(cls.CALLBACKS_ENABLED_OPTION_VAR, enabled))
        
    @classmethod
    def onAnimKeyEdited(cls, keyChanges, data):
        # We naively perform an autosnap everytime a Keyframe is edited.
        # It is cheaper to just do it than to check if we need to.
        # First, we check which time range has been affected by these changes.
        changedRangeMin = None
        changedRangeMax = None
        for keyChange in keyChanges:
            animCurve = OpenMayaAnim.MFnAnimCurve(keyChange.paramCurve)
            keyIndex = keyChange.keyIndex
            keyCount = animCurve.numKeys()
            
            rangeMin = None
            rangeMax = None
            if keyIndex > keyCount:
                # This only happens when deleting keys, the index will be a huge number.
                # We retrieve the keys using the time the keyframe was deleted at.
                keyTime = keyChange.time
                
                if keyCount == 0:
                    # If we removed all keys, we use the key's time as it is, instead of the next/previous key's, since the first and last keys must be on the list of deleted keys too.
                    rangeMin = keyTime
                    rangeMax = keyTime
                else:
                    closestKeyIndex = animCurve.findClosest(keyTime)
                    closestKeyTime = animCurve.time(closestKeyIndex)
                    if closestKeyTime > keyTime:
                        rangeMax = closestKeyTime
                        rangeMin = animCurve.time(closestKeyIndex - 1) if closestKeyIndex > 0 else keyTime  # This checks if the deleted keyframe was the first one to use it's time instead.
                    else:
                        rangeMin = closestKeyTime
                        rangeMax = animCurve.time(closestKeyIndex + 1) if closestKeyIndex < keyCount - 1 else keyTime  # This checks if the deleted keyframe was the last one to use it's time instead.
            else:
                rangeMin = animCurve.time(max(0, keyIndex - 1))
                rangeMax = animCurve.time(min(keyCount - 1, keyIndex + 1))
                
            if changedRangeMin is None or changedRangeMin > rangeMin:
                changedRangeMin = rangeMin
            if changedRangeMax is None or changedRangeMax < rangeMax:
                changedRangeMax = rangeMax
                
        # We have to return the new changes performed by this call.
        # However, asuming the KeyingGroups are enabled, the AutoSnap will only perform value changes to the Keys.
        # TODO: Value changes are not that usefull to our tools (yet), so we will just ignore them.
        newKeyChanges = []
        
        # We snap all the rig chains on each keyframe they have on the changed time range.
        needsUndo = False
        with UndoContext("AutoSnap"):
            rigChains = IKFKChain.getInstances()
            for rigChain in rigChains:
                if rigChain.autoSnap:
                    # We use the FK/IK Blend attribute's keys to perform the snap.
                    # Usually, the keys will be synced, so this method should be enough.
                    ikFkBlendPlug = rigChain.ikFkBlendPlug
                    if ikFkBlendPlug is not None:
                        keyTimes = cmds.keyframe(ikFkBlendPlug, q=True, time=(changedRangeMin.asUnits(OpenMaya.MTime.uiUnit()), changedRangeMax.asUnits(OpenMaya.MTime.uiUnit()))) or []
                        ikToFkSnaps = []
                        fkToIkSnaps = []
                        for keyTime in keyTimes:
                            ikFkBlend = cmds.getAttr(ikFkBlendPlug, time=keyTime)
                            if ikFkBlend == 0:
                                ikToFkSnaps.append(keyTime)
                            else:
                                fkToIkSnaps.append(keyTime)
                                
                        if len(ikToFkSnaps) > 0:
                            rigChain.snapIKToFK(times=ikToFkSnaps)
                            needsUndo = True
                        if len(fkToIkSnaps) > 0:
                            rigChain.snapFKToIK(times=fkToIkSnaps)
                            needsUndo = True
                            
        if needsUndo:
            AnimSystems.AnimSystemsUndo().commit()
        
        return keyChanges + newKeyChanges
