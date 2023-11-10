import maya.cmds as cmds

import TimeSlider
import TimeSlider.TimeSliderFilter as TimeSliderFilter

import Utils.Maya.ToolContext as ToolContextUtils


from AnimSystems.IKManipulator import IKManipulatorController, FKManipulatorController

translateAttributes = ["translateX", "translateY", "translateZ"]
rotateAttributes = ["rotateX", "rotateY", "rotateZ"]
scaleAttributes = ["scaleX", "scaleY", "scaleZ"]
ikFkBlendAttributes = ["arm_blend", "leg_blend"]

transformAttributes = translateAttributes + rotateAttributes + scaleAttributes

class FilterTransformKeys(TimeSliderFilter.TimeSliderFilter):

    colorizedAttributes = transformAttributes + ikFkBlendAttributes
    
    translateBackgroundColor = (0.5, 0.0, 0.0)
    rotateBackgroundColor = (0.0, 0.5, 0.0)
    scaleBackgroundColor = (0.0, 0.0, 0.5)
    defaultBackgroundColor = (68.0 / 255.0, 68.0 / 255.0, 68.0 / 255.0)

    def __init__(self, manager):
        TimeSliderFilter.TimeSliderFilter.__init__(self, manager)

        self.attrFilter = []

    def onUpdateSelectionList(self, enabled):
        self.attrFilter = []
        attrColor = {}
        
        if enabled and self.isEnabled():
            currentContext = ToolContextUtils.currentContextManipulator()

            if currentContext == "manipMove" or currentContext == IKManipulatorController.CONTEXT_CLASS:
                self.attrFilter += translateAttributes
                for attr in translateAttributes:
                    attrColor[attr] = self.translateBackgroundColor
                
            elif currentContext == "manipRotate" or currentContext == FKManipulatorController.CONTEXT_CLASS:
                self.attrFilter += rotateAttributes
                for attr in rotateAttributes:
                    attrColor[attr] = self.rotateBackgroundColor

            elif currentContext == "manipScale":
                self.attrFilter += scaleAttributes
                for attr in scaleAttributes:
                    attrColor[attr] = self.scaleBackgroundColor
            
            # Special case: If rotating FK controls like they were IK (or viceversa), we need to display the IK/FK Blend keyframes as well.
            # The IK/FK Blend keys are used since they should be shared for each controls and won't be used by non-chain controls.
            # We trust these keyframes are syncrhonized.
            if currentContext == IKManipulatorController.CONTEXT_CLASS:
                self.attrFilter += ikFkBlendAttributes
                for attr in ikFkBlendAttributes:
                    attrColor[attr] = self.translateBackgroundColor
            elif currentContext == FKManipulatorController.CONTEXT_CLASS:
                self.attrFilter += ikFkBlendAttributes 
                for attr in ikFkBlendAttributes:
                    attrColor[attr] = self.rotateBackgroundColor
        
        for attr in self.colorizedAttributes:
            if attr in self.attrFilter:
                cmds.channelBox(TimeSlider.mainChannelBox, e=True, attrRegex=attr, attrBgColor=attrColor[attr])
            else:
                cmds.channelBox(TimeSlider.mainChannelBox, e=True, attrRegex=attr, attrBgColor=self.defaultBackgroundColor)

    def shouldNodeAttributeBeVisible(self, node, attribute):
        if self.attrFilter:
            return attribute in self.attrFilter

        return True

    def onUnregister(self):
        for attr in self.colorizedAttributes:
            cmds.channelBox(TimeSlider.mainChannelBox, e=True, attrRegex=attr, attrBgColor=self.defaultBackgroundColor)
            

class ShowOnlyTransformKeys(TimeSliderFilter.TimeSliderFilter):
    
    def shouldNodeAttributeBeVisible(self, node, attribute):
            return attribute in transformAttributes
