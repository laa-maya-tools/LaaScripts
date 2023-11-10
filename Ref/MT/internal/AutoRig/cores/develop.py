from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import QtCustomWidgets.UIFileWidget as UIFileWidget
import os
import sys
import maya.cmds as cmds
from AutoRig.cores import vectors
from AutoRig.cores import naming

class BaseWidget(UIFileWidget.UIFileWidget):
    __uiPath__ = None

    def __init__(self, uiParent=None):
        # init ui
        self.__uiPath__ = UIFileWidget.UIFileWidget.__init__(self, os.path.join(UIFileWidget.ProjectPath.getToolsFolder(), self.__uiPath__), parent=uiParent)
        # init data
        self.uiWdgDict = {}

    @classmethod
    def _checkData_(self, arg, dataName, existence=False):
        if not arg:
            cmds.warning('Input "{}" not registered'.format(dataName))
            return True
        if not existence:
            return False
        if type(arg) not in [list,tuple]:
            arg = [arg]
        for elem in arg:
            if not cmds.objExists(elem):
                cmds.warning('Input {} "{}" does not exists'.format(dataName, elem))
                return True

    def _getWidgetData_(self):
        '''To get self.ui widgets data'''
        # self.uiWdgDict['example'] = pass
            
    def __widgetDo__(self):
        '''Call __do__ with widget input data as flags'''
        self._getWidgetData_()
        self.__do__(**self.uiWdgDict)
        
    
    @classmethod
    def __do__(self, **args):
        '''Do whatever defined system must do'''

class HierarchyRig(BaseWidget):
    __uiPath__ = r'AutoRig\ui\HierarchyRigWidget.ui'
    hierarchy = ['rig','export','controls','setup','geo','templates']

    def __init__(self, uiParent=None):
        super(HierarchyRig, self).__init__(uiParent)

    def __widgetDo__(self):
        self.__do__()

    @classmethod
    def __do__(self):
        cmds.namespace(set=":")
        if cmds.objExists(self.hierarchy[0]):
            return [each for each in self.hierarchy if cmds.objExists(each)]
        cmds.createNode('transform', n=self.hierarchy[0])
        [cmds.createNode('transform', n=each, p=self.hierarchy[0]) for each in self.hierarchy[1:]]
        for elem in self.hierarchy:
            for at in ".tx",".ty",".tz",".rx",".ry",".rz",".sx",".sy",".sz",".v":
                cmds.setAttr(elem + at, keyable=False, channelBox=True)
        cmds.rename(cmds.spaceLocator()[0], "DC_Root")
        cmds.parent("DC_Root", self.hierarchy[1])
        Control.__do__("Main", 0, self.hierarchy[2])
        cmds.warning("Hierarchy Rig | Result: 1")
        return self.hierarchy

class FootRollSnapping(BaseWidget):
    __uiPath__ = r'AutoRig\ui\FootRollSnappingWidget.ui'

    def __init__(self, uiParent=None):
        super(FootRollSnapping, self).__init__(uiParent)
        # clicked connections
        self.ui.footRollControlsQButton.clicked.connect(self.__footRollControlsQButtonAction__)
        self.ui.ballControlQButton.clicked.connect(self.__ballControlQButtonAction__)
        self.ui.footIkControlQButton.clicked.connect(self.__footIkControlQButtonAction__)

    def __footRollControlsQButtonAction__(self):
        self.ui.footRollControlsQLine.setText(", ".join(cmds.ls(sl=True)))
    
    def __ballControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ballControlQLine.setText(cmds.ls(sl=True)[0])
    
    def __footIkControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.footIkControlQLine.setText(cmds.ls(sl=True)[0])
    
    def _getWidgetData_(self):
        self.uiWdgDict['footIkControl'] = self.ui.footIkControlQLine.text()
        self.uiWdgDict['ballControl'] = self.ui.ballControlQLine.text()
        self.uiWdgDict['footRollControls'] = self.ui.footRollControlsQLine.text().replace(" ","").split(",")

    @classmethod
    def __do__(self, footIkControl, ballControl, footRollControls):
        metaData = '{}:MetadataFootRollSnapping'.format(cmds.namespaceInfo(currentNamespace=True))
        if cmds.objExists(metaData):
            cmds.warning('MetadataFootRollSnapping for namespace "{}" already exists'.format(cmds.namespaceInfo(currentNamespace=True)))
            return
        metaData = cmds.scriptNode(n='MetadataFootRollSnapping')
        # attributes creation
        cmds.addAttr(metaData, ln='footRollControls', m=True, at='message')
        cmds.addAttr(metaData, ln='footIkSnapper', at='message')
        cmds.addAttr(metaData, ln='ballControl', at='message')
        cmds.addAttr(metaData, ln='footIkControl', at='message')
        cmds.addAttr(metaData, ln='ballSnapper', at='message')
        # attributes setting
        cmds.setAttr(metaData + '.ihi', 0)
        cmds.setAttr(metaData + '.nodeState', 1)
        cmds.setAttr(metaData + '.sourceType', 1, l=True)
        for control in footIkControl, ballControl:
            snapper = control.split(":")[-1].replace(naming._ndTyp_dict_['control'], naming._ndTyp_dict_['snapper'])
            snapper = cmds.createNode('transform', n=snapper, p=control)
            cmds.parent(snapper, w=True)
            if cmds.listConnections(metaData + ".footIkControl"):
                cmds.connectAttr(control + ".message", '{}.ballControl'.format(metaData))
                cmds.connectAttr(snapper + ".message", '{}.ballSnapper'.format(metaData))
            else:
                cmds.connectAttr(control + ".message", '{}.footIkControl'.format(metaData))
                cmds.connectAttr(snapper + ".message", '{}.footIkSnapper'.format(metaData))
        for ind, control in enumerate(footRollControls):
            cmds.connectAttr(control + '.message', '{}.footRollControls[{}]'.format(metaData, ind))
        return metaData

class LimbSnapping(BaseWidget):
    __uiPath__ = r'AutoRig\ui\LimbSnappingWidget.ui'

    def __init__(self, uiParent=None):
        super(LimbSnapping, self).__init__(uiParent)
        # clicked connections
        self.ui.switchControlQButton.clicked.connect(self.__switchControlQButtonAction__)
        self.ui.ikControlQButton.clicked.connect(self.__ikControlQButtonAction__)
        self.ui.fkControlsQButton.clicked.connect(self.__fkControlsQButtonAction__)
        self.ui.poleVControlQButton.clicked.connect(self.__poleVControlQButtonAction__)

    def __poleVControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ikControlQLine.setText(cmds.ls(sl=True)[0])

    def __fkControlsQButtonAction__(self):
        self.ui.fkControlsQLine.setText(", ".join(cmds.ls(sl=True)))
    
    def __ikControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ikControlQLine.setText(cmds.ls(sl=True)[0])

    def __switchControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ballControlQLine.setText(cmds.ls(sl=True)[0])

    def _getWidgetData_(self):
        self.uiWdgDict['switchControl'] = self.ui.footIkControlQLine.text()
        self.uiWdgDict['fkControls'] = self.ui.fkControlsQLine.text().replace(" ","").split(",")
        self.uiWdgDict['ikControl'] = self.ui.ikControlQLine.text()
        self.uiWdgDict['poleVControl'] = self.ui.poleVControlQLine.text()
        self.uiWdgDict['poleVMultiplier'] = -1 if self.ui.poleVMultQCombo.currentIndex() else 1

    @classmethod
    def __do__(self, switchControl, fkControls, ikControl, poleVControl, poleVMultiplier=1):
        metaData = '{}:MetadataLimbSnapping'.format(cmds.namespaceInfo(currentNamespace=True))
        if cmds.objExists(metaData):
            cmds.warning('MetadataLimbSnapping for namespace "{}" already exists'.format(cmds.namespaceInfo(currentNamespace=True)))
            return
        metaData = cmds.scriptNode(n='MetadataLimbSnapping')#, beforeScript=baseCode
        # attributes creation
        cmds.addAttr(metaData, ln='switchControl', at='message')
        cmds.addAttr(metaData, ln='poleVControl', at='message')
        cmds.addAttr(metaData, ln='poleVSnapper', at='message')
        cmds.addAttr(metaData, ln='poleVMultiplier', at='long', min=-1, max=1, dv=poleVMultiplier)
        cmds.addAttr(metaData, ln='fkControls', m=True, at='message')
        cmds.addAttr(metaData, ln='fkSnappers', m=True, at='message')
        cmds.addAttr(metaData, ln='ikControl', at='message')
        cmds.addAttr(metaData, ln='ikSnapper', at='message')
        # attributes setting
        cmds.setAttr(metaData + '.ihi', 0)
        cmds.setAttr(metaData + '.nodeState', 1)
        cmds.setAttr(metaData + '.sourceType', 1, l=True)
        cmds.connectAttr(switchControl + ".message", metaData + ".switchControl")
        for control in ikControl, poleVControl:
            snapper = control.split(":")[-1].replace(naming._ndTyp_dict_['control'], naming._ndTyp_dict_['snapper'])
            snapper = cmds.createNode('transform', n=snapper, p=control)
            cmds.parent(snapper, w=True)
            if cmds.listConnections(metaData + ".ikControl"):
                cmds.connectAttr(control + ".message", '{}.poleVControl'.format(metaData))
                cmds.connectAttr(snapper + ".message", '{}.poleVSnapper'.format(metaData))
            else:
                cmds.connectAttr(control + ".message", '{}.ikControl'.format(metaData))
                cmds.connectAttr(snapper + ".message", '{}.ikSnapper'.format(metaData))
        for ind, control in enumerate(fkControls):
            snapper = control.split(":")[-1].replace(naming._ndTyp_dict_['control'], naming._ndTyp_dict_['snapper'])
            snapper = cmds.createNode('transform', n=snapper, p=control)
            cmds.parent(snapper, w=True)
            cmds.connectAttr(control + '.message', '{}.fkControls[{}]'.format(metaData, ind))
            cmds.connectAttr(snapper + '.message', '{}.fkSnappers[{}]'.format(metaData, ind))
        return metaData

