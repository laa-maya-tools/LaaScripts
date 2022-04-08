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

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Data.user_data import UserData


class PlaybackManager(object):

    def __init__(self):
        """
        Initializes all the instance variables.
        """
        self._user_data = UserData.read_user_data()

    def go_to_the_next_frame(self):
        """
        Goes to the next frame time depending on the playback_mode behaviour.
        """
        i = self._user_data[c.TIME_INCREMENT]
        playback_start_time = TimelineUtils.get_playback_range()[0]
        playback_end_time = TimelineUtils.get_playback_range()[1]
        animation_end_time = TimelineUtils.get_animation_range()[1]
        next_time = TimelineUtils.get_current_time() + i

        if next_time > animation_end_time:
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
        info.show_info('Frame >> {0}'.format(int(next_time)))

    def go_to_the_prev_frame(self):
        """
        Goes to the previous frame time depending on the playback_mode behaviour.
        """
        i = self._user_data[c.TIME_INCREMENT]
        playback_start_time = TimelineUtils.get_playback_range()[0]
        playback_end_time = TimelineUtils.get_playback_range()[1]
        animation_start_time = TimelineUtils.get_animation_range()[0]
        prev_time = TimelineUtils.get_current_time() - i

        if prev_time < animation_start_time:
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
        info.show_info('{0} << Frame'.format(int(prev_time)))











