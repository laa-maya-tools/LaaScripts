# -*- coding: utf-8 -*-
import ActorManager.AnimPresetHolder as AnimPresetHolder

import ProjectPath
from Utils.Maya.UndoContext import UndoContext

from  ActorManager  import SubActor

import RigManager.Rig as Rig

class Actor(AnimPresetHolder.AnimPresetHolder):

    _Type           = "actor"
    _typeAttribute  = "type"
    _name           = "name"
    _subActors      = "subActorList"
    _animPresets    = "animPresetList"
    _rig            = "rig"
    _mainSubActor   = "mainSubActor" 
    _animSubActor   = "animSubActor"


    def __init__(self, node=None):
        super(Actor, self).__init__(node)

    # en este wrapper el nombre de los set asociados a un atributo se compone con la variable node, en otros es con otra variable
    def getCollectionName(self):
        return self.node
    
    #--------- PROPERTIES
    # name
    @property
    def name(self):
        return self.getAttr(self._name)
    
    @name.setter
    def name(self, value):
        with UndoContext("Set Actor Name"):
            self.setStringAttribute(self._name, value)

    # mainSubActor
    @property
    def mainSubActor(self):
        return self.getInputSingle(self._mainSubActor, cls=SubActor.SubActor)
        
    @mainSubActor.setter
    def mainSubActor(self, inputWrapper): 
        with UndoContext("Set Actor MainSubActor"):
            self.setInputWrapper(self._mainSubActor, inputWrapper, inputAttribute="message")
    
    # animSubActor
    @property
    def animSubActor(self):
        return self.getInputSingle(self._animSubActor, cls=SubActor.SubActor)
        
    @animSubActor.setter
    def animSubActor(self, inputWrapper): 
        with UndoContext("Set Actor MainSubActor"):
            self.setInputWrapper(self._animSubActor, inputWrapper, inputAttribute="message")
    
    # rig
    @property
    def rig(self):
        r = self.getInputSingle(self._rig, cls=Rig.Rig)
        if r == None:
            with UndoContext("Create Actor Rig"):
                r = Rig.Rig().create()
                self.rig = r
        return r
        
    @rig.setter
    def rig(self, inputWrapper): 
        with UndoContext("Set Actor Rig"):
            self.setInputWrapper(self._rig, inputWrapper, inputAttribute="actor")
    
    # type
    @property
    def type(self):
        return self.getAttr(self._typeAttribute)
    
    @type.setter
    def type(self, value): 
        self.setNumericAttribute(self._typeAttribute, value)
    
    @property
    def typestr(self):
        return self.getEnumerateValue(self._typeAttribute, self.type)
    
    @typestr.setter
    def typestr(self, value): 
        self.type = self.getEnumerateIndex(self._typeAttribute, value)
     
    def getTypes(self):
        return self.getEnumerateList(self._typeAttribute)
    
    #--------- Create. Overriden. Calls to base class create and do extra actions)
    def create(self, nodeName=_Type, unique=True):
        theNode = super(self.__class__, self).create(nodeName, unique)
        return theNode
    
    #--------- METHODS
    def getPathTokenizer(self, branch="{Game}"):
        pathTokenizer = ProjectPath.PathTokenizer(branch=branch)
        pathTokenizer.Update({ ProjectPath.Tokens.TActorType : self.typestr })
        pathTokenizer.Update({ ProjectPath.Tokens.TActorName : self.name })
        return pathTokenizer
    
    #--------- SUBACTORS
    def createSubActor(self, name):
        with UndoContext("Create SubActor"):
            theSubActor = SubActor.SubActor()
            theSubActor.create(name)
            self.appendInputPlug(self._subActors,  theSubActor.getPlug(theSubActor._actor))
            #self.addItem( self._subActors, theSubActor.getPlug(theSubActor._actor))
            return theSubActor

    def getSubActors(self, wrapper=True):
        if wrapper:
            wrapperCLS = SubActor.SubActor
        else:
            wrapperCLS = None   
        return self.getInputFromListAttribute(self._subActors, cls=wrapperCLS) or []
    
    def getSubActorsByTags(self, tagsFilter=[], anyMatch=False, wrapper=True):
        wrapperCLS = SubActor.SubActor
        theList = self.getInputFromListAttribute(self._subActors, cls=wrapperCLS) or []
        listResult = []
        for obj in theList:
            if anyMatch:
                if any(filterValue in obj.tags for filterValue in tagsFilter):
                    listResult.append(obj)
            else:
                if all(filterValue in obj.tags for filterValue in tagsFilter):
                    listResult.append(obj)
        if wrapper:
            return listResult
        else:
            return self.getNodeList(listResult)                

    #--------- OVERRIDE
    
    def getMainSubHolder(self):
        return self.animSubActor
    
    def getDisplayName(self):
        if self.isReferencedNodes:
            return self.getNamespace()
        else:
            return self.name
    