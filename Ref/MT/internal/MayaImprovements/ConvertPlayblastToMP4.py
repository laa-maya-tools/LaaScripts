# encoding: utf-8

import maya.cmds as cmds
import maya.mel as mel

import os

from MayaImprovements import MayaImprovement
import ProjectPath

class ConvertPlayblastToMP4(MayaImprovement):

    initialized = False

    # Constants
    performPlayblastProcedureOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\performPlayblast.mel")
    convertPlayblastToMP4OptionVar = "convertPlayblastToMP4Enabled"

    @classmethod
    def isConvertPlayblastToMP4Enabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.convertPlayblastToMP4OptionVar):
            default = True  # Enabled by default
            cls.setConvertPlayblastToMP4Enabled(default)
            return default
        
        return cmds.optionVar(q=cls.convertPlayblastToMP4OptionVar)

    @classmethod
    def setConvertPlayblastToMP4Enabled(cls, enabled):
        cmds.optionVar(iv=(cls.convertPlayblastToMP4OptionVar, enabled))

    @classmethod
    def overridePerformPlayblastProcedure(cls):
        overridePath = "\"" + cls.performPlayblastProcedureOverrideScript + "\";"
        overridePath = overridePath.replace("\\", "/")
        mel.eval("source " + overridePath)
        mel.eval("source " + overridePath)  # Por alguna razón hay que ejecutarlo dos veces :D

    @classmethod
    def initialize(cls):
        cls.initialized = True

        cls.overridePerformPlayblastProcedure()

    @classmethod
    def uninitialize(cls):
        cls.initialized = False

