import NodeManager.NodeWrapper as NodeWrapper
import CinematicEditor.CutsceneActor as CutsceneActor

import maya.cmds as cmds

from Utils.Maya.UndoContext import UndoContext, UndoOff
import Utils.Maya.AnimLayers as AnimLayerUtils

import ProjectPath

class Shot(NodeWrapper.NodeWrapper):
    
    _Type = "cutsceneShot"
    
    # Attributes ----------
    
    _cutscene = "cutscene"
    _id = "id"
    _splitParentID = "splitParentID"
    _enabled = "enabled"
    _active = "active"
    _shotName = "shotName"
    _description = "description"
    _start = "start"
    _end = "end"
    _color = "color"
    _camera = "camera"
    _cutsceneActors = "cutsceneActors"
    _ignoreLayers = "ignoreLayers"
    
    # Properties ----------
        
    @property
    def id(self):
        return self.getAttr(self._id)

    @id.setter
    def id(self, value):
        with UndoContext("Set Shot ID"):
            self.setNumericAttribute(self._id, value)
        
    @property
    def splitParentID(self):
        return self.getAttr(self._splitParentID)

    @splitParentID.setter
    def splitParentID(self, value):
        with UndoContext("Set Shot Split Parent ID"):
            self.setNumericAttribute(self._splitParentID, value)
        
    @property
    def enabled(self):
        return self.getAttr(self._enabled)

    @enabled.setter
    def enabled(self, value):
        with UndoContext("Set Shot Enabled"):
            self.setNumericAttribute(self._enabled, value)
        
    @property
    def active(self):
        return self.getAttr(self._active)

    @active.setter
    def active(self, value):
        with UndoContext("Set Shot Active"):
            self.setNumericAttribute(self._active, value)
        
    @property
    def shotName(self):
        return self.getAttr(self._shotName)

    @shotName.setter
    def shotName(self, value):
        with UndoContext("Set Shot Name"):
            self.setStringAttribute(self._shotName, value)
        
    @property
    def description(self):
        return self.getAttr(self._description)

    @description.setter
    def description(self, value):
        with UndoContext("Set Shot Description"):
            self.setStringAttribute(self._description, value)
        
    @property
    def start(self):
        return self.getAttr(self._start)

    @start.setter
    def start(self, value):
        with UndoContext("Set Shot Start"):
            self.setNumericAttribute(self._start, value)
            if value >= self.end:
                self.end = value + 1
        
    @property
    def end(self):
        return self.getAttr(self._end)

    @end.setter
    def end(self, value):
        with UndoContext("Set Shot End"):
            self.setNumericAttribute(self._end, value)
            if value <= self.start:
                self.start = value - 1
            
    @property
    def color(self):
        return self.getAttr(self._color)[0]

    @color.setter
    def color(self, value): 
        with UndoContext("Set Shot Color"):
            self.setFloat3Attribute(self._color, value)
            
    @property
    def camera(self):
        return self.getInputSingle(self._camera)

    @camera.setter
    def camera(self, value): 
        with UndoContext("Set Shot Camera"):
            if value == None:
                self.clearConnection(self._camera)
            else:
                self.connect(self.getPlug(self._camera), "{}.message".format(value))
    
    # Cutscene ------------
    
    def getCutscene(self, forceCutsceneExists=True):
        import CinematicEditor.Cutscene as Cutscene
        cutscene = self.getOutputSingle(self._cutscene, cls=Cutscene.Cutscene)
        if len(cutscene) == 0:
            cutscene = None
        else:
            cutscene = cutscene[0]
        if forceCutsceneExists and cutscene == None:
            raise AssertionError("The Shot doesn't belong to any cutscene!")
        return cutscene
    
    def getSurroundingShots(self):
        shots = self.getCutscene().getShots()    
        index = shots.index(self)
        surroundingShots = []
        if index > 0:
            surroundingShots.append(shots[index - 1])
        if index < len(shots) - 1:
            surroundingShots.append(shots[index + 1])
        return surroundingShots

    # CutsceneActors --------------

    def getCutsceneActors(self, wrapper=True, remap=False):
        cutsceneActors = self.getInputFromListAttribute(self._cutsceneActors, cls=CutsceneActor.CutsceneActor) or []
        if remap:
            cutsceneActors = [cutsceneActor.remap or cutsceneActor for cutsceneActor in cutsceneActors]
        if not wrapper:
            cutsceneActors = [cutsceneActor.node for cutsceneActor in cutsceneActors]
        return cutsceneActors
        
    def setCutsceneActors(self, cutsceneActors):
        with UndoContext("Set Shot CutsceneActors"):
            self.setInputListWrappers(self._cutsceneActors, cutsceneActors, inputAttribute=CutsceneActor.CutsceneActor._shot)

    def addCutsceneActor(self, cutsceneActor):
        with UndoContext("Add CutsceneActor to Shot"):
            self.addItem(self._cutsceneActors, cutsceneActor.getPlug(cutsceneActor._shot))

    def removeCutsceneActor(self, cutsceneActor):
        with UndoContext("Remove CutsceneActor from Shot"):
            self.removeItemListByPlug(self._cutsceneActors, cutsceneActor.getPlug(cutsceneActor._shot))
            
    # Ignore Layers -------

    def getIgnoredLayers(self):
        return self.getInputFromListAttribute(self._ignoreLayers) or []
    
    def getShotLayers(self):
        animLayers = AnimLayerUtils.getAnimLayers()
        ignoredLayers = self.getIgnoredLayers()
        return [animLayer for animLayer in animLayers if animLayer not in ignoredLayers]

    def addLayer(self, layer):
        with UndoContext("Add Layer on Shot"):
            self.removeItemListByPlug(self._ignoreLayers, "{}.message".format(layer))

    def removeLayer(self, layer):
        with UndoContext("Remove Layer on Shot"):
            self.addItem(self._ignoreLayers, "{}.message".format(layer))

    # Split ---------------
    
    def getSplitParent(self):
        cutscene = self.getCutscene()
        cutscene.getShotByID(self.splitParentID)
    
    def setSplitParent(self, shot):
        if shot == None:
            self.splitParentID = -1
        else:
            self.splitParentID = shot.id
        
    def splitShot(self, splitFrame):
        if splitFrame <= self.start or splitFrame >= self.end:
            raise AssertionError("Unable to split shot: Split frame out of range! {}".format(splitFrame))
        
        with UndoContext("Split Shot"):
            cutscene = self.getCutscene()
            index = cutscene.getShotIndex(self)
            newShot = cutscene.createShot(index=(index + 1))
            
            newShot.shotName = "{}_split".format(self.shotName)
            newShot.color = self.color
            newShot.camera = self.camera
            newShot.setCutsceneActors(self.getCutsceneActors())
            newShot.setSplitParent(self)
            
            newShot.start = splitFrame
            newShot.end = self.end
            self.end = splitFrame
            
            return newShot
    
    # Duplicate -----------
    
    def duplicateShot(self, newID=None, rename=False):
        with UndoContext("Duplicate Shot"):
            cutscene = self.getCutscene()
            newShot = self.clone()
            
            if newID == None:
                newID = cutscene.askForID()
            newShot.id = newID
            
            shotIndex = cutscene.getShotIndex(self)
            cutscene.insertShot(newShot, shotIndex + 1)
            
            if rename:
                newShotName = self.shotName + "_copy"
                i = 1
                while cutscene.getShotByName(newShotName) != None:
                    newShotName = self.shotName + "_copy{}".format(i)
                    i += 1
                newShot.shotName = newShotName
            
            return newShot
    
    # Methods -------
    
    goToStart = "start"
    goToEnd = "end"
    goToClamp = "clamp"
    goToNone = None
    
    def applyAnimRange(self, goTo=goToStart):
        with UndoOff():
            cmds.playbackOptions(e=True, min=self.start, ast=self.start, max=self.end, aet=self.end)
            if goTo == Shot.goToStart:
                cmds.currentTime(self.start, e=True)
            elif goTo == Shot.goToEnd:
                cmds.currentTime(self.end, e=True)
            elif goTo == Shot.goToClamp:
                currentTime = cmds.currentTime(q=True)
                clampedTime = min(max(self.start, currentTime), self.end)
                if clampedTime != currentTime:
                    cmds.currentTime(clampedTime, e=True)
        
    def applyCamera(self, selectCamera=False, applyToCurrent=False):
        with UndoOff():
            if selectCamera:
                cmds.select(self.camera)
                
            viewports = cmds.getPanel(type="modelPanel")
            shots = self.getCutscene().getShots()
            shotCameras = [shot.camera for shot in shots]
            for viewport in viewports:
                camera = cmds.modelPanel(viewport, q=True, cam=True)
                if cmds.nodeType(camera) == "camera":
                    camera = cmds.listRelatives(camera,  parent=True, path=True)[0]
                if camera in shotCameras:
                    cmds.modelPanel(viewport, e=True, cam=self.camera)
            
            if applyToCurrent:
                activeEditor = cmds.playblast(ae=True)
                viewport = activeEditor.split("|")[-1]
                cmds.modelPanel(viewport, e=True, cam=self.camera)
                
    def applyAnimLayers(self):
        AnimLayerUtils.setEnabledAnimLayers(self.getShotLayers())
    
    def getDuration(self):
        return self.end - self.start
    
    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = self.getCutscene().getPathTokenizer(branch=branch)
        pathTokenizer.Update({ ProjectPath.Tokens.TShotName : self.shotName })
        return pathTokenizer
    
    # Export -------
    
    def exportCamera(self, restoreAfterExport=True, checkout=True, convert=True, compile=True):
        return self.getCutscene().export(shots=[self], cameras=True, forceShots=True, restoreAfterExport=restoreAfterExport, checkout=checkout, convert=convert, compile=compile)

    def exportActors(self, actors, force=False, restoreAfterExport=True, checkout=True, convert=True, compile=True):
        return self.getCutscene().export(shots=[self], actors=actors, forceActors=force, forceShots=True, restoreAfterExport=restoreAfterExport, checkout=checkout, convert=convert, compile=compile)
