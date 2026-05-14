"""
ack timing tools - Timing, tangent, and curve manipulation utilities.
Original MEL scripts by Aaron Koressel:
  ackSteppedTween, ackTimingFramework, ackSpreadSqueezeTiming,
  ackCycleTangents, ackToggleTangentType, ackToggleKeyColor
"""
import maya.cmds as cmd
import maya.mel as mel


# ---------------------------------------------------------------------------
# stepped_tween  (ackSteppedTween)
# ---------------------------------------------------------------------------
def stepped_tween():
    connection = cmd.editor('graphEditor1GraphEd', q=True, mainListConnection=True)
    graph_objects = mel.eval('expandSelectionConnectionAsArray "{0}"'.format(connection)) or []
    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []
    key_count = cmd.keyframe(an='keys', q=True, keyframeCount=True)
    cur_time = cmd.currentTime(q=True)

    on_what = graph_objects if key_count == 0 else selected_curves
    if not on_what:
        return

    prev_key = cmd.findKeyframe(*on_what, time=(cur_time, cur_time), which='previous')
    next_key = cmd.findKeyframe(*on_what, time=(cur_time, cur_time), which='next')

    cmd.keyTangent(*on_what, outTangentType='linear', time=(prev_key, prev_key))
    cmd.keyTangent(*on_what, inTangentType='linear', time=(next_key, next_key))
    cmd.setKeyframe(*on_what, insert=True, time=cur_time)
    cmd.keyTangent(*on_what, outTangentType='step', time=(prev_key, next_key))


# ---------------------------------------------------------------------------
# timing_framework  (ackTimingFramework)
# ---------------------------------------------------------------------------
def timing_framework():
    all_times = cmd.keyframe(q=True, timeChange=True) or []
    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []

    max_val = len(all_times)
    if len(selected_curves) > 1:
        max_val = sum(len(cmd.keyframe(c, q=True, timeChange=True) or []) for c in selected_curves) + len(selected_curves)

    cmd.progressWindow(title='ackTimingFramework', maxValue=max(max_val, 1),
                       status='', isInterruptable=True)
    try:
        if len(selected_curves) <= 1:
            for t in all_times:
                if cmd.progressWindow(q=True, isCancelled=True):
                    break
                cmd.progressWindow(e=True, step=1)
                cmd.setKeyframe(insert=True, time=t)
        else:
            for channel in selected_curves:
                if cmd.progressWindow(q=True, isCancelled=True):
                    break
                for t in all_times:
                    if cmd.progressWindow(q=True, isCancelled=True):
                        break
                    cmd.progressWindow(e=True, step=1)
                    cmd.setKeyframe(channel, insert=True, time=t)
    finally:
        cmd.progressWindow(endProgress=True)


# ---------------------------------------------------------------------------
# spread_squeeze_timing  (ackSpreadSqueezeTiming)
# ---------------------------------------------------------------------------
def spread_squeeze_timing(direction):
    confirm_thresh = 500

    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    all_sel = cmd.keyframe(selected=True, q=True, indexValue=True) or []
    if len(all_sel) > confirm_thresh:
        result = cmd.confirmDialog(
            title='ackSpreadSqueezeTiming',
            message='About to operate on a large number of keys. Proceed?',
            button=['OK', 'Cancel'], defaultButton='OK',
            cancelButton='Cancel', dismissString='Cancel')
        if result != 'OK':
            return

    selected_curves = cmd.keyframe(selected=True, q=True, name=True) or []
    max_val = sum(len(cmd.keyframe(c, q=True, indexValue=True) or []) for c in selected_curves) + len(selected_curves)

    cmd.progressWindow(title='ackSpreadSqueezeTiming', maxValue=max(max_val, 1),
                       status='', isInterruptable=True)
    try:
        for channel in selected_curves:
            if cmd.progressWindow(q=True, isCancelled=True):
                break
            cmd.progressWindow(e=True, step=1)

            index_array = [int(i) for i in (cmd.keyframe(channel, selected=True, q=True, indexValue=True) or [])]
            time_delta = 1 if direction == 'spread' else -1

            for i in range(len(index_array)):
                if cmd.progressWindow(q=True, isCancelled=True):
                    break
                cmd.progressWindow(e=True, step=1)

                indices_to_move = index_array[i:]
                for idx in reversed(indices_to_move):
                    cmd.keyframe(channel, option='over', relative=True,
                                 index=(idx, idx), timeChange=time_delta)

                cmd.snapKey(channel, timeMultiple=1.0)
    finally:
        cmd.progressWindow(endProgress=True)


# ---------------------------------------------------------------------------
# cycle_tangents  (ackCycleTangents)
# ---------------------------------------------------------------------------
def cycle_tangents():
    order = ('step', 'linear', 'auto')

    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    cur = cmd.keyTangent(q=True, outTangentType=True)
    if not cur:
        return

    current = cur[0]
    if current in order:
        next_tangent = order[(order.index(current) + 1) % len(order)]
    else:
        next_tangent = order[0]

    cmd.keyTangent(inTangentType=next_tangent, outTangentType=next_tangent)


# ---------------------------------------------------------------------------
# toggle_tangent_type  (ackToggleTangentType)
# ---------------------------------------------------------------------------
def toggle_tangent_type():
    if not cmd.keyframe(an='keys', q=True, keyframeCount=True):
        return

    cur_lock = cmd.keyTangent(q=True, lock=True)
    if cur_lock is None:
        return

    cmd.keyTangent(lock=not cur_lock[0])
    cmd.keyTangent(weightLock=False)
