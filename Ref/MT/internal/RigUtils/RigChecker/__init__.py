import os
from math import pow,sqrt
import re

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel

import RigUtils.Skinning as skn
import RigUtils.Shapes as rigshapes
import StandaloneProcess

def CheckMgearJointVisibility(mgearRigNode):
    correctState = False
    messages = []
    atrtibuteExists = pm.attributeQuery("jnt_vis", node=mgearRigNode, exists=True)
    attributeValue = None
    if (atrtibuteExists):
        attributeValue = mgearRigNode.jnt_vis.get()
        if (attributeValue == 0):
            correctState = True
        else:
            messages.append("-Rig joints are visible")
    return correctState, messages

def FixMgearJointVisibility(mgearRigNode):
    success = False
    atrtibuteExists = pm.attributeQuery("jnt_vis", node=mgearRigNode, exists=True)
    attributeValue = None
    if (atrtibuteExists):
        attributeValue = mgearRigNode.jnt_vis.get()
        if (attributeValue == 0):
            success = True
        elif (attributeValue == 1):
            attributeValue = mgearRigNode.jnt_vis.set(0)
            success = True
    return success

def GetNode(nodeName):
    node = None
    try:
        node = pm.PyNode(nodeName)
    except pm.general.MayaNodeError:
        pass
    return node

def GetRigNode():
    return GetNode("rig")

def GetNodeIgnoreCase(nodeName):
    node = None
    nameLowercase = nodeName.lower()
    nameUpperase = nodeName.upper()
    nameLength = len(nodeName)
    regex = re.compile("[{}{}]{{{}}}".format(nameLowercase, nameUpperase, nameLength))
    allElements = cmds.ls()
    matchedElements = list()
    for element in allElements:
        matched = regex.match(element)
        if matched:
            matchedElements.append(element)
    if (len(matchedElements) > 0):
        node = pm.PyNode(matchedElements[0])
    return node

def GetSkeletonGroup():
    return GetNodeIgnoreCase("skeleton")

def GetRigControllersGrp():
    return GetNode("rig_controllers_grp")

def GetSceneMeshes():
    shapesList = pm.ls(type="mesh")
    transformList = pm.listRelatives(shapesList, parent=True)
    # Unique values
    transformList = list(set(transformList))
    return transformList

def GetSceneMeshShapes():
    shapesList = pm.ls(type="mesh")
    return shapesList

def GetSceneActors():
    actors = pm.ls(type="actor")
    return actors

def GetActorMeshes(actors):
    actorMeshes = []
    
    for actor in actors:
        # Check empty main subactor
        mainSubActorResult = pm.listConnections(actor.mainSubActor, type="subActor")
        if (len(mainSubActorResult) == 0):
            correctState = False
            break
        
        # Check empty anim subactor
        animSubActorResult = pm.listConnections(actor.animSubActor, type="subActor")
        if (len(animSubActorResult) == 0):
            correctState = False
            break
        
        # Loop subactors
        subActorList = pm.listConnections(actor.subActorList, type="subActor")
        for subActor in subActorList:
            geometrySets = pm.listConnections(subActor.geometrySet)
            for geometrySet in geometrySets:
                geoList = pm.listConnections(geometrySet.list)
                for geo in geoList:
                    if (not (geo in actorMeshes)):
                        actorMeshes.append(geo)
    
    return actorMeshes

