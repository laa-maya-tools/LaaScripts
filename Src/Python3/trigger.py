# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: trigger_bck.py
-----------------------------------------------------------------------------
This is an intermidiate module that triggers all the user actions.
That´s the module that need to be imported when the user defines
a hotkey.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2022 | Python 3
=============================================================================
"""
import maya.cmds as cmd
from PySide2 import QtCore as cor

from LaaScripts.Src.Python3.Core import Navigation
from LaaScripts.Src.Python3.Core import Keyframing
from LaaScripts.Src.Python3.Core import Playback
from LaaScripts.Src.Python3.Core import Prefs
from LaaScripts.Src.Python3.Core import Viewport
from LaaScripts.Src.Python3.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Python3.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Python3.Constants import constants as c

global LAA_FRAME_MARKER
global LAA_TIMELINE_SECTION


class Trigger(object):

    def __init__(self):
        super(Trigger, self).__init__()

        self._smart_manipulator = Navigation.smart_manipulator.SmartManipulator()
        self._channels_filter = Navigation.channels_filter.ChannelsFilter()
        self._retiming_tools = Keyframing.retiming_tools.RetimingTools()
        self._playback_manager = Playback.playback_manager.PlaybackManager()
        self._frame_marker = Playback.frame_marker.FrameMarker()
        self._timeline_section = Playback.timeline_section.TimelineSection()
        self._hotkey_manager = Prefs.hotkey_manager.HotkeyManager()
        self._viewport_manager = Viewport.viewport_manager.ViewportManager()

    # =========================================================================
    # NAVIGATION
    # =========================================================================
    def switch_translate_manipulator(self):
        self._smart_manipulator.switch_translate_manipulator()

    def switch_rotate_manipulator(self):
        self._smart_manipulator.switch_rotate_manipulator()

    def switch_scale_manipulator(self):
        self._smart_manipulator.switch_scale_manipulator()

    def filter_translate_channels_on_ones(self):
        self._channels_filter.filter_translate_channels_on_ones()

    def filter_translate_channels_on_twos(self):
        self._channels_filter.filter_translate_channels_on_twos()

    def filter_translate_channels_on_threes(self):
        self._channels_filter.filter_translate_channels_on_threes()

    def filter_rotate_channels_on_ones(self):
        self._channels_filter.filter_rotate_channels_on_ones()

    def filter_rotate_channels_on_twos(self):
        self._channels_filter.filter_rotate_channels_on_twos()

    def filter_rotate_channels_on_threes(self):
        self._channels_filter.filter_rotate_channels_on_threes()

    def filter_scale_channels_on_ones(self):
        self._channels_filter.filter_scale_channels_on_ones()

    def filter_scale_channels_on_twos(self):
        self._channels_filter.filter_scale_channels_on_twos()

    def filter_scale_channels_on_threes(self):
        self._channels_filter.filter_scale_channels_on_threes()

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
    def copy_keys(self):
        self._retiming_tools.copy_keys()

    def paste_keys(self):
        self._retiming_tools.paste_keys()

    def cut_keys(self):
        self._retiming_tools.cut_keys()

    def retime_keys(self):
        self._retiming_tools.retime_keys(-2)

    def add_inbetween(self, time_increment=1):
        self._retiming_tools.add_inbetween(time_increment)

    def remove_inbetween(self, time_increment=1):
        self._retiming_tools.remove_inbetween(time_increment)

    # =========================================================================
    # PREFS
    # =========================================================================
    def toggle_hotkey_sets(self):
        self._hotkey_manager.toggle_hotkey_sets()

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
        self._playback_manager.go_to_the_next_marker(c.ALL)

    def go_to_the_prev_marker(self):
        self._playback_manager.go_to_the_prev_marker(c.ALL)

    def go_to_the_next_key_marker(self):
        self._playback_manager.go_to_the_next_marker(c.KEY)

    def go_to_the_prev_key_marker(self):
        self._playback_manager.go_to_the_prev_marker(c.KEY)

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
            LAA_FRAME_MARKER.add_frame_markers(c.KEY)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.KEY)

    def add_breakdown_markers(self):
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.BREAKDOWN)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.BREAKDOWN)

    def add_inbetween_markers(self):
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.INBETWEEN)
        except NameError:
            Trigger.load_frame_markers(self)
            LAA_FRAME_MARKER.add_frame_markers(c.INBETWEEN)

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

    # @staticmethod
    # def remove_timeline_section():
    #     try:
    #         LAA_TIMELINE_SECTION.remove_frame_markers()
    #     except NameError:
    #         Trigger.load_timeline_sections()
    #         LAA_TIMELINE_SECTION.remove_frame_markers()




