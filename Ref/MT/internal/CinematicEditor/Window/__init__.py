from PySide2 import QtWidgets, QtGui

import maya.api.OpenMaya as OpenMaya

import maya.cmds as cmds
import maya.mel as mel

from QtCustomWidgets.UIFileWidget import UIFileWidget
from QtCustomWidgets.ColorPickerButton import ColorPickerButton

import AnimSystems.Noise as Noise

from Utils.Maya.UndoContext import UndoContext
import Utils.Maya as MayaUtils

import random
import functools

# ------------------------------------
# | Instance                         |
# ------------------------------------

instance = None

def show():
    global instance
    if isVisible():
        instance.close()
    
    from .CinematicEditorMainWindow import CinematicEditorMainwindow
    instance = CinematicEditorMainwindow()
    instance.show()
    
def isVisible():
    global instance
    return instance != None and instance.isVisible()

# ------------------------------------
# | Color Methods                    |
# ------------------------------------

def getRandomColor(distinctFrom=[]):
    distinctHues = [int(c.hue()) for c in distinctFrom]
    hue = None
    while hue == None or hue in distinctHues:
        hue = 60 * random.randint(0, 5)
    return QtGui.QColor.fromHsl(hue, 64, 153)

def colorAsTuple(color):
    return (color.red(), color.green(), color.blue())

def tupleAsColor(tuple):
    return QtGui.QColor(tuple[0], tuple[1], tuple[2])

# ------------------------------------
# | UI Methods                       |
# ------------------------------------

tooltipTemplate = "{preffix}<h3 style=\"color:{color};\">({index}) {delegatedStatus}{name}</h3><p>{description}</p><p>Camera: <b>{camera}</b><br>Start: <b>{start}</b><br>End: <b>{end}</b></b><br>Duration: <b>{duration}</b></p>{overlaps}{suffix}"
tooltipOverlapsTemplate = "<b style=\"color:red;\">Overlaps with:</b><ul style=\"margin-left: 10px; margin-top: 2px; -qt-list-indent: 0;\">{overlaps}</ul>"
 
def getShotTooltip(shot, preffix="", suffix="", shotOverlaps=None, owned=True):
    if shotOverlaps == None:
        shotOverlaps = shot.getCutscene().getShotOverlaps(shot)
    
    colorStr = "rgb{}".format(shot.color)
    indexStr = shot.getCutscene().getShotIndex(shot) + 1
    delegatedStatusStr = "<i>[NOT OWNED]</i> " if not owned else ""
    descriptionStr = shot.description or ""
    overlaps = ["<li>{}</li>".format(shotOverlap.shotName) for shotOverlap in shotOverlaps]
    overlapsStr = tooltipOverlapsTemplate.format(overlaps="".join(overlaps)) if overlaps else ""
    tooltip = tooltipTemplate.format(color=colorStr, index=indexStr, delegatedStatus=delegatedStatusStr, name=shot.shotName, description=descriptionStr, camera=shot.camera, start=shot.start, end=shot.end, duration = shot.getDuration(), overlaps=overlapsStr, preffix=preffix, suffix=suffix)
    
    return tooltip

# ------------------------------------
# | Camera Methods                   |
# ------------------------------------

CAMERA_ATTRIBUTE_CATEGORY = "CinematicEditor"

