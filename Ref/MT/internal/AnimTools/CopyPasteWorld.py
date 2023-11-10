from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

from PySide2 import QtWidgets

import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

from Utils.Maya.UndoContext import UndoContext
from Utils.Python import frange

import ControlTagger
import TimeSlider

import os
import math
import json
import tempfile


DEFAULT_FILE_PATH = os.path.join(tempfile.gettempdir(), "Maya", "CopyPasteWorld", "copiedTransforms.json")


class CopiedTransformEncoder(json.JSONEncoder):
    
    def default(self, o):
        if isinstance(o, OpenMaya.MMatrix):
            return {
                "class" : "MMatrix",
                "value" : [e for e in o]
            }
        
        return super().default(o)


class CopiedTransformDecoder(json.JSONDecoder):
    
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, dict):
        if "class" in dict:
            if dict["class"] == "MMatrix":
                return OpenMaya.MMatrix(dict["value"])
        
        return dict


def getSelectedTransforms():
    selection = cmds.ls(selection=True) or []
    i = 0
    while i < len(selection):
        if not cmds.objectType(selection[i], isa="transform"):
            parent = cmds.listRelatives(selection[i], parent=True, type="transform")
            if parent:
                selection[i] = parent[0]
            else:
                selection.pop(i)
                i -= 1
        i += 1
    return cmds.ls(selection, long=True)

def getSelectedAnimRange(defaultToCurrentRange=False):
    if cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeVisible=True):
        return tuple(cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, rangeArray=True))
    elif defaultToCurrentRange:
        start = cmds.playbackOptions(q=True, min=True)
        end = cmds.playbackOptions(q=True, max=True)
        return (start, end)
    else:
        currentTime = cmds.currentTime(q=True)
        return (currentTime, currentTime)

def getTransformKeyTimes(obj, animRange=None):
    keyTimes = set()
    if animRange != None:
        keyTimes.update(cmds.keyframe(obj, at="translate", q=True, time=animRange) or [])
        keyTimes.update(cmds.keyframe(obj, at="rotate", q=True, time=animRange) or [])
        keyTimes.update(cmds.keyframe(obj, at="scale", q=True, time=animRange) or [])
    else:
        keyTimes.update(cmds.keyframe(obj, at="translate", q=True) or [])
        keyTimes.update(cmds.keyframe(obj, at="rotate", q=True) or [])
        keyTimes.update(cmds.keyframe(obj, at="scale", q=True) or [])
    keyTimes = list(keyTimes)
    keyTimes.sort()
    return keyTimes

def getWorldTransform(obj, time=None):
    # It's easier to get the world matrix using xform rather than OpenMaya
    if time != None:
        worldMatrix = cmds.getAttr("{}.worldMatrix".format(obj), time=time)
        scale = cmds.getAttr("{}.scale".format(obj), time=time)
    else:
        worldMatrix = cmds.getAttr("{}.worldMatrix".format(obj))
        scale = cmds.getAttr("{}.scale".format(obj))
        
    mTfMatrix = OpenMaya.MTransformationMatrix(OpenMaya.MMatrix(worldMatrix))
    mTfMatrix.setScale(scale[0], OpenMaya.MSpace.kTransform)
    
    return mTfMatrix.asMatrix()

def setWorldTransform(obj, matrix):
    targetTrf = OpenMaya.MTransformationMatrix(matrix)
    position = list(targetTrf.translation(OpenMaya.MSpace.kTransform))
    scale = list(targetTrf.scale(OpenMaya.MSpace.kTransform))
    
    currentTrf = OpenMaya.MTransformationMatrix(getWorldTransform(obj))
    offset = currentTrf.rotation(OpenMaya.MSpace.kTransform).inverse() * targetTrf.rotation(OpenMaya.MSpace.kTransform)
    angles = offset.asEulerRotation()
    angles = [angle * 180.0 / math.pi for angle in angles]
        
    with UndoContext("Set World Transform"):
        # We use cmds to set the matrix since it is easy to undo.
        # We need to manually set a keyframe or Maya won't add one nor set the right value.
        cmds.move(*position, obj, ws=True, absolute=True)
        cmds.setKeyframe("{}.{}".format(obj, "translate"))
        
        cmds.rotate(*angles, obj, relative=True, ws=True, forceOrderXYZ=True)
        cmds.setKeyframe("{}.{}".format(obj, "rotate"))
        
        cmds.scale(*scale, obj, ws=False, absolute=True)
        cmds.setKeyframe("{}.{}".format(obj, "scale"))
        
