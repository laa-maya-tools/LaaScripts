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

from .._Constants import constants as c
reload(c)


class NavigationUtils(object):

    @staticmethod
    def get_current_move_mode():
        """
        Gets the current move manipulator mode (local or world).
        :return: Current move mode.
        :rtype: str
        """
        return cmd.manipMoveContext(c.MOVE, q=True, mode=True)

    @staticmethod
    def set_current_move_mode(mode):
        """
        Sets the current move manipulator mode.
        :param str mode: Move mode (local or world).
        """
        cmd.manipMoveContext(c.MOVE, e=True, mode=mode)

    @staticmethod
    def get_current_rotate_mode():
        """
        Gets the current rotate manipulator mode (local, world or gimbal).
        :return: Current rotate mode.
        :rtype: str
        """
        return cmd.manipRotateContext(c.ROTATE, q=True, mode=True)

    @staticmethod
    def set_current_rotate_mode(mode):
        """
        Sets the current rotate manipulator mode.
        :param str mode: Rotate mode (local, world or gimbal).
        """
        cmd.manipRotateContext(c.ROTATE, e=True, mode=mode)

    @staticmethod
    def get_current_scale_mode():
        """
        Gets the current scale manipulator mode (local or world).
        :return: Current scale mode.
        :rtype: str
        """
        return cmd.manipScaleContext(c.SCALE, q=True, mode=True)

    @staticmethod
    def set_current_scale_mode(mode):
        """
        Sets the current scale manipulator mode.
        :param str mode: Scale mode (local or world).
        """
        cmd.manipScaleContext(c.SCALE, e=True, mode=mode)

    @staticmethod
    def reset_move_mode(mode):
        """
        Resets move manipulator to its default state.
        :param str mode: Default move mode.
        """
        cmd.manipMoveContext(c.MOVE, e=True, mode=mode)

    @staticmethod
    def reset_rotate_mode(mode):
        """
        Resets rotate manipulator to its default state.
        :param str mode: Default rotate mode.
        """
        cmd.manipRotateContext(c.ROTATE, e=True, mode=mode)

    @staticmethod
    def reset_scale_mode(mode):
        """
        Resets scale manipulator to its default state.
        :param str mode: Default scale mode.
        """
        cmd.manipScaleContext(c.SCALE, e=True, mode=mode)

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
