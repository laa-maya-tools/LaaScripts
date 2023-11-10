import os
import ActorManager
import maya.cmds                    as cmds
import maya.mel                     as mel
import QtCustomWidgets.UIFileWidget as UIFileWidget
from maya.app.general.mayaMixin     import MayaQWidgetBaseMixin
from xml.dom                        import minidom
from ProjectPath                    import PathTokenizer, Tokens
from PySide2                        import QtCore, QtGui, QtWidgets

class ModelCheckerUI(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    refreshIcon = QtGui.QImage(":/refresh.png").copy(1, 1, 18, 18)
    __ui_path__ = os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), r'ModelChecker\modelChecker.ui')

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, self.__ui_path__, parent=parent)
        self.setObjectName('ModelChecker')
        self.setWindowTitle('Model Checker')

        self.meshesDict = {}
        self.ui.actorsWidget = None
        self.getGeometry()
        # icons
        self.ui.refreshUIQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/refresh.png").copy(1, 1, 18, 18) )))
        self.ui.refreshOutputQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/refresh.png").copy(1, 1, 18, 18) )))
        self.ui.actorSceneSelectQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        self.ui.subActorSceneSelectQButton.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage( QtGui.QImage(":/selectModel.png").copy(1, 1, 25, 25) )))
        # check
        self.ui.allCheckersQCheck.clicked.connect(self.allCheckersFunc)
        
        self.ui.generalCheckersQCheck.clicked.connect(self.generalCheckersFunc)
        self.ui.polyCheckersQCheck.clicked.connect(self.polyCheckersFunc)
        self.ui.transformCheckersQCheck.clicked.connect(self.transformCheckersFunc)
        self.ui.skinCheckersQCheck.clicked.connect(self.skinCheckersFunc)

        self.refreshUIFunc()
        self.ui.actorsQBox.setEnabled(False)
        self.ui.subActorsQBox.setEnabled(False)

        # buttons clicked connections
        self.ui.actorSceneSelectQButton.clicked.connect(self.qListSelectFunc)
        self.ui.subActorSceneSelectQButton.clicked.connect(self.qListSelectFunc)
        self.ui.subActorPathQButton.clicked.connect(self.subActorPathFunc)
        self.ui.refreshUIQButton.clicked.connect(self.refreshUIFunc)
        self.ui.refreshOutputQButton.clicked.connect(self.ui.outputInfoQText.clear)
        self.ui.actorsQList.itemSelectionChanged.connect(self.actorSelected)
        self.ui.subActorsQList.itemSelectionChanged.connect(self.subActorsSelected)
        self.ui.mdlIMatsInSceneQButton.clicked.connect(self.mdlIMatsInSceneFunc)
        self.ui.jorientQButton.clicked.connect(self.jorientFunc)
        #
        self.ui.uselessSkinClustersQButton.clicked.connect(self.uselessSkinClustersFunc)
        self.ui.uselessSkinClustersDelQButton.clicked.connect(self.uselessSkinClustersDelFunc)
        #
        self.ui.uselessBindPosesQButton.clicked.connect(self.uselessBindPosesInfoFunc)
        self.ui.uselessBindPosesDelQButton.clicked.connect(self.uselessBindPosesDelFunc)
        #
        self.ui.skinClusterMaxInfQSpin.valueChanged.connect(self.skinClusterMaxInfQSpinFunc)
        #
        self.ui.skinClusterMaxInfQButton.clicked.connect(self.skinClusterMaxInfFunc)
        #
        self.ui.multipleBindPosesInfoQButton.clicked.connect(self.bindPosesInfoFunc)
        self.ui.multipleBindPosesFixQButton.clicked.connect(self.bindPosesFixFunc)
        #
        self.ui.deformersQButton.clicked.connect(self.deformersFunc)
        self.ui.componentsActiveQButton.clicked.connect(self.componentSelectionFunc)
        self.ui.componentsActiveCleanQButton.clicked.connect(self.componentSelectionCleanFunc)
        self.ui.ngonsQButton.clicked.connect(self.ngonsFunc)
        self.ui.ngonsSelectQButton.clicked.connect(self.ngonsSelectFunc)
        self.ui.invalidVertexQButton.clicked.connect(self.invalidVertexFunc)
        self.ui.invalidVertexSelectQButton.clicked.connect(self.invalidVertexSelectFunc)
        self.ui.pivotsQButton.clicked.connect(self.pivotsFunc)
        self.ui.matrixQButton.clicked.connect(self.matrixFunc)
        self.ui.skinClusterQButton.clicked.connect(self.skinClusterFunc)
        self.ui.skinClusterInfluencesQButton.clicked.connect(self.skinClusterInfluencesFunc)
        self.ui.applyQButton.clicked.connect(self.applyFunc)
        self.ui.actorsSelectionQRadio.toggled.connect(self.actorsToogleFunc)
        
    #checkers
    def allCheckersFunc(self):
        val = self.ui.allCheckersQCheck.isChecked()
        for wdgName, wdg in self.ui.__dict__.items():
            if "QCheck" in wdgName:
                wdg.setChecked(val)
    
    def generalCheckersFunc(self):
        val = self.ui.generalCheckersQCheck.isChecked()
        self.ui.skinClusterMaxInfQCheck.setChecked(val)
        self.ui.uselessSkinClustersQCheck.setChecked(val)
        self.ui.uselessBindPosesQCheck.setChecked(val)
        self.ui.jorientQCheck.setChecked(val)
    
    def polyCheckersFunc(self):
        val = self.ui.polyCheckersQCheck.isChecked()
        self.ui.deformersQCheck.setChecked(val)
        self.ui.componentsActiveQCheck.setChecked(val)
        self.ui.ngonsQCheck.setChecked(val)
        self.ui.invalidVertexQCheck.setChecked(val)

    def transformCheckersFunc(self):
        val = self.ui.transformCheckersQCheck.isChecked()
        self.ui.pivotsQCheck.setChecked(val)
        self.ui.matrixQCheck.setChecked(val)

    def skinCheckersFunc(self):
        val = self.ui.skinCheckersQCheck.isChecked()
        self.ui.skinClusterQCheck.setChecked(val)
        self.ui.skinClusterInfluencesQCheck.setChecked(val)
        self.ui.multipleBindPosesQCheck.setChecked(val)
    
    #ui funcs
    def jorientFunc(self):
        if self.ui.actorsSelectionQRadio.isChecked():
            joints = []
            actorsSelected = [elem.text() for elem in self.ui.actorsQList.selectedItems()]
            subActorsSelected = [elem.text() for elem in self.ui.subActorsQList.selectedItems()]
            if not actorsSelected:
                return
            for actor in ActorManager.getActors():
                for subactor in actor.getSubActors():
                    if not subActorsSelected or subactor.node in subActorsSelected:
                        joints.extend( [jnt for jnt in subactor.getJointNodes() if cmds.nodeType(jnt) == "joint"] )
        elif self.ui.sceneSelectionQRadio.isChecked():
            joints = cmds.ls(sl=True, type='joint')
        else:
            joints = cmds.ls(type='joint')
        currentText = self.ui.outputInfoQText.toPlainText()
        addText = ""
        for jnt in joints:
            jo = cmds.getAttr(jnt + ".jo")[0]
            if jo != (0,0,0):
                addText += "{}: {}\n".format(jnt, jo)
        currentText += "################## Joints with non zero joint orient:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)

    def uselessSkinClustersDelFunc(self):
        cmds.delete(ModelChecker.uselessSkinClustersCheck())
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Non connected Skin Clusters removed"
        self.ui.outputInfoQText.setText(currentText)

    def uselessBindPosesDelFunc(self):
        cmds.delete(ModelChecker.uselessBindPosesCheck())
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Non connected Dag Poses removed"
        self.ui.outputInfoQText.setText(currentText)

    def subActorsSelected(self):
        self.ui.mdlPathQText.setEnabled(True)
        self.ui.subActorPathQButton.setEnabled(True)
        if len(self.ui.subActorsQList.selectedItems()) >= 2:
            self.ui.mdlPathQText.setEnabled(False)
            self.ui.subActorPathQButton.setEnabled(False)

    def subActorPathFunc(self):
        subActorName = self.ui.subActorsQList.currentItem()
        if not subActorName:
            cmds.warning("No Sub-Actor selected")
            return
        custDict = {Tokens.TActorName : None, Tokens.TSubActorName : None, Tokens.TActorType : None}
        fullDict = PathTokenizer(custDict).GetFullDictionary()
        fullDict['ActorName'] = self.ui.actorsQList.currentItem().text()
        fullDict['SActorName'] = subActorName.text()
        fullDict['ActorType'] = cmds.attributeQuery('type',node=fullDict['ActorName'], le=True)[0].split(":")[cmds.getAttr( fullDict['ActorName'] + ".type" )]
        subActorPath = cmds.getAttr(subActorName.text() + ".modelPath")
        if not subActorPath:
            cmds.warning("No 'modelPath' attribute setted")
            return
        for token,value in fullDict.items():
            subActorPath = subActorPath.replace("{"+token+"}", value)
        self.ui.mdlPathQText.setText(subActorPath)

    def qListSelectFunc(self):
        iterableList = self.ui.actorsQList
        if "subActor" in self.sender().objectName():
            iterableList = self.ui.subActorsQList
        cmds.select(clear=True)
        for item in iterableList.selectedItems():
            cmds.select(item.text(), add=True)

    def refreshUIFunc(self):
        self.getGeometry()
        self.ui.actorsQList.clear()
        self.ui.actorsQList.addItems(cmds.ls(type='actor') or [])

    def actorSelected(self):
        self.ui.subActorsQList.clear()
        for item in self.ui.actorsQList.selectedItems():
            self.ui.subActorsQList.addItems(cmds.listConnections(item.text() + ".subActorList") or [])
    
    def getGeometry(self):
        if self.ui.actorsSelectionQRadio.isChecked():
            geometries = []
            actorsSelected = [elem.text() for elem in self.ui.actorsQList.selectedItems()]
            subActorsSelected = [elem.text() for elem in self.ui.subActorsQList.selectedItems()]
            if not actorsSelected:
                return
            for actor in ActorManager.getActors():
                for subactor in actor.getSubActors():
                    if not subActorsSelected or subactor.node in subActorsSelected:
                        geometries.extend( subactor.getGeometryNodes() )
        elif self.ui.allSceneQRadio.isChecked():
            geometries = [mesh for mesh in cmds.ls(type='mesh') if "Orig" not in mesh]
        else:
            geometries = cmds.ls(selection=True)
        self.meshesDict = {mesh:ModelChecker(mesh) for mesh in geometries}

    def actorsToogleFunc(self):
        self.ui.actorsQBox.setEnabled(False)
        self.ui.subActorsQBox.setEnabled(False)
        #self.ui.iMatsQBox.setEnabled(False)
        if self.ui.actorsSelectionQRadio.isChecked():
            self.ui.actorsQBox.setEnabled(True)
            self.ui.subActorsQBox.setEnabled(True)
            #self.ui.iMatsQBox.setEnabled(True)

    def skinClusterMaxInfQSpinFunc(self):
        ModelChecker.maxInfluences = self.ui.skinClusterMaxInfQSpin.value()
    
    def applyFunc(self):
        #
        if self.ui.mdlIMatsInSceneQCheck.isChecked(): self.mdlIMatsInSceneFunc()
        #
        if self.ui.skinClusterMaxInfQCheck.isChecked(): self.skinClusterMaxInfFunc()
        if self.ui.uselessSkinClustersQCheck.isChecked(): self.uselessSkinClustersFunc()
        if self.ui.uselessBindPosesQCheck.isChecked(): self.uselessBindPosesInfoFunc()
        if self.ui.jorientQCheck.isChecked(): self.jorientFunc()
        #
        if self.ui.skinClusterQCheck.isChecked(): self.skinClusterFunc()
        if self.ui.skinClusterInfluencesQCheck.isChecked(): self.skinClusterInfluencesFunc()
        if self.ui.multipleBindPosesQCheck.isChecked(): self.bindPosesInfoFunc()
        #
        if self.ui.deformersQCheck.isChecked(): self.deformersFunc()
        if self.ui.componentsActiveQCheck.isChecked(): self.componentSelectionFunc()
        if self.ui.ngonsQCheck.isChecked(): self.ngonsFunc()
        if self.ui.invalidVertexQCheck.isChecked(): self.invalidVertexFunc()
        #
        if self.ui.pivotsQCheck.isChecked(): self.pivotsFunc()
        if self.ui.matrixQCheck.isChecked(): self.matrixFunc()

    def uselessBindPosesInfoFunc(self):
        cmds.waitCursor(state=True)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Non connected Dag Poses:\n{}\n\n".format(ModelChecker.uselessBindPosesCheck() or "")
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
        
    def mdlIMatsInSceneFunc(self):
        self.getGeometry()
        inputPath = self.ui.mdlPathQText.text()
        currentText = self.ui.outputInfoQText.toPlainText()
        if not inputPath:
            currentText += "################## .mdl imaterials in scene: NO INPUT REGISTERED"
            self.ui.outputInfoQText.setText(currentText)
            cmds.warning("No input registered")
            return
        cmds.waitCursor(state=True)
        result = ModelChecker.mdlPathIMatsInSceneCheck(inputPath)
        currentText += "################## .mdl imaterials in scene:\n{}\n\n".format(result)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
    
    def uselessSkinClustersFunc(self):
        cmds.waitCursor(state=True)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Non connected Skin Clusters:\n{}\n\n".format(ModelChecker.uselessSkinClustersCheck() or "")
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def skinClusterMaxInfFunc(self):
        cmds.waitCursor(state=True)
        currentText = self.ui.outputInfoQText.toPlainText()
        addText = ""
        for key, val in ModelChecker.skinMaxInfluencesCheck().items():
            addText += "{}: {}\n".format(key, val)
        currentText += "################## Max influences Skin Clusters invalids (<UseMaxInfluences>, <MaxInfluences>):\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
        
    def deformersFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        resultDict = {mesh:inst.nonSkinClusterDeformers for mesh,inst in self.meshesDict.items()}
        currentText = self.ui.outputInfoQText.toPlainText()
        addText=""
        for key,val in resultDict.items():
            addText += "{}: {}\n".format(key, val)
        currentText += "################## Non Skin Cluster deformers:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
    
    def componentSelectionFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        result = [mesh for mesh,inst in self.meshesDict.items() if inst.componetsActiveList]
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Components active list:\n{}\n\n".format(result or "")
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def componentSelectionCleanFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        sel = cmds.ls(sl=True)
        for mesh in self.meshesDict.keys():
            cmds.select(mesh)
            mel.eval('SelectEdgeMask;')
            cmds.select(clear=True)
            mel.eval('SelectVertexMask;')
            cmds.select(clear=True)
            mel.eval('SelectFacetMask;')
            cmds.select(clear=True)
        cmds.selectMode(o=True)
        cmds.select(sel)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Components active list has been cleaned"
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def ngonsFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        addText = ""
        for mesh,inst in self.meshesDict.items():
            if inst.ngonsLs:
                addText += "{}: True\n".format(mesh)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Ngon faces:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def ngonsSelectFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        cmds.select(clear=True)
        [cmds.select(inst.ngonsLs, add=True) for inst in self.meshesDict.values()]
        cmds.waitCursor(state=False)

    def invalidVertexFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        result = [mesh for mesh,inst in self.meshesDict.items() if inst.uselessVertexLs]
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Invalid vertex active list:\n{}\n\n".format(result or "")
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def invalidVertexSelectFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        cmds.select(clear=True)
        [cmds.select(inst.uselessVertexLs, add=True) for inst in self.meshesDict.values()]
        cmds.waitCursor(state=False)

    def pivotsFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        currentText = self.ui.outputInfoQText.toPlainText()
        addText = ""
        for mesh in self.meshesDict.keys():
            if 'shape' in cmds.nodeType(mesh, i=True):
                continue
            pivots = cmds.xform(mesh, pivots=True, query=True)
            if pivots != [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
                addText += "{}: {}\n".format(mesh, pivots)
        currentText += "################## Non zero pivots:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
        
    def matrixFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        addText = ""
        for mesh in self.meshesDict.keys():
            if 'shape' in cmds.nodeType(mesh, i=True):
                continue
            print(mesh, "<<<<")
            tr = cmds.xform(mesh, t=True, query=True)
            rt = cmds.xform(mesh, ro=True, query=True)
            sc = cmds.xform(mesh, s=True, query=True)
            print(mesh, "post query")
            if any([tr != [0,0,0], rt != [0,0,0], sc != [1,1,1]]):
                addText += "{}: {}\n".format(mesh, tr + rt + sc)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Non zero transform:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def skinClusterFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        currentText = self.ui.outputInfoQText.toPlainText()
        addText = ""
        for mesh, inst in self.meshesDict.items():
            if inst.skinCluster:
                addText += "{}: {}\n".format(mesh, inst.skinCluster)
        currentText += "################## Meshes with SkinCluster:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

    def skinClusterInfluencesFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        addText=""
        for mesh, inst in self.meshesDict.items():
            if inst.skinCluster and not cmds.skinCluster(inst.skinCluster, inf=True, q=True):
                addText += "{}: {}\n".format(mesh, inst.skinCluster)
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Skin Cluster with no influences:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
    
    def bindPosesInfoFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        resultDict = {mesh:inst.bindPoses for mesh,inst in self.meshesDict.items() if inst.bindPoses}
        currentText = self.ui.outputInfoQText.toPlainText()
        addText = ""
        for key, val in resultDict.items():
            addText += "{}: {}\n".format(key, val)
        currentText += "################## Meshes's with SkinClusters' bindPoses:\n{}\n\n".format(addText)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)
    
    def bindPosesFixFunc(self):
        cmds.waitCursor(state=True)
        self.getGeometry()
        resultDict = {}
        for mesh, inst in self.meshesDict.items():
            inst._bindPosesRebuild_()
            resultDict[mesh] = inst.bindPoses
        currentText = self.ui.outputInfoQText.toPlainText()
        currentText += "################## Mesh's SkinClusters' new bindPoses:\n{}\n\n".format(resultDict)
        self.ui.outputInfoQText.setText(currentText)
        cmds.waitCursor(state=False)

