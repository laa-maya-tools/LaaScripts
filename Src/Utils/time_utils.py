"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to get/set timeline keyframing
data.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel
import PySide2.QtCore as cor


class TimeUtils(object):
    def __init__(self):
        self._timer = cor.QTimer()
        self._timer.timeout.connect(self.on_timeout_finished)

    def start_timeout(self, timeout):
        self._timer.start(timeout)

    def stop_timeout(self):
        self._timer.stop()

    def on_timeout_finished(self):
        print 'timeout finished'


if __name__ == '__main__':
    time_utils = TimeUtils()
    time_utils.start_timeout(500)



