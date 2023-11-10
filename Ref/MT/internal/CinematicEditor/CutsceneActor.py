import NodeManager.NodeWrapper as NodeWrapper

import ActorManager.Actor as Actor
import ActorManager.SubActor as SubActor

from Utils.Maya.UndoContext import UndoContext

import ProjectPath

import os

class CutsceneActor(NodeWrapper.NodeWrapper):
    
    _Type = "cutsceneActor"
    
    # Attributes ----------
    
    _cutscene = "cutscene"
    _shot = "shot"
    _actor = "actor"
    _subActor = "subActor"
    _remap = "remap"
    _active = "active"
    
    # Properties ----------

    @property
    def actor(self):
        return self.getInputSingle(self._actor, cls=Actor.Actor)

    @actor.setter
    def actor(self, value): 
        with UndoContext("Set CutsceneActor Actor"):
            if value == None:
                self.clearConnection(self._actor)
            else:
                self.connect(self.getPlug(self._actor), value.getPlug("message"))

    @property
    def subActor(self):
        return self.getInputSingle(self._subActor, cls=SubActor.SubActor)

    @subActor.setter
    def subActor(self, value): 
        with UndoContext("Set CutsceneActor SubActor"):
            if value == None:
                self.clearConnection(self._subActor)
            else:
                self.connect(self.getPlug(self._subActor), value.getPlug("message"))

    @property
    def remap(self):
        return self.getInputSingle(self._remap, cls=CutsceneActor)

    @remap.setter
    def remap(self, value): 
        with UndoContext("Set Actor Remap"):
            if value == None:
                self.clearConnection(self._remap)
            else:
                self.connect(self.getPlug(self._remap), value.getPlug("message"))

    @property
    def active(self):
        return self.getAttr(self._active)
    
    @active.setter
    def active(self, value):
        with UndoContext("Set Actor Active"):
            self.setNumericAttribute(self._active, value)
    
    # Cutscene ------------
    
    def getCutscene(self, forceCutsceneExists=True):
        import CinematicEditor.Cutscene as Cutscene
        cutscene = self.getOutputSingle(self._cutscene, cls=Cutscene.Cutscene)
        if len(cutscene) == 0:
            cutscene = None
        else:
            cutscene = cutscene[0]
        if forceCutsceneExists and cutscene == None:
            raise AssertionError("The Actor doesn't belong to any cutscene!")
        return cutscene
    
    def getActorShots(self):
        import CinematicEditor.Shot as Shot
        return self.getOutputFromListAttribute(self._shot, cls=Shot.Shot)
    
    # Actor ------------
    
    def getActorName(self):
        remap = self.remap
        if remap:
            return remap.getActorName()
        else:
            return self.actor.getNamespace()
    
    def getAnimSubActor(self):
        return self.actor.animSubActor
    
    def getModelSubActor(self):
        subActor = self.subActor
        if subActor == None:
            subActor = self.actor.mainSubActor
        return subActor
    
    def getDCRootNode(self):
        return self.getAnimSubActor().getDCRootNode()
    
    def getDCRootControlNode(self):
        return self.getAnimSubActor().getDCRootControlNode()
    
    def getModelPath(self, translated=False, relative=False, removeFirstSlash=False, branch="{Game}"):
        subActor = self.getModelSubActor()
        modelPath = os.path.join(subActor.modelPath, "{}.mdl".format(subActor.modelName))
        if translated:
            pathTokenizer = subActor.getPathTokenizer(branch=branch)
            if relative:
                pathTokenizer.Update({ProjectPath.Tokens.TPrjBranch: "", ProjectPath.Tokens.TActors: "actors"})
            modelPath = pathTokenizer.Translate(modelPath)
            if removeFirstSlash and (modelPath.startswith("/") or modelPath.startswith("\\")):
                modelPath = modelPath[1:]
        return modelPath
    
    def getActorCharclass(self):
        subActor = self.getModelSubActor()
        pathTokenizer = subActor.getPathTokenizer()
        
        # FAILSAFE: Fix for missing field
        cinematicCharclass = subActor.cinematicCharclass
        if not cinematicCharclass:
            if subActor.name == "Power":
                cinematicCharclass = "{ActorName}"
            else:
                cinematicCharclass = "{SubActorName}"
        
        return pathTokenizer.Translate(cinematicCharclass)

    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = self.getCutscene().getPathTokenizer(branch=branch)
        pathTokenizer.Update({ProjectPath.Tokens.TActorName : self.actor.getNamespace()})
        return pathTokenizer
    
    # Export ------------
    
    def export(self, shots, force=False, restoreAfterExport=True, checkout=True, convert=True, compile=True):
        return self.getCutscene().export(shots=shots, actors=[self], forceShots=force, forceActors=True, restoreAfterExport=restoreAfterExport, checkout=checkout, convert=convert, compile=compile)