def CheckGeometryGroups(meshes):
    correctState = True
    messages = []
    # Loop meshes and check if they are in an 'empty' group and if they are not in 'DC_Root'
    for mesh in meshes:
        meshParentResult = pm.listRelatives(mesh, parent=True)
        meshParent = None
        if (len(meshParentResult) == 0):
            # If it has no parent, break
            correctState = False
            messages.append("-" + mesh.getName() + ": should have a parent")
            break
        else:
            meshParent = meshParentResult[0]
        if (meshParent.getName().lower() == "dc_root"):
            # If parent is DC_Root, break
            correctState = False
            messages.append("-" + mesh.getName() + ": shouldn't be a child of DC_Root")
            break

        meshParentChildren = pm.listRelatives(meshParent, children=True)
        childrenAreMeshes = True
        for child in meshParentChildren:
            if (not (child.nodeType() == "transform")):
                childrenAreMeshes = False
                messages.append("-" + mesh.getName() + ": parent is not empty")
                break
            
            shapes = pm.listRelatives(child, s=True)
            if (len(shapes) == 0):
                continue
            
            isMesh = False
            for shape in shapes:
                if (shape.nodeType() == "mesh" or shape.nodeType() == "nurbsCurve" or shape.nodeType() == "bezierCurve"):
                    isMesh = True
                    break
            
            if (isMesh):
                continue
            else:
                childrenAreMeshes = False
                messages.append("-" + child.getName() + ": incorrect mesh children shapes")
                break
        
        if (not childrenAreMeshes):
            correctState = False
            break
    
    return correctState, messages

def CheckKeyedMeshes(meshes):
    correctState = True
    messages = []
    for mesh in meshes:
        keys = pm.keyframe(mesh, query=True)
        if (len(keys) > 0):
            correctState = False
            messages.append("-" + mesh.getName() + ": shouldn't have keys")
            break
    
    return correctState, messages

def IsAttrLocked(attr):
    return pm.getAttr(attr, lock=True)

def ResetTransforms(node):
    if (not IsAttrLocked(node.translateX)):
        node.translateX.set(0)
    if (not IsAttrLocked(node.translateY)):
        node.translateY.set(0)
    if (not IsAttrLocked(node.translateZ)):
        node.translateZ.set(0)
    if (not IsAttrLocked(node.rotateX)):
        node.rotateX.set(0)
    if (not IsAttrLocked(node.rotateY)):
        node.rotateY.set(0)
    if (not IsAttrLocked(node.rotateZ)):
        node.rotateZ.set(0)
    if (not IsAttrLocked(node.scaleX)):
        node.scaleX.set(1)
    if (not IsAttrLocked(node.scaleY)):
        node.scaleY.set(1)
    if (not IsAttrLocked(node.scaleZ)):
        node.scaleZ.set(1)

def FixKeyedMeshes(meshes):
    success = False
    
    for mesh in meshes:
        pm.cutKey(mesh, s=True)
        ResetTransforms(mesh)
        
    success = True
    return success

def GetDisplayLayer(node):
    displayLayer = None
    conns = pm.listConnections(node, type="displayLayer")
    if (len(conns) > 0):
        displayLayer = conns[0]
    
    currentNode = node
    if (displayLayer == None):
        parentFound = True
        while (parentFound and (displayLayer == None)):
            nodeParentResult = pm.listRelatives(currentNode, parent=True)
            nodeParent = None
            if (len(nodeParentResult) == 0):
                # If it has no parent, break
                parentFound = False
                break
            else:
                nodeParent = nodeParentResult[0]
                conns = pm.listConnections(nodeParent, type="displayLayer")
                currentNode = nodeParent
                if (len(conns) > 0):
                    displayLayer = conns[0]
    
    return displayLayer

def CheckFreezedMeshes(meshes):
    correctState = True
    messages = []
    for mesh in meshes:
        meshShape = mesh.getShape()
        displayType = meshShape.overrideDisplayType.get()
        if (displayType == 2):
            continue
        
        displayLayer = GetDisplayLayer(mesh)
        if (displayLayer == None):
            correctState = False
            messages.append("-" + mesh.getName() + ": has no display layer to be freezed")
            break
        
        layerDisplayType = displayLayer.displayType.get()
        if (layerDisplayType != 2):
            correctState = False
            messages.append("-" + mesh.getName() + ": display layer is not freezed")
            break
    
    return correctState, messages

