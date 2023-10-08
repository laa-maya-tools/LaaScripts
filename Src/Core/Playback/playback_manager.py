# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: channels_filter.py
-----------------------------------------------------------------------------
This module manages the channelbox selection.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2020 | Python 2
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

import PySide2.QtCore as cor

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Data.user_data import UserData
from LaaScripts.Src.Data.scene_data import SceneData


class PlaybackManager(object):

    def __init__(self):
        self._user_data = UserData.read_user_data(c.PATH.USER_DATA_FILE)
        self._next_frame_timer = cor.QTimer()
        self._prev_frame_timer = cor.QTimer()
        self._next_frame_timer.timeout.connect(self.on_next_frame_timeout)
        self._prev_frame_timer.timeout.connect(self.on_prev_frame_timeout)

    def go_to_the_next_frame(self):
        """
        Goes to the next frame time depending on the playback_mode behaviour.
        """
        i = self._user_data[c.USER_DATA.TIME_INCREMENT]
        playback_start_time = TimelineUtils.get_playback_range()[0]
        playback_end_time = TimelineUtils.get_playback_range()[1]
        animation_end_time = TimelineUtils.get_animation_range()[1]
        next_time = TimelineUtils.get_current_time() + i

        if next_time > animation_end_time and not self._user_data[c.PLAYBACK_MODE] == c.LOOP:
            return

        if next_time > playback_end_time:
            if self._user_data[c.PLAYBACK_MODE] == c.STOP:
                return
            elif self._user_data[c.PLAYBACK_MODE] == c.LOOP:
                next_time = playback_start_time
            elif self._user_data[c.PLAYBACK_MODE] == c.MOVE:
                TimelineUtils.set_playback_range(playback_start_time + time_increment,
                                                 playback_end_time + time_increment)
            elif self._user_data[c.PLAYBACK_MODE] == c.EXPAND:
                TimelineUtils.set_playback_range(playback_start_time, playback_end_time + time_increment)

        TimelineUtils.set_current_time(next_time)
        if self._user_data[c.USER_DATA.INFO_ENABLED]:
            info.show_info('Next Frame >> {0}'.format(int(next_time)))

    def go_to_the_prev_frame(self):
        """
        Goes to the previous frame time depending on the playback_mode behaviour.
        """
        i = self._user_data[c.USER_DATA.TIME_INCREMENT]
        playback_start_time = TimelineUtils.get_playback_range()[0]
        playback_end_time = TimelineUtils.get_playback_range()[1]
        animation_start_time = TimelineUtils.get_animation_range()[0]
        prev_time = TimelineUtils.get_current_time() - i

        if prev_time < animation_start_time and not self._user_data[c.PLAYBACK_MODE] == c.LOOP:
            return

        if prev_time < playback_start_time:
            if self._user_data[c.PLAYBACK_MODE] == c.STOP:
                return
            elif self._user_data[c.PLAYBACK_MODE] == c.LOOP:
                prev_time = playback_end_time
            elif self._user_data[c.PLAYBACK_MODE] == c.MOVE:
                TimelineUtils.set_playback_range(playback_start_time - i, playback_end_time - i)
            elif self._user_data[c.PLAYBACK_MODE] == c.EXPAND:
                TimelineUtils.set_playback_range(playback_start_time - i, playback_end_time)

        TimelineUtils.set_current_time(prev_time)
        if self._user_data[c.USER_DATA.INFO_ENABLED]:
            info.show_info('{0} << Prev Frame'.format(int(prev_time)))

    def next_frame_playback_press(self):
        self.go_to_the_next_frame()
        self._next_frame_timer.start(c.TIMEOUT)

    def prev_frame_playback_press(self):
        self.go_to_the_prev_frame()
        self._prev_frame_timer.start(c.TIMEOUT)

    def next_frame_playback_release(self):
        TimelineUtils.stop_timeline()
        self._next_frame_timer.stop()

    def prev_frame_playback_release(self):
        TimelineUtils.stop_timeline()
        self._prev_frame_timer.stop()

    def on_next_frame_timeout(self):
        TimelineUtils.play_timeline_forward()
        self._next_frame_timer.stop()

    def on_prev_frame_timeout(self):
        TimelineUtils.play_timeline_back()
        self._prev_frame_timer.stop()

    def go_to_the_next_key(self):
        next_key = cmd.findKeyframe(timeSlider=True, which="next")
        TimelineUtils.set_current_time(next_key)
        if self._user_data[c.USER_DATA.INFO_ENABLED]:
            info.show_info('{0} << Prev Key'.format(int(next_key)))

    def go_to_the_prev_key(self):
        prev_key = cmd.findKeyframe(timeSlider=True, which="previous")
        TimelineUtils.set_current_time(prev_key)
        if self._user_data[c.USER_DATA.INFO_ENABLED]:
            info.show_info('{0} << Prev Key'.format(int(prev_key)))

    def get_frame_markers(self):
        """
        Initiates the the frame markers stored in the scene.
        """
        markers = SceneData.load_scene_data(c.NODES.FRAME_MARKER_NODE, c.NODES.FRAME_MARKERS_ATTR).split('#')
        frames = []

        if not markers[0] == '':
            for marker in markers:
                frames.append(float(marker.split(',')[0]))

        return sorted(frames)

    def get_key_markers(self):
        """
        Initiates the the frame markers stored in the scene.
        """
        markers = SceneData.load_scene_data(c.NODES.FRAME_MARKER_NODE, c.NODES.FRAME_MARKERS_ATTR).split('#')
        frames = []

        if not markers[0] == '':
            for marker in markers:
                f = float(marker.split(',')[0])
                t = int(marker.split(',')[1])
                if t == c.KEY:
                    frames.append(f)

        return sorted(frames)

    def go_to_the_next_marker(self, marker_type):
        markers = self.get_key_markers() if marker_type == c.KEY else self.get_frame_markers()
        current_time = TimelineUtils.get_current_time()

        if not markers:
            return

        for i, _ in enumerate(markers):
            if current_time >= markers[-1] or current_time < markers[0]:
                TimelineUtils.set_current_time(markers[0])
                if self._user_data[c.USER_DATA.INFO_ENABLED]:
                    info.show_info('Next Marker >> {0}'.format(int(markers[0])))
                return
            if markers[i] <= current_time < markers[i+1]:
                TimelineUtils.set_current_time(markers[i+1])
                if self._user_data[c.USER_DATA.INFO_ENABLED]:
                    info.show_info('Next Marker >> {0}'.format(int(markers[i+1])))
                return

    def go_to_the_prev_marker(self, marker_type):
        markers = self.get_key_markers() if marker_type == c.KEY else self.get_frame_markers()
        current_time = TimelineUtils.get_current_time()

        if not markers:
            return

        for i, _ in enumerate(markers):
            if current_time <= markers[0] or current_time > markers[-1]:
                TimelineUtils.set_current_time(markers[-1])
                if self._user_data[c.USER_DATA.INFO_ENABLED]:
                    info.show_info('{0} << Prev Marker'.format(int(markers[-1])))
                return
            if markers[i] < current_time <= markers[i+1]:
                TimelineUtils.set_current_time(markers[i])
                if self._user_data[c.USER_DATA.INFO_ENABLED]:
                    info.show_info('{0} << Prev Marker'.format(int(markers[i])))
                return











