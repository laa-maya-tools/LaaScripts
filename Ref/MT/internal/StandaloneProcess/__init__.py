import subprocess
import sys
import os

EXECUTABLES_FOLDER  = "ExecutableScripts"
MAYAPY_EXECUTABLE   = "mayapy"

def ExecuteMayaPyProcess(scriptName, params=[]):
    # Get Executable Script path
    currentDir = os.path.dirname(__file__)
    scriptFile = os.path.join(currentDir, EXECUTABLES_FOLDER, scriptName)
    
    # Get MayaPy Execution path
    mayapyFolder    = os.path.split(sys.executable)[0]
    
    # Prepare Execution parameters
    execParams = [MAYAPY_EXECUTABLE]
    execParams += [scriptFile]
    execParams += params
    
    # This flags are for preventing the cmd window from showing
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    # Execute process
    process = subprocess.Popen(execParams, cwd=mayapyFolder, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(execParams)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise RuntimeError(process.returncode, stderr)


def CreateAnimFile(rigFile, nameSpace="", animFile=""):
    """Intented for creating an "_anim" file based on a previously existing "_rig" file.
    As for the file structure in "Alter", the anim file would be created a folcer above the "rig"
    folder, where the "_rig" file should exist.
    
    Args:
        rigFile (string): rig file full path
        nameSpace (string): namespace for the referenced actor
        animFile (str, optional): _description_. Defaults to "".
        
    Raises:
        e: RunTimeError
        
    Returns:
        string: Full path for the Anim file
    """
    
    executableScriptName = "CreateAnimFile.py"
    
    # If no nameSpace is specified, get it from rigFile
    if (not nameSpace):
        rigFileSplit = os.path.split(rigFile)
        rigFileName = rigFileSplit[1].split(".")[0]
        nameSpace = rigFileName.lower().replace("_rig","")
    
    # If not animFile is specified, then the default behavior is:
    if (not animFile):
        rigFileSplit = os.path.split(rigFile)
        animFilePath = os.path.join(rigFileSplit[0], "..")
        animFileName = rigFileSplit[1].lower().replace("_rig", "_anim")
        animFile = os.path.join(animFilePath, animFileName)
    animFile = os.path.normpath(animFile)
    
    try:
        ExecuteMayaPyProcess(executableScriptName, [rigFile, nameSpace, animFile])
    except RuntimeError as e:
        raise e
    else:
        return animFile