class SpineSnapping(BaseWidget):
    __uiPath__ = r'AutoRig\ui\SpineSnappingWidget.ui'

    def __init__(self, uiParent=None):
        super(SpineSnapping, self).__init__(uiParent)
        # clicked connections
        self.ui.switchControlQButton.clicked.connect(self.__switchControlQButtonAction__)
        self.ui.fkControlsQButton.clicked.connect(self.__fkControlsQButtonAction__)
        self.ui.ikControlsQButton.clicked.connect(self.__ikControlsQButtonAction__)

    def __switchControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ballControlQLine.setText(cmds.ls(sl=True)[0])
    
    def __fkControlsQButtonAction__(self):
        self.ui.fkControlsQLine.setText(", ".join(cmds.ls(sl=True)))

    def __ikControlsQButtonAction__(self):
        self.ui.ikControlsQLine.setText(", ".join(cmds.ls(sl=True)))

    def _getWidgetData_(self):
        self.uiWdgDict['switchControl'] = self.ui.footIkControlQLine.text()
        self.uiWdgDict['fkControls'] = self.ui.fkControlsQLine.text().replace(" ","").split(",")
        self.uiWdgDict['ikControls'] = self.ui.ikControlsQLine.text().replace(" ","").split(",")        
    
    @classmethod
    def __do__(self, switchControl, fkControls, ikControls):
        metaData = '{}:MetadataSpineSnapping'.format(cmds.namespaceInfo(currentNamespace=True))
        if cmds.objExists(metaData):
            cmds.warning('MetadataSpineSnapping for namespace "{}" already exists'.format(cmds.namespaceInfo(currentNamespace=True)))
            return
        metaData = cmds.scriptNode(n='MetadataSpineSnapping')
        # attributes creation
        cmds.addAttr(metaData, ln='switchControl', at='message')
        cmds.addAttr(metaData, ln='fkControls', m=True, at='message')
        cmds.addAttr(metaData, ln='fkSnappers', m=True, at='message')
        cmds.addAttr(metaData, ln='ikControls', m=True, at='message')
        cmds.addAttr(metaData, ln='ikSnappers', m=True, at='message')
        # attributes setting
        cmds.setAttr(metaData + '.ihi', 0)
        cmds.setAttr(metaData + '.nodeState', 1)
        cmds.setAttr(metaData + '.sourceType', 1, l=True)
        for ind, control in enumerate(fkControls):
            snapper = control.split(":")[-1].replace(naming._ndTyp_dict_['control'], naming._ndTyp_dict_['snapper'])
            snapper = cmds.createNode('transform', n=snapper, p=control)
            cmds.parent(snapper, w=True)
            cmds.connectAttr(control + '.message', '{}.fkControls[{}]'.format(metaData, ind))
            cmds.connectAttr(snapper + '.message', '{}.fkSnappers[{}]'.format(metaData, ind))
        for ind, control in enumerate(ikControls):
            snapper = control.split(":")[-1].replace(naming._ndTyp_dict_['control'], naming._ndTyp_dict_['snapper'])
            snapper = cmds.createNode('transform', n=snapper, p=control)
            cmds.parent(snapper, w=True)
            cmds.connectAttr(control + '.message', '{}.ikControls[{}]'.format(metaData, ind))
            cmds.connectAttr(snapper + '.message', '{}.ikSnappers[{}]'.format(metaData, ind))
        return metaData

class Template(BaseWidget):
    __uiPath__ = r'AutoRig\ui\TemplateWidget.ui'
    __preExecutionAttr__ = '_preExecution'
    __postExecutionAttr__ = '_postExecution'

    def __init__(self, uiParent=None):
        super(Template, self).__init__(uiParent)
        # clicked connections
        self.ui.templateQButton.clicked.connect(self.__templateQButtonAction__)
        self.ui.templateParentQButton.clicked.connect(self.__templateParentQButtonAction__)
        # init
        if cmds.ls(sl=True):
            self.ui.templateQLine.setText(cmds.ls(sl=True)[0])
        if len(cmds.ls(sl=True)) > 1:
            self.ui.templateParentQLine.setText(cmds.ls(sl=True)[1])

    def __templateQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.templateQLine.setText(cmds.ls(sl=True)[0])

    def __templateParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.templateParentQLine.setText(cmds.ls(sl=True)[0])
    
    def _getWidgetData_(self):
        self.uiWdgDict['relatedTo'] = self.ui.templateQLine.text()
        self.uiWdgDict['code'] = self.ui.templateQTextEdit.toPlainText()
        self.uiWdgDict['templateParent'] = self.ui.templateParentQLine.text()
        '''self.uiWdgDict['postExecution'] = self.ui.templateParentQLine.text()
        self.uiWdgDict['postExecution'] = self.ui.templateParentQLine.text()'''
    
    @classmethod
    def __do__(self, relatedTo, code, templateParent=None, preExecution=None, postExecution=None):
        '''Creates locator as template related to input object and set what to do'''
        if self._checkData_(relatedTo, 'relatedTo', True):
            return
        # templateRoot group
        cmds.namespace(set=":")
        namespace = relatedTo.rpartition(":")[0]
        templateRoot = "{}_00_{}".format(naming._ndTyp_dict_['template'].title(), naming._ndTyp_dict_['template'])
        if not cmds.objExists(templateRoot):
            templateRoot = cmds.createNode('transform', n=templateRoot)
            cmds.addAttr(templateRoot, ln="metadataTemplate", at="message", h=True)
        # create locator, attribute and connect
        namDict = naming.getName(relatedTo)
        namDict['system'] += naming._ndTyp_dict_['template'].title()
        if not templateParent:
            templateParent = templateRoot
        template = None
        for cnn in cmds.listConnections(relatedTo + '.message', p=True) or []:
            if '._relatedTo' in cnn:
                template = cnn.split(".")[0]
                break
        if not template:
            if "Metadata" in relatedTo:
                template = "Tpl_" + relatedTo
            else:
                template = naming.setName(**namDict)
            template = cmds.spaceLocator(n=template)[0]
            cmds.addAttr(template, ln='_relatedTo', at='message', h=True, m=True)
            cmds.parent(template, templateParent)
            cmds.connectAttr(relatedTo + ".message", template + '._relatedTo[0]')
            if cmds.nodeType(relatedTo) in cmds.nodeType('dagNode', itn=True, d=True):
                cmds.xform(template, ws=True, m=cmds.xform(relatedTo, ws=True, m=True, q=True))
        # code
        baseCode = 'import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]'
        metaD = 'MetadataTemplate'
        if not cmds.objExists(metaD):
            metaD = cmds.scriptNode(n='MetadataTemplate', beforeScript=baseCode)
            cmds.addAttr(metaD, ln='_inputTemplate', m=True, at='message')
            cmds.addAttr(metaD, ln=self.__preExecutionAttr__, m=True, at='message')
            cmds.addAttr(metaD, ln=self.__postExecutionAttr__, m=True, at='message')
            cmds.setAttr(metaD + '.ihi', 0)
            cmds.setAttr(metaD + '.nodeState', 1)
            cmds.setAttr(metaD + '.sourceType', 1, l=True)
            cmds.connectAttr(metaD + '.message', templateRoot + '.metadataTemplate')
        ind = len(cmds.listConnections(metaD + '._inputTemplate') or [])
        cmds.connectAttr(template + '.message', metaD + '._inputTemplate[{}]'.format(ind))
        if preExecution and "MetadataTemplate" in preExecution:
            cmds.connectAttr(preExecution + '.message', '{}.{}'.format(metaD, __preExecutionAttr__))
        if postExecution and "MetadataTemplate" in postExecution:
            cmds.connectAttr(postExecution + '.message', '{}.{}'.format(metaD, __postExecutionAttr__))
        currentCode = cmds.scriptNode(metaD, beforeScript=True, q=True)
        addCode = '\n#{}\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + "._inputTemplate[{}]")[0]\n'.format(relatedTo, ind)
        if not code:
            code = 'this = cmds.listConnections(template + "._relatedTo[0]")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))'
        addCode += code
        addCode += '\ndel template, this'
        cmds.scriptNode(metaD, beforeScript=currentCode + addCode, e=True)
        cmds.select(relatedTo, template)
        cmds.warning("Code create in MetadataTemplate in intput '{}'".format(template))
        return [template, metaD]

