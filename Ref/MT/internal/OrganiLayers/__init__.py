import maya.cmds as cmds

import OrganiLayers.JSONUtils   as JSONUtils
import Utils.Maya.MayaBridge    as MayaBridge

from NodeManager.NodeWrapper    import NodeWrapper
from OrganiLayers.OrganiSet     import OrganiSetWrapper   as oSet
from OrganiLayers.OrganiItem    import OrganiItemWrapper  as oItem

# ------------------------------------
# - OrganiSets Handling
# -----------------------------------
# Create a new Set
def CreateSet(setName):
    result = oSet()
    result.create(setName)
    return result

# Get all Scene OrganiSets
def GetOrganiSets(wrapper=True):
    nodeList = cmds.ls(type="OrganiSet", ap=True)
    if wrapper:
        return oSet.getWrapperList(nodeList)
    else:
        return nodeList

# Get Current Active OrganiSet in Scene
def GetActiveOrganiSet(wrapper=True):
    nodeList = cmds.ls(type="OrganiSet", ap=True)
    for n in nodeList:
        nWrap = oSet(n)
        if (nWrap.isActive):
            if (wrapper):
                return nWrap
            else:
                return n
    return None

# ------------------------------------
# - OrganiItems Handling
# -----------------------------------
# Creates an OrganiItem, given the Maya Node and the parent OrganiLayer Wrapper
def CreateOrganiItem(dagNodeName, parentOrganiLayer):
        result = None
        result = oItem()
        result.create(dagNodeName)
        CopyDrawOverrideData(dagNodeName, result)
        result.dagNode = dagNodeName
        result.parentLayer = parentOrganiLayer
        return result

# Get possibly existing OrganiItems for the desired Maya Nodes in the desired Set
def GetOrganiItemsByNodes(set, arrayNodes):
    result = []
    for lyr in set.getComponentLayers():
        for itm in lyr.getChildrenItems():
            if (itm.dagNode.node in arrayNodes):
                result.append(itm)
                arrayNodes.remove(itm.dagNode.node)
    return result

# Adds the desired Maya Nodes to a layer (by full layer path) on a desired set. If any Maya node
# has already an OrganiItem on the set, this function uses that instead of creating a new one
def AddItemsToLayerByPath(dagNodeNames, layerPath, set):
    layer = GetOrCreateLayerByPath(set, layerPath)
    auxList = list(dagNodeNames)
    
    existingOrganiItems = GetOrganiItemsByNodes(set, auxList)
    for itm in existingOrganiItems:
        itm.parentLayer = layer
    
    newItems = []
    for n in auxList:
        item = CreateOrganiItem(n, layer)
        newItems.append(item)

# Copies a Node Draw Override Data to an OrganiItem Draw Info
def CopyDrawOverrideData(origin, organiItem):
    origNode = NodeWrapper(origin)
    shapes = MayaBridge.GetShapeNodes(origin)
    if (shapes):
        origNode = NodeWrapper(shapes[0])
    if (origNode.getAttr("overrideEnabled")):
        organiItem.displayType      = origNode.getAttr("overrideDisplayType")
        organiItem.levelOfDetail    = origNode.getAttr("overrideLevelOfDetail")
        organiItem.shading          = origNode.getAttr("overrideShading")
        organiItem.texturing        = origNode.getAttr("overrideTexturing")
        organiItem.playback         = origNode.getAttr("overridePlayback")
        organiItem.visibility       = origNode.getAttr("overrideVisibility")
        organiItem.hideOnPlayback   = origNode.getAttr("hideOnPlayback")
        organiItem.overrideRGBColors = origNode.getAttr("overrideRGBColors")
        organiItem.color            = origNode.getAttr("overrideColor")
        organiItem.overrideColorRGB = origNode.getAttr("overrideColorRGB")[0]

# ------------------------------------
# - OrganiLayers Handling
# -----------------------------------
# Get possibly existing OrganiLayer Wrapper, in the desired set, by layer path from root (with dots '.')
def GetLayerByPath(set, layerPath):
    layers = set.getComponentLayers()
    for layer in layers:
        if (layer.getLayerPath() == layerPath):
            return layer
    return None

# Gets existing layer from desired path or creates the neccesary layers on the fly
def GetOrCreateLayerByPath(set, layerPath):
    layerLevelsNames = layerPath.split(".")
    currentLevel = ""
    lastLayer = None
    
    for layerLevel in layerLevelsNames:
        currentLevel += layerLevel
        lyr = GetLayerByPath(set, currentLevel)
        if (lyr):
            lastLayer = lyr
        else:
            lastLayer = set.createLayer(layerLevel, lastLayer)
        currentLevel += "."
    
    return lastLayer

