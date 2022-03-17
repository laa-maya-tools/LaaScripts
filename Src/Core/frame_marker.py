# =========================================================================== #
# frame_marker.py                                                             #
# ---------------------------------------------------------                   #
# SUMMARY:  Add, edit or delete markers on the selected frames.               #
# AUTHOR:   Leandro Adeodato                                                  #
# VERSION:  1.0.0 | Maya 2018 | Python 2                                      #
# =========================================================================== #
import maya.cmds as cmd

from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as cor

from .._Utils import utils as utl
from .._Data import scene_data as scd
from .._Constants import constants as cns


reload(utl)
reload(scd)

FRAMES, TYPES = 'frames', 'types'
KEY, BREAKDOWN, INBETWEEN, ALL = 0, 1, 2, 3
INDEX, FRAME, TYPE = 0, 1, 2
TIME_CONTROL_OBJ = "$gPlayBackSlider"

global AK_FRAME_MARKER


class FrameMarker(wdg.QWidget):

    def __init__(self):
        self._scene_data = scd.SceneData()
        self.time_control = utl.Utils.get_maya_control(cns.TIME_CONTROL)

        super(FrameMarker, self).__init__(self.time_control)

        self.markers_colors = {
            KEY: gui.QColor(cor.Qt.red),
            BREAKDOWN: gui.QColor(cor.Qt.green),
            INBETWEEN: gui.QColor(cor.Qt.yellow)
        }

        self.markers = {
            FRAMES: [],
            TYPES: []
        }

        self.initiate_markers()

    # =========================================================================
    # INITIATE MARKERS
    # =========================================================================
    def initiate_markers(self):
        markers = self._scene_data.load_scene_data('ak_frame_markers')
        if markers:
            self.markers = markers

    # =========================================================================
    # REFRESH MARKERS
    # =========================================================================
    def refresh_markers(self):
        self._scene_data.store_scene_data('ak_frame_markers', self.markers)
        self.update()

    # =========================================================================
    # ADD FRAME MARKERS
    # =========================================================================
    def add_frame_markers(self, type):
        print 'add frame markers'
        frames = self.get_timeline_range()
        for frame in frames:
            self.add_frame_marker(frame, type)

    # =========================================================================
    # ADD FRAME MARKER
    # =========================================================================
    def add_frame_marker(self, frame, type):
        frames = self.markers[FRAMES]
        types = self.markers[TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            frames.append(frame)
            types.append(type)
        else:
            types[index] = type

        self.markers[FRAMES] = frames
        self.markers[TYPES] = types
        self.refresh_markers()

    # =========================================================================
    # REMOVE FRAME MARKERS
    # =========================================================================
    def remove_frame_markers(self):
        print 'remove frame markers'
        frames = self.get_timeline_range()
        for frame in frames:
            self.remove_frame_marker(frame)

    # =========================================================================
    # REMOVE FRAME MARKER
    # =========================================================================
    def remove_frame_marker(self, frame):
        frames = self.markers[FRAMES]
        types = self.markers[TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            return

        frames.pop(index)
        types.pop(index)

        self.markers[FRAMES] = frames
        self.markers[TYPES] = types
        self.refresh_markers()

    # =========================================================================
    # CLEAR ALL FRAME MARKERS
    # =========================================================================
    def clear(self):
        self.markers[FRAMES] = []
        self.markers[TYPES] = []
        self.refresh_markers()

    # # =========================================================================
    # # CLEAR SELECTED FRAME MARKERS
    # # =========================================================================
    # def clear_selected_frame_markers(self):
    #     frame_times = self.get_selected_frame_times()
    #     for marker in self.markers:
    #         #print marker[FRAME]
    #         self.markers.remove(marker)
    #         # if marker[FRAME] in frame_times:
    #         #     del self.markers[index]
    #     self.refresh_markers()

    # =========================================================================
    # CLEAR ALL FRAME MARKERS
    # =========================================================================
    def clear_all_frame_markers(self):
        self.markers[FRAMES] = []
        self.markers[TYPES] = []
        self.refresh_markers()

    # =========================================================================
    # GET DATA FROM FRAME
    # =========================================================================
    def get_data_from_frame(self, frame):
        if frame in self.markers[FRAMES]:
            index = self.markers[FRAMES].index(frame)
            type = self.markers[TYPES][index]
            return index, frame, type
        return -1, frame, None

    # # =========================================================================
    # # GET MARKERS TIMES
    # # =========================================================================
    # def get_markers_times(self, marker_type):
    #     if marker_type == ALL:
    #         return sorted(self.markers.keys())
    #     markers_times = []
    #     for marker in sorted(self.markers.keys()):
    #         if self.markers[marker] == marker_type:
    #             markers_times.append(marker)
    #     return markers_times

    # =========================================================================
    # GET SELECTED FRAME TIMES
    # =========================================================================
    # def get_selected_frame_times(self):
    #     selected_range = self.get_selected_range()
    #     frame_times = []
    #     for frame_time in range(selected_range[0], selected_range[1]):
    #         frame_times.append(frame_time)
    #     return frame_times

    # # =========================================================================
    # # GET SELECTED RANGE
    # # =========================================================================
    # def get_selected_range(self):
    #     selected_range = cmd.timeControl(self.time_control, q=True, rangeArray=True)
    #     return [int(selected_range[0]), int(selected_range[1])]

    # =========================================================================
    # GET TIMELINE RANGE
    # =========================================================================
    def get_timeline_range(self):
        timeline_range = cmd.timeControl(self.time_control, q=True, rangeArray=True)
        return range(int(timeline_range[0]), int(timeline_range[1]))

    # =========================================================================
    # PAINT EVENT
    # =========================================================================
    def paintEvent(self, paint_event):
        if not self.markers[FRAMES] or not self.markers[TYPES]:
            return

        self.draw_frame_markers(KEY)
        self.draw_frame_markers(BREAKDOWN)
        self.draw_frame_markers(INBETWEEN)

    # =========================================================================
    # DRAW FRAME MARKERS
    # =========================================================================
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

            for frame_time in self.markers[FRAMES]:
                data = self.get_data_from_frame(frame_time)
                if data[TYPE] == marker_type:
                    frame_x = padding + ((frame_time - range_start) * frame_width) + 0.5
                    painter.fillRect(frame_x, frame_y, frame_width, frame_height, fill_color)
                    painter.drawRect(frame_x, frame_y, frame_width, frame_height)