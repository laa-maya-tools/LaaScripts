import ActorManager.AnimPresetHolder as AnimPresetHolder

import maya.cmds as cmds

from NodeCustom.Management.NodeCollection import NodeCollection

import ActorManager.Actor as Actor

from Utils.Maya.UndoContext import UndoContext
import Utils.Maya.Mirror as MirrorUtils
import Utils.Maya as MayaUtils

import ProjectPath
import Exporter

class CameraSet(AnimPresetHolder.AnimPresetHolder, AnimPresetHolder.AnimPresetSubHolder):

    _Type           = "cameraSetActor"
    
    _name           = "name"
    _path           = "path"
    _cameras        = "cameras"
    _cameraLeft     = "cameraLeft"
    _cameraRight    = "cameraRight"
    _actor          = "actor"
    
    
    def getCollectionName(self):
        return self.node
    
    #--------- PROPERTIES
    # Name
    @property
    def name(self):
        return self.getAttr(self._name)
    
    @name.setter
    def name(self, value):
        with UndoContext("Set CameraSet Name"):
            self.setStringAttribute(self._name, value)
            
    # Path
    @property
    def path(self):
        p = self.getAttr(self._path)
        if not p:
            p = ProjectPath.Tokens.curled(ProjectPath.Tokens.TSubActorAnimPath) # The default path will be the selected actor animSubActor's path
        return p
    
    @path.setter
    def path(self, value):
        with UndoContext("Set CameraSet Path"):
            self.setStringAttribute(self._path, value)

    # Actor
    @property
    def actor(self):
        return self.getInputSingle(self._actor, cls=Actor.Actor)
        
    @actor.setter
    def actor(self, inputWrapper): 
        with UndoContext("Set CameraSet Actor"):
            self.setInputWrapper(self._actor, inputWrapper, inputAttribute="message")
    
    # Cameras
    @property
    def cameras(self):
        return self.getCollectionAttribute(self._cameras, NodeCollection)
    
    @cameras.setter
    def cameras(self, value):
        with UndoContext("Set CameraSet Cameras"):
            cameras = self.cameras
            cameras.clear()
            if value:
                cameras += value
    @property
    def cameraLeft(self):
        return self.getInputSingle(self._cameraLeft)
    
    @cameraLeft.setter
    def cameraLeft(self, value):
        with UndoContext("Set CameraSet Left Camera"):
            self.setInputNode(self._cameraLeft, value, inputAttribute="message")
    @property
    def cameraRight(self):
        return self.getInputSingle(self._cameraRight)
    
    @cameraRight.setter
    def cameraRight(self, value):
        with UndoContext("Set CameraSet Right Camera"):
            self.setInputNode(self._cameraRight, value, inputAttribute="message")
    
    #--------- OVERRIDE
    
    def getHolder(self):
        return self
    
    def getPathTokenizer(self, branch="{Game}"):
        if self.actor:
            pathTokenizer = self.actor.animSubActor.getPathTokenizer(branch=branch)
        else:
            pathTokenizer = ProjectPath.PathTokenizer(branch=branch)
        
        # We hijack the animations folder to export on the cameras folder
        pathTokenizer.Update({ ProjectPath.Tokens.TAnimations : "cameras" })
        
        return pathTokenizer
    
    def getAnimPath(self):
        return self.path
    
    def getDisplayName(self):
        return self.name
    
    def onPreExport(self):
        cameras = self.cameras
        cameraLeft = self.cameraLeft
        cameraRight = self.cameraRight
        
        try:
            originalCameraNames = []
            oldCameras = []
            exportCameras = []
            for camera in cameras:
                names = []
                if camera == cameraLeft:
                    names.append("CameraLeft")
                if camera == cameraRight:
                    names.append("CameraRight")
                if not names:
                    names = [None]
                oldCamera = camera
                for name in names:
                    originalCameraNames.append(oldCamera)
                    oldCamera, exportCamera = Exporter.createExportCamera(oldCamera, name=name)
                    oldCameras.append(oldCamera)
                    exportCameras.append(exportCamera)
        except:
            # In case of error, restore the cameras that have been converted
            for i in range(len(exportCameras) - 1, -1, -1): # A single camera might have been renamed multiple times, we need to undo the name renaming in the reverse order.
                Exporter.deleteExportCamera(oldCameras[i], exportCameras[i], originalCameraName=originalCameraNames[i])
            raise
    
        return exportCameras, oldCameras, originalCameraNames
    
    def onPostExport(self, data):
        exportCameras = data[0]
        oldCameras = data[1]
        originalCameraNames = data[2]
        for i in range(len(exportCameras) - 1, -1, -1): # A single camera might have been renamed multiple times, we need to undo the name renaming in the reverse order.
            Exporter.deleteExportCamera(oldCameras[i], exportCameras[i], originalCameraName=originalCameraNames[i])
    
    def getExportNodes(self, data):
        exportCameras = data[0]
        return exportCameras
    
    def mirrorAnimation(self, data):
        #TODO:
        # - Solo mirrorea en la capa actual, habría que replicar el comportamiento del mirror que hace RigManager (o refactorizarlo a un código común)
        # - Si las cámaras están bloqueadas el mirror no tendrá efecto, habría que desbloquearlas antes de mirrorearlas
        exportCameras = list(data[0])   # Duplicate the list to modify the copy
        originalCameras = data[1]
        
        leftCameraIndex = None
        rightCameraIndex = None
        for i, camera in enumerate(exportCameras):
            if leftCameraIndex == None and camera == "CameraLeft":
                leftCameraIndex = i
            elif rightCameraIndex == None and camera == "CameraRight":
                rightCameraIndex = i
        
        # We mirror the original cameras. The export cameras are constrained to them
        MirrorUtils.mirrorControls(originalCameras, keysOption=MirrorUtils.KeysOption.All, mirrorPlane=MirrorUtils.MirrorPlane.XY)
        
        if leftCameraIndex != None and cmds.objExists("CameraRight"):
            rightCameraTempName = MayaUtils.renameCamera("CameraRight", "CameraRight_Temp", autoRenameDuplicated=True)
            if rightCameraIndex != None:
                exportCameras[rightCameraIndex] = rightCameraTempName
        if rightCameraIndex != None and cmds.objExists("CameraLeft"):
            leftCameraTempName = MayaUtils.renameCamera("CameraLeft", "CameraLeft_Temp", autoRenameDuplicated=True)
            if leftCameraIndex != None:
                exportCameras[leftCameraIndex] = leftCameraTempName
        
        if leftCameraIndex != None:
            exportCameras[leftCameraIndex] = MayaUtils.renameCamera(exportCameras[leftCameraIndex], "CameraRight")
        if rightCameraIndex != None:
            exportCameras[rightCameraIndex] = MayaUtils.renameCamera(exportCameras[rightCameraIndex], "CameraLeft")
        
        return exportCameras, data[1], data[2]
    
    def getExportFileType(self):
        return Exporter.EXPORTER_CAMERA_FILE_TYPE
    