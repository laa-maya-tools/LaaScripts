"""
=============================================================================
MODULE: frame_marker.py
-----------------------------------------------------------------------------
Adds, Remove or Clear Frame Markers on the timeline.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
from LaaScripts.Src.constants import constants as c
from LaaScripts.Src.data.scene_data import SceneData
from LaaScripts.Src.utils.scene import info_utils as info
from LaaScripts.Src.utils.animation.timeline_utils import TimelineUtils
from LaaScripts.Src.utils.ui.widget_utils import WidgetUtils
from LaaScripts.Src.utils.qt_compat import QtGui as gui, QtWidgets as wdg
from LaaScripts.Src.data.user_data import UserData

global LAA_FRAME_MARKER


class FrameMarker(wdg.QWidget):

    def __init__(self):
        self.time_control = WidgetUtils.get_maya_control(c.MAYA_CONTROLS.TIME_CONTROL)
        self.time_control_widget = WidgetUtils.get_maya_control_widget(c.MAYA_CONTROLS.TIME_CONTROL)

        super(FrameMarker, self).__init__(self.time_control_widget)

        ud = UserData().user_data
        self.markers_colors = {
            c.PLAYBACK.KEY:       gui.QColor(ud.get(c.USER_DATA.MARKER_COLOR_KEY,       c.PLAYBACK.COLOR_KEY)),
            c.PLAYBACK.BREAKDOWN: gui.QColor(ud.get(c.USER_DATA.MARKER_COLOR_BREAKDOWN, c.PLAYBACK.COLOR_BREAKDOWN)),
            c.PLAYBACK.INBETWEEN: gui.QColor(ud.get(c.USER_DATA.MARKER_COLOR_INBETWEEN, c.PLAYBACK.COLOR_INBETWEEN)),
            c.PLAYBACK.CUSTOM:    gui.QColor(ud.get(c.USER_DATA.MARKER_COLOR_CUSTOM,    c.PLAYBACK.COLOR_CUSTOM)),
        }

        self.markers = {
            c.PLAYBACK.FRAMES: [],
            c.PLAYBACK.TYPES: []
        }

        self.initiate_markers()
        self.refresh_markers()

    def initiate_markers(self):
        """
        Initiates the the frame markers stored in the scene.
        """
        markers = SceneData.load_scene_data(c.NODES.FRAME_MARKER_NODE, c.NODES.FRAME_MARKERS_ATTR).split('#')
        frames, types = [], []

        if not markers[0] == '':
            for marker in markers:
                frames.append(float(marker.split(',')[0]))
                types.append(int(marker.split(',')[1]))

        self.markers[c.PLAYBACK.FRAMES] = frames
        self.markers[c.PLAYBACK.TYPES] = types

    def refresh_markers(self):
        """
        Saves the frame markers from the dictionary to the scene nodes and updates the Gui.
        """
        markers = ''

        for f, t in zip(self.markers[c.PLAYBACK.FRAMES], self.markers[c.PLAYBACK.TYPES]):
            markers = markers + str(int(f)) + ',' + str(t) + '#'

        SceneData.save_scene_data(c.NODES.FRAME_MARKER_NODE, c.NODES.FRAME_MARKERS_ATTR, markers[:-1])
        self.update()

    def add_frame_markers(self, type):
        """
        Adds frame markers.
        :param int type: Frame marker type (key, breakdown or inbetween).
        """
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.add_frame_marker(frame, type)
        info.show_info('+ {0} Marker'.format(c.PLAYBACK.MARKER_TYPE_NAMES[type]))

    def add_frame_marker(self, frame, type):
        """

        :param frame:
        :param type:
        :return:
        """
        frames = self.markers[c.PLAYBACK.FRAMES]
        types = self.markers[c.PLAYBACK.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            frames.append(frame)
            types.append(type)
        else:
            types[index] = type

        self.markers[c.PLAYBACK.FRAMES] = frames
        self.markers[c.PLAYBACK.TYPES] = types
        self.refresh_markers()

    def remove_frame_markers(self):
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.remove_frame_marker(frame)
        info.show_info('- FRAME Marker')

    def remove_frame_marker(self, frame):
        frames = self.markers[c.PLAYBACK.FRAMES]
        types = self.markers[c.PLAYBACK.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            return

        frames.pop(index)
        types.pop(index)

        self.markers[c.PLAYBACK.FRAMES] = frames
        self.markers[c.PLAYBACK.TYPES] = types
        self.refresh_markers()

    def clear(self):
        self.markers[c.PLAYBACK.FRAMES] = []
        self.markers[c.PLAYBACK.TYPES] = []
        self.refresh_markers()

    def clear_all_frame_markers(self):
        self.markers[c.PLAYBACK.FRAMES] = []
        self.markers[c.PLAYBACK.TYPES] = []
        self.refresh_markers()

    def get_data_from_frame(self, frame):
        if frame in self.markers[c.PLAYBACK.FRAMES]:
            index = self.markers[c.PLAYBACK.FRAMES].index(frame)
            type = self.markers[c.PLAYBACK.TYPES][index]
            return index, frame, type
        return -1, frame, None

    def set_marker_color(self, marker_type, color):
        self.markers_colors[marker_type] = gui.QColor(color)
        self.update()

    def paintEvent(self, event):
        if not self.markers[c.PLAYBACK.FRAMES] or not self.markers[c.PLAYBACK.TYPES]:
            return

        self.draw_frame_markers(c.PLAYBACK.KEY)
        self.draw_frame_markers(c.PLAYBACK.BREAKDOWN)
        self.draw_frame_markers(c.PLAYBACK.INBETWEEN)
        self.draw_frame_markers(c.PLAYBACK.CUSTOM)

    def draw_frame_markers(self, marker_type):
        parent = self.parentWidget()
        if parent:
            self.setGeometry(parent.geometry())

            range_start = cmd.playbackOptions(q=True, minTime=True)
            range_end = cmd.playbackOptions(q=True, maxTime=True)
            displayed_frame_count = range_end - range_start + 1

            padding = self.width() * 0.005
            frame_width = (self.width() * 0.99) / displayed_frame_count
            frame_height = 0.25 * self.height()
            frame_y = self.height() - frame_height

            painter = gui.QPainter(self)
            pen = painter.pen()
            pen.setWidth(1)
            pen.setColor(self.markers_colors[marker_type])
            painter.setPen(pen)

            fill_color = gui.QColor(self.markers_colors[marker_type])
            fill_color.setAlpha(75)

            for frame_time in self.markers[c.PLAYBACK.FRAMES]:
                data = self.get_data_from_frame(frame_time)
                if data[c.PLAYBACK.TYPE] == marker_type:
                    frame_x = padding + ((frame_time - range_start) * frame_width) + 0.5
                    painter.fillRect(frame_x, frame_y, frame_width, frame_height, fill_color)
                    painter.drawRect(frame_x, frame_y, frame_width, frame_height)