# ------------------------------------
# - Sets import/export Json Handling
# -----------------------------------
def LoadDrawInfo(inheritedObj, drawInfo):
    inheritedObj.displayType      = drawInfo["displayType"]
    inheritedObj.levelOfDetail    = drawInfo["levelOfDetail"]
    inheritedObj.shading          = drawInfo["shading"]
    inheritedObj.texturing        = drawInfo["texturing"]
    inheritedObj.playback         = drawInfo["playback"]
    inheritedObj.enabled          = drawInfo["enabled"]
    inheritedObj.visibility       = drawInfo["visibility"]
    inheritedObj.hideOnPlayback   = drawInfo["hideOnPlayback"]
    inheritedObj.overrideRGBColors= drawInfo["overrideRGBColors"]
    inheritedObj.color            = drawInfo["color"]
    inheritedObj.overrideColorRGB = drawInfo["overrideColorRGB"]

def RecreateLayerData(data, setWrapper):
    lyrName = data["name"]
    newLayer = setWrapper.createLayer(lyrName)
    
    for itm in data["childItems"]:
        itmNode = itm["dagNode"]
        try:
            organiItem = CreateOrganiItem(itmNode, newLayer)
            if ("drawInfo" in itm):
                LoadDrawInfo(organiItem, itm["drawInfo"])
        except Exception as e:
            pass #TODO:  collect possible errors in order to emit a warning
    
    for lyrItm in data["childLayers"]:
        childLayer = RecreateLayerData(lyrItm, setWrapper)
        childLayer.parentLayer = newLayer
    
    if ("drawInfo" in data):
        LoadDrawInfo(newLayer, data["drawInfo"])

    return newLayer

def RecreateSetData(data):
    newSet = oSet()
    try:
        newSet.create(data["name"])
    except Exception as err:
        MayaBridge.printWarning("Could not create Set named: {}".format(data["name"]))
        raise
    
    for lyr in data["layers"]:
        newLayer = RecreateLayerData(lyr, newSet)
        newSet.activeLayer = newLayer
    return newSet

def CreateExportLayer(layerWrapper):
    exportLayer = JSONUtils.Layer()
    exportLayer.name = layerWrapper.name
    
    for item in layerWrapper.getChildrenItems():
        exportItem = JSONUtils.Item()
        exportItem.dagNode = item.dagNode.node
        
        exportLayer.childItems.append(exportItem)
    
    for subLayer in layerWrapper.getChildrenLayers():
        exportLayer.childLayers.append(CreateExportLayer(subLayer))
    
    return exportLayer

def CreateExportSet(setWrapper):
    #Create Export Set
    exportSet = JSONUtils.Set()
    exportSet.name = setWrapper.name
    
    #Create Component Layers
    for layer in setWrapper.getComponentLayers():
        if (not layer.parentLayer):
            exportSet.componentLayers.append(CreateExportLayer(layer))
    
    return exportSet

def ExportSets(setWrappersArray, folder):
    for set in setWrappersArray:
        exportSet = CreateExportSet(set)
        fileName = "{}\\{}.json".format(folder, set.name)
        JSONUtils.WriteJSON(fileName, exportSet)

def ImportOrganiLayersFromFile(filePath):
    data = JSONUtils.ReadJSON(filePath)
    newSet = RecreateSetData(data)
    return newSet


# ------------------------------------
# - Scene Cleaning
# -----------------------------------
def CleanAllNodesInScene():
    # Clean OrganiLayers the right way
    organiSets = GetOrganiSets()
    for s in organiSets:
        s.deleteSet()
    
    # Reassure that, after deleting the existing OrganiSets
    # no orphan OrganiLayer and OrganiItem nodes are kept in the scene:
    orphanNodes = cmds.ls(type=["OrganiLayer", "OrganiItem"], ap=True)
    if (orphanNodes):
        cmds.delete(orphanNodes)
    
    CleanAllOrganiLayersCallbacks()

def CleanAllOrganiLayersCallbacks():
    allScriptJobs = cmds.scriptJob(listJobs=True)
    organilayersCallbacks = list(filter(lambda x: "OrganiLayers" in x, allScriptJobs))
    callbacksNumbers = list(map(lambda x: x.split(":")[0], organilayersCallbacks))
    for jobId in callbacksNumbers:
        cmds.scriptJob(kill=int(jobId), force=True)