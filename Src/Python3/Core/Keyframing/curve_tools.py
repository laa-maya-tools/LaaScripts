# -----------------------------------------------------------------------------
# SCRIPT: keyframe_manager v2.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Queries the Hotkey pressed and decide with action to perform based on the
# current selection. It uses the Graph Tools if an animation curve is
# selected, the ChannelBox Tools if an attribute is selected or the Timeline
# Tools if the timeline is on focus.
# -----------------------------------------------------------------------------

import maya.cmds as cmds
import maya.mel as mel


class CurveTools (object):

    def __init__(self):
        pass

    def is_curve_selected(self):

        if (cmds.animCurveEditor('graphEditor1GraphEd', query=True, acs=True)):
            return True
        else:
            return False

    def count_selected_keys(self):

        num_keys = cmds.keyframe(q=True, kc=True, sl=True)
        return num_keys

    def list_anim_curves(self):

        # Get selected number of keys
        num_keys = self.count_selected_keys()
        anim_curves = []

        # If no keys are selected, get all anim curves
        if (num_keys == 0):
            connections = cmds.listConnections(t='animCurve')

            # If channels are muted
            if (connections == None):
                connections = cmds.listConnections(t='mute')

        # Get the anim curves from the selected keys
        else:
            connections = cmds.keyframe(q=True, n=True, sl=True)

        for con in connections:
            if (con.split('_')[0] == 'mute'):
                anim_curves.append(con.replace('mute_', ''))
            else:
                anim_curves.append(con)

        return anim_curves

    def list_channels(self):

        # List anim curves
        anim_curves = self.list_anim_curves()
        anim_channels = []

        for curve in anim_curves:
            obj = curve.split('_')[0]
            attr = curve.split('_')[-1]
            anim_channels.append(obj + '.' + attr)

        return anim_channels

    def toggle_infinity_cycle(self, mode):

        anim_curves = self.list_anim_curves()

        if anim_curves == None:
            return

        for curve in anim_curves:
            attr_name = curve + '.' + mode
            if cmds.getAttr(attr_name) == 0:
                cmds.setAttr(attr_name, 3)
            elif cmds.getAttr(attr_name) == 3:
                cmds.setAttr(attr_name, 4)
            else:
                cmds.setAttr(attr_name, 0)

    def cycle_tangent_type(self, sel_objs, sel_attrs):
        pass

    def apply_euler_filter(self):

        anim_curves = self.list_anim_curves()

        if anim_curves == None:
            return

        for curve in anim_curves:
            cmds.filterCurve(curve)

    def insert_key(self):

        anim_curves = self.list_anim_curves()
        cur_time = cmds.currentTime(q=True)
        cmds.setKeyframe(anim_curves, i=True, t=cur_time)

    def toggle_buffer_curves(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, sb='tgl')

    def toggle_infinity(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, di='tgl')

    def delete_redundant(self, sel_objs, sel_attrs):
        pass

    def toggle_tangent_break(self):

        num_keys = self.count_selected_keys()

        if (num_keys == 0):
            return

        sel_keys = cmds.keyTangent(q=True, l=True)

        cmds.keyTangent(l=not(sel_keys[0]))

    def toggle_tangent_weight(self):

        num_keys = self.count_selected_keys()

        if (num_keys == 0):
            return

        sel_keys = cmds.keyTangent(q=True, wt=True)

        cmds.keyTangent(wt=not(sel_keys[0]))

    def toggle_view_modes(self):

        stacked_state = cmds.animCurveEditor('graphEditor1GraphEd', q=True, sc=True)
        normalized_state = cmds.animCurveEditor('graphEditor1GraphEd', q=True, dn=True)

        if normalized_state:
            if stacked_state:
                cmds.animCurveEditor('graphEditor1GraphEd', e=True, sc=False, dn=True)
            else:
                cmds.animCurveEditor('graphEditor1GraphEd', e=True, sc=False, dn=False)
        else:
            cmds.animCurveEditor('graphEditor1GraphEd', e=True, sc=True, dn=True)

    def toggle_tangents_visibility(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, dtn='tgl')

    def toggle_mute_channel(self):

        anim_channels = self.list_channels()
        mute_state = cmds.mute(anim_channels[0], q=True)

        for channel in anim_channels:
            if (mute_state):
                cmds.mute(channel, d=True)
            else:
                cmds.mute(channel)

    def set_tangent_type(self, tangent_type):

        print(tangent_type)

        # num_keys = self.count_selected_keys()
        # selection = cmds.ls(sl=True)
        # print num_keys, selection, tangent_type

        # if (num_keys == 0):
        #     pass
        # else:
        #     cur = cmds.keyTangent(q=True, l=True)
        #     cmds.keyTangent(selection, itt=tangent_type, ott=tangent_type)

    def bake_channel(self, sel_objs, sel_attrs):
        pass

    def toggle_isolate_curve(self, sel_objs, sel_attrs):
        pass

    def toggle_template_channel(self):

        anim_curves = self.list_anim_curves()
        anim_channels = self.list_channels()
        mute_state = cmds.mute(anim_channels[0], q=True)

        template_state = cmds.getAttr(anim_curves[0] + '.ktv', l=True)

        # Template selected/all anim curves
        for curve in anim_curves:
            if (template_state):
                cmds.setAttr(curve + '.ktv', l=False)
                cmds.animCurveEditor('graphEditor1GraphEd', edit=True, dat='on')
            else:
                cmds.setAttr(curve + '.ktv', l=True)
                cmds.animCurveEditor('graphEditor1GraphEd', edit=True, dat='off')

        # Lock selected/all channels
        for channel in anim_channels:
            try:
                cmds.setAttr(channel, l=not(template_state))
            except:
                cmds.warning('Referenced attributes cannot be locked/unlocked')

    def swap_keys(self, sel_objs, sel_attrs):
        pass

    def align_keys(self, sel_objs, sel_attrs):
        pass

    def zero_out_keys(self, sel_objs, sel_attrs):
        pass

    def converge_to_buffer(self, sel_objs, sel_attrs):
        pass

    def invert_keys(self, sel_objs, sel_attrs):
        pass

    def push_and_pull(self, sel_objs, sel_attrs):
        pass

    def spread_squeeze_keys(self, sel_objs, sel_attrs):
        pass

    def move_to_time(self, sel_objs, sel_attrs):
        pass

    def match_first_last_keys(self, sel_objs, sel_attrs):
        pass

    def key_all_keyed(self, sel_objs, sel_attrs):
        pass

    def build_dynamic_queue(self, sel_objs, sel_attrs):
        pass

    def copy_curve(self, sel_objs, sel_attrs):
        pass

    def paste_curve(self, sel_objs, sel_attrs):
        pass

