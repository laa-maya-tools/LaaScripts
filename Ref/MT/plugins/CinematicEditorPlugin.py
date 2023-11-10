import maya.api.OpenMaya as OpenMaya

import NodeID

import CinematicEditor
import CinematicEditor.MasterSlave as MasterSlave

def maya_useNewAPI():
    pass

onSaveCallback = None
onLoadCallback = None

class Cutscene(OpenMaya.MPxNode):
    
    # Plugin data
    nodeName = "cutscene"

    # Node Attributes
    path = OpenMaya.MObject()
    cutsceneRoot = OpenMaya.MObject()
    cutsceneActors = OpenMaya.MObject()
    shots = OpenMaya.MObject()
    masterSlaveID = OpenMaya.MObject()
    nextAvailableID = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return Cutscene()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()

        # Path
        Cutscene.path = typedAttribute.create("path", "p", OpenMaya.MFnData.kString)
        Cutscene.addAttribute(Cutscene.path)

        # Cutscene Root
        Cutscene.cutsceneRoot = messageAttribute.create("cutsceneRoot", "cr")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Cutscene.addAttribute(Cutscene.cutsceneRoot)
        
        # Actors
        Cutscene.cutsceneActors = messageAttribute.create("cutsceneActors", "ca")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        Cutscene.addAttribute(Cutscene.cutsceneActors)
        
        # Shots
        Cutscene.shots = messageAttribute.create("shots", "sht")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        Cutscene.addAttribute(Cutscene.shots)

        # Master-Slave ID
        Cutscene.masterSlaveID = numericAttribute.create("masterSlaveID", "msid", OpenMaya.MFnNumericData.kInt, -1)
        numericAttribute.keyable = False
        numericAttribute.connectable = False
        Cutscene.addAttribute(Cutscene.masterSlaveID)

        # Next Available ID
        Cutscene.nextAvailableID = numericAttribute.create("nextAvailableID", "nid", OpenMaya.MFnNumericData.kInt)
        numericAttribute.keyable = False
        numericAttribute.connectable = False
        Cutscene.addAttribute(Cutscene.nextAvailableID)

    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)


