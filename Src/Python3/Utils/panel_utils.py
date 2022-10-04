"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to get/set timeline keyframing
data.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from .widget_utils import WidgetUtils
from ..Constants import constants as c
import imp
imp.reload(c)


class PanelUtils(object):

    @staticmethod
    def get_active_panel():
        """
        Gets the active panel.
        :return: Panel.
        :rtype: str
        """
        return cmd.getPanel(withFocus=True)

    @staticmethod
    def get_hovered_panel():
        """
        Gets the panel under the cursor.
        :return: Panel.
        :rtype: str
        """
        return cmd.getPanel(underPointer=True)

    @staticmethod
    def toggle_viewport_elements(elements_type):

        panel = PanelUtils.get_hovered_panel()
        if not cmd.getPanel(to=panel) == c.MODEL_PANEL:
            all_panels = cmd.getPanel(type=c.MODEL_PANEL)
            get_command = 'cmd.modelEditor(all_panels[0], q=True, {0}=True)'.format(elements_type)
            current_state = eval(get_command)
            for p in all_panels:
                set_command = 'cmd.modelEditor(p, edit=True, {0}=not current_state)'.format(elements_type)
                exec(set_command)
            return 'XRAY: All | {0}'.format(current_state)

        get_command = 'cmd.modelEditor(panel, q=True, {0}=True)'.format(elements_type)
        current_state = eval(get_command)
        set_command = 'cmd.modelEditor(panel, edit=True, {0}=not current_state)'.format(elements_type)
        exec(set_command)
        return 'XRAY: Active | {0}'.format(current_state)

    @staticmethod
    def get_user_cameras():
        default_cameras = cmd.ls(DEFAULT_CAMERAS_REGEX)
        user_cameras = [cam for cam in cmd.listRelatives(cmd.ls(cameras=1), parent=1) if cam not in default_cameras]
        return user_cameras


    def show_all (self, show=True, panel = cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        cmd.modelEditor(panel, e=True, alo=show)
        cmd.modelEditor(panel, e=True, nc=show)
        cmd.modelEditor(panel, e=True, ns=show)
        cmd.modelEditor(panel, e=True, cv=show)
        cmd.modelEditor(panel, e=True, hu=show)
        cmd.modelEditor(panel, e=True, gr=show)
        cmd.modelEditor(panel, e=True, m=show)

    def toggle_displayed_lights (self, mode, panel = cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        # Toogle Silhouette Mode
        if mode == 'all':
            if cmd.modelEditor(panel, q=True, dl=True) == 'all':
                cmd.modelEditor(panel, e=True, dl='default')
            else:
                cmd.modelEditor(panel, e=True, dl='all')
            return

        # Toogle Flat Lighting Mode
        if mode == 'flat':

            if (cmd.modelEditor(panel, q=True, dl=True) == 'flat'):
                cmd.modelEditor(panel, e=True, dl='default')
            else:
                cmd.modelEditor(panel, e=True, dl='flat')
            return

    def toggle_viewport_renderer(self, panel=cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        if (cmd.modelEditor(panel, q=True, rnm=True) == 'vp2Renderer'):
            cmd.modelEditor(panel, edit=True, rnm='base_OpenGL_Renderer')
            cmd.setAttr('hardwareRenderingGlobals.multiSampleEnable', False)
            cmd.setAttr('hardwareRenderingGlobals.ssaoEnable', False)
        else:
            cmd.modelEditor(panel, e=True, rnm='vp2Renderer')
            cmd.setAttr('hardwareRenderingGlobals.multiSampleEnable', True)
            cmd.setAttr('hardwareRenderingGlobals.ssaoEnable', True)

    def toggle_resolution_gate(self, panel=cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        cam_name = cmd.modelEditor(panel, q=True, cam=True)
        film_gate = cmd.camera(cam_name, q=True, dfg=True)
        res_gate = cmd.camera(cam_name, q=True, dr=True)

        if (res_gate):
            cmd.camera(cam_name, e=True, dfg=False, dr=False, ovr=1.0)
        else:
            cmd.camera(cam_name, e=True, dfg=False, dr=True, ovr=1.3)
            cmd.setAttr(cam_name + 'Shape.displayGateMaskOpacity', 1)
            cmd.setAttr(cam_name + 'Shape.displayGateMaskColor', 0.03, 0.03, 0.03, type="double3")

    def set_default_viewport(self, panel=cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        cam_name = cmd.modelEditor(panel, q=True, cam=True)
        film_gate = cmd.camera(cam_name, q=True, dfg=True)
        res_gate = cmd.camera(cam_name, q=True, dr=True)

        cmd.modelEditor(panel, e=True, xr=False)
        cmd.modelEditor(panel, e=True, wos=False)
        cmd.modelEditor(panel, e=True, udm=False)
        cmd.modelEditor(panel, e=True, dl='default')
        cmd.modelEditor(panel, e=True, rnm='vp2Renderer')
        cmd.setAttr('hardwareRenderingGlobals.multiSampleEnable', True)
        cmd.setAttr('hardwareRenderingGlobals.ssaoEnable', True)
        cmd.camera(cam_name, e=True, dfg=False, dr=False, ovr=1.0)
        cmd.modelEditor(panel, e=True, gr=True)

    def set_two_side_lighting (self, panels = cmd.getPanel(type='modelPanel')):

        for panel in panels:
            cmd.modelEditor(panel, edit=True, tsl=True)

