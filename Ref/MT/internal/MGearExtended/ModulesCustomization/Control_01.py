import pymel.core as pm
import MGearExtended.ModulesCustomization   as cMod
import MGearExtended.PostProUtils           as PostP

# Utils
def GetCtl(moduleName):
    return pm.PyNode("{}_ctl".format(moduleName))

def GetJoint(moduleName):
    mConst = GetMatrixConstraint(moduleName)
    if (mConst):
        conn = mConst.drivenParentInverseMatrix.connections(type="joint")
        if (conn):
            return conn[0]
    return None

def GetMatrixConstraint(moduleName):
    ctl = GetCtl(moduleName)
    mConst = ctl.worldMatrix.connections(type="mgear_matrixConstraint")
    if (mConst):
        return mConst[0]
    return None
######################################################################

def FixNonUniformScaling(moduleName):
    mconst = GetMatrixConstraint(moduleName)
    jnt = GetJoint(moduleName)
    mconst.scaleZ.disconnect()
    mconst.scale.connect(jnt.scale)

def AlignRootOrientToGuide(moduleName):
    guideRoot   = cMod.GetGuideRoot(moduleName)
    ctlRoot     = cMod.GetModuleControlsRoot(moduleName)
    pm.matchTransform(ctlRoot, guideRoot, rotation=True)
    #Set ik_cns child transform to 0
    ikcnsChild = [x for x in ctlRoot.getChildren() if "_ik_cns" in x.getName()]
    for c in ikcnsChild:
        PostP.SetAttribLocked([c.rx, c.ry, c.rz], False)
        c.rx.set(0)
        c.ry.set(0)
        c.rz.set(0)
        PostP.SetAttribLocked([c.rx, c.ry, c.rz], True)

def SetParentDriver(moduleName, nodeName, maintainOffset=False):
    ctlRoot = cMod.GetModuleControlsRoot(moduleName)
    driver = pm.PyNode(nodeName)
    
    pm.parentConstraint(driver, ctlRoot, mo=maintainOffset)

def MirrorBehavior(moduleName, axisMirror="x", keepChildrenOnMirror=False):
    axisMirror = axisMirror.lower()
    if (axisMirror in ["x", "y", "z"]):
        ctlRoot = cMod.GetModuleControlsRoot(moduleName)
        ctlNode = pm.PyNode("{}_ctl".format(moduleName))
        mirrorNode = pm.group(empty=True, parent=ctlRoot, name="{}_mirrGrp".format(ctlRoot.getName()))
        if (not keepChildrenOnMirror):
            ctlChildren = ctlNode.getChildren(type=pm.nodetypes.Transform)
            print(ctlChildren)
            auxGrp = pm.group(empty=True, world=True)
            for child in ctlChildren:
                child.setParent(auxGrp)
        ctlNode.getParent().setParent(mirrorNode)
        scaleAttribute = getattr(mirrorNode, "s{}".format(axisMirror))
        scaleAttribute.set(-1)
        if (not keepChildrenOnMirror):
            for child in ctlChildren:
                child.setParent(ctlNode)
            pm.delete(auxGrp)
    else:
        raise Exception("Invalid Axis to Mirror. Should be X, Y or Z")