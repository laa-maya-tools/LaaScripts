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

import PySide2.QtCore as cor

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Data.user_data import UserData


class TimeoutTest(object):

    def __init__(self):
        self._timer = cor.QTimer()

    def test_timeout(self):
        # self.timer = cor.QTimer()
        # timer.singleShot(1000, TimeoutTest.on_timeout_finished)
        # timer.start()
        # timer.stop()
        # self.timer.timeout.connect(self.on_timeout_finished)
        # self.timer.start(3000)

        self.timer = cor.QTimer()
        self.timer.timeout.connect(self.on_timeout_finished)
        self.timer.start(500)


    def on_timeout_finished(self):
        print 'timeout finished'
        self.timer.stop()


if __name__ == '__main__':
    timeout = TimeoutTest()
    timeout.test_timeout()













