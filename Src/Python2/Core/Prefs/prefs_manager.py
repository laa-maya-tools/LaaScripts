# =============================================================================
# SCRIPT: Hotkey Manager v1.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Loops through all hotkey sets.
# =============================================================================
from PySide2 import QtWidgets as wdg

import maya.cmds as cmd

from LaaScripts.Src.Python2.Constants import constants as c
from LaaScripts.Src.Python2.Utils import info_utils as info
from LaaScripts.Src.Python2.Utils.graph_utils import GraphUtils
from LaaScripts.Src.Python2.Utils.widget_utils import WidgetUtils


class PrefsManager(object):

    @staticmethod
    def get_tangents():
        return cmd.keyTangent(q=True, g=True, ott=True)[0]

    @staticmethod
    def set_tangents(in_tangent, out_tangent):
        curves_selected = GraphUtils.get_selection_from_outliner()
        key_count = GraphUtils.count_selected_keys()

        if key_count == 0:
            cmd.keyTangent(g=True, itt=in_tangent)
            cmd.keyTangent(g=True, ott=out_tangent)
            info.show_info('Tangents Prefs: {0}'.format(out_tangent.upper()))
        else:
            for curve in curves_selected:
                cmd.keyTangent(curve, itt=in_tangent, ott=out_tangent)
            info.show_info('Key Tangents: {0}'.format(out_tangent.upper()))

    @staticmethod
    def toggle_tangents():
        current_tangents = PrefsManager.get_tangents()
        if current_tangents == 'auto':
            PrefsManager.set_tangents('linear', 'step')
        elif current_tangents == 'step':
            PrefsManager.set_tangents('linear', 'linear')
        else:
            PrefsManager.set_tangents('auto', 'auto')

    @staticmethod
    def set_timeline_height(timeline_height):
        timeline_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)
        timeline_widget.setFixedHeight(timeline_height)
        timeline_widget.setSizePolicy(wdg.QSizePolicy.Minimum, wdg.QSizePolicy.Minimum)
        info.show_info('Timeline Height: {0}'.format(str(timeline_height)))

    @staticmethod
    def toggle_timeline_height():
        timeline_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)
        timeline_height = timeline_widget.size().height()
        if timeline_height == 32:
            PrefsManager.set_timeline_height(64)
        elif timeline_height == 64:
            PrefsManager.set_timeline_height(128)
        else:
            PrefsManager.set_timeline_height(32)


if __name__ == "__main__":
    PrefsManager.set_tangents('auto', 'auto')

