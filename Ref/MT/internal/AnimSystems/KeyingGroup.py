# coding: utf-8

from maya import OpenMaya, OpenMayaAnim, cmds

from PySide2 import QtCore, QtGui

from NodeManager.NodeWrapper import NodeWrapper

import AnimSystems

import CommandCallback
import TimeSlider
import TimeSlider.TimeSliderOverlay as TimeSliderOverlay

import Utils.Maya.AnimLayers as AnimLayerUtils
import Utils.OpenMaya as OpenMayaUtils
import Utils.OpenMaya.AnimNodes as AnimNodeUtils

from Utils.Maya.UndoContext import UndoContext

import json
import sys

# TODO:
# - Se necesita una manera de refrescar el overlay al cambiar el valor del atributo Enabled (?)

def exportKeyingGroupsToFile(keyingGroups, path):
    data = []
    for keyingGroup in keyingGroups:
        v = keyingGroup.asJson()
        data.append(v)
        
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def importKeyingGroupsFromFile(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for kgData in data:
        KeyingGroup.fromJson(kgData)

def getConflicts():
    keyingGroups = KeyingGroup.getInstances()
    conflicts = {}
    attrs = {}
    for keyingGroup in keyingGroups:
        affectedAttributes = keyingGroup.getAffectedAttributes(includeChildren=False)
        for attr in affectedAttributes:
            if attr in attrs:
                if attr not in conflicts:
                    conflicts[attr] = [attrs[attr]]
                conflicts[attr].append(keyingGroup)
            else:
                attrs[attr] = keyingGroup
    return conflicts

class KeyingGroup(NodeWrapper):
    
    _Type = "customKeyingGroup"
    
    # Attributes ------------
    
    _enabled = "enabled"
    _affectedAttributes = "affectedAttributes"
    _parentKeyingGroup = "parentKeyingGroup"
    _childKeyingGroups = "childKeyingGroups"
    
    # Properties ------------
        
    @property
    def enabled(self):
        return self.getAttr(self._enabled)
    
    @enabled.setter
    def enabled(self, value):
        with UndoContext("Set Keying Group Enabled"):
            self.setNumericAttribute(self._enabled, value)
            
        KeyingGroupManager.timeSliderPainter.setDirty(update=True)

    # Affected Attributes ---

    def getAffectedAttributes(self, includeChildren=False, onlyEnabledChildren=True):
        affectedAttributes = self.getInputFromListAttribute(self._affectedAttributes, plugs=True) or []
        if includeChildren:
            children = self.getChildKeyingGroups()
            for child in children:
                if not onlyEnabledChildren or child.enabled:
                    affectedAttributes.extend(child.getAffectedAttributes(includeChildren=True))
        return affectedAttributes
    
    def setAffectedAttributes(self, plugs):
        with UndoContext("Set Affected Attributes"):
            self.setInputListPlugs(self._affectedAttributes, plugs)
    
    def clearAffectedAttributes(self):
        with UndoContext("Clear Affected Attributes"):
            self.clearList(self._affectedAttributes)

    def addAffectedAttribute(self, plug):
        with UndoContext("Add Affected Attribute"):
            self.addItem(self._affectedAttributes, plug)

    def removeAffectedAttribute(self, plug):
        with UndoContext("Remove Affected Attribute"):
            self.removeItemListByPlug(self._affectedAttributes, plug)

    # Child Keing Groups ----
    
    def getParentKeyingGroups(self):
        return self.getOutputSingle(self._parentKeyingGroup, cls=KeyingGroup)
    
    def getRootKeyingGroups(self, onlyEnabled=False):
        roots = set()
        if not onlyEnabled or self.enabled:
            parents = self.getParentKeyingGroups()
            for parent in parents:
                roots.update(parent.getRootKeyingGroups(onlyEnabled=onlyEnabled))
            if len(roots) == 0:
                roots.add(self)
        return roots
        
    def clearParentKeyingGroups(self):
        with UndoContext("Clear Parent Keying Groups"):
            self.clearConnection(self._parentKeyingGroup)
            
    def getChildKeyingGroups(self):
        return self.getInputFromListAttribute(self._childKeyingGroups, cls=KeyingGroup) or []
            
    def setChildKeyingGroups(self, children):
        with UndoContext("Set Child Keying Groups"):
            for child in children:
                child.clearConnection(child._parentKeyingGroup)
            self.setInputListWrappers(self._childKeyingGroups, children, inputAttribute=KeyingGroup._parentKeyingGroup)
    
    def clearChildKeyingGroups(self):
        with UndoContext("Clear Child Keying Groups"):
            self.clearList(self._childKeyingGroups)

    def addChildKeyingGroup(self, child):
        with UndoContext("Add Child Keying Group"):
            child.clearConnection(child._parentKeyingGroup)
            self.addItem(self._childKeyingGroups, child.getPlug(child._parentKeyingGroup))

    def removeChildKeyingGroup(self, child):
        with UndoContext("Remove Child Keying Group"):
            self.removeItemListByPlug(self._childKeyingGroups, child.getPlug(self._parentKeyingGroup))

    # JSON ----
    
    def asJson(self):
        attrData = []
        affectedAttributes = self.getAffectedAttributes(includeChildren=False)
        for attr in affectedAttributes:
            attrData.append(attr)
            
        childData = []
        children = self.getChildKeyingGroups()
        for child in children:
            childData.append(child.asJson())
            
        data = {}
        data["name"] = self.node
        data["enabled"] = self.enabled
        data["affectedAttributes"] = attrData
        data["children"] = childData
        
        return data
    
    @classmethod
    def fromJson(self, data):
        with UndoContext("KeyingGroup From JSON"):
            kg = KeyingGroup().create(nodeName=data["name"])
            
            kg.enabled = data.get("enabled", True)
            
            missingAttributesMessage = ""
            for attr in data["affectedAttributes"]:
                if cmds.objExists(attr):
                    kg.addAffectedAttribute(attr)
                else:
                    missingAttributesMessage += "\n- {}".format(attr)
            if missingAttributesMessage != "":
                print("Warning: Missing Attribute when importing KeyingGroup:{}".format(missingAttributesMessage))

            for child in data["children"]:
                kg.addChildKeyingGroup(KeyingGroup.fromJson(child))
        
        return kg


class KeyingGroupTimeSliderPainter(TimeSliderOverlay.TimeSliderPainter):
    
    OPTIONVAR_ENABLED = "KEYINGGROUPTIMESLIDERPAINTER_ENABLE"
    OPTIONVAR_COLOR_SYNC_KEYS = "KEYINGGROUPTIMESLIDERPAINTER_COLOR_SYNC_KEYS"
    OPTIONVAR_DISPLAY_MISSING_KEYS = "KEYINGGROUPTIMESLIDERPAINTER_DISPLAY_MISSING_KEYS"
    
    # This proxy method is mainly used so the menu can ask this class wheter or not it's options should be enabled or not.
    @classmethod
    def isTimeSliderOverlayEnabled(cls):
        import MayaImprovements.CustomTimeSlider     # JIT import to avoid cycles
        return MayaImprovements.CustomTimeSlider.CustomTimeSliderManager.isTimeSliderOverlayEnabled()
    
    @classmethod
    def isKeyingGroupsOverlayEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isTimeSliderOverlayEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.OPTIONVAR_ENABLED):
            default = True  # Enabled by default
            cls.setKeyingGroupsOverlayEnabled(default, refresh=False)
            return default
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ENABLED)
    
    @classmethod
    def setKeyingGroupsOverlayEnabled(cls, value, refresh=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_ENABLED, value))
        
        KeyingGroupManager.timeSliderPainter.setDirty(update=refresh)

    @classmethod
    def isColorSyncKeysEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isKeyingGroupsOverlayEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.OPTIONVAR_COLOR_SYNC_KEYS):
            default = True  # Enabled by default
            cls.setColorSyncKeysEnabled(default, refresh=False)
            return default
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_COLOR_SYNC_KEYS)
    
    @classmethod
    def setColorSyncKeysEnabled(cls, value, refresh=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_COLOR_SYNC_KEYS, value))
        
        KeyingGroupManager.timeSliderPainter.setDirty(update=refresh)

    @classmethod
    def isDisplayMissingKeysEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isKeyingGroupsOverlayEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.OPTIONVAR_DISPLAY_MISSING_KEYS):
            default = True  # Enabled by default
            cls.setDisplayMissingKeysEnabled(default, refresh=False)
            return default
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_DISPLAY_MISSING_KEYS)
    
    @classmethod
    def setDisplayMissingKeysEnabled(cls, value, refresh=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_DISPLAY_MISSING_KEYS, value))
        
        KeyingGroupManager.timeSliderPainter.setDirty(update=refresh)

    def __init__(self, enabled=True):
        TimeSliderOverlay.TimeSliderPainter.__init__(self, enabled=enabled)

        self.clean = False
        self.pixmap = None
        self.keyframeColors = {}

    def setDirty(self, dirty=True, update=False):
        self.clean = not dirty
        if update and self.overlay: # If the improvements are Off, this Painter will exist, but it won't be registered on the overlay
            self.overlay.update()
            
    def onOverlayResized(self, size):
        self.pixmap = QtGui.QPixmap(size.width(), size.height())
        self.setDirty()

    def onSelectionChanged(self):
        self.setDirty()

    def onAnimationRangeChanged(self):
        self.setDirty()

    def onChannelBoxLabelSelected(self):
        # We need the timeline to update if it is not synced to the channelbox (to update the previous value)
        update = cmds.optionVar(q="timeSliderShowKeys") != "mainChannelBox"
        self.setDirty(update=update)

    def onSyncTimeSliderOptionChanged(self):
        self.setDirty(update=True)  # We need the timeline to update here

    def onAnimLayerDisplayOptionsChanged(self):
        self.setDirty()

    def onAnimCurveEdited(self, animCurves):
        self.setDirty()
        
    def onConnectionChanged(self, sourcePlug, destinationPlug, connectionMade):
        self.setDirty()

    def paint(self, painter, event):
        # If a new scene is being opened, we might retrieve animation curves for objects that no longer exist.
        if cmds.isTrue("opening") or cmds.isTrue("newing"):
            return
        
        if not KeyingGroupManager._callbacksEnabled or not self.isKeyingGroupsOverlayEnabled():
            return

        rangeStart = cmds.playbackOptions(q=True, min=True)
        rangeEnd = cmds.playbackOptions(q=True, max=True)
        displayRange = (rangeStart, rangeEnd + 1) # The display range always shows the next to last frame as well
        displayRangeLength = displayRange[1] - displayRange[0]
        if cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeVisible=True):
            selectedRange = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeArray=True)
        else:
            selectedRange = None

        if not self.clean:
            self.keyframeColors = {}
            selectedAnimCurves = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, animCurveNames=True) or []
            selectedPlugs = set()
            affectedPlugs = set()
            for animCurve in selectedAnimCurves:
                plugs = AnimNodeUtils.getTargetPlugsForAnimNode(OpenMayaUtils.asMObject(animCurve, api=OpenMaya), api=OpenMaya)
                plugNames = set([plug.name() for plug in plugs])
                selectedPlugs.update(plugNames)
                affectedPlugs.update(KeyingGroupManager.getPlugsToModify(plugNames, filterByLayer=False))
            
            layeredAffectedPlugs = affectedPlugs if len(AnimLayerUtils.getAnimLayers()) <= 1 else [plug for plug in affectedPlugs if AnimLayerUtils.getBestAnimLayerForPlug(plug)]
            
            keyTimes = {}
            for affectedPlug in affectedPlugs:
                times = cmds.keyframe(affectedPlug, q=True, time=displayRange) or []
                for time in times:
                    if time not in keyTimes:
                        keyTimes[time] = set()
                    keyTimes[time].add(affectedPlug)
            
            affectedPlugsCount = len(affectedPlugs)
            layeredAffectedPlugsCount = len(layeredAffectedPlugs)
            syncColor = QtCore.Qt.cyan if self.isColorSyncKeysEnabled() else None
            layerSyncColor = QtGui.QColor.fromRgb(255, 128, 0) if self.isColorSyncKeysEnabled() else None
            missingColor = QtCore.Qt.black if self.isDisplayMissingKeysEnabled() else None
            unsyncColor = QtCore.Qt.magenta
            for keyTime, plugs in keyTimes.items():
                plugCount = len(plugs)
                if plugCount == affectedPlugsCount:
                    self.keyframeColors[keyTime] = syncColor
                elif selectedPlugs.isdisjoint(plugs):
                    self.keyframeColors[keyTime] =  missingColor
                elif plugCount == layeredAffectedPlugsCount:
                    self.keyframeColors[keyTime] =  layerSyncColor
                else:
                    self.keyframeColors[keyTime] =  unsyncColor

        if not self.clean or self.previousSelectedRange != selectedRange:
            timeArea = QtCore.QRectF(self.overlay.rect())
            timeArea.setX(timeArea.x() + self.TIME_AREA_MARGIN_LEFT)
            timeArea.setY(timeArea.y())
            timeArea.setWidth(timeArea.width() - self.TIME_AREA_MARGIN_RIGHT)
            timeArea.setHeight(timeArea.height())

            timeToPixelFactor = timeArea.width() / displayRangeLength
            tickSize = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, tickSize=True)

            self.pixmap.fill(QtCore.Qt.transparent)
            
            pixmapPainter = QtGui.QPainter(self.pixmap)
            pixmapPainter.setRenderHint(painter.Antialiasing)
            for keyTime, color in self.keyframeColors.items():
                if color == None:
                    continue

                if color != QtCore.Qt.black and selectedRange != None and keyTime >= selectedRange[0] and keyTime < selectedRange[1]:
                    color = QtCore.Qt.yellow

                horizontalOffset = timeArea.x() + (keyTime - rangeStart) * timeToPixelFactor + 0.5 * tickSize
                verticalOffset = timeArea.y()
                height = timeArea.height()
                
                pixmapPainter.fillRect(horizontalOffset, verticalOffset, tickSize, height, color)
            pixmapPainter.end()
        
        self.previousSelectedRange = selectedRange              
        self.clean = True

        if self.pixmap != None:
            painter.drawPixmap(self.overlay.rect(), self.pixmap)


