import maya.cmds as cmds

import Utils.Maya.Attributes as MayaAttributesUtils

from Utils.Maya.UndoContext import UndoContext

def convertNode(node, newType, transferHierarchy=True, transferAttributes=True, transferConnections=True):
    with UndoContext("Convert {}".format(newType)):
        oldSelection = cmds.ls(selection=True)
        
        newNode = cmds.createNode(newType)
        
        try:
            if transferHierarchy:
                children = cmds.listRelatives(node, children=True)
                parent = (cmds.listRelatives(node, parent=True) or [None])[0]
                
                if parent != None:
                    cmds.parent(newNode, parent, relative=True)
                cmds.parent(children, newNode, shape=True, relative=True)
                
            if transferAttributes:
                userAttributes = cmds.listAttr(node, userDefined=True) or []
                for attribute in userAttributes:
                    MayaAttributesUtils.copyNodeAttribute(node, newNode, attribute)
                    
            if transferAttributes or transferConnections:
                cmds.copyAttr(node, newNode, v=True, ic=transferConnections, oc=transferConnections)
            
        except Exception:
            cmds.delete(newNode)
            raise
                
        finally:
            cmds.select(oldSelection)
        
        cmds.delete(node)
        newNode = cmds.rename(newNode, node)
        
    return newNode

def convertToBasicTransform(transform, transferHierarchy=True, transferAttributes=True, transferConnections=True):
    return convertNode(transform, "transform", transferHierarchy=transferHierarchy, transferAttributes=transferAttributes, transferConnections=transferConnections)

def convertToAdditiveTransform(transform, transferHierarchy=True, transferAttributes=True, transferConnections=True):
    return convertNode(transform, "AdditiveTransform", transferHierarchy=transferHierarchy, transferAttributes=transferAttributes, transferConnections=transferConnections)
