"""
ackDeadPixelFinder - Find stepped/linear/held-pose keys in the graph editor.
Original MEL: ackDeadPixelFinder.mel by Aaron Koressel
"""
import maya.cmds as cmd


def show():
    if cmd.window('winDeadPixelFinder', exists=True):
        cmd.deleteUI('winDeadPixelFinder')

    cmd.window('winDeadPixelFinder', title='ackDeadPixelFinder', maximizeButton=False,
               sizeable=False, widthHeight=(360, 145), resizeToFitChildren=True)
    cmd.columnLayout(rowSpacing=2)
    cmd.rowColumnLayout(numberOfColumns=2,
                        columnWidth=[(1, 80), (2, 260)],
                        columnSpacing=[(1, 6)])

    cmd.rowColumnLayout(numberOfRows=1)
    cmd.text(label='Search For:')
    cmd.setParent('..')
    cmd.rowColumnLayout(numberOfRows=1)
    cmd.checkBox('ackDPF_chkStepped', label='Stepped', value=True)
    cmd.checkBox('ackDPF_chkLinear', label='Linear', value=True)
    cmd.checkBox('ackDPF_chkHeldPoses', label='Held Poses', value=True)
    cmd.setParent('..')

    cmd.rowColumnLayout(numberOfRows=1)
    cmd.text(label='Using:')
    cmd.setParent('..')
    cmd.rowColumnLayout(numberOfRows=1)
    cmd.radioCollection('ackDPF_rdoSelCollection')
    cmd.radioButton('ackDPF_rdoSelCurves', label='Sel Curves', select=True)
    cmd.radioButton('ackDPF_rdoSelObjects', label='Sel Objects')
    cmd.radioButton('ackDPF_rdoAllObjects', label='All Objects')
    cmd.setParent('..')

    cmd.rowColumnLayout(numberOfRows=1)
    cmd.text(label='When Found:')
    cmd.setParent('..')
    cmd.rowColumnLayout(numberOfRows=1)
    cmd.checkBox('ackDPF_chkChangeTime', label='Change Time', value=True)
    cmd.checkBox('ackDPF_chkSelectKey', label='Select Key', value=True)
    cmd.checkBox('ackDPF_chkCenterView', label='Center View', value=False)
    cmd.setParent('..')
    cmd.setParent('..')

    cmd.separator(height=10, width=360)
    cmd.rowColumnLayout(numberOfColumns=4,
                        columnSpacing=[(1, 4), (2, 42), (3, 6), (4, 42)],
                        columnWidth=[(1, 20), (2, 100), (3, 100), (4, 35)])
    cmd.button(label='?', command=lambda *a: _show_help())
    cmd.button(label='<<  Find Previous', command=lambda *a: _find('prev'))
    cmd.button(label='Find Next  >>', command=lambda *a: _find('next'))
    cmd.button(label='Close', command=lambda *a: cmd.deleteUI('winDeadPixelFinder'))

    cmd.showWindow('winDeadPixelFinder')
    cmd.window('winDeadPixelFinder', e=True, widthHeight=(360, 145))


def _show_help():
    help_text = (
        'ackDeadPixelFinder helps find sections of animation that need attention.\n\n'
        'SEARCH FOR\n'
        '> Stepped: finds remaining stepped tangents.\n'
        '> Linear: finds remaining linear tangents.\n'
        '> Held Poses: finds plateaus of flat-tangent keys with the same value.\n\n'
        'USING\n'
        '> Sel Curves: searches selected curves in the graph editor.\n'
        '> Sel Objects: searches selected objects.\n'
        '> All Objects: searches all animated objects in the scene.\n\n'
        'WHEN FOUND\n'
        '> Change Time: moves the time cursor to the found key.\n'
        '> Select Key: selects the found key.\n'
        '> Center View: centers the graph editor on the found key.\n\n'
        'Created by Aaron Koressel  |  www.aaronkoressel.com'
    )
    if cmd.window('winDPF_Help', exists=True):
        cmd.deleteUI('winDPF_Help')
    cmd.window('winDPF_Help', title='ackDeadPixelFinder Help',
               resizeToFitChildren=True, maximizeButton=False, widthHeight=(330, 300))
    form = cmd.formLayout()
    txt = cmd.scrollField(editable=False, wordWrap=True, font='fixedWidthFont',
                          width=300, height=200, numberOfLines=15, text=help_text)
    cmd.formLayout(form, e=True,
                   attachForm=[(txt, 'top', 0), (txt, 'left', 0),
                                (txt, 'right', 0), (txt, 'bottom', 0)])
    cmd.showWindow('winDPF_Help')


def _find(direction):
    chk_stepped = cmd.checkBox('ackDPF_chkStepped', q=True, value=True)
    chk_linear = cmd.checkBox('ackDPF_chkLinear', q=True, value=True)
    chk_held = cmd.checkBox('ackDPF_chkHeldPoses', q=True, value=True)
    start_frame = cmd.currentTime(q=True)

    sel_mode = cmd.radioCollection('ackDPF_rdoSelCollection', q=True, select=True)
    if sel_mode == 'ackDPF_rdoAllObjects':
        curve_set = cmd.ls(type='animCurve') or []
    elif sel_mode == 'ackDPF_rdoSelObjects':
        selection = cmd.ls(sl=True) or []
        curve_set = cmd.listConnections(selection, type='animCurve') or [] if selection else []
    else:
        curve_set = cmd.keyframe(selected=True, q=True, name=True) or []

    found = False
    found_key = 999999999 if direction == 'next' else -999999999
    found_channel = ''

    for channel in curve_set:
        if cmd.keyframe(channel, q=True, keyframeCount=True) <= 1:
            continue

        if direction == 'prev':
            nearest = cmd.findKeyframe(channel, time=(start_frame, start_frame), which='previous')
            if nearest >= start_frame:
                continue
        else:
            nearest = cmd.findKeyframe(channel, time=(start_frame, start_frame), which='next')
            if nearest <= start_frame:
                continue

        key_times = cmd.keyframe(channel, q=True, timeChange=True) or []
        nearest_idx = next((i for i, t in enumerate(key_times) if t == nearest), 0)

        value_array = cmd.keyframe(channel, q=True, valueChange=True) or []
        index_dir = -1 if direction == 'prev' else 1
        i = nearest_idx

        while 0 <= i < len(value_array):
            found_this = False
            tangent_type = cmd.keyTangent(channel, index=(i, i), q=True, outTangentType=True)

            if chk_held and i < len(value_array) - 1:
                if value_array[i] == value_array[i + 1]:
                    found_this = True
            if chk_stepped and tangent_type and tangent_type[0] == 'step':
                found_this = True
            if chk_linear and tangent_type and tangent_type[0] == 'linear':
                found_this = True

            if found_this:
                key_time = cmd.keyframe(channel, index=(i, i), q=True, timeChange=True)
                if key_time:
                    t = key_time[0]
                    if (direction == 'prev' and t > found_key) or (direction == 'next' and t < found_key):
                        found = True
                        found_key = t
                        found_channel = channel
                break

            i += index_dir

    if found:
        if cmd.checkBox('ackDPF_chkChangeTime', q=True, value=True):
            cmd.currentTime(found_key, edit=True)
        if cmd.checkBox('ackDPF_chkSelectKey', q=True, value=True):
            cmd.selectKey(found_channel, time=(found_key, found_key))
        if cmd.checkBox('ackDPF_chkCenterView', q=True, value=True):
            cmd.animCurveEditor('graphEditor1GraphEd', e=True, lookAt='currentTime')
