import maya.cmds as cmds

import maya.api.OpenMaya as OpenMaya

import CinematicEditor.Cutscene as Cutscene
import CinematicEditor.Shot as Shot

import CinematicEditor.Window as CinematicEditorUtils

import ActorManager
import ProjectPath
import ScreenDrawer

from Utils.Maya.UndoContext import UndoOff

import P4.Tools as P4Tools

import xml.etree.ElementTree as XML

import os
import sys
import shutil
import tempfile
import subprocess

from Utils.Maya.OptionVar import OptionVarConfiguration

MASTERSLAVEFILE_PATH = "MasterSlave"
MASTERSLAVEFILE_NAME = "MasterSlave.xml"

MASTERSLAVE_CAMERA_NAME = "MasterSlaveCamera"

PREVIEW_PATH = "Playblast"
PREVIEW_CACHE_PATH = os.path.join(tempfile.gettempdir(), "Maya", "CinematicEditor", "MasterSlave", "PreviewCache")

FFMPEG_PATH = os.path.join(ProjectPath.getExternalFolder(), "FFMpeg", "ffmpeg.exe")
FFPROBE_PATH = os.path.join(ProjectPath.getExternalFolder(), "FFMpeg", "ffprobe.exe")

MASTERSLAVE_OVERLAY_ENABLED_OPTIONVAR = OptionVarConfiguration("MasterSlaveOverlayEnabled", "CINEMATIC_EDITOR_MASTERSLAVE_OVERLAY_ENABLED", OptionVarConfiguration.TYPE_INTEGER, True)  # Default is Enabled

class MasterSlaveScreenDrawer(ScreenDrawer.ScreenDrawer):
    
    NOT_OWNED_TEXT = "NOT OWNED"
    
    class Data(object):
        def __init__(self, masterSlaveScreenDrawer, cameraPath, frameContext):
            self.enabled = masterSlaveScreenDrawer.enabled
            if not self.enabled:
                return
            
            self.enabled = CinematicEditorUtils.isVisible()
            if not self.enabled:
                return
            
            masterSlaveFile = CinematicEditorUtils.instance.cachedMasterSlaveFile
            self.enabled = masterSlaveFile != None and masterSlaveFile.exists()
            if not self.enabled:
                return
            
            masterSlaveCamera = masterSlaveFile.getMasterSlaveCamera(createIfNotExists=False)
            self.enabled = masterSlaveCamera != None and cameraPath.fullPathName() == cmds.ls(cmds.listRelatives(masterSlaveCamera, shapes=True, type="camera"), long=True)[0]
            if not self.enabled:
                return
            
            currentShot = CinematicEditorUtils.instance.cinematicEditorTimeline.getCurrentShot()
            self.currentShotOwned = currentShot != None and masterSlaveFile.ownsShot(currentShot)
            
            self.color = OpenMaya.MColor((1, 0, 0, 1))
            self.fontSize = 16
            
            self.dimensions = ScreenDrawer.ScreenDrawerManager.getCameraRect(cameraPath, frameContext)
            
    @property
    def enabled(self):
        return MASTERSLAVE_OVERLAY_ENABLED_OPTIONVAR.value
    
    @enabled.setter
    def enabled(self, v):
        MASTERSLAVE_OVERLAY_ENABLED_OPTIONVAR.value = v
        
        cmds.refresh(force=True)
    
    def prepareForDraw(self, objPath, cameraPath, frameContext):
        return MasterSlaveScreenDrawer.Data(self, cameraPath, frameContext)
    
    def addUIDrawables(self, objPath, drawManager, frameContext, data):
        if data.enabled:
            drawManager.beginDrawable()
            
            drawManager.setColor(data.color)
            drawManager.setFontSize(data.fontSize)
            
            if not data.currentShotOwned:
                drawManager.text2d(OpenMaya.MPoint(data.dimensions[0] + 5, data.dimensions[1] + 5), MasterSlaveScreenDrawer.NOT_OWNED_TEXT)
            
            drawManager.endDrawable()


