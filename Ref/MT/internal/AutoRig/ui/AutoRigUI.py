import maya.api.OpenMaya as OpenMaya
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtWidgets, QtGui, QtCore
import QtCustomWidgets.UIFileWidget as UIFileWidget
import NodeCustom.Transformations.Plugins.MatrixMirror as MatrixMirror
import maya.cmds as cmds
import maya.mel as mel
import sys
import os

from AutoRig.cores import develop
from AutoRig.cores import naming

class AutoRigWin(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    __ui_path__ = r"AutoRig\ui\AutoRigWin.ui"
    __mod_path__ = r"AutoRig\misc\modules"
    __templateDict__ = {}
    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__ui_path__), parent=parent)
        self.__mod_path__= os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__mod_path__)
        self.setObjectName('AutoRigManager')
        self.setWindowTitle('Auto Rig Manager')

        self.__setModulesQTreeItems__()
        # connections
        self.ui.referenceQButton.clicked.connect( self.__moduleQButtonAction__ )
        self.ui.importQButton.clicked.connect( self.__moduleQButtonAction__ )
        self.ui.referenceEditorQButton.clicked.connect( self.__referenceEditorQButtonAction__ )
        self.ui.namespaceEditorQButton.clicked.connect( self.__namespaceEditorQButtonAction__ )
        self.ui.mirrorQButton.clicked.connect( self.__mirrorQButtonAction )
        self.ui.hierarchizeQButton.clicked.connect( self.__hierarchizeQButtonAction__ )
        self.ui.breakRefsQButton.clicked.connect( self.__breakRefsQButtonAction__ )
        self.ui.templateEditQButton.clicked.connect( self.__templateEditQButtonAction__ )
        self.ui.templateGetPoseQButton.clicked.connect( self.__templateGetPoseQButtonAction__ )
        self.ui.templateSetPoseQButton.clicked.connect( self.__templateSetPoseQButtonAction__ )
        self.ui.hierarchyToogleQButton.clicked.connect( self.__hierarchyToogleQButtonAction__ )
        self.ui.saveModCompQButton.clicked.connect( self.__saveModCompQButtonAction__ )
        self.ui.methodsQList.itemClicked.connect( self.__methodsQListChangeAction__ )
        self.ui.modulesQTree.itemSelectionChanged.connect( self.__modCompPathQLineUpdate__ )
        self.ui.mainQTabWidget.currentChanged.connect( self.ui.charDocQPText.clear )
        # initialize
        self.ui.methodsQList.addItems( sorted(develop.__mainUI_relation__.keys()) )

    def __colorSideDefault__(self, controlsSet):
        namespace = ""
        if ":" in controlsSet:
            namespace = controlsSet.rpartition(":")[0]
        for ctl in cmds.sets(controlsSet, q=True):
            if self.ui.moduleQSide.currentText() == "lf":
                main = 15
                second = 18
            elif self.ui.moduleQSide.currentText() == "rt":
                main = 23
                second = 14
            elif self.ui.moduleQSide.currentText() == "cn":
                main = 13
                second = 20
            cmds.setAttr(ctl + ".overrideEnabled", True)
            cmds.setAttr(ctl + ".overrideColor", main)

    
    def __setModulesQTreeItems__(self):
        self.ui.modulesQTree.clear()
        itemWdgParent = self.ui.modulesQTree
        level = {}
        for root, dirs, files in os.walk(self.__mod_path__):
            rt = root.split("\\")[-1]
            if rt == '.mayaSwatches':
                continue
            if root != self.__mod_path__:
                itemWdgParent = level[rt]
            for item in dirs:
                if item == '.mayaSwatches':
                    continue
                itemWidget = QtWidgets.QTreeWidgetItem(itemWdgParent)
                itemWidget.setText(0, item)
                level[item] = itemWidget
            for item in files:
                if not item.endswith(".ma") and not item.endswith(".mb"):
                    continue
                item = item.split("_")[-1][:-3]                
                itemWidget = QtWidgets.QTreeWidgetItem(itemWdgParent)
                itemWidget.setText(0, item)
    
    def __getModulesQTreeItem__(self):
        if not self.ui.modulesQTree.selectedIndexes():
            return ""
        item = self.ui.modulesQTree.selectedIndexes()[0]
        itemName = ""
        for step in range(100):
            itemParent = item.parent()
            itemChild = item.child(0,0)
            if itemChild.data() != None and not step:
                return None
            itemName = "\{}".format(item.data()) + itemName
            if itemParent.data() == None:
                break
            item = itemParent
        return itemName

    def __modCompPathQLineUpdate__(self):
        self.ui.charDocQPText.clear()
        path = "{}{}.txt".format(self.__mod_path__, self.__getModulesQTreeItem__())
        self.ui.modCompPathQLine.setText( path )
        if cmds.file( path, exists=True, query=True ):
            with open(path, 'r') as text:
                text = text.read()
            self.ui.charDocQPText.appendPlainText(text)

    def __hierarchyToogleQButtonAction__(self):
        hierarchy = develop.HierarchyRig.hierarchy
        templates = hierarchy[5]
        if not cmds.objExists(hierarchy[0]):
            cmds.warning('No {} hierarchy'.format(hierarchy[0]))
            return
        cmds.setAttr(hierarchy[4] + '.overrideEnabled', True)
        if cmds.getAttr(hierarchy[1] + '.v'):
            cmds.setAttr(hierarchy[1] + '.v', False)
            cmds.setAttr(hierarchy[4] + '.overrideDisplayType', 2)
            if cmds.objExists(templates):
                cmds.setAttr(templates + '.v', False)
        else:
            cmds.setAttr(hierarchy[1] + '.v', True)
            cmds.setAttr(hierarchy[4] + '.overrideDisplayType', 0)
            if cmds.objExists(templates):
                cmds.setAttr(templates + '.v', True)
    
    def __templateEditQButtonAction__(self):
        template = cmds.ls(sl=True)
        if not template:
            cmds.warning('No selection registered')
            return
        template = template[0]
        templateRoot = "{}_00_{}".format(naming._ndTyp_dict_['template'].title(), naming._ndTyp_dict_['template'])
        namespace = ""
        if ":" in template:
            namespace = template.rpartition(":")[0] + ":"
        if not cmds.objExists("{}{}".format(namespace, templateRoot)):
            cmds.warning('Template root group does not exists in namespace "{}"'.format(namespace))
            return
        if not cmds.objExists("{}{}.metadataTemplate".format(namespace, templateRoot)):
            cmds.warning('Template root group has not MetadataTemplate related'.format(namespace))
            return
        metadata = cmds.listConnections("{}{}.metadataTemplate".format(namespace, templateRoot))[0]
        if not metadata:
            cmds.warning('Template root group has not MetadataTemplate related'.format(namespace))
            return
        state = cmds.getAttr("{}{}.v".format(namespace, templateRoot))
        if not state:
            for root in cmds.ls('::{}'.format(templateRoot)):
                cmds.setAttr('{}.v'.format(root), True)
            cmds.select(cmds.listRelatives('{}:{}'.format(namespace, templateRoot))[0])
        else:
            for root in cmds.ls('::{}'.format(templateRoot)):
                cmds.setAttr('{}.v'.format(root), False)
            # pre execution
            for preMetadata in cmds.listConnections('{}.{}'.format(metadata, develop.Template.__preExecutionAttr__)) or []:
                cmds.select(preMetadata)
                exec( cmds.scriptNode(preMetadata, beforeScript=True, q=True) )
            # execution
            cmds.select(metadata)
            exec( cmds.scriptNode(metadata, beforeScript=True, q=True) )
            # post execution
            for postMetadata in cmds.listConnections('{}.{}'.format(metadata, develop.Template.__postExecutionAttr__)) or []:
                cmds.select(postMetadata)
                exec( cmds.scriptNode(postMetadata, beforeScript=True, q=True) )
            cmds.select("{}:{}".format(namespace, templateRoot))

    def __methodsQListChangeAction__(self):
        while self.ui.systemQVBoxLayout.count():
            child = self.ui.systemQVBoxLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        sel = self.ui.methodsQList.currentItem().text()
        widget = develop.__mainUI_relation__[sel].__call__(None)
        self.ui.systemQVBoxLayout.addWidget(widget)
        self.ui.systemQButton.clicked.connect(widget.__widgetDo__)
            
    def __moduleQButtonAction__(self):
        name = self.ui.moduleQName.text()
        side = self.ui.moduleQSide.currentText()
        templateString = '*::{}_00_{}'.format(naming._ndTyp_dict_['template'].title(), naming._ndTyp_dict_['template'])
        currentTemplates = [tpl for tpl in cmds.ls(templateString,l=1) if tpl.count("|") < 2]
        namespace = ""
        namespaceDict = {'name':name, 'side':side}
        itemSelected = self.__getModulesQTreeItem__()
        modulePath = "{}{}.ma".format(self.__mod_path__, itemSelected)
        mergeNamespace = True
        fileFnDict = {}
        if not itemSelected:
            cmds.warning('No module selected')
            return
        if name:
            namespace = "{name}"
            fileFnDict["namespace"] = "{name}"
            fileFnDict["mergeNamespacesOnClash"] = False
        if side == "None" and cmds.namespace(ex=namespace.format(**namespaceDict)):
            cmds.warning('Namespace "{}" already registered'.format(namespace).format(**namespaceDict))
            return
        elif side != "None":
            namespace = "{side}_" + namespace
            fileFnDict["mergeNamespacesOnClash"] = False
        namespace = namespace.format(**namespaceDict)
        while cmds.namespace(ex=namespace):
            namespace = namespace.replace("_","__")
        if not namespace:
            namespace = ":"
        fileFnDict["namespace"] = namespace
        if "import" in self.sender().objectName():
            fileFnDict["i"] = True
            fileFnDict["preserveReferences"] = True
            cmds.file(modulePath, **fileFnDict)
            newTemplate = [tpl for tpl in cmds.ls(templateString,l=1) if tpl.count("|") < 2]            
            cmds.select(set(newTemplate) - set(currentTemplates))
            cmds.warning("{} imported | Result: 1".format(modulePath))
            return
        if not namespace or namespace == ":":
            cmds.warning('No name or side setted. Set at least one')
            return
        fileFnDict["r"] = True
        cmds.file(modulePath, **fileFnDict)
        newTemplate = [tpl for tpl in cmds.ls(templateString,l=1) if tpl.count("|") < 2]
        cmds.select(set(newTemplate) - set(currentTemplates))
        cmds.select('*:{}_00_{}'.format(naming._ndTyp_dict_['template'].title(), naming._ndTyp_dict_['template']))
        cmds.warning("{}:{} referenced | Result: 1".format(itemSelected, name))
        
    def __namespaceEditorQButtonAction__(self):
        mel.eval('NamespaceEditor;')
    
    def __referenceEditorQButtonAction__(self):
        mel.eval('ReferenceEditor;')
    
    def __mirrorQButtonAction(self):
        def __set__():
            # using open maya
            parentMtx = OpenMaya.MMatrix(cmds.getAttr(parentObj + ".wm[0]"))
            selMtx = OpenMaya.MMatrix(cmds.getAttr(sel + ".wm[0]"))
            parentInvMtx = OpenMaya.MMatrix(cmds.getAttr(mirrorObj + ".pim[0]"))
            MSpace = OpenMaya.MSpace.kTransform
            aReflection = OpenMaya.MTransformationMatrix().setScale([-1, 1, 1],MSpace).asMatrix()
            fReflection = OpenMaya.MTransformationMatrix().setScale([-1,-1,-1],MSpace).asMatrix()
            outtMtx = fReflection * (selMtx * parentMtx.inverse()) * aReflection * parentMtx * parentInvMtx
            outLocalMtx = OpenMaya.MTransformationMatrix(outtMtx)
            outTr = outLocalMtx.translation(OpenMaya.MSpace.kTransform)
            outRt = outLocalMtx.rotation(asQuaternion=False)
            outRt = outRt[:-1]
            for at,val in zip([".tx",".ty",".tz",".rx",".ry",".rz"], [outTr + outRt]):
                try:
                    cmds.setAttr(mirrorObj + at, val)
                except: continue
        
        def __connect__():
            selName = naming.getName(sel)
            selName['nodeType'] = "matrixMirror"
            mtxm = cmds.createNode("MatrixMirror", n=naming.setName(**selName), ss=True)
            cmds.setAttr(mtxm + ".flipAxis", 6)
            cmds.connectAttr(parentObj + ".wm[0]", mtxm + ".pivotMatrix")
            cmds.connectAttr(sel + ".wm[0]", mtxm + ".inputMatrix")
            cmds.connectAttr(mirrorObj + ".pim[0]", mtxm + ".parentInverseMatrix")
            cmds.connectAttr(mtxm + ".t", mirrorObj + ".t")
            cmds.connectAttr(mtxm + ".r", mirrorObj + ".r")

        sel = cmds.ls(sl=True)
        if not sel:
            raise
        if "lf" not in sel[0] and "rt" not in sel[0]:
            raise
        for sel in sel:
            side = "lf" if "lf" in sel else "rt"
            tokens = sel.split(":")
            for ind, tk in enumerate(tokens):
                if side in tk:
                    tokens[ind] = "*"
                    break
            mirrorObj = cmds.ls(":".join(tokens))
            mirrorObj.remove(sel)
            mirrorObj = mirrorObj[0]
            parentObj = cmds.listRelatives(sel, parent=True)[0]
            while side in parentObj:
                parentObj = cmds.listRelatives(parentObj, parent=True)[0]
            __set__()
            if not self.ui.mirrorQCheck.isChecked():
                continue
            __connect__()
    
    def __hierarchizeQButtonAction__(self):
        sel = cmds.ls(sl=True)
        target = sel[-1]
        del sel[-1]
        for elem in sel:
            cmds.namespace(set=":")
            namespace = elem.rpartition(":")[0]
            if namespace:
                cmds.namespace(set=namespace)
            nameDict = naming.getName(elem)
            nameDict['system'] += naming._ndTyp_dict_[nameDict['nodeType']].title()
            nameDict['nodeType'] = "hierarchize"
            hrch = cmds.createNode('transform', n=naming.setName(**nameDict), p=elem)
            cmds.parent(hrch, target)
            cmds.parent(elem, hrch)
        cmds.namespace(set=":")        

    def __saveModCompQButtonAction__(self, fileDir):
        '''Creates Dict with Reference nodes and its dependencies'''
        def _getModule(refNode):
            # convert maya ref node's name into last token (":") and the file referenced
            # example: lf_Hand:ARN --> A:fingerThreeJoints
            refFile = cmds.referenceQuery(refNode, filename=True)
            refModule = cmds.referenceQuery(refFile, filename=True).split("/")[-1].split(".")[0]
            if not cmds.referenceQuery(refFile, isLoaded=True):
                refModule = None    
            refNode = refNode.split(":")[-1][:-2]
            if refNode.endswith("_"):
                for it in range(10):
                    refNode = refNode.replace("_"*it,"_"*(it-1))
                refNode += "_"
            return "{}:{}".format(refNode, refModule)
        def _lineStyle(refNode):
            parent = cmds.referenceQuery(refNode, referenceNode=True, parent=True)
            space = "|    " if parent else ""
            return "{}{}{}".format("     "*refNode.count(":"), space, _getModule(refNode))
        fileDir = "{}{}.txt".format(self.__mod_path__, self.__getModulesQTreeItem__())
        if not fileDir:
            cmds.warning('No directory file path setted')
            return
        text = ""
        for ref in sorted(cmds.ls(rf=True)):
            parent = cmds.referenceQuery(ref, referenceNode=True, parent=True)
            if "None" in _lineStyle(ref):
                continue
            if parent:
                if _lineStyle(parent) not in text:
                    text += _lineStyle(parent)
                text = text.replace(_lineStyle(parent), "{}\n{}".format(_lineStyle(parent), _lineStyle(ref)))
            else:
                if _lineStyle(ref) not in text:
                    text += _lineStyle(ref)
            text += "\n"
        for it in range(2, 10)[::-1]:
            text = text.replace("\n"*it, "\n"*(it-1))
        if ".txt" not in fileDir:
            fName = cmds.file(sn=True, q=True).split("/")[-1][:-3]
            fileDir = r"{0}\{1}.txt".format(fileDir, fName)
        with open(fileDir, 'w') as fResult:
            fResult.write( text )
        cmds.warning('| Modules saved')
        return text
    
    def __templateGetPoseQButtonAction__(self):
        self.__templateDict__.clear()
        templateGrp = develop.HierarchyRig.hierarchy[5]
        if not templateGrp:
            cmds.warning("No template found to saved | Result: 0")
            return
        for tplShape in cmds.listRelatives("::{}".format(templateGrp), ad=True, f=True, type="locator"):
            tplTr = cmds.listRelatives(tplShape, p=True)[0]
            if not cmds.getAttr(tplTr + ".v"):
                continue
            attrDict = {}
            attrLs = cmds.listAttr(tplTr, k=True) + (cmds.listAttr(tplTr, cb=True) or [])
            for at in attrLs:
                at = "{}.{}".format(tplTr, at)
                if cmds.listConnections(at):
                    continue
                attrDict[at] = cmds.getAttr(at)
            self.__templateDict__[tplTr] = attrDict
        cmds.warning("Template pose saved in scene | Result: 1")
        return self.__templateDict__
    
    def __templateSetPoseQButtonAction__(self):
        for tpl, attrDict in self.__templateDict__.items():
            for atName, atVal in attrDict.items():
                cmds.setAttr(atName, atVal)
        cmds.warning("Template pose setted | Result: 1")


    def __breakRefsQButtonAction__(self):
        if cmds.confirmDialog(m='You can not Undo this action. Continue?',
                              t='WARNING', b=['Yes','No'], db='No', cb='No') == 'No':
            cmds.warning('"Break References" canceled')
            return
        # break references
        deletableLs = ['MayaNodeEditorSavedTabsInfo',
                       'sceneConfigurationScriptNode',
                       'poseInterpolatorManager',
                       'shapeEditorManager',
                       'uiConfigurationScriptNode',
                       'defaultRenderLayer',]
        skipLs = ['renderLayerManager']
        for it in range(222):
            rf = cmds.file(q=True, reference=True)
            if not rf:
                break
            rf = rf[0]
            if not cmds.referenceQuery(rf, isLoaded=True):
                cmds.file(rf, removeReference=True)
                continue
            #rf = cmds.file(q=True, reference=True)[0]
            cmds.file(rf, importReference=True)
        # namespaces management
        for nmspc in sorted(cmds.namespaceInfo(recurse=True, listOnlyNamespaces=True),key=len,reverse=True):
            for node in cmds.ls(nmspc + ":*"):
                if node.split(":")[-1] in deletableLs:
                    cmds.delete(node)
                    continue
                elif node.split(":")[-1] in skipLs:
                    continue
                if "Shape" not in node:
                    cmds.rename(node, "".join(node.split(":")).replace("____","___").replace("___","__").replace("__","_"))
            if nmspc not in ["shared","UI"]:
                cmds.namespace( removeNamespace=":" + nmspc )
        # export hierarchy joints management
        for joint in cmds.ls(type="joint"):
            if "parent" not in cmds.listAttr(joint):
                continue
            parentCnn = cmds.listConnections(joint + ".parent")
            parentCmd = cmds.listRelatives(joint, parent=True)
            if not parentCnn:
                cmds.parent(joint, "DC_Root")
                cmds.warning("Joint '{}' has no parent related. DC_Root will be parent for this joint")
            elif not parentCmd:
                cmds.parent(joint, "DC_Root")
                cmds.warning("Joint '{}' has no parent related. DC_Root will be parent for this joint")
            elif parentCmd != parentCnn:
                cmds.parent(joint, parentCnn)

        cmds.warning('|| References imported')

def show():
    global autorig
    try:
        if autorig.isVisible():
            autorig.close()
    except NameError:
        pass
    autorig = AutoRigWin()
    autorig.show()