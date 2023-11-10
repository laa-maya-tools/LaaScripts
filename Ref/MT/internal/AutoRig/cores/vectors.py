import maya.OpenMaya as om
import maya.cmds as cmds

def queryPointsInVector(start, end, points=3):
    if type(start) in [str, unicode]:
        start = cmds.xform(start, t=True, ws=True, q=True)
    if type(end) in [str, unicode]:
        end = cmds.xform(end, t=True, ws=True, q=True)
    vec = [a-b for a,b in zip(end, start)]
    result = [start]
    for ind in range(1, points+2):
        result.insert(ind, [(ax/float(points+1))*(ind)+start[off] for off,ax in enumerate(vec)] )
    return result

def queryCrossVector(orig, start, end, asAxis=False):
    origv = om.MVector(*cmds.xform(orig, t=1, ws=1, q=1))
    startv = om.MVector(*cmds.xform(start, t=1, ws=1, q=1))
    endv = om.MVector(*cmds.xform(end, t=1, ws=1, q=1))
    firstv = (startv - origv)
    secondv = (endv - origv)
    rvec = om.MVector(abs((firstv.y * secondv.z) - (firstv.z * secondv.y)),
                    abs((firstv.z * secondv.x) - (firstv.x * secondv.z)),
                    abs((firstv.x * secondv.y) - (firstv.y * secondv.x))).normal()
    return {0:'x', 1:'y', 2:'z'}[rvec.index(max(rvec))] if asAxis else rvec

def queryVector(start, end, asAxis=False):
    temp = cmds.createNode('transform', p=end, ss=True)
    cmds.parent(temp, start)
    aimv = cmds.getAttr(temp + '.t')[0]
    cmds.delete(temp)
    aimmn, aimmx = min(aimv), max(aimv)
    if abs(aimmn) > aimmx:
        if aimv.index(aimmn) == 0:
            return 'x' if asAxis else [-1,0,0]
        elif aimv.index(aimmn) == 1:
            return 'y' if asAxis else [0,-1,0]
        else:
            return 'z' if asAxis else [0,0,-1]
    else:
        if aimv.index(aimmx) == 0:
            return 'x' if asAxis else [1,0,0]
        elif aimv.index(aimmx) == 1:
            return 'y' if asAxis else [0,1,0]
        else:
            return 'z' if asAxis else [0,0,1]