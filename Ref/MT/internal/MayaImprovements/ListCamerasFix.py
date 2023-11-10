from MayaImprovements import MayaImprovement

import maya.mel as mel

import ProjectPath

import os

class ListCamerasFix(MayaImprovement):

    # Constants
    procedureOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\updateModelPanelBar.mel")
    
    @classmethod
    def overrideProcedure(cls):
        deleteScriptPath = "\"" + cls.procedureOverrideScript + "\";"
        deleteScriptPath = deleteScriptPath.replace("\\", "/")
        mel.eval("source " + deleteScriptPath)

    @classmethod
    def initialize(cls):
        cls.overrideProcedure()

    @classmethod
    def uninitialize(cls):
        pass
