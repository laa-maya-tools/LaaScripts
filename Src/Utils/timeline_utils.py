"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to get/set timeline keyframing
data.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Utils.widget_utils import WidgetUtils
from LaaScripts.Src.Constants import constants as c


class TimelineUtils(object):

    @staticmethod
    def get_current_time():
        """
        Gets the current frame.
        :return: Current frame.
        :rtype: float
        """
        return cmd.currentTime(query=True)

    @staticmethod
    def set_current_time(current_time):
        """
        Sets the current frame.
        :param float current_time: Current frame.
        """
        cmd.currentTime(current_time, edit=True)

    @staticmethod
    def get_playback_range(option=c.ALL_RANGE):
        """
        Get the entire playback range, the playback range from start to the current frame or the playback
        range from current frame to the end.
        :param int option: ALL_RANGE(0), BEFORE_CURRENT_FRAME(1), AFTER_CURRENT_FRAME(2)
        :return: playback range
        :rtype: [float, float]
        """
        current_time = TimelineUtils().get_current_time()
        playback_start_time = cmd.playbackOptions(minTime=True, query=True)
        playback_end_time = cmd.playbackOptions(maxTime=True, query=True)

        if option == c.BEFORE_CURRENT_TIME:
            return [int(playback_start_time), int(current_time)]
        elif option == c.AFTER_CURRENT_TIME:
            return [int(current_time), int(playback_end_time)]
        else:
            return [int(playback_start_time), int(playback_end_time)]

    @staticmethod
    def get_animation_range(option=c.ALL_RANGE):
        """
        Get the entire animation range, the playback range from start to the current frame or the
        animation range from current frame to the end.
        :param int option: ALL_RANGE(0), BEFORE_CURRENT_FRAME(1), AFTER_CURRENT_FRAME(2)
        :return: animation range
        :rtype: [int, int]
        """
        current_time = TimelineUtils().get_current_time()
        animation_start_time = cmd.playbackOptions(animationStartTime=True, query=True)
        animation_end_time = cmd.playbackOptions(animationEndTime=True, query=True)

        if option == c.BEFORE_CURRENT_TIME:
            return [int(animation_start_time), int(current_time)]
        elif option == c.AFTER_CURRENT_TIME:
            return [int(current_time), int(animation_end_time)]
        else:
            return [int(animation_start_time), int(animation_end_time)]

    @staticmethod
    def get_selected_range():
        """
        Gets the selected timeline range.
        :return: [Selection start time, Selection end time].
        :rtype: list of float
        """
        time_control = mel.eval("$tempVar={0}".format(c.TIME_CONTROL))
        timeline_range = cmd.timeControl(time_control, q=True, rangeArray=True)
        return [int(timeline_range[0]), int(timeline_range[1])]

    @staticmethod
    def get_selected_frame_times():
        """
        Gets the frame times on a selected range.
        :return: List of frame times.
        :rtype: list of float
        """
        timeline_range = TimelineUtils.get_selected_range()
        return range(int(timeline_range[0]), int(timeline_range[1]))



    @staticmethod
    def set_playback_range(start, end):
        """
        Sets the playback range.
        :param float start: Playback start time.
        :param float end: Playback end time.
        """
        cmd.playbackOptions(minTime=start)
        cmd.playbackOptions(maxTime=end)

    @staticmethod
    def set_animation_range(start, end):
        """
        Sets the Animation range.
        :param float start: Animation start time.
        :param float end: Animation end time.
        """
        cmd.playbackOptions(animationStartTime=start)
        cmd.playbackOptions(animationEndTime=end)

    @staticmethod
    def find_keyframe(which, time=None):
        """
        Finds the neighbor keyframe of a specified time.
        :param str which: Previous, Next, First or Last.
        :param float time: Keytime.
        """
        kwargs = {'which': which}
        if which in [c.NEXT, c.PREVIOUS]:
            kwargs['time'] = (time, time)

        return cmd.findKeyframe(**kwargs)

    @staticmethod
    def change_keyframe_time(current_time, new_time):
        """
        Changes keyframe time.
        :param float current_time: Current time.
        :param float new_time: New time.
        """
        cmd.keyframe(e=True, time=(current_time, current_time), timeChange=new_time)

    @staticmethod
    def get_start_keyframe_time(range_start_time):
        """
        Gets the start time.
        """
        start_times = cmd.keyframe(q=True, time=(range_start_time, range_start_time))
        if start_times:
            return start_times[0]
        start_time = TimelineUtils.find_keyframe(c.PREVIOUS, range_start_time)
        return start_time

    @staticmethod
    def get_last_keyframe_time():
        """
        Gets the last keyframe time.
        """
        return TimelineUtils.find_keyframe(c.LAST)

    @staticmethod
    def is_playing():
        return cmd.play(q=True, state=True)

    @staticmethod
    def play_timeline_forward():
        cmd.play(forward=True)

    @staticmethod
    def play_timeline_back():
        cmd.play(forward=False)

    @staticmethod
    def stop_timeline():
        cmd.play(state=False)

