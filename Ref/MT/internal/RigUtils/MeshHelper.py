import pymel.core as pm

import ModellingUtils.Core as Modelling

def CreateTrianglesOnReferences(references, triangleSize, axis=[1,0,0], extraRot=[0,0,0]):
    references = [pm.PyNode(x) for x in references]
    trianglesTransf = []
    for i in range(len(references)):
        tri = Modelling.CreateTriangle(triangleSize, axis)
        # Position the Triangles for future UV mapping 
        tri.tz.set(i * triangleSize)
        trianglesTransf.append(tri)
    
    # Create planar UVs
    faces = [getattr(x, "f")[0] for x in trianglesTransf]
    pm.polyProjection(faces, ch=1, ibd=True, type="planar", mapDirection="x")
    
    # Reposition Triangles based on references
    for i in range(len(references)):
        pm.matchTransform(trianglesTransf[i], references[i], position=True, rotation=True)
        if (extraRot != [0,0,0]):
            pm.rotate(trianglesTransf[i], extraRot, relative=True, objectSpace=True)
    
    # Combine Meshes and delete history
    combineResult = pm.polyUnite(trianglesTransf)
    pm.delete(combineResult, constructionHistory = True)
    
    return combineResult[0]

def CreateSingleFollicleOnMeshFaces(meshNode, sysName):
    meshNode = pm.PyNode(meshNode)
    pm.select(meshNode.f)
    pm.mel.eval("createHair 1 2 2 0 0 1 0 25 0 2 2 2")
    
    hairSysNode = pm.ls("hairSystemShape*")[0]
    # OutputCurves Parent Transform
    outCurvesParent = hairSysNode.outputHair[0].connections()[0].outCurve.connections()[0].getParent()
    # Nucleus
    nucleusNode = hairSysNode.currentState.connections()[0]
    # HairSystem
    hairsSysParent = hairSysNode.getParent()
    # Follicles Group
    folliclesGrp = hairSysNode.inputHair[0].connections()[0].getParent()
    
    # Delete unused nodes
    pm.delete(outCurvesParent, nucleusNode, hairsSysParent)
    
    folliclesGrp.setName("{}_follicles".format(sysName))
    for idx, child in enumerate(folliclesGrp.getChildren()):
        child.setName("{}_follicle{}".format(sysName, idx))
        grandChildTransform = child.getChildren(type="transform")[0]
        grandChildTransform.setName("{}_{}_npo".format(sysName, idx))
        grandChildTransform.rotate.set([180, -90, 0])
    
    return folliclesGrp