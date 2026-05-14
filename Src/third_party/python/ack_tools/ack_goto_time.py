"""
ackGotoTime - Quick jump-to-frame dialog.
Original MEL: ackGotoTime.mel by Aaron Koressel
"""
import maya.cmds as cmd


def goto_time():
    if cmd.window('winAckGotoTime', exists=True):
        cmd.deleteUI('winAckGotoTime')

    cmd.window('winAckGotoTime', width=80, height=50, title='Go To Frame')
    layout = cmd.formLayout()
    txt = cmd.textField('ack_txtGotoTime', width=80, height=50,
                        enterCommand=lambda *a: _exec())
    cmd.formLayout(layout, e=True,
                   attachForm=[(txt, 'top', 1), (txt, 'left', 1),
                                (txt, 'bottom', 1), (txt, 'right', 1)])
    cmd.showWindow('winAckGotoTime')
    cmd.window('winAckGotoTime', e=True, width=80, height=50)


def _exec():
    text = cmd.textField('ack_txtGotoTime', q=True, text=True)
    try:
        cmd.currentTime(float(text), edit=True)
    except ValueError:
        pass
    cmd.deleteUI('winAckGotoTime', window=True)
