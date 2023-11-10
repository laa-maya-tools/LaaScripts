import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaAnim as OpenMayaAnim

from PySide2 import QtWidgets, QtCore, QtGui

from MayaImprovements import MayaImprovement

import Utils.Maya.AnimLayers as  AnimLayerUtils
from Utils.Maya.OptionVar import OptionVarConfiguration
from Utils.Python.Versions import long
import TimeSlider

import shiboken2
import collections

class CustomChannelBoxDelegate(QtWidgets.QItemDelegate):
    
    def __init__(self, baseDelegate):
        super().__init__()
        
        self.baseDelegate = baseDelegate
        
        baseDelegate.setParent(self)
        baseDelegate.commitData.connect(self.commitData)
        
        self.cacheAttributes()
        
    def getChannelBoxAttributes(self, obj):
        attrs = cmds.listAttr(obj, k=True) or []
        attrs += cmds.listAttr(obj, cb=True) or []
        
        attrs = ["{}.{}".format(obj, attr) for attr in attrs if "." not in attr]
        attrs = [attr for attr in attrs if not cmds.addAttr(attr, q=True, ex=True) or not cmds.addAttr(attr, q=True, hidden=True)]
        
        return attrs
        
    def cacheAttributes(self):
        self.mainObjectAttributes = {}
        self.shapesAttributes = collections.OrderedDict()
        self.inputAttributes = collections.OrderedDict()
        self.outputAttributes = collections.OrderedDict()
        
        mainObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, mainObjectList=True) or []
        if mainObjects:
            mainObject = mainObjects[0]
            attrs = self.getChannelBoxAttributes(mainObject)
            niceNameDict = {}
            for attr in attrs:
                niceNameDict[cmds.attributeName(attr, nice=True)] = attr
            self.mainObjectAttributes[mainObject] = niceNameDict
            
        shapeObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, shapes=True) or []
        for shapeObject in shapeObjects:
            attrs = self.getChannelBoxAttributes(shapeObject)
            niceNameDict = {}
            for attr in attrs:
                niceNameDict[cmds.attributeName(attr, nice=True)] = attr
            self.shapesAttributes[shapeObject] = niceNameDict
            
        inputObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, inputs=True) or []
        unfoldedInputObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, historyObjectList=True) or []
        for inputObject in inputObjects:
            attrs = self.getChannelBoxAttributes(inputObject)
            niceNameDict = {}
            if inputObject in unfoldedInputObjects:
                for attr in attrs:
                    niceNameDict[cmds.attributeName(attr, nice=True)] = attr
            self.inputAttributes[inputObject] = niceNameDict
             
        outputObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, outputs=True) or []
        unfoldedOutputObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, outputObjectList=True) or []
        for outputObject in outputObjects:
            attrs = self.getChannelBoxAttributes(outputObject)
            niceNameDict = {}
            if outputObject in unfoldedOutputObjects:
                for attr in attrs:
                    niceNameDict[cmds.attributeName(attr, nice=True)] = attr
            self.outputAttributes[outputObject] = niceNameDict
        
    def getAttributeFromIndex(self, index):
        niceName = index.siblingAtColumn(0).data()
        
        if self.mainObjectAttributes:
            row = index.row()
            if row == 0:
                return None
            row -= 1
            
            for obj, niceNameDict in self.mainObjectAttributes.items():
                if row < len(niceNameDict):
                    if niceName not in niceNameDict:
                        return None
                    return niceNameDict[niceName]
                row -= len(niceNameDict)
        
        if self.shapesAttributes:
            if row == 0:
                return None
            row -= 1
            
            unfoldedShapeObjects = cmds.channelBox(TimeSlider.mainChannelBox, q=True, shapeObjectList=True) or []
            for obj, niceNameDict in self.shapesAttributes.items():
                if row == 0:
                    return None
                row -= 1
                
                if obj in unfoldedShapeObjects:
                    if row < len(niceNameDict):
                        if niceName not in niceNameDict:
                            return None
                        return niceNameDict[niceName]
                    row -= len(niceNameDict)
        
        if self.inputAttributes:
            if row == 0:
                return None
            row -= 1
            
            for obj, niceNameDict in self.inputAttributes.items():
                if row == 0:
                    return None
                row -= 1
                
                if row < len(niceNameDict):
                    if niceName not in niceNameDict:
                        return None
                    return niceNameDict[niceName]
                row -= len(niceNameDict)
        
        if self.outputAttributes:
            if row == 0:
                return None
            row -= 1
            
            for obj, niceNameDict in self.outputAttributes.items():
                if row == 0:
                    return None
                row -= 1
                
                if row < len(niceNameDict):
                    if niceName not in niceNameDict:
                        return None
                    return niceNameDict[niceName]
                row -= len(niceNameDict)
            
        return None
    
    def paint(self, painter, styleOptions, index):
        self.baseDelegate.paint(painter, styleOptions, index)
        
        if index.column() == 1:
            if AnimLayerUtils.getBaseLayer() != None:
                attribute = self.getAttributeFromIndex(index)
                if attribute and cmds.objExists(attribute) and cmds.getAttr(attribute, k=True):
                    color = None
                    borderColor = None
                    bestLayer = AnimLayerUtils.getBestAnimLayerForPlug(attribute)
                    if bestLayer == None:
                        if ChannelBoxFix.isMarkNonAnimatableEnabled():
                            color = QtGui.QColor.fromHsv(0, 0, 0)
                    else:
                        affectedLayers = AnimLayerUtils.getAffectedLayersForAttribute(attribute)
                        if affectedLayers:
                            if ChannelBoxFix.isMarkNonOnSelectedLayerEnabled():
                                selectedLayers = AnimLayerUtils.getSelectedAnimLayers()
                                if bestLayer not in selectedLayers:
                                        color = QtGui.QColor.fromRgb(0, 0, 255)
                            
                            if ChannelBoxFix.isPaintAnimatedOnLayerEnabled():
                                if cmds.keyframe(attribute, q=True, keyframeCount=True) > 0:
                                    ct = cmds.currentTime(q=True)
                                    if cmds.keyframe(attribute, q=True, time=(ct, ct)):
                                        borderColor = QtGui.QColor.fromRgb(205, 39, 41)
                                    else:
                                        borderColor = QtGui.QColor.fromRgb(221, 114, 122)
                      
                    rect = QtCore.QRect(styleOptions.rect)
                    rect.setWidth(7)
                    painter.save()
                    if color:
                        painter.fillRect(rect, color)
                    if borderColor:
                        painter.setPen(borderColor)
                        painter.setBrush(borderColor)
                        painter.drawPolygon([rect.bottomLeft(), rect.topRight(), rect.bottomRight()])
                    painter.restore()
    
    def createEditor(self, *args, **kwargs):
        return self.baseDelegate.createEditor(*args, **kwargs)
    
    def setEditorData(self, *args, **kwargs):
        return self.baseDelegate.setEditorData(*args, **kwargs)

    def setModelData(self, *args, **kwargs):
        return self.baseDelegate.setModelData(*args, **kwargs)


