import maya.cmds as cmds

def deleteCamera(camera, deleteTarget=True, deleteUp=True):
    if not cmds.objExists(camera):
        raise AssertionError("Unable to delete camera: The provided camera doesn't exist!")
    
    lookAtNode = getCameraLookAtNode(camera)
    if lookAtNode:
        up = getLookAtUpNode(lookAtNode)
        target = getLookAtTargetNode(lookAtNode)
        if up and deleteUp:
            cmds.delete(up)
        if target and deleteTarget:
            cmds.delete(target)
        
        if cmds.objExists(lookAtNode):
            cmds.delete(lookAtNode) # Deleting the target node might delete the lookAt node as well
            
    if cmds.objExists(camera):
        cmds.delete(camera) # Deleting the lookAt node might delete the camera node as well
        
def renameCamera(camera, newName, autoRenameDuplicated=False):
    if not cmds.objExists(camera):
        raise AssertionError("Unable to rename camera: The provided camera doesn't exist!")
    if cmds.objExists(newName) and not autoRenameDuplicated:
        raise ValueError("Unable to rename camera: The provided name is already in use!")
    
    newName = cmds.rename(camera, newName)  # This operation is performed first to get the new name in case it's already in use and Maya asigns it a different one
    
    lookAtNode = getCameraLookAtNode(newName)
    if lookAtNode:
        target = getLookAtTargetNode(lookAtNode)
        up = getLookAtUpNode(lookAtNode)
        if target:
            cmds.rename(target, "{}_aim".format(newName))
        if up and target != up:
            cmds.rename(up, "{}_up".format(newName))
                
        cmds.rename(lookAtNode, "{}_group".format(newName))
    
    return newName

def getCameraLookAtNode(camera):
    lookAtNode = cmds.listConnections("{}.translate".format(camera), type="lookAt", s=False, d=True)
    return lookAtNode[0] if lookAtNode else None
    
def getLookAtTargetNode(lookAtNode):
    targetNode = cmds.listConnections("{}.target[0].targetParentMatrix".format(lookAtNode), s=True, d=False)
    return targetNode[0] if targetNode else None
    
def getLookAtUpNode(lookAtNode):
    upNode = cmds.listConnections("{}.worldUpMatrix".format(lookAtNode), s=True, d=False)
    return upNode[0] if upNode else None
    
def getAxisFromRotateOrder(rotateOrder):
    if rotateOrder <= 2:
        return [(rotateOrder + i) % 3 for i in range(3)]
    else:
        return [(rotateOrder - 3 - i) % 3 for i in range(3)]

def getFrameRate(unit=None):
    if unit == None:
        unit = cmds.currentUnit(q=True, time=True)
        
    if unit == "game":
        return 15.0
    if unit == "film":
        return 24.0
    if unit == "pal":
        return 25.0
    if unit == "ntsc":
        return 30.0
    if unit == "show":
        return 48.0
    if unit == "palf":
        return 50.0
    if unit == "ntscf":
        return 60.0
