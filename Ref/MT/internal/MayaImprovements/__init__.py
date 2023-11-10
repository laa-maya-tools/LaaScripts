import maya.cmds as cmds

import CustomMenu
import ProjectPath

import os, traceback

class MayaImprovement(object):

    @classmethod
    def initialize(cls):
        pass

    @classmethod
    def uninitialize(cls):
        pass


import MayaImprovements.CustomTimeSlider as CustomTimeSlider
import MayaImprovements.CustomPlaybackRange as CustomPlaybackRange
import MayaImprovements.CustomUI as CustomUIManager
import MayaImprovements.DeleteKeysFix as DeleteKeysFix
import MayaImprovements.ListCamerasFix as ListCamerasFix
import MayaImprovements.OverwriteMovedKeys as OverwriteMovedKeys
import MayaImprovements.ConvertPlayblastToMP4 as ConvertPlayblastToMP4
import MayaImprovements.ClearFocusOnEnter as ClearFocusOnEnter
import MayaImprovements.AnimLayerFix as AnimLayerFix
import MayaImprovements.TimeSliderFix as TimeSliderFix
import MayaImprovements.HotkeyManagerFix as HotkeyManagerFix
import MayaImprovements.ChannelBoxFix as ChannelBoxFix

improvements = [
    CustomTimeSlider.CustomTimeSliderManager,
    CustomPlaybackRange.CustomPlaybackRangeManager,
    CustomUIManager.CustomUIManager,
    AnimLayerFix.AnimLayerFix,
    DeleteKeysFix.DeleteKeysFix,
    ListCamerasFix.ListCamerasFix,
    OverwriteMovedKeys.OverwriteMovedKeys,
    ConvertPlayblastToMP4.ConvertPlayblastToMP4,
    ClearFocusOnEnter.ClearFocusOnEnter,
    TimeSliderFix.TimeSliderFix,
    HotkeyManagerFix.HotkeyManagerFix,
    ChannelBoxFix.ChannelBoxFix
]

menuPath = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements", "Resources", "MayaImprovementsMenu.json")
buttonLayout = "RangeSlider|MainPlaybackRangeLayout|formLayout9|formLayout10"

configurationButton = None

def createConfigurationButton():
    global configurationButton
    configurationButton = cmds.iconTextButton("MayaImprovementsConfiguration", image1="hotkeySetSettings.png", width=25, height=25, annotation="Maya Improvements Configuration", parent=buttonLayout)
    cmds.formLayout(buttonLayout, edit=True, attachForm=[(configurationButton, "top", 0), (configurationButton, "right", 0)])
    
    CustomMenu.createPopUpMenuFromFile(menuPath, parent=configurationButton, button=1)

def deleteConfigurationButton():
    global configurationButton
    cmds.deleteUI(configurationButton)
    configurationButton = None

def initialize():
    problematicItems = []
    for item in improvements:
        try:
            item.initialize()
        except:
            problematicItems.append(item)
            traceback.print_exc()

    for problematicItem in problematicItems:
        improvements.remove(problematicItem)

    createConfigurationButton()

def uninitialize():
    for item in improvements:
        item.uninitialize()

    deleteConfigurationButton()
