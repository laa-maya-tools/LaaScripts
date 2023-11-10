import os
import sys
import json
import xml.etree.ElementTree as ET

import pymel.core   as pm
import maya.mel     as mel
import maya.cmds    as cmds

# ############################################################
# ######################## Bind TMs ##########################
# ############################################################
def ResetJointBindTMs(jointList):
    sknClusters = []
    sys.stdout.write('Reset/recache Bind Matrices for {} JOINT/S.'.format(len(jointList)))
    
    for jnt in jointList:
        # Get joint connections to any possible SkinCluster node
        matrixPlugs = cmds.listConnections(jnt + ".worldMatrix", type="skinCluster", p=True) or []
        for mp in matrixPlugs:
            # Save all SkinCluster nodes for the recaching instruction later
            sknClusters.append(mp.split('.')[0])
            
            # If bindPreMatrix has no input, then connect the worldInverseMatrix of the joint
            bindPreMatrixPlug = mp.replace('matrix', 'bindPreMatrix')
            if cmds.listConnections(bindPreMatrixPlug, s=True, d=False):
                continue
            
            wim = cmds.getAttr(jnt + ".worldInverseMatrix")
            cmds.setAttr(bindPreMatrixPlug,  *wim, type="matrix")
    
    # set(x) => Work only with non duplicates of x
    for sknClusterNode in set(sknClusters):
        cmds.skinCluster(sknClusterNode, edit=True, recacheBindMatrices=True)

def ResetMeshBindTMs(meshList):
    sknClusters = []
    sys.stdout.write('Reset/recache Bind Matrices for {} MESH/ES.'.format(len(meshList)))
    
    for msh in meshList:
        sknCluster = cmds.listConnections(msh + ".inMesh", type="skinCluster", s=True, d=False) or None
        if (sknCluster):
            sknClusters.append(sknCluster[0])
            
            plugs = cmds.listConnections(sknCluster[0] + ".matrix", p=True, c=True, s=True, d=False)
            plugsIterator = iter(plugs)
            for x in plugsIterator:
                con = x
                plg = next(plugsIterator)
                
                bindPreMatrixPlug = con.replace('matrix', 'bindPreMatrix')
                if cmds.listConnections(bindPreMatrixPlug, s=True, d=False):
                    continue
                
                jnt = plg.split('.')[0]
                wim = cmds.getAttr(jnt + ".worldInverseMatrix")
                cmds.setAttr(bindPreMatrixPlug,  *wim, type="matrix")
        
        for sknClusterNode in set(sknClusters):
            cmds.skinCluster(sknClusterNode, edit=True, recacheBindMatrices=True)

def ResetAllBindTMs():
    jointList = cmds.ls(type="joint")
    if (jointList):
        ResetJointBindTMs(jointList)

# ############################################################
# ######################## Skn Utils #########################
# ############################################################
def FindRelatedSkinCluster(mesh):
    history = pm.listHistory(mesh, interestLevel=1, pruneDagObjects=1)
    skn = [x for x in history if (type(x) == pm.nodetypes.SkinCluster)]
    if (skn):
        skn = skn[0]
        return skn
    return None

def GetSkinClusterBones(mesh):
    """
    Args:
        mesh (string): Name of the mesh to get affecting joints.

    Raises:
        Exception: No SkinCluster on the mesh node

    Returns:
        [Pynodes]: Joints affecting the SkkinCluster of the mesh
    """
    skn = FindRelatedSkinCluster(mesh)
    if (skn):
        return pm.skinCluster(mesh, q=True, influence=True)
    else:
        raise Exception("No Skin Cluster found for the mesh: {}".format(mesh))

def RemoveUnusedSkinInfluences(mesh):
    """Removes the unused skin influences of a mesh

    Args:
        mesh (string): Mesh node to work on
    """
    sknCluster = FindRelatedSkinCluster(mesh)
    allInfluences = pm.skinCluster(sknCluster, q=True, inf=True)
    weightedInfluences = pm.skinCluster(sknCluster, q=True, wi=True)
    unusedInfluences = [inf for inf in allInfluences if inf not in weightedInfluences]
    pm.skinCluster(sknCluster, e=True, removeInfluence=unusedInfluences)
    print("## {} unused influences removed".format(len(unusedInfluences)))

def SkinWrap(meshToSkin, skinnedMesh, maxInfluences=4, removeUnusedInfluences=False):
    """Creates a skinCluster on the 'skinnedMesh' and tries to copy the weights from the 'meshToSkin'

    Args:
        MeshToSkin (string): name of the mesh to copy wieghts from
        skinnedMesh (strin): name of the mesh that will receive the copied weights
        maxInfluences (int, optional): Max Inlfuences for the new skinCluster. Defaults to 4.
        removeUnusedInfluences (bool, optional): Remove the unused influences when the copy has been done. Defaults to False.

    Returns:
        PyNode: Newly created skinCluster node.
    """
    joints = GetSkinClusterBones(skinnedMesh)
    newSknCluster = pm.skinCluster(joints + [meshToSkin], maximumInfluences=maxInfluences, toSelectedBones=True)
    pm.copySkinWeights(sourceSkin=FindRelatedSkinCluster(skinnedMesh), destinationSkin=newSknCluster, noMirror=True, ia=["name","label"], sa="rayCast")
    print("## '{}' Skin Wrapped to '{}'".format(meshToSkin.getName(), skinnedMesh.getName()))
    if (removeUnusedInfluences):
        RemoveUnusedSkinInfluences(newSknCluster)
    
    return newSknCluster

