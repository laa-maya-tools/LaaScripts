import pymel.core as pm
import MGearExtended.PostProUtils as PostP

def DropOriginOffset(moduleName):
    """Eliminates the offset that exists between the first control and the real origin

    Args:
        moduleName (String): Base Name of the module to operate with.
    """
    refNode = pm.PyNode("{}_0_cns".format(moduleName))
    inMotionPaths = refNode.translate.inputs(type="motionPath")
    if inMotionPaths:
        inMotionPaths[0].uValue.set(0)

def CreateOriginTranslationSpace(moduleName, destiny, UICtl):
    """_summary_

    Args:
        moduleName (String): Base Name of the module to operate with.
        destiny (String): Name of the object that will be connected as Translation Space
        UICtl (String): Name of the 'UI' control that will hold the switch 'enum' attribute.
    """
    refNode = pm.PyNode("{}_ik0_npo".format(moduleName))
    refDestiny = pm.PyNode(destiny)
    
    switchNode = pm.group(em=True, name="{}_ik0_switch".format(moduleName))
    refNodeParent = refNode.getParent()
    pm.matchTransform(switchNode, refNodeParent, pos=True, rot=True)
    switchNode.setParent(refNodeParent)
    refNode.setParent(switchNode)
    
    #create destiny switch ref
    destinySwitchRef =  pm.group(em=True, name="{}_ik0_switchRef".format(moduleName))
    pm.matchTransform(destinySwitchRef, refNodeParent, pos=True, rot=True)
    destinySwitchRef.setParent(refDestiny)
    
    #create PointConstraint
    cns = pm.pointConstraint([refNodeParent, destinySwitchRef], switchNode)
    
    #create Attribute
    pm.addAttr(UICtl, ln="origin_ref", at="enum", en=["self", destiny], k=True)
    ui = pm.PyNode(UICtl)
    
    #connect Attribute to constraint
    revNode = pm.createNode("reverse")
    ui.origin_ref.connect(revNode.inputX)
    
    realPlug = cns.target[0].targetWeight.inputs(p=True)[0]
    revNode.outputX.connect(realPlug)
    realPlug = cns.target[1].targetWeight.inputs(p=True)[0]
    ui.origin_ref.connect(realPlug)

def CreateIKChestSpaceSwitches(moduleName, targets, UICtl):
    """Create Space Switches for the Chest IK of the spine
    
    Args:
        moduleName (String): Base Name of the module to operate with.
        targets (Array(String)): Destination Spaces
        UICtl (String): Name of the Control that will hold the attrbite
    """
    PostP.CreateSpaceSwitches(moduleName, "ik1", targets, UICtl, "chest_IK")
