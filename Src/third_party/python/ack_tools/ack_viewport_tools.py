"""
ack viewport tools - Viewport display and camera utilities.
Original MEL scripts by Aaron Koressel and others:
  ackToggleCams, ackToggleHighlight, ackToggleImagePlane, ackToggleModel,
  ackToggleNURBSCurves, ackToggleRotateMode, ackToggleSound,
  ackToggleTranslateMode, ackNewGraphEditor
"""
import re
import maya.cmds as cmd
import maya.mel as mel

_camera1 = ''
_camera2 = ''
_sound = ''


# ---------------------------------------------------------------------------
# toggle_highlight  (ackToggleHighlight)
# ---------------------------------------------------------------------------
def toggle_highlight():
    current = cmd.displayPref(q=True, wireframeOnShadedActive=True)
    cmd.displayPref(wireframeOnShadedActive='full' if current == 'none' else 'none')


# ---------------------------------------------------------------------------
# toggle_image_plane  (ackToggleImagePlane)
# ---------------------------------------------------------------------------
def toggle_image_plane():
    planes = cmd.ls(type='imagePlane') or []
    if not planes:
        return
    cur = cmd.getAttr(planes[0] + '.displayMode')
    new_val = 3 if cur == 0 else 0
    for plane in planes:
        cmd.setAttr(plane + '.displayMode', new_val)


# ---------------------------------------------------------------------------
# toggle_model  (ackToggleModel)
# ---------------------------------------------------------------------------
def toggle_model():
    panel = cmd.getPanel(underPointer=True)
    if panel and cmd.getPanel(typeOf=panel) == 'modelPanel':
        val = not cmd.modelEditor(panel, q=True, nurbsSurfaces=True)
        cmd.modelEditor(panel, e=True, nurbsSurfaces=val, polymeshes=val, subdivSurfaces=val)


# ---------------------------------------------------------------------------
# toggle_nurbs_curves  (ackToggleNURBSCurves)
# ---------------------------------------------------------------------------
def toggle_nurbs_curves():
    panel = cmd.getPanel(underPointer=True)
    if panel and cmd.getPanel(typeOf=panel) == 'modelPanel':
        val = not cmd.modelEditor(panel, q=True, nurbsCurves=True)
        cmd.modelEditor(panel, e=True, nurbsCurves=val)


# ---------------------------------------------------------------------------
# toggle_rotate_mode  (ackToggleRotateMode)
# ---------------------------------------------------------------------------
def toggle_rotate_mode():
    mode = cmd.manipRotateContext('Rotate', q=True, mode=True)
    cmd.manipRotateContext('Rotate', e=True, mode=2 if mode == 0 else 0)


# ---------------------------------------------------------------------------
# toggle_translate_mode  (ackToggleTranslateMode)
# ---------------------------------------------------------------------------
def toggle_translate_mode():
    mode = cmd.manipMoveContext('Move', q=True, mode=True)
    cmd.manipMoveContext('Move', e=True, mode=0 if mode == 2 else 2)


# ---------------------------------------------------------------------------
# toggle_sound  (ackToggleSound)
# ---------------------------------------------------------------------------
def toggle_sound():
    global _sound
    slider = mel.eval('$tmpVar = $gPlayBackSlider')
    cur = cmd.timeControl(slider, q=True, sound=True)

    if not cur and not _sound:
        cmd.confirmDialog(title='Error', message=(
            'Make the desired sound active first, then run toggle_sound again. '
            'That sound will be used for the rest of this session.'))
        return

    if cur and not _sound:
        _sound = cur

    if not cur:
        mel.eval('setSoundDisplay "{0}" 1'.format(_sound))
    else:
        mel.eval('setSoundDisplay "{0}" 0'.format(_sound))


# ---------------------------------------------------------------------------
# toggle_cams  (ackToggleCams)
# ---------------------------------------------------------------------------
def toggle_cams():
    global _camera1, _camera2
    _init_cams()

    if not _camera1 or not _camera2:
        return
    if not cmd.ls(_camera1) or not cmd.ls(_camera2):
        return

    panel = cmd.getPanel(underPointer=True)
    if panel and cmd.getPanel(typeOf=panel) == 'modelPanel':
        cur_cam = cmd.modelPanel(panel, q=True, camera=True)
        if cur_cam == _camera1:
            mel.eval('lookThroughModelPanel "{0}" {1}'.format(_camera2, panel))
        elif cur_cam == _camera2:
            mel.eval('lookThroughModelPanel "{0}" {1}'.format(_camera1, panel))


