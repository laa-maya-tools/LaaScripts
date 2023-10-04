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

from LaaScripts.Src.Python3.Constants import constants as c
from LaaScripts.Src.Python3.Utils import info_utils as info
from LaaScripts.Src.Python3.Utils.navigation_utils import NavigationUtils


class ChannelsFilter(object):

    def __init__(self):
        """
        Initializes all the instance variables.
        """
        self._selected_channels = []

        self._transform_attrs = {
            c.MOVE: [c.TX, c.TY, c.TZ],
            c.ROTATE: [c.RX, c.RY, c.RZ],
            c.SCALE: [c.SX, c.SY, c.SZ],
            c.ALL: [c.TX, c.TY, c.TZ, c.RX, c.RY, c.RZ, c.SX, c.SY, c.SZ]
        }

    def filter_translate_channels_on_ones(self):
        """
        Filter the translate channels on the channelbox on by one.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if len(selected_translate_channels) == 1:
            if selected_translate_channels[0] == self._transform_attrs[c.MOVE][0]:
                selected_channels = [self._transform_attrs[c.MOVE][1]] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))
                return
            elif selected_translate_channels[0] == self._transform_attrs[c.MOVE][1]:
                selected_channels = [self._transform_attrs[c.MOVE][2]] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))
                return

        selected_channels = [self._transform_attrs[c.MOVE][0]] + selected_rotate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))

    def filter_translate_channels_on_twos(self):
        """
        Filter the translate channels on the channelbox two by two.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if len(selected_translate_channels) == 2:
            if selected_translate_channels[0] == c.TX and selected_translate_channels[1] == c.TY:
                selected_channels = [c.TX, c.TZ] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return
            if selected_translate_channels[0] == c.TX and selected_translate_channels[1] == c.TZ:
                selected_channels = [c.TY, c.TZ] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return

        selected_channels = [c.TX, c.TY] + selected_rotate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))

    def filter_translate_channels_on_threes(self):
        """
        Selects/deselects all translate channels on the channelbox.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if selected_translate_channels:
            cmd.channelBox('mainChannelBox', e=True, select=False)
            selected_channels = selected_rotate_channels + selected_scale_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: CLEAR')
        else:
            selected_channels = self._transform_attrs[c.MOVE] + selected_rotate_channels + selected_scale_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: {0} {1} {2}'.format(selected_channels[0].upper(), selected_channels[1].upper(), selected_channels[2].upper()))

    def filter_rotate_channels_on_ones(self):
        """
        Filters rotate channels on the channelbox one by one.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if len(selected_rotate_channels) == 1:
            if selected_rotate_channels[0] == self._transform_attrs[c.ROTATE][0]:
                selected_channels = [self._transform_attrs[c.ROTATE][1]] + selected_translate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))
                return
            if selected_rotate_channels[0] == self._transform_attrs[c.ROTATE][1]:
                selected_channels = [self._transform_attrs[c.ROTATE][2]] + selected_translate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info(
                    'SELECTION: {0}'.format(selected_channels[0].upper()))
                return

        selected_channels = [self._transform_attrs[c.ROTATE][0]] + selected_translate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))

    def filter_rotate_channels_on_twos(self):
        """
        Filters the rotate channels on the channelbox two by two.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if len(selected_rotate_channels) == 2:
            if selected_rotate_channels[0] == c.RX and selected_rotate_channels[1] == c.RY:
                selected_channels = [c.RX, c.RZ] + selected_translate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return
            if selected_rotate_channels[0] == c.RX and selected_rotate_channels[1] == c.RZ:
                selected_channels = [c.RY, c.RZ] + selected_translate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return

        selected_channels = [c.RX, c.RY] + selected_translate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))

    def filter_rotate_channels_on_threes(self):
        """
        Selects/deselects all rotate channels on the channelbox.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_scale_channels = NavigationUtils.get_selected_scale_channels()

        if selected_rotate_channels:
            cmd.channelBox('mainChannelBox', e=True, select=False)
            selected_channels = selected_translate_channels + selected_scale_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: CLEAR')
        else:
            selected_channels = self._transform_attrs[c.ROTATE] + selected_translate_channels + selected_scale_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: {0} {1} {2}'.format(selected_channels[0].upper(), selected_channels[1].upper(), selected_channels[2].upper()))

    def filter_scale_channels_on_ones(self):
        """
        Filters the scale channels on the channelbox one by one.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_scale_channels = NavigationUtils.get_selected_scale_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()

        if len(selected_scale_channels) == 1:
            if selected_scale_channels[0] == self._transform_attrs[c.SCALE][0]:
                selected_channels = [self._transform_attrs[c.SCALE][1]] + selected_translate_channels + selected_rotate_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))
                return
            if selected_scale_channels[0] == self._transform_attrs[c.SCALE][1]:
                selected_channels = [self._transform_attrs[c.SCALE][2]] + selected_translate_channels + selected_rotate_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))
                return

        selected_channels = [self._transform_attrs[c.SCALE][0]] + selected_translate_channels + selected_rotate_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0}'.format(selected_channels[0].upper()))

    def filter_scale_channels_on_twos(self):
        """
        Filters the scale channels on the channelbox two by two.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_scale_channels = NavigationUtils.get_selected_scale_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()

        if len(selected_scale_channels) == 2:
            if selected_scale_channels[0] == c.SX and selected_scale_channels[1] == c.SY:
                selected_channels = [c.SX, c.SZ] + selected_translate_channels + selected_rotate_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return
            if selected_scale_channels[0] == c.SX and selected_scale_channels[1] == c.SZ:
                selected_channels = [c.SY, c.SZ] + selected_translate_channels + selected_rotate_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))
                return

        selected_channels = [c.SX, c.SY] + selected_translate_channels + selected_rotate_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        info.show_info('SELECTION: {0} {1}'.format(selected_channels[0].upper(), selected_channels[1].upper()))

    def filter_scale_channels_on_threes(self):
        """
        Selects/deselects all scale channels on the channelbox.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_scale_channels = NavigationUtils.get_selected_scale_channels()
        selected_translate_channels = NavigationUtils.get_selected_translate_channels()
        selected_rotate_channels = NavigationUtils.get_selected_rotate_channels()

        if selected_scale_channels:
            cmd.channelBox('mainChannelBox', e=True, select=False)
            selected_channels = selected_translate_channels + selected_rotate_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: CLEAR')
        else:
            selected_channels = self._transform_attrs[c.SCALE] + selected_translate_channels + selected_rotate_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)
            info.show_info('SELECTION: {0} {1} {2}'.format(selected_channels[0].upper(), selected_channels[1].upper(), selected_channels[2].upper()))

    def filter_all_channels(self):
        """
        Toggles between all channels, all transform channels or none.
        """
        selected_objects = NavigationUtils.get_selected_objects()
        if not selected_objects:
            return

        selected_channels = NavigationUtils.get_selected_channels()
        common_channels = NavigationUtils.list_common_channels(selected_objects)

        if len(selected_channels) == len(common_channels):
            NavigationUtils.clear_all_channels()
            info.show_info('SELECTION: NONE')
        elif len(selected_channels) == 0:
            NavigationUtils.select_channels(selected_objects, self._transform_attrs[c.ALL])
            info.show_info('SELECTION: XFORMS')
        else:
            NavigationUtils.select_channels(selected_objects, common_channels)
            info.show_info('SELECTION: ALL')

    def toggle_sync_mode(self):
        """
        Toggles timeline/graph editor display on the channelbox.
        """
        state = 'true'
        try:
            state = (str(not cmd.menuItem('cbTimelineSyncMenu', checkBox=True, query=True))).lower()
        except:
            # Initializes the channelbox sync
            mel.eval('toggleChannelBoxTimelineSync {0};'.format(state))
            mel.eval('toggleChannelBoxGraphEdSync {0};'.format(state))

        mel.eval('toggleChannelBoxTimelineSync {0};'.format(state))
        mel.eval('toggleChannelBoxGraphEdSync {0};'.format(state))

        info.show_info('CHANNELBOX SYNC')