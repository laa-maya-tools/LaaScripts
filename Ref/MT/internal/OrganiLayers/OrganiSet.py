import maya.cmds as cmds

from OrganiLayers.OrganiLayer               import OrganiLayerWrapper   as OLayer
from NodeManager.NodeWrapper    import NodeWrapper          as NWrapper
from Utils.Maya.UndoContext     import UndoContext

class OrganiSetWrapper(NWrapper):
    # NodeWrapper inherited "virtual" variable: Maya Node PlugIn:
    _Type = "OrganiSet"
    
    # Maya Node PlugIn Attributes:
    # Item Specific Plugs
    at_message          = "message"
    at_componentLayers  = "componentLayers"
    at_name             = "name"
    at_isActive         = "isActive"
    at_activeLayer      = "activeLayer"
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Properties -----------------------------
    #       -------------------------------------------------------------------------------
    @property
    def name(self):
        return self.getAttr(self.at_name)
    
    @name.setter
    def name(self, value):
        nodeName = "{}_{}".format(self._Type, value.replace(" ", "_"))
        
        if self.nodeExists():
            if self.name != value:
                if not cmds.objExists(nodeName) or self.node == nodeName:
                    with UndoContext("Set OrganiSet Name"):
                        self.renameNode(nodeName)
                        self.setStringAttribute(self.at_name, value)
                else:
                    raise AssertionError("Duplicated node name: {}".format(nodeName))
        else:
            raise AssertionError("Attempting to rename an unexisting node: {}".format(nodeName))
    
    #************************************************************
    @property
    def isActive(self):
        return self.getAttr(self.at_isActive) 
    
    @isActive.setter
    def isActive(self, value):
        self.setNumericAttribute(self.at_isActive, value)
        self.setAsDriver(value)
    
    #************************************************************
    @property
    def activeLayer(self):
        return self.getInputSingle(self.at_activeLayer, cls=OLayer)
    
    @activeLayer.setter
    def activeLayer(self, oLayerWrapper):
        self.setInputWrapper(self.at_activeLayer, oLayerWrapper, inputAttribute=oLayerWrapper.at_message)
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ----------------------- NodeWrapper Overriden Methods -------------------------
    #       -------------------------------------------------------------------------------
    def create(self, name):
        if name == "":
            raise NotImplementedError("Name must not be empty.")
        
        with UndoContext("Create OrganiSet"):                
            nodeName = "{}_{}".format(self._Type, name)
            super(OrganiSetWrapper, self).create(nodeName=nodeName, unique=True, skipSelect=True)
            
            self.name = name
    
    def delete(self):
        with UndoContext("Delete OrganiItem"):
            super(OrganiSetWrapper,self).delete()
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Methods --------------------------------
    #       -------------------------------------------------------------------------------
    def __init__(self, node=None):
        super(OrganiSetWrapper, self).__init__(node)
    
    def getComponentLayers(self):
        return self.getOutputSingle(self.at_componentLayers, cls=OLayer)
    
    def getRootLayers(self):
        allLayers = self.getComponentLayers()
        return [x for x in allLayers if x.parentLayer==None]
    
    def createLayer(self, layerName, parentLayer=None):
        newLayer = OLayer()
        
        try:
            newLayer.create(layerName)
            if (parentLayer and type(parentLayer) == OLayer):
                newLayer.parentLayer = parentLayer
            newLayer.organiSet = self
            #self.activeLayer = newLayer #Do not make the new layer as active by default
        except Exception as ex:
            raise ex
        
        return newLayer
    
    def deleteSet(self):
        for lyr in self.getRootLayers():
            lyr.deleteLayer()
        
        self.delete()
    
    def setAsDriver(self, value):
        for lyr in self.getRootLayers():
            lyr.setAsDriver(value)
    #endregion