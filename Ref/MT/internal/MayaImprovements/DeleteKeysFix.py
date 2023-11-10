import maya.cmds as cmds
import maya.mel as mel

import os

from MayaImprovements import MayaImprovement
import ProjectPath

class DeleteKeysFix(MayaImprovement):

    initialized = False

    # Constants
    deleteProcedureOverrideScript = os.path.join(ProjectPath.getToolsFolder(), "MayaImprovements\\MelOverride\\doDelete.mel")
    deleteKeysFixOptionVar = "deleteKeysFixEnabled"

    @classmethod
    def isDeleteKeysFixEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.deleteKeysFixOptionVar):
            default = True  # True by default
            cls.setDeleteKeysFixEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.deleteKeysFixOptionVar)

    @classmethod
    def setDeleteKeysFixEnabled(cls, enabled):
        cmds.optionVar(iv=(cls.deleteKeysFixOptionVar, enabled))

    @classmethod
    def overrideDeleteProcedure(cls):
        deleteScriptPath = "\"" + cls.deleteProcedureOverrideScript + "\";"
        deleteScriptPath = deleteScriptPath.replace("\\", "/")
        mel.eval("source " + deleteScriptPath)

    @classmethod
    def initialize(cls):
        cls.initialized = True

        cls.overrideDeleteProcedure()

    @classmethod
    def uninitialize(cls):
        cls.initialized = False

