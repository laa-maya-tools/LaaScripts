import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya

import Utils.OpenMaya as OpenMayaUtils
import Utils.Maya.AnimLayers as AnimLayerUtils

from ImportAnimationFromMax.ImportAnimationFromMax import IKLimb

NAMESPACE = "Zebesian"

LEG_TRUE_FK_FOOT_CTL_B = "{namespace}:leg_{side}0_fk2_ctl"
LEG_TRUE_IK_CTL_B = "{namespace}:leg_{side}0_ik_ctl"
LEG_TRUE_POLE_CTL_B = "{namespace}:leg_{side}0_upv_ctl"
LEG_TRUE_UI_CTL_B = "{namespace}:legUI_{side}0_ctl"

LEG_FAKE_IK_CTL_B = "{namespace}:leg_{side}1_ik_ctl"
LEG_FAKE_POLE_CTL_B = "{namespace}:leg_{side}1_upv_ctl"
LEG_FAKE_UI_CTL_B = "{namespace}:legUI_{side}1_ctl"

LEG_TRUE_TOES_CTL_B = [
    "{namespace}:foot_{side}0_fk0_ctl",
    "{namespace}:Toe_{side}0_fk0_ctl",
    "{namespace}:Toe_{side}1_fk0_ctl"
    ]
LEG_FAKE_TOES_CTL_B = [
    "{namespace}:foot_{side}1_fk0_ctl",
    "{namespace}:Toe_{side}2_fk0_ctl",
    "{namespace}:Toe_{side}3_fk0_ctl"
    ]

LEG_TRUE_CTLS_B = [
    "{namespace}:leg_{side}0_fk0_ctl",
    "{namespace}:leg_{side}0_fk1_ctl",
    LEG_TRUE_FK_FOOT_CTL_B,
    LEG_TRUE_IK_CTL_B,
    LEG_TRUE_POLE_CTL_B,
    LEG_TRUE_UI_CTL_B
    ] + LEG_TRUE_TOES_CTL_B

LEG_BLEND_PLUG = "{}.leg_blend"

LEG_FOOT_OFFSET = {
    "L": OpenMaya.MVector(0.913589, -5.10956, 0.743643),
    "R": OpenMaya.MVector(-0.913589, -5.10956, 0.743643)
}