class MasterSlaveFile(object):
    
    UPDATE_STATUS_NOT_IN_DEPOT = "not_in_depot"
    UPDATE_STATUS_SYNC = "sync"
    UPDATE_STATUS_UNSYNC = "unsync"
    UPDATE_STATUS_UNSYNC_CHECKOUT = "unsync_checkout"
    
    def __init__(self, cutscene : Cutscene.Cutscene):
        self.cutscene : Cutscene.Cutscene = cutscene
        
        self.delegatedShots : dict[Shot.Shot, int] = {}
        self.shotDurations : dict[str, int] = {}
    
    @property
    def masterID(self):
        return 0    # Right now the master ID is fixed. A cutscene instance with ID 0 is considered the master.
    
    # Main -------------------------
    
    # Returns wether or not exists a Master-Slave file for the cutscene.
    # If checkPerforce is True, it will consider it to exist if it is Perforce, regradless of any local file.
    def exists(self, checkPerforce=False):
        path = self.getMasterFilePath()
        if not path:
            return False
        
        p4File = P4Tools.P4File(path)
        if checkPerforce:
            if not p4File.isFileUnderPerforcePath():
                return False
            if p4File.isFileInDepot():
                return True
        return p4File.doesLocalFileExist()
    
    # Returns if the current file is the Master of the Cutscene.
    # If id is provided, the file with that id will be checked instead of the current one.
    def isMaster(self, id : "int|None" = None):
        if id == None:
            id = self.cutscene.masterSlaveID
        return id == self.masterID
    
    # Returns if the current file is a Slave of the Cutscene.
    # If id is provided, the file with that id will be checked instead of the current one.
    def isSlave(self, id : "int|None" = None):
        if id == None:
            id = self.cutscene.masterSlaveID
        return id == -2 or id > 0 # and self.cutscene.masterSlaveID != self.masterID
    
    # Generates a new Master-Slave ID for the cutscene.
    # Used when a Slave claims a Shot to identify itself.
    def generateNewID(self):
        ids = self.delegatedShots.values()
        if not ids:
            newId = -1
        else:
            newId = max(ids) + 1
            if newId == 0:
                newId = 1
            
        if newId <= 0 or newId in ids:
            raise AssertionError("Something went wrong when generating a new ID!")
        
        return newId
    
    # The current file becomes the Master of the cutscene.
    def becomeMaster(self):
        self.cutscene.masterSlaveID = self.masterID
        
        self.delegatedShots = {}
        
        self.saveMasterFile()
    
    # The current file becomes a Slave to the cutscene.
    def becomeSlave(self):
        self.cutscene.masterSlaveID = -2    # An ID of -2 indicates a Slave file with no claimed Shots.
    
    # Frees the file from the master-slave system, deleting the MasterSlaveCamera and clearing it's MasterSlaveID.
    # It may also clear the cutscene path so this file won't interfere with the other ones.
    def becomeFree(self, clearPath=False):
        # Clears the path. This is usually done to free a file without affecting others.
        if clearPath:
            self.cutscene.path = ""
        
        self.cutscene.masterSlaveID = -1    # And ID of -1 indicates a file not affected by the Master-Slave system.
        
        # Deletes the MasterSlaveCamera (and the ImagePlanes with it)
        masterSlaveCamera = self.getMasterSlaveCamera(createIfNotExists=False)
        if masterSlaveCamera:
            cmds.delete(masterSlaveCamera)
    
    # Makes a Slave the Master for the cutscene.
    def overrideMaster(self):
        if not self.isSlave():
            raise AssertionError("Only Slave files can override the Master!")
        
        ownedShots = self.getOwnedShots()
        self.cutscene.masterSlaveID = self.masterID
        self.claimShots(ownedShots, save=True)
    
    # Makes a Slave identify itself as another Slave.
    # Both Slaves will be considered the same and all the Shots' claimed by this file will be added to the other one.
    def overrideSlave(self, newID : int):
        if not self.isSlave():
            raise AssertionError("Only Slave files can override another Slave!")
        
        if newID not in self.getSlaveIDs():
            raise AssertionError("The provided Slave ID doesn't exist!")
        
        ownedShots = self.getOwnedShots()
        for shot in ownedShots:
            self.delegatedShots[shot] = newID
        self.cutscene.masterSlaveID = newID
    
    # Releases the cutscene, reverting it to a normal cutscene without Master nor Slaves.
    def release(self):
        # Removes all the files
        self.deleteFile(self.getMasterFilePath())
        for shot in self.delegatedShots:
            self.deleteDelegatedShotFile(shot)
        
        self.becomeFree(clearPath=False)
    
    # Checks if a Shot is delegated.
    def isShotDelegated(self, shot : Shot.Shot):
        return shot in self.delegatedShots
    
    # Checks if a delegated Shot has been claimed by a Slave.
    # NOTE: This method will raise an exception if the provided shot has not been delegated.
    def isShotClaimed(self, shot : Shot.Shot):
        if not self.isShotDelegated(shot):
            raise AssertionError("Only Delegated shots can be claimed!")
        
        return self.delegatedShots[shot] > 0
    
    # Checks if the current file owns the provided Shot.
    # Masters owns every non-delegated Shots.
    # Slaves owns the delegated Shot's they have claimed.
    def ownsShot(self, shot : Shot.Shot):
        if self.isShotDelegated(shot):
            return self.delegatedShots[shot] == self.cutscene.masterSlaveID
        else:
            return self.isMaster()
    
    # Returns the Shot's owned by this file.
    # See the method ownsShot for details about owning shots.
    def getOwnedShots(self, id : "int|None" = None):
        if id == None:
            id = self.cutscene.masterSlaveID
            
        delegatedShots = [shot for shot, ownerID in self.delegatedShots.items() if ownerID == id]
        
        if self.isMaster(id=id):
            shots = self.cutscene.getEnabledShots()
            for delegatedShot in delegatedShots:
                shots.remove(delegatedShot)
            return shots
        
        elif self.isSlave(id=id):
            return delegatedShots
    
    # Returns the IDs for all the Slaves that have claimed Shots.
    def getSlaveIDs(self):
        ids = set(self.delegatedShots.values())
        if -1 in ids:
            ids.remove(-1)
        return ids
    
    # Delegates a Shot.
    # The Master can call this function to delegate a non-delegated Shot.
    # A Slave can call this function to free a Shot they had claimed.
    def delegateShot(self, shot : Shot.Shot, save=True):
        self.delegateShots([shot], save=save)
    
    # Delegates multiple Shots.
    def delegateShots(self, shots : "list[Shot.Shot]", save=True):
        for shot in shots:
            if not shot.enabled:
                raise AssertionError("Only Enabled shots can be delegated!")
            if not self.ownsShot(shot):
                raise AssertionError("You can't delegate a shot you don't own!")
        
        masterSlaveCamera = self.getMasterSlaveCamera()
        for shot in shots:
            self.delegatedShots[shot] = -1
            shot.camera = masterSlaveCamera
            self.cacheShotPreview(shot.shotName)
        
        if save:
            if self.isMaster():
                self.saveMasterFile()
            for shot in shots:
                self.saveDelegatedShotFile(shot)
    
    # Claims a delegated Shot.
    # The Master can call this funcion to reclaim a delegated Shot so it is no longer delegated.
    # A Slave can call this function to claim a delegated Shot.
    def claimShot(self, shot : Shot.Shot, save=True):
        self.claimShots([shot], save=save)
    
    # Claims multiple Shot.
    def claimShots(self, shots : "list[Shot.Shot]", save=True):
        if not self.isMaster():
            for shot in shots:
                if self.isShotClaimed(shot):
                    raise AssertionError("The shot has already been claimed!")
        
        if self.isMaster():
            for shot in shots:
                self.delegatedShots.pop(shot)
                shot.camera = None
                if save:
                    self.deleteDelegatedShotFile(shot)
            if save:
                self.saveMasterFile()
        
        elif self.isSlave():
            if self.cutscene.masterSlaveID == -2:
                self.cutscene.masterSlaveID = self.generateNewID()
            
            for shot in shots:
                self.delegatedShots[shot] = self.cutscene.masterSlaveID
                shot.camera = None
                if save:
                    self.saveDelegatedShotFile(shot)
            
        else:
            raise AssertionError("Attempting to claim a Shot when the file is neither a Master nor a Slave!")   
    
    # Master-Slave Files --------------
    
    # Returns the path to the Master file.
    def getMasterFilePath(self):
        if not self.cutscene.path:
            return None
        cutscenePath = self.cutscene.getPathTokenizer(branch="{3D}").Translate(self.cutscene.path)
        return os.path.join(cutscenePath, MASTERSLAVEFILE_PATH, MASTERSLAVEFILE_NAME)

    # Returns the path to the provided delegated Shot's file.
    def getDelegatedShotFilePath(self, shotName : str):
        cutscenePath = self.cutscene.getPathTokenizer(branch="{3D}").Translate(self.cutscene.path)
        return os.path.join(cutscenePath, MASTERSLAVEFILE_PATH, "{}.xml".format(shotName))
    
    # Returns both the Master file path and all the delegated Shots' file paths.
    def getFilePaths(self):
        files = [self.getMasterFilePath()]
        for shot in self.delegatedShots.keys():
            files.append(self.getDelegatedShotFilePath(shot.shotName))
        return files
    
    # Returns the update status for the provided files. A single status is returned, the highest priority one.
    # * If there is a file which is checked out and is not synced, "unsync_checkout" will be returned.
    # * Else, if there is a file which is not synced, "unsync" will be returned.
    # * Else, if there is a file which is not in Perforce, "not_in_depot" will be returned.
    # * Else, "sync" is returned.
    def getUpdateStatus(self, files : "list[str]"):
        statuses = set()
        for file in files:
            p4File = P4Tools.P4File(file)
            if not file or not p4File.isFileInDepot():
                statuses.add(self.UPDATE_STATUS_NOT_IN_DEPOT)
            elif p4File.isFileLastRevision():
                statuses.add(self.UPDATE_STATUS_SYNC)
            elif p4File.isFileCheckedOut():
                statuses.add(self.UPDATE_STATUS_UNSYNC_CHECKOUT)
            else:
                statuses.add(self.UPDATE_STATUS_UNSYNC)
        
        if self.UPDATE_STATUS_UNSYNC_CHECKOUT in statuses:
            return self.UPDATE_STATUS_UNSYNC_CHECKOUT
        elif self.UPDATE_STATUS_UNSYNC in statuses:
            return self.UPDATE_STATUS_UNSYNC
        elif self.UPDATE_STATUS_NOT_IN_DEPOT in statuses:
            return self.UPDATE_STATUS_NOT_IN_DEPOT
        elif self.UPDATE_STATUS_SYNC in statuses:
            return self.UPDATE_STATUS_SYNC
        else:
            raise AssertionError("Unkown Update State")
    
    # Checks if all the Master-Slave files are up-to-date.
    # If the files are not even on Perforce they will be considered up-to-date too.
    def isUpdated(self):
        files = self.getFilePaths()
        
        status = self.getUpdateStatus(files)
        return status == self.UPDATE_STATUS_SYNC or status == self.UPDATE_STATUS_NOT_IN_DEPOT 
    
    # Gets the lastest revision for all the Master-Slave files.
    def syncFiles(self):
        files = self.getFilePaths()
        for file in files:
            if file:
                p4File = P4Tools.P4File(file)
                if p4File.isFileInDepot():
                    p4File.syncFile()
    
    # Returns the file path for the current Maya file.
    def getCurrentMayaFilePath(self) -> str:
        return cmds.file(q=True, sn=True)
    
    # Returns the current Windows user.
    def getCurrentUser(self):
        return os.getlogin()
    
    # Saves the Master file.
    # The Master file includes a list of all the Shots, indicating which are enabled and which are delegated.
    # It also includes a list of all the Actors.
    def saveMasterFile(self, checkout=True, revertIfUnchanged=True):
        p4File = P4Tools.P4File(self.getMasterFilePath())
        if checkout:
            if not p4File.isFileUnderPerforcePath():
                raise AssertionError("Cutscene path not under Perforce Path!")
            p4File.smartCheckout()
        elif p4File.doesLocalFileExist() and p4File.isLocalFileReadOnly():
            raise AssertionError("Unable to save the Master file: The file already exists and is marked as read-only!")
        
        rootElement = XML.Element("MasterSlave")
        rootElement.attrib["cutscene"] = self.cutscene.getCutsceneName()
        rootElement.attrib["path"] = self.cutscene.getPathTokenizer().Translate(self.cutscene.path)
        
        masterElement = XML.Element("Master")
        rootElement.append(masterElement)
        
        masterIdElement = XML.Element("ID")
        masterElement.append(masterIdElement)
        masterIdElement.text = str(self.masterID)
        
        masterOwnersElement = XML.Element("Owners")
        masterElement.append(masterOwnersElement)
        
        ownerElement = XML.Element("Owner")
        masterOwnersElement.append(ownerElement)
        ownerElement.attrib["user"] = self.getCurrentUser()
        ownerElement.attrib["file"] = self.getCurrentMayaFilePath()
        
        cutsceneRootElement = XML.Element("CutsceneRoot")
        rootElement.append(cutsceneRootElement)
        with UndoOff():
            currentTime = cmds.currentTime(q=True)
            cmds.currentTime(0, e=True)
            cutsceneRootPos = cmds.xform(self.cutscene.cutsceneRoot, q=True, translation=True, worldSpace=True)
            cmds.currentTime(currentTime, e=True)
        cutsceneRootElement.attrib["x"] = str(cutsceneRootPos[0])
        cutsceneRootElement.attrib["y"] = str(cutsceneRootPos[1])
        cutsceneRootElement.attrib["z"] = str(cutsceneRootPos[2])
        
        shotsElement = XML.Element("Shots")
        rootElement.append(shotsElement)
        
        cutsceneShots = self.cutscene.getShots()
        for shot in cutsceneShots:
            shotElement = XML.Element("Shot")
            shotsElement.append(shotElement)
            shotElement.text = shot.shotName
            shotElement.attrib["description"] = shot.description or ""
            shotElement.attrib["enabled"] = str(shot.enabled)
            shotElement.attrib["delegated"] = str(shot in self.delegatedShots)
        
        actorsElement = XML.Element("Actors")
        rootElement.append(actorsElement)
        
        pathTokenizer = ProjectPath.PathTokenizer(branch="{3D}")
        cutsceneActors = self.cutscene.getCutsceneActors(nonRemapped=True)
        for cutsceneActor in cutsceneActors:
            actorElement = XML.Element("Actor")
            actorsElement.append(actorElement)
            actorElement.text = cutsceneActor.actor.getNamespace()
            actorElement.attrib["file"] = pathTokenizer.Tokenize(cutsceneActor.actor.getReferenceFile())
            
        xmlTree = XML.ElementTree(rootElement)
        with open(p4File.file, "wb") as file:
            xmlTree.write(file)
            
        if checkout and revertIfUnchanged:
            if p4File.isFileInDepot():
                p4File.revertFile(onlyUnchanged=True)
    
    # Saves the Slave file for a delegated Shot.
    # It only includes the ID of the file that owns it. An ID of -1 indicates it is not owned by any Slave.
    def saveDelegatedShotFile(self, shot : Shot.Shot, checkout=True, revertIfUnchanged=True):
        if shot not in self.delegatedShots:
            raise AssertionError("Shot not delegated!")
        
        p4File = P4Tools.P4File(self.getDelegatedShotFilePath(shot.shotName))
        if checkout:
            if not p4File.isFileUnderPerforcePath():
                raise AssertionError("Cutscene path not under Perforce Path!")
            p4File.smartCheckout()
        elif p4File.doesLocalFileExist() and p4File.isLocalFileReadOnly():
            raise AssertionError("Unable to save the Slave file: The file already exists and is marked as read-only!")
        
        rootElement = XML.Element("DelegatedShot")
        rootElement.attrib["cutscene"] = self.cutscene.getCutsceneName()
        rootElement.attrib["path"] = self.cutscene.getPathTokenizer().Translate(self.cutscene.path)
         
        shotNameElement = XML.Element("ShotName")
        rootElement.append(shotNameElement)
        shotNameElement.text = shot.shotName
        
        slaveIdElement = XML.Element("SlaveID")
        rootElement.append(slaveIdElement)
        slaveIdElement.text = str(self.delegatedShots[shot])
        
        ownersElement = XML.Element("Owners")
        rootElement.append(ownersElement)
        
        ownerElement = XML.Element("Owner")
        ownersElement.append(ownerElement)
        ownerElement.attrib["user"] = self.getCurrentUser()
        ownerElement.attrib["file"] = self.getCurrentMayaFilePath()
        
        xmlTree = XML.ElementTree(rootElement)
        with open(p4File.file, "wb") as file:
            xmlTree.write(file)
            
        if checkout and revertIfUnchanged:
            if p4File.isFileInDepot():
                p4File.revertFile(onlyUnchanged=True)
    
    # Deletes a file. If checkout is True, deletes it on Perforce.
    def deleteFile(self, path : str, checkout=True):
        p4File = P4Tools.P4File(path)
        if checkout:
            p4File.markFileForDelete(deleteLocalIfNotInDepot=True)
        else:
            p4File.deleteLocalFile()
    
    # Deletes the Slave file for a delegated Shot.
    # This is done when a Shot is reclaimed by the Master and it is no longer delegated.
    def deleteDelegatedShotFile(self, shot : Shot.Shot, checkout=True):
        self.deleteFile(self.getDelegatedShotFilePath(shot.shotName), checkout=checkout)
    
    # Saves all the files for every delegated Shot, deleting the ones for no-longer-delegated Shots.
    # This function is used as a consistency measure when manually saving.
    def saveOrDeleteAllDelegatedShotsFiles(self, checkout=True, revertIfUnchanged=True):
        shots = self.cutscene.getShots()
        for shot in shots:
            if shot in self.delegatedShots:
                self.saveDelegatedShotFile(shot, checkout=checkout, revertIfUnchanged=revertIfUnchanged)
            else:
                self.deleteDelegatedShotFile(shot, checkout=checkout)
    
    # Loads the contents of every Master-Slave file and caches the information into this object.
    # If this method is not called on an instance of this object, most of the methods won't work correctly.
    # NOTE: If recreate is True, Shots will be reconfigured to conform to the data specified on the Master file.
    # Shots and Actors will be created and deleted if necessary on Slave files.
    # NOTE: If cachePreviews is True, the previews for each Shot will be converted into an image sequence and their ImagePlanes will be created.
    def load(self, recreate=False, cachePreviews=False):
        if not self.exists():
            raise AssertionError("Unable to load Master-Slave file: No master file present on this cutscene!")
        
        # Resets this instance cached data.
        self.delegatedShots = {}
        
        # Parses the Master file and retrieves the Shots and Actors information.
        masterDoc = XML.parse(self.getMasterFilePath())
        rootElement = masterDoc.getroot()
        
        cutsceneRootElement = rootElement.find("CutsceneRoot")
        cutsceneRootPosition = (float(cutsceneRootElement.get("x")), float(cutsceneRootElement.get("y")), float(cutsceneRootElement.get("z")))
        
        shotsElement = rootElement.find("Shots")
        shotElements = shotsElement.findall("Shot")
        shotInfo : list[(str, str, bool, bool, int)] = []
        for shotElement in shotElements:
            shotName = shotElement.text
            shotDescription = shotElement.get("description", default="")
            enabled = shotElement.get("enabled") == "True"
            delegated = shotElement.get("delegated") == "True"
            if delegated:
                # Parses the delegated Shot's file and retrieves the ID of the Slave which claimed it.
                slaveDoc = XML.parse(self.getDelegatedShotFilePath(shotName))
                slaveIdElement = slaveDoc.getroot().find("SlaveID")
                id = int(slaveIdElement.text)
            else:
                id = int(self.masterID)
            shotInfo.append((shotName, shotDescription, enabled, delegated, id))
            
        actorsElement = rootElement.find("Actors")
        actorElements = actorsElement.findall("Actor")
        actorInfo : list[(str, str)] = []
        for actorElement in actorElements:
            namespace = actorElement.text
            file = actorElement.get("file")
            actorInfo.append((namespace, file))
        
        if cachePreviews:
            # Generates the image sequence for each Preview and their ImagePlanes.
            self.shotDurations = {}
            cmds.delete(self.getImagePlanes())
            for shotName, shotDescription, enabled, delegated, id in shotInfo:
                if enabled and id != self.cutscene.masterSlaveID:
                    self.cacheShotPreview(shotName)
         
        if recreate:
            if self.isSlave():
                # Places the CutsceneRoot at the position specified by the Master
                cutsceneRoot = self.cutscene.cutsceneRoot
                cmds.lockNode(cutsceneRoot, lock=False)
                cmds.cutKey(cutsceneRoot)
                cmds.xform(cutsceneRoot, translation=cutsceneRootPosition, worldSpace=True)
                cmds.setAttr("{}.translate".format(cutsceneRoot), lock=True)
                cmds.setAttr("{}.rotate".format(cutsceneRoot), lock=True)
                cmds.setAttr("{}.scale".format(cutsceneRoot), lock=True)
                cmds.lockNode(cutsceneRoot, lock=True)
                
                # Recreates the Shot structure while preserving the information on this file.
                # Missing Shots will be created and Shots not present on the Master file will be deleted.
                newShots = []
                for shotName, shotDescription, enabled, delegated, id in shotInfo:
                    owned = delegated and id == self.cutscene.masterSlaveID
                    if owned:
                        shot = self.cutscene.getShotByName(shotName)
                    else:
                        shot = self.cutscene.getShotByName(shotName)
                        if not shot:
                            shot = self.cutscene.createShot()
                            shot.shotName = shotName
                    shot.description = shotDescription
                    shot.enabled = enabled
                    newShots.append(shot)
                    
                shots = self.cutscene.getShots()
                for shot in shots:
                    self.cutscene.removeShot(shot, disableAllActors=False)
                for shot in newShots:
                    self.cutscene.addShot(shot, enableAllActors=False)
                
                # Creates the necessary actors, merging their files into the scene.
                pathTokenizer = ProjectPath.PathTokenizer(branch="{3D}")
                for namespace, file in actorInfo:
                    references = cmds.ls(rf=True) or []
                    found = False
                    for reference in references:
                        referenceNamespace = cmds.referenceQuery(reference, namespace=True, shortName=True)
                        if namespace == referenceNamespace:
                            found = True
                            if not cmds.referenceQuery(reference, il=True):
                                cmds.file(loadReference=reference)
                            break
                                    
                    actor = ActorManager.getActorByNameSpace(namespace)
                    if not actor:
                        if found:
                            sys.stderr.write("Error: Conflicting Actor namespace, already in use: {}".format(namespace))
                            continue
                        
                        file = pathTokenizer.Translate(file)
                        if not os.path.exists(file):
                            sys.stderr.write("Error: Actor file not found: {}".format(file))
                            continue
                        
                        ActorManager.createActorReference(pathTokenizer.Translate(file), namespace=namespace)
                        actor = ActorManager.getActorByNameSpace(namespace)
                    
                    cutsceneActor = self.cutscene.getCutsceneActorFromActor(actor)
                    if not cutsceneActor:
                        self.cutscene.createCutsceneActor(actor)
                
                cutsceneActors = self.cutscene.getCutsceneActors(nonRemapped=True)
                namespaces = [namespace for namespace, file in actorInfo]
                for cutsceneActor in cutsceneActors:
                    if cutsceneActor.actor.getNamespace() not in namespaces:
                        self.cutscene.removeCutsceneActor(cutsceneActor)
            
            # Conforms the configuration of each Shot to mach the data on the Master file.
            for shotName, shotDescription, enabled, delegated, id in shotInfo:
                if id != self.cutscene.masterSlaveID:
                    shot = self.cutscene.getShotByName(shotName)
                    shot.start = 1
                    shot.end = max(2, self.shotDurations.get(shotName, 0))
                    shot.camera = self.getMasterSlaveCamera()
        
        # Stores the information for the owner of each delegated Shot so it can be quickly accessed.
        for shotName, shotDescription, enabled, delegated, id in shotInfo:
            if delegated:
                self.delegatedShots[self.cutscene.getShotByName(shotName)] = id
    
    # Previews ---------------------
    
    # Returns the cutscene's shared preview folder.
    def getShotPreviewFolder(self):
        cutscenePath = self.cutscene.getPathTokenizer(branch="{3D}").Translate(self.cutscene.path)
        previewFolder = os.path.join(cutscenePath, PREVIEW_PATH)
        return previewFolder
    
    # Returns the path to the preview for a specific Shot.
    # Since previews can have different extensions, looks for a file named as the Shot.
    def getShotPreviewFilePath(self, shotName : str):
        previewFolder = self.getShotPreviewFolder()
        if os.path.exists(previewFolder):
            for path in os.listdir(previewFolder):
                path = os.path.join(previewFolder, path)
                if os.path.isfile(path):
                    fileName, extension = os.path.splitext(os.path.basename(path))
                    if fileName.lower() == shotName.lower():
                        return path
        return None
    
    # Returns the paths for the Shots' previews.
    # If onlyOwned is True, only the owned Shots' preview file paths will be returned.
    def getShotPreviewFilePaths(self, onlyOwned=False):
        if onlyOwned:
            shots = self.getOwnedShots()
        else:
            shots = self.cutscene.getEnabledShots()
        files = [self.getShotPreviewFilePath(shot.shotName) for shot in shots]
        return files
    
    # Checks if all the preview files are up-to-date.
    # If the files are not even on Perforce they will be considered up-to-date too.
    def arePreviewsUpdated(self, onlyOwned=False):
        files = self.getShotPreviewFilePaths(onlyOwned=onlyOwned)
        if not files:
            return True
        status = self.getUpdateStatus(files)
        return status == self.UPDATE_STATUS_SYNC or status == self.UPDATE_STATUS_NOT_IN_DEPOT 
    
    # Gets the lastest revision for all the Preview files.
    def syncPreviewFiles(self):
        files = self.getShotPreviewFilePaths()
        for file in files:
            if file:
                p4File = P4Tools.P4File(file)
                if p4File.isFileInDepot():
                    p4File.syncFile()
    
    # Creates an image sequence from a Shot's preview and an ImagePlane for that sequence so it can be displayed on the MasterSlaveCamera.
    # The image sequence won't be created if the preview file has not been modified and the ImagePlane won't be created if it already exists.
    def cacheShotPreview(self, shotName : str):
        previewFilePath = self.getShotPreviewFilePath(shotName)
        if previewFilePath:
            cacheFolder = os.path.join(PREVIEW_CACHE_PATH, shotName)
            imageSequencePath = os.path.join(cacheFolder, "{}.%d.png".format(shotName))
            firstImagePath = imageSequencePath % 1
            
            # Creates a image sequence for the preview. ImagePlanes cannot use compressed videos, so a 
            if not os.path.exists(firstImagePath) or os.path.getmtime(previewFilePath) > os.path.getmtime(firstImagePath):
                if os.path.exists(cacheFolder):
                    shutil.rmtree(cacheFolder)
                os.makedirs(cacheFolder)
                subprocess.run([FFMPEG_PATH, "-i", previewFilePath, imageSequencePath])
            
            # Assigns the image sequence to an ImagePlane
            imagePlaneName = "{}_imagePlane".format(shotName)
            imagePlanes = self.getImagePlanes()
            if imagePlaneName not in imagePlanes:
                oldSelection = cmds.ls(selection=True)
                
                imagePlaneTrf, imagePlaneShape = cmds.imagePlane(camera=self.getMasterSlaveCamera(), showInAllViews=False, fileName=firstImagePath)
                imagePlaneTrf = cmds.rename(imagePlaneTrf, imagePlaneName)
                imagePlaneShape = cmds.listRelatives(imagePlaneTrf, shapes=True, type="imagePlane")[0]
                cmds.setAttr("{}.useFrameExtension".format(imagePlaneShape), True)
                cmds.setAttr("{}.depth".format(imagePlaneShape), 0.101)
                
                cmds.select(oldSelection)
            
            # Use FFProbe to get the preview's duration (the result is return in seconds)
            result = subprocess.run([FFPROBE_PATH, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", previewFilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.shotDurations[shotName] = int(float(result.stdout) * 30)
            
        else:
            self.shotDurations[shotName] = 0
    
    # Gets the camera to display the previews for delegated Shots.
    # If the camera doesn't exist, it will be created.
    def getMasterSlaveCamera(self, createIfNotExists=True):
        if not cmds.objExists(MASTERSLAVE_CAMERA_NAME):
            if createIfNotExists:
                cameraTrf, cameraShape = cmds.camera(
                    lt=True,
                    displayResolution=True,
                    displayGateMask=True,
                    overscan=1.0,
                    filmFit="overscan",
                    aspectRatio=16.0/9.0
                )
                cmds.setAttr("{}.overscan".format(cameraShape), e=True, lock=True)
                cmds.setAttr("{}.visibility".format(cameraTrf), 0)
                
                cameraTrf = cmds.rename(cameraTrf, MASTERSLAVE_CAMERA_NAME)
            else:
                return None
        return MASTERSLAVE_CAMERA_NAME
    
    # Retrieves all the ImagePlanes attached to the MasterSlaveCamera.
    def getImagePlanes(self):
        cameraShape = cmds.listRelatives(self.getMasterSlaveCamera(), shapes=True, type="camera")
        imagePlanes = cmds.ls(type="imagePlane")
        imagePlanes = [cmds.listRelatives(imagePlane, parent=True)[0] for imagePlane in imagePlanes if cameraShape == cmds.imagePlane(imagePlane, q=True, camera=True)]
        return imagePlanes
    
    # Shows the ImagePlane for the provided Shot and hides the other ones.
    def displayShotPreview(self, shot : Shot.Shot):
        imagePlanes = self.getImagePlanes()
        shotImagePlane = "{}_imagePlane".format(shot.shotName)
        for imagePlane in imagePlanes:
            cmds.setAttr("{}.visibility".format(imagePlane), imagePlane == shotImagePlane)
    
    # Cehcks out the owned Shots' preview files.
    def checkoutPlayblastFiles(self):
        files = self.getShotPreviewFilePaths(onlyOwned=True)
        for file in files:
            if file:
                p4File = P4Tools.P4File(file)
                p4File.smartCheckout()
    