class Shot(OpenMaya.MPxNode):
    
    # Plugin data
    nodeName = "cutsceneShot"

    # Node Attributes
    cutscene = OpenMaya.MObject()
    id = OpenMaya.MObject()
    splitParentID = OpenMaya.MObject()
    enabled = OpenMaya.MObject()
    active = OpenMaya.MObject()
    shotName = OpenMaya.MObject()
    description = OpenMaya.MObject()
    start = OpenMaya.MObject()
    end = OpenMaya.MObject()
    color = OpenMaya.MObject()
    camera = OpenMaya.MObject()
    cutsceneActors = OpenMaya.MObject()
    ignoreLayers = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return Shot()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        unitAttribute = OpenMaya.MFnUnitAttribute()

        # Cutscene       
        Shot.cutscene = messageAttribute.create("cutscene", "cut")
        messageAttribute.writable = False
        messageAttribute.readable = True
        Shot.addAttribute(Shot.cutscene)

        # ID
        Shot.id = numericAttribute.create("id", "id", OpenMaya.MFnNumericData.kInt)
        numericAttribute.keyable = False
        numericAttribute.connectable = False
        Shot.addAttribute(Shot.id)

        # Split Parent
        Shot.splitParentID = numericAttribute.create("splitParentID", "spid", OpenMaya.MFnNumericData.kInt, -1)
        numericAttribute.keyable = False
        numericAttribute.connectable = False
        Shot.addAttribute(Shot.splitParentID)
        
        # Enabled
        Shot.enabled = numericAttribute.create("enabled", "enb", OpenMaya.MFnNumericData.kBoolean, True)
        Shot.addAttribute(Shot.enabled)
        
        # Active
        Shot.active = numericAttribute.create("active", "a", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = False
        Shot.addAttribute(Shot.active)
        
        # Shot Name
        Shot.shotName = typedAttribute.create("shotName", "sn", OpenMaya.MFnData.kString)
        Shot.addAttribute(Shot.shotName)

        # Description
        Shot.description = typedAttribute.create("description", "dsc", OpenMaya.MFnData.kString)
        Shot.addAttribute(Shot.description)

        # Start
        Shot.start = unitAttribute.create("start", "s", OpenMaya.MFnUnitAttribute.kTime)
        unitAttribute.keyable = False
        Shot.addAttribute(Shot.start)

        # End
        Shot.end = unitAttribute.create("end", "e", OpenMaya.MFnUnitAttribute.kTime)
        unitAttribute.keyable = False
        Shot.addAttribute(Shot.end)

        # Color
        Shot.color = numericAttribute.createColor("color", "col")
        numericAttribute.keyable = False
        Shot.addAttribute(Shot.color)

        # Camera       
        Shot.camera = messageAttribute.create("camera", "cam")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Shot.addAttribute(Shot.camera)

        # Actors
        Shot.cutsceneActors = messageAttribute.create("cutsceneActors", "ca")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        Shot.addAttribute(Shot.cutsceneActors)

        # Ignore Layers
        Shot.ignoreLayers = messageAttribute.create("ignoreLayers", "il")
        messageAttribute.array = True
        messageAttribute.writable = True
        messageAttribute.readable = False
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        Shot.addAttribute(Shot.ignoreLayers)

    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(False)
 
 
class CutsceneActor(OpenMaya.MPxNode):
    
    # Plugin data
    nodeName = "cutsceneActor"

    # Node Attributes
    cutscene = OpenMaya.MObject()
    shot = OpenMaya.MObject()
    actor = OpenMaya.MObject()
    subActor = OpenMaya.MObject()
    remap = OpenMaya.MObject()
    active = OpenMaya.MObject()
    
    @staticmethod
    def creator():
        return CutsceneActor()
    
    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()

        # Cutscene
        CutsceneActor.cutscene = messageAttribute.create("cutscene", "cut")
        messageAttribute.writable = False
        messageAttribute.readable = True
        CutsceneActor.addAttribute(CutsceneActor.cutscene)

        # Shot
        CutsceneActor.shot = messageAttribute.create("shot", "sht")
        messageAttribute.writable = False
        messageAttribute.readable = True
        CutsceneActor.addAttribute(CutsceneActor.shot)

        # Actor
        CutsceneActor.actor = messageAttribute.create("actor", "act")
        messageAttribute.writable = True
        messageAttribute.readable = False
        CutsceneActor.addAttribute(CutsceneActor.actor)

        # SubActor
        CutsceneActor.subActor = messageAttribute.create("subActor", "sact")
        messageAttribute.writable = True
        messageAttribute.readable = False
        CutsceneActor.addAttribute(CutsceneActor.subActor)

        # Remap
        CutsceneActor.remap = messageAttribute.create("remap", "rmp")
        messageAttribute.writable = True
        messageAttribute.readable = False
        CutsceneActor.addAttribute(CutsceneActor.remap)
        
        # Active
        CutsceneActor.active = numericAttribute.create("active", "a", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.storable = False
        CutsceneActor.addAttribute(CutsceneActor.active)

    def postConstructor(self):
        self.setExistWithoutInConnections(False)
        self.setExistWithoutOutConnections(False)


def onSave(*args):
    cutscene = CinematicEditor.getCutscene()
    if cutscene:
        masterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
        if masterSlaveFile.exists():
            masterSlaveFile.load()
            if masterSlaveFile.isMaster():
                masterSlaveFile.saveMasterFile()
            elif masterSlaveFile.isSlave():
                for shot in masterSlaveFile.getOwnedShots():
                    masterSlaveFile.saveDelegatedShotFile(shot)

def onLoad(*args):
    cutscene = CinematicEditor.getCutscene()
    if cutscene:
        masterSlaveFile = MasterSlave.MasterSlaveFile(cutscene)
        if masterSlaveFile.exists():
            masterSlaveFile.load(recreate=True)

# initialize the script plug-in
def initializePlugin(mobject):
    global onSaveCallback
    global onLoadCallback
    
    mplugin = OpenMaya.MFnPlugin(mobject)

    mplugin.registerNode(Cutscene.nodeName, NodeID.CinematicEditorCutsceneID, Cutscene.creator, Cutscene.initializer)
    mplugin.registerNode(Shot.nodeName, NodeID.CinematicEditorShotID, Shot.creator, Shot.initializer)
    mplugin.registerNode(CutsceneActor.nodeName, NodeID.CinematicEditorCutsceneActorID, CutsceneActor.creator, CutsceneActor.initializer)

    onSaveCallback = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterSave, onSave)
    onLoadCallback = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterOpen, onLoad)

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    global onSaveCallback
    global onLoadCallback

    mplugin = OpenMaya.MFnPlugin(mobject)

    OpenMaya.MSceneMessage.removeCallback(onSaveCallback)
    OpenMaya.MSceneMessage.removeCallback(onLoadCallback)

    mplugin.deregisterNode(NodeID.CinematicEditorCutsceneID)
    mplugin.deregisterNode(NodeID.CinematicEditorShotID)
    mplugin.deregisterNode(NodeID.CinematicEditorCutsceneActorID)
