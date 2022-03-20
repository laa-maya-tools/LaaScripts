import LaaScripts.Src._Utils.timeline_utils as tu
reload(tu)
from LaaScripts.Src._Utils.timeline_utils import TimelineUtils
from LaaScripts.Src._Constants import constants as c
reload(c)

if __name__ == '__main__':
    #print TimelineUtils().get_current_time()
    #TimelineUtils().set_current_time(25.3)
    #print TimelineUtils().find_keyframe(c.NEXT)
    print TimelineUtils.get_last_keyframe_time()
    print TimelineUtils.get_start_keyframe_time(55)