for side in ["L", "R"]:
    # Step 1: Preparations
    # Retrieve the right controls for each side
    LEG_TRUE_FK_FOOT_CTL = LEG_TRUE_FK_FOOT_CTL_B.format(namespace=NAMESPACE, side=side)
    LEG_TRUE_IK_CTL = LEG_TRUE_IK_CTL_B.format(namespace=NAMESPACE, side=side)
    LEG_TRUE_POLE_CTL = LEG_TRUE_POLE_CTL_B.format(namespace=NAMESPACE, side=side)
    LEG_TRUE_UI_CTL = LEG_TRUE_UI_CTL_B.format(namespace=NAMESPACE, side=side)
    
    LEG_FAKE_IK_CTL = LEG_FAKE_IK_CTL_B.format(namespace=NAMESPACE, side=side)
    LEG_FAKE_POLE_CTL = LEG_FAKE_POLE_CTL_B.format(namespace=NAMESPACE, side=side)
    LEG_FAKE_UI_CTL = LEG_FAKE_UI_CTL_B.format(namespace=NAMESPACE, side=side)
    
    LEG_TRUE_TOES_CTL = []
    for s in LEG_TRUE_TOES_CTL_B:
        LEG_TRUE_TOES_CTL.append(s.format(namespace=NAMESPACE, side=side))
        
    LEG_FAKE_TOES_CTL = []
    for s in LEG_FAKE_TOES_CTL_B:
        LEG_FAKE_TOES_CTL.append(s.format(namespace=NAMESPACE, side=side))
    
    LEG_TRUE_CTLS = []
    for s in LEG_TRUE_CTLS_B:
        LEG_TRUE_CTLS.append(s.format(namespace=NAMESPACE, side=side))
    
    # Mute all layers and removes the True controls from them if necessary
    animLayers = cmds.ls(type="animLayer") or []
    baseLayer = cmds.animLayer(q=True, root=True)
    plugsToRemove = []
    for node in LEG_TRUE_CTLS:
        attrs = cmds.listAttr(node, k=True)
        for attr in attrs:
            plugsToRemove.append("{}.{}".format(node, attr))
    for animLayer in animLayers:
        if animLayer != baseLayer:
            cmds.animLayer(animLayer, e=True, removeAttribute=plugsToRemove)
            cmds.animLayer(animLayer, e=True, mute=True, lock=True)
    
    # For some reason, if we run this script from the batcher and never read the True IK Foot's scale, it is set to 0 when cutting keys...
    # And this only happens to the left foot... but I refuse to hardcode just reading one foot scale.
    cmds.getAttr("{}.scale".format(LEG_TRUE_IK_CTL))
    
    # Retrieve a transform handler for the legs to easily set transformations
    trueFootTransformFn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(LEG_TRUE_IK_CTL))
    truePoleTransformFn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(LEG_TRUE_POLE_CTL))
    fakeFootTransformFn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(LEG_FAKE_IK_CTL))
    fakePoleTransformFn = OpenMaya.MFnTransform(OpenMayaUtils.asDagPath(LEG_FAKE_POLE_CTL))
    
    # Creates an IKLimb object to manage the change between IK and FK
    trueLegIKLimb = list(IKLimb.getIKLimbsFromNodes([LEG_TRUE_FK_FOOT_CTL], namespace=NAMESPACE).values())[0]
    fakeBlendPlug = LEG_BLEND_PLUG.format(LEG_FAKE_UI_CTL)
    
    # Step 2: When there is a keyframe on the Fake leg, align the True leg to the Fake one
    # Iterate through layers. If there are None, add the base layer (it should be None, so we need to check for it)
    if len(animLayers) == 0:
        animLayers = [baseLayer]
    for animLayer in animLayers:
        # If it is not the base layer, unmute it and add the True leg controls to it
        if animLayer != baseLayer:
            cmds.animLayer(animLayer, e=True, mute=False, lock=False)
            
            AnimLayerUtils.addNodesToLayer(animLayer, LEG_TRUE_CTLS, skipEnumAttributes=True)
        
        # Sets the layer as the preferred one
        if animLayer != None:   # If there are no layers this step is unnecessary
            cmds.animLayer(animLayer, e=True, preferred=True)
        
        # Removes all the keyframes on the layer
        cmds.cutKey(LEG_TRUE_CTLS, clear=True)
        
        # If it on the first layer, sets the Leg to IK on the first key (a keyframe must be used if there are layers)
        # NOTE: The Blend keyframes will be used to check times, assuming the limb's keys are synchronized
        keyTimes = cmds.keyframe(fakeBlendPlug, q=True, timeChange=True) or []
        if animLayer == baseLayer:
            cmds.setKeyframe(LEG_BLEND_PLUG.format(LEG_TRUE_UI_CTL), time=(keyTimes[0] if keyTimes else 0), value=1)
        
        if keyTimes:
            # Align the feet and pole when the Fake leg has a keyframe
            # NOTE: This will align the Fake IK foot and pole to the True IK's, assuming the IK is snapped to the FK
            for keyTime in keyTimes:
                cmds.currentTime(keyTime)
                
                # Sets the tangent type of the True leg equal to the Fake leg's. This will also set a new keyframe
                trueLegIKLimb.copyTangent("{}.translateX".format(LEG_FAKE_IK_CTL), [LEG_TRUE_IK_CTL, LEG_TRUE_POLE_CTL], time=keyTime)
                
                # Calculates the new foot transformation
                newFootPosition = fakeFootTransformFn.translation(OpenMaya.MSpace.kWorld)
                newFootRotation = fakeFootTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
                
                newFootPosition += LEG_FOOT_OFFSET[side].rotateBy(newFootRotation)
                
                # Aligns the foot's translation and rotation and the pole's translation
                trueFootTransformFn.setTranslation(newFootPosition, OpenMaya.MSpace.kWorld)
                trueFootTransformFn.setRotation(newFootRotation, OpenMaya.MSpace.kWorld)
                
                truePoleTransformFn.setTranslation(fakePoleTransformFn.translation(OpenMaya.MSpace.kWorld), OpenMaya.MSpace.kWorld)
                
                # Snaps the True FK to the IK
                trueLegIKLimb.modifyFKToMatchIK()
                
            # Apply an euluer filter
            cmds.filterCurve(LEG_TRUE_CTLS, filter="euler")
            
        # Copies the toes' animation
        copiedKeysCount = cmds.copyKey(LEG_FAKE_TOES_CTL)
        if copiedKeysCount > 0:
            cmds.pasteKey(LEG_TRUE_TOES_CTL, option="replace")
        
        # Mutes the layer back
        if animLayer != baseLayer:
            cmds.animLayer(animLayer, e=True, mute=True, lock=True)
                
    # Setp 3: Back on the base layer, sets the IK state for the limb
    if baseLayer != None:
        cmds.animLayer(baseLayer, e=True, preferred=True)
    keyTimes = cmds.keyframe(fakeBlendPlug, q=True, timeChange=True) or []
    for keyTime in keyTimes:
        cmds.currentTime(keyTime)
            
        fakeLegIKState = cmds.getAttr(fakeBlendPlug)
        trueLegIKLimb.setIKState(fakeLegIKState)

# Hides the fake legs and shows the true ones
cmds.setAttr("{}.visibility".format("FakeLegs"), False)
cmds.setAttr("{}.visibility".format("TrueLegs"), True)
