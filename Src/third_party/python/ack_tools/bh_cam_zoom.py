"""
bh_camZoom - Camera zoom/pan control UI.
Original MEL: bh_camZoom.mel by Brian Horgan
"""
import maya.cmds as cmd


def show():
    panel = cmd.getPanel(withFocus=True)
    zoom_camera = cmd.modelPanel(panel, q=True, camera=True) if panel else ''

    if cmd.window('zoomUI', exists=True):
        cmd.deleteUI('zoomUI')

    cmd.window('zoomUI', title='bh_camZoom', titleBar=True)
    cmd.columnLayout('mainCol', adjustableColumn=True)

    cmd.textFieldGrp('cameraField', editable=False, text=zoom_camera,
                     columnAlign=(1, 'left'))

    cmd.floatSliderGrp('Zoom', label='Zoom  ', field=False,
                       minValue=0.01, maxValue=1.0,
                       fieldMinValue=0.001, fieldMaxValue=1.0,
                       value=1.0, step=0.001,
                       dragCommand=lambda *a: _bh_zoom(),
                       changeCommand=lambda *a: _bh_zoom())

    cmd.floatSliderGrp('PanLR', label='Pan L-R', field=False,
                       minValue=-1.0, maxValue=1.0,
                       fieldMinValue=-1.0, fieldMaxValue=1.0,
                       value=0.0, step=0.001,
                       dragCommand=lambda *a: _bh_pan(),
                       changeCommand=lambda *a: _bh_pan())

    cmd.floatSliderGrp('PanUD', label='Pan U-D', field=False,
                       minValue=-1.0, maxValue=1.0,
                       fieldMinValue=-1.0, fieldMaxValue=1.0,
                       value=0.0, step=0.001,
                       dragCommand=lambda *a: _bh_pan(),
                       changeCommand=lambda *a: _bh_pan())

    cmd.rowColumnLayout(numberOfColumns=2)
    cmd.checkBox('togSwitch', label='Toggle', value=True,
                 onCommand=lambda *a: _bh_toggle_zoom(True),
                 offCommand=lambda *a: _bh_toggle_zoom(False))
    cmd.button('resetCamButton', label='Reset', width=60,
               command=lambda *a: _bh_reset_cam())

    cmd.showWindow('zoomUI')


def _get_cam_shape():
    cam_name = cmd.textFieldGrp('cameraField', q=True, text=True)
    shapes = cmd.listRelatives(cam_name, shapes=True) or []
    return shapes[0] if shapes else None


def _bh_zoom():
    shape = _get_cam_shape()
    if not shape:
        return
    cmd.setAttr(shape + '.panZoomEnabled', 1)
    cmd.setAttr(shape + '.zoom', cmd.floatSliderGrp('Zoom', q=True, value=True))


def _bh_pan():
    shape = _get_cam_shape()
    if not shape:
        return
    cmd.setAttr(shape + '.panZoomEnabled', 1)
    cmd.setAttr(shape + '.horizontalPan', cmd.floatSliderGrp('PanLR', q=True, value=True))
    cmd.setAttr(shape + '.verticalPan', cmd.floatSliderGrp('PanUD', q=True, value=True))


def _bh_reset_cam():
    cmd.floatSliderGrp('Zoom', e=True, value=1.0)
    cmd.floatSliderGrp('PanLR', e=True, value=0.0)
    cmd.floatSliderGrp('PanUD', e=True, value=0.0)
    _bh_zoom()
    _bh_pan()
    shape = _get_cam_shape()
    if shape:
        cmd.setAttr(shape + '.panZoomEnabled', 0)


def _bh_toggle_zoom(state):
    shape = _get_cam_shape()
    if shape:
        cmd.setAttr(shape + '.panZoomEnabled', int(state))
