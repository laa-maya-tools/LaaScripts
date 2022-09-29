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


class GraphTools (object):

    # -----------------------------------------------------------------------------
    # Reads the corresponding Json file for the active character. Returns a dict
    # with the character controls hierarchy
    # -----------------------------------------------------------------------------
    def __init__(self, hotkey):

        self.perform_hotkey_action(hotkey)

    # -----------------------------------------------------------------------------
    # Rerturn True if at least one animation curve is selected
    # -----------------------------------------------------------------------------
    def perform_hotkey_action(self, hotkey):

        if (hotkey == 'alt_i'):
            self.toggle_infinity()
        if (hotkey == 'alt_f'):
            self.toggle_buffer_curves()
        if (hotkey == 'alt_v'):
            self.toggle_view_modes()
        if (hotkey == 'alt_s'):
            self.insert_key()
        if (hotkey == 'alt_a'):
            self.toggle_infinity_cycle('pre')
        if (hotkey == 'alt_d'):
            self.toggle_infinity_cycle('pst')
        if (hotkey == 'alt_e'):
            self.apply_euler_filter()
        if (hotkey == 'alt_b'):
            self.toggle_tangent_break()
        if (hotkey == 'alt_w'):
            self.toggle_tangent_weight()
        if (hotkey == 'alt_m'):
            self.toggle_mute_channel()
        if (hotkey == 'alt_t'):
            self.toggle_template_channel()
        if (hotkey == 'alt_1'):
            self.set_tangent_type('step')
        if (hotkey == 'alt_2'):
            self.set_tangent_type('linear')
        if (hotkey == 'alt_3'):
            self.set_tangent_type('auto')
        if (hotkey == 'alt_4'):
            self.set_tangent_type('spline')
        if (hotkey == 'alt_5'):
            self.set_tangent_type('flat')

    # -----------------------------------------------------------------------------
    # Rerturn True if at least one animation curve is selected
    # -----------------------------------------------------------------------------
    def is_curve_selected(self):

        if (cmds.animCurveEditor('graphEditor1GraphEd', query=True, acs=True)):
            return True
        else:
            return False

    # -----------------------------------------------------------------------------
    # Count the number of selected keys
    # -----------------------------------------------------------------------------
    def count_selected_keys(self):

        num_keys = cmds.keyframe(q=True, kc=True, sl=True)
        return num_keys

    # -----------------------------------------------------------------------------
    # List Selected/All Animation Curves
    # -----------------------------------------------------------------------------
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

    # -----------------------------------------------------------------------------
    # List Selected/All Channels
    # -----------------------------------------------------------------------------
    def list_channels(self):

        # List anim curves
        anim_curves = self.list_anim_curves()
        anim_channels = []

        for curve in anim_curves:
            obj = curve.split('_')[0]
            attr = curve.split('_')[-1]
            anim_channels.append(obj + '.' + attr)

        return anim_channels

    # -----------------------------------------------------------------------------
    # Toggle Pre/Post Infinity Cycle Modes
    # -----------------------------------------------------------------------------
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

    # -----------------------------------------------------------------------------
    # Cycle Tangent Type
    # -----------------------------------------------------------------------------
    def cycle_tangent_type(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Apply Euler Filter
    # -----------------------------------------------------------------------------
    def apply_euler_filter(self):

        anim_curves = self.list_anim_curves()

        if anim_curves == None:
            return

        for curve in anim_curves:
            cmds.filterCurve(curve)

    # -----------------------------------------------------------------------------
    # Insert key on selected/all animation curves
    # -----------------------------------------------------------------------------
    def insert_key(self):

        anim_curves = self.list_anim_curves()
        cur_time = cmds.currentTime(q=True)
        cmds.setKeyframe(anim_curves, i=True, t=cur_time)

    # -----------------------------------------------------------------------------
    # Toggle Buffer Curves
    # -----------------------------------------------------------------------------
    def toggle_buffer_curves(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, sb='tgl')

    # -----------------------------------------------------------------------------
    # Toggle Infinity
    # -----------------------------------------------------------------------------
    def toggle_infinity(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, di='tgl')

    # -----------------------------------------------------------------------------
    # Delete Redundant
    # -----------------------------------------------------------------------------
    def delete_redundant(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Toggle Tangents between Break/Unify Mode
    # -----------------------------------------------------------------------------
    def toggle_tangent_break(self):

        num_keys = self.count_selected_keys()

        if (num_keys == 0):
            return

        sel_keys = cmds.keyTangent(q=True, l=True)

        cmds.keyTangent(l=not(sel_keys[0]))

    # -----------------------------------------------------------------------------
    # Toggle Tangent Mode between Break/Unify and Weighted/NonWeighted
    # -----------------------------------------------------------------------------
    def toggle_tangent_weight(self):

        num_keys = self.count_selected_keys()

        if (num_keys == 0):
            return

        sel_keys = cmds.keyTangent(q=True, wt=True)

        cmds.keyTangent(wt=not(sel_keys[0]))

    # -----------------------------------------------------------------------------
    # Toggle View Modes
    # -----------------------------------------------------------------------------
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

    # -----------------------------------------------------------------------------
    # Toggle Tangents Visibility
    # -----------------------------------------------------------------------------
    def toggle_tangents_visibility(self):

        cmds.animCurveEditor('graphEditor1GraphEd', edit=True, dtn='tgl')

    # -----------------------------------------------------------------------------
    # Toggle Mute Channel
    # -----------------------------------------------------------------------------
    def toggle_mute_channel(self):

        anim_channels = self.list_channels()
        mute_state = cmds.mute(anim_channels[0], q=True)

        for channel in anim_channels:
            if (mute_state):
                cmds.mute(channel, d=True)
            else:
                cmds.mute(channel)

    # -----------------------------------------------------------------------------
    # Bake Channel
    # -----------------------------------------------------------------------------
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

        # -----------------------------------------------------------------------------
        # Bake Channel
        # -----------------------------------------------------------------------------
    def bake_channel(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Toggle Isolate Curve
    # -----------------------------------------------------------------------------
    def toggle_isolate_curve(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Toggle Lock Channel
    # -----------------------------------------------------------------------------
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

    # -----------------------------------------------------------------------------
    # Swap Keys
    # -----------------------------------------------------------------------------
    def swap_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Align Keys
    # -----------------------------------------------------------------------------
    def align_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Zero Out Keys
    # -----------------------------------------------------------------------------
    def zero_out_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Converge to Buffer
    # -----------------------------------------------------------------------------
    def converge_to_buffer(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Invert Keys
    # -----------------------------------------------------------------------------
    def invert_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Push and Pull
    # -----------------------------------------------------------------------------
    def push_and_pull(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Spread Squeeze Keys
    # -----------------------------------------------------------------------------
    def spread_squeeze_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Move to Time
    # -----------------------------------------------------------------------------
    def move_to_time(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Match First Last Keys
    # -----------------------------------------------------------------------------
    def match_first_last_keys(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Key All Keyed
    # -----------------------------------------------------------------------------
    def key_all_keyed(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Build Dynamic Queue
    # -----------------------------------------------------------------------------
    def build_dynamic_queue(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Copy Curve
    # -----------------------------------------------------------------------------
    def copy_curve(self, sel_objs, sel_attrs):
        pass

    # -----------------------------------------------------------------------------
    # Paste Curve
    # -----------------------------------------------------------------------------
    def paste_curve(self, sel_objs, sel_attrs):
        pass

