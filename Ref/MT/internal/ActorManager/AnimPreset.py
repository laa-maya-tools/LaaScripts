# -*- coding: utf-8 -*-
from NodeManager import NodeWrapper

import maya.cmds as cmds

import Exporter

from Utils.Maya.UndoContext import UndoContext, UndoOff, AutoUndo
import Utils.Maya.AnimLayers as AnimLayerUtils

import os

class WeightedLayer(NodeWrapper.NodeWrapper):
    _Type           = "weightedLayer"
    
    #------------ Attr
    _animLayer      = "animLayer"
    _weight         = "weight"
    
    # animLayer --------------------------------------
    @property
    def animLayer(self):
        return self.getInputSingle(self._animLayer)
    
    @animLayer.setter
    def animLayer(self, value):
        with UndoContext("Set WeightedLayer AnimLayer"):
            self.setInputNode(self._animLayer, value)

    # weight --------------------------------------
    @property
    def weight(self):
        return self.getAttr(self._weight)
    
    @weight.setter
    def weight(self, value):
        with UndoContext("Set WeightedLayer Weight"):
            self.setNumericAttribute(self._weight, value)


class AnimPreset(NodeWrapper.NodeWrapper): 
    _Type           = "animPreset"
    
    #------------ Attr
    _nameParts          = "nameParts"
    _enabled            = "enabled"
    _active             = "active"
    _path               = "path"
    _start              = "rangeStart"  # Debido a una conversión de tipo (int -> MTime) ahora usamos otro atributo
    _end                = "rangeEnd"    # Debido a una conversión de tipo (int -> MTime) ahora usamos otro atributo
    _loop               = "loop"
    _mirror             = "mirror"
    _pose               = "pose"
    _color              = "color"
    _holder             = "actor"       # Debido a un cambio de paradigma, el atributo no ha cambiado de nombre en el nodo y sigue llamándose "actor"
    _subHolder          = "subActor"    # Debido a un cambio de paradigma, el atributo no ha cambiado de nombre en el nodo y sigue llamándose "subActor"
    _animLayerList      = "animLayerList"
    _category           = "category"
    
    def __init__(self, node=None):
        super(AnimPreset, self).__init__(node)
    
    def clone(self):
        with UndoContext("Clone Wrapped Node"):
            clonedNode = cmds.duplicate(self.node, inputConnections=True)[0]
            clonedAnimPreset = AnimPreset(node=clonedNode)
            
            weightedLayers = self.getWeightedLayers()
            clonedWeightedLayers = [weightedLayer.clone() for weightedLayer in weightedLayers]
            clonedAnimPreset.setWeightedLayers(clonedWeightedLayers, deleteOld=False)

            return clonedAnimPreset

    # nameParts --------------------------------------

    def getConcatenatedName(self):
        return ''.join(self.getNameParts()).lstrip()
    
    def getNameParts(self):
        return self.getAttr(self._nameParts) or []
    
    def getNamePartByIndex(self,index):
        temp = self.getAttr(self._nameParts)
        return temp[index]    
    
    def setNameParts(self, listValue):
        with UndoContext("Set AnimPreset NameParts"):
            self.setStringArrayAttribute(self._nameParts, listValue)
            
    def setNamePartByIndex(self, value, index):
        with UndoContext("Set AnimPreset NameParts"):
            listValue = self.getAttr(self._nameParts)
            listValue[index] = value
            self.setStringArrayAttribute(self._nameParts, listValue) 

    # enabled --------------------------------------
    @property
    def enabled(self):
        return self.getAttr(self._enabled)
    
    @enabled.setter
    def enabled(self, value):
        with UndoContext("Set AnimPreset Enabled"):
            self.setNumericAttribute(self._enabled, value)

    # active --------------------------------------
    @property
    def active(self):
        return self.getAttr(self._active)
    
    @active.setter
    def active(self, value):
        with UndoContext("Set AnimPreset Active"):
            self.setNumericAttribute(self._active, value)

    # path --------------------------------------
    @property
    def path(self):
        p = self.getAttr(self._path)
        if not p:
            p = self.getSubHolder().getAnimPath()
        return p
    
    @path.setter
    def path(self, value):
        with UndoContext("Set AnimPreset Path"):
            defaultAnimPath = self.getSubHolder().getAnimPath()
            if os.path.normpath(value).lower() == os.path.normpath(defaultAnimPath).lower():
                value = ""
            self.setStringAttribute(self._path, value)

    # start --------------------------------------
    @property
    def start(self):
        return self.getAttr(self._start)
    
    @start.setter
    def start(self, value):
        with UndoContext("Set AnimPreset Start"):
            self.setNumericAttribute(self._start, value)

    # end --------------------------------------
    @property
    def end(self):
        return self.getAttr(self._end)
    
    @end.setter
    def end(self, value):
        with UndoContext("Set AnimPreset End"):
            self.setNumericAttribute(self._end, value)

    # loop --------------------------------------
    @property
    def loop(self):
        return self.getAttr(self._loop)
    
    @loop.setter
    def loop(self, value):
        with UndoContext("Set AnimPreset Loop"):
            self.setNumericAttribute(self._loop, value)

    # mirror ------------------------------------
    @property
    def mirror(self):
        return self.getAttr(self._mirror)
    
    @mirror.setter
    def mirror(self, value):
        with UndoContext("Set AnimPreset Mirror"):
            self.setNumericAttribute(self._mirror, value)

    # pose --------------------------------------
    @property
    def pose(self):
        return self.getAttr(self._pose)
    
    @pose.setter
    def pose(self, value):
        with UndoContext("Set AnimPreset Pose"):
            self.setNumericAttribute(self._pose, value)

    # color --------------------------------------
    @property
    def color(self):
        return self.getAttr(self._color)[0]
    
    @color.setter
    def color(self, value): 
        with UndoContext("Set AnimPreset Color"):
            self.setFloat3Attribute(self._color, value)
        
    # subHolder --------------------------------------
    @property
    def subHolder(self):
        import ActorManager.AnimPresetHolder as AnimPresetHolder
        return self.getInputSingle(self._subHolder, cls=AnimPresetHolder.AnimPresetSubHolder)
    
    @subHolder.setter
    def subHolder(self, inputWrapper):
        with UndoContext("Set AnimPreset SubHolder"):
            self.setInputWrapper(self._subHolder, inputWrapper, inputAttribute=inputWrapper.getSubHolderPlug() if inputWrapper else "")

    # holder --------------------------------------
    def getHolder(self):
        holder = self.getOutputSingle(self._holder)
        if len(holder) > 0:
            import ActorManager.Actor as Actor
            import ActorManager.CameraSet as CameraSet
            holder = holder[0]
            holderNodeType = cmds.nodeType(holder)
            if holderNodeType == Actor.Actor._Type:
                return Actor.Actor(holder)
            elif holderNodeType == CameraSet.CameraSet._Type:
                return CameraSet.CameraSet(holder)
            else:
                raise AssertionError("Unknown Holder Class: {}".format(holderNodeType))
        else:
            return None
    
    def getSubHolder(self):
        subHolder = self.subHolder
        if subHolder == None:
            subHolder = self.getHolder().getMainSubHolder()
        return subHolder
    
    def changeHolder(self, newHolder):
        currentHolder = self.getHolder()
        if currentHolder != newHolder:
            with UndoContext("Change AnimPreset Holder"):
                self.subHolder = None
                currentHolder.removeAnimPreset(self, delete=False)
                newHolder.addAnimPreset(self)
                
                selfNameParts = self.getNameParts()
                selfNamePartsCount = len(selfNameParts)
                
                newActorAnimPresets = list(newHolder.getAnimPresets())
                newActorAnimPresets.remove(self)
                if newActorAnimPresets:
                    newActorNamePartsCount = len(newActorAnimPresets[0].getNameParts())
                    
                    if newActorNamePartsCount < selfNamePartsCount:
                        for animPreset in newActorAnimPresets:
                            nameParts = animPreset.getNameParts()
                            nameParts += [""] * (selfNamePartsCount - newActorNamePartsCount)
                            animPreset.setNameParts(nameParts)
                    
                    elif newActorNamePartsCount > selfNamePartsCount:
                        selfNameParts += [""] * (newActorNamePartsCount - selfNamePartsCount)
                        self.setNameParts(selfNameParts)

    # animLayerList --------------------------------------

    def getWeightedLayers(self):
        return self.getInputFromListAttribute(self._animLayerList, cls=WeightedLayer)
    
    def getAnimLayers(self):    
        weightedLayers = self.getWeightedLayers()
        return [weightedLayer.animLayer for weightedLayer in weightedLayers]
    
    def getWeightedLayerByAnimLayer(self, animLayer):
        weightedLayers = self.getWeightedLayers()
        for weightedLayer in weightedLayers:
            if weightedLayer.animLayer == animLayer:
                return weightedLayer
        return None
    
    def setAnimLayerWeight(self, animLayer, weight, enableInactive=False):
        weightedLayer = self.getWeightedLayerByAnimLayer(animLayer)
        if not weightedLayer:
            if not enableInactive:
                return
            else:
                self.addAnimLayer(animLayer)
                weightedLayer = self.getWeightedLayerByAnimLayer(animLayer)
        
        weightedLayer.weight = weight
    
    def addAnimLayer(self, animLayer, weight=1):
        with UndoContext("Add AnimLayer to AnimPreset"):
            weightedLayer = WeightedLayer().create()
            weightedLayer.animLayer = animLayer
            weightedLayer.weight = weight
            self.appendInputPlug(self._animLayerList, weightedLayer.getPlug("message"))
    
    def removeAnimLayer(self, animLayer, delete=True):
        with UndoContext("Remove AnimLayer from AnimPreset"):
            weightedLayer = self.getWeightedLayerByAnimLayer(animLayer)
            if weightedLayer:
                self.removeItemListByPlug(self._animLayerList, weightedLayer.getPlug("message"), delete=delete)
    
    def clearAnimLayers(self, delete=True):
        with UndoContext("Clear AnimPreset Layers"):
            self.clearList(self._animLayerList, removeInput=True, removeOutput=False, deleteInputNode=delete, deleteOutputNode=False)      
    
    def setWeightedLayers(self, weightedLayers, deleteOld=True):
        with UndoContext("Set AnimPreset Layers"):
            self.clearAnimLayers(delete=deleteOld)
            self.setInputListWrappers(self._animLayerList, weightedLayers, inputAttribute="message")

    def setAnimLayers(self, animLayerList, weightList=None, deleteOld=True):
        if weightList != None and len(weightList) != len(animLayerList):
            raise AssertionError("Weight List size not matching the number of AnimLayers provided!")
        
        with UndoContext("Set AnimPreset Layers"):
            weightedLayers = []
            for i in range(len(animLayerList)):
                weightedLayer = WeightedLayer().create()
                weightedLayer.animLayer = animLayerList[i]
                if weightList != None:
                    weightedLayer.weight = weightList[i]
                weightedLayers.append(weightedLayer)
            
            self.setWeightedLayers(weightedLayers, deleteOld=deleteOld)

    @staticmethod
    def shouldUseAnimLayerWeight(animLayer):
        weightedLayers = WeightedLayer.getConnectedWrappers([animLayer])
        for weightedLayer in weightedLayers:
            if weightedLayer.weight != 1:
                return True
        return False

    # category --------------------------------------
    @property
    def category(self):
        return self.getAttr(self._category)
    
    @category.setter
    def category(self, value):
        with UndoContext("Set AnimPreset Category"):
            self.setStringAttribute(self._category, value)

        
    # Methods ---------------------------------------
    
    goToStart = "start"
    goToEnd = "end"
    goToClamp = "clamp"
    goToRelative = "relative"
    goToNone = None
    
    oldStart = None
    oldEnd = None
    
    def applyAnimRange(self, goTo=goToStart, combine=False):
        with UndoContext("Apply AnimPreset Range"):
            if not combine:
                AnimPreset.oldStart = cmds.playbackOptions(q=True, min=True)
                AnimPreset.oldEnd = cmds.playbackOptions(q=True, max=True)
                
            start = self.start
            end = self.end
            if combine:
                start = min(start, cmds.playbackOptions(q=True, ast=True))
                end = max(end, cmds.playbackOptions(q=True, aet=True))
            cmds.playbackOptions(e=True, min=start, ast=start, max=end, aet=end)
            
            if goTo == AnimPreset.goToStart:
                cmds.currentTime(start, e=True)
                
            elif goTo == AnimPreset.goToEnd:
                cmds.currentTime(end, e=True)
                
            elif goTo == AnimPreset.goToClamp:
                currentTime = cmds.currentTime(q=True)
                clampedTime = min(max(start, currentTime), end)
                if clampedTime != currentTime:
                    cmds.currentTime(clampedTime, e=True)
                    
            elif goTo == AnimPreset.goToRelative:
                currentTime = cmds.currentTime(q=True)
                f = (currentTime - AnimPreset.oldStart) / (AnimPreset.oldEnd - AnimPreset.oldStart)
                relativeTime = int(start + f * (end - start))
                if relativeTime != currentTime:
                    cmds.currentTime(relativeTime, e=True)

    def applyAnimLayers(self, selectLastLayer=True, combine=False, applyWeights=True):
        with UndoContext("Apply AnimPreset AnimLayers"):
            baseLayer = cmds.animLayer(q=True, root=True)
            if baseLayer != None:
                weightedLayers = self.getWeightedLayers()
                activeAnimLayers = {}
                for weightedLayer in weightedLayers:
                    activeAnimLayers[weightedLayer.animLayer] = weightedLayer
                
                animLayers = self.getHolder().getAnimLayers()
                for animLayer in animLayers:
                    active = animLayer in activeAnimLayers
                    if not combine or cmds.animLayer(animLayer, q=True, m=True):
                        cmds.animLayer(animLayer, e=True, m=not active, l=not active)
                    
                    if applyWeights and self.shouldUseAnimLayerWeight(animLayer):
                        weightPlug = "{}.weight".format(animLayer)
                        isWeightAnimated = cmds.keyframe(weightPlug, q=True, keyframeCount=True) > 0
                        if active:
                            if isWeightAnimated:
                                cmds.error("Unable to change AnimLayer's weight: The layer's weight is animated.")
                            else:
                                cmds.setAttr(weightPlug, activeAnimLayers[animLayer].weight)
                        elif not isWeightAnimated:
                            cmds.setAttr(weightPlug, 1)
                
                if selectLastLayer:
                    sortedAnimLayers = AnimLayerUtils.sortAnimLayers(activeAnimLayers.keys())
                    if len(sortedAnimLayers) == 0:
                        sortedAnimLayers = [AnimLayerUtils.getBaseLayer()]
                    AnimLayerUtils.setSelectedAnimLayers([sortedAnimLayers[-1]])

    def export(self, pathTokenizer=None, force=False, exportMirror=True, checkout=True, convert=True, compile=True, prepareSubHolderForExport=True, restoreAfterExport=True, subHolderExportData=None):
        with UndoOff():
            if not self.enabled and not force:
                return []
            
            if pathTokenizer == None:
                pathTokenizer = self.getPathTokenizer()
            
            if restoreAfterExport:
                currentAnimRange = (cmds.playbackOptions(q=True, ast=True), cmds.playbackOptions(q=True, aet=True), cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
                animLayers = cmds.ls(type="animLayer")
                currentAnimLayers = [animLayer for animLayer in animLayers if not cmds.animLayer(animLayer, q=True, m=True)]
            
            self.applyAnimRange()
            self.applyAnimLayers(selectLastLayer=False)
            
            rangeEnd = self.end if not self.pose else self.start + 1
            path = pathTokenizer.Translate(self.path)
            animName = self.getConcatenatedName()
            
            if not animName:
                raise AssertionError("Unable to export AnimPReset: Invalid name! -> [{}]".format(animName))
            if self.start >= rangeEnd:
                raise AssertionError("Unable to export AnimPreset: Invalid range! -> [{}, {}]".format(self.start, rangeEnd))
            if not self.start.is_integer() or not rangeEnd.is_integer():
                raise AssertionError("Unable to export AnimPreset: Range is not an Integer number!")
            
            exportSubHolder = self.getSubHolder()
            if prepareSubHolderForExport:
                subHolderExportData = exportSubHolder.onPreExport()
            
            try:
                result = []
                result += Exporter.exportAnimation(exportSubHolder.getExportNodes(subHolderExportData), animName.format(left="left", right="right"), path, self.start, rangeEnd, self.loop, fileType=exportSubHolder.getExportFileType(), checkout=checkout, convert=convert, compile=False)   # In case we have to mirror, we postpone the compiling
                
                if exportMirror and self.mirror:
                    with AutoUndo():
                        mirrorData = exportSubHolder.mirrorAnimation(subHolderExportData)
                        result += Exporter.exportAnimation(exportSubHolder.getExportNodes(mirrorData), animName.format(left="right", right="left"), path, self.start, rangeEnd, self.loop, fileType=exportSubHolder.getExportFileType(), checkout=checkout, convert=convert, compile=False)
            
            finally:
                if prepareSubHolderForExport:
                    exportSubHolder.onPostExport(subHolderExportData)
            
            if compile:
                Exporter.compileAssetFiles(result)
            
            if restoreAfterExport:
                cmds.playbackOptions(e=True, ast=currentAnimRange[0], aet=currentAnimRange[1], min=currentAnimRange[2], max=currentAnimRange[3])
                for animLayer in animLayers:
                    cmds.animLayer(animLayer, e=True, m=(animLayer not in currentAnimLayers))
            
            return result
        
    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = self.getSubHolder().getPathTokenizer(branch=branch)
        return pathTokenizer