def toggle_cams_setup():
    global _camera1, _camera2
    _init_cams()

    if cmd.window('win_ackToggleCams', exists=True):
        cmd.deleteUI('win_ackToggleCams')

    cmd.window('win_ackToggleCams', title='ackToggleCams Setup', maximizeButton=False,
               sizeable=False, widthHeight=(418, 215))
    cmd.rowColumnLayout(numberOfColumns=2,
                        columnSpacing=[(1, 4), (2, 4)],
                        columnWidth=[(1, 200), (2, 200)])

    cmd.text(label='Camera 1')
    cmd.text(label='Camera 2')
    cmd.textField('ackTC_txt1', changeCommand=_set_camera1)
    cmd.textField('ackTC_txt2', changeCommand=_set_camera2)
    cmd.textScrollList('ackTC_lst1', height=120,
                       selectCommand=lambda *a: _select_cam(1),
                       doubleClickCommand=lambda *a: mel.eval(
                           'lookThroughModelPanel "{0}" `getPanel -withFocus`'.format(_camera1)))
    cmd.textScrollList('ackTC_lst2', height=120,
                       selectCommand=lambda *a: _select_cam(2),
                       doubleClickCommand=lambda *a: mel.eval(
                           'lookThroughModelPanel "{0}" `getPanel -withFocus`'.format(_camera2)))
    cmd.button(label='Grab Current', command=lambda *a: _grab_cam(1))
    cmd.button(label='Grab Current', command=lambda *a: _grab_cam(2))

    for cam in (cmd.ls(cameras=True) or []):
        parent = cmd.listRelatives(cam, parent=True)
        if parent:
            cmd.textScrollList('ackTC_lst1', e=True, append=parent[0])
            cmd.textScrollList('ackTC_lst2', e=True, append=parent[0])

    cmd.textField('ackTC_txt1', e=True, text=_camera1)
    cmd.textField('ackTC_txt2', e=True, text=_camera2)

    cmd.showWindow('win_ackToggleCams')
    cmd.window('win_ackToggleCams', e=True, widthHeight=(418, 215))


def _init_cams():
    global _camera1, _camera2
    if not _camera1:
        panel = cmd.getPanel(withFocus=True)
        if panel and cmd.getPanel(typeOf=panel) == 'modelPanel':
            cur_cam = cmd.modelPanel(panel, q=True, camera=True)
            if cur_cam != 'persp':
                _camera1 = cur_cam
    if not _camera2:
        _camera2 = 'persp'


def _set_camera1(value, *args):
    global _camera1
    _camera1 = value


def _set_camera2(value, *args):
    global _camera2
    _camera2 = value


def _select_cam(slot):
    global _camera1, _camera2
    lst = 'ackTC_lst1' if slot == 1 else 'ackTC_lst2'
    txt = 'ackTC_txt1' if slot == 1 else 'ackTC_txt2'
    sel = cmd.textScrollList(lst, q=True, selectItem=True)
    if sel:
        cmd.textField(txt, e=True, text=sel[0])
        if slot == 1:
            _camera1 = sel[0]
        else:
            _camera2 = sel[0]


def _grab_cam(slot):
    panel = cmd.getPanel(withFocus=True)
    if not panel or cmd.getPanel(typeOf=panel) != 'modelPanel':
        return
    cam = cmd.modelPanel(panel, q=True, camera=True)
    txt = 'ackTC_txt1' if slot == 1 else 'ackTC_txt2'
    cmd.textField(txt, e=True, text=cam)
    if slot == 1:
        global _camera1
        _camera1 = cam
    else:
        global _camera2
        _camera2 = cam


# ---------------------------------------------------------------------------
# new_graph_editor  (ackNewGraphEditor)
# ---------------------------------------------------------------------------
def new_graph_editor():
    for panel in (cmd.getPanel(invisiblePanels=True) or []):
        if re.match(r'graphEditor', panel):
            cmd.scriptedPanel(panel, e=True, tearOff=True)
            return

    max_num = 0
    for panel in (cmd.getPanel(type='scriptedPanel') or []):
        m = re.match(r'graphEditor(\d+)', panel)
        if m:
            max_num = max(max_num, int(m.group(1)))

    mel.eval('tearOffPanel "Graph Editor{0}" graphEditor true'.format(max_num + 1))
