"""
ack key tools - Graph editor key manipulation utilities.
Original MEL scripts by Aaron Koressel:
  ackDeleteKey, ackZeroOutKeys, ackSnapKeyValues, ackSliceCurves,
  ackMoveKeys, ackNegateKeys, ackPushPull, ackConvergeBuffer,
  ackSnapAnimation, ackSnapEndKeyValues, ackSnapToTime,
  ackSwapKeys, ackDeleteRedundant, ackPlayblastSelectedKeys
"""
import maya.cmds as cmd
import maya.mel as mel

from . import ack_setup as setup

_key_color_flag = False


# ---------------------------------------------------------------------------
# delete_key  (ackDeleteKey)
# ---------------------------------------------------------------------------
def delete_key():
    key_count = cmd.keyframe(an='keys', q=True, keyframeCount=True)
    if key_count == 0:
        mel.eval('timeSliderClearKey')
    else:
        cmd.cutKey(animation='keys', clear=True)


# ---------------------------------------------------------------------------
# zero_out_keys  (ackZeroOutKeys)
# ---------------------------------------------------------------------------
def zero_out_keys():
    if cmd.keyframe(an='keys', q=True, keyframeCount=True):
        cmd.keyframe(valueChange=0)


# ---------------------------------------------------------------------------
# snap_key_values  (ackSnapKeyValues)
# ---------------------------------------------------------------------------
def snap_key_values():
    snap_to = cmd.keyframe(q=True, lastSelected=True, valueChange=True) or []
    if snap_to:
        cmd.keyframe(valueChange=snap_to[0])


# ---------------------------------------------------------------------------
# toggle_key_color  (ackToggleKeyColor)
# ---------------------------------------------------------------------------
def toggle_key_color():
    global _key_color_flag
    _key_color_flag = not _key_color_flag
    cmd.keyframe(tickDrawSpecial=int(_key_color_flag))


# ---------------------------------------------------------------------------
# slice_curves  (ackSliceCurves)
# ---------------------------------------------------------------------------
def slice_curves():
    connection = cmd.editor('graphEditor1GraphEd', q=True, mainListConnection=True)
    cur_time = cmd.currentTime(q=True)
    key_count = cmd.keyframe(an='keys', q=True, keyframeCount=True)

    if key_count == 0:
        graph_objects = mel.eval('expandSelectionConnectionAsArray "{0}"'.format(connection)) or []
        if graph_objects:
            cmd.setKeyframe(graph_objects, insert=True, time=cur_time)
    else:
        selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []
        if selected_curves:
            cmd.setKeyframe(selected_curves, insert=True, time=cur_time)


# ---------------------------------------------------------------------------
# move_keys  (ackMoveKeys)
# ---------------------------------------------------------------------------
def move_keys(direction):
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    if direction == 'left':
        cmd.keyframe(animation='keys', option='over', relative=True, timeChange=-1)
        return
    if direction == 'right':
        cmd.keyframe(animation='keys', option='over', relative=True, timeChange=1)
        return

    fixed_factor = setup._fixed_factor
    scale_factor = setup._scale_factor
    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []

    if direction in ('up', 'down'):
        for channel in selected_curves:
            total_keys = cmd.keyframe(channel, q=True, keyframeCount=True)
            sel_indices = [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]
            if not sel_indices:
                continue

            prev_idx = max(sel_indices[0] - 1, 0)
            next_idx = min(sel_indices[-1] + 1, total_keys - 1)

            prev_val = cmd.keyframe(channel, index=(prev_idx, prev_idx), q=True, valueChange=True)
            next_val = cmd.keyframe(channel, index=(next_idx, next_idx), q=True, valueChange=True)
            if not prev_val or not next_val:
                continue

            delta = next_val[0] - prev_val[0]
            if delta == 0:
                delta = fixed_factor * 10
            move_dir = 1 if delta > 0 else -1

            sign = 1 if direction == 'up' else -1
            for i in sel_indices:
                cmd.keyframe(channel, relative=True, index=(i, i),
                             valueChange=delta * fixed_factor * move_dir * sign)

    elif direction in ('convergeLeft', 'convergeRight'):
        for channel in selected_curves:
            time_array = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
            if not time_array:
                continue

            if direction == 'convergeLeft':
                pt = cmd.findKeyframe(channel, which='previous', time=(time_array[0], time_array[0]))
            else:
                pt = cmd.findKeyframe(channel, which='next', time=(time_array[-1], time_array[-1]))

            pivot_val = cmd.keyframe(channel, time=(pt, pt), q=True, valueChange=True)
            if not pivot_val:
                continue

            sel_indices = [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]
            for i in sel_indices:
                cmd.scaleKey(channel, index=(i, i), valuePivot=pivot_val[0], valueScale=scale_factor)


