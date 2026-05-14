# =============================================================================
# SCRIPT: Hotkey Manager v1.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Loops through all hotkey sets.
# =============================================================================
from collections import namedtuple
from functools import wraps

from PySide2 import QtWidgets as wdg

import maya.cmds as cmd
from LaaScripts.Src.Constants import constants_bck as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Utils.graph_utils import GraphUtils


class PrefsManager(object):

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
    def set_timeline_height(timeline_height):
        timeline_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)
        timeline_widget.setFixedHeight(timeline_height)
        timeline_widget.setSizePolicy(wdg.QSizePolicy.Minimum, wdg.QSizePolicy.Minimum)
        info.show_info('Timeline Height: {0}'.format(str(timeline_height)))