def createCamera(targetCamera=False, configureDefaults=True, connectShape=True, addNoise=True, addFrustrum=False, select=True):
    with UndoContext("Create Cinematic Camera"):
        activeViewport = cmds.playblast(ae=True).split("|")[-1]
        viewportCamera = cmds.modelPanel(activeViewport, q=True, camera=True)
        
        newCamera = cmds.duplicate(viewportCamera)[0]   # Duplicating the camera this way will only copy the current state and not it's animations. The duplicated camera will be a Free Camera.
        cmds.camera(newCamera, e=True, lockTransform=False)
        cmds.showHidden(newCamera)
        if cmds.listRelatives(newCamera, parent=True):
            cmds.parent(newCamera, world=True)
        
        newCameraName = "DC_Cam001"
        count = 1
        while cmds.objExists(newCameraName):
            count += 1
            newCameraName = "DC_Cam{}".format(str(count).zfill(3))
        newCamera = cmds.rename(newCamera, newCameraName)
        cameraShape = cmds.listRelatives(newCamera, children=True, shapes=True, type="camera")[0]
        
        if targetCamera:
            mel.eval("cameraMakeNode 2 {}".format(newCamera)) # This will transform the camera into a Target Camera.
            
            # Changes the shape of the target. By default it doesn't really have one, it only shows it's Rotate Pivot.
            targetNode = MayaUtils.getLookAtTargetNode(MayaUtils.getCameraLookAtNode(newCamera))
            cmds.setAttr("{}.displayRotatePivot".format(targetNode), 0)
            targetShape = cmds.listRelatives(targetNode, shapes=True)[0]
            cmds.delete(targetShape)
            targetShape = cmds.createNode("PointLocator", parent=targetNode, name=targetShape)
            cmds.setAttr("{}.size".format(targetShape), 10)
            cmds.setAttr("{}.cube".format(targetShape), 0)
            cmds.setAttr("{}.sphere".format(targetShape), 1)
            
            for coord in ["X", "Y", "Z"]:
                # Por alguna razón no funciona si no se ejecuta con evalDeferred
                cmds.evalDeferred(functools.partial(cmds.setAttr, "{}.rotate{}".format(newCamera, coord), e=True, k=False, cb=True))  # This is done to prevent the camera from being added to AnimLayers
            
        if configureDefaults:
            configureCinematicCamera(newCamera, cameraShape, rotateOrder=(0 if targetCamera else 2), pivotInPlaceMode=(not targetCamera))
        
        if connectShape:
            connectShapeToCamera(newCamera, cameraShape, attrs=["focalLength"])
            if targetCamera:
                cameraGroup = cmds.listRelatives(newCamera, parent=True)[0]
                connectShapeToCamera(newCamera, cameraGroup, attrs=["twist"])
        
        if addNoise:
            Noise.addNoiseToTransform(newCamera, rotation=True)
            
        if addFrustrum:
            connectFrustrum(newCamera, cameraShape, coneSize=200)
            
        if select:
            cmds.select(newCamera)
        
        return newCamera
    
def configureCinematicCamera(cameraTransform, cameraShape, rotateOrder=2, undoableMovements=True, displayGate=True, filmFit="overscan", aspectRatio=16.0/9.0, overscan=1.0, lockOverscan=True, pivotInPlaceMode=None):
    with UndoContext("Configure Cinematic Camera"):
        cmds.camera(cameraShape, e=True,
                    journalCommand=undoableMovements,
                    displayResolution=displayGate,
                    displayGateMask=displayGate,
                    overscan=overscan,
                    filmFit=filmFit,
                    aspectRatio=aspectRatio
                    )
        
        cmds.setAttr("{}.rotateOrder".format(cameraTransform), rotateOrder) # 2 = ZXY
        
        cmds.setAttr("{}.locatorScale".format(cameraShape), 20)
        
        if lockOverscan:
            cmds.setAttr("{}.overscan".format(cameraShape), e=True, lock=True)
        
        if pivotInPlaceMode != None:
            setCameraPivotInPlaceMode(cameraShape, pivotInPlaceMode, changePivot=False)

