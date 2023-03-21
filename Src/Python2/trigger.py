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
from PySide2 import QtCore as cor

from LaaScripts.Src.Python2.Core import Navigation
from LaaScripts.Src.Python2.Core import Keyframing
from LaaScripts.Src.Python2.Core import Playback
from LaaScripts.Src.Python2.Core import Prefs
from LaaScripts.Src.Python2.Core import Viewport
from LaaScripts.Src.Python2.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Python2.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Python2.Constants import constants as c

global LAA_FRAME_MARKER
global LAA_TIMELINE_SECTION


class Trigger(object):

    def __init__(self):
        super(Trigger, self).__init__()

    # =========================================================================
    # NAVIGATION
    # =========================================================================
    @staticmethod
    def switch_translate_manipulator():
        Navigation.SmartManipulator().switch_translate_manipulator()

    @staticmethod
    def switch_rotate_manipulator():
        Navigation.SmartManipulator().switch_rotate_manipulator()

    @staticmethod
    def switch_scale_manipulator():
        Navigation.SmartManipulator().switch_scale_manipulator()

    @staticmethod
    def filter_translate_channels_on_ones():
        Navigation.ChannelsFilter().filter_translate_channels_on_ones()

    @staticmethod
    def filter_translate_channels_on_twos():
        Navigation.ChannelsFilter().filter_translate_channels_on_twos()

    @staticmethod
    def filter_translate_channels_on_threes():
        Navigation.ChannelsFilter().filter_translate_channels_on_threes()

    @staticmethod
    def filter_rotate_channels_on_ones():
        Navigation.ChannelsFilter().filter_rotate_channels_on_ones()

    @staticmethod
    def filter_rotate_channels_on_twos():
        Navigation.ChannelsFilter().filter_rotate_channels_on_twos()

    @staticmethod
    def filter_rotate_channels_on_threes():
        Navigation.ChannelsFilter().filter_rotate_channels_on_threes()

    @staticmethod
    def filter_scale_channels_on_ones():
        Navigation.ChannelsFilter().filter_scale_channels_on_ones()

    @staticmethod
    def filter_scale_channels_on_twos():
        Navigation.ChannelsFilter().filter_scale_channels_on_twos()

    @staticmethod
    def filter_scale_channels_on_threes():
        Navigation.ChannelsFilter().filter_scale_channels_on_threes()

    @staticmethod
    def filter_all_channels():
        Navigation.ChannelsFilter().filter_all_channels()

    @staticmethod
    def select_all_channels():
        Navigation.ChannelsFilter().select_all_channels()

    @staticmethod
    def clear_all_channels():
        Navigation.ChannelsFilter().clear_all_channels()

    @staticmethod
    def toggle_sync_mode():
        Navigation.ChannelsFilter().toggle_sync_mode()

    # =========================================================================
    # KEYFRAMING
    # =========================================================================
    @staticmethod
    def add_inbetween(time_increment=1):
        Keyframing.retiming_tools.retime_keys(time_increment, True, False)

    @staticmethod
    def remove_inbetween(time_increment=-1):
        Keyframing.retiming_tools.retime_keys(time_increment, True, False)

    # =========================================================================
    # PLAYBACK
    # =========================================================================
    @staticmethod
    def go_to_the_next_frame():
        Playback.playback_manager.go_to_the_next_frame()

    @staticmethod
    def go_to_the_prev_frame():
        Playback.playback_manager.go_to_the_prev_frame()

    @staticmethod
    def next_frame_playback_press():
        Playback.playback_manager.next_frame_playback_press()

    @staticmethod
    def prev_frame_playback_press():
        Playback.playback_manager.prev_frame_playback_press()

    @staticmethod
    def next_frame_playback_release():
        Playback.playback_manager.next_frame_playback_release()

    @staticmethod
    def prev_frame_playback_release():
        Playback.playback_manager.prev_frame_playback_release()

    @staticmethod
    def go_to_the_next_key():
        Playback.playback_manager.go_to_the_next_key()

    @staticmethod
    def go_to_the_prev_key():
        Playback.playback_manager.go_to_the_prev_key()

    @staticmethod
    def go_to_the_next_marker():
        Playback.playback_manager.go_to_the_next_marker(c.ALL)

    @staticmethod
    def go_to_the_prev_marker():
        Playback.playback_manager.go_to_the_prev_marker(c.ALL)

    @staticmethod
    def go_to_the_next_key_marker():
        Playback.playback_manager.go_to_the_next_marker(c.KEY)

    @staticmethod
    def go_to_the_prev_key_marker():
        Playback.playback_manager.go_to_the_prev_marker(c.KEY)

    @staticmethod
    def load_frame_markers():
        global LAA_FRAME_MARKER

        try:
            LAA_FRAME_MARKER.setParent(None)
            LAA_FRAME_MARKER.deleteLater()
            LAA_FRAME_MARKER = None
        except NameError:
            pass

        LAA_FRAME_MARKER = Playback.FrameMarker()
        LAA_FRAME_MARKER.setVisible(True)

    @staticmethod
    def add_key_markers():
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.KEY)
        except NameError:
            Trigger.load_frame_markers()
            LAA_FRAME_MARKER.add_frame_markers(c.KEY)

    @staticmethod
    def add_breakdown_markers():
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.BREAKDOWN)
        except NameError:
            Trigger.load_frame_markers()
            LAA_FRAME_MARKER.add_frame_markers(c.BREAKDOWN)

    @staticmethod
    def add_inbetween_markers():
        try:
            LAA_FRAME_MARKER.add_frame_markers(c.INBETWEEN)
        except NameError:
            Trigger.load_frame_markers()
            LAA_FRAME_MARKER.add_frame_markers(c.INBETWEEN)

    @staticmethod
    def remove_frame_markers():
        try:
            LAA_FRAME_MARKER.remove_frame_markers()
        except NameError:
            Trigger.load_frame_markers()
            LAA_FRAME_MARKER.remove_frame_markers()

    @staticmethod
    def load_timeline_sections():
        global LAA_TIMELINE_SECTION

        try:
            LAA_TIMELINE_SECTION.setParent(None)
            LAA_TIMELINE_SECTION.deleteLater()
            LAA_TIMELINE_SECTION = None
        except NameError:
            pass

        LAA_TIMELINE_SECTION = Playback.TimelineSection()
        LAA_TIMELINE_SECTION.setVisible(True)

    @staticmethod
    def add_timeline_section(random_color=False):
        try:
            LAA_TIMELINE_SECTION.add_timeline_section(random_color)
        except NameError:
            Trigger.load_timeline_sections()
            LAA_TIMELINE_SECTION.add_timeline_section(random_color)

    # @staticmethod
    # def remove_timeline_section():
    #     try:
    #         LAA_TIMELINE_SECTION.remove_frame_markers()
    #     except NameError:
    #         Trigger.load_timeline_sections()
    #         LAA_TIMELINE_SECTION.remove_frame_markers()


if __name__ == '__main__':
    Trigger.load_timeline_sections()
    Trigger.add_timeline_section(True)
    # # print LAA_TIMELINE_SECTION.get_unused_colors()
    # print LAA_TIMELINE_SECTION.get_random_color()
    #







