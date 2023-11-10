import pymel.core as pm
# ############################################# Utils #############################################
def GetConstraintWeightAttrib(cns, index):
    return cns.target[index].targetWeight.inputs(p=True)[0]

# ############################################# Custom 'Constraints' #############################################
def CreateBlendMatrixOri(nodeA, nodeB, targetNode, weight=1.0):
    nodeA = pm.PyNode(nodeA)
    nodeB = pm.PyNode(nodeB)
    targetNode = pm.PyNode(targetNode)

    # Create Blend Matrix
    blendMat = pm.createNode("blendMatrix")
    nodeA.worldMatrix[0].connect(blendMat.inputMatrix)
    nodeB.worldMatrix[0].connect(blendMat.target[0].targetMatrix)
    blendMat.target[0].useScale.set(False)
    blendMat.target[0].useTranslate.set(0)
    blendMat.target[0].useShear.set(False)
    blendMat.target[0].weight.set(weight)

    # Create Decompose Matrix
    decoMat = pm.createNode("decomposeMatrix")
    blendMat.outputMatrix.connect(decoMat.inputMatrix)
    decoMat.outputRotate.connect(targetNode.rotate)