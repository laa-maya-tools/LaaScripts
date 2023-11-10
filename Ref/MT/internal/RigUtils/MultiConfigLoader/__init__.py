import os
import pymel.core as pm

import AnimSystems.KeyingGroup as KG
import OrganiLayers as OL

_DEFAULT_SUBFOLDER = "configFiles"

# This is the dictionary that tells wich files (mare accurately, wich partt of the name must containt a file)
# are going to be taken care of for import, and wich function is used for importing. Those functions should,
# preferrably, only get a path to the file that we want to import.
_CONFIGFILES_EXECUTION = {
    "KeyingGroups": KG.importKeyingGroupsFromFile,
    "OrganiLayers": OL.ImportOrganiLayersFromFile
}

def GetFolderFiles(folderPath, nameKey=""):
    if not(nameKey):
        return [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
    else:
        return [f for f in os.listdir(folderPath) if (os.path.isfile(os.path.join(folderPath, f)) and (nameKey.lower() in f.lower()))]

def ImportFileDefaultConfigs(folder=None):
    if not folder:
        folder = pm.system.sceneName().parent
        folder = os.path.join(folder, _DEFAULT_SUBFOLDER)
    
    totalImported = 0
    
    if (os.path.isdir(folder)):
        fileName = pm.system.sceneName().basename().splitext()[0]
        filenameClean = fileName.replace("_rig", "")

        # Get any file from every configuration
        for cfKey in _CONFIGFILES_EXECUTION.keys():
            cfMatches = GetFolderFiles(folder, nameKey=cfKey)
            cfMatchFile = None

            # If there's more than one match, try and find the one with the same file name
            if (cfMatches):
                if len(cfMatches) == 1:
                    cfMatchFile = cfMatches[0]
                else:
                    cfMatches = cfMatches = GetFolderFiles(folder, nameKey="{}_{}".format(cfKey, filenameClean))

                    # If there's still miltuple config files for the same type and file, warn about it
                    if (cfMatches):
                        if len(cfMatches) > 1:
                            pm.warning("There's multiple {} files for the file: {}".format(cfKey, fileName))
                        else:
                            cfMatchFile = cfMatches[0]
            
            if cfMatchFile:
                print("Importing '{}' config file: {}".format(cfKey, cfMatchFile))
                try:
                    _CONFIGFILES_EXECUTION[cfKey](os.path.join(folder, cfMatchFile))
                    totalImported += 1
                except Exception as e:
                    pm.error("ERROR importing '{}' config file: '{}'. {}".format(cfKey, cfMatchFile, e))
        
        print("Total imported configurations: {}".format(totalImported))
    else:
        print("Default Configurations Folder not found: {}".format(folder))