# =============================================================================
# SCRIPT: Blending Tools v1.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Loops through all hotkey sets.
# =============================================================================
import maya.cmds as cmd
from LaaScripts.Src.Python3.Utils import info_utils as info


class BlendingTools(object):

    def __init__(self):
        pass

    def tween(self, percentage, obj=None, attrs=None, selection=True):

        if not obj and not selection:
            raise ValueError("No object given to tween")

        if not obj:
            obj = cmds.ls(sl=1)[0]

        if not attrs:
            attrs = cmds.listAttr(obj, keyable=True)

        currentTime = cmds.currentTime(query=True)

        for attr in attrs:
            attrFull = '%s.%s' % (obj, attr)
            keyframes = cmds.keyframe(attrFull, query=True)

            if not keyframes:
                continue

            previousKeyframes = []

            for k in keyframes:
                if k < currentTime:
                    previousKeyframes.append(k)

            laterKeyframes = [frame for frame in keyframes if frame > currentTime]

            if not previousKeyframes and not laterKeyframes:
                continue

            if previousKeyframes:
                previousFrame = max(previousKeyframes)
            else:
                previousFrame = None

            nextFrame = min(laterKeyframes) if laterKeyframes else None

            if previousFrame is None:
                previousFrame = nextFrame

            nextFrame = previousFrame if nextFrame is None else nextFrame
            previousValue = cmds.getAttr(attrFull, time=previousFrame)
            nextValue = cmds.getAttr(attrFull, time=nextFrame)

            if nextFrame is None:
                currentValue = previousValue
            elif previousFrame is None:
                currentValue = nextValue
            elif previousValue == nextValue:
                currentValue = previousValue
            else:
                difference = nextValue - previousValue
                biasedDifference = (difference * percentage) / 100.0
                currentValue = previousValue + biasedDifference

            cmds.setAttr(attrFull, currentValue)
            cmds.setKeyframe(attrFull, time=currentTime, value=currentValue)


if __name__ == '__main__':
    bt = BlendingTools()
    bt.tween(25.0)