def connectShapeToCamera(camera, target, attrs=[]):
    if attrs:
        separatorAttr = "shapeConnectSeparatorAttr"
        if not cmds.attributeQuery(separatorAttr, n=camera, ex=True):
            cmds.addAttr(camera, longName=separatorAttr, niceName="Shape", at="enum", enumName="------", dv=0, k=False, r=False, category=CAMERA_ATTRIBUTE_CATEGORY)
            cmds.setAttr("{}.{}".format(camera, separatorAttr), e=True, channelBox=True)
        
        for attr in attrs:
            if not cmds.attributeQuery(attr, n=camera, ex=True):
                cmds.addAttr(camera, ln=attr, proxy="{}.{}".format(target, attr), dcb=2, category=CAMERA_ATTRIBUTE_CATEGORY)
            else:
                cmds.connectAttr("{}.{}".format(target, attr), "{}.{}".format(camera, attr), force=True)

def isCameraPivotInPlaceMode(cameraShape):
    return cmds.getAttr("{}.usePivotAsLocalSpace".format(cameraShape))

def setCameraPivotInPlaceMode(cameraShape, pivotInPlaceMode, changePivot=True):
        cmds.setAttr("{}.usePivotAsLocalSpace".format(cameraShape), pivotInPlaceMode)
        
        if pivotInPlaceMode:
            cmds.setAttr("{}.tumblePivot".format(cameraShape), 0, 0, 0, type="double3")
            
        elif changePivot:
            selectionList = OpenMaya.MGlobal.getActiveSelectionList()
            boundingBox = None
            for i in range(selectionList.length()):
                mObject = selectionList.getDependNode(i)
                if mObject.hasFn(OpenMaya.MFn.kDagNode):
                    fn = OpenMaya.MFnDagNode(mObject)
                    if boundingBox == None:
                        boundingBox = OpenMaya.MBoundingBox()
                    boundingBox.expand(fn.boundingBox)
                    
            if boundingBox != None:
                pivot = boundingBox.center
                cmds.setAttr("{}.tumblePivot".format(cameraShape), pivot.x, pivot.y, pivot.z, type="double3")

def connectFrustrum(camera, cameraShape, frustrum=None, coneSize=None):
    if frustrum == None:
        frustrum = cmds.createNode("CameraFrustrum", parent=camera, skipSelect=True)
    else:
        cmds.parent(frustrum, camera, shape=True, relative=True)
    
    for attr in ["focalLength", "horizontalFilmAperture", "verticalFilmAperture"]:
        cmds.connectAttr("{}.{}".format(cameraShape, attr), "{}.{}".format(frustrum, attr))
        
    if coneSize != None:
        cmds.setAttr("{}.coneSize".format(frustrum), coneSize)

def isCinematicCamera(camera):
    if cmds.nodeType(camera) == "camera":
        camera = cmds.listRelatives(camera, parent=True)[0]
    messageConnections = cmds.listConnections("{}.message".format(camera), type="cutsceneShot") or None
    return messageConnections != None

# ------------------------------------
# | Edit Shot Dialog                 |
# ------------------------------------

