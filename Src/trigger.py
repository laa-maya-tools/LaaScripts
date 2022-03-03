# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: trigger.py
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

reload(utl)
reload(info)
reload(usd)
reload(cns)
reload(pbk)


class Trigger(cor.QObject):

    def __init__(self):
        super(Trigger, self).__init__()
        self._user_data = usd.UserData().read_user_data()
        self._utils = utl.Utils()

        self._playback = pbk.Playback()
        self._utils.supress_script_editor_info(True)

    # =========================================================================
    # GO TO THE NEXT FRAME
    # =========================================================================
    def go_to_the_next_frame(self):
        self._playback.go_to_the_next_frame()








