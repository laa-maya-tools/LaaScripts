import maya.cmds as cmds

import TimeSlider.TimeSliderFilter as TimeSliderFilter

import Utils.Maya.AnimLayers as AnimLayerUtils


class HideUnlayeredAttributesFilter(TimeSliderFilter.TimeSliderFilter):
    
    def __init__(self, manager):
        TimeSliderFilter.TimeSliderFilter.__init__(self, manager)

        self.shouldFilter = False
        self.baseLayer = None

    def onUpdateSelectionList(self, enabled):
        self.shouldFilter = False
        self.baseLayer = AnimLayerUtils.getBaseLayer()
        
        if enabled and self.isEnabled():
            if cmds.optionVar(q="animLayerSelectionKey") == 2:
                selectedLayers = AnimLayerUtils.getSelectedAnimLayers()
                if selectedLayers and self.baseLayer not in selectedLayers:
                    self.shouldFilter = True
    
    def shouldNodeAttributeBeVisible(self, node, attribute):
        if self.shouldFilter:
            affectedLayers = AnimLayerUtils.getAffectedLayersForAttribute("{}.{}".format(node, attribute))
            if not affectedLayers or affectedLayers == [self.baseLayer]:
                return False
                
        return True