# ############################################################
# ##################### Custom Import ########################
# ############################################################
def CreateAndImportXMLSkin(fullFilePath, mesh):
    """Creates a new skinCLuster and imports an XML file

    Args:
        fullFilePath (string): path of the XML to import
        mesh (string): name of the mesh that will get skin weights imported
    """
    tree = ET.parse(fullFilePath)
    root = tree.getroot()
    usedJoints = []
    for weightData in root.iter("weights"):
        usedJoints.append(weightData.attrib['source'])
    sknCluster = pm.skinCluster(usedJoints + [mesh], toSelectedBones=True)
    
    fileName = os.path.basename(fullFilePath)
    filePath = os.path.dirname(fullFilePath)
    
    pm.deformerWeights(fileName, df=sknCluster, im=True, method="index", path=filePath)
    print("Weights for mesh '{}' loaded".format(mesh))

















# ############################
# ######## Bind Poses ########
# ############################
ALT_SKIN_CLUSTER_SAVED = {}

def RebuildHierarchyDagPose(rootNode):
    dagPoses = []
    connectedSkinClusters = []
    
    jointList = cmds.listRelatives(rootNode, pa=True, ad=True, type="joint")
    if (cmds.objectType(rootNode) == "joint"):
        jointList += [rootNode]
    
    for jnt in jointList:
        dagConnections = cmds.listConnections(jnt, type="dagPose") or []
        for conn in dagConnections:
            if conn not in dagPoses:
                dagPoses.append(conn)
                
    for pose in dagPoses:
        skinClusters = cmds.listConnections(pose, type="skinCluster") or []
        for skn in skinClusters:
            if skn not in connectedSkinClusters:
                connectedSkinClusters.append(skn)
    
    cmds.delete(dagPoses)
    cmds.select(jointList, r=True)
    newPose = cmds.dagPose(sl=True, s=True, bp=True)
    cmds.select(None)
    for skn in connectedSkinClusters:
        sknPyNode = pm.PyNode(skn)
        connections = sknPyNode.outputGeometry[0].connections()
        geoNode = None
        if (connections):
            geoNode = connections[0]
            pm.select(geoNode, add=True)
        print("Connecting bindPose '{}' to skinCluster '{}' on '{}'".format(newPose, skn, geoNode))
        cmds.connectAttr("{}.message".format(newPose), "{}.bindPose".format(skn))

def GetSkinBones(meshList):
    result = []
    for msh in meshList:
        sknCluster = cmds.listConnections(msh + ".inMesh", type="skinCluster", s=True, d=False) or None
        if (sknCluster):
            joints = cmds.listConnections(sknCluster[0] + ".matrix", s=True, d=False)
            
            result.append(joints)
            
    return result

def SaveSkin():
    for node in cmds.ls(sl=True):
        ALT_SKIN_CLUSTER_SAVED[node] = GetSkinDict(node)

def GetSkinDict(node):
    skinCls = mel.eval('findRelatedSkinCluster ' + node)
    if not skinCls:
        cmds.warning("Node '{}' has no SkinCluster related.".format(node))
        return
    #cmds.skinPercent(skinCls, normalize=True)
    typeDict = {'nurbsCurve':'cv',
                'mesh':'vtx',
                'lattice':'pt'}
    cmds.skinCluster(skinCls, e=True, forceNormalizeWeights=True)
    outputType = cmds.listConnections(skinCls + ".outputGeometry", p=True)[0].split(".")[0]
    outputType = cmds.nodeType(outputType)
    infDict = {}
    for ind in cmds.getAttr(skinCls + ".matrix", mi=True):
        infDict[ind] = cmds.listConnections("{}.matrix[{}]".format(skinCls, ind))[0]
    skinDict = {}
    for ind in cmds.getAttr(skinCls + '.weightList', mi=True):
        dKey = "{}.{}[{}]".format(node, typeDict[outputType], ind)
        skinDict[dKey] = []
        indLs = cmds.getAttr('{}.weightList[{}].weights'.format(skinCls, ind), mi=True)
        valLs = cmds.getAttr('{}.weightList[{}].weights'.format(skinCls, ind))[0]
        for inf,val in zip(indLs, valLs):
            if val >= 0.001: skinDict[dKey].append( [infDict[inf], val] )
    sys.stdout.write("// Result: '{}' SkinCluster related saved.\n".format(node))
    return {'influences':list(infDict.values()), 'skinCls':skinCls, 'weights':skinDict}

