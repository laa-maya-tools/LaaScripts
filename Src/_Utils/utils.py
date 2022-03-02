"""
=============================================================================
MODULE: utils.py
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
from .._Constants import constants as cns
reload(cns)


class Utils(object):

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

        if cmd.getPanel(typeOf=panel) == cns.TIME_CONTROL:
            return wrapInstance(long(mui.MQtUtil.findControl(panel)), wdg.QWidget)
        else:
            return wrapInstance(long(mui.MQtUtil.mainWindow()), wdg.QWidget)

    @staticmethod
    def supress_script_editor_info(state=True):
        cmd.scriptEditorInfo(suppressInfo=state, suppressErros=state, suppressWarnings=state)

