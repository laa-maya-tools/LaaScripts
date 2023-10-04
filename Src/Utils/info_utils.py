"""
=============================================================================
MODULE: info_utils.py
-----------------------------------------------------------------------------
This class is responsible for showing info and warnings to the user.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as cor

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils.widget_utils import WidgetUtils


msg_ui = None


class InfoUtils(wdg.QDialog):

    def __init__(self, text, warning, timeout, parent=WidgetUtils().get_maya_control_widget(c.RANGE_SLIDER)):
        super(InfoUtils, self).__init__(parent)

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
    if not c.INFO_ENABLED:
        return
    global msg_ui
    try:
        msg_ui.setParent(None)
        msg_ui.deleteLater()
    except:
        pass

    msg_ui = InfoUtils(text, warning, timeout)
    msg_ui.show()

