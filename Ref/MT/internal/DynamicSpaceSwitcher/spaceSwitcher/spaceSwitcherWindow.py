# -*- coding: utf-8 -*-

import maya.cmds as cmds

import NodeCustom.Transformations.SpaceSwitcher as SpaceSwitcher
import NodeManager.NodeWrapper as NodeWrapper

import DynamicSpaceSwitcher.mayalib.ui_cmds.baseWindow as baseWindow
import DynamicSpaceSwitcher.spaceSwitcher.spaceController as spaceController

# debug mode
# region
#import NodeCustom.Management.NodeCollection as NodeCollection
#import NodeMayaWrapper.ChoiceWrapper as CW
#import NodeManager.Lib.AttributeWrapperBase as AWB
#
#import importlib
#importlib.reload(baseWindow)
#importlib.reload(spaceController)
#importlib.reload(NodeCollection)
#importlib.reload(SpaceSwitcher)
#importlib.reload(CW)
#importlib.reload(NodeWrapper)
#importlib.reload(AWB)
# endregion

BaseWindow = baseWindow.BaseWindow
SpaceController = spaceController.SpaceController

class SpaceSwitcherWindow(baseWindow.BaseWindow):
    WINDOW_NAME = "SpaceSwitch"
    WINDOW_TITLE = "Dynamic Space Switcher"
    WIDTH = 300
    HEIGHT = 700
    SCROLLABLE = False
    
    def __init__(self):
        super().__init__()
        #super(SpaceSwitcherWindow, self).__init__()
        
        self.updateSpacesControllers()

    def createCustomUI(self):  
        self.frameLayout = cmds.frameLayout(label="Switch Spaces", width=self.WIDTH, marginHeight=5, marginWidth=5, collapsable=False)
        
        #cmds.separator()
        self.serchSpaceButton = cmds.button("Update", command=self.updateSpacesControllers)
        self.addSpaceButton   = cmds.button("Add", backgroundColor=[0.15, 0.4, 0.15], command=self.addSpaceController)
        cmds.separator()
        self.spaceScroll      = cmds.scrollLayout(width=self.WIDTH, height=self.HEIGHT -100, parent = self.contentLayout)
        self.spaceContent     = cmds.columnLayout(width=self.WIDTH - 20, adjustableColumn=True, parent=self.spaceScroll)

    def clearSpacesControllers(self, *args): 
        theList = (cmds.columnLayout(self.spaceContent, q=True, childArray=True) ) or[]
        for item in theList:
            cmds.deleteUI(self.spaceContent + "|" + item)

    def updateSpacesControllers(self, *args):     
        self.clearSpacesControllers()
        
        spaceNodeList = cmds.ls(type="spaceSwitcher")
        for spaceNode in spaceNodeList:
            SpaceController(spaceNode, self.spaceContent)    

    def addSpaceController(self, *args):
        selection =  cmds.ls(selection=True,type="transform")
        if not selection or len(selection) == 0:
            cmds.warning("seleccione un objeto para configurar SpaceSwitch")
            return 
        
        for theNode in selection:
            SpaceSwitcherWrapper = SpaceSwitcher.SpaceSwitcher()
            nWrapper = NodeWrapper.NodeWrapper(theNode)

            currentSpace = nWrapper.getInputSingle("offsetParentMatrix", cls = SpaceSwitcherWrapper.__class__, plugs=False, type = SpaceSwitcherWrapper._Type)
            if currentSpace:    
                cmds.warning("Objeto {} ya configurado con SpaceSwitcher".format(theNode))
                continue
            else:  
                SpaceSwitcherWrapper.create (nodeName=None, outputNode=nWrapper.node ,unique=False, skipSelect=False)   

        self.updateSpacesControllers()