class ChannelBoxFix(MayaImprovement):
    
    initialized = False
    
    # Option Vars
    MARK_NON_ANIMATABLE_OPTIONVAR = OptionVarConfiguration("Mark Non Animatable", "CHANNELBOX_MARK_NON_ANIMATABLE_OPTIONVAR", OptionVarConfiguration.TYPE_INTEGER, True)
    MARK_NON_ON_SELECTED_LAYER_OPTIONVAR = OptionVarConfiguration("Mark Non On Selected Layer", "CHANNELBOX_MARK_NON_ON_SELECTED_LAYER_OPTIONVAR_OPTIONVAR", OptionVarConfiguration.TYPE_INTEGER, True)
    PAINT_ANIMATED_ON_LAYER_OPTIONVAR = OptionVarConfiguration("Paint Animated On Layer", "CHANNELBOX_PAINT_ANIMATED_ON_LAYER_OPTIONVAR_OPTIONVAR", OptionVarConfiguration.TYPE_INTEGER, True)
    
    # Delegate
    defaultChannelBoxDelegate = None
    customChannelBoxDelegate = None
    
    # Callbacks
    scriptJobs = []
    apiCallbacks = []
    
    @classmethod
    def isMarkNonAnimatableEnabled(cls):
        return cls.initialized and cls.MARK_NON_ANIMATABLE_OPTIONVAR.value

    @classmethod
    def setMarkNonAnimatableEnabled(cls, enabled):
        cls.MARK_NON_ANIMATABLE_OPTIONVAR.value = enabled
        
        cls.refreshChannelBox()

    @classmethod
    def isMarkNonOnSelectedLayerEnabled(cls):
        return cls.initialized and cls.MARK_NON_ON_SELECTED_LAYER_OPTIONVAR.value

    @classmethod
    def setMarkNonOnSelectedLayerEnabled(cls, enabled):
        cls.MARK_NON_ON_SELECTED_LAYER_OPTIONVAR.value = enabled
        
        cls.refreshChannelBox()

    @classmethod
    def isPaintAnimatedOnLayerEnabled(cls):
        return cls.initialized and cls.PAINT_ANIMATED_ON_LAYER_OPTIONVAR.value

    @classmethod
    def setPaintAnimatedOnLayerEnabled(cls, enabled):
        cls.PAINT_ANIMATED_ON_LAYER_OPTIONVAR.value = enabled
        
        cls.refreshChannelBox()
        
    @classmethod
    def refreshChannelBox(cls, *args):
        channelBoxTableView = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl(TimeSlider.mainChannelBox)), QtWidgets.QTableView)
        channelBoxTableView.viewport().update()
    
    @classmethod
    def onSelectionChanged(cls):
        cls.customChannelBoxDelegate.cacheAttributes()
        
        cls.refreshChannelBox()
    
    @classmethod
    def registerChannelBoxDelegate(cls):
        channelBoxTableView = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl(TimeSlider.mainChannelBox)), QtWidgets.QTableView)
        
        if cls.defaultChannelBoxDelegate == None:
            cls.defaultChannelBoxDelegate = channelBoxTableView.itemDelegate()
        
        if cls.customChannelBoxDelegate == None:
            cls.customChannelBoxDelegate = CustomChannelBoxDelegate(cls.defaultChannelBoxDelegate)
        
        channelBoxTableView.setItemDelegate(cls.customChannelBoxDelegate)
    
    @classmethod
    def unregisterChannelBoxDelegate(cls):
        channelBoxTableView = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl(TimeSlider.mainChannelBox)), QtWidgets.QTableView)
        
        channelBoxTableView.setItemDelegate(cls.defaultChannelBoxDelegate)
        
    @classmethod
    def registerCallbacks(cls):
        cls.scriptJobs = []
        cls.scriptJobs.append(cmds.scriptJob(e=("SelectionChanged", cls.onSelectionChanged)))
        cls.scriptJobs.append(cmds.scriptJob(e=("NameChanged", cls.onSelectionChanged)))
        cls.scriptJobs.append(cmds.scriptJob(e=("animLayerRefresh", cls.refreshChannelBox)))
        
        cls.apiCallbacks = []
        cls.apiCallbacks.append(OpenMayaAnim.MAnimMessage.addAnimKeyframeEditedCallback(cls.refreshChannelBox))
    
    @classmethod
    def unregisterCallbacks(cls):
        for callback in cls.scriptJobs:
            cmds.scriptJob(k=callback)
        cls.scriptJobs = []
        
        for callback in cls.apiCallbacks:
            OpenMaya.MMessage.removeCallback(callback)
        cls.apiCallbacks = []
    
    @classmethod
    def initialize(cls):
        cls.initialized = True
        
        cls.registerChannelBoxDelegate()
        
        cls.registerCallbacks()
        
    @classmethod
    def uninitialize(cls):
        cls.initialized = False
        
        cls.unregisterCallbacks()
        
        cls.unregisterChannelBoxDelegate()
