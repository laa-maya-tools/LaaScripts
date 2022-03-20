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
from PySide2 import QtCore as cor

from ..Constants import constants as cns
from ..Utils import utils as utl
reload(cns)
reload(utl)

msg_ui = None


class Info(wdg.QDialog):

    def __init__(self, text, warning, timeout, parent=utl.Utils().get_maya_control(cns.RANGE_SLIDER)):
        super(Info, self).__init__(parent)

        width = parent.size().width()
        height = parent.size().height()
        x_pos = 0
        y_pos = 0

        # DIALOG PREFERENCES
        self.setWindowFlags(cor.Qt.FramelessWindowHint)
        self.setFixedSize(width, height)
        self.setGeometry(cor.QRect(x_pos, y_pos, width, height))
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

        # SHOW INFO
        msg = wdg.QLabel(text)
        msg.setFont(msg_font)
        msg.setAlignment(cor.Qt.AlignCenter | cor.Qt.AlignCenter)
        msg.setContentsMargins(0, 0, 0, 0)
        if warning:
            msg.setStyleSheet('background-color: #FF7258; color: #333333;')
        else:
            msg.setStyleSheet('background-color: #424242; color: #cccccc;')

        h_layout.addWidget(msg)

        # SET TIMEOUT
        timer = cor.QTimer()
        timer.singleShot(timeout, self.close)


def show_info(text, warning=False, timeout=1000):
    if not cns.INFO_ENABLED:
        return
    global msg_ui
    try:
        msg_ui.setParent(None)
        msg_ui.deleteLater()
    except:
        pass

    msg_ui = Info(text, warning, timeout)
    msg_ui.show()
