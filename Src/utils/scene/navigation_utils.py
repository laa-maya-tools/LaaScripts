"""
=============================================================================
MODULE: navigation_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods that extends maya's navigation
functionality.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Constants import constants as c


class NavigationUtils(object):

    @staticmethod
    def get_current_move_mode():
        """
        Gets the current move manipulator mode (local or world).
        :return: Current move mode.
        :rtype: str
        """
        return cmd.manipMoveContext(c.NAVIGATION.MOVE, q=True, mode=True)

    @staticmethod
    def set_current_move_mode(mode):
        """
        Sets the current move manipulator mode.
        :param str mode: Move mode (local or world).
        """
        cmd.manipMoveContext(c.NAVIGATION.MOVE, e=True, mode=mode)

    @staticmethod
    def get_current_rotate_mode():
        """
        Gets the current rotate manipulator mode (local, world or gimbal).
        :return: Current rotate mode.
        :rtype: str
        """
        return cmd.manipRotateContext(c.NAVIGATION.ROTATE, q=True, mode=True)

    @staticmethod
    def set_current_rotate_mode(mode):
        """
        Sets the current rotate manipulator mode.
        :param str mode: Rotate mode (local, world or gimbal).
        """
        cmd.manipRotateContext(c.NAVIGATION.ROTATE, e=True, mode=mode)

    @staticmethod
    def get_current_scale_mode():
        """
        Gets the current scale manipulator mode (local or world).
        :return: Current scale mode.
        :rtype: str
        """
        return cmd.manipScaleContext(c.NAVIGATION.SCALE, q=True, mode=True)

    @staticmethod
    def set_current_scale_mode(mode):
        """
        Sets the current scale manipulator mode.
        :param str mode: Scale mode (local or world).
        """
        cmd.manipScaleContext(c.NAVIGATION.SCALE, e=True, mode=mode)

    @staticmethod
    def reset_move_mode(mode):
        """
        Resets move manipulator to its default state.
        :param str mode: Default move mode.
        """
        cmd.manipMoveContext(c.NAVIGATION.MOVE, e=True, mode=mode)

    @staticmethod
    def reset_rotate_mode(mode):
        """
        Resets rotate manipulator to its default state.
        :param str mode: Default rotate mode.
        """
        cmd.manipRotateContext(c.NAVIGATION.ROTATE, e=True, mode=mode)

    @staticmethod
    def reset_scale_mode(mode):
        """
        Resets scale manipulator to its default state.
        :param str mode: Default scale mode.
        """
        cmd.manipScaleContext(c.NAVIGATION.SCALE, e=True, mode=mode)

    @staticmethod
    def fix_translate_marking_menu():
        """
        Fixes translate manipulator marking menu popup.
        """
        mel.eval('buildTranslateMM;')
        mel.eval('TranslateToolWithSnapMarkingMenuPopDown;')

    @staticmethod
    def fix_rotate_marking_menu():
        """
        Fixes rotate manipulator marking menu popup.
        """
        mel.eval('buildRotateMM;')
        mel.eval('RotateToolWithSnapMarkingMenuPopDown;')

    @staticmethod
    def fix_scale_marking_menu():
        """
        Fixes scale manipulator marking menu popup.
        """
        mel.eval('buildScaleMM;')
        mel.eval('ScaleToolWithSnapMarkingMenuPopDown;')

    @staticmethod
    def get_selected_objects():
        selected_objects = cmd.ls(sl=True)
        return selected_objects or []

    @staticmethod
    def get_selected_channels():
        selected_channels = cmd.channelBox('mainChannelBox', q=True, sma=True)
        return selected_channels or []

    @staticmethod
    def get_selected_channels_of_type(transform_type):
        channels_list = []
        selected_channels = NavigationUtils.get_selected_channels()
        for channel in selected_channels:
            if channel in transform_type:
                channels_list.append(channel)
        return channels_list

    @staticmethod
    def get_selected_translate_channels():
        return NavigationUtils.get_selected_channels_of_type(c.NAVIGATION.TRS_XYZ)

    @staticmethod
    def get_selected_rotate_channels():
        return NavigationUtils.get_selected_channels_of_type(c.NAVIGATION.ROT_XYZ)

    @staticmethod
    def get_selected_scale_channels():
        return NavigationUtils.get_selected_channels_of_type(c.NAVIGATION.SCL_XYZ)

    @staticmethod
    def select_channels(selected_objects, channels):
        attributes = []
        for obj in selected_objects:
            for channel in channels:
                full_attr = '{0}.{1}'.format(obj, channel)
                if cmd.objExists(full_attr):
                    attributes.append(full_attr)


        print(attributes)
        cmd.channelBox('mainChannelBox', e=True, select=attributes)

    @staticmethod
    def sync_timeline_display(state):
        mel.eval('toggleChannelBoxTimelineSync {0};'.format(state))

    @staticmethod
    def sync_graph_editor_display(state):
        mel.eval('toggleChannelBoxGraphEdSync {0};'.format(state))

    @staticmethod
    def list_all_channels(selected_objects):
        all_channels = cmd.listAttr(selected_objects)
        cb_channels = cmd.listAnimatable(selected_objects)

        if all_channels and cb_channels:
            channels = [attr for attr in all_channels for cb in cb_channels if cb.endswith(attr)]
            return channels

    @staticmethod
    def list_common_channels(selected_objects):
        if len(selected_objects) == 1:
            anim_attrs = cmd.listAnimatable(selected_objects[0])
            return [attr.split('.')[-1] for attr in anim_attrs]

        anim_attrs = cmd.listAnimatable(selected_objects)
        anim_channels = list(set([attr.split('.')[-1] for attr in anim_attrs]))
        for object in selected_objects:
            for channel in anim_channels:
                full_attr = '{0}.{1}'.format(object, channel)
                if not cmd.objExists(full_attr):
                    anim_channels.remove(channel)
        return anim_channels

    @staticmethod
    def clear_all_channels():
        cmd.channelBox('mainChannelBox', e=True, select=False)