def ExportSkin():
    sel = cmds.ls(sl=True)
    if not sel:
        return
    if not [mel.eval('findRelatedSkinCluster ' + node) for node in sel]:
        return
    path = cmds.fileDialog2(ds=1, cap='Export Path', fm=3)
    if not path:
        return
    for node in sel:
        skinCls = mel.eval('findRelatedSkinCluster ' + node)
        if skinCls:
            cmds.skinCluster(skinCls, e=True, forceNormalizeWeights=True)
            #with open("{}/{}.json".format(path[0], ))
            cmds.deformerWeights("{}.json".format(node.split(":")[-1]), path=path[0], export=True, deformer=skinCls, format="JSON", wp=8)
        else:
            sys.stdout.write("Node '{}' has no SkinCluster related.\n".format(node))

def ImportSkin(skinClsSufix="SkinCls"):
    pathLs = cmds.fileDialog2(ds=1, cap='Import Path', fm=4, ff='*.json')
    if not pathLs:
        return
    couldNot = []
    typeDict = {'nurbsCurve':'cv',
                'mesh':'vtx',
                'lattice':'pt'}
    for path in pathLs:
        pathTokens = path.rpartition("/")
        with open(path, 'r') as f:
            skinDict = json.load(f)
        mesh = skinDict['deformerWeight']['shapes'][0]['name']
        if not cmds.objExists(mesh):
            couldNot.append("Mesh '{}' not founded in scene".format(mesh))
            continue
        skinCls = mel.eval("findRelatedSkinCluster " + mesh)
        skinInfluences = None
        fileInfluences = []
        doNotExists = []
        for influence in skinDict['deformerWeight']['weights']:
            if cmds.objExists(influence['source']):
                fileInfluences.append(influence['source'])
            else:
                doNotExists.append(influence['source'])
        if doNotExists:
            couldNot.append("Influences '{}' for mesh '{}' not founded in scene".format(doNotExists, pathTokens[2].split(".")[0]))
            continue
        # check skin creation or just import
        if not skinCls:
            skinCls = cmds.skinCluster(fileInfluences, mesh, bindMethod=1, n="{}_{}".format(pathTokens[2].split(".")[0], skinClsSufix), toSelectedBones=True, forceNormalizeWeights=True)[0]
            skinInfluences = fileInfluences
        else:
            skinInfluences = cmds.skinCluster(skinCls, inf=True, q=True)
        # search for errors
        if skinInfluences != fileInfluences:
            outInfluences = [inf for inf in fileInfluences if inf not in skinInfluences]
            if outInfluences:
                raise ValueError("File influences not registered in skin influences. {}".format(outInfluences))
            outInfluences = [inf for inf in skinInfluences if inf not in fileInfluences]
            raise ValueError("Skin influences not registered in file influences. {}".format(outInfluences))
        #->
        componentLs = {}
        weightLs = []
        for weight in skinDict['deformerWeight']['weights']:
            inf = weight['source']
            for point in weight['points']:
                pointName = "{}.{}[{}]".format(mesh, typeDict[cmds.nodeType(mesh)], point['index'])
                if pointName in componentLs.keys():
                    componentLs[pointName].append( (inf, point['value']) )
                else:
                    componentLs[pointName] = [(inf, point['value'])]
        for comp, weight in componentLs.items():
            cmds.skinPercent(skinCls, comp, transformValue=weight)
        #cmds.deformerWeights(pathTokens[2], im=True, path=pathTokens[0], deformer=skinCls)
        #cmds.skinCluster(skinCls, e=True, forceNormalizeWeights=True)
        sys.stdout.write("// Result: Skin Cluster file '{}' imported into '{}'\n".format(path, pathTokens[2].split(".")[0]))
    if couldNot:
        [cmds.warning(msg) for msg in couldNot]

def SaveAndUnbindSkin():
    cmds.waitCursor(st=True)
    for node in cmds.ls(sl=True):
        if node not in ALT_SKIN_CLUSTER_SAVED.keys():
            ALT_SKIN_CLUSTER_SAVED[node] = GetSkinDict(node)
            cmds.skinCluster(node, ub=True, e=True)
        #sys.stdout.write("// Result: '{}' SkinCluster saved and unbind.\n".format(node))
    cmds.waitCursor(st=False)

def BindSavedSkin():
    cmds.waitCursor(st=True)
    sel = cmds.ls(sl=True)
    for node in cmds.ls(sl=True):
        if node not in ALT_SKIN_CLUSTER_SAVED.keys():
            cmds.warning("Node '{}' has no SkinCluster saved.".format(node))
            continue
        skinCls = cmds.skinCluster(ALT_SKIN_CLUSTER_SAVED[node]['influences'], node, n=ALT_SKIN_CLUSTER_SAVED[node]['skinCls'])[0]
        for vtx,val in ALT_SKIN_CLUSTER_SAVED[node]['weights'].items():
            cmds.skinPercent( skinCls, vtx, transformValue=val)
        sys.stdout.write("// Result: '{}' saved SkinCluster binded.\n".format(node))
    cmds.select(sel)
    cmds.waitCursor(st=False)