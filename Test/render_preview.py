import pymel.core as pm
import maya.cmds as cmd


def get_timeline_limit():
    time_control = pm.lsUI(type='timeControl')[0]
    tml_limit = pm.timeControl(time_control, ra=True, q=True)

    print(tml_limit)
    return tml_limit


def playblast_shot():
    scene_full_name = cmd.file(query=True, sn=True)
    scene_name_ext = scene_full_name.split('/')[-1]
    scene_name = scene_name_ext.split('.')[0]
    scene_path = scene_full_name.replace(scene_name_ext, '')
    video_name = scene_path + scene_name + '.mov'

    print(scene_name)
    print(scene_path)
    print(video_name)

    tml_limit = get_timeline_limit()
    start_frame = cmd.playbackOptions(q=True, min=True)
    end_frame = cmd.playbackOptions(q=True, max=True)

    # Selection on timeline
    if tml_limit[0] != tml_limit[1] - 1:
        start_frame = tml_limit[0]
        end_frame = tml_limit[1] - 1

    aPlayBackSliderPython = mel.eval('$tmpVar=$gPlayBackSlider')
    audio_node = cmd.timeControl(aPlayBackSliderPython, q=True, s=True)

    cmd.playblast(fmt='qt', f=video_name, s=audio_node, fo=True, sqt=False, cc=True, v=True, orn=False, fp=4, p=100,
                   c='H.264', qlt=100, wh=[1280, 720], st=start_frame, et=end_frame)


playblast_shot()
