import maya.cmds as cmds

def FootRollSnapping():
    # check selection
    rawInput = cmds.ls(sl=True)
    if not rawInput:
        raise ValueError("Invalid fk or ik member selection")
    connections = cmds.listConnections(rawInput[0] + ".message") or []
    metadata = None
    for cnn in connections:
        if "MetadataFootRollSnapping" in cnn:
            metadata = cnn
            break
    if not metadata:
        raise ValueError("Item selected is not member of FootRoll system")
    def __resetFootRollCtrLs__():
        for ctr in footRollCtr:
            attrLs = cmds.listAttr(ctr, k=True) + (cmds.listAttr(ctr, cb=True) or [])
            for attr in attrLs:
                attrDefVal = cmds.attributeQuery(attr, node=ctr, ld=True)[0]
                cmds.setAttr("{}.{}".format(ctr, attr), attrDefVal)
    footIkCtr = cmds.listConnections(metadata + ".footIkControl")[0]
    ballCtr = cmds.listConnections(metadata + ".ballControl")[0]
    footIkSnapper = cmds.listConnections(metadata + ".footIkSnapper")[0]
    ballSnapper = cmds.listConnections(metadata + ".ballSnapper")[0]
    footRollCtr = [ctr for ctr in cmds.listConnections(metadata + ".footRollControls")]
    # get info
    footIkMatrix = cmds.xform(footIkSnapper, m=True, ws=True, q=True)
    ballMatrix = cmds.xform(ballSnapper, m=True, ws=True, q=True)
    # reset controls
    __resetFootRollCtrLs__()
    # set only foot and toe info
    cmds.xform(footIkCtr, m=footIkMatrix, ws=True)
    cmds.xform(ballCtr, m=ballMatrix, ws=True)