# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: trigger.py
-----------------------------------------------------------------------------
This is an intermidiate module that triggers all the user actions.
That´s the module that need to be imported when the user defines
a hotkey.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2022+ | Python 3
=============================================================================
"""
from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Core import Keyframing
from LaaScripts.Src.Core import Navigation
from LaaScripts.Src.Core import Playback
from LaaScripts.Src.Core import Prefs
from LaaScripts.Src.Core import Viewport
from LaaScripts.Src.Utils.panel_utils import PanelUtils
from LaaScripts.Src.Data.user_data import UserData

global LAA_FRAME_MARKER
global LAA_TIMELINE_SECTION


class Trigger(object):

    def __init__(self):
        super(Trigger, self).__init__()

        self._prefs_manager = Prefs.prefs_manager.PrefsManager()
        self._hotkey_manager = Prefs.hotkey_manager.HotkeyManager()
        self._channels_filter = Navigation.channels_filter.ChannelsFilter()
        self._smart_manipulator = Navigation.smart_manipulator.SmartManipulator()
        self._retiming_tools = Keyframing.retiming_tools.RetimingTools()
        self._blending_tools = Keyframing.blending_tools.BlendingTools()
        self._baking_tools = Keyframing.baking_tools.BakingTools()
        self._playback_manager = Playback.playback_manager.PlaybackManager()
        self._frame_marker = Playback.frame_marker.FrameMarker()
        self._timeline_section = Playback.timeline_section.TimelineSection()
        self._viewport_manager = Viewport.viewport_manager.ViewportManager()

        self._user_data = UserData()

    # =========================================================================
    # PREFS
    # =========================================================================
    def set_stepped_tangents(self):
        self._prefs_manager.set_tangents('linear', 'step')

    def set_linear_tangents(self):
        self._prefs_manager.set_tangents('linear', 'linear')

    def set_auto_tangents(self):
        self._prefs_manager.set_tangents('auto', 'auto')

    def toggle_timeline_height(self):
        self._prefs_manager.toggle_timeline_height()

    def set_timeline_height_1x(self):
        self._prefs_manager.set_timeline_height(32)

    def set_timeline_height_2x(self):
        self._prefs_manager.set_timeline_height(64)

    def set_timeline_height_4x(self):
        self._prefs_manager.set_timeline_height(128)

    def toggle_hotkey_sets(self):
        self._hotkey_manager.toggle_hotkey_sets()

    def clear_hotkey(self, hotkey):
        self._hotkey_manager.clear_hotkey(hotkey)

    def is_hotkey_assigned(self, hotkey):
        return self._hotkey_manager.is_hotkey_assigned(hotkey)

    def get_command_from_hotkey(self, hotkey):
        self._hotkey_manager.get_command_from_hotkey(hotkey)

    def create_hotkey(self, name, command, annotation, hotkey):
        self._hotkey_manager.create_hotkey(name, command, annotation, hotkey)

    # =========================================================================
    # NAVIGATION
    # =========================================================================
    def smart_translate_manipulator(self):
        self._smart_manipulator.smart_translate_manipulator()

    def smart_rotate_manipulator(self):
        self._smart_manipulator.smart_rotate_manipulator()

    def smart_scale_manipulator(self):
        self._smart_manipulator.smart_scale_manipulator()

    def filter_translate_channels_on_ones(self):
        self._channels_filter.filter_translate_channels_on_ones()

    def filter_translate_channels_on_twos(self):
        self._channels_filter.filter_translate_channels_on_twos()

    def filter_translate_channels(self):
        self._channels_filter.filter_translate_channels()

    def filter_rotate_channels_on_ones(self):
        self._channels_filter.filter_rotate_channels_on_ones()

    def filter_rotate_channels_on_twos(self):
        self._channels_filter.filter_rotate_channels_on_twos()

    def filter_rotate_channels(self):
        self._channels_filter.filter_rotate_channels()

    def filter_scale_channels_on_ones(self):
        self._channels_filter.filter_scale_channels_on_ones()

    def filter_scale_channels_on_twos(self):
        self._channels_filter.filter_scale_channels_on_twos()

    def filter_scale_channels(self):
        self._channels_filter.filter_scale_channels()

    def filter_all_channels(self):
        self._channels_filter.filter_all_channels()

    def select_all_channels(self):
        self._channels_filter.select_all_channels()

    def clear_all_channels(self):
        self._channels_filter.clear_all_channels()

    def toggle_sync_mode(self):
        self._channels_filter.toggle_sync_mode()

    # =========================================================================
    # KEYFRAMING
    # =========================================================================
    def tween(self, value, mode):
        self._blending_tools.tween(value, mode)

    def push_prev_key(self):
        self._retiming_tools.push_prev_key()

    def push_next_key(self):
        self._retiming_tools.push_next_key()

    def push_prev_keys(self):
        self._retiming_tools.push_prev_keys()

    def push_next_keys(self):
        self._retiming_tools.push_next_keys()

    def pull_prev_key(self):
        self._retiming_tools.pull_prev_key()

    def pull_next_key(self):
        self._retiming_tools.pull_next_key()

    def pull_prev_keys(self):
        self._retiming_tools.pull_prev_keys()

    def pull_next_keys(self):
        self._retiming_tools.pull_next_keys()

    def add_inbetween(self, time_increment=1):
        self._retiming_tools.add_inbetween(time_increment)

    def remove_inbetween(self, time_increment=1):
        self._retiming_tools.remove_inbetween(time_increment)

    def copy_keys(self):
        self._retiming_tools.copy_keys()

    def cut_keys(self):
        self._retiming_tools.cut_keys()

    def paste_keys(self):
        self._retiming_tools.paste_keys()

    def bake_on_ones(self):
        self._baking_tools.bake_on_ones()

    def key_on_markers(self):
        self._baking_tools.key_on_markers()

    def bake_on_markers(self):
        self._baking_tools.bake_on_markers()

    def key_on_key_markers(self):
        self._baking_tools.key_on_key_markers(True)

    def bake_on_key_markers(self):
        self._baking_tools.bake_on_key_markers(True)

    def rebuild_on_twos(self):
        self._baking_tools.rebuild(2)

    def rebuild_on_fours(self):
        self._baking_tools.rebuild(4)

    def set_smart_key(self):
        self._retiming_tools.set_smart_key()


    # =========================================================================
    # VIEWPORT
    # =========================================================================
    def toggle_xray(self):
        self._viewport_manager.toggle_xray()

    def toggle_wireframe(self):
        self._viewport_manager.toggle_wireframe()

    def toggle_default_material(self):
        self._viewport_manager.toggle_default_material()

    def toggle_cameras(self):
        self._viewport_manager.toggle_cameras()

    def toggle_grid(self):
        self._viewport_manager.toggle_grid()

    def toggle_plane(self):
        self._viewport_manager.toggle_plane()

    def toggle_joints(self):
        self._viewport_manager.toggle_joints()

    def toggle_lights(self):
        self._viewport_manager.toggle_lights()

    def toggle_locators(self):
        self._viewport_manager.toggle_locators()

    def toggle_handles(self):
        self._viewport_manager.toggle_handles()

    def toggle_curves(self):
        self._viewport_manager.toggle_curves()

    def toggle_polygons(self):
        self._viewport_manager.toggle_polygons()

    def toggle_all_viewport_elements(self):
        self._viewport_manager.toggle_all_viewport_elements()

    # =========================================================================
    # PLAYBACK
    # =========================================================================
    def go_to_the_next_frame(self):
        self._playback_manager.go_to_the_next_frame()

    def go_to_the_prev_frame(self):
        self._playback_manager.go_to_the_prev_frame()

    def next_frame_playback_press(self):
        self._playback_manager.next_frame_playback_press()

    def prev_frame_playback_press(self):
        self._playback_manager.prev_frame_playback_press()

    def next_frame_playback_release(self):
        self._playback_manager.next_frame_playback_release()

    def prev_frame_playback_release(self):
        self._playback_manager.prev_frame_playback_release()

    def go_to_the_next_key(self):
        self._playback_manager.go_to_the_next_key()

    def go_to_the_prev_key(self):
        self._playback_manager.go_to_the_prev_key()

    def go_to_the_next_marker(self):
        self._playback_manager.go_to_the_next_marker(c.PLAYBACK.ALL)

    def go_to_the_prev_marker(self):
        self._playback_manager.go_to_the_prev_marker(c.PLAYBACK.ALL)

    def go_to_the_next_key_marker(self):
        self._playback_manager.go_to_the_next_marker(c.PLAYBACK.KEY)

    def go_to_the_prev_key_marker(self):
        self._playback_manager.go_to_the_prev_marker(c.PLAYBACK.KEY)

    def load_frame_markers(self):
        global LAA_FRAME_MARKER

        try:
            LAA_FRAME_MARKER.setParent(None)
            LAA_FRAME_MARKER.deleteLater()
            LAA_FRAME_MARKER = None
        except NameError:
            pass

        LAA_FRAME_MARKER = self._frame_marker
        LAA_FRAME_MARKER.setVisible(True)

    def add_key_markers(self):
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.KEY)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.KEY)

    def add_breakdown_markers(self):
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.BREAKDOWN)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.BREAKDOWN)

    def add_inbetween_markers(self):
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.INBETWEEN)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.PLAYBACK.INBETWEEN)

    def remove_frame_markers(self):
        try:
            LAA_FRAME_MARKER.remove_frame_markers()
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.remove_frame_markers()

    def load_timeline_sections(self):
        global LAA_TIMELINE_SECTION

        try:
            LAA_TIMELINE_SECTION.setParent(None)
            LAA_TIMELINE_SECTION.deleteLater()
            LAA_TIMELINE_SECTION = None
        except NameError:
            pass

        LAA_TIMELINE_SECTION = self._timeline_section
        LAA_TIMELINE_SECTION.setVisible(True)

    def add_timeline_section(self, random_color=False):
        try:
            LAA_TIMELINE_SECTION.add_timeline_section(random_color)
        except NameError:
            Trigger.load_timeline_sections(self)
            LAA_TIMELINE_SECTION.add_timeline_section(random_color)

    def remove_timeline_section(self):
        try:
            LAA_TIMELINE_SECTION.remove_timeline_section()
        except NameError:
            Trigger.load_timeline_sections(self)
            LAA_TIMELINE_SECTION.remove_timeline_section()
