# coding: utf-8

import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

import TimeSlider

class TimeSliderFilter(object):

    def __init__(self, manager):
        self.manager = manager
        
        self._enabled = True
        
    def isEnabled(self):
        return self.manager._initialized and self._enabled

    def setEnabled(self, enabled):
        self._enabled = enabled
        
        self.manager.updateTimeSliderSelectionListAndOverlay()
        
    def onUpdateSelectionList(self, enabled):
        pass

    def shouldNodeAttributeBeVisible(self, node, attribute):
        return True

    def onRegister(self):
        pass

    def onUnregister(self):
        pass


class TimeSliderFilterManager(object):

    def __init__(self, timeSliderOverlay=None):
        self.timeSliderOverlay = timeSliderOverlay

        self._initialized = False

        self.timeSliderFilters = []

        self.filteredTimeSliderSelectionList = None

    def initialize(self):
        if not self._initialized:
            self._initialized = True

            self.filteredTimeSliderSelectionList = cmds.selectionConnection()
            cmds.timeControl(TimeSlider.defaultTimeSlider, e=True, mainListConnection=self.filteredTimeSliderSelectionList)
            
            self.registerCallbacks()

            self.updateTimeSliderSelectionListAndOverlay()

    def uninitialize(self):
        if self._initialized:
            self._initialized = False
            
            cmds.timeControl(TimeSlider.defaultTimeSlider, e=True, mainListConnection="animationList")
            self.updateTimeSliderSelectionListAndOverlay()
            
            self.unregisterCallbacks()
            
    def registerCallbacks(self):
        self.selectionChangedCallback = cmds.scriptJob(e=("SelectionChanged", self.updateTimeSliderSelectionList))  # The SelectionChanged callback doesn't seem to work properly on the API
        self.timelineSyncChangedCallback = cmds.scriptJob(ovc=("timeSliderShowKeys", self.updateTimeSliderSelectionList))
        self.animLayerDisplayOptionsChangedCallback = cmds.scriptJob(ovc=("timeSliderAnimLayerOptions", self.updateTimeSliderSelectionList))
        
        self.animationLayerRefreshCallback = OpenMaya.MEventMessage.addEventCallback("animLayerRefresh", self.updateTimeSliderSelectionListAndOverlay)
        self.postToolChangedCallback = OpenMaya.MEventMessage.addEventCallback("PostToolChanged", self.updateTimeSliderSelectionListAndOverlay)
        self.channelBoxLabelSelectedCallback = OpenMaya.MEventMessage.addEventCallback("ChannelBoxLabelSelected", self.onChannelBoxLabelSelected)
        
    def unregisterCallbacks(self):
        cmds.scriptJob(kill=self.selectionChangedCallback)
        cmds.scriptJob(kill=self.timelineSyncChangedCallback)
        cmds.scriptJob(kill=self.animLayerDisplayOptionsChangedCallback)

        OpenMaya.MMessage.removeCallback(self.animationLayerRefreshCallback)
        OpenMaya.MMessage.removeCallback(self.postToolChangedCallback)
        OpenMaya.MMessage.removeCallback(self.channelBoxLabelSelectedCallback)
        
    def registerTimeSliderFilter(self, timeSliderFilter):
        if timeSliderFilter in self.timeSliderFilters:
            raise AssertionError("TimeSliderFilter already registered! {}".format(timeSliderFilter))

        self.timeSliderFilters.append(timeSliderFilter)
        timeSliderFilter.onRegister()
        
        self.updateTimeSliderSelectionListAndOverlay()

    def unregisterTimeSliderFilter(self, timeSliderFilter):
        if timeSliderFilter not in self.timeSliderFilters:
            raise AssertionError("TimeSliderFilter not registered yet! {}".format(timeSliderFilter))

        self.timeSliderFilters.remove(timeSliderFilter)
        timeSliderFilter.onUnregister()
        
        self.updateTimeSliderSelectionListAndOverlay()
    
    def clearTimeSliderFilters(self):
        while len(self.timeSliderFilters) > 0:
            self.unregisterTimeSliderFilter(self.timeSliderFilters[-1])
        
    def updateFilters(self, enabled):
        for timeSliderFilter in self.timeSliderFilters:
            timeSliderFilter.onUpdateSelectionList(enabled)

    def updateTimeSliderSelectionList(self, *args): # The *args parameter is used to take unused user data sent by some callbacks
        if cmds.isTrue("opening"):
            return
        
        channelBox = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, showKeys=True)
        if cmds.channelBox(channelBox, q=True, exists=True):
            selectedChannels = cmds.channelBox(channelBox, q=True, selectedMainAttributes=True) or []
            hasChannelsSelected = len(selectedChannels) > 0
            if hasChannelsSelected:
                # Channels are returned as short names, we need the long names
                selectedObject = cmds.channelBox(channelBox, q=True, mainObjectList=True)[0]
                selectedChannels = [cmds.listAttr("{}.{}".format(selectedObject, channel))[0] for channel in selectedChannels]
        else:
            hasChannelsSelected = False
        
        self.updateFilters(not hasChannelsSelected)
        
        if self._initialized and cmds.selectMode(q=True, o=True):
            cmds.selectionConnection(self.filteredTimeSliderSelectionList, e=True, clear=True)
            selectedNodes = cmds.ls(selection=True) or []
            for node in selectedNodes:
                nodeAttributes = cmds.listAttr(node, keyable=True, multi=True) or []
                for attribute in nodeAttributes:
                    if hasChannelsSelected: # When there are channels selected, we don't want to apply any filters
                        shouldBeVisible = attribute in selectedChannels
                    else:
                        shouldBeVisible = True
                        for timeSliderFilter in self.timeSliderFilters:
                            if timeSliderFilter.isEnabled() and not timeSliderFilter.shouldNodeAttributeBeVisible(node, attribute):
                                shouldBeVisible = False
                                break
                    if shouldBeVisible:
                        plug = "{}.{}".format(node, attribute)
                        while plug != None and cmds.addAttr(plug, q=True, exists=True) and cmds.addAttr(plug, q=True, usedAsProxy=True):
                            plug = cmds.listConnections(plug, s=True, d=False, plugs=True) or []
                            plug = plug[0] if len(plug) > 0 else None
                        if plug != None:
                            cmds.selectionConnection(self.filteredTimeSliderSelectionList, e=True, select=plug)
                        
            cmds.timeControl(TimeSlider.defaultTimeSlider, e=True, mainListConnection=self.filteredTimeSliderSelectionList) # Even if the selection list is already set, we need to set it again so Maya realizes it has changed
        
    def updateTimeSliderSelectionListAndOverlay(self, *args):
        self.updateTimeSliderSelectionList()

        if self.timeSliderOverlay != None:
            self.timeSliderOverlay.onSelectionChanged()
            self.timeSliderOverlay.update()
            
    def onChannelBoxLabelSelected(self, *args):
        # Normally changing the channel will change the current tool, prompting another callback.
        # But when deselecting all channels, the tool won't change, so we need to manually update the selectionList in this case.
        selectedChannels = cmds.channelBox("mainChannelBox", q=True, selectedMainAttributes=True) or []
        if len(selectedChannels) == 0:
            self.updateTimeSliderSelectionList()
