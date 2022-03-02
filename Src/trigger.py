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
reload(info)


class Trigger(cor.QObject):

    def __init__(self):
        super(Trigger, self).__init__()

    # =========================================================================
    # GO TO THE NEXT FRAME
    # =========================================================================
    def go_to_the_next_frame(self):
        print ("go_to_the_next_frame1")
        info.show_info('Info', True)
        # self.supress_script_editor_info(True)
        # self._playback_tools.go_to_the_next_frame()
        # info.show_message('Next Frame >>')
        # self.supress_script_editor_info(False)








