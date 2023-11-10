from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui, QtCore
import QtCustomWidgets.UIFileWidget as UIFileWidget

import maya.cmds as cmds
import sys
import json
import os

class ShapeControlEditorWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"ShapeControlEditor\ShapeControlEditor.ui"
    __images_path__ = r"ShapeControlEditor\images"
    __charImages_path__ = r"ShapeControlEditor\images\chars"
    __library_path__ = r"ShapeControlEditor\shapesLibrary"

    _replaceShapes_ = False

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.__images_path__ = os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__images_path__)
        self.__charImages_path__ = os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__charImages_path__)
        self.__library_path__ = os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__library_path__)

        self.setObjectName('ShapeControlEditor')
        self.setWindowTitle('Shape Control Editor')

        self.ui.replaceShapesQButton.clicked.connect( self.replaceShapesQButtonAction )
        self.ui.addShapesQButton.clicked.connect( self.addShapesQButtonAction )
        self.ui.saveShapesQButton.clicked.connect( self.saveShapesQButtonAction )
        self.ui.charsSaveShapesQButton.clicked.connect( self.charsSaveShapesQButtonAction )
        self.ui.charsSetShapesQButton.clicked.connect( self.charsSetShapesQButtonAction )

        # IMAGES
        self.imagesQListUpdate()
        self.ui.imagesQList.setIconSize(QtCore.QSize(150,150))
        self.ui.charsImagesQList.setIconSize(QtCore.QSize(150,150))
        
        # LINE WIDTH
        self.ui.lineWidthQSlider.valueChanged.connect( self.lineWidthQSliderAction )
            
    def charsSetShapesQButtonAction(self):
        char = self.ui.charsImagesQList.selectedItems()
        if not char:
            cmds.warning("No character selection registered | Result: 0\n".format(char))
            return
        with open("{}\{}.json".format(self.__library_path__, char[0].toolTip()), 'r') as f:
            controlsDict = json.load(f)
        for control, shapesDict in controlsDict.items():
            if cmds.objExists(control):
                cmds.delete(cmds.listRelatives(control, shapes=True, type="nurbsCurve"))
                self.__addShapes__(control, shapesDict)
        sys.stdout.write("Char '{}' controls shapes setted | Result: 1\n".format(char[0].toolTip()))

    def addShapesQButtonAction(self):
        imagesLs = self.ui.imagesQList.selectedItems()
        if not imagesLs:
            cmds.warning("No shapes selection registered | Result: 0\n".format(char))
            return
        sel = cmds.ls(sl=True)
        if not sel:
            cmds.warning("No scene selection registered | Result: 0")
        for node in sel:
            if self._replaceShapes_:
                cmds.delete(cmds.listRelatives(node, shapes=True))
            for image in imagesLs:
                with open("{}\{}.json".format(self.__library_path__, image.toolTip()), 'r') as f:
                    curveDict = json.load(f)
                self.__addShapes__(node, curveDict)
        cmds.select(sel)
        sys.stdout.write("| Result: 1\n")

    def replaceShapesQButtonAction(self):
        self._replaceShapes_ = True
        self.addShapesQButtonAction()
        self._replaceShapes_ = False

    def saveShapesQButtonAction(self):
        sel = cmds.ls(sl=True)
        if not sel:
            cmds.warning("Nothing is selected\n")
            return
        with open("{}\{}.json".format(self.__library_path__, sel[0]), 'w') as f:
            json.dump( self.__saveShapes__(sel[0]), f, indent=True )
        self.shapeTakePicture(sel[0])
        sys.stdout.write("Generic '{}' shape saved | Result: 1\n".format(sel[0]))

    def charsSaveShapesQButtonAction(self):
        charName = self.ui.charsSaveShapesQLine.text()
        if not charName:
            cmds.warning("No input Name registered for character\n")
            return
        controlLs = []
        charControlDict = {}
        for control in cmds.ls(sl=True):
            shape = cmds.listRelatives(control, shapes=True)
            if not shape or cmds.nodeType(shape[0]) != "nurbsCurve":
                continue
            controlLs.append(control)
        for control in controlLs:
            charControlDict[control] = self.__saveShapes__(control)
        with open("{}\{}.json".format(self.__library_path__, charName), 'w') as f:
            json.dump( charControlDict, f, indent=True )
        self.shapeTakePicture(charName, True)
        sys.stdout.write("Char '{}' controls shapes saved | Result: 1\n".format(charName))
    
    def __addShapes__(self, curveName, curveDict):
        for shape, shapeDict in curveDict.items():
            shapeDict = curveDict[shape]
            tempCurve = cmds.curve(ws=True, point=shapeDict['point'], degree=shapeDict['degree'], knot=shapeDict['knot'], periodic=shapeDict['periodic'])
            shape = cmds.listRelatives(tempCurve, shapes=True)[0]
            cmds.setAttr("{}.overrideEnabled".format(shape), shapeDict['overrideEnabled'])
            cmds.setAttr("{}.overrideColor".format(shape), shapeDict['overrideColor'])
            cmds.setAttr("{}.overrideRGBColors".format(shape), shapeDict['overrideRGBColors'])
            cmds.setAttr("{}.overrideColorRGB".format(shape), *shapeDict['overrideColorRGB'])
            cmds.parent( shape, curveName, relative=True, shape=True )
            cmds.rename( shape, curveName + "Shape" )
            cmds.delete(tempCurve)
        
    def __saveShapes__(self, curve):
        crvDict = {}
        for shape in cmds.listRelatives(curve, shapes=True):
            if cmds.nodeType(shape) != "nurbsCurve":
                continue
            cinf = cmds.arclen(shape, ch=True)
            crvDict[shape] = {'point':cmds.getAttr(shape + ".cv[*]"),
            'degree':cmds.getAttr(shape + ".degree"),
            'periodic':bool(cmds.getAttr(shape + ".form")),
            'knot':cmds.getAttr(cinf + ".knots")[0],
            'overrideColor':cmds.getAttr(shape + ".overrideColor"),
            'overrideEnabled':cmds.getAttr(shape + ".overrideEnabled"),
            'overrideRGBColors':cmds.getAttr(shape + ".overrideRGBColors"),
            'overrideColorRGB':cmds.getAttr(shape + ".overrideColorRGB")[0]}
            indexExtend = len(cmds.getAttr(cinf + ".knots")[0]) - cmds.getAttr(shape + ".degree") + 1
            if len(cmds.getAttr(shape + ".cv[*]")) != indexExtend:
                indexExtend = abs(len(cmds.getAttr(shape + ".cv[*]")) - indexExtend)
                crvDict[shape]['point'].extend( crvDict[shape]['point'][:indexExtend] )
            cmds.delete(cinf)
        return crvDict
    
    def shapeTakePicture(self, imageName, char=False):
        imagePath = self.__images_path__
        if char:
            imagePath = self.__charImages_path__
        sel = cmds.ls(sl=True)
        isolated_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
        cmds.isolateSelect( isolated_panel, state=True )
        cmds.isolateSelect( isolated_panel, addSelected=True )
        cmds.select(clear=True)
        cmds.playblast(format='image', completeFilename=r"{}\{}.jpg".format(imagePath, imageName), st=1, et=1, viewer=False,
                        showOrnaments=False, percent=100, compression="jpg", quality=100, widthHeight=(150,150))
        cmds.isolateSelect( isolated_panel, state=False )
        cmds.select(sel)
        self.imagesQListUpdate()
    
    def imagesQListUpdate(self):
        self.__addImageQListItem__(self.ui.imagesQList, self.__images_path__)
        self.__addImageQListItem__(self.ui.charsImagesQList, self.__charImages_path__)
    
    def __addImageQListItem__(self, widget, imagesPath):
        widget.clear()
        for img in cmds.getFileList( folder=imagesPath ):
            imgQWidget = QtGui.QIcon(r"{}\{}".format(imagesPath, img))
            itemQWidget = QtWidgets.QListWidgetItem()
            itemQWidget.setToolTip( img[:-4] )
            itemQWidget.setIcon( imgQWidget )
            widget.addItem(itemQWidget)

    def lineWidthQSliderAction(self):
        sel = cmds.ls(sl=True)
        for each in sel:
            sel.extend( cmds.listRelatives(each, shapes=True) or [] )
        for node in sel:
            if "nurbsCurve" == cmds.nodeType(node):
                cmds.setAttr(node + ".lineWidth", self.ui.lineWidthQSlider.value()/10.0)

def show():
    global shapeControlEditor
    try:
        if shapeControlEditor.isVisible():
            shapeControlEditor.close()
    except NameError:
        pass
    shapeControlEditor = ShapeControlEditorWin()
    shapeControlEditor.show()