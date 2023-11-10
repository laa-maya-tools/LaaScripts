# coding: utf8

#-----------------------
#|    CONFIGURE ENV    |
#-----------------------
# Configures the environment variables, adding them to the Maya.env file.
# This file has a list of variables that should be added if they where not already on the file.
# Additional values can be added to an already existing variable, keeping the previous value as well.

import os
import sys
import logging
import traceback

import maya.cmds as cmds

# Definition for a variable configuration.
# The ADD attribute indicates if the value should be concantenated to the current one (it will replace it otherwise)
class EnvVarConfig():

    def __init__(self, var, value, add=True, addToSysPath=False):
        self.var = var
        self.value = value
        self.add = add
        self.addToSysPath = addToSysPath
                        
    def configureVariable(self, lines):
        varFound = False
        varModified = False

        for i in range(len(lines)):
            split = lines[i].split("=")
            if self.var == split[0]:
                varFound = True
                if self.add:
                    if not self.value in split[1]:
                        self.value += ";" + split[1]
                        lines[i] = self.var + "=" + self.value
                        varModified = True
                else:
                    if self.value != split[1]:
                        lines[i] = self.var + "=" + self.value
                        varModified = True

        if not varFound:
            # Variable not in list, adds it
            lines.append(self.var + "=" + self.value)
            varModified = True

        if self.addToSysPath:
            path = os.path.expandvars(self.value)
            if path not in sys.path:
                sys.path.append(path)

        if varModified:
            logging.warning("Environment variable [{0}] has been modified. Please restart Maya to apply changes.".format(self.var))

        return varModified

def processEnvironmentVariableConfigurations(configurations):
    envFilePath = os.path.join(cmds.internalVar(userAppDir=True), cmds.about(version=True), "Maya.env")

    # Opens the ENV file and get it's lines
    try:
        file = open(envFilePath, "r")
        lines = file.readlines()
    except:
        traceback.print_exc()
        return
    finally:
        file.close()

    # Removes the end of line characters at the end of each line
    for i in range(len(lines)):
        while lines[i].endswith("\r") or lines[i].endswith("\n"):
            lines[i] = lines[i][:-1]

    # Applies the configuration to the readed lines
    varModified = False
    for config in configurations:
        varModified |= config.configureVariable(lines)
    if varModified:
        cmds.confirmDialog(title="Configure Environment", message="Environment variables have been modified, please restart Maya to apply changes.")

    # Re-adds the end of line characters
    for i in range(len(lines)):
            lines[i] += "\n"

    # Saves the ENV file with the modified data
    try:
        file = open(envFilePath, "w")
        file.writelines(lines)
    except:
        traceback.print_exc()
        return
    finally:
        file.close()

def setEnvironmentVariable(variable, value, add=True):
    processEnvironmentVariableConfigurations([EnvVarConfig(variable, value, add=add)])

version = cmds.about(version=True)

# List of variable configurations
envVarConfigs = [
    # MSE Environment Variables
    EnvVarConfig("CODE_FOLDER", "GAME/Tools/MayaTools", add=False),                                   # Relative path to the code folder  # TODO: Actualizar si se cambia la ubicación del código de Maya
    EnvVarConfig("PYTHONPATH", "$P4_ROOT_FOLDER/$CODE_FOLDER/internal", add=True, addToSysPath=True), # Python module load folder, set to the absolute path to the internal and external tool folders
    EnvVarConfig("PYTHONPATH", "$P4_ROOT_FOLDER/$CODE_FOLDER/external", add=True, addToSysPath=True),
    EnvVarConfig("MAYA_MODULE_PATH", "$P4_ROOT_FOLDER/$CODE_FOLDER/external", add=True),              # Maya module load folder, set to the absolute path to the external tools folder (the module path is like the Python path, but it also loads plugins and module files)
    EnvVarConfig("MAYA_PLUG_IN_PATH", "$P4_ROOT_FOLDER/$CODE_FOLDER/plugins", add=True),              # Maya plugin load folder, set to the absolute path to our plugin folder
    EnvVarConfig("XBMLANGPATH", "$P4_ROOT_FOLDER/$CODE_FOLDER/icons", add=True),                      # Maya folder to look for icons, set to the absolute path to out icons folder (these icons are for Maya, Qt applications should have their own way to handle icons)
    EnvVarConfig("MAYA_NO_WARNING_FOR_MISSING_DEFAULT_RENDERER", "1", add=False),                     # Disables a warning when starting Maya when the default renderer is disabled
    EnvVarConfig("PYTHONDONTWRITEBYTECODE", "1", add=False),                                          # Prevents Python from creating cache files when executing that may be uploaded to perforce by mistake
    EnvVarConfig("MAYA_ENABLE_LEGACY_VIEWPORT", "1", add=False),                                      # Enables back the Legacy Viewport (the user may choose which renderer to use). Certain features are not available on Viewport 2.0

    # Nintendo Environment Variables
    EnvVarConfig("NINTENDO_MAYA_ROOT", "$NINTENDO_SDK_ROOT/Tools/Graphics/MayaPlugins", add=False),
    EnvVarConfig("NINTENDO_MAYA_APP_ROOT", "$MAYA_LOCATION", add=False),
    EnvVarConfig("NW4F_MAYA_ROOT", "$NINTENDO_MAYA_ROOT", add=False),
    EnvVarConfig("NW4F_MAYA_PLUGIN_ROOT", "$NINTENDO_MAYA_ROOT", add=False),
    EnvVarConfig("MAYA_SCRIPT_PATH", "$NINTENDO_MAYA_ROOT/Scripts", add=True, addToSysPath=True),
    EnvVarConfig("MAYA_PLUG_IN_PATH", "$NINTENDO_MAYA_ROOT/Plugins", add=True),
    EnvVarConfig("MAYA_PLUG_IN_PATH", "$NINTENDO_MAYA_ROOT/Plugins-{version}".format(version=version), add=True),
    EnvVarConfig("XBMLANGPATH", "$NINTENDO_MAYA_ROOT/icons", add=True),
    EnvVarConfig("MAYA_DET_TANGENT", "1", add=False),
]

def init():
    processEnvironmentVariableConfigurations(envVarConfigs)