class ReversedFK(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ReversedFKWidget.ui'

    def __init__(self, uiParent=None):
        super(ReversedFK, self).__init__(uiParent)
        # clicked connections
        self.ui.chainQButton.clicked.connect(self.__chainQButtonAction__)

        self.__chainQButtonAction__()

    def __chainQButtonAction__(self):
        self.ui.chainQLine.setText(", ".join(cmds.ls(sl=True)))
    
    def _getWidgetData_(self):
        self.uiWdgDict['controlChain'] = self.ui.chainQLine.text().replace(" ","").split(",")

    @classmethod
    def __do__(self, controlChain):
        if self._checkData_(controlChain, "master", True):
            return
        cmds.namespace(set=":")
        if controlChain[0].rpartition(":")[0]:
            cmds.namespace(set=controlChain[0].rpartition(":")[0])
        result = []
        for ind, ctr in enumerate(controlChain):
            ctDict = naming.getName(ctr)
            ctDict['system'] += 'Rev'
            ctDict['nodeType'] = 'constraintAux'
            aux = cmds.createNode('transform', p=ctr, n=naming.setName(**ctDict))
            ctDict['nodeType'] = 'parentConstraint'
            #ctDict['system'] = ctDict['system'] + naming._ndTyp_dict_['constraintAux'].title()
            if ind < len(controlChain) - 1:
                cns = cmds.createNode('parentConstraint', p=aux, n=naming.setName(**ctDict))
                cmds.connectAttr(ctr + '.wm[0]', cns + '.target[0].tpm')
                cmds.connectAttr(controlChain[ind+1] + '.wim[0]', cns + '.cpim')
                cmds.connectAttr(cns + '.ct', aux + '.t')
                cmds.connectAttr(cns + '.cr', aux + '.r')
            if ind:
                #cmds.connectAttr(controlChain[ind+1] + '.wim[0]', cns + '.cpim')
                revCtr = Control.__do__(ctDict['system'], ctDict['num'], aux, aux)
                cmds.parent(result[-1], revCtr[-1])
            result.append(aux)
        cmds.setAttr(controlChain[0] + '.r', 0,0,0)
        cmds.select(result)
        cmds.namespace(set=":")
        return result

class Sets(BaseWidget):
    __uiPath__ = r'AutoRig\ui\SetsWidget.ui'

    def __init__(self, uiParent=None):
        super(Sets, self).__init__(uiParent)
        # clicked connections
        self.ui.controlsQButton.clicked.connect(self.__controlsQButtonAction__)
        self.ui.secondaryControlsQButton.clicked.connect(self.__secondaryControlsQButtonAction__)
        self.ui.skinJointsQButton.clicked.connect(self.__skinJointsQButtonAction__)
        self.ui.linkQButton.clicked.connect(self.__linkQButtonAction__)
        
    def __controlsQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.controlsQLine.setText(", ".join(sel))

    def __secondaryControlsQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.secondaryControlsQLine.setText(", ".join(sel))
    
    def __skinJointsQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.skinJointsQLine.setText(", ".join(sel))
    
    def __linkQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.linkQLine.setText(", ".join(sel))
    
    def _getWidgetData_(self):
        if self.ui.controlsQLine.text():
            self.uiWdgDict['controls'] = self.ui.controlsQLine.text().replace(" ","").split(",")
        if self.ui.secondaryControlsQLine.text():
            self.uiWdgDict['secondaryControls'] = self.ui.secondaryControlsQLine.text().replace(" ","").split(",")
        if self.ui.skinJointsQLine.text():
            self.uiWdgDict['skinJoints'] = self.ui.skinJointsQLine.text().replace(" ","").split(",")
        if self.ui.linkQLine.text():
            self.uiWdgDict['link'] = self.ui.linkQLine.text().replace(" ","").split(",")
    
    @classmethod
    def __do__(self, controls=[], secondaryControls=[], skinJoints=[], link=[]):
        if controls and self._checkData_(controls, "controls", True):
            return
        if skinJoints and self._checkData_(skinJoints, "skinJoints", True):
            return
        if link and self._checkData_(link, "link", True):
            return
        for setNode,setContent in zip(["ControlsSet","Secondaries","SkinJointsSet","LinkSet"], [controls,secondaryControls,skinJoints,link]):
            if cmds.objExists(setNode):
                cmds.sets(setContent, forceElement=setNode, edit=True)
            else:
                cmds.sets(setContent, n=setNode)
        if "Secondaries" not in cmds.sets("ControlsSet",q=True):
            cmds.sets("Secondaries", fe="ControlsSet",e=True)
        cmds.warning("Sets | Result: 1")
        return "ControlsSet","SkinJointsSet","LinkSet"

class OptimizedConstraint(BaseWidget):
    __uiPath__ = r'AutoRig\ui\OptimizedConstraintWidget.ui'

    def __init__(self, uiParent=None):
        super(OptimizedConstraint, self).__init__(uiParent)
        # clicked connections
        self.ui.masterQButton.clicked.connect(self.__masterQButtonAction__)
        self.ui.slaveQButton.clicked.connect(self.__slaveQButtonAction__)
        # ui init behaviour
        if cmds.ls(sl=True):
            self.ui.masterQLine.setText(", ".join(cmds.ls(sl=True)[:-1]))
            self.ui.slaveQLine.setText(cmds.ls(sl=True)[-1])
    
    def __masterQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.masterQLine.setText(", ".join(sel[:2]))

    def __slaveQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.slaveQLine.setText(cmds.ls(sl=True)[0])
    
    def _getWidgetData_(self):
        self.uiWdgDict['master'] = self.ui.masterQLine.text().replace(" ","").split(",")
        self.uiWdgDict['slave'] = self.ui.slaveQLine.text()
        self.uiWdgDict['cType'] = self.ui.cTypeQCombo.currentText()
    
    @classmethod
    def __do__(self, master, slave, cType='parent'):
        if self._checkData_(master, "master", True) or self._checkData_(slave, "slave", True):
            return
        if type(master) != list:
            master = [master]
        csMasterDict = naming.getName(slave)
        csMasterDict['num'] = int(csMasterDict['num'])
        slaveNdTp = naming._ndTyp_dict_[csMasterDict['nodeType']]
        csMasterDict['nodeType'] = cType + "Constraint"
        csMasterDict['system'] += slaveNdTp.title()
        cmds.namespace(set=":")
        if slave.rpartition(":")[0]:
            cmds.namespace(set=slave.rpartition(":")[0])
        cns = cmds.createNode('{}Constraint'.format(cType), p=slave, n=naming.setName(**csMasterDict))
        csMasterDict['nodeType'] = "constraintAux"
        for ind, mst in enumerate(master):
            cmst = cmds.duplicate(slave, po=True, n=naming.setName(**csMasterDict))[0]
            cmds.parent(cmst, mst)
            cmds.connectAttr(cmst + '.wm[0]', '{}.target[{}].targetParentMatrix'.format(cns, ind))
        cmds.connectAttr(slave + '.pim[0]', cns + '.cpim')
        if cType in ['parent','point']:
            cmds.connectAttr(cns + '.constraintTranslateX', slave + '.tx')
            cmds.connectAttr(cns + '.constraintTranslateY', slave + '.ty')
            cmds.connectAttr(cns + '.constraintTranslateZ', slave + '.tz')
        if cType in ['parent','orient']:
            cmds.connectAttr(cns + '.constraintRotateX', slave + '.rx')
            cmds.connectAttr(cns + '.constraintRotateY', slave + '.ry')
            cmds.connectAttr(cns + '.constraintRotateZ', slave + '.rz')
        if cType == 'scale':
            cmds.connectAttr(cns + '.constraintScaleX', slave + '.rx')
            cmds.connectAttr(cns + '.constraintScaleY', slave + '.ry')
            cmds.connectAttr(cns + '.constraintScaleZ', slave + '.rz')
        cmds.select(master, slave)
        cmds.namespace(set=":")
        return cns

class ControlTag(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ControlTagWidget.ui'
    hierarchy = ['rig','export','controls','setup','geo','templates']

    def __init__(self, uiParent=None):
        super(ControlTag, self).__init__(uiParent)
        self.ui.controlQButton.clicked.connect(self.__controlQButtonAction__)
        self.ui.controlParentQButton.clicked.connect(self.__controlParentQButtonAction__)
        self.ui.controlChildrensQButton.clicked.connect(self.__controlChildrensQButtonAction__)

        for ind, elem in enumerate(cmds.ls(sl=True) or []):
            if not ind:
                self.ui.controlQLine.setText(elem)
            else:
                self.ui.controlParentQLine.setText(elem)

    def __controlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.controlQLine.setText(cmds.ls(sl=True)[0])

    def __controlParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.controlParentQLine.setText(cmds.ls(sl=True)[0])

    def __controlChildrensQButtonAction__(self):
        self.ui.controlChildrensQLine.setText(", ".join(cmds.ls(sl=True)))
    
    def _getWidgetData_(self):
        self.uiWdgDict['control'] = self.ui.controlQLine.text()
        self.uiWdgDict['controlParent'] = self.ui.controlParentQLine.text()
        self.uiWdgDict['controlParentMode'] = "a" if self.ui.controlParentAddModeQRadio.isChecked() else "r"
        if self.ui.controlChildrensQLine.text():
            self.uiWdgDict['controlChildrens'] = self.ui.controlChildrensQLine.text().replace(" ","").split(",")
    
    @classmethod
    def __do__(self, control, controlParent=None, controlParentMode="r", controlChildrens=[]):
        if self._checkData_(control, "control", True):
            return
        def __createTag__(_control_):
            tagName = naming.getName(_control_)
            tagName['nodeType'] = "controller"
            tag = cmds.createNode("controller", n=naming.setName(**tagName))
            cmds.connectAttr(_control_ + ".message", tag + ".controllerObject")
            cmds.namespace(set=":")
            return tag
        def __queryTag__(_control_):
            msgConecctions = cmds.listConnections(_control_ + ".message")
            if not msgConecctions:
                return __createTag__(_control_)
            tag = None
            for cnn in msgConecctions:
                if cmds.nodeType(cnn) == "controller":
                    tag = cnn
                    break
            if not tag:
                return __createTag__(_control_)
            return tag
        def __fixChildrenConnections__():
            for tag in cmds.ls(type='controller'):
                if not cmds.listConnections(tag + ".children"):
                    cmds.connectAttr(tag + ".message", tag + ".children[0]")
        cmds.namespace(set=":")
        if control.rpartition(":")[0]:
            cmds.namespace(set=control.rpartition(":")[0])
        if controlParentMode not in "ra":
            cmds.warning('Arg "controlParentMode" must be "r" (replace) or "a" (add)')
            return
        thisTag = __queryTag__(control)
        result = [thisTag]
        for child in controlChildrens:
            childTag = __queryTag__(child)
            result.append( childTag )
            children = cmds.listConnections(thisTag + ".children", p=True) or []
            ind = len(children)
            if thisTag + ".message" in children:
                cmds.disconnectAttr(thisTag + ".message", thisTag + ".children[0]")
                ind = 0
            if childTag + ".parent" not in children:
                cmds.connectAttr(childTag + ".parent", "{}.children[{}]".format(thisTag, ind))
        if not controlParent:
            __fixChildrenConnections__()
            cmds.warning("{} | Result: 1".format(control))
            return result
        currentParentTag = cmds.listConnections(thisTag + ".parent", p=True) or []
        if controlParentMode == "r" and currentParentTag:
            cmds.disconnectAttr(thisTag + ".parent", currentParentTag[0])
        parentTag = __queryTag__(controlParent)
        result.append( parentTag )
        parentTagChildren = cmds.listConnections(parentTag + ".children", p=True) or []
        ind = len(parentTagChildren)
        if parentTag + ".message" in parentTagChildren:
            cmds.disconnectAttr(parentTag + ".message", parentTag + ".children[0]")
            ind = 0
        if thisTag + ".parent" not in parentTagChildren:
            cmds.connectAttr(thisTag + ".parent", "{}.children[{}]".format(parentTag, ind), f=True)
        __fixChildrenConnections__()
        cmds.namespace(set=":")
        cmds.warning("{} | Result: 1".format(control))
        return result

class ControlAttr(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ControlAttrWidget.ui'

    def __init__(self, uiParent=None):
        super(ControlAttr, self).__init__(uiParent)

    def _getWidgetData_(self):
        self.uiWdgDict['longName'] = self.ui.longNameQLine.text()
        self.uiWdgDict['isDisplayed'] = self.ui.isDisplayedQCheck.isChecked()
        self.uiWdgDict[{0:'at', 1:'dt'}[self.ui.typeQCombo.currentIndex()]] = self.ui.typeQLine.text()
        self.uiWdgDict['k'] = self.ui.isKeyableQCheck.isChecked()
        for arg in self.ui.otherArgsQLine.text().replace(" ","").split(","):
            if not arg:
                continue
            arg = arg.replace("'","").replace('"','')
            argName, argVal = arg.split("=")
            neg = False
            if argVal.startswith("-"):
                neg = True
                argVal = argVal[1:]
            if "." in argVal:
                argVal = -float(argVal) if neg else float(argVal)
            elif argVal.isdigit():
                argVal = -int(argVal) if neg else int(argVal)
            elif type(argVal) == unicode:
                argVal = str(argVal)
            self.uiWdgDict[str(argName)] = argVal
    
    @classmethod
    def __do__(self, inputNode, longName, isDisplayed=True, **attrDict):
        cmds.addAttr(inputNode, ln=longName, **attrDict)
        if 'k' in attrDict.keys() and not attrDict['k'] and isDisplayed:
            cmds.setAttr('{}.{}'.format(inputNode, longName), cb=True)
        elif 'keyable' in attrDict.keys() and not attrDict['keyable'] and isDisplayed:
            cmds.setAttr('{}.{}'.format(inputNode, longName), cb=True)

class Control(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ControlWidget.ui'

    def __init__(self, uiParent=None):
        super(Control, self).__init__(uiParent)
        # clicked connections
        self.ui.controlParentQButton.clicked.connect(self.__controlParentQButtonAction__)
        self.ui.controlSnapQButton.clicked.connect(self.__controlSnapQButtonAction__)
        self.ui.newAttrAddQButton.clicked.connect(self.__newAttrAddQButtonAction__)
        self.ui.newAttrRemoveQButton.clicked.connect(self.__newAttrRemoveQButtonAction__)
        self.ui.keyAllTQCheck.stateChanged.connect(self.__keyAllTCheckChange__)
        self.ui.keyAllRQCheck.stateChanged.connect(self.__keyAllRCheckChange__)
        self.ui.keyAllSQCheck.stateChanged.connect(self.__keyAllSCheckChange__)
        self.ui.keyAllXQCheck.stateChanged.connect(self.__keyAllXCheckChange__)
        self.ui.keyAllYQCheck.stateChanged.connect(self.__keyAllYCheckChange__)
        self.ui.keyAllZQCheck.stateChanged.connect(self.__keyAllZCheckChange__)
        # initialize
        self.attrWidget = []
        # ui init behaviour
        self.__controlParentQButtonAction__()
        self.__controlSnapQButtonAction__()

    def __keyAllTCheckChange__(self):
        val = self.ui.keyAllTQCheck.isChecked()
        self.ui.keyTXQCheck.setChecked(val)
        self.ui.keyTYQCheck.setChecked(val)
        self.ui.keyTZQCheck.setChecked(val)

    def __keyAllRCheckChange__(self):
        val = self.ui.keyAllRQCheck.isChecked()
        self.ui.keyRXQCheck.setChecked(val)
        self.ui.keyRYQCheck.setChecked(val)
        self.ui.keyRZQCheck.setChecked(val)

    def __keyAllSCheckChange__(self):
        val = self.ui.keyAllSQCheck.isChecked()
        self.ui.keySXQCheck.setChecked(val)
        self.ui.keySYQCheck.setChecked(val)
        self.ui.keySZQCheck.setChecked(val)

    def __keyAllXCheckChange__(self):
        val = self.ui.keyAllXQCheck.isChecked()
        self.ui.keyTXQCheck.setChecked(val)
        self.ui.keyRXQCheck.setChecked(val)
        self.ui.keySXQCheck.setChecked(val)

    def __keyAllYCheckChange__(self):
        val = self.ui.keyAllYQCheck.isChecked()
        self.ui.keyTYQCheck.setChecked(val)
        self.ui.keyRYQCheck.setChecked(val)
        self.ui.keySYQCheck.setChecked(val)

    def __keyAllZCheckChange__(self):
        val = self.ui.keyAllZQCheck.isChecked()
        self.ui.keyTZQCheck.setChecked(val)
        self.ui.keyRZQCheck.setChecked(val)
        self.ui.keySZQCheck.setChecked(val)

    def __controlParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.controlParentQLine.setText(cmds.ls(sl=True)[0])

    def __controlSnapQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.controlSnapQLine.setText(cmds.ls(sl=True)[0])

    def __newAttrAddQButtonAction__(self):
        self.ui.attrsQScroll.setMaximumHeight(100)
        cAttrWidget = ControlAttr(self)
        self.ui.newAttrQVLayout.addWidget(cAttrWidget)
        self.attrWidget.append(cAttrWidget)

    def __newAttrRemoveQButtonAction__(self):
        if self.ui.newAttrQVLayout.count():
            child = self.ui.newAttrQVLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            del self.attrWidget[0]
        else:
            self.ui.attrsQScroll.setMaximumHeight(0)
    
    def _getWidgetData_(self):
        self.uiWdgDict['systemName'] = self.ui.systemNameQLine.text()
        self.uiWdgDict['systemNum'] = self.ui.systemNumQSpin.value()
        self.uiWdgDict['controlParent'] = self.ui.controlParentQLine.text()
        self.uiWdgDict['controlSnap'] = self.ui.controlSnapQLine.text()
        self.uiWdgDict['groupsNum'] = self.ui.groupsQSpin.value()
        keyableAttrsLs = []
        if self.ui.keyVQCheck.isChecked():
            keyableAttrsLs = ["v"]
        for qname, qcheck in self.ui.__dict__.items():
            if not all(["key" in qname, "All" not in qname, qname.endswith("QCheck")]):
                continue
            if qcheck.isChecked():
                keyableAttrsLs.append(qcheck.text())
        self.uiWdgDict['keyableAttrs'] = keyableAttrsLs

    def __widgetDo__(self):
        self._getWidgetData_()
        ctr = self.__do__(**self.uiWdgDict)
        if not ctr:
            cmds.warning("Control not created | Result: 0")
            return
        for at in self.attrWidget:
            at.uiWdgDict['inputNode'] = ctr[-1]
            at.__widgetDo__()

    @classmethod
    def __do__(self, systemName, systemNum=0, controlParent=None, controlSnap=None, groupsNum=1, keyableAttrs=["tx","ty","tz","rx","ry","rz"]):
        #print keyableAttrs, ">"*10
        if self._checkData_(systemName, 'systemName'):
            return
        namingDict = {'system':systemName,
                      'nodeType':'control',
                      'num':systemNum}
        this = cmds.circle(n=naming.setName(**namingDict), ch=0, r=10)[0]
        grpsId = ['root'] + ['offset']*(groupsNum-1)
        grps = []
        for it in range(groupsNum):
            namingDict['nodeType'] = grpsId[it]
            grps.append( cmds.group(this, n=naming.setName(**namingDict)) )
        if controlSnap:
            cmds.delete(cmds.parentConstraint(controlSnap, grps[0]))
        if controlParent:
            cmds.parent(grps[0], controlParent)
        #print list(set(["tx","ty","tz","rx","ry","rz","sx","sy","sz","v"]) - set(keyableAttrs)), "<"*15
        for at in set(["tx","ty","tz","rx","ry","rz","sx","sy","sz","v"]) - set(keyableAttrs):
            cmds.setAttr("{}.{}".format(this, at), k=False, l=True)
        cmds.select(this)
        return grps + [this]

class Joint(BaseWidget):
    __uiPath__ = r'AutoRig\ui\JointWidget.ui'
    parentAttribute = "parent"

    def __init__(self, uiParent=None):
        super(Joint, self).__init__(uiParent)
        # clicked connections
        self.ui.jointParentQButton.clicked.connect(self.__jointParentQButtonAction__)
        self.ui.jointSnapQButton.clicked.connect(self.__jointSnapQButtonAction__)
        # ui init behaviour
        self.__jointParentQButtonAction__()
        self.__jointSnapQButtonAction__()
        
    def __jointParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.jointParentQLine.setText(cmds.ls(sl=True)[0])

    def __jointSnapQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.jointSnapQLine.setText(cmds.ls(sl=True)[0])

    def _getWidgetData_(self):
        self.uiWdgDict['systemName'] = self.ui.systemQLine.text()
        self.uiWdgDict['systemNum'] = self.ui.systemNumQSpin.value()
        self.uiWdgDict['parent'] = self.ui.jointParentQLine.text() or None
        self.uiWdgDict['snap'] = self.ui.jointSnapQLine.text()
        self.uiWdgDict['connect'] = self.ui.jointConnectQCheck.isChecked()

    @classmethod
    def __do__(self, systemName="", systemNum=0, parent=None, snap=None, connect=True):
        jointDict = {'system':systemName,
                     'num':systemNum,
                     'nodeType':'joint'}
        joint = cmds.createNode('joint', p=parent, n=naming.setName(**jointDict))
        cmds.addAttr(joint, ln=self.parentAttribute, at='message', k=False)
        if parent and connect:
            cmds.connectAttr(parent + ".message", "{}.{}".format(joint, parentAttribute))
        if snap:
            cmds.delete(cmds.parentConstraint(snap, joint))
        return joint

class Chain(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ChainWidget.ui'

    def __init__(self, uiParent=None):
        super(Chain, self).__init__(uiParent)
        # clicked connections
        self.ui.chainParentQButton.clicked.connect(self.__chainParentQLineUpdate__)
        self.ui.preferredAngleQCombo.setCurrentIndex(3)
        # ui init behaviour
        self.__chainParentQLineUpdate__()
        
    def __chainParentQLineUpdate__(self):
        if cmds.ls(sl=True):
            self.ui.chainParentQLine.setText(cmds.ls(sl=True)[0])

    def _getWidgetData_(self):
        indexDict = {0:[1,0,0], 1:[-1,0,0],
                     2:[0,1,0], 3:[0,-1,0],
                     4:[0,0,1], 5:[0,0,-1]}
        self.uiWdgDict['systemName'] = self.ui.systemQLine.text()
        self.uiWdgDict['members'] = self.ui.membersQBox.value()
        self.uiWdgDict['direction'] = indexDict[self.ui.directionQCombo.currentIndex()]
        self.uiWdgDict['preferredAngle'] = indexDict[self.ui.preferredAngleQCombo.currentIndex()]
        self.uiWdgDict['chainParent'] = self.ui.chainParentQLine.text() or None

    @classmethod
    def __do__(self, systemName="", members=2, direction=[1,0,0], preferredAngle=[0,-1,0], chainParent=None):
        result = [chainParent]
        for iterNum in range(members):
            jnt = Joint.__do__(systemName, iterNum, result[-1])
            cmds.setAttr(jnt + '.preferredAngle', *[90 * ax for ax in preferredAngle])
            if iterNum:
                cmds.setAttr(jnt + '.t', *direction*5)
                cmds.connectAttr(result[-1] + '.scale', jnt + '.inverseScale')
            result.append(jnt)
        del result[0]
        return result

class ChainCrvBased(BaseWidget):
    __uiPath__ = r'AutoRig\ui\ChainCrvBasedWidget.ui'

    def __init__(self, uiParent=None):
        super(ChainCrvBased, self).__init__(uiParent)
        # clicked connections
        self.ui.chainParentQButton.clicked.connect(self.__chainParentQLineAction__)
        self.ui.curveQButton.clicked.connect(self.__curveQButtonAction__)
        self.ui.sourceUpQButton.clicked.connect(self.__sourceUpQButtonAction__)
        # ui init behaviour
        self.ui.sourceVectorUpQCombo.setCurrentIndex(2)
        sel = cmds.ls(sl=True)
        if sel:
            shp = cmds.listRelatives(sel[0], s=True)
            if shp and cmds.nodeType(shp[0]) == "nurbsCurve":
                self.ui.curveQLine.setText(sel[0])
            else:
                self.ui.chainParentQLine.setText(sel[0])
        if len(sel) > 1:
            self.ui.chainParentQLine.setText(sel[1])
        if len(sel) > 2:
            self.ui.sourceUpQLine.setText(sel[2])
        if len(sel) > 3:
            self.ui.sourceUpQLine.setText(", ".join(sel[2:4]))
    
    def __sourceUpQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.sourceUpQLine.setText(", ".join(sel[:2]))
        
    def __chainParentQLineAction__(self):
        sel = cmds.ls(sl=True)
        curveQLine = self.ui.curveQLine.text()
        if sel and sel[0] != curveQLine:
            self.ui.chainParentQLine.setText(sel[0])
    
    def __curveQButtonAction__(self):
        sel = cmds.ls(sl=True)
        if not sel:
            return
        for elem in sel:
            shp = cmds.listRelatives(elem, s=True)
            if shp and cmds.nodeType(shp[0]) == "nurbsCurve":
                self.ui.curveQLine.setText(elem)
    
    def _getWidgetData_(self):
        self.uiWdgDict['systemName'] = self.ui.systemNameQLine.text()
        self.uiWdgDict['curve'] = self.ui.curveQLine.text()
        self.uiWdgDict['members'] = self.ui.membersQBox.value()
        self.uiWdgDict['chainParent'] = self.ui.chainParentQLine.text() or None
        self.uiWdgDict['hierarchize'] = self.ui.hierarchizeQRadio.isChecked()
        self.uiWdgDict['keepConnections'] = self.ui.connectionsQRadio.isChecked()
        self.uiWdgDict['alignRotateToCurve'] = self.ui.alignToCrvQRadio.isChecked()
        self.uiWdgDict['connectParentAttr'] = self.ui.connectParentAttrQCheck.isChecked()
        sourceUp = self.ui.sourceUpQLine.text().replace(" ","").split(",")
        vectorDict = {0:[1,0,0], 1:[-1,0,0],
                      2:[0,1,0], 3:[0,-1,0],
                      4:[0,0,1], 5:[0,0,-1]}
        if sourceUp[0]:
            if self.ui.rotationUpQRadio.isChecked():
                self.uiWdgDict['rotationUp'] = sourceUp
                self.uiWdgDict['objectUp'] = []
            elif self.ui.objectUpQRadio.isChecked():
                self.uiWdgDict['objectUp'] = sourceUp
                self.uiWdgDict['rotationUp'] = []
        self.uiWdgDict['aimv'] = vectorDict[self.ui.directionQCombo.currentIndex()]
        self.uiWdgDict['vectorUp'] = vectorDict[self.ui.sourceVectorUpQCombo.currentIndex()]
    
    @classmethod
    def __do__(self, curve, systemName="Spl", members=3, aimv=[1,0,0], alignRotateToCurve=False, objectUp=[], rotationUp=[], vectorUp=[0,1,0], chainParent=None, hierarchize=True, keepConnections=False, connectParentAttr=False):
        if self._checkData_(curve, "curve", True):
            return
        if hierarchize and keepConnections:
            cmds.warning("Arg 'hierarchize' and 'keepConnections' both can not be True")
            return
        twistAx = '.rx'
        result = []
        toDelete = []
        twistResult = [None]
        finalUp = None
        twist = False
        mpWUOVal = None
        aimDict = {'aim':aimv,
                'u':vectorUp,
                'worldUpVector':[0,1,0],
                'worldUpType':'vector'}
        mpWUTVal = 3
        if [aimv[0], aimv[2]] == [0,0]:
            twistAx = '.ry'
        elif [aimv[0], aimv[1]] == [0,0]:
            twistAx = '.rz'
        if rotationUp:
            if objectUp:
                cmds.warning("Arg 'objectUp' and 'rotationUp' both can not be setted")
                return
            aimDict['worldUpType'] = 'objectrotation'
            aimDict['worldUpObject'] = rotationUp[0]
            mpWUTVal = 2
            finalUp = rotationUp
            mpWUOVal = rotationUp[0]
            if len(rotationUp) > 1:
                twist = True
        elif objectUp:
            aimDict['worldUpType'] = 'object'
            aimDict['worldUpObject'] = objectUp[0]
            mpWUTVal = 1
            finalUp = objectUp
            mpWUOVal = objectUp[0]
            if len(objectUp) > 1:
                twist = True
        
        # Align to curve
        for ind in range(members):
            jnt = Joint.__do__(systemName, parent=chainParent, connect=connectParentAttr)
            mp = cmds.createNode('motionPath', n=naming.setName(systemName, 'motionPath', ind))
            uval = cmds.arclen(curve)/max((members-1), 1)
            uval = uval/cmds.arclen(curve)*(ind)
            cmds.connectAttr(curve + '.ws[0]', mp + '.geometryPath')
            cmds.setAttr(mp + '.fractionMode', True)
            cmds.setAttr(mp + '.uValue', uval)
            cmds.setAttr(jnt + ".t", *cmds.getAttr(mp + ".allCoordinates")[0]) # alignCrv ; pose ; no rot or obj up
            result.append(jnt)
            if ind and not alignRotateToCurve:
                cmds.connectAttr(mp + ".allCoordinates", jnt + ".t")
                if not keepConnections:
                    cmds.delete(mp)
                continue
            cmds.setAttr(mp + '.rotateOrder', cmds.getAttr(jnt + '.rotateOrder'))
            cmds.setAttr(mp + '.worldUpType', mpWUTVal)
            cmds.setAttr(mp + '.frontAxis', aimv.index(1) if 1 in aimv else aimv.index(-1))
            cmds.setAttr(mp + '.upAxis', vectorUp.index(1) if 1 in vectorUp else vectorUp.index(-1))
            if -1 in vectorUp:
                cmds.setAttr(mp + '.inverseUp', True)
            if -1 in aimv:
                cmds.setAttr(mp + '.inverseFront', True)
            if mpWUOVal: # alignCrv ; pose ; rot/obj up 1
                cmds.setAttr(mp + '.worldUpVector', *vectorUp)
                if ind == (members - 1) and twist:
                    mpWUOVal = finalUp[1]
                if ind != (members - 1) and twist: # alignCrv ; pose ; rot/obj up 2
                    rot = cmds.getAttr(finalUp[1] + twistAx) - cmds.getAttr(finalUp[0] + twistAx)
                    cmds.setAttr(mp + '.frontTwist', rot * (1.0/(members-1) * ind))
                cmds.setAttr(mp + '.worldUpMatrix', cmds.getAttr(mpWUOVal + '.wm[0]'), type='matrix')
            cmds.setAttr(jnt + '.rotate', *cmds.getAttr(mp + '.rotate')[0])
            if not keepConnections:
                cmds.delete(mp)
                continue
            #cmds.connectAttr(mp + ".orientMatrix", jnt + ".offsetParentMatrix")
            cmds.connectAttr(mp + ".allCoordinates", jnt + ".t")
            cmds.connectAttr(mp + '.rotate', jnt + '.rotate') # alignCrv ; connect
            if mpWUOVal: # alignCrv ; connect ; at least rot/obj up 1
                cmds.connectAttr(mpWUOVal + '.wm[0]', mp + '.worldUpMatrix')
            if not twist or ind in [0, members - 1]:
                continue
            # alignCrv ; connect ; rot/obj up 2
            minus = cmds.createNode('floatMath', n=naming.setName(systemName, 'floatMath', ind))
            blendClr = cmds.createNode('blendColors', n=naming.setName(systemName, 'blendColors', ind))            
            cmds.setAttr(minus + ".operation", 1)
            cmds.setAttr(blendClr + '.blender', 1.0/ max(members-1, 1) * ind)
            cmds.connectAttr(result[0] + twistAx, minus + '.floatB')
            cmds.connectAttr(minus + '.outFloat', blendClr + '.c1r')
            cmds.connectAttr(blendClr + '.outputR', mp + '.frontTwist')
            twistResult.append(minus)
            
        if members <= 1:
            return result
        if alignRotateToCurve:
            for ind in range(1,members):
                if hierarchize:
                    cmds.parent(result[ind], result[ind-1])
                    cmds.connectAttr(result[ind-1] + ".message", "{}.{}".format(result[ind], Joint.parentAttribute), force=True)
                if len(twistResult) > 1 and twist and ind != members - 1:
                    cmds.connectAttr(result[-1] + twistAx, twistResult[ind] + ".floatA")
            return result
        
        # aling to next child
        for ind, memb in enumerate(result):
            if ind == (members - 1):
                cnsMst = result[ind-1]
                aimDict['aim'] = [-1*a for a in aimDict['aim']]
                if twist and memb:
                    aimDict['worldUpObject'] = finalUp[1]
            else:
                cnsMst = result[ind+1]
            if 'worldUpObject' in aimDict.keys():
                aimDict['worldUpVector'] = aimDict['u']
            cns = cmds.aimConstraint(cnsMst, memb, **aimDict)[0]
            cmds.setAttr(memb + ".jo", 0,0,0)
            if ind in [0, members - 1] or not twist:
                if not keepConnections:
                    cmds.delete(cns)
                continue
            blendMtx = cmds.createNode('blendMatrix')
            cmds.connectAttr(result[0] + ".wm[0]", blendMtx + ".inputMatrix")
            cmds.connectAttr(result[-1] + ".wm[0]", blendMtx + ".target[0].targetMatrix")
            cmds.setAttr(blendMtx + ".target[0].useScale", 0)
            cmds.setAttr(blendMtx + ".target[0].useTranslate", 0)
            cmds.setAttr(blendMtx + ".target[0].useShear", 0)
            cmds.setAttr(blendMtx + ".target[0].weight", 1.0/(members-1)*ind)
            cmds.setAttr(cns + ".worldUpType", 2)
            cmds.setAttr(cns + ".worldUpVector", *aimDict['u'])
            cmds.connectAttr(blendMtx + ".outputMatrix", cns + ".worldUpMatrix", force=True)
            if not keepConnections:
                toDelete.extend([cns, blendMtx])
                continue
        if toDelete:
            cmds.delete(toDelete)
        if not hierarchize:
            return result
        for ind in range(1, members):
            cmds.parent(result[ind], result[ind-1])
            cmds.connectAttr(result[ind-1] + ".message", "{}.{}".format(result[ind], Joint.parentAttribute), force=True)
        return result

class SpaceSwitch(BaseWidget):
    __uiPath__ = r'AutoRig\ui\SpaceSwitchWidget.ui'

    def __init__(self, uiParent=None):
        super(SpaceSwitch, self).__init__(uiParent)
        # clicked connections
        self.ui.targetQButton.clicked.connect(self.__targetQLineUpdate__)
        self.ui.attrSourceQButton.clicked.connect(self.__attrSourceQButtonAction__)
        self.ui.spacesParentQButton.clicked.connect(self.__spacesParentQButtonAction__)
        # ui init behaviour
        self.__targetQLineUpdate__()
        self.__attrSourceQButtonAction__()

    def __targetQLineUpdate__(self):
        if cmds.ls(sl=True):
            self.ui.targetQLine.setText(cmds.ls(sl=True)[0])

    def __attrSourceQButtonAction__(self):
        sel = cmds.ls(sl=True)
        at = cmds.channelBox('mainChannelBox', sma=True, q=True)
        if sel and at:
            self.ui.attrSourceQLine.setText("{}.{}".format(sel[0], at[0]))
    
    def __spacesParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.spacesParentQLine.setText(", ".join(cmds.ls(sl=True)))
    
    def _getWidgetData_(self):
        self.uiWdgDict['target'] = self.ui.targetQLine.text()
        self.uiWdgDict['attrSource'] = self.ui.attrSourceQLine.text()
        self.uiWdgDict['constraint'] = self.ui.constraintQCombo.currentText()
        self.uiWdgDict['spacesParent'] = self.ui.spacesParentQLine.text().replace(" ","").split(",")

    @classmethod
    def __do__(self, target, attrSource, constraint='parent', spacesParent=[]):
        if self._checkData_(target, "target", True) or self._checkData_(attrSource, "attrSource", True):
            return
        spaces = cmds.addAttr(attrSource, en=True, q=True).split(":")
        spacesParent = spacesParent + [None] * abs(len(spaces) - len(spacesParent))
        resultGroups = []
        resultChoices = []
        doublePoint = False
        cmds.namespace(set=":")
        if target.rpartition(":")[0]:
            cmds.namespace(set=target.rpartition(":")[0])
        if constraint == 'doublePoint':
            doublePoint = True
            constraint = "point"
        for ind, spc in enumerate(spaces):
            spcDict = naming.getName(target)
            cnsDict = naming.getName(target)
            spcDict['system'] += (spc[0].title() + spc[1:])
            spcDict['nodeType'] = "space"
            cnsDict['nodeType'] = constraint + "Constraint"
            spc = cmds.createNode('transform', n=naming.setName(**spcDict))
            cmds.delete(cmds.parentConstraint(target, spc))
            resultGroups.append(spc)
            if doublePoint:
                csn = cmds.pointConstraint(attrSource.split(".")[0], spc, mo=True)[0]
            cns = eval('cmds.{}Constraint(spc, target, n=naming.setName(**cnsDict))'.format(constraint, spc))[0]
            if spacesParent[ind]:
                cmds.parent("{}".format(spc), spacesParent[ind])
                cmds.setAttr("{}.t".format(spc), 0,0,0)
                cmds.setAttr("{}.r".format(spc), 0,0,0)
        if constraint not in ['point','scale']:
            cmds.setAttr(cns + '.interpType', 0)
        targets = cmds.listAttr(cns, ud=True)
        for ind, spc in enumerate(spaces):
            chDict = naming.getName(spc)
            chDict['system'] = "Space" + chDict['system']
            chDict['nodeType'] = "choice"
            choice = cmds.createNode('choice', n=naming.setName(**chDict))
            resultChoices.append(choice)
            resultChoices.append(choice)
            map(lambda chInd: cmds.setAttr('{}.input[{}]'.format(choice, chInd), 0), range(len(spaces)))
            cmds.setAttr('{}.input[{}]'.format(choice, ind), 1)
            cmds.connectAttr(attrSource, choice + '.selector')
            cmds.connectAttr(choice + '.output', '{}.{}'.format(cns, targets[ind]))
        cmds.namespace(set=":")
        return resultGroups, cns, resultChoices

class StretchLocDist(BaseWidget):
    __uiPath__ = r'AutoRig\ui\StretchLocDistWidget.ui'

    def __init__(self, uiParent=None):
        super(StretchLocDist, self).__init__(uiParent)
        # clicked connections
        self.ui.chainQButton.clicked.connect(self.__chainQButtonAction__)
        self.ui.referencesQButton.clicked.connect(self.__referencesQButtonAction__)
        # ui init behaviour
        self.__chainQButtonAction__()
    
    def __chainQButtonAction__(self):
        sel = cmds.ls(sl=True)
        jntLs = []
        for elem in sel:
            if cmds.nodeType(elem) == 'joint':
                jntLs.append(elem)
        if not jntLs:
            return
        self.ui.chainQLine.setText(", ".join(jntLs))
    
    def __referencesQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.referencesQLine.setText(", ".join(sel[:2]))

    def _getWidgetData_(self):
        self.uiWdgDict['chain'] = self.ui.chainQLine.text().replace(" ","").split(",")
        start, end = self.ui.referencesQLine.text().replace(" ","").split(",")
        self.uiWdgDict['startPoint'] = start
        self.uiWdgDict['endPoint'] = end
        
    @classmethod
    def __do__(self, chain, startPoint, endPoint):
        if self._checkData_(chain, 'chain', True) or self._checkData_(startPoint, 'startPoint', True) or self._checkData_(endPoint, 'endPoint', True):
            return
        distDict = naming.getName(startPoint)
        distDict['nodeType'] = 'distanceBetween'
        dist = naming.setName(**distDict)
        distDict['nodeType'] = 'locator'
        sloc = naming.setName(**distDict)
        distDict['nodeType'] = 'multiplyDivide'
        factor = naming.setName(**distDict)
        distDict['nodeType'] = 'clamp'
        clamp = naming.setName(**distDict)
        ##################################
        endDict = naming.getName(endPoint)
        endDict['nodeType'] = 'locator'
        eloc = naming.setName(**endDict)
        if not cmds.objExists(dist):
            dist = cmds.createNode("distanceBetween", n=dist)
        if not cmds.objExists(sloc):
            sloc = cmds.createNode("locator", p=startPoint, n=sloc)
        if not cmds.objExists(eloc):
            eloc = cmds.createNode("locator", p=endPoint, n=eloc)
        if not cmds.objExists(factor):
            factor = cmds.createNode("multiplyDivide", n=factor)
        if not cmds.objExists(clamp):
            clamp = cmds.createNode("clamp", n=clamp)
        ##################################################
        cmds.connectAttr(sloc + '.wp[0]', dist + '.point1')
        cmds.connectAttr(eloc + '.wp[0]', dist + '.point2')
        cmds.connectAttr(dist + '.distance', factor + '.i1x')
        cmds.connectAttr(factor + '.outputX', clamp + '.inputR')
        ##############################################################
        cmds.setAttr(factor + '.i2x', cmds.getAttr(dist + '.distance'))
        cmds.setAttr(factor + '.operation', 2)
        cmds.setAttr(clamp + '.mxr', 999)
        cmds.setAttr(clamp + '.mnr', 1)
        ax = vectors.queryVector(chain[0], chain[1], True)
        for jnt in chain:
            cmds.connectAttr(clamp + '.outputR', '{}.s{}'.format(jnt, ax))
        return dist, factor, clamp

class StretchCrvLen(BaseWidget):
    __uiPath__ = r'AutoRig\ui\StretchCrvLenWidget.ui'

    def __init__(self, uiParent=None):
        super(StretchCrvLen, self).__init__(uiParent)
        # clicked connections
        self.ui.chainQButton.clicked.connect(self.__chainQLineUpdate__)
        self.ui.curveQButton.clicked.connect(self.__curveQLineUpdate__)
        # ui init behaviour
        self.__chainQLineUpdate__()
        self.__curveQLineUpdate__()

    def __chainQLineUpdate__(self):
        sel = cmds.ls(sl=True)
        jntLs = []
        for elem in sel:
            if cmds.nodeType(elem) == 'joint':
                jntLs.append(elem)
        if not jntLs:
            return
        self.ui.chainQLine.setText(", ".join(jntLs))
    
    def __curveQLineUpdate__(self):
        sel = cmds.ls(sl=True)
        if not sel:
            return
        for elem in sel:
            shp = cmds.listRelatives(elem, s=True)
            if shp and cmds.nodeType(shp[0]) == "nurbsCurve":
                self.ui.curveQLine.setText(elem)

    def _getWidgetData_(self):
        self.uiWdgDict['chain'] = self.ui.chainQLine.text().replace(" ","").split(",")
        self.uiWdgDict['curve'] = self.ui.curveQLine.text()
        self.uiWdgDict['autoSquash'] = self.ui.autoSquashQCheck.isChecked()
    
    @classmethod
    def __do__(self, chain, curve, autoSquash=False):
        if self._checkData_(chain, 'chain', True) or self._checkData_(curve, 'curve', True):
            return
        dist = cmds.arclen(curve, ch=True)
        namingDict = naming.getName(chain[0])
        namingDict['nodeType'] = "multiplyDivide"
        namingDict['system'] += "Stretch"
        div = cmds.createNode("multiplyDivide", n=naming.setName(**namingDict))
        cmds.connectAttr(dist + '.arcLength', div + '.i1x')
        cmds.setAttr(div + '.i2x', cmds.getAttr(dist + '.arcLength'))
        at = vectors.queryVector(chain[0], chain[1], True)
        for jnt in chain:
            cmds.connectAttr(div + '.ox', "{}.s{}".format(jnt, at))
        if not autoSquash:
            return dist, div
        namingDict['nodeType'] = 'multiplyDivide'
        namingDict['system'] = namingDict['system'].replace("Stretch","AutoSquash")
        sqh = cmds.createNode('multiplyDivide', n=naming.setName(**namingDict))
        cmds.setAttr(sqh + '.i1x', 1)
        cmds.setAttr(sqh + '.operation', 2)
        cmds.connectAttr(div + '.ox', sqh + '.i2x')
        cnn = "".join("xyz".split(at))
        for jnt in chain:
            cmds.connectAttr(sqh + '.ox', '{}.s{}'.format(jnt, cnn[0]))
            cmds.connectAttr(sqh + '.ox', '{}.s{}'.format(jnt, cnn[1]))
        return dist, div, sqh

class IkSpline(BaseWidget):
    __uiPath__ = r'AutoRig\ui\IkSplineWidget.ui'

    def __init__(self, uiParent=None):
        super(IkSpline, self).__init__(uiParent)
        # clicked connections
        self.ui.chainQButton.clicked.connect(self.__chainQButtonAction__)
        self.ui.ikParentQButton.clicked.connect(self.__ikParentQButtonAction__)
        self.ui.curveQButton.clicked.connect(self.__curveQButtonAction__)
        self.ui.twistQButton.clicked.connect(self.__twistQButtonAction__)
        # ui init behaviour
        self.__chainQButtonAction__()
        self.__curveQButtonAction__()

    def __twistQButtonAction__(self):
        sel = cmds.ls(sl=True)
        self.ui.twistQLine.setText(", ".join(sel[:2]))

    def __chainQButtonAction__(self):
        sel = cmds.ls(sl=True)
        jntLs = []
        for elem in sel:
            if cmds.nodeType(elem) == 'joint':
                jntLs.append(elem)
        if not jntLs:
            return
        self.ui.chainQLine.setText(", ".join(jntLs))
    
    def __curveQButtonAction__(self):
        sel = cmds.ls(sl=True)
        if not sel:
            return
        for elem in sel:
            shp = cmds.listRelatives(elem, s=True)
            if shp and cmds.nodeType(shp[0]) == "nurbsCurve":
                self.ui.curveQLine.setText(elem)

    def __ikParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ikParentQLine.setText(cmds.ls(sl=True)[0])
    
    def __controlsQbuttonAction__(self):
        if cmds.ls(sl=True):
            self.ui.controlsQLine.setText(", ".join(cmds.ls(sl=True)))

    def _getWidgetData_(self):
        self.uiWdgDict['chain'] = self.ui.chainQLine.text().replace(" ","").split(",")
        self.uiWdgDict['ikParent'] = self.ui.ikParentQLine.text()
        self.uiWdgDict['curve'] = self.ui.curveQLine.text()
        self.uiWdgDict['endMember'] = self.ui.endFixerQCheck.isChecked()
        self.uiWdgDict['twist'] = self.ui.twistQLine.text().replace(" ","").split(",")

    @classmethod
    def __do__(self, chain, curve, twist=[], endMember=False, ikParent=None):
        if self._checkData_(chain, 'chain', True) or self._checkData_(curve, 'curve', True):
            return
        if endMember:
            endMemberDict = naming.getName(chain[-1])
            endMemberDict['system'] += "End"
            chain.append( cmds.createNode('joint', p=chain[-1], n=naming.setName(**endMemberDict)) )
            cmds.setAttr(chain[-1] + '.t', *[0.1 if t else 0 for t in cmds.getAttr(chain[-2] + '.t')[0]])
            cmds.setAttr(chain[-2] + '.t', *[t-0.1 for t in cmds.getAttr(chain[-2] + '.t')[0]])
        crvDict = naming.getName(chain[0])
        crvDict['nodeType'] = 'ikSpline'
        ikh = cmds.ikHandle(sj=chain[0], ee=chain[-1], solver='ikSplineSolver', ccv=False,
                            n=naming.setName(**crvDict), pcv=False, c=curve)[0]
        if ikParent:
            cmds.parent(ikh, curve, ikParent)
        if not twist:
            return ikh
        cmds.setAttr(ikh + '.dTwistControlEnable', True)
        cmds.setAttr(ikh + '.dWorldUpType', 3)
        cmds.connectAttr(twist[0] + '.wm[0]', ikh + '.dWorldUpMatrix')
        atDict = {0:[ [1,0,0], 0, [0,1,0] ],
                  1:[ [-1,0,0], 1, [0,-1,0] ],
                  2:[ [0,1,0], 3, [0,0,1] ],
                  3:[ [0,-1,0], 4, [0,0,-1] ],
                  4:[ [0,0,1], 6, [1,0,0] ],
                  5:[ [0,0,-1], 7, [-1,0,0] ]}
        aimv = vectors.queryVector(*chain[:2])
        for ind, data in atDict.items():
            if data[0] == aimv:
                cmds.setAttr(ikh + '.dForwardAxis', ind)
                cmds.setAttr(ikh + '.dWorldUpAxis', data[1])
                cmds.setAttr(ikh + '.dWorldUpVector', *data[2])
                cmds.setAttr(ikh + '.dWorldUpVectorEnd', *data[2])
        if len(twist) == 2:
            cmds.setAttr(ikh + '.dWorldUpType', 4)
            cmds.connectAttr(twist[-1] + '.wm[0]', ikh + '.dWorldUpMatrixEnd')
        return ikh

class Ik(BaseWidget):
    __uiPath__ = r'AutoRig\ui\IkWidget.ui'

    def __init__(self, uiParent=None):
        super(Ik, self).__init__(uiParent)
        # clicked connections
        self.ui.chainQButton.clicked.connect(self.__chainQButtonAction__)
        self.ui.ikParentQButton.clicked.connect(self.__ikParentQButtonAction__)
        self.ui.ikControlQButton.clicked.connect(self.__ikControlQButtonAction__)
        self.ui.poleControlQButton.clicked.connect(self.__poleControlQButtonAction__)
        # ui init behaviour
        self.__chainQButtonAction__()

    def __chainQButtonAction__(self):
        sel = cmds.ls(sl=True)
        jntLs = []
        for elem in sel:
            if cmds.nodeType(elem) == 'joint':
                jntLs.append(elem)
        if not jntLs:
            return
        self.ui.chainQLine.setText(", ".join(jntLs))

    def __ikParentQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ikParentQLine.setText(cmds.ls(sl=True)[0])
    
    def __ikControlQButtonAction__(self):
        if cmds.ls(sl=True):
            self.ui.ikControlQLine.setText(cmds.ls(sl=True)[0])
    
    def __poleControlQButtonAction__(self, qline):
        if cmds.ls(sl=True):
            self.ui.poleControlQLine.setText(cmds.ls(sl=True)[0])

    def _getWidgetData_(self):
        self.uiWdgDict['chain'] = self.ui.chainQLine.text().replace(" ","").split(",")
        self.uiWdgDict['ikSolver'] = {0:'ikRPsolver', 1:'ikSCsolver'}[self.ui.ikSolverQCombo.currentIndex()]
        self.uiWdgDict['ikParent'] = self.ui.ikParentQLine.text()
        self.uiWdgDict['ikControl'] = self.ui.ikControlQLine.text()
        self.uiWdgDict['poleControl'] = self.ui.poleControlQLine.text()
        self.uiWdgDict['origControl'] = self.ui.origControlQCheck.isChecked()

    @classmethod
    def __do__(self, chain, ikSolver='ikRPsolver', ikParent=None, ikControl=None, poleControl=None, origControl=True):
        ikhDict = naming.getName(chain[0])
        ikhDict['nodeType'] = ikSolver
        ikh = cmds.ikHandle(sj=chain[0], ee=chain[-1], solver=ikSolver,
                            n=naming.setName(**ikhDict))[0]
        if poleControl:
            cmds.poleVectorConstraint(poleControl, ikh)
        if ikControl:
            cmds.pointConstraint(ikControl, ikh)
        if origControl:
            cmds.pointConstraint(origControl, chain[0])
        if ikParent:
            cmds.parent(ikh, ikParent)
        return ikh

class CreateCrv(BaseWidget):
    __uiPath__ = r'AutoRig\ui\CreateCrvWidget.ui'

    def __init__(self, uiParent=None):
        super(CreateCrv, self).__init__(uiParent)
        # clicked connections
        self.ui.referencesQButton.clicked.connect(self.__referencesQButtonAction__)
        # ui init behaviour
        self.__referencesQButtonAction__()
    
    def __referencesQButtonAction__(self):
        self.ui.referencesQLine.setText(", ".join(cmds.ls(sl=True)))

    def _getWidgetData_(self):
        self.uiWdgDict['systemName'] = self.ui.systemNameQLine.text()
        self.uiWdgDict['references'] = self.ui.referencesQLine.text().replace(" ","").split(",")
        self.uiWdgDict['degree'] = self.ui.degreeQSpin.value()
        self.uiWdgDict['connect'] = self.ui.connectQCheck.isChecked()
        
    @classmethod
    def __do__(self, references, degree=1, connect=True, systemName='Curve'):
        if self._checkData_(references, 'references', True):
            return
        if len(references) < 2:
            cmds.warning('Flag "references" need at least two inputs')
            return
        if len(references) > degree:
            crvPnts = [cmds.xform(ref, ws=True, t=True, q=True) for ref in references]
        else:
            crvPnts = vectors.queryPointsInVector(references[0], references[-1], degree - 1)
        crvName = naming.setName(systemName,'curve')
        crv = cmds.curve(d=degree, p=crvPnts, n=crvName)
        if not connect:
            return crv
        result = [crv]
        for ind,pnt in enumerate(crvPnts):
            locName = naming.setName(systemName,'locator')
            loc = cmds.spaceLocator(n=locName)[0]
            cmds.xform(ws=True, t=pnt)
            cmds.connectAttr(loc + '.wp[0]', '{}.cp[{}]'.format(crv, ind))
            result.append(loc)
        return result

__mainUI_relation__ = {'chain':Chain,
                       'chainCrvBased':ChainCrvBased,
                       'control':Control,
                       'controlTag':ControlTag,
                       'createCrv':CreateCrv,
                       'hierarchyRig':HierarchyRig,
                       'ik':Ik,
                       'ikSpline':IkSpline,
                       'joint':Joint,
                       'optimizedConstraint':OptimizedConstraint,
                       'reversedFk':ReversedFK,
                       'sets':Sets,
                       'snappingFootRoll':FootRollSnapping,
                       'snappingLimb':LimbSnapping,
                       'snappingSpine':SpineSnapping,
                       'spaceSwitch':SpaceSwitch,
                       'stretchLocDist':StretchLocDist,
                       'stretchCrvLen':StretchCrvLen,
                       'template':Template,
                       }