def FixFreezedMeshes(meshes):
    success = True
    
    for mesh in meshes:
        displayLayer = GetDisplayLayer(mesh)
        if (displayLayer == None):
            success = False
        else:
            displayType = displayLayer.displayType.get()
            if (displayType != 2):
                displayLayer.displayType.set(2)
    
    return success
    
def CheckMeshesDeformers(meshes):
    correctState = True
    messages = []
    for mesh in meshes:
        deformerHistory = pm.listHistory(mesh, pruneDagObjects=True, interestLevel=1)
        for deformer in deformerHistory:
            if (pm.nodeType(deformer) != "skinCluster"):
                correctState = False
                break
        if (not correctState):
            messages.append("-" + mesh.getName() + ": has deformers")
            break
    
    return correctState, messages

def GetExportJoints():
    skeleton = GetSkeletonGroup()
    joints = []
    if (skeleton):
        joints = pm.listRelatives(skeleton, allDescendents=True, type="joint")
    return joints

def CheckJointsRotation(joints):
    correctState = True
    messages = []
    
    decimalThreshold = 0.00001
    threshold = 360 + decimalThreshold
    
    for joint in joints:
        if (joint.rotateX.get() > threshold or joint.rotateX.get() < -threshold):
            correctState = False
            messages.append("-" + joint.getName() + ": has rotations above 360")
            break
        if (joint.rotateY.get() > threshold or joint.rotateY.get() < -threshold):
            correctState = False
            messages.append("-" + joint.getName() + ": has rotations above 360")
            break
        if (joint.rotateZ.get() > threshold or joint.rotateZ.get() < -threshold):
            correctState = False
            messages.append("-" + joint.getName() + ": has rotations above 360")
            break
    
    return correctState, messages

def CheckJointsOrient(joints):
    correctState = True
    messages = []
    for joint in joints:
        if (joint.jointOrientX.get() != 0):
            correctState = False
            messages.append("-" + joint.getName() + ": has joint orient values")
            break
        if (joint.jointOrientY.get() != 0):
            correctState = False
            messages.append("-" + joint.getName() + ": has joint orient values")
            break
        if (joint.jointOrientZ.get() != 0):
            correctState = False
            messages.append("-" + joint.getName() + ": has joint orient values")
            break
    
    return correctState, messages

def FixJointsOrient(joints):
    success = False
    
    for joint in joints:
        conns = pm.listConnections(joint.rotateX, type="constraint")
        if (len(conns) > 0):
            # Is constrained
            joint.jointOrientX.set(0)
            joint.jointOrientY.set(0)
            joint.jointOrientZ.set(0)
        else:
            # Is not constrained
            orientation = pm.xform(joint, query=True, worldSpace=True, rotation=True)
            joint.jointOrientX.set(0)
            joint.jointOrientY.set(0)
            joint.jointOrientZ.set(0)
            pm.xform(joint, worldSpace=True, rotation=orientation)
    
    success = True
    return success

def CheckJointsSegmentScaleCompensate(joints):
    correctState = True
    messages = []
    for joint in joints:
        if (joint.segmentScaleCompensate.get() != 0):
            correctState = False
            messages.append("-" + joint.getName() + ": segment scale compaste should be disabled")
            break
    
    return correctState, messages

def FixJointsSegmentScaleCompensate(joints):
    success = False
    
    for joint in joints:
        if (joint.segmentScaleCompensate.get() != 0):
            joint.segmentScaleCompensate.set(0)
    success = True
    
    return success

def GetJointsFromGroup(group):
    joints = pm.listRelatives(group, allDescendents=True, type="joint")
    return joints

def GetDistance(objA, objB):
    return sqrt(pow(objA[0]-objB[0],2)+pow(objA[1]-objB[1],2)+pow(objA[2]-objB[2],2))