# ---------------------------------------------------------------------------
# negate_keys  (ackNegateKeys)
# ---------------------------------------------------------------------------
def negate_keys():
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    pivot = setup._pivot or 'left'
    pivot_value = None
    if pivot == 'last':
        pivot_value = cmd.keyframe(lastSelected=True, q=True, valueChange=True)

    for channel in (cmd.keyframe(selected=True, q=True, name=True) or []):
        time_array = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
        if not time_array:
            continue

        if pivot == 'left':
            pt = cmd.findKeyframe(channel, which='previous', time=(time_array[0], time_array[0]))
            pivot_value = cmd.keyframe(channel, time=(pt, pt), q=True, valueChange=True)
        elif pivot == 'right':
            pt = cmd.findKeyframe(channel, which='next', time=(time_array[-1], time_array[-1]))
            pivot_value = cmd.keyframe(channel, time=(pt, pt), q=True, valueChange=True)

        if not pivot_value:
            continue

        for i in [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]:
            cmd.scaleKey(channel, index=(i, i), valuePivot=pivot_value[0], valueScale=-1)


# ---------------------------------------------------------------------------
# push_pull  (ackPushPull)
# ---------------------------------------------------------------------------
def push_pull(direction):
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    pivot = setup._pivot or 'left'
    scale_factor = setup._scale_factor
    pivot_value = None
    if pivot == 'last':
        pivot_value = cmd.keyframe(lastSelected=True, q=True, valueChange=True)

    for channel in (cmd.keyframe(selected=True, q=True, name=True) or []):
        time_array = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
        if not time_array:
            continue

        if pivot == 'left':
            pt = cmd.findKeyframe(channel, which='previous', time=(time_array[0], time_array[0]))
            pivot_value = cmd.keyframe(channel, time=(pt, pt), q=True, valueChange=True)
        elif pivot == 'right':
            pt = cmd.findKeyframe(channel, which='next', time=(time_array[-1], time_array[-1]))
            pivot_value = cmd.keyframe(channel, time=(pt, pt), q=True, valueChange=True)

        if not pivot_value:
            continue

        scale = (1.0 / scale_factor) if direction == 'push' else scale_factor
        for i in [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]:
            cmd.scaleKey(channel, index=(i, i), valuePivot=pivot_value[0], valueScale=scale)


# ---------------------------------------------------------------------------
# converge_buffer  (ackConvergeBuffer)
# ---------------------------------------------------------------------------
def converge_buffer(direction):
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    scale_factor = setup._scale_factor

    for channel in (cmd.keyframe(selected=True, q=True, name=True) or []):
        time_array = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
        if not time_array:
            continue

        cmd.bufferCurve(swap=True)
        buffer_values = [
            (cmd.keyframe(channel, time=(t, t), q=True, eval=True) or [0])[0]
            for t in time_array
        ]
        cmd.bufferCurve(swap=True)

        sel_indices = [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]
        for idx, i in enumerate(sel_indices):
            bv = buffer_values[idx]
            if direction == 'toward':
                cmd.scaleKey(channel, index=(i, i), valuePivot=bv, valueScale=scale_factor)
            elif direction == 'away':
                cmd.scaleKey(channel, index=(i, i), valuePivot=bv, valueScale=1.0 / scale_factor)
            elif direction == 'snap':
                cmd.keyframe(channel, index=(i, i), valueChange=bv)


# ---------------------------------------------------------------------------
# snap_animation  (ackSnapAnimation)
# ---------------------------------------------------------------------------
def snap_animation():
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    pivot = setup._pivot or 'left'

    for channel in (cmd.keyframe(selected=True, q=True, name=True) or []):
        time_array = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
        if not time_array:
            continue

        if pivot in ('left', 'last'):
            end_key = time_array[0]
            match_key = cmd.findKeyframe(channel, time=(end_key, end_key), which='previous')
        else:
            end_key = time_array[-1]
            match_key = cmd.findKeyframe(channel, time=(end_key, end_key), which='next')

        match_val = cmd.keyframe(channel, time=(match_key, match_key), q=True, valueChange=True)
        end_val = cmd.keyframe(channel, time=(end_key, end_key), q=True, valueChange=True)
        if not match_val or not end_val:
            continue

        delta = match_val[0] - end_val[0]
        for i in [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]:
            cmd.keyframe(channel, relative=True, index=(i, i), valueChange=delta)


