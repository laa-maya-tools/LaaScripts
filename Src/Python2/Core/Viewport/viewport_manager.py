# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: channels_filter.py
-----------------------------------------------------------------------------
This module manages the channelbox selection.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2020 | Python 2
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Python2.Constants import constants as c
from LaaScripts.Src.Python2.Utils import info_utils as info
from LaaScripts.Src.Python2.Utils.panel_utils import PanelUtils


class ViewportManager(object):

    def __init__(self):
        pass

    def toggle_xray(self):
        msg = PanelUtils.toggle_viewport_elements(c.XRAY)
        info.show_info(msg)

    def toggle_wireframe(self):
        msg = PanelUtils.toggle_viewport_elements(c.WIREFRAME)
        info.show_info(msg)

    def toggle_default_material(self):
        msg = PanelUtils.toggle_viewport_elements(c.DEF_MATERIAL)
        info.show_info(msg)

    def toggle_cameras(self):
        msg = PanelUtils.toggle_viewport_elements(c.CAMERAS)
        info.show_info(msg)

    def toggle_grid(self):
        msg = PanelUtils.toggle_viewport_elements(c.GRID)
        info.show_info(msg)

    def toggle_image_plane(self):
        msg = PanelUtils.toggle_viewport_elements(c.IMG_PLANE)
        info.show_info(msg)

    def toggle_joints(self):
        msg = PanelUtils.toggle_viewport_elements(c.JOINTS)
        info.show_info(msg)

    def toggle_lights(self):
        msg = PanelUtils.toggle_viewport_elements(c.LIGHTS)
        info.show_info(msg)

    def toggle_locators(self):
        msg = PanelUtils.toggle_viewport_elements(c.LOCATORS)
        info.show_info(msg)

    def toggle_handles(self):
        msg = PanelUtils.toggle_viewport_elements(c.HANDLES)
        info.show_info(msg)

    def toggle_curves(self):
        msg = PanelUtils.toggle_viewport_elements(c.CURVES)
        info.show_info(msg)

    def toggle_polygons(self):
        msg = PanelUtils.toggle_viewport_elements(c.POLYGONS)
        info.show_info(msg)

    def toggle_resolution_gate(self):
        msg = PanelUtils.toggle_resolution_gate()
        info.show_info(msg)

    def toggle_viewport_modes(self):
        hovered_panel = PanelUtils.get_hovered_model_panel()
        active_panel = PanelUtils.get_active_model_panel()
        model_panels = PanelUtils.get_all_model_panels()
        panels = []

        if hovered_panel:
            panels.append(hovered_panel)
        elif active_panel:
            panels.append(active_panel)
        else:
            panels = model_panels

        for panel in panels:
            wireframe = cmd.modelEditor(panels[0], q=True, wos=True)
            xray = cmd.modelEditor(panels[0], q=True, xr=True)
            default_mtl = cmd.modelEditor(panels[0], q=True, udm=True)
            renderer = cmd.modelEditor(panels[0], q=True, rnm=True)
            light_type = cmd.modelEditor(panels[0], q=True, dl=True)
            ao_enabled = cmd.getAttr('hardwareRenderingGlobals.ssaoEnable')

            if renderer == 'base_OpenGL_Renderer':
                PanelUtils.set_viewport_mode('default', False, False, False, 'vp2Renderer', True, True, panel)
                info.show_info('Viewport Mode: VIEWPORT 2.0')
            else:
                if default_mtl:
                    if wireframe:
                        PanelUtils.set_viewport_mode('default', True, True, False, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: XRAY')
                    elif xray:
                        PanelUtils.set_viewport_mode('default', False, False, False, 'base_OpenGL_Renderer', False,
                                                     False, panel)
                        info.show_info('Viewport Mode: DEFAULT RENDERER')
                    else:
                        PanelUtils.set_viewport_mode('default', False, True, True, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: WIREFRAME')

                else:
                    if light_type == 'default':
                        if ao_enabled:
                            PanelUtils.set_viewport_mode('flat', False, False, False, 'vp2Renderer', True, True, panel)
                            info.show_info('Viewport Mode: FLAT LIGHTING')
                        else:
                            PanelUtils.set_viewport_mode('default', False, False, False, 'vp2Renderer', True, True,
                                                         panel)
                            info.show_info('Viewport Mode: VIEWPORT 2.0')
                    elif light_type == 'flat':
                        PanelUtils.set_viewport_mode('all', False, False, False, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: SILHOUETTE')
                    elif light_type == 'all':
                        PanelUtils.set_viewport_mode('default', False, True, False, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: NO TEXTURE')

    def toggle_all_viewport_elements(self):
        panel = cmd.getPanel(wf=True)
        if not (cmd.getPanel(to=panel) == 'modelPanel'):
            return
        curves_vis = cmd.modelEditor(panel, q=True, nc=True)
        locators_vis = cmd.modelEditor(panel, q=True, lc=True)
        if locators_vis:
            cmd.modelEditor(panel, edit=True, alo=False)
            cmd.modelEditor(panel, edit=True, m=False)
            cmd.modelEditor(panel, edit=True, hu=False)
            cmd.modelEditor(panel, edit=True, gr=False)
            cmd.modelEditor(panel, edit=True, cv=False)
            cmd.modelEditor(panel, edit=True, nc=True)
            cmd.modelEditor(panel, edit=True, pm=True)
            info.show_info('SHOW: Curves and Geo')
        else:
            if curves_vis:
                cmd.modelEditor(panel, edit=True, alo=False)
                cmd.modelEditor(panel, edit=True, m=False)
                cmd.modelEditor(panel, edit=True, hu=False)
                cmd.modelEditor(panel, edit=True, gr=False)
                cmd.modelEditor(panel, edit=True, cv=False)
                cmd.modelEditor(panel, edit=True, nc=False)
                cmd.modelEditor(panel, edit=True, pm=True)
                info.show_info('SHOW: Only Geo')
            else:
                cmd.modelEditor(panel, edit=True, alo=True)
                cmd.modelEditor(panel, edit=True, m=True)
                cmd.modelEditor(panel, edit=True, hu=True)
                cmd.modelEditor(panel, edit=True, gr=True)
                cmd.modelEditor(panel, edit=True, cv=True)
                cmd.modelEditor(panel, edit=True, nc=True)
                info.show_info('SHOW: All Elements')

    def toggle_perspective_cameras(self):
        current_cam = cmd.lookThru(q=True)
        all_cams = cmd.listCameras(p=True)
        next_cam = None

        for i, cam in enumerate(all_cams):
            if current_cam == all_cams[-1]:
                next_cam = all_cams[0]
            elif current_cam == all_cams[i]:
                next_cam = all_cams[i + 1]

        cmd.lookThru(next_cam)
        info.show_info('CAM: {0}'.format(next_cam))

    def toggle_ortographic_cameras(self):
        current_panel = PanelUtils.get_hovered_panel()
        if not current_panel:
            current_panel = PanelUtils.get_active_panel()

        if PanelUtils.is_model_panel(current_panel):
            if cmd.modelPanel(current_panel, q=True, cam=True) == 'persp':
                mel.eval('switchModelView side;')
                info.show_info('CAM: Side View')
            elif cmd.modelPanel(current_panel, q=True, cam=True) == 'side':
                mel.eval('switchModelView front;')
                info.show_info('CAM: Front View')
            elif cmd.modelPanel(current_panel, q=True, cam=True) == 'front':
                mel.eval('switchModelView top;')
                info.show_info('CAM: Top View')
            else:
                mel.eval('switchModelView persp;')
                info.show_info('CAM: Persp View')
        else:
            info.show_info('Panel not valid')

        # if ($currentPanel == "")
        #     $currentPanel = `getPanel - withFocus`;
        #
        # if (`getPanel - to $currentPanel` == "modelPanel")
        #     {
        #     if (`modelPanel - q - cam $currentPanel` == "persp")
        #     switchModelView
        #     side;
        #     else if (`modelPanel - q - cam $currentPanel` == "side")
        #     switchModelView front;
        #     else if (`modelPanel -q -cam $currentPanel` == "front")
        #     switchModelView top;
        #     else
        #     switchModelView persp;
        #     }
        # else
        #     error("I’m sorry, but that is not a valid camera panel.")


if __name__ == '__main__':
    vm = ViewportManager()
    vm.toggle_resolution_gate()