def CheckBindPoses(skeletonGroup, meshes):
    correctState = True
    messages = []
    joints = GetJointsFromGroup(skeletonGroup)
    for joint in joints:
        bindPoses = pm.listConnections(joint.message, type="dagPose")
        if (len(bindPoses) != 1):
            # Multiple bind poses found
            correctState = False
            messages.append("-" + joint.getName() + ": multiple bind poses found")
            break
    
    if (correctState):
        bindMatrices = {}
        for mesh in meshes:
            skinClusterName = mel.eval('findRelatedSkinCluster ' + mesh)
            if (skinClusterName != ""):
                skinCluster = pm.PyNode(skinClusterName)
                
                if (skinCluster is not None):
                    jointsAmount = skinCluster.matrix.numElements()
                    jointsFound = 0
                    idx = 0
                    while (jointsFound < jointsAmount):
                        try:
                            joint = pm.listConnections(skinCluster.matrix[idx])[0]
                            if (joint.getName() in bindMatrices):
                                if (bindMatrices[joint.getName()] != skinCluster.bindPreMatrix[idx].get()):
                                    correctState = False
                                    messages.append("-" + joint.getName() + ": multiple bind matrices found")
                                    break
                            else:
                                bindMatrices[joint.getName()] = skinCluster.bindPreMatrix[idx].get()
                            jointsFound += 1
                        except IndexError:
                            pass
                        idx += 1
                    
                    if (not correctState):
                        break
            
            if (not correctState):
                break
    
    return correctState, messages

def FixBindPoses(skeletonGroup, meshes):
    success = False
    
    dcRoot = None
    results = pm.listRelatives(skeletonGroup, allDescendents=True)
    filteredResult = []
    for result in results:
        if (result.getName() == "DC_Root"):
            filteredResult.append(result)
    if (len(filteredResult) == 1):
        dcRoot = filteredResult[0]
        skn.RebuildHierarchyDagPose(dcRoot.longName())
        selection = cmds.ls(sl=True, type="transform")
        if (selection):
            skn.ResetMeshBindTMs(selection)
        success = True
    
    return success

def GetDcsCtls():
    regex = re.compile("[dc_]{3}\w+[_ctl]{4}$", re.IGNORECASE)
    allElements = cmds.ls()
    dcsCtls = list()
    for element in allElements:
        nameToMatch = element.split("|")[-1]
        if regex.match(nameToMatch):
            matchedNode = pm.PyNode(element)
            if (type(matchedNode) == pm.nodetypes.Transform):
                dcsCtls.append(pm.PyNode(element))
    return dcsCtls

def CheckDcsAsPointLocators(dcsCtls):
    correctState = True
    messages = []
    for dc in dcsCtls:
        shapes = pm.listRelatives(dc, shapes=True)
        pointLocatorFound = False
        for shape in shapes:
            if (pm.nodeType(shape) == "PointLocator"):
                pointLocatorFound = True
                break
        if (not pointLocatorFound):
            messages.append("-" + dc.getName() + ": should be pointLocator")
            correctState = False
            break
    
    return correctState, messages

def FixDcsAsPointLocators(dcsCtls):
    success = False
    
    noPointLocatorDcs = []
    
    for dc in dcsCtls:
        shapes = pm.listRelatives(dc, shapes=True)
        pointLocatorFound = False
        for shape in shapes:
            if (pm.nodeType(shape) == "PointLocator"):
                pointLocatorFound = True
                break
        if (not pointLocatorFound):
            noPointLocatorDcs.append(dc)
    
    rigshapes.ChangeShapeToPointLocator(noPointLocatorDcs)
    success = True
    
    return success

