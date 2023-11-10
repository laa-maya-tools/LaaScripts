import maya.cmds as cmds
import maya.mel as mel

from MayaImprovements import MayaImprovement

import ActorManager

import Utils.Maya.QuickLayerMerge as QuickLayerMerge
import Utils.Maya.AnimLayers as AnimLayerUtils
from Utils.Maya.OptionVar import OptionVarConfiguration
from Utils.Maya.UndoContext import UndoContext

import functools

class AnimLayerFix(MayaImprovement):

    initialized = False
    
    # Option Vars
    ENABLE_QUICK_LAYER_MERGE_OPTIONVAR = OptionVarConfiguration("Enable Quick Layer Merge", "ANIMLAYERS_QUICK_MERGE_ENABLED", OptionVarConfiguration.TYPE_INTEGER, True)
    SKIP_ENUM_ATTRIBUTES_OPTIONVAR = OptionVarConfiguration("Skip Enum Attributes on AnimLayers", "ANIMLAYER_SKIP_ENUM_ATTRIBUTES", OptionVarConfiguration.TYPE_INTEGER, True)
    SHOW_ACTOR_OPTIONS_OPTIONVAR = OptionVarConfiguration("Show Actor Options for AnimLayers", "ANIMLAYER_SHOW_ACTOR_OPTIONS", OptionVarConfiguration.TYPE_INTEGER, True)
    SHOW_ANIMLAYER_PANEL_BY_DEFAULT_OPTIONVAR = OptionVarConfiguration("Show AnimLayers Panel by default", "ANIMLAYER_SHOW_ANIMLAYER_PANEL_BY_DEFAULT", OptionVarConfiguration.TYPE_INTEGER, False)
    
    # Constants
    animLayerEditor = "AnimLayerTabanimLayerEditor"
    animLayerButtonLayout = cmds.treeView(animLayerEditor, q=True, parent=True)
    animLayerTab = cmds.formLayout(animLayerButtonLayout, q=True, parent=True)
    layerTabLayout = cmds.control(animLayerTab, q=True, parent=True)
    
    selectedAnimLayerButton = animLayerButtonLayout + "|symbolButton5"
    layersMenu = animLayerTab + "|menu8"
    animLayerPopUpMenu = animLayerButtonLayout + "|AnimLayerTabanimLayerEditor|popupMenu3"

    # Created controls
    createLayerOnActorButton = None
    
    quickLayerMergeMenuItem = None
    
    actorLayersMenu = None
    actorLayersMenuDivider = None
    createLayerOnActorMenuItem = None
    createOverrideLayerOnActorMenuItem = None
    caddActorToLayerMenuItem = None
    removeActorFromLayerMenuItem = None
    extractActorFromLayerMenuItem = None

    @classmethod
    def isQuickLayerMergeEnabled(cls):
        return cls.initialized and cls.ENABLE_QUICK_LAYER_MERGE_OPTIONVAR.value

    @classmethod
    def setQuickLayerMergeEnabled(cls, enabled, updateOptionVar=True):
        if updateOptionVar:
            cls.ENABLE_QUICK_LAYER_MERGE_OPTIONVAR.value = enabled
            
        if cls.quickLayerMergeMenuItem:
            cmds.menuItem(cls.quickLayerMergeMenuItem, e=True, visible=enabled)

    @classmethod
    def isSkipEnumAttributesEnabled(cls):
        return cls.initialized and cls.SKIP_ENUM_ATTRIBUTES_OPTIONVAR.value

    @classmethod
    def setSkipEnumAttributesEnabled(cls, enabled, updateOptionVar=True):
        if updateOptionVar:
            cls.SKIP_ENUM_ATTRIBUTES_OPTIONVAR.value = enabled
        
        if enabled:
            cls.skipEnumAttributes()

    @classmethod
    def isLayerOptionsForActorsEnabled(cls):
        return cls.initialized and cls.SHOW_ACTOR_OPTIONS_OPTIONVAR.value

    @classmethod
    def setLayerOptionsForActorsEnabled(cls, enabled, updateOptionVar=True):
        if updateOptionVar:
            cls.SHOW_ACTOR_OPTIONS_OPTIONVAR.value = enabled
        
        if cls.createLayerOnActorButton:
            cmds.symbolButton(cls.createLayerOnActorButton, e=True, visible=enabled)
        if cls.actorLayersMenu:
            cmds.menuItem(cls.actorLayersMenu, e=True, visible=enabled)
        if cls.actorLayersMenuDivider:
            cmds.menuItem(cls.actorLayersMenuDivider, e=True, visible=enabled)

    @classmethod
    def isShowAnimLayerPanelByDefaultEnabled(cls):
        return cls.initialized and cls.SHOW_ANIMLAYER_PANEL_BY_DEFAULT_OPTIONVAR.value

    @classmethod
    def setShowAnimLayerPanelByDefaultEnabled(cls, enabled, updateOptionVar=True):
        if updateOptionVar:
            cls.SHOW_ANIMLAYER_PANEL_BY_DEFAULT_OPTIONVAR.value = enabled
        
        if enabled:
            cls.switchToAnimLayerPanel()

    @classmethod
    def getMenuItemByLabel(cls, menu, label):
        menuItems = cmds.menu(menu, q=True, itemArray=True)
        if menuItems != None:
            menuLabels = [cmds.menuItem(menuItem, q=True, label=True) for menuItem in menuItems]
            if label in menuLabels:
                return menuItems[menuLabels.index(label)]
            
        cmds.warning("Label {} not found on menu {}!".format(menu, label))
        return None
    
    @classmethod
    def mergeSelectedLayers(cls, *args):
        QuickLayerMerge.mergeSelectedLayers()

    @classmethod
    def getSelectedRigs(cls, check=False):
        #selectedRigs = Rig.getConnectedWrappers(cmds.ls(selection=True) or [])
        # The rigs are not configured yet, we use the selected nodes' namespaces to know which rigs to use.
        objNamespaces = cmds.ls(selection=True, showNamespace=True)
        namespaces = set()
        for i in range(1, len(objNamespaces), 2):
            namespaces.add(objNamespaces[i])
        actors = [ActorManager.getActorByNameSpace(namespace) for namespace in namespaces]
        selectedRigs = [actor.rig for actor in actors if actor != None]
           
        if len(selectedRigs) == 0:
            cmds.warning("None of the selected controls belong to an Actor!")
            return None
        
        elif len(selectedRigs) > 1:
            actorListStr = ""
            for rig in selectedRigs:
                actorListStr += "\n- {}".format(rig.getActor().name)
            result = cmds.confirmDialog(title="Actor Layer", message="Selected controls belong to multiple Actors. Do you want to continue?\n{}".format(actorListStr), button=['Yes','Cancel'], defaultButton='Yes', cancelButton='Cancel', dismissString='Cancel' )
            if result == "Cancel":
                return None
            
        return selectedRigs

    @classmethod
    def createLayerOnSelectedActor(cls, *args, override=False):
        selectedRigs = cls.getSelectedRigs(check=True)
        
        if selectedRigs:
            with UndoContext("Create Layer on Actor"):
                animLayer = AnimLayerUtils.createLayer("AnimLayer1", override=override)
                for rig in selectedRigs:
                    rig.addControlsToLayer(animLayer)
    
    @classmethod
    def addSelectedActorToSelectedLayers(cls, *args):
        selectedRigs = cls.getSelectedRigs(check=True)
        selectedLayers = AnimLayerUtils.getSelectedAnimLayers(ignoreBaseLayer=True)
        
        if selectedRigs:
            with UndoContext("Add Actor to Layer"):
                for animLayer in selectedLayers:
                    for rig in selectedRigs:
                        rig.addControlsToLayer(animLayer)
    
    @classmethod
    def removeSelectedActorFromSelectedLayers(cls, *args):
        selectedRigs = cls.getSelectedRigs(check=True)
        selectedLayers = AnimLayerUtils.getSelectedAnimLayers(ignoreBaseLayer=True)
        
        if selectedRigs:
            with UndoContext("Remove Actor From Layer"):
                for animLayer in selectedLayers:
                    for rig in selectedRigs:
                        rig.removeControlsFromLayer(animLayer)
    
    @classmethod
    def extractSelectedActorFromSelectedLayers(cls, *args):
        selectedRigs = cls.getSelectedRigs(check=True)
        selectedLayers = AnimLayerUtils.getSelectedAnimLayers(ignoreBaseLayer=True)
        
        if selectedRigs:
            with UndoContext("Remove Actor From Layer"):
                for animLayer in selectedLayers:
                    extractLayer = AnimLayerUtils.createLayer("{}_extract".format(animLayer))
                    for rig in selectedRigs:
                        rig.extractControlsFromLayer(animLayer, extractLayer)
    
    @classmethod
    def skipEnumAttributes(cls):
        cmds.optionVar(iv=("animLayerAddObjectsAttributesToUse", 2))
        
        cmds.optionVar(iv=("animLayerAddObjectsExcTranslate", False))
        cmds.optionVar(iv=("animLayerAddObjectsExcRotate", False))
        cmds.optionVar(iv=("animLayerAddObjectsExcScale", False))
        cmds.optionVar(iv=("animLayerAddObjectsExcDyn", False))
        cmds.optionVar(iv=("animLayerAddObjectsExcBool", True))
        cmds.optionVar(iv=("animLayerAddObjectsExcEnum", True))
    
    @classmethod
    def switchToAnimLayerPanel(cls):
        cmds.tabLayout(cls.layerTabLayout, e=True, selectTabIndex=2)
    
    @classmethod
    def animationLayerTabContextMenuCommand(cls, layer):
        # Builds the default context menu
        melCommand = "layerEditorBuildPopupMenu \"AnimLayerTab\" \"" + cls.animLayerPopUpMenu + "\" \"" + layer + "\""
        mel.eval(melCommand)
        
        # The menu can be created without options. Stop here for consistency.
        if not cmds.menu(cls.animLayerPopUpMenu, q=True, itemArray=True):
            return
        
        # Adds the option for quick layer merging
        if cls.isQuickLayerMergeEnabled():
            prev = cls.getMenuItemByLabel(cls.animLayerPopUpMenu, "Merge Layers")
            if prev:
                cmds.menuItem(parent=cls.animLayerPopUpMenu, insertAfter=prev, label="Quick Merge", command=cls.mergeSelectedLayers)
        
        # Adds the option for actors
        if cls.isLayerOptionsForActorsEnabled():
            layerAvailable = mel.eval("layerAvailable();")
            selectedLayers = AnimLayerUtils.getSelectedAnimLayers()
            layerSelected = len(selectedLayers) > 0
            rootLayerSelected = not layerSelected or AnimLayerUtils.getBaseLayer() in selectedLayers
            
            actorLayersMenu = cmds.menuItem(label="Actor", subMenu=True, tearOff=True, image="character.svg", parent=cls.animLayerPopUpMenu, insertAfter="")
            
            createLayerOnActorMenuItem = cmds.menuItem(parent=actorLayersMenu, label="Create Layer on Selected Actor", ann="Creates a Layer and add the controls of the selected actor to it. If multiple actors are selected, all will be added to the same layer.", command=cls.createLayerOnSelectedActor)
            createOverrideLayerOnActorMenuItem = cmds.menuItem(parent=actorLayersMenu, label="Create Override Layer on Selected Actor", ann="Creates an Override Layer and add the controls of the selected actor to it. If multiple actors are selected, all will be added to the same layer.", command=functools.partial(cls.createLayerOnSelectedActor, override=True))
            caddActorToLayerMenuItem = cmds.menuItem(parent=actorLayersMenu, label="Add Selected Actor to Layer", ann="Adds the selected actor's controls to the selected layer.", command=cls.addSelectedActorToSelectedLayers)
            removeActorFromLayerMenuItem = cmds.menuItem(parent=actorLayersMenu, label="Remove Selected Actor from Layer", ann="Removes the selected actor's controls from the selected layer.", command=cls.removeSelectedActorFromSelectedLayers)
            extractActorFromLayerMenuItem = cmds.menuItem(parent=actorLayersMenu, label="Extract Selected Actor from Layer", ann="Extrats the selected actor's controls from the selected layer into a new one.", command=cls.extractSelectedActorFromSelectedLayers)
        
            cmds.menuItem(divider=True, parent=cls.animLayerPopUpMenu, insertAfter=actorLayersMenu)
             
            cmds.menuItem(createLayerOnActorMenuItem, e=True, enable=layerAvailable)
            cmds.menuItem(createOverrideLayerOnActorMenuItem, e=True, enable=layerAvailable)
            cmds.menuItem(caddActorToLayerMenuItem, e=True, enable=not rootLayerSelected)
            cmds.menuItem(removeActorFromLayerMenuItem, e=True, enable=not rootLayerSelected)
            cmds.menuItem(extractActorFromLayerMenuItem, e=True, enable=not rootLayerSelected)
        
        return True
    
    @classmethod
    def animationLayerLayersMenuCommand(cls, *args):
        # Builds the default menu
        melCommand = "layerEditorBuildAnimLayerMenu \"" + cls.layersMenu + "\" \"AnimLayerTab\""
        mel.eval(melCommand)
        
        # Adds the option for quick layer merging
        if cls.isQuickLayerMergeEnabled():
            if cls.quickLayerMergeMenuItem == None:
                prev = cls.getMenuItemByLabel(cls.layersMenu, "Merge Layers")
                if prev:
                    cls.quickLayerMergeMenuItem = cmds.menuItem(parent=cls.layersMenu, insertAfter=prev, label="Quick Merge", command=cls.mergeSelectedLayers)
        
        # Adds the option for actors
        if cls.isLayerOptionsForActorsEnabled():
            layerAvailable = mel.eval("layerAvailable();")
            selectedLayers = AnimLayerUtils.getSelectedAnimLayers()
            layerSelected = len(selectedLayers) > 0
            rootLayerSelected = not layerSelected or AnimLayerUtils.getBaseLayer() in selectedLayers
            
            if cls.actorLayersMenu == None:
                cls.actorLayersMenu = cmds.menuItem(label="Actor", subMenu=True, tearOff=True, image="character.svg", parent=cls.layersMenu, insertAfter="")
                
                cls.createLayerOnActorMenuItem = cmds.menuItem(parent=cls.actorLayersMenu, label="Create Layer on Selected Actor", ann="Creates a Layer and add the controls of the selected actor to it. If multiple actors are selected, all will be added to the same layer.", command=cls.createLayerOnSelectedActor)
                cls.createOverrideLayerOnActorMenuItem = cmds.menuItem(parent=cls.actorLayersMenu, label="Create Override Layer on Selected Actor", ann="Creates an Override Layer and add the controls of the selected actor to it. If multiple actors are selected, all will be added to the same layer.", command=functools.partial(cls.createLayerOnSelectedActor, override=True))
                cls.caddActorToLayerMenuItem = cmds.menuItem(parent=cls.actorLayersMenu, label="Add Selected Actor to Layer", ann="Adds the selected actor's controls to the selected layer.", command=cls.addSelectedActorToSelectedLayers)
                cls.removeActorFromLayerMenuItem = cmds.menuItem(parent=cls.actorLayersMenu, label="Remove Selected Actor from Layer", ann="Removes the selected actor's controls from the selected layer.", command=cls.removeSelectedActorFromSelectedLayers)
                cls.extractActorFromLayerMenuItem = cmds.menuItem(parent=cls.actorLayersMenu, label="Extract Selected Actor from Layer", ann="Extrats the selected actor's controls from the selected layer into a new one.", command=cls.extractSelectedActorFromSelectedLayers)
            
                cls.actorLayersMenuDivider = cmds.menuItem(divider=True, parent=cls.layersMenu, insertAfter=cls.actorLayersMenu)
             
            cmds.menuItem(cls.createLayerOnActorMenuItem, e=True, enable=layerAvailable)
            cmds.menuItem(cls.createOverrideLayerOnActorMenuItem, e=True, enable=layerAvailable)
            cmds.menuItem(cls.caddActorToLayerMenuItem, e=True, enable=not rootLayerSelected)
            cmds.menuItem(cls.removeActorFromLayerMenuItem, e=True, enable=not rootLayerSelected)
            cmds.menuItem(cls.extractActorFromLayerMenuItem, e=True, enable=not rootLayerSelected)
        
        return True
    
    @classmethod
    def createCustomMenuCommands(cls):
        # Replaces the Animation Layer Tab's "Layers" menu command with a custom one that adds the new options.
        cmds.menu(cls.layersMenu, edit=True, postMenuCommand=cls.animationLayerLayersMenuCommand)
        
        # Replaces the Animation Layer Tab's context menu command with a custom one that adds the new options.
        cmds.treeView("AnimLayerTabanimLayerEditor", edit=True, contextMenuCommand=cls.animationLayerTabContextMenuCommand)
    
    @classmethod
    def createActorAnimLayerOptions(cls):
        layerAvailable = mel.eval("layerAvailable();")
        
        # Creates the button for creating a layer on an Actor
        cls.createLayerOnActorButton = cmds.symbolButton(parent=cls.animLayerButtonLayout, image="other/newLayerCharacter.png", annotation="Create Layer on Selected Actor", enable=layerAvailable, command=cls.createLayerOnSelectedActor)
        cmds.formLayout(cls.animLayerButtonLayout, e=True, 
                        attachForm=[
                            (cls.createLayerOnActorButton, "top", 1),
                            (cls.createLayerOnActorButton, "right", 2),
                            (cls.selectedAnimLayerButton, "top", 1)
                            ],
                        attachNone=[
                            (cls.createLayerOnActorButton, "bottom"),
                            (cls.createLayerOnActorButton, "left"),
                            (cls.selectedAnimLayerButton, "bottom"),
                            (cls.selectedAnimLayerButton, "left")
                        ],
                        attachControl=[
                            (cls.selectedAnimLayerButton, "right", 1, cls.createLayerOnActorButton)
                        ]
                        )   # Places the button inside the layout
        #mel.eval("$gLEAddButtons[size($gLEAddButtons)] = \"{}\";".format(cls.createLayerOnActorButton))  # Registers the button on this array so Maya updates it with the other buttons for creating anim layers.
    
    @classmethod
    def deleteOptions(cls):
        if cls.createLayerOnActorButton:
            cmds.deleteUI(cls.createLayerOnActorButton)
            cls.createLayerOnActorButton = None
            cmds.formLayout(cls.animLayerButtonLayout, e=True, 
                        attachForm=[
                            (cls.selectedAnimLayerButton, "top", 1),
                            (cls.selectedAnimLayerButton, "right", 2)
                            ],
                        attachNone=[
                            (cls.selectedAnimLayerButton, "bottom"),
                            (cls.selectedAnimLayerButton, "left")
                        ]
                        )   # Restores the layout
        
        if cls.actorLayersMenu:
            cmds.deleteUI(cls.actorLayersMenu)
            cls.actorLayersMenu = None
        
        if cls.actorLayersMenuDivider:
            cmds.deleteUI(cls.actorLayersMenuDivider)
            cls.actorLayersMenuDivider = None

        if cls.quickLayerMergeMenuItem:
            cmds.deleteUI(cls.quickLayerMergeMenuItem)
            cls.quickLayerMergeMenuItem = None

    @classmethod
    def initialize(cls):
        cls.initialized = True
        
        # Creates the options for adding actors to layers
        cls.createActorAnimLayerOptions()
        
        # Registers the custom menu commands so new options can be added
        cls.createCustomMenuCommands()
        
        # Initializes the options
        cls.setQuickLayerMergeEnabled(cls.isQuickLayerMergeEnabled(), updateOptionVar=False)
        cls.setLayerOptionsForActorsEnabled(cls.isLayerOptionsForActorsEnabled(), updateOptionVar=False)
        cls.setSkipEnumAttributesEnabled(cls.isSkipEnumAttributesEnabled(), updateOptionVar=False)
        cls.setShowAnimLayerPanelByDefaultEnabled(cls.isShowAnimLayerPanelByDefaultEnabled(), updateOptionVar=False)
        
    @classmethod
    def uninitialize(cls):
        cls.initialized = False
        
        # Deletes the created options
        cls.deleteOptions()
