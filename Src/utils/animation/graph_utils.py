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
from collections import namedtuple

Key = namedtuple('Key', 'current_key prev_key next_key anim_curve')


class GraphUtils(object):

    @staticmethod
    def get_all_selected_curves():
        """
        Get all the selected animation curves from the graph editor.
        :return: A list of animation curves
        :rtype: list[str]
        """
        return cmd.keyframe(query=True, name=True, selected=True) or []

    @staticmethod
    def count_all_selected_keys():
        """
        Count all the selected keys from the graph editor.
        :return: Number of selected keys
        :rtype: int
        """
        return cmd.keyframe(query=True, keyframeCount=True, selected=True)

    @staticmethod
    def count_selected_keys_in_curve(anim_curve):
        """
        Count all the selected keys in a specific animation curve.
        :return: Number of selected keys in a curve
        :rtype: int
        """
        return cmd.keyframe(anim_curve, query=True, keyframeCount=True, selected=True)

    @staticmethod
    def get_all_keys_from_curve(anim_curve):
        """
        Get all keys from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key indexes
        :rtype: list[int]
        """
        return cmd.keyframe(anim_curve, query=True, indexValue=True)

    @staticmethod
    def get_selected_keys_from_curve(anim_curve):
        """
        Get selected keys from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key indexes
        :rtype: list[int]
        """
        return cmd.keyframe(anim_curve, query=True, indexValue=True, selected=True)

    @staticmethod
    def get_all_keys_times_from_curve(anim_curve):
        """
        Get all key times from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key times
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, timeChange=True)

    @staticmethod
    def get_selected_keys_times_from_curve(anim_curve):
        """
        Get selected key times from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key times
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, timeChange=True, selected=True)

    @staticmethod
    def get_all_key_values_from_curve(anim_curve):
        """
        Get all key values from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key values
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, valueChange=True)

    @staticmethod
    def get_selected_key_values_from_curve(anim_curve):
        """
        Get selected key values from a specific animation curve.
        :param anim_curve: Animation curve
        :return: List of key values
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, valueChange=True, selected=True)

    @staticmethod
    def get_time_from_key(anim_curve, key_index):
        """
        Get the key time from a specified key index.
        :param str anim_curve: Animation curve
        :param int key_index: Key index in a curve
        :return: List of key times
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, index=(key_index, key_index), timeChange=True)[0]

    @staticmethod
    def get_value_from_key(anim_curve, key_index):
        """
        Get the key value from a specified key index.
        :param str anim_curve: Animation curve
        :param int key_index: Key index in a curve
        :return: List of key values
        :rtype: list[float]
        """
        return cmd.keyframe(anim_curve, query=True, index=(key_index, key_index), valueChange=True)[0]

    @staticmethod
    def get_index_from_time(anim_curve, key_time):
        """
        Get the key index from a specified key time.
        :param str anim_curve: Animation curve
        :param int key_time: Key time in a curve
        :return: List of key indexes
        :rtype: list[int]
        """
        return cmd.keyframe(anim_curve, query=True, time=(key_time, key_time), indexValue=True)[0]

    @staticmethod
    def get_default_value_from_curve(curve):
        obj = curve.split('_')[0]
        attr = curve.split('_')[1]
        return cmd.attributeQuery(attr, node=obj, listDefault=True)[0] or 0.0

    @staticmethod
    def get_keys_after_current_index(anim_curve, key_index):
        """
        Get all deselected keys after the specified key index.
        :param str anim_curve: Animation curve
        :param int key_index: Key index
        :return: List of deselected key indexes
        :rtype: list[int]
        """
        all_keys = GraphUtils.get_all_keys_from_curve(anim_curve)

        return [key for key in all_keys if key > key_index and not GraphUtils.is_key_selected(anim_curve, key)]

    @staticmethod
    def get_keys_before_current_index(anim_curve, key_index):
        """
        Get all deselected keys before the specified key index.
        :param str anim_curve: Animation curve
        :param int key_index: Key index
        :return: List of deselected key indexes
        :rtype: list[int]
        """
        all_keys = GraphUtils.get_all_keys_from_curve(anim_curve)

        return [key for key in all_keys if key < key_index and not GraphUtils.is_key_selected(anim_curve, key)]

    @staticmethod
    def get_prev_key_on_curve(anim_curve, key_index):
        key_time = GraphUtils.get_time_from_key_index(anim_curve, key_index)
        prev_key_time = cmd.findKeyframe(anim_curve, time=(key_time, key_time), which="previous")
        if prev_key_time == key_time:
            return None
        return GraphUtils.get_index_from_key_time(anim_curve, prev_key_time)

    @staticmethod
    def get_next_key_time_on_curve(anim_curve, key_time):
        next_key_time = cmd.findKeyframe(anim_curve, time=(key_time, key_time), which="next")
        if next_key_time == key_time:
            return None
        return next_key_time

    @staticmethod
    def get_prev_key_time_on_curve(anim_curve, key_time):
        prev_key_time = cmd.findKeyframe(anim_curve, time=(key_time, key_time), which="previous")
        if prev_key_time == key_time:
            return None
        return prev_key_time

    @staticmethod
    def is_key_selected(anim_curve, key_index):
        """
        Check if a specified key_index is selected.
        :param str anim_curve: Animation curve
        :param int key_index: Key index
        :return: True if key is selected, False if not
        :rtype: bool
        """
        selected_keys = GraphUtils.get_selected_keys_from_curve(anim_curve)
        return True if key_index in selected_keys else False

    @staticmethod
    def get_key_data_from_curve(anim_curve, key_index):
        selected = GraphUtils.is_key_selected(anim_curve, key_index)
        if not selected:
            return None
        all_keys = GraphUtils.get_all_keys_from_curve(anim_curve)
        time = GraphUtils.get_time_from_key(anim_curve, key_index)
        value = GraphUtils.get_value_from_key(anim_curve, key_index)
        keys_after = GraphUtils.get_keys_after_current_index(anim_curve, key_index)
        keys_before = GraphUtils.get_keys_before_current_index(anim_curve, key_index)

        next_key = min(keys_after) if keys_after else None
        prev_key = max(keys_before) if keys_before else None

        if next_key:
            next_key = next_key
            next_time = GraphUtils.get_time_from_key(anim_curve, next_key)
            next_value = GraphUtils.get_value_from_key(anim_curve, next_key)
        else:
            next_key = all_keys[-1]
            next_time = GraphUtils.get_time_from_key(anim_curve, all_keys[-1])
            next_value = GraphUtils.get_value_from_key(anim_curve, all_keys[-1])

        if prev_key:
            prev_key = prev_key
            prev_time = GraphUtils.get_time_from_key(anim_curve, prev_key)
            prev_value = GraphUtils.get_value_from_key(anim_curve, prev_key)
        else:
            prev_key = all_keys[0]
            prev_time = GraphUtils.get_time_from_key(anim_curve, all_keys[0])
            prev_value = GraphUtils.get_value_from_key(anim_curve, all_keys[0])

        key = Key(
            current_key=[key_index, time, value],
            prev_key=[prev_key, prev_time, prev_value],
            next_key=[next_key, next_time, next_value],
            anim_curve=anim_curve
        )

        return key

    @staticmethod
    def get_graph_outliner():
        return cmd.editor('graphEditor1GraphEd', q=True, mainListConnection=True)

    @staticmethod
    def get_selection_from_outliner():
        return cmd.selectionConnection('graphEditor1FromOutliner', q=True, object=True)

    @staticmethod
    def get_selected_key_tangents():
        return cmd.keyTangent(q=True, ott=True)

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
    def list_selected_keys():
        """
        Counts all the selected keys
        :return: num_keys
        :rtype: int
        """
        selected_keys = []
        selected_curves = GraphUtils.list_selected_anim_curves()
        for curve in selected_curves:
            selected_keys.append(cmd.keyframe(curve, q=True, iv=True, sl=True))
        return selected_keys

    @staticmethod
    def list_selected_keys_from_curve():
        pass

    # key_indexes = cmd.keyframe(curve, q=True, iv=True, sl=True)
    # key_times = cmd.keyframe(curve, q=True, tc=True, sl=True)
    # key_values = cmd.keyframe(curve, q=True, vc=True, sl=True)
    # times = GraphUtils.list_selected_key_values()
    # # print('{0}: {1}'.format(curve, key_indexes))
    # # print('{0}: {1}'.format(curve, key_times))
    # # print('{0}: {1}'.format(curve, key_values))
    # for index in key_indexes:
    #     cur_key = cmd.keyframe(curve, query=True, index=(index, index), timeChange=True)[0]
    #     next_key = cmd.findKeyframe(curve, time=(cur_key, cur_key), which="next")
    #     print('{0}: {1}'.format(cur_key, next_key))

    @staticmethod
    def list_selected_key_values():
        """
        Counts all the selected keys
        :return: num_keys
        :rtype: int
        """
        key_times = cmd.keyframe(query=True, timeChange=True)
        key_times = []
        selected_curves = GraphUtils.list_selected_anim_curves()
        for curve in selected_curves:
            times.append(cmd.keyframe(curve, q=True, tc=True))
            print(cmd.keyframe(curve, q=True, index=(i, i)[0]))
        return key - times

    @staticmethod
    def list_selected_anim_curves():
        return cmd.keyframe(query=True, name=True, selected=True) or []

    @staticmethod
    def list_selected_anim_channels():
        return GraphUtils.get_selection_from_outliner() or []

    @staticmethod
    def list_anim_curves():
        """
        List the animation curves.
        :return: Animation Curves
        :rtype: list of str
        """
        num_keys = GraphUtils.count_selected_keys()

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

        if anim_curves is None:
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
        cmd.keyTangent(l=not (sel_keys[0]))

    @staticmethod
    def toggle_tangent_weight():
        """
        Toggles tangents between Weighted/Non-Weighted tangents.
        """
        num_keys = self.count_selected_keys()
        if num_keys == 0:
            return
        sel_keys = cmd.keyTangent(q=True, wt=True)
        cmd.keyTangent(wt=not (sel_keys[0]))

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
                cmd.setAttr(channel, l=not (template_state))
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


if __name__ == '__main__':
    anim_curves = GraphUtils.list_selected_anim_channels()
    print(anim_curves)
    # for curve in anim_curves:
    #     selected_keys = GraphUtils.list_selected_keys()
    #     print(selected_keys)
    # print(GraphUtils.list_selected_keys())
