# -*- coding: utf-8 -*-
from  NodeManager   import NodeWrapper

from Utils.Maya.UndoContext import UndoContext
import Utils.Maya.Mirror as MirrorUtils 

from  ActorManager  import AnimPreset

class AnimPresetSubHolder():
    
    # Devuelve el AnimPresetHolder que posee este SubHolder
    def getHolder(self):
        raise NotImplementedError()
    
    # Devuelve el PathTokenizer necesario para interpretar las rutas de exportación de los AnimPresets
    def getPathTokenizer(self):
        raise NotImplementedError()
    
    # Devuelve el plug que se utiliza para identificar a este SubHolder
    def getSubHolderPlug(self):
        raise NotImplementedError()
    
    # Devuelve el path en el que se exportan las animaciones de este SubHolder
    def getAnimPath(self):
        raise NotImplementedError()
    
    # Devuelve el nombre que debería mostrarse para este SubHolder
    def getDisplayName(self):
        raise NotImplementedError()
    
    # Operaciones que hacer antes de exportar una animación de este SubHolder
    # Permite devolver un objeto que será pasado como parámetro a los otros métodos de exportación
    def onPreExport(self):
        # NOTE: Por defecto no hace ni devuelve nada
        return None
    
    # Operaciones que hacer después de exportar una animación de este SubHolder
    # Recibe un objeto que haya sido devuelto por onPreExport
    def onPostExport(self, data):
        # NOTE: Por defecto no hace nada
        pass
    
    # Devuelve los nodos (o su raiz) que se vayan a exportar en una animación de este SubHolder
    # Recibe el objeto de datos devuelto por onPreExport
    def getExportNodes(self, data):
        raise NotImplementedError()
    
    # Operación a realizar cuando se necesite hacer mirror a la animación de este SubHolder
    # Recibe el objeto de datos devuelto por onPreExport
    # Devuelve un nuevo objeto de datos con los cambios que haya necesitado hacer
    def mirrorAnimation(self, data):
        # NOTE: Por defecto mirrorea en el plano XY los nodos especificados como nodos de exportación
        MirrorUtils.mirrorControls(self.getExportNodes(), mirrorPlane=MirrorUtils.MirrorPlane.XY)
        return data
    
    # Devuelve el tipo de archivo de las animaciones que se exportan desde este SubHolder
    def getExportFileType(self):
        raise NotImplementedError()
    

class AnimPresetHolder(NodeWrapper.NodeWrapper):

    _animPresets    = "animPresetList"
    
    # ------ ANIM PRESETS

    def createAnimPreset(self):
        with UndoContext("Create Actor AnimPreset"):
            animPreset = AnimPreset.AnimPreset()
            animPreset.create()
            self.appendInputPlug(self._animPresets,  animPreset.getPlug(animPreset._holder))
            return animPreset

    def getAnimPresets(self, wrapper=True):
        if wrapper:
            wrapperCLS = AnimPreset.AnimPreset
        else:
            wrapperCLS = None   
        return self.getInputFromListAttribute(self._animPresets,cls=wrapperCLS)

    def setAnimPresets(self, animPresets):
        with UndoContext("Set Actor AnimPresets"):
            self.setInputListWrappers(self._animPresets, animPresets, inputAttribute=AnimPreset.AnimPreset._holder)

    def appendAnimPresets(self, animPresets):
        with UndoContext("Append Actor AnimPresets"):
            self.appendInputListWrappers(self._animPresets, animPresets, inputAttribute=AnimPreset.AnimPreset._holder)
            
    def addAnimPreset(self, animPreset):
        with UndoContext("Add Actor AnimPreset"):
            self.appendInputPlug(self._animPresets,  animPreset.getPlug(animPreset._holder))
            
    def insertAnimPreset(self, animPreset, index):
        with UndoContext("Insert Actor AnimPreset"):
            self.insertItemList(self._animPresets, index, animPreset.getPlug(animPreset._holder))

    def removeAnimPreset(self, animPreset, delete=True):
        with UndoContext("Remove Actor AnimPreset"):
            self.removeItemListByPlug(self._animPresets, animPreset.getPlug(animPreset._holder), delete=delete)
    
    def deleteAnimPreset(self, animPreset):
        with UndoContext("Delete Actor AnimPreset"):
            self.removeItemListByPlug(self._animPresets, animPreset.getPlug(animPreset._holder), delete=True)

    def normalizeAnimPresetsNameParts(self):
        # Make sure that all the actor's animpresets have the same amount of name parts
        with UndoContext("Normalize AnimPreset Name Parts"):
            animPresets = self.getAnimPresets()
            
            namePartsCount = 0
            for animPreset in animPresets:
                namePartsCount = max(namePartsCount, len(animPreset.getNameParts()))
            
            for animPreset in animPresets:
                nameParts = animPreset.getNameParts()
                while len(nameParts) < namePartsCount:
                    nameParts.append("")
                animPreset.setNameParts(nameParts)
    
    # ------ VIRTUAL METHODS
    
    # Devuelve la lista de layers que pertenecen al Holder.
    # Las subclases pueden sobreescribirlo para devolver una sublista de layers.
    def getAnimLayers(self, includeBaseLayer=False):
        # NOTE: Por defecto devolvemos todas las layers, en el orden de la interfaz.
        import maya.cmds as cmds
        
        def getChildLayers(layer):
            layers = [layer]
            children = cmds.animLayer(layer, q=True, c=True) or []
            for c in children:
                layers += getChildLayers(c)
            return layers
            
        rootLayer = cmds.animLayer(q=True, root=True)
        if rootLayer != None:
            layers = getChildLayers(rootLayer)
            if not includeBaseLayer:
                layers.remove(rootLayer)
            return layers
        else:
            return []
    
    # En caso de usar SubHolders (como SubActor), devuelve el SubHolder principal usado en animación.
    def getMainSubHolder(self):
        # NOTE: Por defecto se asume que no se usan SubHolders, así que se devuelve el propio Holder.
        return self
    
    # Devuelve el nombre que debería mostrarse para este AnimPresetHolder
    def getDisplayName(self):
        raise NotImplementedError()
    