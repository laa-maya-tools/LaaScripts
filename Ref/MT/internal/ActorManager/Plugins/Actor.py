# -*- coding: utf-8 -*-
import ActorManager.Plugins.AnimPresetHolder as AnimPresetHolder

import NodeID
import NodeID.PluginNodes as PluginNodes

#Maya API 2 
import maya.api.OpenMaya as OpenMaya
#import maya.api.OpenMayaUI as omui

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass

class Actor(AnimPresetHolder.AnimPresetHolder, PluginNodes.PluginNode):
    
    # Plugin data
    nodeName    = "actor"
    nodeID      = NodeID.ActorManagerActorID
    
    typesDict = {
        'Characters': 0,
        'Cameras'   : 1,
        'Events'    : 2,
        'FX'        : 3,
        'Instances' : 4,
        'Items'     : 5,
        'Props'     : 6,
        'SpawnGroups': 7,
        'SpawnPoints': 8,
        'Weapons'   :9,
        'LogicPathGroups': 10,
        'Shared'    : 11
    }

    name            = OpenMaya.MObject()
    type            = OpenMaya.MObject()
    mainSubActor    = OpenMaya.MObject()
    animSubActor    = OpenMaya.MObject()
    subActorList    = OpenMaya.MObject()
    rig             = OpenMaya.MObject()
    animLayerList   = OpenMaya.MObject()
    cinematicActor  = OpenMaya.MObject()
    
    
    #Method to return an instance    
    @staticmethod
    def creator():
        return Actor()
    
    #Method called by Maya at initialization
    #Set attributes
    @staticmethod
    def initializer():
        #Attributes are defined using the create method of a subclass of the MFnAttribute class.
        messageAttribute = OpenMaya.MFnMessageAttribute()
        typedAttribute = OpenMaya.MFnTypedAttribute()        
        enumAttribute = OpenMaya.MFnEnumAttribute()
        
        #mainSubActor       
        Actor.mainSubActor = messageAttribute.create("mainSubActor", "msa")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Actor.addAttribute(Actor.mainSubActor)        
        
        #animSubActor       
        Actor.animSubActor = messageAttribute.create("animSubActor", "asa")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Actor.addAttribute(Actor.animSubActor)        
        
        #subActorList
        Actor.subActorList = messageAttribute.create("subActorList", "sacl")
        messageAttribute.array = True
        #messageAttribute.indexMatters = True
        messageAttribute.writable = True
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        messageAttribute.readable = False
        Actor.addAttribute(Actor.subActorList) 
        
        #mainSubActor       
        Actor.rig = messageAttribute.create("rig", "rig")
        messageAttribute.writable = True
        messageAttribute.readable = False
        Actor.addAttribute(Actor.rig)

        #animLayerList
        Actor.animLayerList = messageAttribute.create("animLayerList", "all")
        messageAttribute.array = True
        #messageAttribute.indexMatters = False
        messageAttribute.writable = True
        messageAttribute.disconnectBehavior = messageAttribute.kDelete
        messageAttribute.readable = False
        Actor.addAttribute(Actor.animLayerList) 

        #name
        Actor.name = typedAttribute.create("name", "nm", OpenMaya.MFnData.kString )
        Actor.addAttribute(Actor.name)

        #type
        Actor.type = enumAttribute.create("type", "t", 0) #The number is the default value (currently: characters)
        enumAttribute.writable = True
        enumAttribute.readable = True
        enumAttribute.storable = True
        for t in Actor.typesDict:
            enumAttribute.addField(t, Actor.typesDict[t])
        Actor.addAttribute(Actor.type)
        
        #cinematicActor       
        Actor.cinematicActor = messageAttribute.create("cinematicActor", "ca")
        messageAttribute.writable = False
        messageAttribute.readable = True
        Actor.addAttribute(Actor.cinematicActor)
        
        # AnimPresetHolder initializer
        AnimPresetHolder.AnimPresetHolder.initializer()

    def postConstructor(self):
        self.setExistWithoutInConnections(True)
        self.setExistWithoutOutConnections(True)
