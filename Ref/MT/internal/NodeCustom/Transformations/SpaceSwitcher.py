# -*- coding: utf-8 -*-

import maya.cmds as cmds

import NodeManager.NodeWrapper as NodeWrapper
import NodeMayaWrapper.ChoiceWrapper as CW

from Utils.Maya.UndoContext import UndoContext

# TODO esta librería podría estar en utils
import DynamicSpaceSwitcher.mayalib.animLib as animLib 

# debug mode
# region

#import importlib
#importlib.reload(NodeWrapper)
#importlib.reload(CW)
#importlib.reload(animLib)

# endregion

class SpaceSwitcher(NodeWrapper.NodeWrapper): 
    _Type                  = "spaceSwitcher"

    _targetMatrix          = "targetMatrix"
    _targetIndex           = "targetIndex"
    _offsetMatrix          = "offsetMatrix"
    _worldInverseParent    = "worldInverseParent"
    _auxInputParent        = "auxInputParent"
    _outputMatrix          = "outputMatrix"

    _unitaryMatrixNode     = "unitaryMatrix"
    _spaceSwitcherGrp      = "spaceSwitcher_grp"

    def __init__(self, node=None):
        super().__init__(node)
        #super(SpaceSwitcher, self).__init__(node)

    # Gestion de targets
    # region:

    # targetsWrapper
    # devuelve el wrapper del nodo choice que contiene las matrices de los distintos targets
    # no comprueba si el spaceSwitcher tiene un nodo choice porque se conecta al crearse el propio nodo spaceSwitcher
    @property
    def targetsWrapper(self):
        # devuelve el wrapper del nodo asociado al attributo targetMatrix (ChoiceWrapper)
        theWrapper = self.getCollectionAttribute(self._targetMatrix, CW.ChoiceWrapper, newNodeAttr = "output")
        if len(theWrapper)==0:
            #creacion de la matriz unitaria para el item 0
            theUnitaryMatrixNode = self.unitaryMatrixNode
            # No tengo claro si para la matriz de mundo usaré un nodo transform o composeMatrix
            if cmds.nodeType(theUnitaryMatrixNode)=="composeMatrix":
                theWrapper.setInputNode("input[0]", theUnitaryMatrixNode, inputAttribute="outputMatrix")
            else:
                theWrapper[0] = (theUnitaryMatrixNode) 

            self.selector = theWrapper.node    
        return theWrapper


    # targetNodes:
    # TODO tengo dudas de como debería operar con los nodos:
    # opcion 1: con la propiedad targetNodes de spaceWrapper.
    # opcion 2: desde el wrapper del choice que devuelve la propidad targetsWrapper del spaceSwitcher

    #devuelve una lista de los nodos conectados en el choice
    @property
    def targetNodes(self):
        # devuelve la lista de los nodos targets
        theWrapper = self.targetsWrapper
        return list(theWrapper)
    
    # Quizas sea mejor trabajarlo a través del wrapper        
    @targetNodes.setter
    def targetNodes(self, nodes):
        # conecta la lista que de nodos que le demos de la forma correcta. 
        # no añade nodos a la lista, configura todas las conexiones con la lista nueva
        with UndoContext("Set spaces: {}".format(nodes)):
            targetsWrapper = self.targetsWrapper
            targetsWrapper.clear()
            targetsWrapper += nodes

    @property
    def unitaryMatrixNode(self):
        # obtenemos un nodo que usaremos para todos los spaces switcher, que definirá la matriz inicial de todos los spaces (worldMatrix)   
        # si no existe en la escena, lo crea.
        # dudo si usar un nodo compose o un transform.
        theNode = self._unitaryMatrixNode
        if not (cmds.objExists(self._unitaryMatrixNode)):
            with UndoContext("SpaceSwitcher: create unitaryMatrixNode"):
                theNode = cmds.createNode("composeMatrix",name=self._unitaryMatrixNode)
        return theNode

        # ___________________________________________ VALUES

    #@property # Antes era una propiedad, pero lo cambie a método para poder usar el argumento index
    # devuelve la matriz del nodo target activado en el choice
    # TODO tengo dudas de si acceder a este attributo desde el wrapper del propio choice o desde esta función.
    def getTargetMatrix(self, index=None): 
        # de momento usaré cmds filtrando los casos específicos.
        
        if index==None:
            index = self.targetIndex

        targetsWrapper = self.targetsWrapper

        # ------------------------- Método 1:
        # obtencion de la matriz con el nodo conectado al choice
        theList = targetsWrapper.getInputFromListAttribute(targetsWrapper._list, plugs=True)
        result = cmds.getAttr(theList[index]) 
        # ------------------------- Método 2:
        # obtención de la matriz con el propio nodo choice
        targetsPlug = targetsWrapper.getPlug(targetsWrapper._list)
        
        indexList = cmds.getAttr(targetsPlug, multiIndices=True)
        thePlug = "{}[{}]".format(targetsPlug, indexList[index])

        attrList = cmds.listAttr(targetsPlug, multi=True)
        thePlug = "{}.{}".format(targetsWrapper.node, attrList[index])
        
        # 2_1: obtener la matriz con cmds
        cmdsFloatMatrix = cmds.getAttr(thePlug)
        
        ## 2_2: obtención de la matriz con OpenMaya
        #omMatrix = utilsOM.asMPlug(thePlug).asMDataHandle().asMatrix()
        #omFloatMatrix = [omMatrix[i] for i in range(16)]

        result = cmdsFloatMatrix
        # ------------------------- 
        return result

    @property
    def targetIndexValue (self):
        # devuelve 
        return self.getAttr(self._targetIndex )
    
    # TODO estudiar la posibilidad de que este valor este en otro nodo y la propidad cambiara el valor del atributo conectado
    @targetIndexValue.setter
    def targetIndex (self, value):
        with UndoContext("Set value in targetIndex attribute of SpaceSwitcher Node"):  
            offsetWrapper = self.offsetWrapper 
            offsetWrapper.setNumericAttribute(self._targetIndex , value)  
    
    @property
    def selectorAttribute (self):
        return self.getAttr(self._targetIndex )
    
    @property
    def selector (self):
        cWrapper =  self.targetsWrapper
        # TODO no estoy seguro de que devuelve getInputSingle cuando el nodo esta vacío
        #if self.isInputConnected(cWrapper._selector):
        #    pass
        return cWrapper.getInputSingle(cWrapper._selector, cls = NodeWrapper.NodeWrapper, plugs=False)

    @selector.setter
    def selector (self, node):
        #from NodeManager.MayaWrapper.ChoiceWrapper import ChoiceWrapper
        with UndoContext("Set value in targetIndex attribute of SpaceSwitcher Node"):    
            cWrapper =  self.targetsWrapper
            cWrapper.setInputWrapper(cWrapper._selector, self, inputAttribute=self._targetIndex)

    # endregion

    # Gestion del offset
    # region

    # devuelve un wrapper del nodo que se usara como offset de transformacion en los switcher
    # si no existe lo crea.
    @property
    def offsetWrapper(self):
        # devuelve el node que vamos a usar como offset
        # si no existe lo crea
        #print("outputNode: ", self.outputNode)
        self.createOffsetNode(self.outputNode)
        return self.getInputSingle(self._offsetMatrix, cls = NodeWrapper.NodeWrapper, plugs=False)

    def createOffsetNode(self, theNode):
        # nodo para agrupar todos los offset de los distintos spaces Switcher y dejar así el outliner más ordenado
        # si no existe en la escena, lo crea.

        if not (cmds.objExists(self. _spaceSwitcherGrp)):
            cmds.createNode( "transform", name=self. _spaceSwitcherGrp)

        if  not self.isInputConnected(self._offsetMatrix):    
            with UndoContext("SpaceSwitcher: Create OffsetNode"):
                offsetNode = cmds.createNode( "transform", n= (theNode+"_SpaceOffset"), parent = self. _spaceSwitcherGrp)
                nWrapper = NodeWrapper.NodeWrapper(offsetNode)

                #TODO attributeType podría ser short
                cmds.addAttr(offsetNode, longName="targetIndex", attributeType="byte", keyable=True, storable=True, readable=True)
                self.setInputNode("targetIndex", offsetNode, inputAttribute="targetIndex")

                #nWrapper.setInputWrapper("offsetParentMatrix", self, inputAttribute=self._outputMatrix)
                self.setInputWrapper(self._offsetMatrix, nWrapper, inputAttribute= "worldMatrix[0]")                

                #theParent =  cmds.listRelatives(self.ouputNode, parent=True)[0] 
                #self.worldInverseParent    =  cmds.listRelatives(self.node, parent=True)[0]      

                return nWrapper
            
    #devuelve el valor de la matriz del nodo offset de transformacion
    @property
    def offsetMatrix (self):
        return self.getAttr(self._offsetMatrix)
    
    ## TODO esta propiedad podría servir para cambiar la posición del offset de transformación
    #@offsetMatrix.setter
    #def offsetMatrix (self, theNode):
    #    print("SpaceSwitcher: setter offsetMatrix")

    # endregion

    # Gestion del nodo al que se le hace el spaceSwitcher
    # region

    @property
    def outputWrapper(self):
        if self.isInputConnected(self._outputMatrix):
            theNode = self.getOutputSingle(self._outputMatrix, cls = None, plugs=False)[0]
            return NodeWrapper.NodeWrapper(theNode)         

    # devuelve el nodo al que se le ha hecho el spaceSwitcher
    @property
    def outputNode(self):
        # devuelve el nodo al que vamos a conectar los spaces switchers
        #return self.outputWrapper.node
        if self.isOutputConnected(self._outputMatrix):
            return self.getOutputSingle(self._outputMatrix, cls = None, plugs=False)[0]  
         
    
    # asignamos el nodo al que corresponde este spaceSwitcher
    # TODO (Estudiar esta posibilidad):
    # falta tener en cuenta que el nodo pueda tener conectado al en el offsetParentMatrix, 
    # el nodo tiene un attributo para guardar esa conexion para restablecerla si se borra el spaceSwitcher.
    @outputNode.setter
    def outputNode (self, node):    
        with UndoContext("SpaceSwitcher node connected in " + node ):    
            # podemos añadir como propiedad desde el wrapper del switcher, el nodo al que le vamos a asignar los spaces.
            theNodeWrapper = NodeWrapper.NodeWrapper(node)
            theNodeWrapper.setInputWrapper("offsetParentMatrix", self, inputAttribute="outputMatrix")

    # el atributo worldInverseParent va conectado al padre del nodo al que le hacemos el spaceSwitcher para no tener redundacias cíclicas
    @property
    def worldInverseParentAttribute(self):
        return self.getAttr(self._worldInverseParent)

    @property
    def worldInverseParent(self):
        if self.isInputConnected(self._worldInverseParent):
            return self.getInputSingle(self._worldInverseParent, cls = NodeWrapper.NodeWrapper, plugs=False)

    @worldInverseParent.setter
    def worldInverseParent(self, node):
        with UndoContext("Connnect worldInverseParent attribute of SpaceSwitcher Node"):    
            theParent =  cmds.listRelatives(node, parent=True)
            if theParent:
                self.setInputNode(self._worldInverseParent, theParent[0], inputAttribute="worldInverseMatrix")
            
    # endregion

    # _____________________________________ GENERAL METHODS  
    # region

    def getCollectionName(self):
        return self._Type

    def delete(self):
        theOffsetParent = cmds.listRelatives(self.offsetWrapper.node, parent=True)
        cmds.delete(self.offsetWrapper.node)
        if not (cmds.listRelatives(theOffsetParent, children=True)):
            cmds.delete(theOffsetParent)
        self.targetsWrapper.delete()
        super().delete()

    def create(self, nodeName=None, outputNode=None, unique=False, skipSelect=True):
        super().create(nodeName=nodeName, unique=unique, skipSelect=skipSelect)
        
        self.outputNode = outputNode
        self.worldInverseParent = outputNode

        # como los nodos offset y target se generan al ser demandados si no existe, no hace falta crearlos. 
        # region
        # el nodo offset es creado si no existe
        #offsetWrapper = self.offsetWrapper        

        #  el nodo choice es creado si no existe
        # junto con el nodo de matriz unitaria
        # y la conexion del targetIndex del SpaceSwitcher al selector del choice
        #targetsWrapper = self.targetsWrapper
        # endregion
    # endregion

    # _____________________________________ ANIMATIONS METHODS
    # region

    def addKey(self):
        with UndoContext("SpaceSwitcher UI: Add Key Space"):  
            time = cmds.currentTime(query=True)  

            theOffsetNode = self.offsetWrapper.node
            animLib.SetKeyframe(theOffsetNode, "targetIndex", self.targetIndex, time, inTangent=animLib._tanStepnext, outTangent=animLib._tanStep) 
            value = cmds.getAttr("{}.translate".format(theOffsetNode))[0]
            animLib.SetPosKeyframe(theOffsetNode, value, time , inTangent=animLib._tanStepnext, outTangent=animLib._tanStep)
            value = cmds.getAttr("{}.rotate".format(theOffsetNode))[0]
            animLib.SetRotKeyframe(theOffsetNode, value, time , inTangent=animLib._tanStepnext, outTangent=animLib._tanStep)

    # endregion