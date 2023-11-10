import maya.cmds as cmds

import AutoUpdate.UpdateTools as UpdateTools
import AutoUpdate.UpdateOpenedFiles as UpdateOpenedFiles
import AutoUpdate.UpdateFileReferences as UpdateFileReferences
import AutoUpdate.UpdateCreatedReferences as UpdateCreatedReferences
import AutoUpdate.UpdateImportedFiles as UpdateImportedFiles

AUTO_UPDATE_ENABLED_OPTIONVAR = "AUTO_UPDATE_ENABLED"

def isAutoUpdateEnabled():
    if not cmds.optionVar(ex=AUTO_UPDATE_ENABLED_OPTIONVAR):
        cmds.optionVar(iv=(AUTO_UPDATE_ENABLED_OPTIONVAR, True))    # Enabled by default
    return cmds.optionVar(q=AUTO_UPDATE_ENABLED_OPTIONVAR)

def setAutoUpdateEnabled(enabled):
    if isAutoUpdateEnabled() != enabled:
        cmds.optionVar(iv=(AUTO_UPDATE_ENABLED_OPTIONVAR, enabled))
        if enabled:
            initialize()
        else:
            uninitialize()
    
def initialize():
    UpdateOpenedFiles.UpdateOpenedFiles.initialize()
    UpdateFileReferences.UpdateFileReferences.initialize()
    UpdateCreatedReferences.UpdateCreatedReferences.initialize()
    UpdateImportedFiles.UpdateImportedFiles.initialize()
    
def uninitialize():
    UpdateOpenedFiles.UpdateOpenedFiles.uninitialize()
    UpdateFileReferences.UpdateFileReferences.uninitialize()
    UpdateCreatedReferences.UpdateCreatedReferences.uninitialize()
    UpdateImportedFiles.UpdateImportedFiles.uninitialize()

def init():
    if isAutoUpdateEnabled():
        UpdateTools.UpdateTools.updateTools(mayRequireRestart=False)
        
        initialize()
        
        cmds.evalDeferred(postInit)

def postInit():
    result = UpdateOpenedFiles.UpdateOpenedFiles.onPreSceneOpened(None, None, onStartup=True)
    if result:
        cmds.evalDeferred(UpdateFileReferences.UpdateFileReferences.onSceneOpened)