def show():
    global modelCheckerUI
    try:
        if modelCheckerUI.isVisible():
            modelCheckerUI.close()
    except NameError:
        pass
    modelCheckerUI = ModelCheckerUI()
    modelCheckerUI.show()



class ModelChecker(object):
    mdlPath = UIFileWidget.ProjectPath.getExportFolder() + "\\actors\\{actorType}\\{assetName}\\models\\{assetName}.mdl"
    maxInfluences = 4
    
    def __init__(self, inMesh):
        self._inMesh_                = inMesh
        self.skinCluster             = None
        self.bindPoses               = []
        self.ngonsLs          = []
        self.uselessVertexLs         = []
        self.componetsActiveList     = []
        self.nonSkinClusterDeformers = []
        #--------------------------------
        self._deformersFinder_()
        self._componentSelectionFinder_()
        self._uselessVertexFinder_()
        self._ngonsFinder_()
        self._skinClusterFinder_()
        self._bindPosesFinder_()

    #fix
    def _bindPosesRebuild_(root):
        self._bindPosesFinder_()
        if not self.bindPoses:
            return
        jointList = {}
        connectedSkinClusters = {}
        for pose in self.bindPoses:
            for joint in cmds.listConnections(pose, type="joint"):
                jointList[joint] = None
            for skin in cmds.listConnections(pose, type="skinCluster"):
                connectedSkinClusters[skin] = None
        cmds.delete(list(self.bindPoses.keys()))
        cmds.select(jointList, r=True)
        newPose = cmds.dagPose(sl=True, s=True, bp=True)
        for skn in list(connectedSkinClusters.keys()):
            cmds.connectAttr("{}.message".format(newPose), "{}.bindPose".format(skn))
        cmds.select(selection)
        self.bindPoses = [newPose]
        return newPose

    #finder
    def _deformersFinder_(self):
        '''Set deformers data are non-deformer or poly-modifier'''
        for deformer in cmds.listHistory(self._inMesh_, pdo=1) or []:
            inheritedTypes = cmds.nodeType(deformer, inherited=True)
            if "skinCluster" not in inheritedTypes:
                self.nonSkinClusterDeformers.append( deformer )
    
    def _componentSelectionFinder_(self):
        goOMode = True if cmds.selectMode(o=True, q=True) else False
    
        mel.eval('SelectEdgeMask;')
        self.componetsActiveList.extend( [component for component in cmds.ls(selection=True, flatten=True) if "." in component] )
        mel.eval('SelectVertexMask;')
        self.componetsActiveList.extend( [component for component in cmds.ls(selection=True, flatten=True) if "." in component] )
        mel.eval('SelectFacetMask;')
        self.componetsActiveList.extend( [component for component in cmds.ls(selection=True, flatten=True) if "." in component] )
        
        if goOMode:
            cmds.selectMode(o=True)
        
    def _uselessVertexFinder_(self):
        '''Set vertex data compounded by 2 edges or less'''
        for vtx in cmds.ls(self._inMesh_ + ".vtx[:]", fl=True):
            edges = [elem for elem in cmds.polyInfo(vtx, vertexToEdge=True)[0].split(" ") if elem]
            edges.remove('VERTEX')
            edges.remove('\n')
            if len(edges) <= 3:
                self.uselessVertexLs.append( vtx )

    def _ngonsFinder_(self):
        '''Set faces data compunded by 5 edges or more'''
        for face in cmds.ls(self._inMesh_ + ".f[:]", fl=True):
            edges = [elem for elem in cmds.polyInfo(face, faceToEdge=True)[0].split(" ") if elem]
            edges.remove('FACE')
            edges.remove('\n')
            if len(edges) >= 6:
                self.ngonsLs.append( face )
                
    def _skinClusterFinder_(self):
        '''Set skinCluster data related to mesh input'''
        self.skinCluster = mel.eval("findRelatedSkinCluster " + self._inMesh_)
    
    def _bindPosesFinder_(self):
        '''Set bindPose data for SkinCluster related to mesh input'''
        self._skinClusterFinder_()
        if not self.skinCluster:
            return
        bindPoses = {}
        for jnt in cmds.skinCluster(self.skinCluster, inf=True, q=True):
            for dagPose in cmds.listConnections(jnt, type="dagPose") or []:
                if cmds.getAttr(dagPose + ".bindPose"):
                    bindPoses[dagPose] = None
        self.bindPoses = list(bindPoses.keys())

    #classmethods
    @classmethod
    def uselessBindPosesCheck(self):
        '''Set bindPose data for SkinCluster related to mesh input'''
        result = []
        for dagPose in cmds.ls(type='dagPose'):
            if not cmds.listConnections(dagPose + '.message'):
                result.append( dagPose )
        return result

    @classmethod
    def uselessSkinClustersCheck(self):
        '''Returns SkinCluster nodes with no influences or mesh connected'''
        result = []
        for skin in cmds.ls(type='skinCluster'):
            inf = cmds.skinCluster(skin, inf=True, q=True)
            mesh = cmds.listConnections(skin + '.outputGeometry')
            if not inf and not mesh:
                result.append( skin )
        return result

    @classmethod
    def mdlPathIMatsInSceneCheck(self, mdlPath):
        result = {}
        mdlIMatLs = []
        mdlFile = minidom.parse(mdlPath)
        for mdlIMat in mdlFile.getElementsByTagName('imat'):
            mdlIMatName = mdlIMat.attributes['path'].value.rpartition('/')[-1][:-5]
            mdlIMatLs.append( mdlIMatName )
        for imat in mdlIMatLs:
            result[imat] = True if cmds.ls(materials=True) else False
        return result

    @classmethod
    def skinMaxInfluencesCheck(self):
        '''Returns True if the skinCluster attached has maxInfluences setted in class'''
        result = {}
        for skin in cmds.ls(type="skinCluster"):
            boolCheck = cmds.getAttr(skin + ".maintainMaxInfluences")
            maxCheck = cmds.getAttr(skin + ".maxInfluences")
            if not boolCheck:
                result[skin] = False, maxCheck
            elif boolCheck and maxCheck > self.maxInfluences:
                result[skin] = True, maxCheck
        return result