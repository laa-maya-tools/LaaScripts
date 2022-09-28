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
reload(c)


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
    def toggle_viewport_elements(elements_type, panel=cmd.getPanel(wf=True)):

        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            cmd.warning('No Panel on Focus.')
            return

        get_command = 'cmd.modelEditor(panel, q=True, {0}=True)'.format(elements_type)
        set_command = 'cmd.modelEditor(panel, edit=True, {0}=not current_state)'.format(elements_type)

        current_state = eval(get_command)
        exec(set_command)

    @staticmethod
    def get_user_cameras():
        default_cameras = cmd.ls(DEFAULT_CAMERAS_REGEX)
        user_cameras = [cam for cam in cmd.listRelatives(cmd.ls(cameras=1), parent=1) if cam not in default_cameras]
        return user_cameras


    def show_all (self, show=True, panel = cmds.getPanel(wf=True)):

        if not (cmds.getPanel(to=panel) == 'modelPanel'):
            cmds.warning('No Panel on Focus.')
            return

        cmds.modelEditor(panel, e=True, alo=show)
        cmds.modelEditor(panel, e=True, nc=show)
        cmds.modelEditor(panel, e=True, ns=show)
        cmds.modelEditor(panel, e=True, cv=show)
        cmds.modelEditor(panel, e=True, hu=show)
        cmds.modelEditor(panel, e=True, gr=show)
        cmds.modelEditor(panel, e=True, m=show)

    def toggle_displayed_lights (self, mode, panel = cmds.getPanel(wf=True)):

        if not (cmds.getPanel(to=panel) == 'modelPanel'):
            cmds.warning('No Panel on Focus.')
            return

        # Toogle Silhouette Mode
        if (mode == 'all'):

            if (cmds.modelEditor(panel, q=True, dl=True) == 'all'):
                cmds.modelEditor(panel, e=True, dl='default')
            else:
                cmds.modelEditor(panel, e=True, dl='all')
            return

        # Toogle Flat Lighting Mode
        if (mode == 'flat'):

            if (cmds.modelEditor(panel, q=True, dl=True) == 'flat'):
                cmds.modelEditor(panel, e=True, dl='default')
            else:
                cmds.modelEditor(panel, e=True, dl='flat')
            return

    # -----------------------------------------------------------------------------
    # Toggle Viewport Renderer
    # -----------------------------------------------------------------------------
    def toggle_viewport_renderer(self, panel=cmds.getPanel(wf=True)):

        if not (cmds.getPanel(to=panel) == 'modelPanel'):
            cmds.warning('No Panel on Focus.')
            return

        if (cmds.modelEditor(panel, q=True, rnm=True) == 'vp2Renderer'):
            cmds.modelEditor(panel, edit=True, rnm='base_OpenGL_Renderer')
            cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', False)
            cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', False)
        else:
            cmds.modelEditor(panel, e=True, rnm='vp2Renderer')
            cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', True)
            cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', True)

    # -----------------------------------------------------------------------------
    # Toggle Resolution Gate
    # -----------------------------------------------------------------------------
    def toggle_resolution_gate(self, panel=cmds.getPanel(wf=True)):

        if not (cmds.getPanel(to=panel) == 'modelPanel'):
            cmds.warning('No Panel on Focus.')
            return

        cam_name = cmds.modelEditor(panel, q=True, cam=True)
        film_gate = cmds.camera(cam_name, q=True, dfg=True)
        res_gate = cmds.camera(cam_name, q=True, dr=True)

        if (res_gate):
            cmds.camera(cam_name, e=True, dfg=False, dr=False, ovr=1.0)
        else:
            cmds.camera(cam_name, e=True, dfg=False, dr=True, ovr=1.3)
            cmds.setAttr(cam_name + 'Shape.displayGateMaskOpacity', 1)
            cmds.setAttr(cam_name + 'Shape.displayGateMaskColor', 0.03, 0.03, 0.03, type="double3")

    # -----------------------------------------------------------------------------
    # Set Default Viewport
    # -----------------------------------------------------------------------------
    def set_default_viewport(self, panel=cmds.getPanel(wf=True)):

        if not (cmds.getPanel(to=panel) == 'modelPanel'):
            cmds.warning('No Panel on Focus.')
            return

        cam_name = cmds.modelEditor(panel, q=True, cam=True)
        film_gate = cmds.camera(cam_name, q=True, dfg=True)
        res_gate = cmds.camera(cam_name, q=True, dr=True)

        cmds.modelEditor(panel, e=True, xr=False)
        cmds.modelEditor(panel, e=True, wos=False)
        cmds.modelEditor(panel, e=True, udm=False)
        cmds.modelEditor(panel, e=True, dl='default')
        cmds.modelEditor(panel, e=True, rnm='vp2Renderer')
        cmds.setAttr('hardwareRenderingGlobals.multiSampleEnable', True)
        cmds.setAttr('hardwareRenderingGlobals.ssaoEnable', True)
        cmds.camera(cam_name, e=True, dfg=False, dr=False, ovr=1.0)
        cmds.modelEditor(panel, e=True, gr=True)

    # -----------------------------------------------------------------------------
    # Set Tweo Side Lighting
    # -----------------------------------------------------------------------------
    def set_two_side_lighting (self, panels = cmds.getPanel(type='modelPanel')):

        for panel in panels:
            cmds.modelEditor(panel, edit=True, tsl=True)