class EditShotDialog(QtWidgets.QDialog):
    
    NO_CAMERA = "<No Camera>"
    NEW_FREE_CAMERA = "New Free Camera"
    NEW_TARGET_CAMERA = "New Target Camera"
    
    def __init__(self, shot, shotBeingCreated=False, color=False, name=False, description=False, camera=False, start=False, end=False, title="Edit Shot", parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        
        self.shot = shot
        self.shotBeingCreated = shotBeingCreated
        self.color = color
        self.name = name
        self.description = description
        self.camera = camera
        self.start = start
        self.end = end
        
        self.setWindowTitle(title)
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        uiWidget = UIFileWidget(r"CinematicEditor/Window/ui/EditShotDialog.ui", parent=self)
        layout.addWidget(uiWidget)
        self.ui = uiWidget.ui
        
        self.colorPickerButton = ColorPickerButton()
        self.ui.colorFieldContainer.layout().addWidget(self.colorPickerButton)
        
        self.ui.okButton.clicked.connect(self.onOKButtonClicked)
        self.ui.cancelButton.clicked.connect(self.onCancelButtonClicked)

    def addSeparatorToComboBox(self, comboBox, width=2):
        for _ in range(width):
            comboBox.insertSeparator(comboBox.count())

    def updateCamerasComboBox(self):
        sceneCameras = cmds.ls(type="camera")
        sceneCameras = [cmds.listRelatives(camera, parent=True, type="transform")[0] for camera in sceneCameras]
        dcCameras = []
        otherCameras = []
        for camera in sceneCameras:
            if camera.startswith("DC_Cam"):
                dcCameras.append(camera)
            else:
                otherCameras.append(camera)
        
        self.ui.cameraComboBox.clear()
        self.ui.cameraComboBox.addItem(self.NO_CAMERA)
        self.addSeparatorToComboBox(self.ui.cameraComboBox)
        self.ui.cameraComboBox.addItem(self.NEW_FREE_CAMERA)
        self.ui.cameraComboBox.addItem(self.NEW_TARGET_CAMERA)
        
        if len(dcCameras) > 0:
            self.addSeparatorToComboBox(self.ui.cameraComboBox)
            dcCameras.sort()
            for camera in dcCameras:
                self.ui.cameraComboBox.addItem(camera)
        
        if len(otherCameras) > 0:
            self.addSeparatorToComboBox(self.ui.cameraComboBox)
            otherCameras.sort()
            for camera in otherCameras:
                self.ui.cameraComboBox.addItem(camera)

    def showEvent(self, event):
        self.updateCamerasComboBox()
        
        self.colorPickerButton.setColor(tupleAsColor(self.shot.color))
        
        self.ui.nameText.setText(self.shot.shotName)
        
        self.ui.descriptionText.setText(self.shot.description)
        
        camera = self.shot.camera
        if camera == None:
            if self.shotBeingCreated:
                self.ui.cameraComboBox.setCurrentText(self.NEW_FREE_CAMERA)
            else:
                self.ui.cameraComboBox.setCurrentText(self.NO_CAMERA)
        else:
            self.ui.cameraComboBox.setCurrentText(camera)
        
        self.ui.startSpinBox.setValue(self.shot.start)
        
        self.ui.endSpinBox.setValue(self.shot.end)
        
        self.ui.colorFieldContainer.setVisible(self.color)
        self.ui.nameFieldContainer.setVisible(self.name)
        self.ui.descriptionFieldContainer.setVisible(self.description)
        self.ui.cameraFieldContainer.setVisible(self.camera)
        self.ui.startFieldContainer.setVisible(self.start)
        self.ui.endFieldContainer.setVisible(self.end)
        
        if self.description:
            self.setMinimumHeight(self.ui.height())
        else:
            self.setFixedHeight(self.ui.height() - self.ui.descriptionFieldContainer.height())
        
        self.ui.okButton.setFocus()
        
    def onOKButtonClicked(self):
        newShotName = self.ui.nameText.text()
        shots = self.shot.getCutscene().getShots()
        for shot in shots:
            if shot != self.shot and shot.shotName == newShotName:
                QtWidgets.QMessageBox.warning(self, "Edit Shot", "There is another shot named {}. Please choose a different name.".format(newShotName))
                return
        
        with UndoContext("Edit Shot"):
            self.shot.color = colorAsTuple(self.colorPickerButton.getColor())
            
            self.shot.shotName = newShotName
            
            self.shot.description = self.ui.descriptionText.toPlainText()
            
            selectedCamera = self.ui.cameraComboBox.currentText()
            if selectedCamera == self.NO_CAMERA:
                self.shot.camera = None
            elif selectedCamera == self.NEW_FREE_CAMERA:
                self.shot.camera = createCamera(targetCamera=False)
            elif selectedCamera == self.NEW_TARGET_CAMERA:
                self.shot.camera = createCamera(targetCamera=True)
            else:
                self.shot.camera = selectedCamera
                
            self.shot.start = self.ui.startSpinBox.value()
            
            self.shot.end = self.ui.endSpinBox.value()
        
        self.accept()

    def onCancelButtonClicked(self):
        self.reject()
