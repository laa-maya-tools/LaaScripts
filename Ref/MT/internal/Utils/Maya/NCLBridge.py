import maya.mel as mel

def setNoCompress(nodeName, value):
    mel.eval('nnSetNoCompressNode_Set_NoCompress("{}", {})'.format(nodeName, value))

def getNoCompress(nodeName):
    return mel.eval('nnSetNoCompressNode_Get_NoCompress "{}"'.format(nodeName))