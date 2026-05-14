import maya.cmds as cmd

from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Utils import info_utils as info
from LaaScripts.Src.Utils.timeline_utils import TimelineUtils
from LaaScripts.Src.Utils.selection_utils import SelectionUtils


class BakingTools(object):

    def __init__(self):
        pass

    def bake_on_ones(self):
        selection = SelectionUtils.list_selected_objects()
        if selection == c.EMPTY_LIST:
            info.show_info('No Object is Selected', c.warning_msg.color, c.warning_msg.background, c.warning_msg.border)
            return

        timeline_range = TimelineUtils.get_selected_range()
        if timeline_range[0] == timeline_range[1]:
            timeline_range = TimelineUtils.get_playback_range()

        for frame in range(int(timeline_range[0]), int(timeline_range[1]) + 1):
            cmd.setKeyframe(selection, time=frame)
            print(frame)

        info.show_info('Keys Baked')

    def rebuild(self, step):
        selection = SelectionUtils.list_selected_objects()
        rebuild_frames = []
        if selection == c.EMPTY_LIST:
            info.show_info('No Object is Selected', c.warning_msg.color, c.warning_msg.background, c.warning_msg.border)
            return

        timeline_range = TimelineUtils.get_selected_range()
        if timeline_range[0] == timeline_range[1]:
            timeline_range = TimelineUtils.get_playback_range()

        for frame in range(int(timeline_range[0]), int(timeline_range[1]) + 1, step):
            rebuild_frames.append(frame)

        for frame in range(int(timeline_range[0]), int(timeline_range[1]) + 1):
            if frame in rebuild_frames:
                cmd.setKeyframe(selection, time=frame)
            else:
                cmd.cutKey(selection, time=(frame, frame + 1))

        info.show_info('Rebuild on {0}s'.format(step))

    def key_on_markers(self, key_markers=False):
        selection = cmd.ls(sl=True)[0]
        if not selection:
            return

        markers = TimelineUtils.get_key_markers() if key_markers else TimelineUtils.get_frame_markers()
        for marker in markers:
            cmd.setKeyframe(selection, time=marker)
        info.show_info('Markers - Keyed')

    def bake_on_markers(self, key_markers=False):
        selection = cmd.ls(sl=True)[0]
        if not selection:
            return

        markers = TimelineUtils.get_key_markers() if key_markers else TimelineUtils.get_frame_markers()
        keytimes = TimelineUtils.get_all_key_times()

        for keytime in keytimes:
            if keytime in markers:
                cmd.setKeyframe(selection, time=keytime)
            else:
                cmd.cutKey(selection, time=(keytime, keytime + 1))

        for marker in markers:
            cmd.setKeyframe(selection, time=marker)
        info.show_info('Markers - Baked')


if __name__ == "__main__":
    bt = BakingTools()
    bt.rebuild(2)