class KeyingGroupManager(AnimSystems.KeyEditedListener, CommandCallback.CommandListener):
    
    _callbacksEnabled = True   # Enabled by default
    _callbackPriority = 100
    
    DISABLING_COMMANDS = [
        ("filterCurve", CommandCallback.CommandCallbackManager.TYPE_COMMAND)
    ]
    
    CALLBACKS_ENABLED_OPTION_VAR = "KEYING_GROUP_CALLBACKS_ENABLED"
    
    brokenAnimCurveConnections = {}
    
    connectionBrokenCallback = None
    
    timeSliderPainter = KeyingGroupTimeSliderPainter()
    
    @classmethod
    def initialize(cls):
        AnimSystems.AnimSystemsCallbackManager.addAnimKeyEditedListener(cls)
        for command, type in cls.DISABLING_COMMANDS:
            CommandCallback.CommandCallbackManager.addCommandCallbackListener(command, type, cls)
        
        cls.connectionBrokenCallback = OpenMaya.MDGMessage.addPreConnectionCallback(cls.onConnectionBroken)
    
        if cmds.optionVar(exists=cls.CALLBACKS_ENABLED_OPTION_VAR):
            cls._callbacksEnabled = cmds.optionVar(q=cls.CALLBACKS_ENABLED_OPTION_VAR)
    
    @classmethod
    def uninitialize(cls):
        AnimSystems.AnimSystemsCallbackManager.removeAnimKeyEditedListener(cls)
        for command, type in cls.DISABLING_COMMANDS:
            CommandCallback.CommandCallbackManager.removeCommandCallbackListener(command, type, cls)
        
        OpenMaya.MMessage.removeCallback(cls.connectionBrokenCallback)
        cls.connectionBrokenCallback = None
    
    @classmethod
    def setCallbacksEnabled(cls, enabled, saveOptionVar=True):
        cls._callbacksEnabled = enabled
        if saveOptionVar:
            cmds.optionVar(iv=(cls.CALLBACKS_ENABLED_OPTION_VAR, enabled))
            
        cls.timeSliderPainter.setDirty(update=True)
    
    @classmethod
    def onAfterCommand(cls, id):
        if cls._callbacksEnabled:
            cls._callbacksEnabled = False
            try:
                OpenMayaAnim.MAnimMessage.flushAnimKeyframeEditedCallbacks()
            finally:
                cls._callbacksEnabled = True
            
    @staticmethod
    def onReset():
        TimeSlider.refresh()
    
    @staticmethod
    def animKeyModedSortFunction(e):
        return e[0][1]

    @staticmethod
    def getKeyIndex(curveFn, mTime):
        scriptUtil = OpenMaya.MScriptUtil()
        scriptUtil.createFromInt(0)
        indexPointer = scriptUtil.asUintPtr()
        if curveFn.find(mTime, indexPointer):
            return scriptUtil.getUint(indexPointer)
        else:
            return None

    @classmethod
    def onConnectionBroken(cls, srcPlug, dstPlug, isNew, data):
        if cls.isCallbacksEnabled() and not isNew and srcPlug.partialName(False, False, False, False, False, True) == "output":
            srcNode = srcPlug.node()
            if srcNode.hasFn(OpenMaya.MFn.kAnimCurve):
                srcNodeFn = OpenMayaAnim.MFnAnimCurve(srcNode)
                if srcNodeFn.numKeys() == 0:
                    plugs = AnimNodeUtils.getTargetPlugsForAnimNode(srcNode, api=OpenMaya)
                    # The plugs seem to break if we store them ant attempt to retrieve them later. So instead, store de the node and the attribute name to retrieve it later.
                    cls.brokenAnimCurveConnections[srcNodeFn.name()] = [(OpenMaya.MFnDependencyNode(plug.node()), plug.partialName(False, False, False, False, False, True)) for plug in plugs]
    
    @classmethod
    def onAnimKeyEdited(cls, keyChanges, data):
        keyChangesAdd = []
        keyChangesRemove = []
        keyChangesMove = []
        for keyChange in keyChanges:
            if keyChange.type == AnimSystems.KeyChange.TYPE_ADD or keyChange.type == AnimSystems.KeyChange.TYPE_REPLACE:
                keyChangesAdd.append(keyChange)
            elif keyChange.type == AnimSystems.KeyChange.TYPE_REMOVE:
                keyChangesRemove.append(keyChange)
            elif keyChange.type == AnimSystems.KeyChange.TYPE_MOVE:
                keyChangesMove.append(keyChange)
            
        if keyChangesAdd:
            keyChanges += cls.onAnimKeyAdded(keyChangesAdd)
        if keyChangesRemove:
            keyChanges += cls.onAnimKeyRemoved(keyChangesRemove)
        if keyChangesMove:
            keyChanges += cls.onAnimKeyMoved(keyChangesMove)
                
        return keyChanges

    @classmethod
    def onAnimKeyAdded(cls, keyChanges):
        newChanges = []
        plugs = cls.getPlugsToModifyFromKeyChanges(keyChanges, skipAffected=True)
        if len(plugs) > 0:
            times = {}
            for keyChange in keyChanges:
                time = keyChange.time.asUnits(OpenMaya.MTime.uiUnit())
                if time not in times:
                    times[time] = keyChange.time
                
            plugData = {}
            for plug in plugs:
                curveName = AnimLayerUtils.getAnimCurveForAttribute(plug)
                if curveName:
                    curve = OpenMayaUtils.asMObject(curveName, api=OpenMaya)
                    curveFn = OpenMayaAnim.MFnAnimCurve(curve)
                    valueAtTime = {}
                    for time, mTime in times.items():
                        index = cls.getKeyIndex(curveFn, mTime)
                        if index != None:
                            valueAtTime[time] = curveFn.value(index)
                        else:
                            valueAtTime[time] = None
                else:
                    curve = None
                    valueAtTime = {}
                    for time in times:
                        valueAtTime[time] = None
                plugData[plug] = (curve, valueAtTime)
                
            with UndoContext("AnimKeyAdded"):
                cmds.setKeyframe(plugs, t=list(times))
                
            AnimSystems.AnimSystemsUndo().commit()
            
            for plug in plugData.keys():
                curve, valueAtTime = plugData[plug]
                if curve == None:
                    curveName = AnimLayerUtils.getAnimCurveForAttribute(plug)
                    if curveName:
                        curve = OpenMayaUtils.asMObject(curveName, api=OpenMaya)
                    else:
                        continue
                        
                curveFn = OpenMayaAnim.MFnAnimCurve(curve)
                for time, mTime in times.items():
                    index = cls.getKeyIndex(curveFn, mTime)
                    
                    change = AnimSystems.KeyChange()
                    
                    change.keyIndex = index
                    change.paramCurve = curve
                    
                    change.type = AnimSystems.KeyChange.TYPE_ADD if valueAtTime[time] == None else AnimSystems.KeyChange.TYPE_REPLACE
                    
                    change.deltaType = OpenMayaAnim.MFnKeyframeDeltaAddRemove.kAdded if valueAtTime[time] == None else OpenMayaAnim.MFnKeyframeDeltaAddRemove.kReplaced
                    change.value = curveFn.value(index)
                    change.time = mTime
                    change.replacedValue = valueAtTime[time]
                    
                    newChanges.append(change)
            
        return newChanges

    @classmethod
    def onAnimKeyRemoved(cls, keyChanges):
        newChanges = []
        plugs = cls.getPlugsToModifyFromKeyChanges(keyChanges, skipAffected=True)
        if len(plugs) > 0:
            # Saves each plug's value in case it is resetted when deleting it's last keyframe
            defaultValues = [cmds.getAttr(plug) for plug in plugs]
            
            times = {}
            for keyChange in keyChanges:
                time = keyChange.time.asUnits(OpenMaya.MTime.uiUnit())
                if time not in times:
                    times[time] = keyChange.time
                    
            plugData = {}
            for plug in plugs:
                curveName = AnimLayerUtils.getAnimCurveForAttribute(plug)
                if curveName:
                    curve = OpenMayaUtils.asMObject(curveName, api=OpenMaya)
                    curveFn = OpenMayaAnim.MFnAnimCurve(curve)
                    indexAtTime = {}
                    for time, mTime in times.items():
                        index = cls.getKeyIndex(curveFn, mTime)
                        if index != None:
                            indexAtTime[time] = index
                    if indexAtTime:
                        plugData[plug] = (curve, indexAtTime)
                
            with UndoContext("AnimKeyRemoved"):
                for time in times:
                    cmds.cutKey(plugs, t=(time, time), clear=True, option="keys")
                
                # If we have deleted the last keyframe on a plug, it will be reset to 0 instead of keeping it's value, restores it
                for i in range(len(plugs)):
                    if cmds.keyframe(plugs[i], q=True, kc=True) == 0:
                        cmds.setAttr(plugs[i], defaultValues[i])
                    
            AnimSystems.AnimSystemsUndo().commit()
            
            for plug in plugData.keys():
                curve, indexAtTime = plugData[plug]
                for time, index in indexAtTime.items():
                    change = AnimSystems.KeyChange()
                    
                    change.keyIndex = sys.maxsize   # The usual behaviour for deleting key is that the index is set to a huge number
                    change.paramCurve = curve
                    
                    change.type = AnimSystems.KeyChange.TYPE_REMOVE
                    
                    change.deltaType = OpenMayaAnim.MFnKeyframeDeltaAddRemove.kRemoved
                    change.value = None
                    change.time = times[time]
                    change.replacedValue = None
                    
                    newChanges.append(change)
            
        return newChanges
    
    @classmethod
    def onAnimKeyMoved(cls, keyChanges):
        changesByTime = {}
        for keyChange in keyChanges:
            timeKey = (keyChange.previousTime.asUnits(OpenMaya.MTime.uiUnit()), keyChange.currentTime.asUnits(OpenMaya.MTime.uiUnit()))
            if timeKey[0] != timeKey[1]:
                if timeKey in changesByTime:
                    changesByTime[timeKey].append(keyChange)
                else:
                    changesByTime[timeKey] = [keyChange]
        
        forwardChanges = []
        backwardChanges = []
        for timeKey, changes in changesByTime.items():
            if timeKey[0] < timeKey[1]:
                forwardChanges.append((timeKey, changes))
            else:
                backwardChanges.append((timeKey, changes))
        forwardChanges.sort(key=cls.animKeyModedSortFunction, reverse=True)
        backwardChanges.sort(key=cls.animKeyModedSortFunction)
        forwardChanges.extend(backwardChanges)
        
        newChanges = []
        needsUndo = False
        with UndoContext("AnimKeyMoved"):
            for timeKey, changes in forwardChanges:
                plugs = cls.getPlugsToModifyFromKeyChanges(changes, skipAffected=True)
                if len(plugs) > 0:
                    plugData = {}
                    mTimeKey = tuple(OpenMaya.MTime(t, OpenMaya.MTime.uiUnit()) for t in timeKey)
                    for plug in plugs:
                        curveName = AnimLayerUtils.getAnimCurveForAttribute(plug)
                        if curveName:
                            curve = OpenMayaUtils.asMObject(curveName, api=OpenMaya)
                            curveFn = OpenMayaAnim.MFnAnimCurve(curve)
                            index = cls.getKeyIndex(curveFn, mTimeKey[0])
                            if index != None:
                                value = curveFn.value(index)
                                plugData[plug] = (curve, index, value)
                    
                    cmds.keyframe(plugs, t=(timeKey[0], timeKey[0]), tc=timeKey[1], option="over", absolute=True)
                    
                    needsUndo = True
                    
                    for plug in plugData.keys():
                        curve, previousIndex, previousValue = plugData[plug]
                        curveFn = OpenMayaAnim.MFnAnimCurve(curve)
                        
                        index = cls.getKeyIndex(curveFn, mTimeKey[1])
                        
                        change = AnimSystems.KeyChange()
                        
                        change.keyIndex = index
                        change.paramCurve = curve
                        
                        change.type = AnimSystems.KeyChange.TYPE_MOVE
                        
                        change.previousTime = mTimeKey[0]
                        change.currentTime = mTimeKey[1]
                        change.previousValue = previousValue
                        change.currentValue = previousValue # The value should not have changed
                        change.previousIndex = previousIndex
                        
                        newChanges.append(change)
                        
        if needsUndo:
            AnimSystems.AnimSystemsUndo().commit()
            
        return newChanges

    @classmethod
    def getPlugsToModifyFromKeyChanges(cls, keyChanges, skipAffected=False):
        return cls.getPlugsToModifyFromCurves([keyChange.paramCurve for keyChange in keyChanges], skipAffected=skipAffected)
    
    @classmethod
    def getPlugsToModifyFromCurves(cls, animCurves, skipAffected=False):
        affectedPlugs = set()
        for animCurve in animCurves:
            animCurveNodeFn = OpenMaya.MFnDependencyNode(animCurve)
            plugs = cls.brokenAnimCurveConnections.pop(animCurveNodeFn.name(), None)
            if plugs != None:
                plugs = [plug[0].findPlug(plug[1], False) for plug in plugs]
            else:
                plugs = AnimNodeUtils.getTargetPlugsForAnimNode(animCurveNodeFn, api=OpenMaya)
            for plug in plugs:
                plugName = plug.name()
                if plugName not in affectedPlugs:
                    affectedPlugs.add(plugName)
        
        return cls.getPlugsToModify(affectedPlugs, skipAffected=skipAffected)
    
    @classmethod
    def getPlugsToModify(cls, affectedPlugs, skipAffected=False, includeNonAffected=False, filterByLayer=True):        
        plugsToModify = []
        affectedKeyingGroups = set()
        for plugName in affectedPlugs:
            keyingGroups = cls.getKeyingGroupsForPlug(plugName)
            if keyingGroups:
                affectedKeyingGroups.update(keyingGroups)
            elif includeNonAffected:
                plugsToModify.append(plugName)
        
        for keyingGroup in affectedKeyingGroups:
            plugs = keyingGroup.getAffectedAttributes(includeChildren=True)
            for plug in plugs:
                if plug not in plugsToModify and (not skipAffected or plug not in affectedPlugs):
                    plugsToModify.append(plug)
        
        if filterByLayer and len(AnimLayerUtils.getAnimLayers()) > 1:
            plugsToModify = [plug for plug in plugsToModify if AnimLayerUtils.getBestAnimLayerForPlug(plug)]
        
        return plugsToModify
        
    @classmethod
    def getKeyingGroupsForPlug(cls, plugName):
        keyingGroups = cmds.listConnections(plugName, s=False, d=True, type="customKeyingGroup") or []
        keyingGroups = [KeyingGroup(kg) for kg in keyingGroups]
        
        keyingGroupSet = set()
        for keyingGroup in keyingGroups:
            keyingGroupSet.update(keyingGroup.getRootKeyingGroups(onlyEnabled=True))
        
        return keyingGroupSet
    
    @classmethod
    def resynchronizeControls(cls, controls, animationRange=None):
        keyingGroups = set()
        for control in controls:
            controlFn = OpenMaya.MFnDependencyNode(control)
            plugs = OpenMaya.MPlugArray()
            controlFn.getConnections(plugs)
            for i in range(plugs.length()):
                keyingGroups.update(cls.getKeyingGroupsForPlug(plugs[i].name()))
            
        with AnimSystems.CallbacksDisabledContext(), UndoContext("Resynchronize Keys"):     
            for keyingGroup in keyingGroups:
                affectedAttributes = keyingGroup.getAffectedAttributes(includeChildren=True)
                keyTimes = set()
                for attr in affectedAttributes:
                    if animationRange != None:
                        keyTimes.update(cmds.keyframe(attr, q=True, timeChange=True, time=(animationRange[0], animationRange[1])) or [])
                    else:
                        keyTimes.update(cmds.keyframe(attr, q=True, timeChange=True) or [])
                
                for keyTime in keyTimes:
                    cmds.setKeyframe(affectedAttributes, insert=True, time=keyTime)
    
    @classmethod
    def resynchronizeSelectedControls(cls, animationRange=None):
        activeList = OpenMaya.MSelectionList()
        OpenMaya.MGlobal.getActiveSelectionList(activeList)
        currentSelection = []
        for i in range(activeList.length()):
            mObject = OpenMaya.MObject()
            activeList.getDependNode(i, mObject)
            currentSelection.append(mObject)
        cls.resynchronizeControls(currentSelection, animationRange=animationRange)
    
    @classmethod
    def resynchronizeSelectedControlsOnCurrentRange(cls):
        if cmds.timeControl(TimeSlider.defaultTimeSlider , q=True, rangeVisible=True):
            selectedRange = cmds.timeControl(TimeSlider.defaultTimeSlider , q=True, range=True)
            selectedRange = selectedRange[1:-1].split(":")  # For some reason, this string has it's content wrapped with an extra layer of quotes (""32:54"")
            currentRange = (int(selectedRange[0]), int(selectedRange[1]))
        else:
            currentRange = (cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
        cls.resynchronizeSelectedControls(animationRange=currentRange)
