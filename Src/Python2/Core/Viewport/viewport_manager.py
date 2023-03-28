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
                        PanelUtils.set_viewport_mode('default', False, False, False, 'base_OpenGL_Renderer', False, False, panel)
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
                            PanelUtils.set_viewport_mode('default', False, False, False, 'vp2Renderer', True, True, panel)
                            info.show_info('Viewport Mode: VIEWPORT 2.0')
                    elif light_type == 'flat':
                        PanelUtils.set_viewport_mode('all', False, False, False, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: SILHOUETTE')
                    elif light_type == 'all':
                        PanelUtils.set_viewport_mode('default', False, True, False, 'vp2Renderer', True, True, panel)
                        info.show_info('Viewport Mode: NO TEXTURE')

    def toggle_all_viewport_elements(self):
        pass
