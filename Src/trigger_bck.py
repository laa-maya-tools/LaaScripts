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
from ._Utils import info
from ._Data import user_data as usd
from ._Constants import constants as cns
from ._Utils import utils as utl

from .Core import playback as pbk
from .Core import frame_marker as fmk

reload(utl)
reload(info)
reload(usd)
reload(cns)
reload(pbk)
reload(fmk)

global AK_FRAME_MARKER


class Trigger(cor.QObject):

    def __init__(self):
        super(Trigger, self).__init__()
        self._user_data = usd.UserData().read_user_data()
        self._utils = utl.Utils()

        self._playback = pbk.Playback()
        self._utils.supress_script_editor_info(True)

        self._frame_marker = fmk.FrameMarker()

        frame_markers = None

    # =========================================================================
    # PLAYBACK
    # =========================================================================
    def go_to_the_next_frame(self):
        self._playback.go_to_the_next_frame()

    def go_to_the_prev_frame(self):
        self._playback.go_to_the_prev_frame()

    def go_to_the_next_key(self):
        self._playback.go_to_the_next_key()

    def go_to_the_prev_key(self):
        self._playback.go_to_the_prev_key()

    def add_frame_markers(self, type):
        AK_FRAME_MARKER.add_frame_markers(type)








