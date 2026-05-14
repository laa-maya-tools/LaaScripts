"""
ackShuttleControl - Navigation/shuttle controls without polluting undo history.
Original MEL: ackShuttleControl.mel by Aaron Koressel
"""
import maya.cmds as cmd
import maya.mel as mel

_last_tool = ''


def shuttle_control(action):
    global _last_tool

    if action == 'nextFrame':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.currentTime(q=True) + 1)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'prevFrame':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.currentTime(q=True) - 1)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'nextKey':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.findKeyframe(which='next'), edit=True)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'prevKey':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.findKeyframe(which='previous'), edit=True)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'firstFrame':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.playbackOptions(q=True, min=True), edit=True)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'lastFrame':
        cmd.undoInfo(stateWithoutFlush=False)
        cmd.currentTime(cmd.playbackOptions(q=True, max=True), edit=True)
        cmd.undoInfo(stateWithoutFlush=True)

    elif action == 'timeDraggerActivate':
        _last_tool = cmd.currentCtx()
        cmd.undoInfo(stateWithoutFlush=False)
        mel.eval('setToolTo TimeDragger')

    elif action == 'timeDraggerDeactivate':
        if _last_tool:
            cmd.setToolTo(_last_tool)
        cmd.undoInfo(stateWithoutFlush=True)
