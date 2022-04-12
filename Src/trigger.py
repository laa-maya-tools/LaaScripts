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

from LaaScripts.Src.Core import Navigation
from LaaScripts.Src.Core import Playback
from LaaScripts.Src.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Constants import constants as c

global LAA_FRAME_MARKER


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








