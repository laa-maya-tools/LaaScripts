import maya.cmds as cmds

import AnimSystems.Noise as Noise

import TimeSlider
import Utils.Maya.OptionBox as OptionBoxUtils
import Utils.Maya.AnimLayers as AnimLayerUtils

def addNoiseToSelectedTransforms(translation=True, rotation=True, scale=False):
    selection = cmds.ls(selection=True, type="transform")
    for obj in selection:
        Noise.addNoiseToTransform(obj, translation=translation, rotation=rotation, scale=scale)

def removeNoiseFromSelectedTransforms(translation=True, rotation=True, scale=True):
    selection = cmds.ls(selection=True, type="transform")
    for obj in selection:
        Noise.removeNoiseFromTransform(obj, translation=translation, rotation=rotation, scale=scale, restoreToNormalTransform=True)

def addNoiseToSelectedAttributes():
    selectedNodes = cmds.channelBox(TimeSlider.mainChannelBox, q=True, mainObjectList=True)
    selectedAttributes = cmds.channelBox(TimeSlider.mainChannelBox, q=True, selectedMainAttributes=True)
    for node in selectedNodes:
        Noise.addNoiseToNode(node, selectedAttributes)

def removeNoiseFromSelectedAttributes():
    selectedNodes = cmds.channelBox(TimeSlider.mainChannelBox, q=True, mainObjectList=True)
    selectedAttributes = cmds.channelBox(TimeSlider.mainChannelBox, q=True, selectedMainAttributes=True)
    for node in selectedNodes:
        Noise.removeNoiseFromNode(node, selectedAttributes, removeNoiseAttributes=True)


class AddNoiseToSelectedTransformsOptionBox(OptionBoxUtils.OptionBoxWindow):
    
    OPTIONVAR_SELECTED_COMPONENTS = "ADDNOISETOSELECTEDTRANSFORMSOPTIONBOX_SELECTED_COMPONENTS"
    
    isAddNoiseToTranslateSelected = None
    isAddNoiseToRotateSelected = None
    isAddNoiseToScaleSelected = None
    
    def __init__(self):
        self.transformationComponentsCheckboxGroup = None
        
        OptionBoxUtils.OptionBoxWindow.__init__(self, "Add Noise to Selected Transforms", "Add Noise")
        
    def onCreateUI(self):
        cmds.columnLayout()
        self.transformationComponentsCheckboxGroup = cmds.checkBoxGrp(
            label="Components:", ann="Selects which components the noise should be applied to.",
            numberOfCheckBoxes=3, label1="Translation", label2="Rotation", label3="Scale",
            changeCommand=self.retrieveOptions
        )
        
    def retrieveOptions(self, *args):
        values = cmds.checkBoxGrp(self.transformationComponentsCheckboxGroup, q=True, valueArray3=True)
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToTranslateSelected = values[0]
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToRotateSelected = values[1]
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToScaleSelected = values[2]
        
    def onApplyOptions(self):
        cmds.checkBoxGrp(self.transformationComponentsCheckboxGroup, e=True,
            value1=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToTranslateSelected,
            value2=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToRotateSelected,
            value3=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToScaleSelected
        )
    
    def onSaveOptions(self):
        cmds.optionVar(ca=AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS)
        cmds.optionVar(iva=(AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS, AddNoiseToSelectedTransformsOptionBox.isAddNoiseToTranslateSelected))
        cmds.optionVar(iva=(AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS, AddNoiseToSelectedTransformsOptionBox.isAddNoiseToRotateSelected))
        cmds.optionVar(iva=(AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS, AddNoiseToSelectedTransformsOptionBox.isAddNoiseToScaleSelected))
        
    def onLoadOptions(self):
        if cmds.optionVar(ex=AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS):
            values = cmds.optionVar(q=AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS)
        else:
            values = (True, True, False)    # Default Values
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToTranslateSelected = values[0]
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToRotateSelected = values[1]
        AddNoiseToSelectedTransformsOptionBox.isAddNoiseToScaleSelected = values[2]
    
    def onResetOptions(self):
        cmds.optionVar(rm=AddNoiseToSelectedTransformsOptionBox.OPTIONVAR_SELECTED_COMPONENTS)
    
    def onApply(self):
        addNoiseToSelectedTransforms(
            translation=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToTranslateSelected,
            rotation=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToRotateSelected,
            scale=AddNoiseToSelectedTransformsOptionBox.isAddNoiseToScaleSelected
        )


