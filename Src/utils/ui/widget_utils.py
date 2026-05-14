"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to manipulates all maya Qt
elements.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.mel as mel
import maya.OpenMayaUI as mui

from shiboken2 import wrapInstance
from PySide2 import QtWidgets as wdg


class WidgetUtils(object):

    @staticmethod
    def get_maya_main_window():
        """
        Gets the Maya's main window widget
        :return: Maya's main window widget.
        :rtype: QWidget
        """
        main_window_ptr = mui.MQtUtil.mainWindow()
        return wrapInstance(int(main_window_ptr), wdg.QWidget)

    @staticmethod
    def get_maya_control(control_name):
        control = mel.eval("$tempVar = {0}".format(control_name))
        return control

    @staticmethod
    def get_maya_control_widget(control_name):
        """
        Gets any maya ui element and converts it to a widget.
        :return: Maya's ui control.
        :rtype: QWidget
        """
        control = mel.eval("$tempVar={0}".format(control_name))
        control_ptr = mui.MQtUtil.findControl(control)
        return wrapInstance(int(control_ptr), wdg.QWidget)
