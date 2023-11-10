import os, subprocess

def GetFurthestExistingFolder(path):
    if path != '':
        if (os.path.isdir(path)):
            return path
        else:
            return GetFurthestExistingFolder(os.path.split(path)[0])
    else:
        return None

def ShowFileExplorer(path):
    path = os.path.normpath(path)
    
    if ("." in path):
        if (os.path.isfile(path)):
            explorer = subprocess.Popen(['explorer', '/select,', path])
            return
        else:
            path = GetFurthestExistingFolder(os.path.split(path)[0])
    
    os.startfile(GetFurthestExistingFolder(path))