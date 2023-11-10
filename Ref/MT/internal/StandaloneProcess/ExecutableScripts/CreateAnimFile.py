import maya.cmds as cmds
import maya.standalone
import sys

# --------------------------------- Initialize Maya StandAlone --------------------------
# region ----------------------- And get access to internal tools -----------------------

# Initialize Maya StandAlone
maya.standalone.initialize("Python")

# Internal Imports
import ActorManager
import Utils.Maya.DefaultScenePreferences as DefaultScenePrefs

# Get the input arguments
rigFile     = sys.argv[1]
nameSpace   = sys.argv[2]
animFile    = sys.argv[3]
# endregion ----------------------------------------------------------------------------

# region - Do what we want: ------------------------------------------------------------
# Set the default prefs and create the reference
DefaultScenePrefs.SetDefaultScenePreferences()
ActorManager.createActorReference(rigFile, nameSpace)

# Save the File
cmds.file(rename=animFile)
cmds.file(save=True, de=False, type='mayaBinary')
# endregion ----------------------------------------------------------------------------