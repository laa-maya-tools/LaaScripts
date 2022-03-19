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
from .Core import Navigation
reload(Navigation)


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







