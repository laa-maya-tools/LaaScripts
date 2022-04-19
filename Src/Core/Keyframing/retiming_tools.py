import maya.cmds as cmd

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils


class RetimingTools(object):

    def __init__(self):
        print('retiming')

    def retime_keys(self, retime_value, incremental, move_to_next):
        range_start_time, range_end_time = TimelineUtils.get_selected_range()
        start_keyframe_time = TimelineUtils.get_start_keyframe_time(range_start_time)
        last_keyframe_time = TimelineUtils.get_last_keyframe_time()
        current_time = start_keyframe_time

        new_keyframe_times = [start_keyframe_time]
        current_keyframe_values = [start_keyframe_time]

        while current_time != last_keyframe_time:
            next_keyframe_time = TimelineUtils.find_keyframe(c.NEXT, current_time)

            if incremental:
                time_diff = next_keyframe_time - current_time
                if current_time < range_end_time:
                    time_diff += retime_value
                    if time_diff < 1:
                        time_diff = 1
            else:
                if current_time < range_end_time:
                    time_diff = retime_value
                else:
                    time_diff = next_keyframe_time - current_time

            new_keyframe_times.append(new_keyframe_times[-1] + time_diff)
            current_time = next_keyframe_time

            current_keyframe_values.append(current_time)

        if len(new_keyframe_times) > 1:
            self.retime_keys_recursive(start_keyframe_time, 0, new_keyframe_times)

        first_keyframe_time = TimelineUtils.find_keyframe(c.FIRST)

        if move_to_next and range_start_time >= first_keyframe_time:
            next_keyframe_time = TimelineUtils.find_keyframe(c.NEXT, start_keyframe_time)
            TimelineUtils.set_current_time(next_keyframe_time)
        elif range_end_time > first_keyframe_time:
            TimelineUtils.set_current_time(start_keyframe_time)
        else:
            TimelineUtils.set_current_time(range_start_time)

    def retime_keys_recursive(self, current_time, index, new_keyframe_times):
        if index >= len(new_keyframe_times):
            return

        updated_keyframe_time = new_keyframe_times[index]
        next_keyframe_time = TimelineUtils.find_keyframe(c.NEXT, current_time)

        if updated_keyframe_time < next_keyframe_time:
            TimelineUtils.change_keyframe_time(current_time, updated_keyframe_time)
            self.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
        else:
            self.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
            TimelineUtils.change_keyframe_time(current_time, updated_keyframe_time)


if __name__ == "__main__":
    rt = RetimingTools()
    rt.retime_keys(1, True, False)

