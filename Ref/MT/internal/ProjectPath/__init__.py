import os

import maya.cmds as cmds

import ConfigureEnv

import collections

def browseProjectFolder(persistent=False):
    path = cmds.fileDialog2(ds=1, fm=3, cap="Select Project Folder (just before Game and 3D)", dir=getProjectFolder())
    if path != None and len(path) > 0:
        setProjectFolder(path[0], persistent=persistent)

def setProjectFolder(path, persistent=False):
    os.environ["P4_ROOT_FOLDER"] = path
    if persistent:
        ConfigureEnv.setEnvironmentVariable("P4_ROOT_FOLDER", path, add=False)

def getProjectFolder():
    return os.path.normpath(os.environ["P4_ROOT_FOLDER"])

def getGameFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "GAME"))

def getExportFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "GAME", "Assets"))

def getCutscenesFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "GAME", "Assets", "cutscenes"))

def getMSFrameworkFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "GAME", "Tools", "MSFramework"))

def get3DFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "3D"))

def getTempFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], "3D", "Assets", "temp"))

def getCodeFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"]))

def getToolsFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"], "internal"))

def getExternalFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"], "external"))

def getStartupFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"], "startup"))

def getIconsFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"], "icons"))

def getPluginsFolder():
    return os.path.normpath(os.path.join(os.environ["P4_ROOT_FOLDER"], os.environ["CODE_FOLDER"], "plugins"))




import json, inspect

class Tokens():
    T3D =                   "3D"
    T3DActors =             "3DActors"
    T3DCuts =               "3DCuts"
    TActorName =            "ActorName"
    TActors =               "Actors"
    TAnimations =           "Anims"
    TCutsceneName =         "CutName"
    TCutsceneNumber =       "CutNum"
    TShotName =             "ShotName"
    TCutscenes =            "Cutscenes"
    TGameActors =           "GameActors"
    TGameCuts =             "GameCuts"
    TBranch =               "Branch"
    TGame =                 "Game"
    TModels =               "Models"
    TPrjRoot =              "PrjRoot"
    TPrjBranch =            "PrjBranch"
    TPrj3D =                "Prj3D"
    TPrjGame =              "PrjGame"
    TSubActorName =         "SubActorName"
    TActorType =            "ActorType"
    TSubActorPath =         "SubActorPath"
    TSubActorExportPath =   "SubActorExportPath"
    TSubActorAnimPath =     "SubActorAnimPath"
    TSubActorModelPath =    "SubActorModelPath"
    
    @staticmethod
    def curled(token):
        return "{{{}}}".format(token)

