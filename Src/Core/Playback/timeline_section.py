"""
=============================================================================
MODULE: frame_marker.py
-----------------------------------------------------------------------------
Adds, Remove or Clear Frame sections on the timeline.
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
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Data.scene_data import SceneData


global LAA_TIMELINE_SECTION


class TimelineSection(wdg.QWidget):

    def __init__(self):
        self.time_control = WidgetUtils.get_maya_control(c.TIME_CONTROL)
        self.time_control_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)

        super(TimelineSection, self).__init__(self.time_control_widget)

        self.sections = {
            c.RANGES: [],
            c.COLORS: []
        }

        self.initiate_sections()
        self.refresh_sections()

    def initiate_sections(self):
        """
        Initiates the the frame sections stored in the scene.
        """
        sections = SceneData.load_scene_data(c.TIMELINE_SECTION_NODE, c.TIMELINE_SECTION_ATTR).split('#')
        ranges, colors = [], []

        if not sections[0] == '':
            for section in sections:
                splitted_attr = section.split(',')
                ranges.append([float(splitted_attr[0]), float(splitted_attr[1])])
                colors.append([int(splitted_attr[2]), int(splitted_attr[3])])

        self.sections[c.SECTION_RANGES] = ranges
        self.sections[c.SECTION_COLORS] = colors

    def refresh_sections(self):
        """
        Saves the frame sections from the dictionary to the scene nodes and updates the Gui.
        """
        sections = ''

        for f, t in itertools.izip(self.sections[c.FRAMES], self.sections[c.TYPES]):
            sections = sections + str(int(f)) + ',' + str(t) + '#'

        SceneData.save_scene_data(c.FRAME_MARKER_NODE, c.FRAME_sections_ATTR, sections[:-1])
        self.update()

    def add_frame_sections(self, type):
        """
        Adds frame sections.
        :param int type: Frame marker type (key, breakdown or inbetween).
        """
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.add_frame_marker(frame, type)
        info.show_info('+ {0} Marker'.format(c.MARKER_TYPE_NAMES[type]))

    def add_frame_marker(self, frame, type):
        """

        :param frame:
        :param type:
        :return:
        """
        frames = self.sections[c.FRAMES]
        types = self.sections[c.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            frames.append(frame)
            types.append(type)
        else:
            types[index] = type

        self.sections[c.FRAMES] = frames
        self.sections[c.TYPES] = types
        self.refresh_sections()

    def remove_frame_sections(self):
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.remove_frame_marker(frame)
        info.show_info('- Frame Marker')

    def remove_frame_marker(self, frame):
        frames = self.sections[c.FRAMES]
        types = self.sections[c.TYPES]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            return

        frames.pop(index)
        types.pop(index)

        self.sections[c.FRAMES] = frames
        self.sections[c.TYPES] = types
        self.refresh_sections()

    def clear(self):
        self.sections[c.FRAMES] = []
        self.sections[c.TYPES] = []
        self.refresh_sections()

    def clear_all_frame_sections(self):
        self.sections[c.FRAMES] = []
        self.sections[c.TYPES] = []
        self.refresh_sections()

    def get_data_from_frame(self, frame):
        if frame in self.sections[c.FRAMES]:
            index = self.sections[c.FRAMES].index(frame)
            type = self.sections[c.TYPES][index]
            return index, frame, type
        return -1, frame, None

    def paintEvent(self, event):
        if not self.sections[c.FRAMES] or not self.sections[c.TYPES]:
            return

        self.draw_frame_sections(c.KEY)
        self.draw_frame_sections(c.BREAKDOWN)
        self.draw_frame_sections(c.INBETWEEN)

    def draw_frame_sections(self, marker_type):
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
            pen.setColor(self.sections_colors[marker_type])
            painter.setPen(pen)

            fill_color = self.sections_colors[marker_type]
            fill_color.setAlpha(75)

            for frame_time in self.sections[c.FRAMES]:
                data = self.get_data_from_frame(frame_time)
                if data[c.TYPE] == marker_type:
                    frame_x = padding + ((frame_time - range_start) * frame_width) + 0.5
                    painter.fillRect(frame_x, frame_y, frame_width, frame_height, fill_color)
                    painter.drawRect(frame_x, frame_y, frame_width, frame_height)
