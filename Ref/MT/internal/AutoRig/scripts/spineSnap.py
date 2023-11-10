import maya.cmds as cmds

def SpineSnapping():
    # check selection
    rawInput = cmds.ls(sl=True)
    if not rawInput:
        raise ValueError("Invalid fk or ik limb member selection")
    connections = cmds.listConnections(rawInput[0] + ".message") or []
    metadata = None
    for cnn in connections:
        if "MetadataSpineSnapping" in cnn:
            metadata = cnn
            break
    if not metadata:
        raise ValueError("Item selected is not member of Limb system")
    switchCtr = cmds.listConnections(metadata + ".switchControl")[0]
    fkCtr = [ctr for ctr in cmds.listConnections(metadata + ".fkControls")]
    fkSnappers = [snapper for snapper in cmds.listConnections(metadata + ".fkSnappers")]
    ikCtr = [ctr for ctr in cmds.listConnections(metadata + ".ikControls")]
    ikSnappers = [snapper for snapper in cmds.listConnections(metadata + ".ikSnappers")]
    # get info
    fkMatrix = [cmds.xform(snapper, m=True, ws=True, q=True) for snapper in fkSnappers]
    ikMatrix = [cmds.xform(snapper, m=True, ws=True, q=True) for snapper in ikSnappers]
    # set info
    state = cmds.getAttr(switchCtr + ".fkIk")
    if state >= 0.5:
        [cmds.xform(ctr, ws=True, m=fkMatrix[ind]) for ind,ctr in enumerate(fkCtr)]
        cmds.setAttr(switchCtr + ".fkIk", 0)
        cmds.select(fkCtr[0])
    else:
        for ind,matrix in enumerate(ikMatrix):
            ctr = ikCtr[ind]
            cmds.xform(ctr, ws=True, m=matrix)
        cmds.setAttr(switchCtr + ".fkIk", 1)
        cmds.select(ikCtr)