def copyWorldTransform(nodes, relative=False, animRange=None, bake=False, fast=False, copyTimes=None):
    if relative:
        if len(nodes) < 2:
            raise RuntimeError("Relative mode requires at least 2 nodes must be selected!")
        relativeTo = nodes[-1]
        nodes = nodes[:-1]
    
    if animRange == None:
        animStart = None
        animEnd = None
        for obj in nodes:
            keyTimes = copyTimes[obj] if copyTimes and obj in copyTimes else getTransformKeyTimes(obj)
            if keyTimes:
                start = min(keyTimes)
                end = max(keyTimes)
                if animStart == None or animStart > start:
                    animStart = start
                if animEnd == None or animEnd < end:
                    animEnd = end
        if animStart == None:
            return {}
        animRange = (animStart, animEnd)
    
    nodeKeyTimes = {}
    for obj in nodes:
        if bake:
            keyTimes = list(frange(animRange[0], animRange[1] + 1))
        elif copyTimes and obj in copyTimes:
            keyTimes = copyTimes[obj]
        else:
            keyTimes = getTransformKeyTimes(obj, animRange)
            
        if keyTimes and fast:
            # Due to a Maya Bug, we first need to check a different arbitrary frame to force the cache to be rebuilt
            getWorldTransform(obj, time=keyTimes[0] - 1)
            if relative:
                getWorldTransform(relativeTo, time=keyTimes[0] - 1)
        
        nodeKeyTimes[obj] = keyTimes
    
    nodeTransforms = {}
    for t in frange(animRange[0], animRange[1] + 1):
        for obj in nodes:
            keyTimes = nodeKeyTimes[obj]
            if keyTimes and t in keyTimes:
                if not fast and cmds.currentTime(q=True) != t:
                    cmds.currentTime(t, e=True)
                keyTime = t if fast else None
                    
                worldMatrix = getWorldTransform(obj, time=keyTime)
                
                if relative:
                    relativeMatrixInverse = getWorldTransform(relativeTo, time=keyTime).inverse()
                    worldMatrix = worldMatrix * relativeMatrixInverse
                
                if obj not in nodeTransforms:
                    nodeTransforms[obj] = {}
                nodeTransforms[obj][t] = worldMatrix
                
                if ":" in obj:
                    # To support using different namespaces, add the node's name without namespace as well
                    # This is done only if there is not already another namespaceless node added with the same name
                    nameWithoutNamespace = "|" + obj.split(":")[-1]
                    if nameWithoutNamespace not in nodeTransforms:
                        nodeTransforms[nameWithoutNamespace] = {}
                    if t not in nodeTransforms[nameWithoutNamespace]:
                        nodeTransforms[nameWithoutNamespace][t] = worldMatrix
    
    return nodeTransforms

def pasteWorldTransform(copiedTransforms, nodes=None, remaps=None, relative=False, start=None, fast=False):
    if nodes == None:
        nodes = list(copiedTransforms.keys())
    
    if relative:
        if len(nodes) < 2:
            raise RuntimeError("Relative mode requires at least 2 nodes must be selected!")
        relativeTo = nodes[-1]
        nodes = nodes[:-1]
    nodes = ControlTagger.SortByHierarchy(nodes)
    
    keyTimes = set()
    for ts in copiedTransforms.values():
        keyTimes.update(ts.keys())
    if not keyTimes:
        return
    
    animStart = min(keyTimes)
    animEnd = max(keyTimes)
    
    with UndoContext("Paste World Transform"):
        originalTime = cmds.currentTime(q=True)
        
        if not fast:
            # The slow mode will paste all the animation on a node before moving to the next one on the hierarchy.
            # This produces better results if the nodes don't have their keys synchronized but will move through the timeline multiple times, thus being slower.
            for copiedTime in frange(animStart, animEnd + 1):
                relativeMatrix = None
                for obj in nodes:
                    target = remaps[obj] if remaps and obj in remaps else obj
                    
                    if target not in copiedTransforms:
                        target = "|" + obj.split(":")[-1]
                    
                    if target in copiedTransforms:
                        keyTimes = copiedTransforms[target]
                        if copiedTime in keyTimes:
                            targetTime = copiedTime if start == None else start + copiedTime - animStart
                            if targetTime != cmds.currentTime(q=True):
                                cmds.currentTime(targetTime, e=True)
                            
                            matrix = keyTimes[copiedTime]
                            if relative:
                                if relativeMatrix is None:
                                    relativeMatrix = getWorldTransform(relativeTo)
                                matrix = matrix * relativeMatrix
                            setWorldTransform(obj, matrix)
        
        else:
            # Fast mode is not reliable and may require multiple pastings to produce the right results.
            # However, the slow mode may also not be reliable on certain rigs and also require multiple pastings.
            for obj in nodes:
                target = remaps[obj] if remaps and obj in remaps else obj
                
                if target not in copiedTransforms:
                    target = "|" + obj.split(":")[-1]
                
                if target in copiedTransforms:
                    keyTimes = copiedTransforms[target]
                    for copiedTime in keyTimes:
                        targetTime = copiedTime if start == None else start + copiedTime - animStart
                        if targetTime != cmds.currentTime(q=True):
                            cmds.currentTime(targetTime, e=True)
                        
                        matrix = keyTimes[copiedTime]
                        if relative:
                            relativeMatrix = getWorldTransform(relativeTo)
                            matrix = matrix * relativeMatrix
                        setWorldTransform(obj, matrix)
          
        cmds.currentTime(originalTime, e=True)

