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

    # =========================================================================
    # PLAYBACK
    # =========================================================================
    @staticmethod
    def load_frame_markers():
        global LAA_FRAME_MARKER

        try:
            LAA_FRAME_MARKER.setParent(None)
            LAA_FRAME_MARKER.deleteLater()
            LAA_FRAME_MARKER = None
        except:
            pass

        parent = WidgetUtils.get_maya_control(c.TIME_CONTROL)
        LAA_FRAME_MARKER = Playback.FrameMarker()
        LAA_FRAME_MARKER.setVisible(True)

    @staticmethod
    def add_key_markers():
        LAA_FRAME_MARKER.add_frame_markers(c.KEY)

    @staticmethod
    def add_breakdown_markers():
        LAA_FRAME_MARKER.add_frame_markers(c.BREAKDOWN)

    @staticmethod
    def add_inbetween_markers():
        LAA_FRAME_MARKER.add_frame_markers(c.INBETWEEN)

    @staticmethod
    def remove_frame_markers():
        LAA_FRAME_MARKER.remove_frame_markers()








