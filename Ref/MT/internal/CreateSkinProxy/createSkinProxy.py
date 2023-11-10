from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui
import QtCustomWidgets.UIFileWidget as UIFileWidget

import maya.cmds as cmds
import maya.mel as mel
import sys, os

class CreateSkinProxyWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __uiPath__ = r"CreateSkinProxy\createSkinProxy.ui"
    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__uiPath__), parent=parent)
        self.setObjectName('CreateSkinProxy')
        self.setWindowTitle('Create Skin Proxy')
        # initialize
        self._proxyMesh_ = None
        self._proxyParent_ = None
        self.meshSource = None
        # ui connections
        self.ui.proxyParentCustomQRadio.toggled.connect(self.__toogleProxyParentCustom__)
        self.ui.proxyParentCustomQButton.clicked.connect(self._setProxyParentCustom_)
        self.ui.meshesModeQRadio.toggled.connect(self.__toogleToolModeWidget__)
        self.ui.influenceModeQRadio.toggled.connect(self.__toogleToolModeWidget__)
        self.ui.applyQButton.clicked.connect(self._do_)
        ##############
        self.__enableMeshesModeWidget__()
        
    # UI methods
    def _getWeightClamp_(self):
        return self.ui.weightClampQSpin.value()

    def _getProxySuffix_(self):
        return self.ui.proxySuffixQLine.text()

    ### tool mode
    def __enableMeshesModeWidget__(self):
        toolModeWidget = MeshesModeWidget(self)
        self.ui.modeQLayout.addWidget(toolModeWidget)
        self._toolModeWidget_ = toolModeWidget
    
    def __enableInfluenceModeWidget__(self):
        toolModeWidget = InfluenceModeWidget(self)
        self.ui.modeQLayout.addWidget(toolModeWidget)
        self._toolModeWidget_ = toolModeWidget

    def __toogleToolModeWidget__(self):
        if self.ui.modeQLayout.count():
            child = self.ui.modeQLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        if self.ui.meshesModeQRadio.isChecked():
            self.__enableMeshesModeWidget__()
        else:
            self.__enableInfluenceModeWidget__()
    #############

    ### proxy parent custom
    def _getProxyParentCustom_(self):
        return self.ui.proxyParentCustomQLine.text()

    def _setProxyParentCustom_(self):
        self.ui.proxyParentCustomQLine.setText(cmds.ls(sl=True)[-1])
        self._proxyParent_ = cmds.ls(sl=True)[-1]
    
    def __toogleProxyParentCustom__(self):
        if self.ui.proxyParentCustomQRadio.isChecked():
            self.ui.proxyParentCustomQLine.setEnabled(True)
            self.ui.proxyParentCustomQButton.setEnabled(True)
        else:
            self.ui.proxyParentCustomQLine.setEnabled(False)
            self.ui.proxyParentCustomQButton.setEnabled(False)
    #######################
    
    # Behave methods
    def _parentProxy_(self):
        if self.ui.proxyParentInfluenceQRadio.isChecked():
            cmds.parent(self._proxyMesh_, self._proxyParent_)
        elif self.ui.proxyParentWorldQRadio.isChecked():
            cmds.parent(self._proxyMesh_, w=True)
        elif self.ui.proxyParentCustomQRadio.isChecked():
            cmds.parent(self._proxyMesh_, self._proxyParent_)
    
    def createInfluencePolyArea(self, influence, vtxLsArea):
        '''Given: source mesh, influence from its skin, and a vertex list as area.
        Creates a duplicated mesh, and delete faces not defined by vertex out of the list'''
        if self.ui.proxyParentInfluenceQRadio.isChecked():
            self._proxyParent_ = influence
        self._proxyMesh_ = cmds.duplicate(self.meshSource, n="{}_{}".format(influence, self._getProxySuffix_()))[0]
        toDelete = []
        for fc in cmds.ls(self._proxyMesh_ + ".f[:]", fl=True):
            vtxLs = cmds.ls(cmds.polyListComponentConversion(fc, ff=True, tv=True), fl=True)
            check = [vtx.replace(self._proxyMesh_, self.meshSource) in vtxLsArea for vtx in vtxLs]
            if not all(check):
                toDelete.append(fc)
        cmds.delete(toDelete)
        for at in ".tx",".ty",".tz",".rx",".ry",".rz",".sx",".sy",".sz",".v":
            cmds.setAttr(self._proxyMesh_ + at, l=False)
        self._parentProxy_()
        return self._proxyMesh_

    def getInfluenceDictSkinVertexArea(self, mesh, weightClamp=0.1):
        '''Given a mesh, create and return a dictionary. Each influence contains affected vertex'''
        skinRelated = mel.eval('findRelatedSkinCluster ' + mesh)
        influencesLs = cmds.skinCluster(skinRelated, inf=True, q=True)
        weightsDict = {k:[] for k in influencesLs}
        for vtx in cmds.ls(mesh + ".vtx[*]", fl=True):
            weightsLs = cmds.skinPercent(skinRelated, vtx, v=True, q=True)
            for ind, weight in enumerate(weightsLs):
                if weight >= weightClamp:
                    weightsDict[influencesLs[ind]].append( vtx )
        return weightsDict
    
    def _do_(self):
        '''Method override based on Tool Mode'''
        self._toolModeWidget_._do_()

class MeshesModeWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __uiPath__ = r"CreateSkinProxy\meshesModeWidget.ui"

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__uiPath__), parent=parent)
        self._parentWidget_ = parent
        self.__progressSteps__ = []
        # ui connections
        self.ui.meshesModeQButton.clicked.connect(self.__meshesModeQButton__)
    
    # UI methods
    def __meshesModeQButton__(self):
        sel = cmds.ls(sl=True)
        inputResult = []
        for each in sel:
            shapes = cmds.listRelatives(each, shapes=True)
            if not shapes:
                continue
            if cmds.nodeType(shapes[0]) == "mesh":
                inputResult.append( each )
        self.ui.meshesModeQLine.setText(", ".join(inputResult))

    def _getUIMesh_(self):
        qlineValue = self.ui.meshesModeQLine.text()
        return qlineValue.replace(" ","").split(",") if qlineValue else ""
    
    def __setProgressSteps__(self):
        meshes = self._getUIMesh_()
        self.__progressSteps__ = []
        for mesh in meshes:
            skinSource = mel.eval('findRelatedSkinCluster ' + mesh)
            self.__progressSteps__.extend(cmds.skinCluster(skinSource, inf=True, q=True))

    def __applyQProgress__(self, step=0):
        factor = 100.0/len(self.__progressSteps__)
        self._parentWidget_.ui.applyQProgress.setValue(factor * step)

    # Behave methods
    def _do_(self):
        self.__setProgressSteps__()
        step = 1
        for mesh in self._getUIMesh_():
            self._parentWidget_.meshSource = mesh
            influenceAreaDict = self._parentWidget_.getInfluenceDictSkinVertexArea(mesh, self._parentWidget_._getWeightClamp_())
            for influence, vtxLs in influenceAreaDict.items():
                self._parentWidget_.createInfluencePolyArea(influence, vtxLs)
                self.__applyQProgress__(step)
                step += 1


class InfluenceModeWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __uiPath__ = r"CreateSkinProxy\influenceModeWidget.ui"

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__uiPath__), parent=parent)
        self._parentWidget_ = parent
        # initialize
        self.__influenceVertexAreaEnabled__ = False
        self.__influenceProxyReplaceCheck__ = False
        self._vertexInfluenceAreaWidget_ = None
        self.influenceAreaDict = {}
        # ui connections
        self.ui.influenceModeQButton.clicked.connect(self.__influenceModeQButton__)
        self.ui.influenceModeQTree.itemSelectionChanged.connect( self.__influenceModeQTreeUpdate__ )
        self.ui.influenceVertexAreaQCheck.stateChanged.connect(self.__toogleVertexInfluenceAreaWidget__)
        
    # UI methods
    def __influenceModeQButton__(self):
        sel = cmds.ls(sl=True)
        if not sel:
            sys.stdout.write("No selection founded")
            return
        selShape = cmds.listRelatives(sel[0], shapes=True)
        if not selShape:
            sys.stdout.write("No shapes founded in selection")
            return
        if cmds.nodeType(selShape[0]) != "mesh":
            sys.stdout.write("Selection first shape is not Mesh type")
            return
        self.ui.influenceModeQLine.setText(sel[0])
        self._parentWidget_.meshSource = sel[0]
        self.influenceAreaDict = self._parentWidget_.getInfluenceDictSkinVertexArea(selShape[0], self._parentWidget_._getWeightClamp_())
        self._setInfluenceModeQTree_(sel[0])
        self.__applyQProgress__(0)
        sys.stdout.write("Setted '{}' as input | Result: 1\n".format(sel[0]))
    
    def __influenceProxyAdd__(self, influence, mesh):
        current = cmds.ls("{}_{}".format(influence, self._parentWidget_._getProxySuffix_()))
        current.remove(mesh)
        if not current:
            return
        if self.__influenceProxyReplaceCheck__:
            cmds.delete(current)
            cmds.rename(mesh, current[0])
            return
        newShape = cmds.listRelatives(mesh, shapes=True)
        cmds.parent(newShape, current[0], r=True, s=True)
        cmds.rename(newShape, current[0] + "Shape")
        cmds.delete(mesh)
    
    def __influenceProxyReplace__(self, influence, mesh):
        self.__influenceProxyReplaceCheck__ = True
        self.__influenceProxyAdd__(influence, mesh)
    
    def _getMesh_(self):
        return self.ui.influenceModeQLine.text()

    def __applyQProgress__(self, step=0):
        factor = 100.0/len(self.influenceAreaDict.keys())
        self._parentWidget_.ui.applyQProgress.setValue(factor * step)

    ### influence mode q tree
    def __influenceModeQTreeUpdate__(self):
        if not self.__influenceVertexAreaEnabled__:
            return
        influence = self._getInfluenceModeQTree_()
        self._vertexInfluenceAreaWidget_._setVertexLs_(self.influenceAreaDict[influence])

    def _setInfluenceModeQTree_(self, mesh):
        skinSource = mel.eval('findRelatedSkinCluster ' + mesh)
        if not skinSource:
            return
        influencesLs = cmds.skinCluster(skinSource, inf=True, q=True)
        influencesLs = sorted(cmds.ls(influencesLs, long=True), key=len)
        self.ui.influenceModeQTree.clear()
        itemWdgParent = self.ui.influenceModeQTree
        level = {}
        for influence in influencesLs:
            parent = cmds.listRelatives(influence, p=True, f=True)
            if parent and parent[0] in influencesLs:
                itemWdgParent = level[parent[0]]
            infWidget = QtWidgets.QTreeWidgetItem(itemWdgParent)
            infWidget.setText(0, influence.split("|")[-1])
            if [child for child in (cmds.listRelatives(influence, f=True) or []) if child in influencesLs]:
                level[influence] = infWidget
        return level
    
    def _getInfluenceModeQTree_(self):
        if not self.ui.influenceModeQTree.selectedIndexes():
            return None
        item = self.ui.influenceModeQTree.selectedIndexes()[0]
        return item.data()
    ####################

    ### vertex influence area widget
    def __disableVertexInfluenceAreaWidget__(self):
        if self.ui.influenceVertexAreaQLayout.count():
            child = self.ui.influenceVertexAreaQLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            self.__influenceVertexAreaEnabled__ = False
        
    def __enableVertexInfluenceAreaWidget__(self):
        vtxInfAreaWidget = VertexInfluenceAreaWidget(self)
        self.ui.influenceVertexAreaQLayout.addWidget(vtxInfAreaWidget)
        self._vertexInfluenceAreaWidget_ = vtxInfAreaWidget
        treeSelection = self._getInfluenceModeQTree_()
        if treeSelection:
            self._vertexInfluenceAreaWidget_._setVertexLs_(self.influenceAreaDict[treeSelection])
        self.__influenceVertexAreaEnabled__ = True

    def __toogleVertexInfluenceAreaWidget__(self):
        if self.__influenceVertexAreaEnabled__:
            self.__disableVertexInfluenceAreaWidget__()
        else:
            self.__enableVertexInfluenceAreaWidget__()
    ################################

    # Behave methods
    def _setInfluenceAreaDictValue_(self, influence, vtxAreaLs):
        self.influenceAreaDict[influence] = vtxAreaLs

    def _do_(self):
        proxyAction = self.__influenceProxyReplace__
        if self.ui.influenceProxyAddQRadio.isChecked():
            proxyAction = self.__influenceProxyAdd__
        progress = 1
        for influence, vtxLs in self.influenceAreaDict.items():
            mesh = self._parentWidget_.createInfluencePolyArea(influence, vtxLs)
            #print influence, mesh, "<"*10
            proxyAction(influence, mesh)
            self.__applyQProgress__(progress)
            progress += 1


class VertexInfluenceAreaWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __uiPath__ = r"CreateSkinProxy\vertexInfluenceAreaWidget.ui"

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__uiPath__), parent=parent)
        self._parentWidget_ = parent
        # ui connections
        self.ui.influenceVertexAreaAddQButton.clicked.connect(self.__influenceVertexAreaAddQButton__)
        self.ui.influenceVertexAreaSetQButton.clicked.connect(self.__influenceVertexAreaSetQButton__)
        self.ui.influenceVertexAreaSelectQButton.clicked.connect(self.__influenceVertexAreaSelectQButton__)
        
    # UI methods
    def __influenceVertexAreaAddQButton__(self):
        sel = self._getSelectionVertexArea_()
        uiContent = self._getVertexLs_()
        for vtx in sel:
            if vtx in uiContent:
                sel.remove(vtx)
        self._setVertexLs_(uiContent + sel)
        self.__updateInfluenceVtxArea__(uiContent + sel)
        sys.stdout.write("Added vertex to '{}' influence area | Result: 1\n".format(self._parentWidget_._getInfluenceModeQTree_()))
    
    def __influenceVertexAreaSetQButton__(self):
        sel = self._getSelectionVertexArea_()
        self._setVertexLs_(sel)
        self.__updateInfluenceVtxArea__(sel)
        sys.stdout.write("Setted vertex area to '{}' influence | Result: 1\n".format(self._parentWidget_._getInfluenceModeQTree_()))
    
    def __influenceVertexAreaSelectQButton__(self):
        cmds.select(self._getVertexLs_(), r=True)
        sys.stdout.write("Query vertex influence area of '{}' influence area | Result: 1\n".format(self._parentWidget_._getInfluenceModeQTree_()))

    def _getVertexLs_(self):
        items = []
        for x in range(self.ui.influenceVertexAreaQList.count()):
            items.append(self.ui.influenceVertexAreaQList.item(x).text())
        return items

    def _setVertexLs_(self, vertexLs):
        self.ui.influenceVertexAreaQList.clear()
        self.ui.influenceVertexAreaQList.addItems(vertexLs)

    # Behave methods
    def _getSelectionVertexArea_(self):
        return [vtx for vtx in cmds.ls(sl=True, fl=True) if ".vtx" in vtx]
    
    def __updateInfluenceVtxArea__(self, vtxAreaLs):
        influenceSelected = self._parentWidget_._getInfluenceModeQTree_()
        self._parentWidget_._setInfluenceAreaDictValue_(influenceSelected, vtxAreaLs)
    



def show():
    global createSkinProxy
    try:
        if createSkinProxy.isVisible():
            createSkinProxy.close()
    except NameError:
        pass
    createSkinProxy = CreateSkinProxyWin()
    createSkinProxy.show()