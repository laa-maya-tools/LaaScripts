import maya.OpenMayaUI as mui

from LaaScripts.Src.utils.qt_compat import QtWidgets as wdg, QtGui as gui, wrapInstance
from LaaScripts.Src.constants import constants as c
from LaaScripts.Src.data.user_data import UserData


_MARKER_LABELS = {
    c.PLAYBACK.KEY:       'Key',
    c.PLAYBACK.BREAKDOWN: 'Breakdown',
    c.PLAYBACK.INBETWEEN: 'Inbetween',
    c.PLAYBACK.CUSTOM:    'Custom',
}

_MARKER_DEFAULTS = {
    c.PLAYBACK.KEY:       c.PLAYBACK.COLOR_KEY,
    c.PLAYBACK.BREAKDOWN: c.PLAYBACK.COLOR_BREAKDOWN,
    c.PLAYBACK.INBETWEEN: c.PLAYBACK.COLOR_INBETWEEN,
    c.PLAYBACK.CUSTOM:    c.PLAYBACK.COLOR_CUSTOM,
}

_USER_DATA_KEYS = {
    c.PLAYBACK.KEY:       c.USER_DATA.MARKER_COLOR_KEY,
    c.PLAYBACK.BREAKDOWN: c.USER_DATA.MARKER_COLOR_BREAKDOWN,
    c.PLAYBACK.INBETWEEN: c.USER_DATA.MARKER_COLOR_INBETWEEN,
    c.PLAYBACK.CUSTOM:    c.USER_DATA.MARKER_COLOR_CUSTOM,
}

_MARKER_ORDER = (c.PLAYBACK.KEY, c.PLAYBACK.BREAKDOWN, c.PLAYBACK.INBETWEEN, c.PLAYBACK.CUSTOM)


class MarkerColorDialog(wdg.QDialog):

    def __init__(self, frame_marker, parent=None):
        if parent is None:
            parent = wrapInstance(int(mui.MQtUtil.mainWindow()), wdg.QWidget)
        super(MarkerColorDialog, self).__init__(parent)
        self._frame_marker = frame_marker
        self._buttons = {}
        self._build_ui()

    def _build_ui(self):
        self.setWindowTitle('Marker Colors')
        self.setFixedWidth(300)
        self.setWindowFlags(self.windowFlags() & ~0x00000400)  # remove WindowContextHelpButtonHint

        root = wdg.QVBoxLayout(self)
        root.setSpacing(6)
        root.setContentsMargins(14, 14, 14, 14)

        for marker_type in _MARKER_ORDER:
            row = wdg.QHBoxLayout()

            label = wdg.QLabel(_MARKER_LABELS[marker_type])
            label.setFixedWidth(80)

            btn = wdg.QPushButton()
            btn.setFixedHeight(26)
            self._refresh_button(btn, self._frame_marker.markers_colors[marker_type])
            btn.clicked.connect(lambda *args, mt=marker_type: self._pick_color(mt))

            self._buttons[marker_type] = btn
            row.addWidget(label)
            row.addWidget(btn)
            root.addLayout(row)

        root.addSpacing(10)

        footer = wdg.QHBoxLayout()
        reset_btn = wdg.QPushButton('Reset Defaults')
        reset_btn.clicked.connect(self._reset_defaults)
        close_btn = wdg.QPushButton('Close')
        close_btn.clicked.connect(self.accept)
        footer.addWidget(reset_btn)
        footer.addWidget(close_btn)
        root.addLayout(footer)

    def _pick_color(self, marker_type):
        current = gui.QColor(self._frame_marker.markers_colors[marker_type])
        current.setAlpha(255)

        picked = wdg.QColorDialog.getColor(
            current, self,
            'Color for {0}'.format(_MARKER_LABELS[marker_type])
        )
        if not picked.isValid():
            return

        self._apply_color(marker_type, picked)

    def _reset_defaults(self):
        ud = UserData()
        for marker_type, hex_color in _MARKER_DEFAULTS.items():
            color = gui.QColor(hex_color)
            self._apply_color(marker_type, color, user_data=ud)
        UserData.store_user_data(ud.user_data, c.PATH.USER_DATA_FILE)

    def _apply_color(self, marker_type, color, user_data=None):
        self._refresh_button(self._buttons[marker_type], color)
        self._frame_marker.set_marker_color(marker_type, color)
        if user_data is None:
            ud = UserData()
            ud.user_data[_USER_DATA_KEYS[marker_type]] = color.name()
            UserData.store_user_data(ud.user_data, c.PATH.USER_DATA_FILE)
        else:
            user_data.user_data[_USER_DATA_KEYS[marker_type]] = color.name()

    @staticmethod
    def _refresh_button(btn, color):
        c = gui.QColor(color)
        c.setAlpha(255)
        btn.setStyleSheet(
            'QPushButton {{ background-color: {0}; border: 1px solid #555; }}'
            'QPushButton:hover {{ border: 1px solid #bbb; }}'.format(c.name())
        )
