import maya.cmds as cmds
import OrganiLayers.InheritableDrawInfo as InheritableDrawInfo

from OrganiLayers.OrganiLayer               import OrganiLayerWrapper as OLayer
from NodeManager                import NodeWrapper
from Utils.Maya.UndoContext     import UndoContext


class OrganiItemWrapper(InheritableDrawInfo.InheritableDrawInfoWrapper):
    # NodeWrapper inherited "virtual" variable: Maya Node PlugIn:
    _Type = "OrganiItem"
    
    __NodeNameBase = "{}_{}_0"
    
    # Maya Node PlugIn Attributes:
    # Item Specific Plugs
    at_message      = "message"
    at_parentLayer  = "parentLayer"
    at_dagNode      = "dagNode"
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Properties -----------------------------
    #       -------------------------------------------------------------------------------
    @property
    def name(self):
        return self.getInputSingle(self.at_dagNode) #TODO: It's neccessary to add the "shapes=True" Flag in GetInputSingle when it calls cmds.listConnections
    
    @name.setter
    def name(self, value):
        if self.nodeExists():
            with UndoContext("Set OrganiItem Name"):
                newName = value
                if (self.dagNode):
                    newName = self.dagNode.renameNode(value)
                    self.renameNode(self.__NodeNameBase.format(self._Type, self.name.replace("|", "_")))
        else:
            raise AssertionError("Attempting to rename an unexisting node: {}".format(value))
    
    #************************************************************
    @property
    def parentLayer(self):
        return self.getInputSingle(self.at_parentLayer, cls=OLayer)
    
    @parentLayer.setter
    def parentLayer(self, inputWrapper):
        if (inputWrapper):
            self.setInputWrapper(self.at_parentLayer, inputWrapper, inputAttribute=inputWrapper.at_childItems)
            self.setInputWrapper(self.at_parentDrawInfo, inputWrapper, inputAttribute=inputWrapper.at_outDrawInfo)
            self.setInputWrapper(self.at_parentSpreadInfo, inputWrapper, inputAttribute=inputWrapper.at_outSpreadInfo)
        else:
            self.clearConnection(self.at_parentLayer, removeInput=True)
            self.clearConnection(self.at_parentDrawInfo, removeInput=True)
            self.clearConnection(self.at_parentSpreadInfo, removeInput=True)
    
    #************************************************************
    @property
    def dagNode(self):
        return self.getInputSingle(self.at_dagNode, cls=NodeWrapper.NodeWrapper)
    
    @dagNode.setter
    # Input value can be a node name or a NodeWrapper instance
    def dagNode(self, dagNode):
        dagNodeWrapper = dagNode
        if (not isinstance(dagNode, NodeWrapper.NodeWrapper)):
            dagNodeWrapper = NodeWrapper.NodeWrapper(dagNode)
        
        if (dagNodeWrapper.node != None):
            self.setInputWrapper(self.at_dagNode, dagNodeWrapper, inputAttribute="message")
            # Find al shape relatives and connect their overrides. Disconnect old connections
            self.clearConnection(self.at_outDrawInfo, removeOutput=True)
            self.setAsDriver(True)
            # Rename the OrganiItem node, erasing "illegal"" characters from the full Path (Maya converts by default "|" to "_"), but it prints a warning we do not want
            self.renameNode(self.__NodeNameBase.format(self._Type, self.name.replace("|", "_")))
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ----------------------- NodeWrapper Overriden Methods -------------------------
    #       -------------------------------------------------------------------------------
    def create(self, name):
        if name == "":
            raise NotImplementedError("Name must not be empty.")
        
        with UndoContext("Create OrganiItem"):
            nodeName = self.__NodeNameBase.format(self._Type, name)
            super(OrganiItemWrapper, self).create(nodeName=nodeName, unique=False)
            
            #self.name = name
    
    def delete(self):
        with UndoContext("Delete OrganiItem"):
            self.setAsDriver(False)
            super(OrganiItemWrapper,self).delete()
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Methods --------------------------------

    #       -------------------------------------------------------------------------------
    def __init__(self, node=None):
        super(OrganiItemWrapper, self).__init__(node)
    
    def getDagNodeShapes(self):
        if (self.dagNode):
            return cmds.listRelatives(self.dagNode.node, shapes=True, path=True) or []
        else:
            return []
    
    def getConnectedShapes(self):
        """Forces the return of connected shapes (or better said: nodes with a drawOverride attribute
        connected), in case of this node not having a DagNode connected but having shapes connected.
        For example: when using instanced shapes (like mGear does with a guide custom shapes)
        """
        return [x for x in self.getOutputSingle(self.at_outDrawInfo) if cmds.attributeQuery("drawOverride", node=x, exists=True)]
    
    def setAsDriver(self, value):
        if (value):
            for shape in self.getDagNodeShapes():
                shapeWrapper = NodeWrapper.NodeWrapper(shape)
                shapeWrapper.clearConnection("drawOverride", removeInput=True)
                self.connect("{}.drawOverride".format(shape), self.getPlug(self.at_outDrawInfo))
        else:
            currentDrawOverrideState = {}
            for shape in self.getConnectedShapes():
                drawOverrideState = {}
                for attribute in cmds.attributeQuery("drawOverride", node=shape, listChildren=True):
                    drawOverrideState[attribute] = cmds.getAttr("{}.{}".format(shape, attribute))
                currentDrawOverrideState[shape] = drawOverrideState
                
            self.clearConnection(self.at_outDrawInfo, removeOutput=True)
            
            for shape, drawOverrideState in currentDrawOverrideState.items():
                for attribute, value in drawOverrideState.items():
                    if isinstance(value, list):
                        value = value[0]    # This case only happens with colors, that are wrapped on a single element array
                    if isinstance(value, tuple):
                        cmds.setAttr("{}.{}".format(shape, attribute), *value)
                    else:
                        cmds.setAttr("{}.{}".format(shape, attribute), value)
                # Try and Force the visibility to True and Unfreeze in order
                # to not let objects in scene invisible or frozen involuntarily
                    cmds.setAttr("{}.overrideVisibility".format(shape), True)
                    cmds.setAttr("{}.overrideDisplayType".format(shape), 0)
    #endregion