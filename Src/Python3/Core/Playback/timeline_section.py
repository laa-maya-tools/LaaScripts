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
import random

from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as cor

from LaaScripts.Src.Python3.Constants import constants as c
from LaaScripts.Src.Python3.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Python3.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Python3.Utils import info_utils as info
from LaaScripts.Src.Python3.Data.scene_data import SceneData


global LAA_TIMELINE_SECTION


class TimelineSection(wdg.QWidget):

    def __init__(self):
        self.time_control = WidgetUtils.get_maya_control(c.TIME_CONTROL)
        self.time_control_widget = WidgetUtils.get_maya_control_widget(c.TIME_CONTROL)

        super(TimelineSection, self).__init__(self.time_control_widget)

        self.sections = {
            c.SECTION_RANGES: [],
            c.SECTION_COLORS: [],
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
                ranges.append((float(splitted_attr[0]), float(splitted_attr[1])))
                colors.append((int(splitted_attr[2]), int(splitted_attr[3])))

        self.sections[c.SECTION_RANGES] = ranges
        self.sections[c.SECTION_COLORS] = colors

    def refresh_sections(self):
        """
        Saves the frame sections from the dictionary to the scene nodes and updates the Gui.
        """
        sections = ''

        for range, color in zip(self.sections[c.SECTION_RANGES], self.sections[c.SECTION_COLORS]):
            sections = '{0}{1},{2},{3},{4}#'.format(sections, str(int(range[0])), str(int(range[1])), str(color[0]), str(color[1]))

        SceneData.save_scene_data(c.TIMELINE_SECTION_NODE, c.TIMELINE_SECTION_ATTR, sections[:-1])
        self.update()

    def get_all_colors(self):
        all_colors = []
        for color in range(0, c.COLOR_VARIATIONS):
            for brightness in range(0, c.BRIGHTNESS_VARIATIONS):
                all_colors.append([color, brightness])
        return all_colors

    def get_used_colors(self):
        used_colors = list(set(self.sections[c.SECTION_COLORS]))
        return used_colors

    def get_unused_colors(self):
        all_colors = self.get_all_colors()
        used_colors = self.get_used_colors()
        return [color for color in all_colors if color not in used_colors]

    def get_random_color(self):
        unused_colors = self.get_unused_colors()
        index = random.randint(0, len(unused_colors)-1)

        return unused_colors[index]

    def get_default_color(self):
        return [c.DARK_GREY, c.MEDIUM]

    def add_timeline_section(self, random_color):
        if random_color:
            section_color = self.get_random_color()
        else:
            section_color = self.get_default_color()

        section_range = TimelineUtils.get_selected_range()

        section_ranges = self.sections[c.SECTION_RANGES]
        section_colors = self.sections[c.SECTION_COLORS]
        section_index, _, _, = self.get_data_from_section(section_range)

        if section_index == -1:
            section_ranges.append(section_range)
            section_colors.append(section_color)
        else:
            section_colors[section_index] = section_color

        self.sections[c.SECTION_RANGES] = section_ranges
        self.sections[c.SECTION_COLORS] = section_colors
        self.refresh_sections()

    def remove_frame_sections(self):
        frames = TimelineUtils.get_selected_frame_times()
        for frame in frames:
            self.remove_frame_marker(frame)
        info.show_info('- Frame Marker')

    def remove_frame_marker(self, frame):
        ranges = self.sections[c.SECTION_RANGES]
        colors = self.sections[c.SECTION_COLORS]
        index, _, _, = self.get_data_from_frame(frame)

        if index == -1:
            return

        ranges.pop(index)
        colors.pop(index)

        self.sections[c.SECTION_RANGES] = ranges
        self.sections[c.SECTION_COLORS] = colors
        self.refresh_sections()

    def clear(self):
        self.sections[c.SECTION_RANGES] = []
        self.sections[c.SECTION_COLORS] = []
        self.refresh_sections()

    def clear_all_frame_sections(self):
        self.sections[c.SECTION_RANGES] = []
        self.sections[c.SECTION_COLORS] = []
        self.refresh_sections()

    def get_data_from_frame(self, frame):
        if frame in self.sections[c.FRAMES]:
            index = self.sections[c.FRAMES].index(frame)
            type = self.sections[c.TYPES][index]
            return index, frame, type
        return -1, frame, None

    def get_data_from_section(self, section_range):
        if section_range in self.sections[c.SECTION_RANGES]:
            section_index = self.sections[c.SECTION_RANGES].index(section_range)
            section_color = self.sections[c.SECTION_COLORS][section_index]
            return section_index, section_range, section_color
        return -1, section_range, None

    def paintEvent(self, event):
        if not self.sections[c.SECTION_RANGES] or not self.sections[c.SECTION_COLORS]:
            return

        for index, range in enumerate(self.sections[c.SECTION_RANGES]):
            self.draw_timeline_section(
                range[0],
                range[1],
                self.sections[c.SECTION_COLORS][index][0],
                self.sections[c.SECTION_COLORS][index][1])

    def draw_timeline_section(self, start_time, end_time, color, brightness):
        parent = self.parentWidget()
        if not parent:
            return

        self.setGeometry(parent.geometry())

        playback_range = TimelineUtils.get_playback_range()
        playback_start = playback_range[0]
        playback_end = playback_range[1]
        section_length = playback_end - playback_start + 1

        padding = self.width() * 0.005
        frame_width = (self.width() * 0.99) / section_length
        section_height = 0.04 * self.height()
        section_y = self.height() - section_height

        painter = gui.QPainter(self)
        pen = painter.pen()
        pen.setWidth(1)
        pen.setColor(c.COLORS[color][brightness])
        painter.setPen(pen)

        fill_color = c.COLORS[color][brightness]
        section_width = (end_time - start_time + 1) * frame_width
        section_x = padding + ((start_time - playback_start) * frame_width) + 0.5
        painter.fillRect(section_x, section_y, section_width, section_height, fill_color)
        painter.drawRect(section_x, section_y, section_width, section_height)