def storeCopiedTransfromsOnFile(copiedTransforms, path=None):
    if path == None:
        path = DEFAULT_FILE_PATH
    
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(copiedTransforms, f, ensure_ascii=False, indent=4, cls=CopiedTransformEncoder)

def loadCopiedTransfromsFromFile(path=None):
    if path == None:
        path = DEFAULT_FILE_PATH
    
    if not os.path.exists(path):
        raise FileNotFoundError("No copied transform information found!")
    
    with open(path, 'r', encoding='utf-8') as f:
        copiedTransforms = json.load(f, cls=CopiedTransformDecoder)
    
    # Due to using JSON for storing the data, the KeyTimes for each object are saved as strings
    # We need to turn them back into numbers
    for obj in copiedTransforms:
        parsed = {}
        for keyTime, value in copiedTransforms[obj].items():
            parsed[float(keyTime)] = value
        copiedTransforms[obj] = parsed
    
    return copiedTransforms


class CopyPasteWorldWindow(MayaQWidgetBaseMixin, QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle("Copy/Paste World")
        
        self.createUI()
        
        self.resize(265, 0) # Min-Height

    def createUI(self):
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setSpacing(4)
        self.setLayout(mainLayout)
        
        relativeFrame = QtWidgets.QGroupBox()
        relativeFrame.setLayout(QtWidgets.QHBoxLayout())
        relativeFrame.layout().setContentsMargins(5, 2, 0, 2)
        mainLayout.addWidget(relativeFrame)
        
        self.absoluteRadioButton = QtWidgets.QRadioButton("Absolute")
        self.absoluteRadioButton.setToolTip("Each object will be pasted at the same position it was copied.")
        relativeFrame.layout().addWidget(self.absoluteRadioButton)
        
        self.relativeRadioButton = QtWidgets.QRadioButton("Relative")
        self.relativeRadioButton.setToolTip("The last selected object will act as a pivot. Each object (except the pivot) will be pasted relative to the pivot.")
        relativeFrame.layout().addWidget(self.relativeRadioButton)
        
        self.absoluteRadioButton.setChecked(True)
        
        copyGroupBox = QtWidgets.QGroupBox("Copy")
        mainLayout.addWidget(copyGroupBox)
        
        copyLayout = QtWidgets.QVBoxLayout()
        copyGroupBox.setLayout(copyLayout)
        
        copyRangeGroupBox = QtWidgets.QGroupBox("Range")
        copyRangeGroupBox.setLayout(QtWidgets.QVBoxLayout())
        copyRangeGroupBox.layout().setContentsMargins(5, 2, 0, 0)
        copyLayout.addWidget(copyRangeGroupBox)
        
        self.selectedRangeRadioButton = QtWidgets.QRadioButton("Selected Range")
        self.selectedRangeRadioButton.setToolTip("Copies the selected range. If no range is selected, only copies the current frame.")
        copyRangeGroupBox.layout().addWidget(self.selectedRangeRadioButton)
        
        self.allKeysRadioButton = QtWidgets.QRadioButton("All Keys")
        self.allKeysRadioButton.setToolTip("Copies all the animated range of each object.")
        copyRangeGroupBox.layout().addWidget(self.allKeysRadioButton)
        
        self.selectedRangeRadioButton.setChecked(True)
        
        self.fastCheckBox = QtWidgets.QCheckBox("Fast")
        self.fastCheckBox.setToolTip("Asks Maya to retrieve the transformation at each frame instead of changing the current time. Some nodes might yield a wrong transformation if this option is enabled.")
        self.fastCheckBox.setChecked(True)
        copyLayout.addWidget(self.fastCheckBox)
        
        self.bakeCheckBox = QtWidgets.QCheckBox("Bake")
        self.bakeCheckBox.setToolTip("Copies the transform on each frame of the selected range instead of only on each object's keys.")
        copyLayout.addWidget(self.bakeCheckBox)
        
        copyButton = QtWidgets.QPushButton("Copy")
        copyButton.clicked.connect(self.onCopyButtonPressed)
        copyButton.setToolTip("<p>Copies the world transformations of the selected objects on the selected range. Use the Paste button to paste this information.</p><ul><li>The copied data can be pasted on a different Maya file (even on a different instance of the program).</li><li>If only one frame is selected, the transform will be copied even if an object doesn't have a key on that frame.</li></ul>")
        copyLayout.addWidget(copyButton)
        
        pasteGroupBox = QtWidgets.QGroupBox("Paste")
        mainLayout.addWidget(pasteGroupBox)
        
        pasteLayout = QtWidgets.QVBoxLayout()
        pasteGroupBox.setLayout(pasteLayout)
        
        pasteStartGroupBox = QtWidgets.QGroupBox("Start")
        pasteStartGroupBox.setLayout(QtWidgets.QVBoxLayout())
        pasteStartGroupBox.layout().setContentsMargins(5, 2, 0, 0)
        pasteLayout.addWidget(pasteStartGroupBox)
        
        self.currentFrameRadioButton = QtWidgets.QRadioButton("Current Frame")
        self.currentFrameRadioButton.setToolTip("Pastes the copied transforms on the current frame. If a range was copied, paste them starting from this frame.")
        pasteStartGroupBox.layout().addWidget(self.currentFrameRadioButton)
        
        self.copiedRangeRadioButton = QtWidgets.QRadioButton("Copied Range")
        self.copiedRangeRadioButton.setToolTip("Pastes the copied transforms on the range they were copied.")
        pasteStartGroupBox.layout().addWidget(self.copiedRangeRadioButton)
        
        self.currentFrameRadioButton.setChecked(True)
        
        pasteButton = QtWidgets.QPushButton("Paste")
        pasteButton.clicked.connect(self.onPasteButtonPressed)
        pasteButton.setToolTip("<p>Pastes the copied world transformations on the selected objects. Use the Copy button to copy this information.</p><ul><li>The transformation will be pasted on the same object it was copied from.</li><li>You can paste the transformation on a node with the same name but different namespace too.</li><li>If only one object was copied, you can paste the transformation on any node, regardless of name.</li></ul>")
        pasteLayout.addWidget(pasteButton)

    def onCopyButtonPressed(self):
        try:
            selection = getSelectedTransforms()
            animRange = getSelectedAnimRange() if self.selectedRangeRadioButton.isChecked() else None
            bake = self.bakeCheckBox.isChecked() or (animRange and animRange[0] == animRange[1])
            fast = self.fastCheckBox.isChecked() and not (animRange and animRange[0] == animRange[1])
            relative = self.relativeRadioButton.isChecked()
        
            copiedTransforms = copyWorldTransform(selection, animRange=animRange, bake=bake, fast=fast, relative=relative)
            storeCopiedTransfromsOnFile(copiedTransforms)
        
        except Exception as ex:
            QtWidgets.QMessageBox.warning(self, "Copy World Transform", str(ex))
            raise ex
        
    def onPasteButtonPressed(self):
        try:
            copiedTransforms = loadCopiedTransfromsFromFile()
            selection = getSelectedTransforms()
            
            relative = self.relativeRadioButton.isChecked()
            remaps = dict({(selection[0], obj) for obj in copiedTransforms}) if len(copiedTransforms) <=2 and len(selection) == (2 if relative else 1) and selection[0] not in copiedTransforms else None
            start = cmds.currentTime(q=True) if self.currentFrameRadioButton.isChecked() else None
        
            pasteWorldTransform(copiedTransforms, nodes=selection, remaps=remaps, start=start, relative=relative)
        
        except Exception as ex:
            QtWidgets.QMessageBox.warning(self, "Paste World Transform", str(ex))
            raise ex


instance = None

def show():
    global instance
    if instance != None and instance.isVisible():
        instance.close()
    
    instance = CopyPasteWorldWindow()
    instance.show()

if __name__ == "__main__":
    show()
