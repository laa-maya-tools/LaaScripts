
import maya.cmds as cmds
import OrganiLayers.InheritableDrawInfo as InheritableDrawInfo

from Utils.Maya.UndoContext import UndoContext

class OrganiLayerWrapper(InheritableDrawInfo.InheritableDrawInfoWrapper):  
    # NodeWrapper inherited "virtual" variable: Maya Node PlugIn:
    _Type = "OrganiLayer"
    
    __NodeNameBase = "{}_{}_0"
    
    # Maya Node PlugIn Attributes:
    # Layer Specific Plugs
    at_message      = "message"
    at_name         = "name"
    at_parentLayer  = "parentLayer"
    at_childLayers  = "childLayers"
    at_childItems   = "childItems"
    at_set          = "set"
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Properties -----------------------------
    #       -------------------------------------------------------------------------------
    @property
    def name(self):
        return self.getAttr(self.at_name)
    
    @name.setter
    def name(self, value):        
        if self.nodeExists():
            with UndoContext("Set OrganiLayer Name"):
                self.setStringAttribute(self.at_name, value)
                nodeName = self.__NodeNameBase.format(self._Type, value.replace(" ", "_"))
                self.renameNode(nodeName)
        else:
            raise AssertionError("Attempting to rename an unexisting node: {}".format(nodeName))
    
    #************************************************************
    @property
    def parentLayer(self):
        return self.getInputSingle(self.at_parentLayer, cls=OrganiLayerWrapper)
    
    @parentLayer.setter
    def parentLayer(self, inputWrapper):
        if (inputWrapper):
            self.setInputWrapper(self.at_parentLayer, inputWrapper, inputAttribute=inputWrapper.at_childLayers)
            self.setInputWrapper(self.at_parentDrawInfo, inputWrapper, inputAttribute=inputWrapper.at_outDrawInfo)
            self.setInputWrapper(self.at_parentSpreadInfo, inputWrapper, inputAttribute=inputWrapper.at_outSpreadInfo)
        else:
            self.clearConnection(self.at_parentLayer, removeInput=True)
            self.clearConnection(self.at_parentDrawInfo, removeInput=True)
            self.clearConnection(self.at_parentSpreadInfo, removeInput=True)
    
    #************************************************************
    @property
    def organiSet(self):
        from OrganiLayers.OrganiSet import OrganiSetWrapper
        return self.getInputSingle(self.at_set, cls=OrganiSetWrapper)
    
    @organiSet.setter
    def organiSet(self, inputWrapper):
        self.setInputWrapper(self.at_set, inputWrapper, inputAttribute=inputWrapper.at_componentLayers)
    #endregion 
    
    #       -------------------------------------------------------------------------------
    #region ----------------------- NodeWrapper Overriden Methods -------------------------
    #       -------------------------------------------------------------------------------
    def create(self, name):
        if name == "":
            raise NotImplementedError("Name must not be empty.")
        
        with UndoContext("Create OrganiLayer"):                
            nodeName = "{}_{}".format(self._Type, name)
            super(OrganiLayerWrapper, self).create(nodeName=nodeName, unique=False)
            
            self.name = name
    
    def delete(self):
        with UndoContext("Delete OrganiLayer"):
            super(OrganiLayerWrapper,self).delete()
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Methods --------------------------------
    #       -------------------------------------------------------------------------------
    def __init__(self, node=None):
        super(OrganiLayerWrapper, self).__init__(node)
    
    def getChildrenLayers(self):
        return self.getOutputSingle(self.at_childLayers, cls=OrganiLayerWrapper)
    
    def getChildrenItems(self):
        from OrganiLayers.OrganiItem import OrganiItemWrapper
        return self.getOutputSingle(self.at_childItems, cls=OrganiItemWrapper)
    
    def cleanInvalidItems(self):
        itemWraps = self.getChildrenItems()
        for itemWrapper in itemWraps:
            if (not itemWrapper.dagNode):
                itemWrapper.delete()
    
    def deleteLayer(self):
        for lyr in self.getChildrenLayers():
            lyr.deleteLayer()
        
        for itm in self.getChildrenItems():
            itm.delete()
        
        self.delete()
    
    def setAsDriver(self, value):
        for lyr in self.getChildrenLayers():
            lyr.setAsDriver(value)
        
        for itm in self.getChildrenItems():
            itm.setAsDriver(value)
    
    def isActive(self):
        return self.organiSet.activeLayer.node == self.node
    
    def getLayerPath(self):
        if (self.parentLayer):
            return "{}.{}".format(self.parentLayer.getLayerPath(), self.name)
        else:
            return self.name
    #endregion

#region --- USE EXAMPLE:
#import wip.OrganiLayers.MayaWrappers as MWrap
#reload(MWrap)
#
#from wip.OrganiLayers.MayaWrappers import OrganiLayerWrapper as OLWrap
#
#a = OLWrap.OrganiLayerWrapper()
#a.create("patata")
#a.delete()
#endregion