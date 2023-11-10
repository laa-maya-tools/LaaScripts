import maya.cmds as cmds
import pymel.core as pm

import RigUtils.RigChecker as rc

import WindowDockBase as wdBase

class RigCheckerWindow(wdBase.UIDockManager):
    def __init__(self, parent=None):
        super(RigCheckerWindow, self).__init__("CheckSkinInfluences", r"C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/RigUtils/RigChecker/Window/ui/rigcheckerui.ui")
        self.setWindowTitle("Rig Checker")
        
        self.resize(360,800)
        
        # Check buttons
        self.ui.jointVisibilityCheckButton.clicked.connect(self.CheckJointVisibility)
        self.ui.geometryGroupsCheckButton.clicked.connect(self.CheckGeometryGroups)
        self.ui.keyedMeshesCheckButton.clicked.connect(self.CheckKeyedMeshes)
        self.ui.freezedMeshesCheckButton.clicked.connect(self.CheckFreezedMeshes)
        self.ui.meshesDeformersCheckButton.clicked.connect(self.CheckMeshesDeformers)
        self.ui.jointsRotationCheckButton.clicked.connect(self.CheckJointsRotation)
        self.ui.jointsOrientCheckButton.clicked.connect(self.CheckJointsOrient)
        self.ui.jointsSegmentScaleCompensateCheckButton.clicked.connect(self.CheckJointsSegmentScaleCompensate)
        self.ui.bindPosesCheckButton.clicked.connect(self.CheckBindPoses)
        self.ui.dcsAsPointLocatorsCheckButton.clicked.connect(self.CheckDcsAsPointLocators)
        self.ui.basicDcsCheckButton.clicked.connect(self.CheckBasicDcs)
        self.ui.dcShotCheckButton.clicked.connect(self.CheckDcShot)
        self.ui.skeletonGroupVisibilityCheckButton.clicked.connect(self.CheckSkeletonGroupVisibility)
        self.ui.displayLayersCheckButton.clicked.connect(self.CheckDisplayLayers)
        self.ui.materialsCheckButton.clicked.connect(self.CheckMaterials)
        self.ui.fpsCheckButton.clicked.connect(self.CheckFps)
        self.ui.generatedActorCheckButton.clicked.connect(self.CheckGeneratedActor)
        self.ui.pastedNodesCheckButton.clicked.connect(self.CheckPastedNodes)
        self.ui.normalizedWeightsCheckButton.clicked.connect(self.CheckNormalizedWeights)
        self.ui.animFileCheckButton.clicked.connect(self.CheckAnimFile)
        
        self.ui.checkAllButton.clicked.connect(self.CheckAll)
        
        # Fix buttons
        self.ui.jointVisibilityFixButton.clicked.connect(self.FixJointVisibility)
        # self.ui.geometryGroupsFixButton.clicked.connect()
        self.ui.keyedMeshesFixButton.clicked.connect(self.FixKeyedMeshes)
        self.ui.freezedMeshesFixButton.clicked.connect(self.FixFreezedMeshes)
        # self.ui.meshesDeformersFixButton.clicked.connect()
        # self.ui.jointsRotationFixButton.clicked.connect()
        self.ui.jointsOrientFixButton.clicked.connect(self.FixJointsOrient)
        self.ui.jointsSegmentScaleCompensateFixButton.clicked.connect(self.FixJointsSegmentScaleCompensate)
        self.ui.bindPosesFixButton.clicked.connect(self.FixBindPoses)
        self.ui.dcsAsPointLocatorsFixButton.clicked.connect(self.FixDcsAsPointLocators)
        # self.ui.basicDcsFixButton.clicked.connect()
        self.ui.dcShotFixButton.clicked.connect(self.FixDcShot)
        self.ui.skeletonGroupVisibilityFixButton.clicked.connect(self.FixSkeletonGroupVisibility)
        self.ui.displayLayersFixButton.clicked.connect(self.FixDisplayLayers)
        self.ui.materialsFixButton.clicked.connect(self.FixMaterials)
        self.ui.fpsFixButton.clicked.connect(self.FixFps)
        # self.ui.generatedActorFixButton.clicked.connect()
        # self.ui.pastedNodesFixButton.clicked.connect()
        self.ui.normalizedWeightsFixButton.clicked.connect(self.FixNormalizedWeights)
        self.ui.animFileFixButton.clicked.connect(self.FixAnimFile)
        
        self.fixButtons = []
        self.fixButtons.append(self.ui.jointVisibilityFixButton)
        self.fixButtons.append(self.ui.geometryGroupsFixButton)
        self.fixButtons.append(self.ui.keyedMeshesFixButton)
        self.fixButtons.append(self.ui.freezedMeshesFixButton)
        self.fixButtons.append(self.ui.meshesDeformersFixButton)
        self.fixButtons.append(self.ui.jointsRotationFixButton)
        self.fixButtons.append(self.ui.jointsOrientFixButton)
        self.fixButtons.append(self.ui.jointsSegmentScaleCompensateFixButton)
        self.fixButtons.append(self.ui.bindPosesFixButton)
        self.fixButtons.append(self.ui.dcsAsPointLocatorsFixButton)
        self.fixButtons.append(self.ui.basicDcsFixButton)
        self.fixButtons.append(self.ui.dcShotFixButton)
        self.fixButtons.append(self.ui.skeletonGroupVisibilityFixButton)
        self.fixButtons.append(self.ui.displayLayersFixButton)
        self.fixButtons.append(self.ui.materialsFixButton)
        self.fixButtons.append(self.ui.fpsFixButton)
        self.fixButtons.append(self.ui.generatedActorFixButton)
        self.fixButtons.append(self.ui.pastedNodesFixButton)
        self.fixButtons.append(self.ui.normalizedWeightsFixButton)
        self.fixButtons.append(self.ui.animFileFixButton)
        
        for fixButton in self.fixButtons:
            # Wider button
            fixButton.setText("   " + fixButton.text() + "   ")
            # Keep size on hide
            self.RetainSizeWhenHidden(fixButton)
            # Disable
            fixButton.setEnabled(False)
        
        # Hide fixes without implementation
        self.ui.geometryGroupsFixButton.setVisible(False)
        self.ui.meshesDeformersFixButton.setVisible(False)
        self.ui.jointsRotationFixButton.setVisible(False)
        self.ui.basicDcsFixButton.setVisible(False)
        self.ui.generatedActorFixButton.setVisible(False)
        self.ui.pastedNodesFixButton.setVisible(False)
    
    def RetainSizeWhenHidden(self, widget):
        spRetain = widget.sizePolicy()
        spRetain.setRetainSizeWhenHidden(True)
        widget.setSizePolicy(spRetain)
    
    def showInfo(self, messages):
        if (messages != None and len(messages) > 0):
            currentInfo = self.ui.outputTextBrowser.toPlainText()
            for message in messages:
                currentInfo += message + "\n"
            self.ui.outputTextBrowser.setText(currentInfo)
            self.ui.outputTextBrowser.verticalScrollBar().setValue(self.ui.outputTextBrowser.verticalScrollBar().maximum())
    
    def DoCheck(self, function, label, fixButton):
        correctState, messages = function()
        if (correctState):
            label.setStyleSheet("background-color: green")
            if (fixButton.isVisible()):
                fixButton.setEnabled(False)
        else:
            label.setStyleSheet("background-color: red")
            if (fixButton.isVisible()):
                fixButton.setEnabled(True)
        self.showInfo(messages)
    
    def DoFix(self, function, label, fixButton):
        success = function()
        if (success):
            label.setStyleSheet("background-color: green")
            fixButton.setEnabled(False)
        else:
            label.setStyleSheet("background-color: red")
            fixButton.setEnabled(True)
    
    def CheckJointVisibility(self):
        self.ui.jointVisibilityLabel.setStyleSheet("")
        rigNode = rc.GetRigNode()
        if (rigNode):
            self.DoCheck(lambda: rc.CheckMgearJointVisibility(rigNode), self.ui.jointVisibilityLabel, self.ui.jointVisibilityFixButton)
        else:
            pm.confirmDialog(message="Check joint visibility: Error trying to find rig node", button="Close")
    
    def CheckGeometryGroups(self):
        self.ui.geometryGroupsLabel.setStyleSheet("")
        sceneMeshes = rc.GetSceneMeshes()
        self.DoCheck(lambda: rc.CheckGeometryGroups(sceneMeshes), self.ui.geometryGroupsLabel, self.ui.geometryGroupsFixButton)
    
    def CheckKeyedMeshes(self):
        self.ui.keyedMeshesLabel.setStyleSheet("")
        sceneMeshes = rc.GetSceneMeshes()
        self.DoCheck(lambda: rc.CheckKeyedMeshes(sceneMeshes), self.ui.keyedMeshesLabel, self.ui.keyedMeshesFixButton)
    
    def CheckFreezedMeshes(self):
        self.ui.freezedMeshesLabel.setStyleSheet("")
        actors = rc.GetSceneActors()
        meshes = rc.GetActorMeshes(actors)
        self.DoCheck(lambda: rc.CheckFreezedMeshes(meshes), self.ui.freezedMeshesLabel, self.ui.freezedMeshesFixButton)
    
    def CheckMeshesDeformers(self):
        self.ui.meshesDeformersLabel.setStyleSheet("")
        actorMeshes = rc.GetActorMeshes(rc.GetSceneActors())
        self.DoCheck(lambda: rc.CheckMeshesDeformers(actorMeshes), self.ui.meshesDeformersLabel, self.ui.meshesDeformersFixButton)
    
    def CheckJointsRotation(self):
        self.ui.jointsRotationLabel.setStyleSheet("")
        exportJoints = rc.GetExportJoints()
        self.DoCheck(lambda: rc.CheckJointsRotation(exportJoints), self.ui.jointsRotationLabel, self.ui.jointsRotationFixButton)
    
    def CheckJointsOrient(self):
        self.ui.jointsOrientLabel.setStyleSheet("")
        exportJoints = rc.GetExportJoints()
        self.DoCheck(lambda: rc.CheckJointsOrient(exportJoints), self.ui.jointsOrientLabel, self.ui.jointsOrientFixButton)
    
    def CheckJointsSegmentScaleCompensate(self):
        self.ui.jointsSegmentScaleCompensateLabel.setStyleSheet("")
        exportJoints = rc.GetExportJoints()
        self.DoCheck(lambda: rc.CheckJointsSegmentScaleCompensate(exportJoints), self.ui.jointsSegmentScaleCompensateLabel, self.ui.jointsSegmentScaleCompensateFixButton)
    
    def CheckBindPoses(self):
        self.ui.bindPosesLabel.setStyleSheet("")
        sceneMeshes = rc.GetSceneMeshes()
        skeletonGroup = rc.GetSkeletonGroup()
        nodesFound = False
        if (len(sceneMeshes) > 0  and skeletonGroup):
            nodesFound = True
        if (nodesFound):
            self.DoCheck(lambda: rc.CheckBindPoses(skeletonGroup, sceneMeshes), self.ui.bindPosesLabel, self.ui.bindPosesFixButton)
        else:
            if (len(sceneMeshes) == 0):
                pm.confirmDialog(message="Check bind poses: No meshes found in scene", button="Close")
            if (skeletonGroup == None):
                pm.confirmDialog(message="Check bind poses: Error trying to find skeleton group", button="Close")
    
    def CheckDcsAsPointLocators(self):
        self.ui.dcsAsPointLocatorsLabel.setStyleSheet("")
        dcsCtls = rc.GetDcsCtls()
        self.DoCheck(lambda: rc.CheckDcsAsPointLocators(dcsCtls), self.ui.dcsAsPointLocatorsLabel, self.ui.dcsAsPointLocatorsFixButton)
    
    def CheckBasicDcs(self):
        self.ui.basicDcsLabel.setStyleSheet("")
        dcsCtls = rc.GetDcsCtls()
        skeletonGroup = rc.GetSkeletonGroup()
        nodesFound = False
        if (len(dcsCtls) > 0  and skeletonGroup):
            nodesFound = True
        if (nodesFound):
            self.DoCheck(lambda: rc.CheckBasicDcs(skeletonGroup, dcsCtls), self.ui.basicDcsLabel, self.ui.basicDcsFixButton)
        else:
            if (len(dcsCtls) == 0):
                pm.confirmDialog(message="Check basic DCs: No DCs controls found in scene", button="Close")
            if (skeletonGroup == None):
                pm.confirmDialog(message="Check basic DCs: Error trying to find skeleton group", button="Close")
    
    def CheckDcShot(self):
        self.ui.dcShotLabel.setStyleSheet("")
        dcsCtls = rc.GetDcsCtls()
        self.DoCheck(lambda: rc.CheckDcShot(dcsCtls), self.ui.dcShotLabel, self.ui.dcShotFixButton)
    
    def CheckSkeletonGroupVisibility(self):
        self.ui.skeletonGroupVisibilityLabel.setStyleSheet("")
        skeletonGroup = rc.GetSkeletonGroup()
        if (skeletonGroup):
            self.DoCheck(lambda: rc.CheckSkeletonGroupVisibility(skeletonGroup), self.ui.skeletonGroupVisibilityLabel, self.ui.skeletonGroupVisibilityFixButton)
        else:
            pm.confirmDialog(message="Check skeleton group visibility: Error trying to find skeleton group", button="Close")
    
    def CheckDisplayLayers(self):
        self.ui.displayLayersLabel.setStyleSheet("")
        sceneDisplayLayers = rc.GetSceneDisplayLayers()
        self.DoCheck(lambda: rc.CheckDisplayLayers(sceneDisplayLayers), self.ui.displayLayersLabel, self.ui.displayLayersFixButton)
    
    def CheckMaterials(self):
        self.ui.materialsLabel.setStyleSheet("")
        sceneMaterials = rc.GetSceneMaterials()
        self.DoCheck(lambda: rc.CheckMaterials(sceneMaterials), self.ui.materialsLabel, self.ui.materialsFixButton)
    
    def CheckFps(self):
        self.ui.fpsLabel.setStyleSheet("")
        targetFps = 30
        self.DoCheck(lambda: rc.CheckFps(targetFps), self.ui.fpsLabel, self.ui.fpsFixButton)
    
    def CheckGeneratedActor(self):
        self.ui.generatedActorLabel.setStyleSheet("")
        sceneActors = rc.GetSceneActors()
        self.DoCheck(lambda: rc.CheckGeneratedActor(sceneActors), self.ui.generatedActorLabel, self.ui.generatedActorFixButton)
    
    def CheckPastedNodes(self):
        self.ui.pastedNodesLabel.setStyleSheet("")
        self.DoCheck(lambda: rc.CheckPastedNodes(), self.ui.pastedNodesLabel, self.ui.pastedNodesFixButton)
    
    def CheckNormalizedWeights(self):
        self.ui.normalizedWeightsLabel.setStyleSheet("")
        sceneActors = rc.GetSceneActors()
        self.DoCheck(lambda: rc.CheckNormalizedWeights(sceneActors), self.ui.normalizedWeightsLabel, self.ui.normalizedWeightsFixButton)
    
    def CheckAnimFile(self):
        self.ui.animFileLabel.setStyleSheet("")
        scenePath = rc.GetScenePath()
        self.DoCheck(lambda: rc.CheckAnimFile(scenePath), self.ui.animFileLabel, self.ui.animFileFixButton)
    
    def ClearLabelsStatus(self):
        self.ui.jointVisibilityLabel.setStyleSheet("")
        self.ui.geometryGroupsLabel.setStyleSheet("")
        self.ui.keyedMeshesLabel.setStyleSheet("")
        self.ui.freezedMeshesLabel.setStyleSheet("")
        self.ui.meshesDeformersLabel.setStyleSheet("")
        self.ui.jointsRotationLabel.setStyleSheet("")
        self.ui.jointsOrientLabel.setStyleSheet("")
        self.ui.jointsSegmentScaleCompensateLabel.setStyleSheet("")
        self.ui.bindPosesLabel.setStyleSheet("")
        self.ui.dcsAsPointLocatorsLabel.setStyleSheet("")
        self.ui.basicDcsLabel.setStyleSheet("")
        self.ui.dcShotLabel.setStyleSheet("")
        self.ui.skeletonGroupVisibilityLabel.setStyleSheet("")
        self.ui.displayLayersLabel.setStyleSheet("")
        self.ui.materialsLabel.setStyleSheet("")
        self.ui.fpsLabel.setStyleSheet("")
        self.ui.generatedActorLabel.setStyleSheet("")
        self.ui.pastedNodesLabel.setStyleSheet("")
        self.ui.normalizedWeightsLabel.setStyleSheet("")
        self.ui.animFileLabel.setStyleSheet("")
    
    def CheckAll(self):
        self.ClearLabelsStatus()
        
        self.CheckJointVisibility()
        self.CheckGeometryGroups()
        self.CheckKeyedMeshes()
        self.CheckFreezedMeshes()
        self.CheckMeshesDeformers()
        self.CheckJointsRotation()
        self.CheckJointsOrient()
        self.CheckJointsSegmentScaleCompensate()
        self.CheckBindPoses()
        self.CheckDcsAsPointLocators()
        self.CheckBasicDcs()
        self.CheckDcShot()
        self.CheckSkeletonGroupVisibility()
        self.CheckDisplayLayers()
        self.CheckMaterials()
        self.CheckFps()
        self.CheckGeneratedActor()
        self.CheckPastedNodes()
        self.CheckNormalizedWeights()
        self.CheckAnimFile()
    
    def FixJointVisibility(self):
        rigNode = rc.GetRigNode()
        if (rigNode):
            self.DoFix(lambda: rc.FixMgearJointVisibility(rigNode), self.ui.jointVisibilityLabel, self.ui.jointVisibilityFixButton)
        else:
            pm.confirmDialog(message="Error trying to find rig node", button="Close")
    
    def FixKeyedMeshes(self):
        sceneMeshes = rc.GetSceneMeshes()
        self.DoFix(lambda: rc.FixKeyedMeshes(sceneMeshes), self.ui.keyedMeshesLabel, self.ui.keyedMeshesFixButton)
    
    def FixFreezedMeshes(self):
        actors = rc.GetSceneActors()
        meshes = rc.GetActorMeshes(actors)
        self.DoFix(lambda: rc.FixFreezedMeshes(meshes), self.ui.freezedMeshesLabel, self.ui.freezedMeshesFixButton)
    
    def FixJointsOrient(self):
        exportJoints = rc.GetExportJoints()
        self.DoFix(lambda: rc.FixJointsOrient(exportJoints), self.ui.jointsOrientLabel, self.ui.jointsOrientFixButton)
    
    def FixJointsSegmentScaleCompensate(self):
        exportJoints = rc.GetExportJoints()
        self.DoFix(lambda: rc.FixJointsSegmentScaleCompensate(exportJoints), self.ui.jointsSegmentScaleCompensateLabel, self.ui.jointsSegmentScaleCompensateFixButton)
    
    def FixBindPoses(self):
        sceneMeshes = rc.GetSceneMeshes()
        skeletonGroup = rc.GetSkeletonGroup()
        nodesFound = False
        if (len(sceneMeshes) > 0  and skeletonGroup):
            nodesFound = True
        if (nodesFound):
            self.DoFix(lambda: rc.FixBindPoses(skeletonGroup, sceneMeshes), self.ui.bindPosesLabel, self.ui.bindPosesFixButton)
        else:
            if (len(sceneMeshes) == 0):
                pm.confirmDialog(message="No meshes found in scene", button="Close")
            if (skeletonGroup == None):
                pm.confirmDialog(message="Error trying to find skeleton group", button="Close")
    
    def FixDcsAsPointLocators(self):
        dcsCtls = rc.GetDcsCtls()
        self.DoFix(lambda: rc.FixDcsAsPointLocators(dcsCtls), self.ui.dcsAsPointLocatorsLabel, self.ui.dcsAsPointLocatorsFixButton)
    
    def FixDcShot(self):
        dcsCtls = rc.GetDcsCtls()
        self.DoFix(lambda: rc.FixDcShot(dcsCtls), self.ui.dcShotLabel, self.ui.dcShotFixButton)
    
    def FixSkeletonGroupVisibility(self):
        skeletonGroup = rc.GetSkeletonGroup()
        if (skeletonGroup):
            self.DoFix(lambda: rc.FixSkeletonGroupVisibility(skeletonGroup), self.ui.skeletonGroupVisibilityLabel, self.ui.skeletonGroupVisibilityFixButton)
        else:
            pm.confirmDialog(message="Error trying to find skeleton group", button="Close")
    
    def FixDisplayLayers(self):
        sceneDisplayLayers = rc.GetSceneDisplayLayers()
        self.DoFix(lambda: rc.FixDisplayLayers(sceneDisplayLayers), self.ui.displayLayersLabel, self.ui.displayLayersFixButton)
    
    def FixMaterials(self):
        sceneMaterials = rc.GetSceneMaterials()
        self.DoFix(lambda: rc.FixMaterials(sceneMaterials), self.ui.materialsLabel, self.ui.materialsFixButton)
    
    def FixFps(self):
        targetFps = 30
        self.DoFix(lambda: rc.FixFps(targetFps), self.ui.fpsLabel, self.ui.fpsFixButton)
    
    def FixNormalizedWeights(self):
        sceneActors = rc.GetSceneActors()
        self.DoFix(lambda: rc.FixNormalizedWeights(sceneActors), self.ui.normalizedWeightsLabel, self.ui.normalizedWeightsFixButton)
    
    def FixAnimFile(self):
        scenePath = rc.GetScenePath()
        self.DoFix(lambda: rc.FixAnimFile(scenePath), self.ui.animFileLabel, self.ui.animFileFixButton)

if __name__ == "__main__":
    try:
        if rigCheckerWindow.isVisible():
            rigCheckerWindow.close()
    except NameError:
        pass
    rigCheckerWindow = RigCheckerWindow()
    rigCheckerWindow.show()
