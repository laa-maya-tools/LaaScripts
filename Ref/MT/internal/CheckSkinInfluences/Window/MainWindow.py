import WindowDockBase               as wdBase
import RigUtils.Skinning    as RigSkin

import pymel.core as pm
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim

# TODO: Optimize the reading of overweighted vertices. It increases the reading time on each execution.
# Based on the algorithm on: https://gist.github.com/chris-lesage/5d8eb501915e4a6335e7eb00aedad7d0


class CheckSkinInfluencesWindow(wdBase.UIDockManager):
    # ############################################################################
    # ################################ Properties ################################
    # ############################################################################
    @property
    def maxInfluences(self):
        return self.ui.spn_maxInfluences.value()
    
    @property
    def pruneValue(self):
        return self.ui.spn_pruneValue.value()
    
    @pruneValue.setter
    def pruneValue(self, value):
        self.ui.spn_pruneValue.setValue(value)
    
    @property
    def pruneGrowValue(self):
        return self.ui.spn_growValue.value()
    
    @property
    def pruneOperation(self):
        if (self.ui.rad_selVerts.isChecked()):
            return 0
        else:
            return 1
    
    # ############################################################################
    # ################################# Functions ################################
    # ############################################################################
    def __init__(self, parent=None):
        super(CheckSkinInfluencesWindow, self).__init__("CheckSkinInfluences", r"CheckSkinInfluences/Window/ui/checkskininfluences.ui")
        self.setWindowTitle('Check Skin Influences')
        
        self.ui.btn_checkMaxInfluences.clicked.connect(self.btn_checkMaxInfluences_clicked)
        self.ui.btn_prune.clicked.connect(self.btn_prune_clicked)
        self.ui.btn_addAndPrune.clicked.connect(self.btn_addAndPrune_clicked)
        self.ui.btn_clearTxt.clicked.connect(self.btn_clearTxt_clicked)
    
    
    def checkInfluences(self, mesh, maxInfluences):
        skinCluster = RigSkin.FindRelatedSkinCluster(mesh)
            
        #pm.skinPercent(skinCluster, mesh)
        # get the MFnSkinCluster for skinCluster
        selList = OpenMaya.MSelectionList()
        selList.add(skinCluster.name())
        clusterNode = OpenMaya.MObject()
        selList.getDependNode(0, clusterNode)
        skinFn = OpenMayaAnim.MFnSkinCluster(clusterNode)
        
        # get the MDagPath for all influence
        infDags = OpenMaya.MDagPathArray()
        skinFn.influenceObjects(infDags)
        
        # create a dictionary whose key is the MPlug indice id and
        # whose value is the influence list id
        infIds = {}
        infs = []
        for x in range(infDags.length()):
            infPath = infDags[x].fullPathName()
            infId = int(skinFn.indexForInfluenceObject(infDags[x]))
            infIds[infId] = x
            infs.append(infPath)
            
        # get the MPlug for the weightList and weights attributes
        wlPlug = skinFn.findPlug('weightList')
        wPlug = skinFn.findPlug('weights')
        wlAttr = wlPlug.attribute()
        wAttr = wPlug.attribute()
        wInfIds = OpenMaya.MIntArray()
        
        # the weights are stored in dictionary, the key is the vertId,
        # the value is another dictionary whose key is the influence id and
        # value is the weight for that influence
        weights = {}
        for vId in range(wlPlug.numElements()):
            vWeights = {}
            # tell the weights attribute which vertex id it represents
            wPlug.selectAncestorLogicalIndex(vId, wlAttr)
            
            # get the indice of all non-zero weights for this vert
            wPlug.getExistingArrayAttributeIndices(wInfIds)
            
            # create a copy of the current wPlug
            infPlug = OpenMaya.MPlug(wPlug)
            for infId in wInfIds:
                # tell the infPlug it represents the current influence id
                infPlug.selectAncestorLogicalIndex(infId, wAttr)
                
                # add this influence and its weight to this verts weights
                try:
                    vWeights[infIds[infId]] = infPlug.asDouble()
                except KeyError:
                    # assumes a removed influence
                    pass
            weights[vId] = vWeights
            
        overWeighted = [x for x in weights.keys() if len(weights[x]) > maxInfluences]
        
        return overWeighted
    
    def InitProcess(self, meshes):
        if (len(meshes) == 0):
            self.ui.txt_result.appendPlainText("--- Select anything first, please ---\n")
            return False
        
        # NOTE: This is a bit of a selection hack. The purpose is this:
        # Even if I have component or object selected, it will search the proper mesh
        # And it puts me into component mode so I can instantly work with the weights
        # And it doesn't remove the transform from my selection list, so I can keep working on the same mesh
        # AND it clears the existing component selection (if you don't, it causes bugs.)
        pm.selectMode(object=True)  # this lets you have components selected when running the script
        for node in meshes:
            pm.selectMode(component=True)
            pm.select(node.vtx, d=True)  # first, clear any vtx selection
        pm.selectMode(object=True)
        return True
    
    # ##############################################################################
    # ################################ Slots #######################################
    # ##############################################################################
    def btn_checkMaxInfluences_clicked(self):
        selection = pm.selected(type='transform')
        
        if (self.InitProcess(selection)):
            for node in selection:
                self.ui.txt_result.appendPlainText("##### {} #####".format(node.getName()))
                overWeighted = self.checkInfluences(node, self.maxInfluences)
                
                if len(overWeighted) == 0:
                    pm.select(node.vtx, d=True)
                    self.ui.txt_result.appendPlainText(("- OK: {} max influences").format(self.maxInfluences))
                else:
                    self.ui.txt_result.appendPlainText("- WARNING: {} overweighted vertices".format(len(overWeighted)))
                    pm.selectMode(component=True)
                    overWeightedVertices = [node.vtx[x] for x in overWeighted]
                    pm.select(overWeightedVertices, add=True)
                
                self.ui.txt_result.appendPlainText("")
    
    def btn_prune_clicked(self):
        selection = pm.selected(type='transform')
        
        if (self.InitProcess(selection)):
            for node in selection:
                self.ui.txt_result.appendPlainText("##### {} #####".format(node.getName()))
                overWeighted = self.checkInfluences(node, self.maxInfluences)
                
                if len(overWeighted) > 0:
                    self.ui.txt_result.appendPlainText("- BEFORE: {} overweighted vertices".format(len(overWeighted)))
                    skinCluster = RigSkin.FindRelatedSkinCluster(node)
                    pruneTarget = node
                    if (self.pruneOperation == 0):
                        pruneTarget = [node.vtx[x] for x in overWeighted]
                    pm.skinPercent(skinCluster, pruneTarget , pruneWeights=self.pruneValue)
                    
                    refreshedOverWeighted = self.checkInfluences(node, self.maxInfluences)
                    self.ui.txt_result.appendPlainText("- AFTER: {} overweighted vertices".format(len(refreshedOverWeighted)))
                    pm.select(node.vtx, d=True)
                    overWeightedVertices = [node.vtx[x] for x in refreshedOverWeighted]
                    pm.select(overWeightedVertices, add=True)
                else:
                    self.ui.txt_result.appendPlainText(("- No overweighted vertices to prune").format(self.maxInfluences))
                self.ui.txt_result.appendPlainText("")
                
    def btn_addAndPrune_clicked(self):
        self.pruneValue = self.pruneValue + self.pruneGrowValue
        self.btn_prune_clicked()
    
    def btn_clearTxt_clicked(self):
        self.ui.txt_result.clear()


if __name__ == '__main__':
    try:
        if checkSkinInfluencesWindow.isVisible():
            checkSkinInfluencesWindow.close()
    except NameError:
        pass
    checkSkinInfluencesWindow = CheckSkinInfluencesWindow()
    checkSkinInfluencesWindow.show()