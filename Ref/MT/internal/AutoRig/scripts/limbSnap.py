import maya.cmds as cmds

def LimbSnapping():
    # check selection
    rawInput = cmds.ls(sl=True)
    if not rawInput:
        raise ValueError("Invalid fk or ik limb member selection")
    connections = cmds.listConnections(rawInput[0] + ".message") or []
    metadata = None
    for cnn in connections:
        if "MetadataLimbSnapping" in cnn:
            metadata = cnn
            break
    if not metadata:
        raise ValueError("Item selected is not member of Limb system")
    switchCtr = cmds.listConnections(metadata + ".switchControl")[0]
    ikCtr = cmds.listConnections(metadata + ".ikControl")[0]
    ikSnapper = cmds.listConnections(metadata + ".ikSnapper")[0]
    poleVCtr = cmds.listConnections(metadata + ".poleVControl")[0]
    poleVSnapper = cmds.listConnections(metadata + ".poleVSnapper")[0]
    poleVMultiplier = cmds.getAttr(metadata + ".poleVMultiplier")
    fkCtr = [ctr for ctr in cmds.listConnections(metadata + ".fkControls")]
    fkSnappers = [snapper for snapper in cmds.listConnections(metadata + ".fkSnappers")]
    # get info
    ikMatrix = cmds.xform(ikSnapper, m=True, ws=True, q=True)
    fkMatrix = [cmds.xform(snapper, m=True, ws=True, q=True) for snapper in fkSnappers]
    # set info
    state = cmds.getAttr(switchCtr + ".fkIk")
    if state >= 0.5:
        [cmds.xform(ctr, ws=True, m=fkMatrix[ind]) for ind,ctr in enumerate(fkCtr)]
        cmds.setAttr(switchCtr + ".fkIk", 0)
        cmds.select(fkCtr[0])
    else:
        cmds.xform(ikCtr, ws=True, m=ikMatrix)
        cmds.setAttr(poleVCtr + ".rx", cmds.getAttr(poleVSnapper + ".rx") * (1 if poleVMultiplier >= 0 else -1))
        cmds.setAttr(switchCtr + ".fkIk", 1)
        cmds.select(ikCtr)