import json, os
import pymel.core as pm

class JSONSerializable(object):
    def __init__(self):
        super(JSONSerializable, self).__init__()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# ************************* Import / Export Sets Data *************************
class DrawInfo(JSONSerializable):
    def __init__(self):
        super(DrawInfo, self).__init__()
        self.displayType = 0
        self.levelOfDetail = 0
        self.shading = True
        self.texturing = True
        self.playback = True
        self.enabled = True
        self.visibility = True
        self.hideOnPlayback = False
        self.overrideRGBColors = True
        self.color = 0
        self.overrideColorRGB = (0,0,0)

class Item(JSONSerializable):
    def __init__(self):
        super(Item, self).__init__()
        self.dagNode = ''
        self.drawInfo = DrawInfo()

class Layer(JSONSerializable):
    def __init__(self):
        super(Layer, self).__init__()
        self.name = ''
        self.drawInfo = DrawInfo()
        self.childItems = []
        self.childLayers = []

class Set(JSONSerializable):
    def __init__(self):
        super(Set, self).__init__()
        self.name = ''
        self.layers = []
        self.activeLayerIdx = None
# *****************************************************************************

def WriteJSON(filePath, data):
    f = open(filePath, "w")
    f.write(data.toJSON())
    f.close()

def ReadJSON(filepath):
    data = []
    if (os.path.isfile(filepath)):
        with open(filepath) as f:
            data = json.load(f)
    
    return data

def CreateDrawInfo(drawableChild):
    exportableDrawInfo = DrawInfo()
    exportableDrawInfo.displayType      = drawableChild.displayType
    exportableDrawInfo.levelOfDetail    = drawableChild.levelOfDetail
    exportableDrawInfo.shading          = drawableChild.shading
    exportableDrawInfo.texturing        = drawableChild.texturing
    exportableDrawInfo.playback         = drawableChild.playback
    exportableDrawInfo.enabled          = drawableChild.enabled
    exportableDrawInfo.visibility       = drawableChild.visibility
    exportableDrawInfo.hideOnPlayback   = drawableChild.hideOnPlayback
    exportableDrawInfo.overrideRGBColors= drawableChild.overrideRGBColors
    exportableDrawInfo.color            = drawableChild.color
    exportableDrawInfo.overrideColorRGB = drawableChild.overrideColorRGB
    return exportableDrawInfo

def CreateJSONItem(itemWrapper):
    exportItem = Item()
    exportItem.dagNode = itemWrapper.dagNode.node
    exportItem.drawInfo = CreateDrawInfo(itemWrapper)
    return exportItem

def CreateJSONLayer(layerWrapper):
    exportLayer = Layer()
    exportLayer.name = layerWrapper.name
    exportLayer.drawInfo = CreateDrawInfo(layerWrapper)
    
    for itemWrap in layerWrapper.getChildrenItems():        
        exportLayer.childItems.append(CreateJSONItem(itemWrap))
    
    for subLayer in layerWrapper.getChildrenLayers():
        exportLayer.childLayers.append(CreateJSONLayer(subLayer))
    
    return exportLayer

def CreateJSONSet(setWrapper):
    #Create Export Set
    exportSet = Set()
    exportSet.name = setWrapper.name
    
    #Create Component Layers
    for layer in setWrapper.getComponentLayers():
        if (not layer.parentLayer):
            exportSet.layers.append(CreateJSONLayer(layer))
    
    return exportSet

def ExportJSONSets(setWrappersArray, folder):
    fileName = pm.system.sceneName().basename().splitext()[0]
    filenameClean = fileName.replace("_rig", "")

    for set in setWrappersArray:
        exportSet = CreateJSONSet(set)
        fileName = "{}\\OrganiLayers_{}_{}.json".format(folder, filenameClean, set.name)
        WriteJSON(fileName, exportSet)