class AddNoiseToAttributesOptionBox(OptionBoxUtils.OptionBoxWindow):
    
    # Option Vars
    OPTIONVAR_USE_LAYER = "ADDNOISETOSELECTEDATTRIBUTESOPTIONBOX_USE_LAYER"
    OPTIONVAR_SHARE_ATTRIBUTES = "ADDNOISETOSELECTEDATTRIBUTESOPTIONBOX_SHARE_ATTRIBUTES"
    OPTIONVAR_SHARE_LABEL = "ADDNOISETOSELECTEDATTRIBUTESOPTIONBOX_SHARE_LABEL"
    
    # Constants
    COMBOBOX_CURRENT_LAYER_OPTION = "<Current Layer>"
    
    # Storable
    useLayer = None
    shareAttributes = None
    shareEnabled = None
    shareSeed = None
    offsetSeed = None
    shareIntensity = None
    shareFrequency = None
    shareJerk = None
    shareLabel = None
    
    # Non-Storable
    selectedLayer = None
    
    def __init__(self):
        self.layerComboBox = None
        self.useLayerCheckBox = None
        
        self.shareAttributesCheckBox = None
        self.shareLabelTextField = None
        self.shareEnabledCheckBox = None
        self.shareSeedCheckBox = None
        self.offsetSeedCheckBox = None
        self.shareIntensityCheckBox = None
        self.shareFrequencyCheckBox = None
        self.shareJerkCheckBox = None
        
        self.nodeList = None
        self.attributeList = None
        
        self.changes = {}
        
        self.selectedLayerChangedScriptJob = None
        
        OptionBoxUtils.OptionBoxWindow.__init__(self, "Add Noise to Attributes", None)
    
    def onShow(self):
        self.updateLayerList()
        self.addSelectedNodesToList()
        
        self.selectedLayerChangedScriptJob = cmds.scriptJob(e=("animLayerRefresh", self.onAnimLayerRefresh))
        
    def onClose(self):
        cmds.scriptJob(kill=self.selectedLayerChangedScriptJob)
        
    def onLoadOptions(self):
        if cmds.optionVar(ex=AddNoiseToAttributesOptionBox.OPTIONVAR_USE_LAYER):
            AddNoiseToAttributesOptionBox.useLayer = cmds.optionVar(q=AddNoiseToAttributesOptionBox.OPTIONVAR_USE_LAYER)
        else:
            AddNoiseToAttributesOptionBox.useLayer = False    # Default Value
        
        if cmds.optionVar(ex=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES):
            values = cmds.optionVar(q=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES)
        else:
            values = [True, True, True, True, False, False, False]    # Default Value
        AddNoiseToAttributesOptionBox.shareAttributes = values[0]
        AddNoiseToAttributesOptionBox.shareEnabled = values[1]
        AddNoiseToAttributesOptionBox.shareSeed = values[2]
        AddNoiseToAttributesOptionBox.offsetSeed = values[3]
        AddNoiseToAttributesOptionBox.shareIntensity = values[4]
        AddNoiseToAttributesOptionBox.shareFrequency = values[5]
        AddNoiseToAttributesOptionBox.shareJerk = values[6]
        
        if cmds.optionVar(ex=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_LABEL):
            AddNoiseToAttributesOptionBox.shareLabel = cmds.optionVar(q=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_LABEL)
        else:
            AddNoiseToAttributesOptionBox.shareLabel = ""    # Default Value
          
    def onSaveOptions(self):
        cmds.optionVar(iv=(AddNoiseToAttributesOptionBox.OPTIONVAR_USE_LAYER, AddNoiseToAttributesOptionBox.useLayer))
        
        cmds.optionVar(ca=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES)
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareAttributes))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareEnabled))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareSeed))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.offsetSeed))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareIntensity))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareFrequency))
        cmds.optionVar(iva=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES, AddNoiseToAttributesOptionBox.shareJerk))
        
        cmds.optionVar(sv=(AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_LABEL, AddNoiseToAttributesOptionBox.shareLabel))
    
    def onResetOptions(self):
        cmds.optionVar(rm=AddNoiseToAttributesOptionBox.OPTIONVAR_USE_LAYER)
        cmds.optionVar(rm=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_ATTRIBUTES)
        cmds.optionVar(rm=AddNoiseToAttributesOptionBox.OPTIONVAR_SHARE_LABEL)
         
    def onApplyOptions(self):
        self.setUseLayer(AddNoiseToAttributesOptionBox.useLayer, updateCheckBox=True)
        
        self.setShareAttributes(AddNoiseToAttributesOptionBox.shareAttributes, updateCheckBox=True)
        self.setShareEnabled(AddNoiseToAttributesOptionBox.shareEnabled, updateCheckBox=True)
        self.setShareSeed(AddNoiseToAttributesOptionBox.shareSeed, updateCheckBox=True)
        self.setOffsetSeed(AddNoiseToAttributesOptionBox.offsetSeed, updateCheckBox=True)
        self.setShareIntensity(AddNoiseToAttributesOptionBox.shareIntensity, updateCheckBox=True)
        self.setShareFrequency(AddNoiseToAttributesOptionBox.shareFrequency, updateCheckBox=True)
        self.setShareJerk(AddNoiseToAttributesOptionBox.shareJerk, updateCheckBox=True)
        
        self.setShareLabel(AddNoiseToAttributesOptionBox.shareLabel, updateTextField=True)
        
    def onCreateUI(self):
        mainFormLayout = cmds.formLayout(width=330)
        
        self.useLayerCheckBox = cmds.checkBox(label="Apply on Layer", changeCommand=self.setUseLayer)
        self.layerComboBox = cmds.optionMenu(width=150, alwaysCallChangeCommand=True, changeCommand=self.onAnimLayerSelected)
        
        paneLayout = cmds.paneLayout(configuration="vertical2")
        
        nodeListFormLayout = cmds.formLayout()
        nodeListHeader = cmds.text(label="Nodes", ann="List of nodes to apply the noise to.")
        addSelectedNodesButton = cmds.button(label="Add Selected Nodes", c=self.addSelectedNodesToList, ann="Adds the selected nodes on the scene to the list.")
        self.nodeList = cmds.treeView(allowDragAndDrop=False, allowMultiSelection=False, itemDblClickCommand=self.passFn, numberOfButtons=1, attachButtonRight=True, pressCommand=(1, self.removeNodeFromList))
        cmds.formLayout(nodeListFormLayout, e=True,
                        attachForm=[
                            (nodeListHeader, "top", 5), (nodeListHeader, "left", 0),
                            (addSelectedNodesButton, "top", 0), (addSelectedNodesButton, "right", 5),
                            (self.nodeList, "bottom", 0), (self.nodeList, "left", 0), (self.nodeList, "right", 0)
                            ],
                        attachControl=[
                            (self.nodeList, "top", 10, nodeListHeader)
                            ]
                        )
        cmds.setParent("..")
        
        attributeListFormLayout = cmds.formLayout()
        attributeListHeader = cmds.text(label="Attributes", ann="List of attributes to apply the noise to. Use the buttons to enable or disable noise on each attribute.")
        resetChangesButton = cmds.button(label="Reset Changes", c=self.resetChanges, ann="Adds the selected nodes on the scene to the list.")
        self.attributeList = cmds.treeView(allowDragAndDrop=False, allowMultiSelection=False, itemDblClickCommand=self.toggleNoiseEnabled, numberOfButtons=1, attachButtonRight=False, pressCommand=(1, self.toggleNoiseEnabled))
        cmds.formLayout(attributeListFormLayout, e=True,
                        attachForm=[
                            (attributeListHeader, "top", 5), (attributeListHeader, "left", 0),
                            (resetChangesButton, "top", 0), (resetChangesButton, "right", 5),
                            (self.attributeList, "bottom", 0), (self.attributeList, "left", 0), (self.attributeList, "right", 0)
                            ],
                        attachControl=[
                            (self.attributeList, "top", 10, attributeListHeader)
                            ]
                        )
        cmds.setParent("..")
        
        cmds.setParent("..")
        
        shareLayout = cmds.frameLayout(label="Share Noise Attributes")
        shareFormLayout = cmds.formLayout()
        
        column1Layout = cmds.columnLayout()
        self.shareAttributesCheckBox = cmds.checkBox(label="Share Attributes", changeCommand=self.setShareAttributes, ann="With sharing enabled, you can make multiple attributes on each node use the same Noise Parameters.")
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Share Label")
        self.shareLabelTextField = cmds.textField(width=100, changeCommand=self.setShareLabel, ann="When sharing, you can have multiple Noise Parameters \"Groups\". The parameters are shared among each group.\nFor instance, you can have a group \"Translation\" with translateX, translateY and translateZ sharing their noise parameters and another group \"Rotation\" for the rotation attributes.\nUse the Share Label to identify these groups (or leave it blank if you don't want to use groups).")
        cmds.setParent("..")
        cmds.setParent("..")
        
        column2Layout = cmds.columnLayout()
        self.shareEnabledCheckBox = cmds.checkBox(label="Share Enabled", changeCommand=self.setShareEnabled, ann="Shares the Noise Enabled parameter.\nSharing this will turn on or off all the noises on the group at once.")
        self.shareSeedCheckBox = cmds.checkBox(label="Share Seed", changeCommand=self.setShareSeed, ann="Shares the Noise Seed parameter.\nSharing seeds is usefull so you don't have to modify several parameters when you just want a different general noise.")
        self.offsetSeedCheckBox = cmds.checkBox(label="Apply Seed Offset", changeCommand=self.setOffsetSeed, ann="If you share the seed, each noise will be identical. This will offset each attribute's seed while still sharing the same base seed.\nSharing seeds is usefull so you don't have to modify several parameters when you just want a different general noise.")
        cmds.setParent("..")
        
        column3Layout = cmds.columnLayout()
        self.shareIntensityCheckBox = cmds.checkBox(label="Share Intensity", changeCommand=self.setShareIntensity, ann="Shares the Noise Intensity parameter.")
        self.shareFrequencyCheckBox = cmds.checkBox(label="Share Frequency", changeCommand=self.setShareFrequency, ann="Shares the Noise Frequency parameter.")
        self.shareJerkCheckBox = cmds.checkBox(label="Share Jerk", changeCommand=self.setShareJerk, ann="Shares the Noise Jerk parameter.")
        cmds.setParent("..")
        
        cmds.formLayout(shareFormLayout, e=True,
                        attachForm=[
                            (column1Layout, "top", 0), (column1Layout, "bottom", 0), (column1Layout, "left", 0),
                            (column2Layout, "top", 0), (column2Layout, "bottom", 0),
                            (column3Layout, "top", 0), (column3Layout, "bottom", 0),
                        ],
                        attachControl=[
                            (column2Layout, "left", 5, column1Layout),
                            (column3Layout, "left", 5, column2Layout),
                        ]
                        )
        
        cmds.setParent("..")
        cmds.setParent("..")
        
        cmds.formLayout(mainFormLayout, e=True,
                        attachForm=[
                            (self.layerComboBox, "top", 0), (self.layerComboBox, "right", 0),
                            (self.useLayerCheckBox, "top", 0),
                            (paneLayout, "left", 0), (paneLayout, "right", 0),
                            (shareLayout, "left", 0), (shareLayout, "bottom", 0), (shareLayout, "right", 0)
                        ],
                        attachControl=[
                            (self.useLayerCheckBox, "right", 10, self.layerComboBox),
                            (paneLayout, "top", 10, self.layerComboBox), (paneLayout, "bottom", 10, shareLayout)
                        ]
                        )
    
    def passFn(self, *args):
        pass
    
    def updateLayerList(self):
        selectedLayer = cmds.optionMenu(self.layerComboBox, q=True, value=True) if cmds.optionMenu(self.layerComboBox, q=True, numberOfItems=True) > 0 else AddNoiseToAttributesOptionBox.selectedLayer
        
        cmds.optionMenu(self.layerComboBox, e=True, deleteAllItems=True)
        
        cmds.menuItem(label=AddNoiseToAttributesOptionBox.COMBOBOX_CURRENT_LAYER_OPTION, parent=self.layerComboBox)
        cmds.menuItem(divider=True)
        
        layers = AnimLayerUtils.getAnimLayers()
        for layer in layers:
            cmds.menuItem(label=layer, parent=self.layerComboBox)
        
        if selectedLayer != None and selectedLayer in layers:
            cmds.optionMenu(self.layerComboBox, e=True, value=selectedLayer)
            
    def setUseLayer(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.useLayer = state
        if updateCheckBox:
            cmds.checkBox(self.useLayerCheckBox, e=True, value=state)
            
        cmds.optionMenu(self.layerComboBox, e=True, en=state)
        self.onAnimLayerSelected()
            
    def setShareAttributes(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareAttributes = state
        if updateCheckBox:
            cmds.checkBox(self.shareAttributesCheckBox, e=True, value=state)
            
        cmds.checkBox(self.shareEnabledCheckBox, e=True, en=state)
        cmds.checkBox(self.shareSeedCheckBox, e=True, en=state)
        cmds.checkBox(self.offsetSeedCheckBox, e=True, en=state and AddNoiseToAttributesOptionBox.shareSeed)
        cmds.checkBox(self.shareIntensityCheckBox, e=True, en=state)
        cmds.checkBox(self.shareFrequencyCheckBox, e=True, en=state)
        cmds.checkBox(self.shareJerkCheckBox, e=True, en=state)
        cmds.textField(self.shareLabelTextField, e=True, en=state)
            
    def setShareEnabled(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareEnabled = state
        if updateCheckBox:
            cmds.checkBox(self.shareEnabledCheckBox, e=True, value=state)
            
    def setShareSeed(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareSeed = state
        if updateCheckBox:
            cmds.checkBox(self.shareSeedCheckBox, e=True, value=state)
            
        cmds.checkBox(self.offsetSeedCheckBox, e=True, en=state and AddNoiseToAttributesOptionBox.shareAttributes)
            
    def setOffsetSeed(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.offsetSeed = state
        if updateCheckBox:
            cmds.checkBox(self.offsetSeedCheckBox, e=True, value=state)
            
    def setShareIntensity(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareIntensity = state
        if updateCheckBox:
            cmds.checkBox(self.shareIntensityCheckBox, e=True, value=state)
            
    def setShareFrequency(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareFrequency = state
        if updateCheckBox:
            cmds.checkBox(self.shareFrequencyCheckBox, e=True, value=state)
            
    def setShareJerk(self, state, updateCheckBox=False):
        AddNoiseToAttributesOptionBox.shareJerk = state
        if updateCheckBox:
            cmds.checkBox(self.shareJerkCheckBox, e=True, value=state)
            
    def setShareLabel(self, text, updateTextField=False):
        AddNoiseToAttributesOptionBox.shareLabel = text
        if updateTextField:
            cmds.textField(self.shareLabelTextField, e=True, text=text)
            
    def getSelectedLayer(self):
        if AddNoiseToAttributesOptionBox.useLayer and cmds.optionMenu(self.layerComboBox, q=True, numberOfItems=True) > 0:
            layer = cmds.optionMenu(self.layerComboBox, q=True, value=True)
            if layer == AddNoiseToAttributesOptionBox.COMBOBOX_CURRENT_LAYER_OPTION:
                layer = ""  # This is the convention for using the current layer defined on the Noise module
        else:
            layer = None
        return layer
    
    def onAnimLayerSelected(self, arg=None):  # The extra argument comes from callbacks and we don't need it
        self.resetChanges()
        AddNoiseToAttributesOptionBox.selectedLayer = self.getSelectedLayer()
    
    def onAnimLayerRefresh(self):
        if self.getSelectedLayer() == "":
            self.updateAttributeIcons()
        
    def getNodesOnList(self):
        return cmds.treeView(self.nodeList, q=True, children=True) or []
    
    def addSelectedNodesToList(self, arg=None):  # The extra argument comes from callbacks and we don't need it
        nodes = self.getNodesOnList()
        selection = cmds.ls(selection=True, type="transform") or []
        for node in selection:
            if node not in nodes:
                nodes.append(node)
        self.setNodesOnList(nodes)
    
    def setNodesOnList(self, nodes):
        cmds.treeView(self.nodeList, e=True, removeAll=True)
        for node in nodes:
            self.addNodeToList(node, updateAttributesList=False)
        self.updateAttributeList()
    
    def addNodeToList(self, node, updateAttributesList=True):
        cmds.treeView(self.nodeList, e=True, addItem=(node, ""))
        cmds.treeView(self.nodeList, e=True, image=(node, 1, "delete.png"), buttonTooltip=(node, 1, "Removes this node from the list."))
        if updateAttributesList:
            self.updateAttributeList()
    
    def removeNodeFromList(self, node, arg=None, updateAttributesList=True):  # The extra argument comes from callbacks and we don't need it
        cmds.treeView(self.nodeList, e=True, removeItem=node)
        if updateAttributesList:
            self.updateAttributeList()
    
    def updateAttributeList(self, arg=None):  # The extra argument comes from callbacks and we don't need it
        cmds.treeView(self.attributeList, e=True, removeAll=True)
        
        nodes = self.getNodesOnList()
        commonAttributes = {}
        for node in nodes:
            attributes = cmds.listAttr(node, keyable=True)
            for attribute in attributes:
                if attribute not in commonAttributes:
                    commonAttributes[attribute] = []
                commonAttributes[attribute].append(node)
        
        newChanges = {}
        nodeCount = len(nodes)
        for attribute, info in commonAttributes.items():
            if len(info) == nodeCount:  # This means the attribute is present on all nodes
                cmds.treeView(self.attributeList, e=True, addItem=(attribute, ""))
                if attribute in self.changes:
                    newChanges[attribute] = self.changes[attribute]
        self.changes = newChanges
                
        self.updateAttributeIcons()
    
    def getNoisedAttributes(self, nodes=None):
        if nodes == None:
            nodes = self.getNodesOnList()
        noisedAttributes = {}
        for node in nodes:
            attrs = Noise.getAttributesWithNoise(node, layer=self.getSelectedLayer(), plugs=False)
            for attr in attrs:
                if attr not in noisedAttributes:
                    noisedAttributes[attr] = []
                noisedAttributes[attr].append(node)
        return noisedAttributes
    
    def toggleNoiseEnabled(self, attribute, arg=None):   # The extra argument comes from callbacks and we don't need it
        nodes = self.getNodesOnList()
        noisedAttributes = self.getNoisedAttributes(nodes=nodes)
        if attribute in self.changes:
            state = not self.changes[attribute]
            if (state and len(noisedAttributes[attribute]) == len(nodes)) or (not state and attribute not in noisedAttributes):
                self.changes.pop(attribute)
            else:
                self.changes[attribute] = state
        else:
            self.changes[attribute] = attribute not in noisedAttributes or len(noisedAttributes[attribute]) != len(nodes)
        self.updateAttributeIcons()
    
    def resetChanges(self, arg=None):   # The extra argument comes from callbacks and we don't need it
        self.changes = {}
        self.updateAttributeIcons()
    
    def updateAttributeIcons(self):
        nodes = self.getNodesOnList()
        noisedAttributes = self.getNoisedAttributes(nodes=nodes)
        
        attributes = cmds.treeView(self.attributeList, q=True, children=True) or []
        nodeCount = len(nodes)
        for attribute in attributes:
            attributeChanged = attribute in self.changes
            cmds.treeView(self.attributeList, e=True, textColor=(attribute, 1, 0.5, 0.5) if attributeChanged else (attribute, 0.73, 0.73, 0.73))
            if (attributeChanged and not self.changes[attribute]) or (not attributeChanged and attribute not in noisedAttributes):
                cmds.treeView(self.attributeList, e=True, image=(attribute, 1, "precompExportUnchecked.png"), buttonTooltip=(attribute, 1, "Noise NOT ENABLED."))
            elif (attributeChanged and self.changes[attribute]) or (not attributeChanged and len(noisedAttributes[attribute]) == nodeCount):
                cmds.treeView(self.attributeList, e=True, image=(attribute, 1, "precompExportChecked.png"), buttonTooltip=(attribute, 1,"Noise ENABLED."))
            else:
                cmds.treeView(self.attributeList, e=True, image=(attribute, 1, "precompExportPartial.png"), buttonTooltip=(attribute, 1,"WARNING! Noise enabled for some nodes only."))
    
    def onApply(self):
        nodes = self.getNodesOnList()
        noisedAttributes = self.getNoisedAttributes(nodes=nodes)
        
        noisesToAdd = {}
        noisesToRemove = {}
        for attribute, state in self.changes.items():
            for node in nodes:
                if state and (attribute not in noisedAttributes or node not in noisedAttributes[attribute]):
                    if node not in noisesToAdd:
                        noisesToAdd[node] = []
                    noisesToAdd[node].append(attribute)
                elif not state and (attribute in noisedAttributes and node in noisedAttributes[attribute]):
                    if node not in noisesToRemove:
                        noisesToRemove[node] = []
                    noisesToRemove[node].append(attribute)
        
        layer = self.getSelectedLayer()
        
        for node, attributes in noisesToAdd.items():
            Noise.addNoiseToNode(node, attributes, layer=layer,
                                 sharedLabel=AddNoiseToAttributesOptionBox.shareLabel,
                                 shareEnabled=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.shareEnabled,
                                 shareSeed=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.shareSeed,
                                 applySeedOffset=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.offsetSeed,
                                 shareIntensity=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.shareIntensity,
                                 shareFrequency=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.shareFrequency,
                                 shareJerk=AddNoiseToAttributesOptionBox.shareAttributes and AddNoiseToAttributesOptionBox.shareJerk,
                                 )

        for node, attributes in noisesToRemove.items():
            Noise.removeNoiseFromNode(node, attributes, layer=layer)
        
        self.resetChanges()