def CheckBasicDcs(skeletonGroup, dcsCtls):
    correctState = True
    messages = []
    basicDcs = ["DC_Root", "DC_Floor", "DC_Center", "DC_FX"]
    basicDcsCtls = ["DC_Root_C0_ctl", "DC_Floor_C0_ctl", "DC_Center_C0_ctl", "DC_FX_C0_ctl"]
    
    dcsFound = []
    results = pm.listRelatives(skeletonGroup, allDescendents=True)
    for result in results:
        if ("dc_" in result.getName().lower()):
                dcsFound.append(result)
    dcsFoundLower = [x.lower() for x in dcsFound]
    for basicDc in basicDcs:
        if (not (basicDc.lower() in dcsFoundLower)):
            correctState = False
            messages.append("-" + basicDc + ": DC not found")
            break
    
    if (correctState):
        # Check if dcs are constrained
        for basicDc in basicDcs:
            dc = GetNodeIgnoreCase(basicDc)
            conns = pm.listConnections(dc, type="constraint")
            if (len(conns) == 0):
                correctState = False
                messages.append("-" + basicDc + ": DC isn't constrained to anything")
                break
    
    return correctState, messages

def GetPointLocatorShape(node):
    pointLocator = None
    shapes = pm.listRelatives(node, shapes=True)
    for shape in shapes:
        if (pm.nodeType(shape) == "PointLocator"):
            pointLocator = shape
            break
    return pointLocator

def GetPointLocatorShownAxes(pointLocator):
    shownAxes = [True, True, True]
    if (pointLocator.x_axis.get() == 0):
        shownAxes[0] = False
    if (pointLocator.y_axis.get() == 0):
        shownAxes[1] = False
    if (pointLocator.y_axis.get() == 0):
        shownAxes[2] = False
    return shownAxes

def CheckDcShot(dcs):
    correctState = True
    messages = []
    dcShot = None
    for dc in dcs:
        if ("dc_shot" in dc.getName().lower()):
            dcShot = dc
            break
    
    if (dcShot != None):
        dcShotPointLocator = GetPointLocatorShape(dcShot)
        if (dcShotPointLocator == None):
            correctState = False
            messages.append("-" + dcShot.getName() + ": is not pointLocator")
        else:
            shownAxes = GetPointLocatorShownAxes(dcShotPointLocator)
            if (not (shownAxes[0] == True and shownAxes[1] == False and shownAxes[2] == False)):
                messages.append("-" + dcShot.getName() + ": only X axis should be visible")
                correctState = False
    
    return correctState, messages

def FixDcShot(dcs):
    success = True
    
    dcShot = None
    for dc in dcs:
        if ("dc_shot" in dc.getName().lower()):
            dcShot = dc
            break
    
    if (dcShot != None):
        dcShotPointLocator = GetPointLocatorShape(dcShot)
        if (dcShotPointLocator == None):
            success = False
        else:
            dcShotPointLocator.x_axis.set(1)
            dcShotPointLocator.y_axis.set(0)
            dcShotPointLocator.z_axis.set(0)
            success = True
    
    return success

def GetScenePath():
    path = pm.system.sceneName()
    return path

def CheckGeneratedActor(actors):
    correctState = True
    messages = []
    if (len(actors) == 0):
        correctState = False
        messages.append("-No actor found")
    else:
        for actor in actors:
            # Check empty main subactor
            mainSubActorResult = pm.listConnections(actor.mainSubActor, type="subActor")
            if (len(mainSubActorResult) == 0):
                correctState = False
                messages.append("-" + actor.getName() + ": no main subactor found")
                break
            
            # Check empty anim subactor
            animSubActorResult = pm.listConnections(actor.animSubActor, type="subActor")
            if (len(animSubActorResult) == 0):
                correctState = False
                messages.append("-" + actor.getName() + ": no anim subactor found")
                break
            
            # Loop subactors
            # sub_actor_list = pm.listConnections(actor.subActorList, type="subActor")
            # for sub_actor in sub_actor_list:
            #     pass
    
    return correctState, messages

