import NodeManager.NodeWrapper as NodeWrapper
import CinematicEditor.Shot as Shot
import CinematicEditor.CutsceneActor as CutsceneActor

import maya.cmds as cmds

import Utils.Maya as MayaUtils
from Utils.Maya.UndoContext import UndoContext, UndoOff
import Utils.Maya.AnimLayers as AnimLayerUtils

import ProjectPath
import Exporter
import AnimSystems

import xml.etree.ElementTree as XML
import subprocess
import functools
import os

class CutsceneExportListener(object):
    
    def onStartExport(self, shots, actors, cameras, structure, compile):
        return True
    
    def onPreExportShots(self, shots):
        return True
    
    def onExportActor(self, actor, actorIndex, shot, shotIndex, actors):
        return True
    
    def onPreExportCameras(self, shots):
        return True
    
    def onExportCamera(self, camera, shot, shotIndex):
        return True
    
    def onCompile(self):
        return True
    
    def onExportStructure(self):
        return True
    
    def onFinishExport(self):
        return True
    
    def onError(self, exception):
        return True


class Cutscene(NodeWrapper.NodeWrapper):
    
    _Type = "cutscene"
    
    # Attributes ----------
    
    _path = "path"
    _cutsceneRoot = "cutsceneRoot"
    _cutsceneActors = "cutsceneActors"
    _shots = "shots"
    _masterSlaveID = "masterSlaveID"
    _nextAvailableID = "nextAvailableID"
    
    # Properties ----------
        
    @property
    def path(self):
        return self.getAttr(self._path)
    
    @path.setter
    def path(self, value):
        with UndoContext("Set Cutscene Path"):
            self.setStringAttribute(self._path, value)
        
    @property
    def cutsceneRoot(self):
        return self.getInputSingle(self._cutsceneRoot)

    @cutsceneRoot.setter
    def cutsceneRoot(self, value):
        with UndoContext("Set Cutscene Root"):
            if value == None:
                self.clearConnection(self._cutsceneRoot)
            else:
                self.connect(self.getPlug(self._cutsceneRoot), "{}.message".format(value))
    
    @property
    def masterSlaveID(self):
        return self.getAttr(self._masterSlaveID)
    
    @masterSlaveID.setter
    def masterSlaveID(self, value):
        with UndoContext("Set Master Slave ID"):
            self.setNumericAttribute(self._masterSlaveID, value)
    
    # CutsceneActors --------------
    
    def createCutsceneActor(self, actor, enableInAllShots=True):
        with UndoContext("Create Cutscene Actor"):
            cutsceneActor = CutsceneActor.CutsceneActor().create()
            cutsceneActor.actor = actor
            self.addCutsceneActor(cutsceneActor, enableInAllShots=enableInAllShots)
            return cutsceneActor
        
    def getCutsceneActorFromActor(self, actor):
        cutsceneActors = self.getCutsceneActors()
        for cutsceneActor in cutsceneActors:
            if cutsceneActor.actor == actor:
                return cutsceneActor
        return None

    def getCutsceneActors(self, wrapper=True, nonRemapped=False):
        cutsceneActors = self.getInputFromListAttribute(self._cutsceneActors, cls=CutsceneActor.CutsceneActor) or []
        if nonRemapped:
            cutsceneActors = [cutsceneActor for cutsceneActor in cutsceneActors if cutsceneActor.remap == None]
        if not wrapper:
            cutsceneActors = [cutsceneActor.node for cutsceneActor in cutsceneActors]
        return cutsceneActors
        
    def getActiveCutsceneActors(self, wrapper=True, nonRemapped=False):
        cutsceneActors = self.getCutsceneActors(wrapper=True, nonRemapped=nonRemapped)
        cutsceneActors = [cutsceneActor for cutsceneActor in cutsceneActors if cutsceneActor.active]
        if not wrapper:
            cutsceneActors = [cutsceneActor.node for cutsceneActor in cutsceneActors]
        return cutsceneActors
    
    def getCutsceneActorIndex(self, cutsceneActor):
        cutsceneActors = self.getCutsceneActors()
        return cutsceneActors.index(cutsceneActor)
    
    def setCutsceneActorIndex(self, cutsceneActor, newIndex):
        with UndoContext("Set Cutscene Actor Index"):
            cutsceneActorIndex = self.getCutsceneActorIndex(cutsceneActor)
            self.moveItemList(self._cutsceneActors, cutsceneActorIndex, newIndex)

    def addCutsceneActor(self, cutsceneActor, enableInAllShots=True):
        if cutsceneActor not in self.getCutsceneActors():
            with UndoContext("Add Cutscene Actor"):
                self.addItem(self._cutsceneActors, cutsceneActor.getPlug(cutsceneActor._cutscene))
                
                if enableInAllShots:
                    shots = self.getShots()
                    for shot in shots:
                        shot.addCutsceneActor(cutsceneActor)

    def insertCutsceneActor(self, cutsceneActor, index, enableInAllShots=True):
        if cutsceneActor not in self.getCutsceneActors():
            with UndoContext("Insert Cutscene Actor"):
                self.insertItemList(self._cutsceneActors, index, cutsceneActor.getPlug(cutsceneActor._cutscene))
                
                if enableInAllShots:
                    shots = self.getShots()
                    for shot in shots:
                        shot.addCutsceneActor(cutsceneActor)

    def removeCutsceneActor(self, cutsceneActor, disableInAllShots=True, delete=False):
        if cutsceneActor in self.getCutsceneActors():
            with UndoContext("Remove Cutscene Actor"):
                if disableInAllShots:
                    shots = self.getShots()
                    for shot in shots:
                        shot.removeCutsceneActor(cutsceneActor)
                    
                self.removeItemListByPlug(self._cutsceneActors, cutsceneActor.getPlug(cutsceneActor._cutscene), delete=delete)
    
    # Shots ---------------
    
    def createShot(self, index=None, id=None, enableAllActors=True):
        with UndoContext("Create Cutscene Shot"):
            shot = Shot.Shot().create()
            if id == None:
                id = self.askForID()
            shot.id = id
            if index != None:
                self.insertShot(shot, index, enableAllActors=enableAllActors)
            else:
                self.addShot(shot, enableAllActors=enableAllActors)
            return shot

    def getShots(self, wrapper=True):
        return self.getInputFromListAttribute(self._shots, cls=(Shot.Shot if wrapper else None)) or []
    
    def getEnabledShots(self):
        shots = self.getShots()
        return [shot for shot in shots if shot.enabled]
    
    def getActiveShots(self):
        shots = self.getEnabledShots()
        return [shot for shot in shots if shot.active]
        
    def getShotByID(self, id):
        shots = self.getShots()
        for shot in shots:
            if shot.id == id:
                return shot
        return None
    
    def getShotByName(self, name):
        shots = self.getShots()
        for shot in shots:
            if shot.shotName == name:
                return shot
        return None
    
    def getShotIndex(self, shot):
        shots = self.getShots()
        return shots.index(shot)
    
    def setShotIndex(self, shot, newIndex):
        with UndoContext("Set Cutscene Shot Index"):
            shotIndex = self.getShotIndex(shot)
            self.moveItemList(self._shots, shotIndex, newIndex)
    
    def addShot(self, shot, enableAllActors=True):
        with UndoContext("Add Cutscene Shot"):
            self.appendInputWrapper(self._shots, shot, inputAttribute=shot._cutscene)
            
            if enableAllActors:
                cutsceneActors = self.getCutsceneActors(nonRemapped=True)
                for cutsceneActor in cutsceneActors:
                    shot.addCutsceneActor(cutsceneActor)

    def insertShot(self, shot, index, enableAllActors=True):
        with UndoContext("Insert Cutscene Shot"):
            self.insertItemWrapper(self._shots, index, shot, inputAttribute=shot._cutscene)
            
            if enableAllActors:
                cutsceneActors = self.getCutsceneActors(nonRemapped=True)
                for cutsceneActor in cutsceneActors:
                    shot.addCutsceneActor(cutsceneActor)

    def removeShot(self, shot, disableAllActors=True, delete=False):
        with UndoContext("Remove Cutscene Shot"):
            if disableAllActors:
                cutsceneActors = self.getCutsceneActors()
                for cutsceneActor in cutsceneActors:
                    shot.removeCutsceneActor(cutsceneActor)

            self.removeItemListByPlug(self._shots, shot.getPlug(shot._cutscene), delete=delete)
            
    # Next Available ID ---
    
    def getNextAvailableID(self):
        return self.getAttr(self._nextAvailableID)
    
    def askForID(self):
        currenID = self.getNextAvailableID()
        self.setNumericAttribute(self._nextAvailableID, currenID + 1)
        return currenID
    
    # Methods -------------
    
    def getCutsceneName(self):
        path = self.path
        return os.path.basename(path) if path else None

    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = ProjectPath.PathTokenizer(branch=branch)
        pathTokenizer.Update({ ProjectPath.Tokens.TCutsceneName : self.getCutsceneName() })
        return pathTokenizer
    
    def getShotsAtTime(self, time, shots=None):
        if shots == None:
            shots = self.getEnabledShots()
        return [shot for shot in shots if time >= shot.start and time <= shot.end]
    
    def getShotOverlaps(self, shot, shots=None):
        if not shot.enabled:
            return []
        
        if shots == None:
            shots = self.getEnabledShots()
            
        start = shot.start
        end = shot.end
        return [s for s in shots if s != shot and s.start <= end and s.end >= start]

    def getTotalDuration(self, shots=None):
        if shots == None:
            shots = self.getEnabledShots()
            
        totalDuration = 0
        for shot in shots:
            totalDuration += shot.getDuration()
        return totalDuration
    
    def getCutsceneFrameFromShot(self, shot, shotFrame=0, shots=None):
        if not shot.enabled:
            raise AssertionError("Unable to get the shot's cutscene frame: The shot is not enabled!")
        
        if shots == None:
            shots = self.getEnabledShots()
            
        if shot not in shots:
            raise AssertionError("Unable to get the shot's cutscene frame: The shot is not part of the cutscene!")
        
        shotIndex = shots.index(shot)
        cutsceneFrame = 0
        for i in range(shotIndex):
            cutsceneFrame += shots[i].getDuration()
        
        return cutsceneFrame + shotFrame

    def getCutsceneFrameFromAnimationFrame(self, animationFrame, preferredShot=None, shots=None):
        if shots == None:
            shots = self.getEnabledShots()
            
        if preferredShot != None and preferredShot in shots and animationFrame >= preferredShot.start and animationFrame <= preferredShot.end:
            shot = preferredShot
        else:
            shotOverlaps = self.getShotsAtTime(animationFrame, shots=shots)
            if len(shotOverlaps) == 0:
                return None
            
            if len(shotOverlaps) == 1 or preferredShot == None or preferredShot not in shots:
                shot = shotOverlaps[0]
            else:
                # This only happens if there are several shots on the same frame and a preferred shot has been specified but it doesn't contain the frame.
                # The next shot to the preferred shot will be used (among the shots that contain the animation frame).
                # If there is not such shot, the closest one will be used.
                preferredShotIndex = shots.index(preferredShot)
                shot = None
                for shotOverlap in shotOverlaps:
                    index = shots.index(shotOverlap)
                    if index >= preferredShotIndex:
                        shot = shotOverlap
                        break
                if shot == None:
                    shot = shotOverlaps[-1]
        
        return self.getCutsceneFrameFromShot(shot, shotFrame=(animationFrame - shot.start), shots=shots)
    
    def getShotAndFrameFromCutsceneFrame(self, cutsceneFrame, shots=None):
        if shots == None:
            shots = self.getEnabledShots()
            
        for shot in shots:
            duration = shot.getDuration()
            if duration > cutsceneFrame or (shot == shots[-1] and duration == cutsceneFrame):
                return shot, cutsceneFrame
            else:
                cutsceneFrame -= duration
                
        return None, None
    
    def frameShots(self, shots):
        if shots:
            start = None
            end = None
            for shot in shots:
                if start == None or start > shot.start:
                    start = shot.start
                if end == None or end < shot.end:
                    end = shot.end
            cmds.playbackOptions(e=True, min=start, max=end, ast=start, aet=end)
    
    def frameAllShots(self):
        shots = self.getEnabledShots()
        self.frameShots(shots)
    
    # Export -------
    
    def createCutsceneRoot(self, name="Cutscene_Root"):
        with UndoContext("Create Cutscene Root"):
            cutsceneRoot = cmds.spaceLocator(name=name)[0]
            cmds.lockNode(cutsceneRoot)
            
            shape = cmds.listRelatives(cutsceneRoot, shapes=True)[0]
            cmds.setAttr("{}.localScale".format(shape), 100, 100, 100)
            
            self.cutsceneRoot = cutsceneRoot
            return cutsceneRoot
    
    def breakRootConnections(self, rootControl):
        plugs = []
        for attr in ["translate", "rotate"]:
            for coord in ["", "X", "Y", "Z"]:
                plugs.append("{}.{}{}".format(rootControl, attr, coord))
        connections = cmds.listConnections(plugs, s=True, d=False, p=True, c=True) or []
        pairs = []
        for i in range(0, len(connections), 2):
            cmds.disconnectAttr(connections[i+1], connections[i])
            pairs.append((connections[i+1], connections[i]))
        return pairs
    
    def restoreRootConnections(self, rootControl, connections):
        for source, destination in connections:
            cmds.connectAttr(source, destination)
    
    def export(self, shots=[], actors=[], cameras=False, structure=False, forceShots=False, forceActors=False, shotsToUpdate=None, restoreAfterExport=True, checkout=True, convert=True, compile=True, runCharEditor=True, exportListener : CutsceneExportListener = None):
        with UndoOff(), AnimSystems.CallbacksDisabledContext():
            # Saves the current scene state to restore it after the export
            if restoreAfterExport:
                currentAnimRange = (cmds.playbackOptions(q=True, ast=True), cmds.playbackOptions(q=True, aet=True), cmds.playbackOptions(q=True, min=True), cmds.playbackOptions(q=True, max=True))
                
                animLayers = AnimLayerUtils.getAnimLayers()
                currentAnimLayers = [animLayer for animLayer in animLayers if not cmds.animLayer(animLayer, q=True, m=True)]
                
                currentSelection = cmds.ls(selection=True)
            
            # Filters which shots and actors are marked for export
            shots = [shot for shot in shots if shot.enabled and (forceShots or shot.active)]
            actors = [actor for actor in actors if forceActors or actor.active]
            
            # Checks if all the data can be exported
            for shot in shots:
                if shot.start >= shot.end:
                    raise AssertionError("Unable to export Shot {}: Invalid range! -> [{}, {}]".format(shot.shotName, shot.start, shot.end))
                if not shot.start.is_integer() or not shot.end.is_integer():
                    raise AssertionError("Unable to export Shot {}: Range is not an Integer number!".format(shot.shotName))
            
            # Begins exporting
            exportedFiles = []
            root = self.cutsceneRoot
            changelistDescription = "Cutscene Export: {}".format(self.getCutsceneName().lower())
            cutsceneExportPath = self.getPathTokenizer().Translate(self.path)
            
            try:
                if exportListener:
                    if not exportListener.onStartExport(shots, actors, cameras, structure, compile):
                        return None
                
                # Actor exporting
                if actors:
                    try:
                        # Prepares the actors for exporting
                        rootConstraints = []
                        rootConnections = {}
                        for actor in actors:
                            rootControl = actor.getDCRootControlNode()
                            if not cmds.parentConstraint(rootControl, q=True):
                                rootConnections[rootControl] = self.breakRootConnections(rootControl)
                                rootConstraints += cmds.parentConstraint(root, rootControl, maintainOffset=False)
                        
                        actorExportStructs = []
                        for shotIndex, shot in enumerate(shots):  # NOTE: We iterate through shots first to avoid changing the enabled AnimLayers too often when exporting
                            # Caches some data
                            shotActors = [actor for actor in shot.getCutsceneActors() if actor in actors]
                            shotLayers = shot.getShotLayers()
                            shotName = shot.shotName
                            shotStart = shot.start
                            shotEnd = shot.end
                            
                            # Creates the export struct for batching
                            for actorIndex, actor in enumerate(shotActors):
                                dcRootNode = actor.getDCRootNode()
                                actorExportPath = os.path.join(cutsceneExportPath, "actors", actor.getActorName())
                                actorExportStructs.append(Exporter.AnimationExportStruct(dcRootNode, shotName, actorExportPath, shotStart, shotEnd, False, animLayers=shotLayers, callback=functools.partial(exportListener.onExportActor, actor, actorIndex, shot, shotIndex, shotActors) if exportListener else None))
                        
                        if exportListener:
                            if not exportListener.onPreExportShots(shots):
                                return None
                        
                        # Exports the actors
                        files = Exporter.exportAnimationBatch(actorExportStructs, fileType=Exporter.EXPORTER_ANIMATION_FILE_TYPE, checkout=checkout, changelist=changelistDescription, convert=convert, compile=False)   # The compilation will be performed on all the exported files at the end
                        
                        if files == None:
                            return None
                        exportedFiles += files
                        
                    finally:
                        # Restores the actors
                        cmds.delete(rootConstraints)
                        for rootControl, connections in rootConnections.items():
                            self.restoreRootConnections(rootControl, connections)
                    
                # Camera exporting
                if cameras:
                    try:
                        # Prepares the cameras for exporting
                        exportCameras = {}
                        shotCameras = [shot.camera for shot in shots]
                        for shotCamera in shotCameras:
                            if shotCamera in exportCameras:
                                oldCamera, exportCamera = exportCameras[shotCamera]
                            else:
                                oldCamera, exportCamera = Exporter.createExportCamera(shotCamera, parent=root)
                                exportCameras[shotCamera] = (oldCamera, exportCamera)
                            
                        # Creates the export struct for batching
                        cameraExportStructs = []
                        camerasPath = os.path.join(cutsceneExportPath, "cameras")
                        for i, shot in enumerate(shots):
                            exportCamera = exportCameras[shotCameras[i]][1]
                            cameraExportStructs.append(Exporter.AnimationExportStruct(exportCamera, shot.shotName, camerasPath, shot.start, shot.end, False, animLayers=shot.getShotLayers(), callback=functools.partial(exportListener.onExportCamera, exportCamera, shot, i) if exportListener else None))
                        
                        if exportListener:
                            if not exportListener.onPreExportCameras(shots):
                                return None
                        
                        # Exports the cameras
                        files = Exporter.exportAnimationBatch(cameraExportStructs, fileType=Exporter.EXPORTER_CAMERA_FILE_TYPE, checkout=checkout, changelist=changelistDescription, convert=convert, compile=False)   # The compilation will be performed on all the exported files at the end
                        if files == None:
                            return None
                        exportedFiles += files
                        
                    finally:
                        # Restores the cameras
                        for oldCamera, exportCamera in exportCameras.values():
                            Exporter.deleteExportCamera(oldCamera, exportCamera)
                        
                # Compiles the animations
                if convert and compile: # Cannot compile the animations if they are not converted first
                    if shots and (cameras or actors):   # Compiling is done when exporting actors or cameras
                        if exportListener:
                            if not exportListener.onCompile():
                                return None
                        Exporter.compileAssetFiles(exportedFiles)
                    
                # Structure exporting
                if structure:
                    if exportListener:
                        if not exportListener.onExportStructure():
                            return None
                    self.exportStructure(runCharEditor=runCharEditor, wait=False, raiseExceptions=True, shotsToUpdate=shotsToUpdate)
                
                if exportListener:
                    if not exportListener.onFinishExport():
                        return None
            
            except Exception as e:
                if exportListener:
                    if not exportListener.onError(e):
                        return None
                raise e
            
            finally:
                # Restores the original scene state
                if restoreAfterExport:
                    cmds.playbackOptions(e=True, ast=currentAnimRange[0], aet=currentAnimRange[1], min=currentAnimRange[2], max=currentAnimRange[3])
                    
                    for animLayer in animLayers:
                        shouldBeMuted = animLayer not in currentAnimLayers
                        if cmds.animLayer(animLayer, q=True, m=True) != shouldBeMuted:
                            cmds.animLayer(animLayer, e=True, m=shouldBeMuted)
                            
                    cmds.select(currentSelection)
                
            return exportedFiles
    
    def exportStructure(self, runCharEditor=True, wait=False, raiseExceptions=True, shotsToUpdate=None):
        xmlRoot = XML.Element("CutSceneExportInfo")
        
        # Cutscene ID
        idNode = XML.Element("Id")
        idNode.text = self.getCutsceneName()
        xmlRoot.append(idNode)
        
        # Cutscene Framerate
        fpsNode = XML.Element("FPS")
        fpsNode.text = str(int(MayaUtils.getFrameRate()))
        xmlRoot.append(fpsNode)
        
        # Cutscene Root Translation
        cutsceneRoot = self.cutsceneRoot
        if cutsceneRoot:
            with UndoOff():
                currentTime = cmds.currentTime(q=True)
                cmds.currentTime(0, e=True)
                cutsceneRootPosition = cmds.xform(cutsceneRoot, q=True, translation=True, worldSpace=True)
                cmds.currentTime(currentTime, e=True)
            
            cutsceneRootNode = XML.Element("ROOT")
            cutsceneRootNode.attrib["x"] = str(cutsceneRootPosition[0])
            cutsceneRootNode.attrib["y"] = str(cutsceneRootPosition[1])
            cutsceneRootNode.attrib["z"] = str(cutsceneRootPosition[2])
            xmlRoot.append(cutsceneRootNode)
        
        # Actors
        actorsNode = XML.Element("Actors")
        xmlRoot.append(actorsNode)
        
        actors = self.getCutsceneActors(nonRemapped=True)
        for actor in actors:
            actorNode = XML.Element("Actor")
            
            actorIdNode = XML.Element("Id")
            actorIdNode.text = actor.actor.getNamespace()
            actorNode.append(actorIdNode)
            
            actorTypeNode = XML.Element("Type")
            actorTypeNode.text = actor.getActorCharclass()
            actorNode.append(actorTypeNode)
            
            actorModelNode = XML.Element("Model")
            actorModelNode.text = actor.getModelPath(translated=True, relative=True, removeFirstSlash=True)
            actorNode.append(actorModelNode)
            
            actorsNode.append(actorNode)
        
        # Shots (called "Takes" on this file)
        shotsNode = XML.Element("Takes")
        xmlRoot.append(shotsNode)
        
        shots = self.getEnabledShots()
        if shotsToUpdate == None:
            shotsToUpdate = shots
        for shot in shots:
            shotNode = XML.Element("Take")
            
            shotIdNode = XML.Element("Id")
            shotIdNode.text = shot.shotName
            shotNode.append(shotIdNode)
            
            shotDurationNode = XML.Element("Duration")
            shotDurationNode.text = str(int(shot.getDuration()))
            shotDurationNode.attrib["update"] = str(shot in shotsToUpdate)
            shotNode.append(shotDurationNode)
            
            shotActorsNode = XML.Element("ActorsConfig")
            shotActorsNode.attrib["update"] = str(shot in shotsToUpdate)
            shotNode.append(shotActorsNode)
            
            shotActors = shot.getCutsceneActors(remap=True)
            for actor in actors:
                shotActorNode = XML.Element(actor.getActorName())
                
                shotActorVisibleNode = XML.Element("Visible")
                shotActorVisibleNode.text = str(actor in shotActors)
                shotActorNode.append(shotActorVisibleNode)
                    
                shotActorsNode.append(shotActorNode)
            
            shotsNode.append(shotNode)
        
        # Saves the XML file
        cutsceneExportPath = self.getPathTokenizer().Translate(self.path)
        filePath = os.path.join(cutsceneExportPath, "ExportInfo.xml")
        
        xmlTree = XML.ElementTree(xmlRoot)
        with open(filePath, "wb") as file:
            xmlTree.write(file)
        
        # Opens the CharacterEditor to process the cutscene
        if runCharEditor:
            characterEditorPath = os.path.join(ProjectPath.getMSFrameworkFolder(), "prjCharEditor.exe")
            if os.path.exists(characterEditorPath):
                command = "{} -cutimport=\"{}\"".format(characterEditorPath, filePath)
                process = subprocess.Popen(command, cwd=ProjectPath.getMSFrameworkFolder())
                
                if wait:
                    stdout, stderr = process.communicate()
                    if raiseExceptions and process.returncode != 0:
                        raise RuntimeError(stderr)
                    
            elif raiseExceptions:
                raise FileNotFoundError("Unable to open CharacterEditor: File not found! {}".format(characterEditorPath))
            
        return filePath
