"""
ackSetup - Shared settings used by multiple ack tools.
Original MEL: ackSetup.mel by Aaron Koressel
"""
import maya.cmds as cmd

_pivot = 'left'       # 'left', 'right', or 'last'
_fixed_factor = 0.05  # used by move_keys up/down
_scale_factor = 0.9   # used by move_keys converge, push_pull


def set_pivot(value, *args):
    global _pivot
    _pivot = value
    if cmd.window('win_ackSetup', exists=True):
        radio_map = {'left': 'rdoAckPivotLeft', 'right': 'rdoAckPivotRight', 'last': 'rdoAckPivotLast'}
        if value in radio_map:
            cmd.radioCollection('rdoAckPivot', e=True, select=radio_map[value])


def set_fixed_factor(value, *args):
    global _fixed_factor
    _fixed_factor = value


def set_scale_factor(value, *args):
    global _scale_factor
    _scale_factor = value


def show(*args):
    global _pivot, _fixed_factor, _scale_factor

    if _pivot not in ('left', 'right', 'last'):
        _pivot = 'left'
    if not (0.0001 < _fixed_factor < 2):
        _fixed_factor = 0.05
    if not (0.0001 < _scale_factor < 0.999):
        _scale_factor = 0.9

    if cmd.window('win_ackSetup', exists=True):
        cmd.deleteUI('win_ackSetup')

    cmd.window('win_ackSetup', title='ackSetup 1.0', maximizeButton=False,
               sizeable=False, widthHeight=(280, 280))
    cmd.columnLayout(columnOffset=('left', 8), rowSpacing=4)

    cmd.rowLayout(numberOfColumns=1, columnOffset1=(1, 'left'), adjustableColumn=1)
    cmd.button(label='Restore Defaults', command=_restore_defaults)
    cmd.setParent('..')

    cmd.separator(width=280)
    cmd.rowLayout(numberOfColumns=2, columnOffset2=('left', 20))
    cmd.text(label='Pivot From:')
    cmd.button(label='?', command=lambda *a: cmd.confirmDialog(message=(
        'Used by:\n ackNegateKeys\n ackPushPull\n ackSnapAnimation\n ackSnapToTime\n ackSnapEndKeyValues')))
    cmd.setParent('..')

    cmd.radioCollection('rdoAckPivot')
    cmd.radioButton('rdoAckPivotLeft', label='Adjacent Left (Multi Pivot)',
                    onCommand=lambda *a: set_pivot('left'))
    cmd.radioButton('rdoAckPivotRight', label='Adjacent Right (Multi Pivot)',
                    onCommand=lambda *a: set_pivot('right'))
    cmd.radioButton('rdoAckPivotLast', label='Last Selected Key (Single Pivot)',
                    onCommand=lambda *a: set_pivot('last'))

    cmd.separator(width=280)
    cmd.rowLayout(numberOfColumns=2, columnOffset2=('left', 20))
    cmd.text(label='Fixed Move Factor:')
    cmd.button(label='?', command=lambda *a: cmd.confirmDialog(message='Used by:\n ackMoveKeys (up/down)'))
    cmd.setParent('..')
    cmd.floatSliderGrp('slideFixedFactor', field=True, columnAlign=(1, 'left'),
                       value=_fixed_factor, minValue=0.001, maxValue=2.0, precision=3,
                       fieldStep=0.01, sliderStep=0.01,
                       changeCommand=lambda v, *a: set_fixed_factor(v))

    cmd.rowLayout(numberOfColumns=2, columnOffset2=('left', 20))
    cmd.text(label='Scale Factor:')
    cmd.button(label='?', command=lambda *a: cmd.confirmDialog(
        message='Used by:\n ackMoveKeys (convergeLeft/convergeRight)\n ackPushPull'))
    cmd.setParent('..')
    cmd.floatSliderGrp('slideScaleFactor', field=True, columnAlign=(1, 'left'),
                       value=_scale_factor, minValue=0.001, maxValue=0.999, precision=3,
                       fieldStep=0.01, sliderStep=0.01,
                       changeCommand=lambda v, *a: set_scale_factor(v))

    radio_map = {'left': 'rdoAckPivotLeft', 'right': 'rdoAckPivotRight', 'last': 'rdoAckPivotLast'}
    if _pivot in radio_map:
        cmd.radioCollection('rdoAckPivot', e=True, select=radio_map[_pivot])

    cmd.showWindow('win_ackSetup')
    cmd.window('win_ackSetup', e=True, widthHeight=(280, 280))


def _restore_defaults(*args):
    global _pivot, _fixed_factor, _scale_factor
    _pivot = ''
    _fixed_factor = 0
    _scale_factor = 0
    show()
