import maya.cmds as cmd
import maya.mel as mel
import maya.OpenMaya as om

from LaaScripts.Src.Python2.Constants import constants as c
from LaaScripts.Src.Python2.Utils import info_utils as info


class CurveTools(object):

    def __init__(self):
        pass

    def set_smart_key(self):
        mel.eval('ackSliceCurves;')
        info.show_info('Smart Key Set')

    def delete_redundant(self):
        mel.eval('ackDeleteRedundant;')
        info.show_info('Redundant Keys Deleted')

    def push_keys(self):
        mel.eval('ackPushPull "push";')
        info.show_info('Keys Pushed')

    def pull_keys(self):
        mel.eval('ackPushPull "pull";')
        info.show_info('Keys Pulled')

    def zero_out_keys(self):
        mel.eval('ackZeroOutKeys;')
        info.show_info('Keys set to Zero')

    def snap_to_buffer(self):
        mel.eval('ackConvergeBuffer "snap";')
        info.show_info('Snap to Buffer')

    def converge_to_buffer(self):
        mel.eval('ackConvergeBuffer "toward"')
        info.show_info('Towards Buffer')

    def diverge_from_buffer(self):
        mel.eval('ackConvergeBuffer "away"')
        info.show_info('Away from Buffer')

    def toggle_break_tangents(self):
        curves = cmd.keyframe(q=True, sl=True, name=True)
        for curve in curves:
            times = cmd.keyframe(curve, q=True, sl=True)
            for time in times:
                locked = cmd.keyTangent(curve, time=(time,), q=True, lock=True)[0]
                cmd.keyTangent(curve, time=(time,), e=True, lock=not locked)
                cmd.keyTangent(curve, time=(time,), e=True, lock=not locked)
                info.show_info('Break Tangents: {0}'.format(locked))

    def reverse_keys(self):
        sel = cmd.ls(selection=True)

        if cmd.scaleKey(attribute=True):
            keys = cmd.keyframe(sel, query=True, selected=True) or []
            attributes = cmd.keyframe(sel, query=True, selected=True, name=True) or []
            first_key = min(keys)
            last_key = max(keys)
            mid_pivot = (first_key + last_key) / 2
            for attribute in attributes:
                cmd.scaleKey(attribute, time=(first_key, last_key), timeScale=-1, timePivot=mid_pivot)
        else:
            channel_attributes = cmd.animCurveEditor('graphEditor1GraphEd', q=True, curvesShown=True)
            list_of_keys = []
            for attribute in channel_attributes:
                list_of_keys.extend(cmd.keyframe(attribute, query=True) or [])

            first_key = min(list_of_keys)
            last_key = max(list_of_keys)
            mid_pivot = (first_key + last_key) / 2
            for attribute in channel_attributes:
                cmd.scaleKey(attribute, time=(first_key, last_key), timeScale=-1, timePivot=mid_pivot)
        info.show_info('Keys Reversed')

    def toggle_infinity_modes(self):
        infinities = ["cycle", "cycleRelative", "constant"]
        infinitiesFromSelection = cmd.setInfinity(q=1, pri=1, poi=1)[0]
        om.MGlobal.displayInfo("Pre Infinity set to " + infinities[infinities.index(infinitiesFromSelection) - 1])
        cmd.setInfinity(pri=infinities[infinities.index(infinitiesFromSelection) - 1])
        cmd.setInfinity(poi=infinities[infinities.index(infinitiesFromSelection) - 1])
        info.show_info('Infinity Mode: {0}'.format(infinities[infinities.index(infinitiesFromSelection) - 1]))


if __name__ == '__main__':
    ct = CurveTools()
    ct.toggle_infinity_modes()
