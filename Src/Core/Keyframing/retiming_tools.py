import maya.mel as mel

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Utils.selection_utils import SelectionUtils


class RetimingTools(object):

    def __init__(self):
        pass

    def set_smart_key(self):
        try:
            mel.eval('ackSliceCurves;')
            info.show_info('Keys Copied')
        except:
            info.show_info('No object is selected.')

    def copy_keys(self):
        selection = SelectionUtils.list_selected_objects()
        if selection == c.STRING.EMPTY:
            info.show_info('No Object is Selected', c.warning_msg.color, c.warning_msg.background, c.warning_msg.border)
            return

        mel.eval('timeSliderCopyKey;')
        info.show_info('Keys Copied')

    def paste_keys(self):
        selection = SelectionUtils.list_selected_objects()
        if selection == c.STRING.EMPTY:
            info.show_info('No Object is Selected', c.warning_msg.color, c.warning_msg.background, c.warning_msg.border)
            return

        mel.eval('performPasteKeyArgList 1 {"0", "animationList", "0"}')
        info.show_info('Keys Pasted')

    def cut_keys(self):
        selection = SelectionUtils.list_selected_objects()
        if selection == c.STRING.EMPTY:
            info.show_info('No Object is Selected', c.warning_msg.color, c.warning_msg.background, c.warning_msg.border)
            return

        mel.eval('timeSliderCutKey;')
        info.show_info('Keys Cut')

    def retime_keys(self, retime_value, incremental, move_to_next):
        range_start_time, range_end_time = TimelineUtils.get_selected_range()
        start_keyframe_time = TimelineUtils.get_start_keyframe_time(range_start_time)
        last_keyframe_time = TimelineUtils.get_last_keyframe_time()
        current_time = start_keyframe_time

        new_keyframe_times = [start_keyframe_time]
        current_keyframe_values = [start_keyframe_time]

        while current_time != last_keyframe_time:
            next_keyframe_time = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, current_time)

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

        first_keyframe_time = TimelineUtils.find_keyframe(c.TIMELINE.FIRST)

        if move_to_next and range_start_time >= first_keyframe_time:
            next_keyframe_time = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, start_keyframe_time)
            TimelineUtils.set_current_time(next_keyframe_time)
        elif range_end_time > first_keyframe_time:
            TimelineUtils.set_current_time(start_keyframe_time)
        else:
            TimelineUtils.set_current_time(range_start_time)

    def retime_keys_recursive(self, current_time, index, new_keyframe_times):
        if index >= len(new_keyframe_times):
            return

        updated_keyframe_time = new_keyframe_times[index]
        next_keyframe_time = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, current_time)

        if updated_keyframe_time < next_keyframe_time:
            TimelineUtils.change_keyframe_time(current_time, updated_keyframe_time)
            self.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
        else:
            self.retime_keys_recursive(next_keyframe_time, index + 1, new_keyframe_times)
            TimelineUtils.change_keyframe_time(current_time, updated_keyframe_time)

    def nudge_key_right(self, time_increment):
        print('nudge_key_right')

    def nudge_key_left(self, time_increment):
        pass

    def add_inbetween(self, time_increment=1):
        i = 1
        while i <= time_increment:
            TimelineUtils.add_inbetween()
            i += 1

    def remove_inbetween(self, time_increment=1):
        i = 1
        current_time = TimelineUtils.get_current_time()
        next_key = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, current_time)

        if current_time < next_key - time_increment:
            while i <= time_increment:
                TimelineUtils.remove_inbetween()
                i += 1
        else:
            TimelineUtils.remove_inbetween()

    def push_prev_key(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()
        prev_key = TimelineUtils.find_keyframe(c.TIMELINE.PREVIOUS, current_time)

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return False

        if current_time in key_times:
            if not (current_time - 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(current_time, current_time - 1)
                    TimelineUtils.set_current_time(current_time - 1)
                    info.show_info('Key Nudged Left')
                    return True
                except RuntimeError:
                    info.show_info('Curves Keytimes Cannot be Selected.')
                    return False
        else:
            if not (prev_key - 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(prev_key, prev_key - 1)
                    info.show_info('Previous Key Pushed')
                    return True
                except RuntimeError:
                    info.show_info('Curves Keytimes Cannot be Selected.')
                    return False

        info.show_info('Key Cannot be Moved')
        return False

    def push_next_key(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()
        next_key = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, current_time)

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        if current_time in key_times:
            if not (current_time + 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(current_time, current_time + 1)
                    TimelineUtils.set_current_time(current_time + 1)
                    info.show_info('Key Nudged Right')
                    return True
                except RuntimeError:
                    info.show_info('Curves Keytimes Cannot be Selected.')
                    return False
        else:
            if not (next_key + 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(next_key, next_key + 1)
                    info.show_info('Next Key Pushed')
                    return True
                except RuntimeError:
                    info.show_info('Curves Keytimes Cannot be Selected.')
                    return False

        info.show_info('Key Cannot be Moved')
        return False

    def push_prev_keys(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        first_key = TimelineUtils.get_first_key()
        TimelineUtils.set_current_time(first_key - 1)
        TimelineUtils.remove_inbetween()
        TimelineUtils.set_current_time(current_time)
        self.push_next_keys()
        info.show_info('Keys [Before Current] Pushed')

    def push_next_keys(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        if current_time in key_times:
            TimelineUtils.set_current_time(current_time - 1)
            TimelineUtils.add_inbetween()
            TimelineUtils.set_current_time(current_time)
        else:
            TimelineUtils.add_inbetween()
        info.show_info('Keys [After Current] Pushed')

    def pull_prev_key(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()
        prev_key = TimelineUtils.find_keyframe(c.TIMELINE.PREVIOUS, current_time)

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        if current_time in key_times:
            if not (current_time + 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(current_time, current_time + 1)
                    TimelineUtils.set_current_time(current_time + 1)
                    info.show_info('Key Nudged Left')
                    return True
                except RuntimeError:
                    info.show_info('Key Cannot be Moved')
                    return False
        else:
            if not (prev_key + 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(prev_key, prev_key + 1)
                    info.show_info('Previous Key Pushed')
                    return True
                except RuntimeError:
                    info.show_info('Key Cannot be Moved')
                    return False

        info.show_info('Key Cannot be Moved')
        return False

    def pull_next_key(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()
        next_key = TimelineUtils.find_keyframe(c.TIMELINE.NEXT, current_time)

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        if current_time in key_times:
            if not (current_time - 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(current_time, current_time - 1)
                    TimelineUtils.set_current_time(current_time - 1)
                    info.show_info('Key Nudged Left')
                    return True
                except RuntimeError:
                    info.show_info('Key Cannot be Moved')
                    return False
        else:
            if not (next_key - 1) in key_times:
                try:
                    TimelineUtils.change_keyframe_time(next_key, next_key - 1)
                    info.show_info('Next Key Pulled')
                    return True
                except RuntimeError:
                    info.show_info('Key Cannot be Moved')
                    return False

            info.show_info('Key Cannot be Moved')
            return False

    def pull_prev_keys(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        first_key = TimelineUtils.get_first_key()
        TimelineUtils.set_current_time(first_key - 1)
        TimelineUtils.add_inbetween()
        TimelineUtils.set_current_time(current_time)
        self.pull_next_keys()
        info.show_info('Keys [Before Current] Pushed')

    def pull_next_keys(self):
        current_time = TimelineUtils.get_current_time()
        key_times = TimelineUtils.get_all_key_times()

        if key_times == c.STRING.EMPTY:
            info.show_info('No keys to be Moved')
            return

        if current_time in key_times:
            TimelineUtils.set_current_time(current_time - 1)
            TimelineUtils.remove_inbetween()
            TimelineUtils.set_current_time(current_time)
        else:
            TimelineUtils.remove_inbetween()
        info.show_info('Keys [After Current] Pushed')
