"""
=============================================================================
MODULE: graph_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to manipulate the animation
curves.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel


class GraphUtils (object):

    @staticmethod
    def is_curve_selected():
        """
        Queries if any animation curve is selected.
        :return: True/False
        :rtype: bool
        """
        if cmd.animCurveEditor('graphEditor1GraphEd', query=True, acs=True):
            return True
        else:
            return False

    @staticmethod
    def count_selected_keys():
        """
        Counts all the selected keys
        :return: num_keys
        :rtype: int
        """
        num_keys = cmd.keyframe(q=True, kc=True, sl=True)
        return num_keys

    @staticmethod
    def list_anim_curves():
        """
        List the animation curves.
        :return: Animation Curves
        :rtype: list of str
        """
        num_keys = self.count_selected_keys()
        anim_curves = []

        if num_keys == 0:
            connections = cmd.listConnections(t='animCurve')
            if connections is None:
                connections = cmd.listConnections(t='mute')
        else:
            connections = cmd.keyframe(q=True, n=True, sl=True)

        for con in connections:
            if con.split('_')[0] == 'mute':
                anim_curves.append(con.replace('mute_', ''))
            else:
                anim_curves.append(con)

        return anim_curves

    @staticmethod
    def list_channels():
        """
        List the animation channels
        :return: Animation Channels
        :rtype: list of str
        """
        anim_curves = GraphUtils.list_anim_curves()
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
            if cmd.getAttr(attr_name) == 0:
                cmd.setAttr(attr_name, 3)
            elif cmd.getAttr(attr_name) == 3:
                cmd.setAttr(attr_name, 4)
            else:
                cmd.setAttr(attr_name, 0)

    @staticmethod
    def apply_euler_filter():
        """
        Applies the Euler Filter to the listed curves.
        """
        anim_curves = self.list_anim_curves()

        if anim_curves is None:
            return

        for curve in anim_curves:
            cmd.filterCurve(curve)

    @staticmethod
    def insert_key():
        """
        Inserts key on selected/all animation curves.
        """
        anim_curves = self.list_anim_curves()
        current_time = cmd.currentTime(q=True)
        cmd.setKeyframe(anim_curves, i=True, t=current_time)

    @staticmethod
    def toggle_buffer_curves():
        """
        Toggles buffer curves.
        """
        cmd.animCurveEditor('graphEditor1GraphEd', edit=True, sb='tgl')

    @staticmethod
    def toggle_infinity():
        """
        Toggles infinity curves.
        """
        cmd.animCurveEditor('graphEditor1GraphEd', edit=True, di='tgl')

    @staticmethod
    def delete_redundant(sel_objs, sel_attrs):
        pass

    @staticmethod
    def toggle_tangent_break():
        """
        Toggles tangents between Break/Unify Modes.
        """
        num_keys = self.count_selected_keys()
        if num_keys == 0:
            return
        sel_keys = cmd.keyTangent(q=True, l=True)
        cmd.keyTangent(l=not(sel_keys[0]))

    @staticmethod
    def toggle_tangent_weight():
        """
        Toggles tangents between Weighted/Non-Weighted tangents.
        """
        num_keys = self.count_selected_keys()
        if num_keys == 0:
            return
        sel_keys = cmd.keyTangent(q=True, wt=True)
        cmd.keyTangent(wt=not(sel_keys[0]))

    @staticmethod
    def toggle_view_modes():
        """
        Toggles view modes.
        """
        stacked_state = cmd.animCurveEditor('graphEditor1GraphEd', q=True, sc=True)
        normalized_state = cmd.animCurveEditor('graphEditor1GraphEd', q=True, dn=True)

        if normalized_state:
            if stacked_state:
                cmd.animCurveEditor('graphEditor1GraphEd', e=True, sc=False, dn=True)
            else:
                cmd.animCurveEditor('graphEditor1GraphEd', e=True, sc=False, dn=False)
        else:
            cmd.animCurveEditor('graphEditor1GraphEd', e=True, sc=True, dn=True)

    @staticmethod
    def toggle_tangents_visibility():
        """
        Toggles tangents visibility.
        """
        cmd.animCurveEditor('graphEditor1GraphEd', edit=True, dtn='tgl')

    @staticmethod
    def toggle_mute_channel():
        """
        Toggles mute/unmute channel
        """
        anim_channels = self.list_channels()
        mute_state = cmd.mute(anim_channels[0], q=True)

        for channel in anim_channels:
            if mute_state:
                cmd.mute(channel, d=True)
            else:
                cmd.mute(channel)



    def bake_channel(self, sel_objs, sel_attrs):
        pass


    def toggle_isolate_curve(self, sel_objs, sel_attrs):
        pass


    def toggle_template_channel(self):

        anim_curves = self.list_anim_curves()
        anim_channels = self.list_channels()
        mute_state = cmd.mute(anim_channels[0], q=True)

        template_state = cmd.getAttr(anim_curves[0] + '.ktv', l=True)

        # Template selected/all anim curves
        for curve in anim_curves:
            if (template_state):
                cmd.setAttr(curve + '.ktv', l=False)
                cmd.animCurveEditor('graphEditor1GraphEd', edit=True, dat='on')
            else:
                cmd.setAttr(curve + '.ktv', l=True)
                cmd.animCurveEditor('graphEditor1GraphEd', edit=True, dat='off')

        # Lock selected/all channels
        for channel in anim_channels:
            try:
                cmd.setAttr(channel, l=not(template_state))
            except:
                cmd.warning('Referenced attributes cannot be locked/unlocked')

    @staticmethod
    def swap_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def align_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def zero_out_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def converge_to_buffer(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def invert_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def push_and_pull(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def spread_squeeze_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def move_to_time(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def match_first_last_keys(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def key_all_keyed(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def build_dynamic_queue(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def copy_curve(self, sel_objs, sel_attrs):
        pass

    @staticmethod
    def paste_curve(self, sel_objs, sel_attrs):
        pass
