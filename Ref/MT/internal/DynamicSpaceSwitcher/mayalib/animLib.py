import maya.cmds as cmds 

_tanAuto     = "auto"
_tanClamped  = "clamped"
_tanFast     = "fast"
_tanFloat    = "float"
_tanLinear   = "linear"
_tanPlateaup  = "plateup"
_tanSlow     = "slow"
_tanSpline   = "spline"
_tanStep     = "step"
_tanStepnext = "stepnext"

def SetKeyframe(node, attr, value, time, inTangent=_tanStepnext, outTangent=_tanStep):
    """Set a keyframe"""
    cmds.setKeyframe(node, attribute=attr, value=value, t=time, inTangentType=inTangent, outTangentType=outTangent)
    
def SetPosKeyframe(node, value, time , inTangent=_tanStepnext, outTangent=_tanStep):
    """Set a Position keyframe"""
    SetKeyframe(node, "translateX", float(value[0]), time, inTangent, outTangent)
    SetKeyframe(node, "translateY", float(value[1]), time, inTangent, outTangent)
    SetKeyframe(node, "translateZ", float(value[2]), time, inTangent, outTangent)
    
def SetRotKeyframe(node, value, time , inTangent=_tanStepnext, outTangent=_tanStep):
    """Set a Rotation keyframe"""
    SetKeyframe(node, "rotateX", float(value[0]), time, inTangent, outTangent)
    SetKeyframe(node, "rotateY", float(value[1]), time, inTangent, outTangent)
    SetKeyframe(node, "rotateZ", float(value[2]), time, inTangent, outTangent)

def SetCurrentPosKey(node, inTangent=_tanStepnext, outTangent=_tanStep):
    """ Set position Keyframe with current value and current time """
    value = cmds.getAttr("{}.translate".format(node))[0]
    time = cmds.currentTime(query=True)
    SetPosKeyframe(node, value, time, inTangent, outTangent )

def SetCurrentRotKey(node, inTangent=_tanStepnext, outTangent=_tanStep):
    """ Set position Keyframe with current value and current time """
    value = cmds.getAttr("{}.rotate".format(node))[0]
    time = cmds.currentTime(query=True)
    SetRotKeyframe(node, value, time, inTangent, outTangent )
