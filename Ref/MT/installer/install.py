#-----------------------
#|      INSTALLER      |
#-----------------------
# Installs the minimum functionality to initialize the tools for Maya:
# * Sets up an environment variable specifying the path to the project on Perforce
# * Copies the mseLoad module to the user's local module folder. This module is used to load all the functionality when Maya starts.


# IMPORTS
import os
import subprocess

import maya.cmds as cmds

from distutils.dir_util import mkpath
from distutils.file_util import copy_file
from distutils.dir_util import copy_tree

from stat import S_IWUSR, S_IREAD   # This constants are used to set file permissions

# CONSTANTS
CURRENT_PROJECT = "PRJ_05"  # TODO: Actualizar al cambiar de proyecto

MAYA_DIRECTORY = cmds.internalVar(userAppDir=True)
MAYA_VERSION = cmds.about(version=True)

P4_ROOT_FOLDER_VAR = "P4_ROOT_FOLDER"

INITIALIZER_MODULE_FILE = "mseLoad.mod"
INITIALIZER_MODULE_FOLDER = "mseLoad"
INITIALIZER_LOADER_FILE = "scripts/userSetup.py"

MAYA_ENV_FILE = "Maya.env"
MAYA_ENV_FILE_BACKUP = "Maya.env_backup"

END_LINE = "\r\n"

# FUNCTIONS

def getLines(envPath):
    with open(envPath) as file:
        lines = file.readlines()
    return lines

def formatLines(lines):
    lines = [line.replace(" ", "") for line in lines]
    lines = [line.replace("\n", "") for line in lines]
    lines = [line.replace("\r", "") for line in lines]
    lines = [line + "\n" for line in lines]
    return lines

def getLineIndexById(id, lines):
    for i, line in enumerate(lines):
        split = line.split("=")
        if split[0].lower() == id.lower():
            return i
    return None

def getMayaEnvFile():
    return os.path.join(MAYA_DIRECTORY, MAYA_VERSION, MAYA_ENV_FILE)

def configureMayaEnvFile(p4RootPath=None):
    envPath = getMayaEnvFile()
    if not os.path.exists(envPath):
        with open(envPath, "w") as file:
            file.write("")

    # Backs Up the file
    backupFile = os.path.join(MAYA_DIRECTORY, MAYA_VERSION, MAYA_ENV_FILE_BACKUP)
    copy_file(envPath, backupFile)

    lines = getLines(envPath)
    newLines = formatLines(lines)

    if not p4RootPath:
        # Asks for the Perforce root path
        perforceGetPathProcess = subprocess.Popen("p4 -F %clientRoot% -ztag info", shell=True, stdout=subprocess.PIPE)
        perforceBasePath = perforceGetPathProcess.stdout.read().decode("ascii").replace(END_LINE, "")
        perforcePath = os.path.normpath(os.path.join(perforceBasePath, CURRENT_PROJECT))
        p4RootPath = cmds.fileDialog2(ds=1, fm=3, cap="Select Project Folder (just before Game and 3D)", dir=perforcePath)
        while p4RootPath == None:
            cmds.confirmDialog(title="Select Project Folder", message="You must select a valid Project Folder.\nPlease select the folder just before the Game and 3D folders.")
            p4RootPath = cmds.fileDialog2(ds=1, fm=3, cap="Select Project Folder (just before Game and 3D)", dir=perforcePath)
        p4RootPath = p4RootPath[0]

    # Registers the Perforce root path
    lineId = getLineIndexById(P4_ROOT_FOLDER_VAR, newLines)
    if lineId == None:
        newLines.insert(0, P4_ROOT_FOLDER_VAR + "=" + p4RootPath + "\n")
    else:
        newLines[lineId] = P4_ROOT_FOLDER_VAR + "=" + p4RootPath + "\n"
    os.environ[P4_ROOT_FOLDER_VAR] = p4RootPath

    with open(envPath, "w") as file:
        file.writelines(newLines)

def changeFolderPermissionsRecursive(path, mode):
    subItems = os.listdir(path)
    for item in subItems:
        subPath = os.path.join(path, item)
        if os.path.isfile(subPath):
            os.chmod(subPath, mode)
        else:
            changeFolderPermissionsRecursive(subPath, mode)

# MAIN

def install(fileDirectory, p4RootPath=None):
    initializerModuleFile = os.path.normpath(os.path.join(fileDirectory, INITIALIZER_MODULE_FILE))
    initializerModuleFolder = os.path.normpath(os.path.join(fileDirectory, INITIALIZER_MODULE_FOLDER))
    
    mayaModulesFolder = os.path.normpath(os.path.join(MAYA_DIRECTORY, MAYA_VERSION, "modules"))
    if not os.path.exists(mayaModulesFolder):
        mkpath(mayaModulesFolder)

    destinationInitializerModuleFile = os.path.normpath(os.path.join(mayaModulesFolder, INITIALIZER_MODULE_FILE))
    destinationInitializerModuleFolder = os.path.normpath(os.path.join(mayaModulesFolder, INITIALIZER_MODULE_FOLDER))

    copy_file(initializerModuleFile, destinationInitializerModuleFile)
    copy_tree(initializerModuleFolder, destinationInitializerModuleFolder)

    # This makes the files read/write (needed since the files come from Perforce and are likely marked as Read Only)
    os.chmod(destinationInitializerModuleFile, S_IWUSR|S_IREAD) 
    changeFolderPermissionsRecursive(destinationInitializerModuleFolder, S_IWUSR|S_IREAD)

    configureMayaEnvFile(p4RootPath=p4RootPath)

    # Runs the loader file to configure Maya for the first time
    if not cmds.about(batch=True):  # No need to do this if running the script without Maya actually opened
        userSetupScriptFile = os.path.normpath(os.path.join(destinationInitializerModuleFolder, INITIALIZER_LOADER_FILE))
        with open(userSetupScriptFile) as file:
            exec(file.read())

    # Global preferences (30FPS):
    cmds.optionVar(stringValue=("workingUnitTimeDefault", "ntsc"))
    # Set Grid Size (1m front, 1m back, 1m left & 1m Right) in divisions of 10 cms
    cmds.optionVar(fv=("gridSize", 100))
    cmds.optionVar(fv=("gridSpacing", 10))
    cmds.optionVar(fv=("gridDivisions", 1))
    
    # When every other process has finished, ends the installation.
    # Execute Deferred is used since other processes might have also been executed deferredly.
    cmds.evalDeferred(endInstallation, lp=True)

def endInstallation():
    cmds.confirmDialog(message="Installation successfull. Please restart Maya to complete the installation.")

def onMayaDroppedPythonFile(*args, **kwargs):
    fileDirectory = os.path.dirname(__file__)
    install(fileDirectory)