# ---------------------------------------------------------------------------
# snap_end_key_values  (ackSnapEndKeyValues)
# ---------------------------------------------------------------------------
def snap_end_key_values():
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    pivot = setup._pivot or 'left'

    for channel in (cmd.keyframe(selected=True, q=True, name=True) or []):
        val_array = cmd.keyframe(channel, q=True, valueChange=True) or []
        index_array = [int(i) for i in (cmd.keyframe(channel, q=True, indexValue=True) or [])]
        if not val_array or not index_array:
            continue

        if pivot in ('left', 'last'):
            cmd.keyframe(channel, index=(index_array[-1], index_array[-1]), valueChange=val_array[0])
        else:
            cmd.keyframe(channel, index=(index_array[0], index_array[0]), valueChange=val_array[-1])


# ---------------------------------------------------------------------------
# snap_to_time  (ackSnapToTime)
# ---------------------------------------------------------------------------
def snap_to_time():
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    pivot = setup._pivot or 'left'
    if pivot == 'last':
        pivot = 'left'

    time_array = cmd.keyframe(q=True, timeChange=True) or []
    if not time_array:
        return

    snap_key = min(time_array) if pivot == 'left' else max(time_array)
    delta = cmd.currentTime(q=True) - snap_key
    cmd.keyframe(relative=True, option='over', timeChange=delta)


# ---------------------------------------------------------------------------
# swap_keys  (ackSwapKeys)
# ---------------------------------------------------------------------------
def swap_keys():
    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []
    if not selected_curves:
        return

    first_times = cmd.keyframe(selected_curves[0], selected=True, q=True, timeChange=True) or []
    if len(first_times) != 2:
        cmd.warning('swap_keys: requires exactly two distinct times per channel.')
        return

    time_a, time_b = first_times[0], first_times[1]

    for channel in selected_curves:
        times = cmd.keyframe(channel, selected=True, q=True, timeChange=True) or []
        if len(times) != 2 or set(times) != {time_a, time_b}:
            cmd.warning('swap_keys: requires exactly two distinct times per channel.')
            return

    buffer_time = -99999.0
    for channel in selected_curves:
        cmd.keyframe(channel, e=True, time=(time_a, time_a), option='over', timeChange=buffer_time)
        cmd.keyframe(channel, e=True, time=(time_b, time_b), option='over', timeChange=time_a)
        cmd.keyframe(channel, e=True, time=(buffer_time, buffer_time), option='over', timeChange=time_b)


# ---------------------------------------------------------------------------
# delete_redundant  (ackDeleteRedundant)
# ---------------------------------------------------------------------------
def delete_redundant():
    tolerance = 0.00001

    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []
    max_val = sum(len(cmd.keyframe(c, q=True, valueChange=True) or []) for c in selected_curves) + len(selected_curves)

    cmd.progressWindow(title='Delete Redundant Keys', maxValue=max(max_val, 1),
                       status='Deleting Redundant Keys...', isInterruptable=True)
    try:
        for channel in selected_curves:
            if cmd.progressWindow(q=True, isCancelled=True):
                break
            cmd.progressWindow(e=True, step=1)

            value_array = cmd.keyframe(channel, q=True, valueChange=True) or []
            delete_times = []
            in_series = False
            started = False

            for i in range(len(value_array) - 1):
                if cmd.progressWindow(q=True, isCancelled=True):
                    break
                cmd.progressWindow(e=True, step=1)

                if abs(value_array[i] - value_array[i + 1]) <= tolerance:
                    if not started and not in_series:
                        started = True
                        in_series = True
                    elif in_series:
                        kt = cmd.keyframe(channel, index=(i, i), q=True, timeChange=True)
                        if kt:
                            delete_times.append(kt[0])
                else:
                    started = False
                    in_series = False

            selected_times = set(cmd.keyframe(channel, q=True, timeChange=True, selected=True) or [])
            for t in delete_times:
                if cmd.progressWindow(q=True, isCancelled=True):
                    break
                if t in selected_times:
                    cmd.cutKey(channel, time=(t, t), clear=True)
    finally:
        cmd.progressWindow(endProgress=True)


# ---------------------------------------------------------------------------
# playblast_selected_keys  (ackPlayblastSelectedKeys)
# ---------------------------------------------------------------------------
def playblast_selected_keys():
    keys = cmd.keyframe(q=True, selected=True, timeChange=True) or []
    if not keys:
        return

    low, hi = min(keys), max(keys)
    slider = mel.eval('$tmpVar = $gPlayBackSlider')
    cur_sound = cmd.timeControl(slider, q=True, sound=True)

    kwargs = dict(startTime=low, endTime=hi)
    if cur_sound:
        kwargs['sound'] = cur_sound
    cmd.playblast(**kwargs)
