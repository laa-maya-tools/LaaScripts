import pymel.core as pm
import maya.cmds as cmds

def SetPivotToWorld(node):
    cmds.xform(node, ws=True, a=True, piv=(0,0,0))
    cmds.makeIdentity(node, apply=True, n=0, pn=1)

def CleanShape(node):
    cmds.lattice(node, dv=(2, 2, 2), oc=True)
    cmds.bakePartialHistory(node, preCache=True)

def CreateTriangle(size, axis=[1,0,0]):
    transf = pm.polyPlane(axis=axis, sx=1, sy=1, w=size, h=size)[0]
    shape = transf.getShape()
    
    # Merge 2 last vertices to have a triangle
    pm.select(shape.vtx[2], shape.vtx[3])
    pm.polyMergeVertex(d=size+0.01)
    pm.select(None)
    
    return transf