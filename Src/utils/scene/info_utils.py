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
from LaaScripts.Src.utils.qt_compat import QtWidgets as wdg, QtGui as gui, QtCore as cor
from LaaScripts.Src.utils.qt_compat import Qt_FramelessWindowHint, Qt_AlignCenter

from LaaScripts.Src.constants import constants as c
from LaaScripts.Src.utils.ui.widget_utils import WidgetUtils

msg_ui = None


class InfoUtils(wdg.QDialog):

    def __init__(self, text, warning, timeout,
                 parent=WidgetUtils.get_maya_control_widget(c.MAYA_CONTROLS.SHELF)):
        super(InfoUtils, self).__init__(parent)

        # width = parent.size().width()
        # height = parent.size().height()
        # x_pos = 0
        # y_pos = 0
        width = 400
        height = 32
        x_pos = parent.size().width() - width - 6
        y_pos = 26

        # DIALOG PREFERENCES
        self.setWindowFlags(Qt_FramelessWindowHint)
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
        msg.setAlignment(Qt_AlignCenter)
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
    if not c.USER_DATA.INFO_ENABLED:
        return
    global msg_ui
    try:
        msg_ui.setParent(None)
        msg_ui.deleteLater()
    except:
        pass

    msg_ui = InfoUtils(text, warning, timeout)
    msg_ui.show()
