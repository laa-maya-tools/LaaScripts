from PySide2 import QtWidgets

import maya.cmds as cmds
import maya.mel as mel

import os

from MayaImprovements import MayaImprovement

from TimeSlider import TimeSliderOverlay, TimeSliderFilter, FilterTransformKeys, AnimLayerFilter
from TimeSlider.ColorizeKeyframeByChannel import *

import AnimSystems.KeyingGroup as KeyingGroup

import ProjectPath

class CustomTimeSliderManager(MayaImprovement):

    initialized = False

    # Constants
    timeSliderMenuOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\TimeSliderMenu.mel")
    channelBoxMenuOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\generateChannelMenu.mel")

    timeSliderOverlayOptionVar = "timeSliderOverlayEnabled"
    timeSliderFiltersOptionVar = "timeSliderFiltersEnabled"
    
    # Variables
    timeSliderOverlay = None
    timeSliderFilterManager = None

    # Colorize Keys
    timeSliderOverlay_displayKeyColorsOptionVar = "timeSliderOverlay_displayKeyColorsEnabled"
    timeSliderOverlay_displayBlendKeysOptionVar = "timeSliderOverlay_displayBlendKeysEnabled"
    timeSliderOverlay_displayTransformKeysOptionVar = "timeSliderOverlay_displayTransformKeysEnabled"
    timeSliderOverlay_displayTransformCoordinatesOptionVar = "timeSliderOverlay_displayTransformCoordinatesEnabled"
    timeSliderOverlay_displayOtherKeysOptionVar = "timeSliderOverlay_displayOtherKeysEnabled"

    timeSliderOverlay_keyframePainter = ColorizeKeyframeByChannel()
    timeSliderOverlay_blendKeyColorizer = IKFKBlendColorFilter()
    timeSliderOverlay_positionKeyColorizer = AttributeColorFilter(["translate", "translateX", "translateY", "translateZ"], QtGui.QColor(128, 0, 0), 100, coordinateColors=[None, "modernGraphEditorTranslateXColor", "modernGraphEditorTranslateYColor", "modernGraphEditorTranslateZColor"])
    timeSliderOverlay_rotationKeyColorizer = AttributeColorFilter(["rotate", "rotateX", "rotateY", "rotateZ"], QtGui.QColor(0, 128, 0), 101, coordinateColors=[None, "modernGraphEditorRotateXColor", "modernGraphEditorRotateYColor", "modernGraphEditorRotateZColor"])
    timeSliderOverlay_scaleKeyColorizer = AttributeColorFilter(["scale", "scaleX", "scaleY", "scaleZ"], QtGui.QColor(0, 0, 128), 102, coordinateColors=[None, "modernGraphEditorScaleXColor", "modernGraphEditorScaleYColor", "modernGraphEditorScaleZColor"])
    timeSliderOverlay_defaultKeyColorizer = DefaultColorFilter()

    # Time Slider Filters
    timeSliderFilters_hideUnlayeredAttributesOptionVar = "timeSliderFilters_hideUnlayeredAttributesEnabled"
    timeSliderFilters_filterByTransformToolOptionVar = "timeSliderFilters_filterByTransformToolEnabled"
    timeSliderFilters_showOnlyTransformOptionVar = "timeSliderFilters_showOnlyTransformEnabled"

    timeSliderFilters_hideUnlayeredAttributesFilter = None
    timeSliderFilters_transformToolFilter = None
    timeSliderFilters_showOnlyTransformFilter = None
    
    # UI
    timeSliderOverlayButton = None

    timeSliderOverlay_displayKeyColorsButton = None
    timeSliderOverlay_displayBlendKeysButton = None
    timeSliderOverlay_displayTransformKeysButton = None
    timeSliderOverlay_displayOtherKeysButton = None


    timeSliderFiltersButton = None

    timeSliderFilters_filterByTransformToolButton = None

    @classmethod
    def isTimeSliderOverlayEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlayOptionVar):
            default = True  # True by default
            cls.setTimeSliderOverlayEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlayOptionVar)

    @classmethod
    def setTimeSliderOverlayEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlayOptionVar, enabled))
            
        cls.timeSliderOverlay.setVisible(enabled)
            
    @classmethod
    def isDisplayKeyframeColorsEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isTimeSliderOverlayEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlay_displayKeyColorsOptionVar):
            default = True  # True by default
            cls.setDisplayKeyframeColorsEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlay_displayKeyColorsOptionVar)

    @classmethod
    def setDisplayKeyframeColorsEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlay_displayKeyColorsOptionVar, enabled))

        cls.timeSliderOverlay_keyframePainter.enabled = enabled

        cls.timeSliderOverlay_keyframePainter.setDirty(update=True)

    @classmethod
    def isDisplayBlendKeysEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isDisplayKeyframeColorsEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlay_displayBlendKeysOptionVar):
            default = True  # True by default
            cls.setDisplayBlendKeysEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlay_displayBlendKeysOptionVar)
        
    @classmethod
    def setDisplayBlendKeysEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlay_displayBlendKeysOptionVar, enabled))

        cls.timeSliderOverlay_blendKeyColorizer.enabled = enabled
        
        cls.timeSliderOverlay_keyframePainter.setDirty(update=True)

    @classmethod
    def isDisplayTransformKeysEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isDisplayKeyframeColorsEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlay_displayTransformKeysOptionVar):
            default = True  # True by default
            cls.setDisplayTransformKeysEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlay_displayTransformKeysOptionVar)

    @classmethod
    def setDisplayTransformKeysEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlay_displayTransformKeysOptionVar, enabled))

        cls.timeSliderOverlay_positionKeyColorizer.enabled = enabled
        cls.timeSliderOverlay_rotationKeyColorizer.enabled = enabled
        cls.timeSliderOverlay_scaleKeyColorizer.enabled = enabled
        
        cls.timeSliderOverlay_keyframePainter.setDirty(update=True)

    @classmethod
    def isDisplayTransformCoordinatesEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isDisplayTransformKeysEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlay_displayTransformCoordinatesOptionVar):
            default = False  # False by default
            cls.setDisplayTransformCoordinatesEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlay_displayTransformCoordinatesOptionVar)

    @classmethod
    def setDisplayTransformCoordinatesEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlay_displayTransformCoordinatesOptionVar, enabled))

        cls.timeSliderOverlay_positionKeyColorizer.enableCoordinateColors = enabled
        cls.timeSliderOverlay_rotationKeyColorizer.enableCoordinateColors = enabled
        cls.timeSliderOverlay_scaleKeyColorizer.enableCoordinateColors = enabled
        
        cls.timeSliderOverlay_keyframePainter.setDirty(update=True)

    @classmethod
    def isDisplayOtherKeysEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isDisplayKeyframeColorsEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderOverlay_displayOtherKeysOptionVar):
            default = True  # False by default
            cls.setDisplayOtherKeysEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderOverlay_displayOtherKeysOptionVar)

    @classmethod
    def setDisplayOtherKeysEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderOverlay_displayOtherKeysOptionVar, enabled))

        cls.timeSliderOverlay_defaultKeyColorizer.enabled = enabled
        
        cls.timeSliderOverlay_keyframePainter.setDirty(update=True)

    @classmethod
    def isTimeSliderFiltersEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderFiltersOptionVar):
            default = True  # True by default
            cls.setTimeSliderFiltersEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderFiltersOptionVar)

    @classmethod
    def setTimeSliderFiltersEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderFiltersOptionVar, enabled))
        
        if enabled:
            cls.timeSliderFilterManager.initialize()
        else:
            cls.timeSliderFilterManager.uninitialize()

    @classmethod
    def isHideUnlayeredAttributesEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isTimeSliderFiltersEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderFilters_hideUnlayeredAttributesOptionVar):
            default = True  # True by default
            cls.setHideUnlayeredAttributesEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderFilters_hideUnlayeredAttributesOptionVar)

    @classmethod
    def setHideUnlayeredAttributesEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderFilters_hideUnlayeredAttributesOptionVar, enabled))

        cls.timeSliderFilters_hideUnlayeredAttributesFilter.setEnabled(enabled)

    @classmethod
    def isFilterByTransformToolEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isTimeSliderFiltersEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderFilters_filterByTransformToolOptionVar):
            default = False  # False by default
            cls.setFilterByTransformToolEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderFilters_filterByTransformToolOptionVar)

    @classmethod
    def setFilterByTransformToolEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderFilters_filterByTransformToolOptionVar, enabled))

        cls.timeSliderFilters_transformToolFilter.setEnabled(enabled)

    @classmethod
    def isShowOnlyTransformEnabled(cls, checkParentOption=True):
        if checkParentOption and not cls.isTimeSliderFiltersEnabled():
            return False
        
        if not cmds.optionVar(exists=cls.timeSliderFilters_showOnlyTransformOptionVar):
            default = False  # False by default
            cls.setShowOnlyTransformEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.timeSliderFilters_showOnlyTransformOptionVar)

    @classmethod
    def setShowOnlyTransformEnabled(cls, enabled, setVar=True):
        if setVar:
            cmds.optionVar(iv=(cls.timeSliderFilters_showOnlyTransformOptionVar, enabled))

        cls.timeSliderFilters_showOnlyTransformFilter.setEnabled(enabled)

    @classmethod
    def getTimeSliderContentsLayout(cls):
        timeSliderWidget = TimeSliderOverlay.TimeSliderOverlay.getTimeSliderWidget()
        timeSliderContentsWidget = timeSliderWidget.children()[0]

        if timeSliderContentsWidget.layout() != None:
            return timeSliderContentsWidget.layout()
        else:
            timeSliderContentsLayout = QtWidgets.QStackedLayout()
            timeSliderContentsLayout.setStackingMode(QtWidgets.QStackedLayout.StackAll)
            timeSliderContentsLayout.setContentsMargins(0, 0, 0, 0)
            timeSliderContentsWidget.setLayout(timeSliderContentsLayout)
            return timeSliderContentsLayout

    @classmethod
    def overrideTimeSliderMenu(cls):
        timeSliderMenuScriptPath = "\"" + cls.timeSliderMenuOverrideScript + "\";"
        timeSliderMenuScriptPath = timeSliderMenuScriptPath.replace("\\", "/")
        mel.eval("source " + timeSliderMenuScriptPath)

    @classmethod
    def overrideChannelBoxMenu(cls):
        channelBoxMenuScriptPath = "\"" + cls.channelBoxMenuOverrideScript + "\";"
        channelBoxMenuScriptPath = channelBoxMenuScriptPath.replace("\\", "/")
        mel.eval("source " + channelBoxMenuScriptPath)

    @classmethod
    def initialize(cls):
        cls.initialized = True

        cls.overrideTimeSliderMenu()
        cls.overrideChannelBoxMenu()
        
        cls.timeSliderOverlay = TimeSliderOverlay.TimeSliderOverlay()
        cls.timeSliderOverlay.setVisible(False)    # The widget needs to be hidden before or else it won't be painted
        cls.getTimeSliderContentsLayout().addWidget(cls.timeSliderOverlay)

        cls.timeSliderOverlay.registerTimeSliderPainter(KeyingGroup.KeyingGroupManager.timeSliderPainter)

        cls.timeSliderOverlay.registerTimeSliderPainter(cls.timeSliderOverlay_keyframePainter)
        cls.timeSliderOverlay_keyframePainter.registerColorFilter(cls.timeSliderOverlay_blendKeyColorizer)
        cls.timeSliderOverlay_keyframePainter.registerColorFilter(cls.timeSliderOverlay_positionKeyColorizer)
        cls.timeSliderOverlay_keyframePainter.registerColorFilter(cls.timeSliderOverlay_rotationKeyColorizer)
        cls.timeSliderOverlay_keyframePainter.registerColorFilter(cls.timeSliderOverlay_scaleKeyColorizer)
        cls.timeSliderOverlay_keyframePainter.registerColorFilter(cls.timeSliderOverlay_defaultKeyColorizer)

        cls.timeSliderFilterManager = TimeSliderFilter.TimeSliderFilterManager(cls.timeSliderOverlay)
        cls.timeSliderFilters_hideUnlayeredAttributesFilter = AnimLayerFilter.HideUnlayeredAttributesFilter(cls.timeSliderFilterManager)
        cls.timeSliderFilters_transformToolFilter = FilterTransformKeys.FilterTransformKeys(cls.timeSliderFilterManager)
        cls.timeSliderFilters_showOnlyTransformFilter = FilterTransformKeys.ShowOnlyTransformKeys(cls.timeSliderFilterManager)
        cls.timeSliderFilterManager.registerTimeSliderFilter(cls.timeSliderFilters_hideUnlayeredAttributesFilter)
        cls.timeSliderFilterManager.registerTimeSliderFilter(cls.timeSliderFilters_transformToolFilter)
        cls.timeSliderFilterManager.registerTimeSliderFilter(cls.timeSliderFilters_showOnlyTransformFilter)
        
        # NOTE: The KeyingGroup timeSliderPainter dosesn't need to load any optionVars, it manages itself
        
        cls.setTimeSliderOverlayEnabled(cls.isTimeSliderOverlayEnabled(), setVar=False)

        cls.setDisplayKeyframeColorsEnabled(cls.isDisplayKeyframeColorsEnabled(checkParentOption=False), setVar=False)
        cls.setDisplayBlendKeysEnabled(cls.isDisplayBlendKeysEnabled(checkParentOption=False), setVar=False)
        cls.setDisplayTransformKeysEnabled(cls.isDisplayTransformKeysEnabled(checkParentOption=False), setVar=False)
        cls.setDisplayTransformCoordinatesEnabled(cls.isDisplayTransformCoordinatesEnabled(checkParentOption=False), setVar=False)
        cls.setDisplayOtherKeysEnabled(cls.isDisplayOtherKeysEnabled(checkParentOption=False), setVar=False)


        cls.setTimeSliderFiltersEnabled(cls.isTimeSliderFiltersEnabled(), setVar=False)
        
        cls.setHideUnlayeredAttributesEnabled(cls.isHideUnlayeredAttributesEnabled(checkParentOption=False), setVar=False)
        cls.setFilterByTransformToolEnabled(cls.isFilterByTransformToolEnabled(checkParentOption=False), setVar=False)
        cls.setShowOnlyTransformEnabled(cls.isShowOnlyTransformEnabled(checkParentOption=False), setVar=False)

    @classmethod
    def uninitialize(cls):
        cls.setHideUnlayeredAttributesEnabled(False, setVar=False)
        cls.setTimeSliderOverlayEnabled(False, setVar=False)
        cls.setTimeSliderFiltersEnabled(False, setVar=False)

        cls.getTimeSliderContentsLayout().removeWidget(cls.timeSliderOverlay)
        cls.timeSliderOverlay.clearTimeSliderPainters()
        cls.timeSliderOverlay = None

        cls.timeSliderFilterManager.uninitialize()
        cls.timeSliderFilterManager.clearTimeSliderFilters()
        cls.timeSliderFilterManager = None

        cls.initialized = True