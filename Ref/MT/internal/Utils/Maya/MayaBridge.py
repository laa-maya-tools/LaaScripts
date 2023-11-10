import maya.cmds as cmds

# --------------------------------------------------
# Nodes and selection operations--------------------
#---------------------------------------------------
def selectNodes(nodesList):
    cmds.select(nodesList)

def typeOf(node):
    return cmds.objectType(node)

def getCurrentSelection():
    return cmds.ls(selection=True)

def getSelectedDAGNodes():
    return cmds.ls(selection=True, type="dagNode")

def getSceneNodesByType(type):
    # Maya me da un asco que flipas con esta mierda
    if (type == "mesh"):
        return cmds.listRelatives(cmds.ls(type=type, noIntermediate=True), type='transform', p=True, pa=True)
    else:
        return cmds.ls(type=type, noIntermediate=True) 

def getHierarchy(rootNode, typesList=[], asTree=True, path=True, recursive=True):
    children = []
    
    # the command "listRelatives" returns also sub-types. For example: Constraints are
    # sub-types of transform. With that in mind, we must re-filter the result
    if (not asTree):
        hier = cmds.listRelatives(rootNode, type=typesList, allDescendents=recursive, path=path) or []
        return [x for x in hier if (cmds.objectType(x) in typesList)]
    else:
        hier = cmds.listRelatives(rootNode, type=typesList, path=path) or []
        relatives = [x for x in hier if (cmds.objectType(x) in typesList)]
    
        if (relatives):
            children = relatives
            if (recursive):
                for i in range(len(children)):
                    children[i] = getHierarchy(children[i], typesList=typesList)
    
        return [rootNode, children]

def getReadOnlyNodes(nodesList):
    cmds.ls(nodesList, ro=True)

def GetParentNode(node):
    result = cmds.listRelatives(node, parent=True)
    if result:
        return result[0]
    else:
        return None

def GetShapeNodes(node):
    return cmds.listRelatives(node, shapes=True, path=True) or []

def getTypeConnections(nodeName, type):
    return cmds.listConnections(nodeName, t=type) or []

def getDagNodeShapes(node):
        return cmds.listRelatives(node, shapes=True, path=True)

def extractPathName(value):
    path = None
    name = value
    idx = value.rfind("|")
    if (idx>-1):
        name = value[idx+1:]
        path = value[:idx+1]
    
    return path, name

# --------------------------------------------------
# Text Format Printing -----------------------------
#---------------------------------------------------
def printWarning(text):
    cmds.warning(text)

def printError(text):
    cmds.error(text)


# --------------------------------------------------
# File Info ----------------------------------------
#---------------------------------------------------
def GetCurrentFilePath():
    return cmds.file(q=True, sn=True)


# --------------------------------------------------
# Script Jobs --------------------------------------
#---------------------------------------------------
# https://download.autodesk.com/us/maya/2009help/CommandsPython/scriptJob.html#flagnodeNameChanged
def CreateScriptJob(e=None, nnc=None):
    if (e):
        return cmds.scriptJob(e=e)
    elif (nnc):
        return cmds.scriptJob(nnc=nnc)

#son el mismo este y el de arriba 
def KillScriptJob(jobNum, force=False):
    if (cmds.scriptJob(exists=jobNum)):
        cmds.scriptJob( kill=jobNum, force=force)


# --------------------------------------------------
# Evaluation ---------------------------------------
#---------------------------------------------------
def EvalDeferred(method):
    cmds.evalDeferred(method)

# --------------------------------------------------
# Plugin Loading -----------------------------------
#---------------------------------------------------
def isPluginLoaded(pluginName):
    return cmds.pluginInfo(pluginName, q=True, loaded=True)

def loadPlugin(pluginName, pythonPlugin=True):
    extension = "py"
    if not pythonPlugin:
        extension = "mll"
    
    cmds.loadPlugin("{}.{}".format(pluginName, extension))

# --------------------------------------------------
# Internal Info ------------------------------------
#---------------------------------------------------
def GetInternalVar(userPrefDir=False):
    result = cmds.internalVar(userPrefDir=userPrefDir)
    return result