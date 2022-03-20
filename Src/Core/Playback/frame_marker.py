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
import itertools

from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as cor

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Data.scene_data import SceneData

global LAA_FRAME_MARKER


class FrameMarker(wdg.QWidget):

    def __init__(self):
        self.time_control = WidgetUtils.get_maya_control(c.TIME_CONTROL)
        self.time_control_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)

        super(FrameMarker, self).__init__(self.time_control_widget)

        self.markers_colors = {
            c.KEY: gui.QColor(cor.Qt.red),
            c.BREAKDOWN: gui.QColor(cor.Qt.green),
            c.INBETWEEN: gui.QColor(cor.Qt.yellow)
        }

        self.markers = {
            c.FRAMES: [],
            c.TYPES: []
        }

        self.initiate_markers()
        self.refresh_markers()

    def initiate_markers(self):
        """
        Initiates the the frame markers stored in the scene.
        """
        markers = SceneData.load_scene_data(c.FRAME_MARKER_NODE, c.FRAME_MARKERS_ATTR).split('#')
        frames, types = [], []

        if not markers[0] == '':
            for marker in markers:
                frames.append(float(marker.split(',')[0]))
                types.append(int(marker.split(',')[1]))

        self.markers[c.FRAMES] = frames
        self.markers[c.TYPES] = types

    def refresh_markers(self):
        """
        Saves the frame markers from the dictionary to the scene nodes and updates the Gui.
        """
        markers = ''

        for frame in self.markers[c.FRAMES]:
            print frame

        for f, t in itertools.izip(self.markers[c.FRAMES], self.markers[c.TYPES]):
            print f, t
            markers = markers + str(int(f)) + ',' + str(t) + '#'

        SceneData.save_scene_data(c.FRAME_MARKER_NODE, c.FRAME_MARKERS_ATTR, markers[:-1])
        self.update()

    def add_frame_markers(self, type):
        """
        Adds frame markers.
        :param int type: Frame marker type (key, breakdown or inbetween).
        """
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.add_frame_marker(frame, type)

    def add_frame_marker(self, frame, type):
        """

        :param frame:
        :param type:
        :return:
        """
        frames = self.markers[c.FRAMES]
        types = self.markers[c.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            frames.append(frame)
            types.append(type)
        else:
            types[index] = type

        self.markers[c.FRAMES] = frames
        self.markers[c.TYPES] = types
        self.refresh_markers()

    def remove_frame_markers(self):
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.remove_frame_marker(frame)

    def remove_frame_marker(self, frame):
        frames = self.markers[c.FRAMES]
        types = self.markers[c.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            return

        frames.pop(index)
        types.pop(index)

        self.markers[c.FRAMES] = frames
        self.markers[c.TYPES] = types
        self.refresh_markers()

    def clear(self):
        self.markers[c.FRAMES] = []
        self.markers[c.TYPES] = []
        self.refresh_markers()

    def clear_all_frame_markers(self):
        self.markers[c.FRAMES] = []
        self.markers[c.TYPES] = []
        self.refresh_markers()

    def get_data_from_frame(self, frame):
        if frame in self.markers[c.FRAMES]:
            index = self.markers[c.FRAMES].index(frame)
            type = self.markers[c.TYPES][index]
            return index, frame, type
        return -1, frame, None

    def paintEvent(self, event):
        if not self.markers[c.FRAMES] or not self.markers[c.TYPES]:
            return

        self.draw_frame_markers(c.KEY)
        self.draw_frame_markers(c.BREAKDOWN)
        self.draw_frame_markers(c.INBETWEEN)

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

            fill_color = self.markers_colors[marker_type]
            fill_color.setAlpha(75)

            for frame_time in self.markers[c.FRAMES]:
                data = self.get_data_from_frame(frame_time)
                if data[c.TYPE] == marker_type:
                    frame_x = padding + ((frame_time - range_start) * frame_width) + 0.5
                    painter.fillRect(frame_x, frame_y, frame_width, frame_height, fill_color)
                    painter.drawRect(frame_x, frame_y, frame_width, frame_height)
