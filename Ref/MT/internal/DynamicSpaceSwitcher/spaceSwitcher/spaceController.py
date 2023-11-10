# -*- coding: utf-8 -*-

import maya.cmds as cmds

import maya.api.OpenMaya as om
import Utils.OpenMaya as utilsOM

from Utils.Maya.UndoContext import UndoContext

import NodeCustom.Transformations.SpaceSwitcher as SpaceSwitcher

# debug mode
# region

#import NodeManager.MayaWrapper.ChoiceWrapper as ChoiceWrapper
## TODO revisar en utils si estos métodos no estan duplicados, añadirlos si es necesario a la librería general.
#import DynamicSpaceSwitcher.mayalib.animLib as animLib 
#
#import importlib
#importlib.reload(SpaceSwitcher)
#importlib.reload(ChoiceWrapper)
#importlib.reload(animLib)
# endregion

class SpaceController():
    def __init__(self, spaceSwitcherNode, parentWidget):
        self.spaceSwitcherWrapper = SpaceSwitcher.SpaceSwitcher(spaceSwitcherNode)
        
        self.parentWidget = parentWidget
        
        self.createUI()
        self.updateSpaces()

    # Metodos de la interface
    # region

    def createUI(self):
        if self.parentWidget != None:
            cmds.setParent(self.parentWidget)

        self.frameLayout = cmds.frameLayout("Space: {}".format(self.spaceSwitcherWrapper.outputNode), marginHeight=5, marginWidth=5, backgroundShade=True)

        cmds.rowLayout(numberOfColumns=4, adjustableColumn=2,parent=self.frameLayout)

        cmds.button("Delete Switcher", backgroundColor=[0.4, 0.15, 0.15],   command=self.removeSwitcher , width=108, height=15)
        cmds.text("")
        cmds.button("Control", backgroundColor=[0.15,0.15,0.4],   command=self.selectControlNode , width=50, height=15, align= "right")
        #cmds.text("Control: ", align= "right", width=90)
        self.ControlResetTransform = cmds.checkBox( label='reset', value=False, align= "right", width=60)
        
        cmds.rowLayout(numberOfColumns=5, adjustableColumn=3,parent=self.frameLayout)
        cmds.button("Add", backgroundColor=[0.15, 0.4, 0.15],   command=self.addSpace , width=53 ,      height=15)
        cmds.button("Del", backgroundColor=[0.4, 0.15, 0.15],   command=self.removeSpace , width=53,    height=15)
        #cmds.text("Offset: ", align= "right", width=90)
        cmds.text("")
        cmds.button("Offset", backgroundColor=[0.15,0.15,0.4],   command=self.selectOffsetNode , width=50, height=15)
        self.OffsetResetTransform = cmds.checkBox( label='reset', value=False, align= "right", width=60)
    
        cmds.rowLayout(numberOfColumns=2, parent=self.frameLayout, adjustableColumn=1)
        self.spaceOptionMenu = cmds.optionMenu(label="",        changeCommand=self.switchSpace, width=170)  
        cmds.button("key",   backgroundColor=[0.15,0.15,0.4],     align="left",   command=self.addKeySpace)

    def deleteUI(self, *arg):
        print("deleteUI: ", self.frameLayout)
        cmds.deleteUI(self.frameLayout)

    def exists(self, *arg): 
        return cmds.frameLayout(self.frameLayout, exists=True)

    def clearUiItemList(self):
        uiItemListID = cmds.optionMenu(self.spaceOptionMenu, query=True, itemListLong=True) or[]
        uiItemNum = cmds.optionMenu(self.spaceOptionMenu, query=True, numberOfItems=True)
        for i in (range(uiItemNum)):
            cmds.deleteUI(uiItemListID[i])
    
    def getUiItemList(self):
        # TODO No estoy seguro de que esta forma se la correcta para conseguir la lista de targets en la ui
        uiItemNum = cmds.optionMenu(self.spaceOptionMenu, query=True, numberOfItems=True)
        uiCurrentItem = cmds.optionMenu(self.spaceOptionMenu,value=True,query=True)
        uiItemList = []
        for i in (range(uiItemNum)):
            cmds.optionMenu(self.spaceOptionMenu, select=i+1, e=True)
            uiItemList.append(cmds.optionMenu(self.spaceOptionMenu,value=True,query=True))
        
        #uiSelect = uiItemList.index(uiCurrentItem)+1
        #cmds.optionMenu(self.spaceOptionMenu,select=uiSelect,e=True)
        cmds.optionMenu(self.spaceOptionMenu,value=uiCurrentItem,e=True)

        return uiItemList

    def updateSpaces(self):
        self.clearUiItemList()

        targetList = list(self.spaceSwitcherWrapper.targetsWrapper)
        for item in targetList:
            cmds.menuItem(label=item, parent=self.spaceOptionMenu)
            
        index = self.spaceSwitcherWrapper.targetIndexValue + 1
        cmds.optionMenu(self.spaceOptionMenu, edit=True, select=index)    

    # endregion

    # Comportamiento de los eventos de la interface
    # region

    # BUTTON 
    def switchSpace(self, *arg):
        with UndoContext("SpaceSwitcher UI: Change Space"):
            pass
 
    # BUTTON    
    def addSpace(self, *arg):
        with UndoContext("SpaceSwitcher UI: Add Space Target"):
            selection = cmds.ls(selection=True)
            
            if not selection:
                cmds.warning("seleccione un objeto para configurarlo como Space")
                return 

            targetsWrapper = self.spaceSwitcherWrapper.targetsWrapper

            for spaceObject in selection:
                if spaceObject in list(targetsWrapper):
                    cmds.warning("Objeto {} ya es un Space configurado".format(spaceObject))
                    continue
                targetsWrapper += [spaceObject]
                cmds.menuItem(label=spaceObject, parent=self.spaceOptionMenu)
                        
            self.updateSpaces()
    
    # BUTTON     
    def removeSpace(self, *arg):
        with UndoContext("SpaceSwitcher UI: Remove Space Target"):
            space = cmds.optionMenu(self.spaceOptionMenu, query=True, value=True)
            if space == None or space=="unitaryMatrix":
                return
            targetsWrapper = self.spaceSwitcherWrapper.targetsWrapper
            targetsWrapper.remove(space) 

            self.updateSpaces()

    # BUTTON
    def removeSwitcher(self, *arg):
        self.deleteUI()
        self.spaceSwitcherWrapper.delete()

    # BUTTON     
    def addKeySpace(self, *arg):
        with UndoContext("SpaceSwitcher UI: Add Key Space"):
            self.setOffsetTrasform()
            self.spaceSwitcherWrapper.addKey()

    # Sin elemento de la interface asociado
    def selectSwitcherNode(self,*arg):
        node = self.spaceSwitcherWrapper.node
        cmds.select(node)

    def selectControlNode(self,*arg):
        node = self.spaceSwitcherWrapper.outputNode
        cmds.select(node)
    
    # Sin elemento de la interface asociado
    def selectOffsetNode(self,*arg):
        node = self.spaceSwitcherWrapper.offsetWrapper.node
        cmds.select(node)

    # endregion

    # Conjunto de métodos de transformacion
    # region

    def setOffsetTrasform(self):
        newIndex = (cmds.optionMenu(self.spaceOptionMenu, query=True, select=True))-1
        currentIndex    = self.spaceSwitcherWrapper.targetIndex  

        offsetNode = utilsOM.asDagPath(self.spaceSwitcherWrapper.offsetWrapper.node)
        offsetMatrix = offsetNode.inclusiveMatrix()

        outputNode = utilsOM.asDagPath(self.spaceSwitcherWrapper.outputNode)

        # cualquiera de los tres métodos es viable.
        # al no entender porque el orden de la multiplicación afecta según tome las matrices de una u otra forma, dejo comentadas las opciones
        # en un principio pensaba que estaba tomando mal el valor de las matrices pero al cambiar el orden de la multiplicación funciona.
        # el tercer método tiene la ventaja de poder usarse tambien con nodos dg
        ## ------------ 1
        #initMatrix = outputNode.inclusiveMatrix()
        #self.spaceSwitcherWrapper.targetIndex = newIndex
        #cmds.dgdirty(self.spaceSwitcherWrapper.outputNode)
        #endMatrix = outputNode.inclusiveMatrix()
        #relativeMatrix = (initMatrix * endMatrix.inverse()) * offsetMatrix
        ##---------------
        ## ------------ 2
        #targetNodes = list(self.spaceSwitcherWrapper.targetsWrapper)
        #endMatrix   = (utilsOM.asDagPath(targetNodes[newIndex])).inclusiveMatrix()
        #initMatrix  = (utilsOM.asDagPath(targetNodes[currentIndex])).inclusiveMatrix()
        #relativeMatrix = offsetMatrix * (initMatrix * endMatrix.inverse())
        #self.spaceSwitcherWrapper.targetIndex = newIndex
        ##---------------
        ## ------------ 3
        endMatrix       = om.MMatrix(self.spaceSwitcherWrapper.getTargetMatrix(newIndex))
        initMatrix      = om.MMatrix(self.spaceSwitcherWrapper.getTargetMatrix(currentIndex)) 
        relativeMatrix = offsetMatrix * (initMatrix * endMatrix.inverse())
        self.spaceSwitcherWrapper.targetIndex = newIndex
        ##---------------

        if (cmds.checkBox(self.OffsetResetTransform,value=True,query=True)):
            om.MFnTransform(offsetNode).setTransformation(om.MTransformationMatrix())
        else:
            om.MFnTransform(offsetNode).setTransformation(om.MTransformationMatrix(relativeMatrix))

        #if not (cmds.checkBox(self.ControlResetTransform,value=True,query=True)):
        if (cmds.checkBox(self.ControlResetTransform,value=True,query=True)):
            outputNode = utilsOM.asDagPath(self.spaceSwitcherWrapper.outputNode)
            om.MFnTransform(outputNode).setTransformation(om.MTransformationMatrix())

     # endregion
    
