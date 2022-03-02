"""
=============================================================================
MODULE: info.py
-----------------------------------------------------------------------------
This class is responsible for showing info to the user. This module must
be used by the trigger module, SHOULD NOT BE USED DIRECTLY.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2019 | Python 2
=============================================================================
"""
from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as core

from shiboken2 import wrapInstance
import maya.OpenMayaUI as mui
import maya.cmds as cmd

from .._Constants import constants as cns
reload(cns)


class Info(wdg.QDialog):

    def __init__(self, message, timeout, parent=get_active_panel()):
        super(Info, self).__init__(parent)

        x_pos = parent.x() + (parent.width() - cns.INFO_X_OFFSET)
        y_pos = parent.y() + cns.INFO_Y_OFFSET

        # DIALOG PREFERENCES
        self.setWindowFlags(core.Qt.FramelessWindowHint)
        self.setFixedSize(cns.INFO_WIDTH, cns.INFO_HEIGHT)
        self.setGeometry(core.QRect(x_pos, y_pos, parent.width(), parent.height()))
        self.setStyleSheet('background-color: #333333;')
        self.setContentsMargins(1, 1, 1, 1)

        # CREATE LAYOUT
        h_layout = wdg.QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(h_layout)

        # CREATE FONT
        msg_font = gui.QFont()
        msg_font.setPointSize(10)
        msg_font.setBold(True)

        # SHOW MESSAGE
        msg = wdg.QLabel(message)
        msg.setFont(msg_font)
        msg.setAlignment(core.Qt.AlignCenter | core.Qt.AlignCenter)
        msg.setContentsMargins(0, 0, 0, 0)
        msg.setStyleSheet('background-color: #424242; color: #cccccc;')
        h_layout.addWidget(msg)

        # SET TIMEOUT
        timer = core.QTimer()
        timer.singleShot(timeout, self.close)


def show_message(message, timeout=1000):
    try:
        msg_ui.setParent(None)
        msg_ui.deleteLater()
    except:
        pass

    msg_ui = InfoUtils(message, timeout)
    msg_ui.show()


if __name__ == '__main__':
    show_message('Mensaje')