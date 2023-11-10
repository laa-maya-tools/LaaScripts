from NodeManager            import NodeWrapper
from Utils.Maya.UndoContext import UndoContext

import maya.cmds as cmds

class InheritableDrawInfoWrapper(NodeWrapper.NodeWrapper):  
    # NodeWrapper inherited "virtual" variable: Maya Node PlugIn:
    _Type = "InheritableDrawInfo"
    
    # Maya Node PlugIn Attributes:
    # Draw Info Plugs
    at_displayType      = "displayType"
    at_levelOfDetail    = "levelOfDetail"
    at_shading          = "shading"
    at_texturing        = "texturing"
    at_playback         = "playback"
    at_enabled          = "enabled"
    at_visibility       = "visibility"
    at_hideOnPlayback   = "hideOnPlayback"
    at_overrideRGBColors= "overrideRGBColors"
    at_color            = "color"
    at_overrideColorRGB = "overrideColorRGB"
    # Spread Info Plugs
    at_spreadDisplayType    = "spreadDisplayType"
    at_spreadLevelOfDetail  = "spreadLevelOfDetail"
    at_spreadColor          = "spreadColor"
    # Parent / Out Info
    at_outDrawInfo      = "outDrawInfo"
    at_parentDrawInfo   = "parentDrawInfo"
    at_outSpreadInfo    = "outSpreadInfo"
    at_parentSpreadInfo = "parentSpreadInfo"
    #at_drawInfo         = "drawInfo"
    #at_spreadInfo       = "spreadInfo"
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Properties -----------------------------
    #       -------------------------------------------------------------------------------
    @property
    def displayType(self):
        return self.getAttr(self.at_displayType)
    
    @displayType.setter
    def displayType(self, value):
        self.setNumericAttribute(self.at_displayType, value)
    
    #************************************************************
    @property
    def levelOfDetail(self):
        return self.getAttr(self.at_levelOfDetail)
        
    @levelOfDetail.setter
    def levelOfDetail(self, value):
        self.setNumericAttribute(self.at_levelOfDetail, value)
    
    #************************************************************
    @property
    def shading(self):
        return self.getAttr(self.at_shading)
    
    @shading.setter
    def shading(self, value):
        self.setNumericAttribute(self.at_shading, value)
    
    #************************************************************
    @property
    def texturing(self):
        return self.getAttr(self.at_texturing)
    
    @texturing.setter
    def texturing(self, value):
        self.setNumericAttribute(self.at_texturing, value)
    
    #************************************************************
    @property
    def playback(self):
        return self.getAttr(self.at_playback)
    
    @playback.setter
    def playback(self, value):
        self.setNumericAttribute(self.at_playback, value)
    
    #************************************************************
    @property
    def enabled(self):
        return self.getAttr(self.at_enabled)
    
    @enabled.setter
    def enabled(self, value):
        self.setNumericAttribute(self.at_enabled, value)
    
    #************************************************************
    @property
    def visibility(self):
        return self.getAttr(self.at_visibility)
    
    @visibility.setter
    def visibility(self, value):
        self.setNumericAttribute(self.at_visibility, value)
    
    #************************************************************
    @property
    def hideOnPlayback(self):
        return self.getAttr(self.at_hideOnPlayback)
    
    @hideOnPlayback.setter
    def hideOnPlayback(self, value):
        self.setNumericAttribute(self.at_hideOnPlayback, value)
    
    #************************************************************
    @property
    def overrideRGBColors(self):
        return self.getAttr(self.at_overrideRGBColors)
    
    @overrideRGBColors.setter
    def overrideRGBColors(self, value):
        self.setNumericAttribute(self.at_overrideRGBColors, value)
    
    #************************************************************
    @property
    def color(self):
        return self.getAttr(self.at_color)
    
    @color.setter
    def color(self, value):
        self.setNumericAttribute(self.at_color, value)
    
    #************************************************************
    @property
    def overrideColorRGB(self):
        return self.getAttr(self.at_overrideColorRGB)[0]
    
    @overrideColorRGB.setter
    def overrideColorRGB(self, value):
        self.setFloat3Attribute(self.at_overrideColorRGB, value)
    
    #************************************************************
    @property
    def spreadDisplayType(self):
        return self.getAttr(self.at_spreadDisplayType)
    
    @spreadDisplayType.setter
    def spreadDisplayType(self, value):
        self.setNumericAttribute(self.at_spreadDisplayType, value)
    
    #************************************************************
    @property
    def spreadLevelOfDetail(self):
        return self.getAttr(self.at_spreadLevelOfDetail)
    
    @spreadLevelOfDetail.setter
    def spreadLevelOfDetail(self, value):
        self.setNumericAttribute(self.at_spreadLevelOfDetail, value)
    
    #************************************************************
    @property
    def spreadColor(self):
        return self.getAttr(self.at_spreadColor)
    
    @spreadColor.setter
    def spreadColor(self, value):
        self.setNumericAttribute(self.at_spreadColor, value)
    
    #************************************************************
    #endregion 
    
    #       -------------------------------------------------------------------------------
    #region ----------------------- NodeWrapper Overriden Methods -------------------------
    #       -------------------------------------------------------------------------------
    def create(self, nodeName=None, unique=False, skipSelect=True):
        with UndoContext("Create InheritableDrawInfo"):
            super(InheritableDrawInfoWrapper, self).create(nodeName, unique, skipSelect)
    
    def delete(self):
        with UndoContext("Delete InheritableDrawInfo"):
            super(InheritableDrawInfoWrapper,self).delete()
    #endregion
    
    #       -------------------------------------------------------------------------------
    #region ------------------------------ Wrapper Methods --------------------------------
    #       -------------------------------------------------------------------------------
    def __init__(self, node=None):
        super(InheritableDrawInfoWrapper, self).__init__(node)
    #endregion