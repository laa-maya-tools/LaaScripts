"""
=============================================================================
MODULE: maya_widgets_utils.py
-----------------------------------------------------------------------------
This class is responsible for showing info to the user. This module must
be used by the trigger module, SHOULD NOT BE USED DIRECTLY.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2018 | Python 2
=============================================================================
"""
import maya.mel as mel
import maya.OpenMayaUI as mui

from shiboken2 import wrapInstance
from PySide2 import QtWidgets as wdg


class AnimUtils(object):

    @staticmethod
    def get_maya_main_window():
        main_window_ptr = mui.MQtUtil.mainWindow()
        return wrapInstance(long(main_window_ptr), wdg.QWidget)

    @staticmethod
    def get_maya_control(control_name):
        control = mel.eval("$tempVar = {0}".format(control_name))
        control_ptr = mui.MQtUtil.findControl(control)
        return wrapInstance(long(control_ptr), wdg.QWidget)

    @staticmethod
    def get_active_panel():
        panel = cmd.getPanel(withFocus=True)

        if cmd.getPanel(typeOf=panel) == MODEL_PANEL:
            return wrapInstance(long(mui.MQtUtil.findControl(panel)), wdg.QWidget)
        else:
            return wrapInstance(long(mui.MQtUtil.mainWindow()), wdg.QWidget)