def CheckAnimFile(scenePath):
    correctState = False
    messages = []
    sceneFolder = scenePath.parent
    characterFolder = sceneFolder.parent
    rigFileName = os.path.basename(scenePath)
    animFileName = rigFileName.lower().replace("_rig", "_anim")
    animFileName = animFileName.split(".")[0]
    
    elements = os.listdir(characterFolder)
    for element in elements:
        elementSplit = element.split(".")
        if (len(elementSplit) > 1):
            elementName = elementSplit[0]
            elementFormat = elementSplit[1]
            if ((elementFormat == "ma") or (elementFormat == "mb")):
                elementName = elementName.lower()
                if (elementName == animFileName):
                    correctState = True
                    break
    
    if (not correctState):
        messages.append("-Anim file not found")
    
    return correctState, messages

def FixAnimFile(scenePath):
    success = False
    
    sceneFolder = scenePath.parent
    characterFolder = sceneFolder.parent
    rigFileName = os.path.basename(scenePath)
    animFileName = rigFileName.replace("_rig", "_anim")
    animPath = os.path.join(characterFolder, animFileName)
    correctState = os.path.exists(animPath)
    
    mainDisk = 'C:'
    splittedPath = scenePath.split('/')
    intialPathIdx = 1
    finalPath = mainDisk
    for i in range(intialPathIdx, len(splittedPath)):
        finalPath += '/' + splittedPath[i]
    
    if (correctState):
        success = True
    else:
        animFile = StandaloneProcess.CreateAnimFile(rigFile=finalPath)
        success = True
    return success

def CheckSkeletonGroupVisibility(skeletonGroup):
    correctState = False
    messages = []
    atrtibuteExists = pm.attributeQuery("visibility", node=skeletonGroup, exists=True)
    attributeValue = None
    if (atrtibuteExists):
        attributeValue = skeletonGroup.visibility.get()
        if (attributeValue == False):
            correctState = True
        else:
            messages.append("-Skeleton group shouldn't be visible")
    return correctState, messages

def FixSkeletonGroupVisibility(skeletonGroup):
    success = False
    atrtibuteExists = pm.attributeQuery("visibility", node=skeletonGroup, exists=True)
    attributeValue = None
    if (atrtibuteExists):
        attributeValue = skeletonGroup.visibility.get()
        if (attributeValue == False):
            success = True
        else:
            attributeValue = skeletonGroup.visibility.set(False)
            success = True
    return success

def GetSceneDisplayLayers():
    sceneDisplayLayers = pm.ls(type="displayLayer")
    exclude = ["defaultLayer"]
    finalDisplayLayers = []
    for sceneDisplayLayer in sceneDisplayLayers:
        if (not (sceneDisplayLayer.getName() in exclude)):
            finalDisplayLayers.append(sceneDisplayLayer)
    return finalDisplayLayers

def CheckDisplayLayers(displayLayers):
    correctState = True
    messages = []
    for displayLayer in displayLayers:
        conns = pm.listConnections(displayLayer.drawInfo)
        if (len(conns) == 0):
            correctState = False
            messages.append("-" + displayLayer.getName() + ": displayLayer shouldn't be empty")
    
    return correctState, messages

def FixDisplayLayers(displayLayers):
    success = False
    
    toDelete = []
    for displayLayer in displayLayers:
        conns = pm.listConnections(displayLayer.drawInfo)
        if (len(conns) == 0):
            toDelete.append(displayLayer)
    pm.delete(toDelete)
    success = True
    
    return success

def GetSceneMaterials():
    exclude = ["lambert1", "standardSurface1", "particleCloud1", "shaderGlow1"]
    allMaterials = pm.ls(mat=True)
    materials = []
    for mat in allMaterials:
        if (mat.getName() not in exclude):
            materials.append(mat)
    return materials

def GetUsedMaterials():
    meshes = GetSceneMeshes()
    usedMaterials = []
    for mesh in meshes:
        shapes = pm.listRelatives(mesh, s=True)
        shadeEng = pm.listConnections(shapes, type="shadingEngine")
        usedMaterials.extend(pm.ls(pm.listConnections(shadeEng), materials=True))
    # Unique list
    usedMaterials = list(set(usedMaterials))
    return usedMaterials
    
