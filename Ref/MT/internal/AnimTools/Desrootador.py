from PySide2 import QtWidgets

from QtCustomWidgets.PickButton import QPickButton

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

import AnimTools.CopyPasteWorld as CopyPasteWorld

import Utils.OpenMaya as OpenMayaUtils
from Utils.Maya.UndoContext import UndoContext

import ControlTagger

def unroot(cogControl, animRange=None, referenceNode=None):    
    cogTag = ControlTagger.GetControllerTag(cogControl)
    if cogTag == None:
        raise RuntimeError("The provided node doesn't have a Controller Tag assigned. Without it, the tool can't retrieve the hierarchy.")
    
    rigHierarchy = list(ControlTagger.GetHierarchyFromTag(cogTag))
    rigHierarchy.remove(cogControl)
    
    with UndoContext("Unroot"):
        transformData = CopyPasteWorld.copyWorldTransform(rigHierarchy, animRange=animRange)
    
        resetRootRotation(cogControl, animRange=animRange, referenceNode=referenceNode)
        
        CopyPasteWorld.pasteWorldTransform(transformData, rigHierarchy)

def resetRootRotation(cogControl, animRange=None, referenceNode=None):
    with UndoContext("Reset Root Rotation"):
        if animRange:
            keyTimes = [animRange[0]]
            keyTimes += cmds.keyframe(cogControl, q=True, at="rotate", time=animRange) or []
            keyTimes.append(animRange[1])
        else:
            keyTimes = cmds.keyframe(cogControl, q=True, at="rotate") or []
        
        cogControlTransformFn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(cogControl))
        
        if referenceNode:
            referenceNode = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(referenceNode))
            
        prev = None
        for time in keyTimes:
            if time != prev:
                cmds.currentTime(time)
                cmds.setKeyframe("{}.rotate".format(cogControl))
                if referenceNode is not None:
                    rotation = referenceNode.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
                    cogControlTransformFn.setRotation(rotation, OpenMaya.MSpace.kWorld)
                else:
                    cogControlTransformFn.setRotation(OpenMaya.MQuaternion.kIdentity, OpenMaya.MSpace.kTransform)
                
                prev = time

class DesrootadorWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle("Desrootador")
        
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        
        cogNodeGroupBox = QtWidgets.QGroupBox("Root")
        cogNodeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        mainLayout.addWidget(cogNodeGroupBox)
        
        self.cogNodePickButton = QPickButton()
        cogNodeGroupBox.layout().addWidget(self.cogNodePickButton)
        
        referenceNodeGroupBox = QtWidgets.QGroupBox("World Reference")
        referenceNodeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        mainLayout.addWidget(referenceNodeGroupBox)
        
        self.referenceNodePickButton = QPickButton(text="World")
        referenceNodeGroupBox.layout().addWidget(self.referenceNodePickButton)
        
        rangeGroupBox = QtWidgets.QGroupBox("Range")
        rangeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        mainLayout.addWidget(rangeGroupBox)
        
        self.selectedRangeRadioButton = QtWidgets.QRadioButton("Selected Range")
        rangeGroupBox.layout().addWidget(self.selectedRangeRadioButton)
        
        self.allKeysRadioButton = QtWidgets.QRadioButton("All Keys")
        rangeGroupBox.layout().addWidget(self.allKeysRadioButton)
        
        self.selectedRangeRadioButton.setChecked(True)
        
        unrootButton = QtWidgets.QPushButton("Unroot")
        unrootButton.clicked.connect(self.onUnrootButtonPressed)
        mainLayout.addWidget(unrootButton)
        
        self.resize(235, 0) # Min-Height
        
    def onUnrootButtonPressed(self):
        cogNode = self.cogNodePickButton.getPickedObject()
        if cogNode == None:
            QtWidgets.QMessageBox.warning("You must pick a Root node.")
            return
        
        referenceNode = self.referenceNodePickButton.getPickedObject()
        animRange = CopyPasteWorld.getSelectedAnimRange(defaultToCurrentRange=True) if self.selectedRangeRadioButton.isChecked() else None
        
        unroot(cogNode, animRange=animRange, referenceNode=referenceNode)
        
    def showEvent(self, event):
        selection = cmds.ls(selection=True)
        if len(selection) >= 1:
            self.cogNodePickButton.setPickedObject(selection[0])
        if len(selection) >= 2:
            self.referenceNodePickButton.setPickedObject(selection[1])


instance = None

def show():
    global instance
    if instance != None and instance.isVisible():
        instance.close()
    
    instance = DesrootadorWindow()
    instance.show()

if __name__ == "__main__":
    show()
