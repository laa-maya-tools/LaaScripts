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
from LaaScripts.Src.Utils.navigation_utils import NavigationUtils


class ChannelsFilter(object):

    def __init__(self):
        self._selected_channels = []

        self._transform_attrs = {
            c.MOVE: [c.TX, c.TY, c.TZ],
            c.ROTATE: [c.RX, c.RY, c.RZ],
            c.SCALE: [c.SX, c.SY, c.SZ]
        }

    def filter_translate_channels_on_ones(self):
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
                return
            if selected_translate_channels[0] == self._transform_attrs[c.MOVE][1]:
                selected_channels = [self._transform_attrs[c.MOVE][2]] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                return

        selected_channels = [self._transform_attrs[c.MOVE][0]] + selected_rotate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        return

    def filter_translate_channels_on_twos(self):
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
                return
            if selected_translate_channels[0] == c.TX and selected_translate_channels[1] == c.TZ:
                selected_channels = [c.TY, c.TZ] + selected_rotate_channels + selected_scale_channels
                NavigationUtils.select_channels(selected_objects, selected_channels)
                return

        selected_channels = [c.TX, c.TY] + selected_rotate_channels + selected_scale_channels
        NavigationUtils.select_channels(selected_objects, selected_channels)
        return

    def filter_translate_channels_on_threes(self):
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
        else:
            selected_channels = self._transform_attrs[c.MOVE] + selected_rotate_channels + selected_scale_channels
            NavigationUtils.select_channels(selected_objects, selected_channels)


    # def toggle_one_translate_channel(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_translate_channels) == 1:
    #         if selected_translate_channels[0] == self._transform_attrs[MOVE][0]:
    #             self._selected_channels = [self._transform_attrs[MOVE][1]] + selected_rotate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_translate_channels[0] == self._transform_attrs[MOVE][1]:
    #             self._selected_channels = [self._transform_attrs[MOVE][2]] + selected_rotate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [self._transform_attrs[MOVE][0]] + selected_rotate_channels + selected_scale_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    #
    # def toggle_two_translate_channels(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_translate_channels) == 2:
    #         if selected_translate_channels[0] == TX and selected_translate_channels[1] == TY:
    #             self._selected_channels = [TX, TZ] + selected_rotate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_translate_channels[0] == TX and selected_translate_channels[1] == TZ:
    #             self._selected_channels = [TY, TZ] + selected_rotate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [TX, TY] + selected_rotate_channels + selected_scale_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_rotate_channels(self, modifier):
    #     selected_objects = cmd.ls(sl=True)
    #     if not selected_objects:
    #         cmd.warning('No object is selected.')
    #         return self._selected_channels
    #
    #     if modifier is NONE:
    #         self.toggle_all_rotate_channels(selected_objects)
    #         return self._selected_channels
    #     if modifier is CTRL:
    #         self.toggle_one_rotate_channel(selected_objects)
    #         return self._selected_channels
    #     if modifier is ALT:
    #         self.toggle_two_rotate_channels(selected_objects)
    #         return self._selected_channels
    #
    # def toggle_all_rotate_channels(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if selected_rotate_channels:
    #         cmd.channelBox('mainChannelBox', e=True, select=False)
    #         self._selected_channels = selected_translate_channels + selected_scale_channels
    #         self.select_channels(selected_objects, self._selected_channels)
    #         return self._selected_channels
    #
    #     self._selected_channels = self._transform_attrs[ROTATE] + selected_translate_channels + selected_scale_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_one_rotate_channel(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_rotate_channels) == 1:
    #         if selected_rotate_channels[0] == self._transform_attrs[ROTATE][0]:
    #             self._selected_channels = [self._transform_attrs[ROTATE][1]] + selected_translate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_rotate_channels[0] == self._transform_attrs[ROTATE][1]:
    #             self._selected_channels = [self._transform_attrs[ROTATE][2]] + selected_translate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [self._transform_attrs[ROTATE][0]] + selected_translate_channels + selected_scale_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_two_rotate_channels(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_rotate_channels) == 2:
    #         if selected_rotate_channels[0] == RX and selected_rotate_channels[1] == RY:
    #             self._selected_channels = [RX, RZ] + selected_translate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_rotate_channels[0] == RX and selected_rotate_channels[1] == RZ:
    #             self._selected_channels = [RY, RZ] + selected_translate_channels + selected_scale_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [RX, RY] + selected_translate_channels + selected_scale_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_scale_channels(self, modifier):
    #     selected_objects = cmd.ls(sl=True)
    #     if not selected_objects:
    #         cmd.warning('No object is selected.')
    #         return self._selected_channels
    #
    #     if modifier is NONE:
    #         self.toggle_all_scale_channels(selected_objects)
    #         return self._selected_channels
    #     if modifier is CTRL:
    #         self.toggle_one_scale_channel(selected_objects)
    #         return self._selected_channels
    #     if modifier is ALT:
    #         self.toggle_two_scale_channels(selected_objects)
    #         return self._selected_channels
    #
    # def toggle_all_scale_channels(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if selected_scale_channels:
    #         cmd.channelBox('mainChannelBox', e=True, select=False)
    #         self._selected_channels = selected_translate_channels + selected_rotate_channels
    #         self.select_channels(selected_objects, self._selected_channels)
    #         return self._selected_channels
    #
    #     self._selected_channels = self._transform_attrs[SCALE] + selected_translate_channels + selected_rotate_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_one_scale_channel(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_scale_channels) == 1:
    #         if selected_scale_channels[0] == self._transform_attrs[SCALE][0]:
    #             self._selected_channels = [self._transform_attrs[SCALE][1]] + selected_translate_channels + selected_rotate_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_scale_channels[0] == self._transform_attrs[SCALE][1]:
    #             self._selected_channels = [self._transform_attrs[SCALE][2]] + selected_translate_channels + selected_rotate_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [self._transform_attrs[SCALE][0]] + selected_translate_channels + selected_rotate_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def toggle_two_scale_channels(self, selected_objects):
    #     selected_translate_channels = self.get_selected_transform_channels(MOVE)
    #     selected_rotate_channels = self.get_selected_transform_channels(ROTATE)
    #     selected_scale_channels = self.get_selected_transform_channels(SCALE)
    #
    #     if len(selected_scale_channels) == 2:
    #         if selected_scale_channels[0] == SX and selected_scale_channels[1] == SY:
    #             self._selected_channels = [SX, SZ] + selected_translate_channels + selected_rotate_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #         if selected_scale_channels[0] == SX and selected_scale_channels[1] == SZ:
    #             self._selected_channels = [SY, SZ] + selected_translate_channels + selected_rotate_channels
    #             self.select_channels(selected_objects, self._selected_channels)
    #             return self._selected_channels
    #
    #     self._selected_channels = [SX, SY] + selected_translate_channels + selected_rotate_channels
    #     self.select_channels(selected_objects, self._selected_channels)
    #     return self._selected_channels
    #
    # def select_channels(self, selected_objects, channels):
    #     for obj in selected_objects:
    #         formated_attrs = ['{0}.{1}'.format(obj, channel) for channel in channels]
    #         cmd.channelBox('mainChannelBox', e=True, select=formated_attrs)
    #
    # def select_all_channels(self, modifier):
    #     selected_objects = cmd.ls(sl=True)
    #     if not selected_objects:
    #         cmd.warning('No object is selected.')
    #         return []
    #
    #     for obj in selected_objects:
    #         formated_attrs = ['{0}.{1}'.format(obj, attr) for attr in TRANSFORM_ATTRS]
    #         cmd.channelBox('mainChannelBox', e=True, select=formated_attrs)
    #     return TRANSFORM_ATTRS
    #
    # def clear_all_channels(self, modifier):
    #     cmd.channelBox('mainChannelBox', e=True, select=False)
    #     return []
    #
    # def activate_sync_mode(self, modifier, state):
    #     state = cmd.menuItem('cbTimelineSyncMenu', checkBox=True, query=True)
    #     if state:
    #         # Turn Sync Off
    #         mel.eval('toggleChannelBoxTimelineSync true;')
    #         mel.eval('toggleChannelBoxGraphEdSync true;')
    #         return True
    #     else:
    #         # Turn Sync On
    #         mel.eval('toggleChannelBoxTimelineSync false;')
    #         mel.eval('toggleChannelBoxGraphEdSync false;')
    #         return False


if __name__ == '__main__':
    print('test')
    print NavigationUtils.get_selected_channels()
    print NavigationUtils.get_selected_translate_channels()




