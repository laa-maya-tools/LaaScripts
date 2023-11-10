import maya.api.OpenMaya as OpenMaya

import RigManager.Plugins.RigChain as RigChainPlugin

import RigManager.IKFKChain as IKFKChainWrapper

import NodeID

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass


class IKFKChainNode(RigChainPlugin.RigChain):
    
    # Plugin data
    nodeName    = "IKFKChain"
    nodeID      = NodeID.RigManagerRigChainID
    
    # Node Attributes
    fkLimbA = OpenMaya.MObject()
    fkLimbB = OpenMaya.MObject()
    fkLimbC = OpenMaya.MObject()
    fkLimbCuadruped = OpenMaya.MObject()
    fkPlanarAxis = OpenMaya.MObject()
    
    ikLimbA = OpenMaya.MObject()
    ikLimbB = OpenMaya.MObject()
    ikLimbC = OpenMaya.MObject()
    ikPlanarAxis = OpenMaya.MObject()
    ikPoleVector = OpenMaya.MObject()
    ikSwivelPlug = OpenMaya.MObject()
    ikSwivelOutputMode = OpenMaya.MObject()
    
    ikFkBlendPlug = OpenMaya.MObject()
    swivelCombineMode = OpenMaya.MObject()
    
    autoSnap = OpenMaya.MObject()
        
    @staticmethod
    def creator():
        return IKFKChainNode()

    @staticmethod
    def initializer():
        messageAttribute = OpenMaya.MFnMessageAttribute()
        unitAttribute = OpenMaya.MFnUnitAttribute()
        enumAttribute = OpenMaya.MFnEnumAttribute()
        numericAttribute = OpenMaya.MFnNumericAttribute()
        
        # FK Limb A
        IKFKChainNode.fkLimbA = messageAttribute.create("fkLimbA", "fka")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.fkLimbA)
        
        # FK Limb B
        IKFKChainNode.fkLimbB = messageAttribute.create("fkLimbB", "fkb")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.fkLimbB)
        
        # FK Limb C
        IKFKChainNode.fkLimbC = messageAttribute.create("fkLimbC", "fkc")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.fkLimbC)
        
        # FK Limb Cuadruped
        IKFKChainNode.fkLimbCuadruped = messageAttribute.create("fkLimbCuadruped", "fkq")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.fkLimbCuadruped)
        
        # FK Planar Axis
        IKFKChainNode.fkPlanarAxis = enumAttribute.create("fkPlanarAxis", "fkpa", 1)
        for i, axis in enumerate(IKFKChainWrapper.IKFKChain.axisEnum):
            enumAttribute.addField(axis[0], i)
        enumAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.fkPlanarAxis)
        
        # IK Limb A
        IKFKChainNode.ikLimbA = messageAttribute.create("ikLimbA", "ika")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikLimbA)
        
        # IK Limb B
        IKFKChainNode.ikLimbB = messageAttribute.create("ikLimbB", "ikb")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikLimbB)
        
        # IK Limb C
        IKFKChainNode.ikLimbC = messageAttribute.create("ikLimbC", "ikc")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikLimbC)
        
        # IK Planar Axis
        IKFKChainNode.ikPlanarAxis = enumAttribute.create("ikPlanarAxis", "ikpa", 1)
        for i, axis in enumerate(IKFKChainWrapper.IKFKChain.axisEnum):
            enumAttribute.addField(axis[0], i)
        enumAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikPlanarAxis)

        # IK Pole Vector
        IKFKChainNode.ikPoleVector = messageAttribute.create("ikPoleVector", "ikpv")
        messageAttribute.writable = True
        messageAttribute.readable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikPoleVector)
        
        # IK Swivel Angle
        IKFKChainNode.ikSwivelPlug = unitAttribute.create("ikSwivelPlug", "iksp", unitAttribute.kAngle)
        unitAttribute.writable = True
        unitAttribute.readable = False
        unitAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikSwivelPlug)
        
        # IK Output Mode
        IKFKChainNode.ikSwivelOutputMode = enumAttribute.create("ikSwivelOutputMode", "iksom", 0)
        enumAttribute.addField("Pole", 0)
        enumAttribute.addField("Swivel", 1)
        enumAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikSwivelOutputMode)
        
        # IK/FK Blend Plug
        IKFKChainNode.ikFkBlendPlug = numericAttribute.create("ikFkBlendPlug", "ikfkb", OpenMaya.MFnNumericData.kDouble, 0)
        numericAttribute.writable = True
        numericAttribute.readable = False
        numericAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.ikFkBlendPlug)
        
        # IK Output Mode
        IKFKChainNode.swivelCombineMode = enumAttribute.create("swivelCombineMode", "scm", 0)
        enumAttribute.addField("Pole And Twist", 0)
        enumAttribute.addField("Only Pole", 1)
        enumAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.swivelCombineMode)
        
        # Auto Snap
        IKFKChainNode.autoSnap = numericAttribute.create("autoSnap", "as", OpenMaya.MFnNumericData.kBoolean, True)
        numericAttribute.keyable = False
        IKFKChainNode.addAttribute(IKFKChainNode.autoSnap)