def CheckMaterials(materials):
    correctState = True
    messages = []
    usedMaterials = GetUsedMaterials()
    for material in materials:
        if (not (material in usedMaterials)):
            correctState = False
            messages.append("-" + material.getName() + ": material is not being used")
            break
    
    return correctState, messages

def FixMaterials(materials):
    success = True
    
    usedMaterials = GetUsedMaterials()
    toDelete = []
    for material in materials:
        if (not (material in usedMaterials)):
            toDelete.append(material)
    
    pm.delete(toDelete)
    success = True
    
    return success

def FpsToString(fps):
    fpsString = str(fps)
    if (fps == 15):
        fpsString = "game"
    elif (fps == 24):
        fpsString = "film"
    elif (fps == 25):
        fpsString = "pal"
    elif (fps == 30):
        fpsString = "ntsc"
    elif (fps == 48):
        fpsString = "show"
    elif (fps == 50):
        fpsString = "palf"
    elif (fps == 60):
        fpsString = "ntscf"
    return fpsString

def CheckFps(targetFps):
    correctState = False
    messages = []
    fpsString = FpsToString(targetFps)
    currrentFps = pm.currentUnit(query=True, time=True)
    if (currrentFps == fpsString):
        correctState = True
    else:
        messages.append("-Fps should be set to 30")
    return correctState, messages

def FixFps(targetFps):
    success = False
    fpsString = FpsToString(targetFps)
    pm.currentUnit(time=fpsString)
    success = True
    return success

def CheckPastedNodes():
    correctState = True
    finalMessages = None
    incorrectMessages = ["-There are pasted nodes:"]
    allNodes = pm.ls()
    pastedNodes = []
    for node in allNodes:
        if ("pasted__" in node.getName().lower()):
            pastedNodes.append(node)
            incorrectMessages.append("    " + node.getName())
    if (len(pastedNodes) > 0):
        correctState = False
        finalMessages = incorrectMessages
    return correctState, finalMessages

def CheckNormalizedWeights(actors):
    correctState = True
    messages = []
    
    #decimalThreshold = 0.000000000000001
    decimalThreshold = 0.0000000001
    
    for actor in actors:
        actorMeshes = GetActorMeshes([actor])
        for actorMesh in actorMeshes:
            verticesAmount = pm.polyEvaluate(actorMesh, v=True)
            skinCluster = str(mel.eval("findRelatedSkinCluster " + actorMesh.getName()))
            for vertexIdx in range(verticesAmount):
                vtxWeight = pm.skinPercent(skinCluster, "{}.vtx[{}]".format(actorMesh.getName(), str(vertexIdx)), query=True, value=True)
                sumWeight = sum(vtxWeight)
                if (sumWeight < (1.0 - decimalThreshold) or sumWeight > (1.0 + decimalThreshold)):
                    print(sumWeight)
                    correctState = False
                    break
            if (not correctState):
                messages.append("-" + actorMesh.getName() + ": weights are not normalized")
                break
        if (not correctState):
            break
    
    return correctState, messages

def FixNormalizedWeights(actors):
    success = True
    
    currentSelection = pm.ls(sl=True)
    
    for actor in actors:
        actorMeshes = GetActorMeshes([actor])
        for actorMesh in actorMeshes:
            skinCluster = mel.eval("findRelatedSkinCluster " + actorMesh.getName())
            skinCluster = pm.PyNode(skinCluster)
            if (skinCluster.normalizeWeights != 1):
                skinCluster.normalizeWeights.set(1)
            pm.select(clear=True)
            pm.select(actorMesh)
            pm.skinPercent(str(skinCluster), normalize=True)
    
    pm.select(clear=True)
    pm.select(currentSelection)
    
    return success
