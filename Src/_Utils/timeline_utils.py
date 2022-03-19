"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to be used by other modules.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2020 | Python 2
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel
import maya.OpenMayaUI as mui

from shiboken2 import wrapInstance
from PySide2 import QtWidgets as wdg
from .._Constants import constants as c
reload(c)


class TimelineUtils(object):

    @staticmethod
    def get_current_time():
        return cmd.currentTime(query=True)

    @staticmethod
    def set_current_time(current_time):
        cmd.currentTime(current_time, edit=True)

    @staticmethod
    def get_playback_range():
        playback_start_time = cmd.playbackOptions(minTime=True, query=True)
        playback_end_time = cmd.playbackOptions(maxTime=True, query=True)
        return [playback_start_time, playback_end_time]

    @staticmethod
    def get_animation_range():
        animation_start_time = cmd.playbackOptions(animationStartTime=True, query=True)
        animation_end_time = cmd.playbackOptions(animationEndTime=True, query=True)
        return [animation_start_time, animation_end_time]

    @staticmethod
    def get_selection_range():
        time_control = pm.lsUI(type='timeControl')[0]
        selection_range = pm.timeControl(time_control, rangeArray=True, query=True)
        return selection_range

    @staticmethod
    def set_playback_range(start, end):
        cmd.playbackOptions(minTime=start)
        cmd.playbackOptions(maxTime=end)

    @staticmethod
    def set_animation_range(start, end):
        cmd.playbackOptions(animationStartTime=start)
        cmd.playbackOptions(animationEndTime=end)

    # ============================================================================= #
    # NAVIGATION                                                                    #
    # ============================================================================= #
    @staticmethod
    def get_current_move_mode():
        return cmd.manipMoveContext(c.MOVE, q=True, mode=True)

    @staticmethod
    def set_current_move_mode(mode):
        cmd.manipMoveContext(c.MOVE, e=True, mode=mode)

    @staticmethod
    def get_current_rotate_mode():
        return cmd.manipRotateContext(c.ROTATE, q=True, mode=True)

    @staticmethod
    def set_current_rotate_mode(mode):
        cmd.manipRotateContext(c.ROTATE, e=True, mode=mode)

    @staticmethod
    def get_current_scale_mode():
        return cmd.manipScaleContext(c.SCALE, q=True, mode=True)

    @staticmethod
    def set_current_scale_mode(mode):
        cmd.manipScaleContext(c.SCALE, e=True, mode=mode)

    @staticmethod
    def reset_move_mode(mode):
        cmd.manipMoveContext(c.MOVE, e=True, mode=mode)

    @staticmethod
    def reset_rotate_mode(mode):
        cmd.manipRotateContext(c.ROTATE, e=True, mode=mode)

    @staticmethod
    def reset_scale_mode(mode):
        cmd.manipScaleContext(c.SCALE, e=True, mode=mode)

    @staticmethod
    def fix_translate_marking_menu():
        mel.eval('buildTranslateMM;')
        mel.eval('TranslateToolWithSnapMarkingMenuPopDown;')

    @staticmethod
    def fix_rotate_marking_menu():
        mel.eval('buildRotateMM;')
        mel.eval('RotateToolWithSnapMarkingMenuPopDown;')

    @staticmethod
    def fix_scale_marking_menu():
        mel.eval('buildScaleMM;')
        mel.eval('ScaleToolWithSnapMarkingMenuPopDown;')