# Depends on 'getProjectFolder()'
class PathTokenizer():
    # "Static" attributes, for reading configuration JSON only once in this session.
    __ConfigTokens = None
    __pathTokensJsonName = "pathTokens.json"
    
    def __init__(self, customDict={}, branch=None):
        # If "Static" variables are not initialized, initialize them from a Json
        # located in the same folder as THIS class definition file.
        if (PathTokenizer.__ConfigTokens == None):
            JSONdata = {}
            thisFilePath = os.path.dirname(inspect.getfile(self.__class__))
            with open(thisFilePath + "\\" + PathTokenizer.__pathTokensJsonName) as f:
                JSONdata = json.load(f)
            
            PathTokenizer.__ConfigTokens = JSONdata["Tokens"]
        
        self.__CompoundDict =   self.__ExtractCompDictionary(PathTokenizer.__ConfigTokens)
        self.__BaseDict =       self.__ExtractBasicDictionary(PathTokenizer.__ConfigTokens)
        
        customDict = customDict.copy()
        customDict[Tokens.TPrjRoot] = getProjectFolder()
        if branch:
            customDict[Tokens.TBranch] = branch
            
        self.Update(customDict)
    
    def __ExtractBasicDictionary(self, theDict):
        return collections.OrderedDict((k, v) for k,v in theDict.items() if (v==None or  (v!=None and v.find("{") == -1)))
    
    def __ExtractCompDictionary(self, theDict):
        return collections.OrderedDict((k, v) for k,v in theDict.items() if (v!=None and v.find("{") != -1))
    
    def __LowerCaseDictionary(self, theDic):
        result = collections.OrderedDict((k.lower(), v.lower() if (v!=None) else None) for k,v in theDic.items())
        return result
    
    # Returns a dictionary with all available Key:Values
    def GetFullDictionary(self):
        result = self.__BaseDict.copy()
        result.update(self.__CompoundDict)
        
        return result
    
    # Updates the Inner Dictionary with the new values from an incoming dictionary
    def Update(self, updateIn):
        interm = self.GetFullDictionary()
        
        for t in updateIn:
            if (updateIn[t] != None):
                interm[t] = "" if updateIn[t] == "" else os.path.normpath(updateIn[t]).lower()
                interm.move_to_end(t, last=False)
            else:
                interm[t] = None
        
        self.__BaseDict =       self.__ExtractBasicDictionary(interm)
        self.__CompoundDict =   self.__ExtractCompDictionary(interm)
    
    # Translates a tokenized string into a full readable string
    def Translate(self, theStr, caseSens=False):
        result = os.path.normcase(theStr)
        matchBaseDict =     self.__BaseDict
        matchCompoundDict = self.__CompoundDict
        
        if (not caseSens):
            result = result.lower()
            matchBaseDict =     self.__LowerCaseDictionary(self.__BaseDict)
            matchCompoundDict = self.__LowerCaseDictionary(self.__CompoundDict)
        
        recursiveDepth = 0
        while True:
            lastResult = result
            for t in matchCompoundDict:
                result = result.replace('{'+t+'}', matchCompoundDict[t])
            if lastResult == result:
                break
            recursiveDepth += 1
            if recursiveDepth >= 50:
                raise Exception("Max recursive depth reached! {}".format(result))
        
        for t in matchBaseDict:
            idx = result.find('{'+t+'}')
            if (idx != -1):
                if (matchBaseDict[t] != None):
                    result = result.replace('{'+t+'}', matchBaseDict[t])
                else:
                    raise Exception("Token found has no value: {}".format(t))
        
        return result
    
    def __ResolveCompoundDict(self, theStr, matchCompoundDict):
        result = theStr
        match = False
        
        for t in matchCompoundDict:
            if (matchCompoundDict[t] != None):
                if (not match and result.find(matchCompoundDict[t]) != -1):
                    match = True
                result = result.replace(matchCompoundDict[t], '{'+t+'}')
        
        if (match):
            result = self.__ResolveCompoundDict(result, matchCompoundDict)
        
        return result
    
    # Converts a full readable string into a tokenized string.
    def Tokenize(self, theStr, caseSens=False, verbose=False):
        result = os.path.normcase(theStr)
        matchBaseDict =     self.__BaseDict
        matchCompoundDict = self.__CompoundDict
        
        if (not caseSens):
            result = result.lower()
            matchBaseDict =     self.__LowerCaseDictionary(self.__BaseDict)
            matchCompoundDict = self.__LowerCaseDictionary(self.__CompoundDict)
        
        sortedByLengthList = list(matchBaseDict.items())
        sortedByLengthList.sort(key=lambda x : len(x[1]) if x[1] != None else 0, reverse=True)
        
        for token, value in sortedByLengthList:
            if (value != None):
                prev = 0
                i = result.find(value)
                while (i != -1):
                    allowTokenization = True
                    for j in range(i-1, prev-1, -1):
                        if (result[j] == os.path.sep or result[j] == "}"):
                            break
                        elif (result[j] == "{"):
                            allowTokenization = False
                            break
                        
                    if (allowTokenization):
                        result = result[:i] + "{" + token + "}" + result[i + len(value):]
                        prev = i + len(token) + 2 # The 2 is for the curly brackets
                    else:
                        prev = i + len(value)
                        
                    i = result.find(value, prev)
                    
            elif (verbose):
                print("**WARNING** Token has no value in dictionary, it will be omitted: {}".format(t))
        
        result = self.__ResolveCompoundDict(result, matchCompoundDict)
        
        return result

# # **************** Use Example: ****************
# # Initialize Tokenizer
# custDict = {Tokens.TActorName : "MiActor", Tokens.TSubActorName : "MiSubActor", Tokens.TType : "MiTipo"}
# tkzr = PathTokenizer(custDict)
#
# # Translate tokenized path to normal path
# TokenPth = "{GameActors}\{Type}\{ActName}\{ActName}_{SActName}.fbx"
# translatedPath = tkzr.Translate(TokenPth)
# print(translatedPath)
#
# # Translate normal path to tokenized path. It has a "Verbose" option (Default False)
# NormalPath = "C:\\perforcelocal\\[ws00]\\PRJ_05\\GAME\\Assets\\actors\\miTipo\\miActor\\miActor_miSubActor.fbx"
# tokenizedPath = tkzr.Tokenize(NormalPath)
# print(tokenizedPath)
#
# # Get the current key/values dictionary of this tokenizer
# tokensDictionary = tkzr.GetFullDictionary()
# print(tokensDictionary)
#
# # Update Specific keys of the dictionary. "Restricted" parameter is intented for
# # adding new custom values when passed as "False" (default True).
# newVals = {"Type": "Cacahuete", "ActName" : "otroActor"}
# tkzr.Update(newVals)

# -----------------------------------------------------------------------------
# ------------------------------- Branches ------------------------------------
# -----------------------------------------------------------------------------
'''
Class intented to be a "rule" asert for a directory to be a Branch.

Current rules:
    - The directory has to have a subdirectory named "Assets" (non case sensitive)
'''
class BranchRules():
    '''
    Main function for checking all the rules
    '''
    @staticmethod
    def DirMatchRules(dir):
        result = True
        
        if (not BranchRules.HasAssetsFolder(dir)):
            return False
        
        return result
    
    @staticmethod
    def HasAssetsFolder(dir):
        for it in os.scandir(dir):
            if (it.is_dir() and it.name.lower() == "assets"):
                return True
        return False

'''
Returns the subfolders that match the rules for being a branch. It can work recursively and
it has an option to return the full path or the trimmed path from the original folder.
'''
def GetBranches(dir, recursive=False, fullPath=True):
    result = []
    
    for it in os.scandir(dir):
        if (it.is_dir()):
            if (BranchRules.DirMatchRules(it)):
                result.append(it.path)
            if (recursive):
                result += GetBranches(it)
    
    if (not fullPath):
        for i in range(len(result)):
            result[i] = result[i].lstrip(dir)
    
    return result