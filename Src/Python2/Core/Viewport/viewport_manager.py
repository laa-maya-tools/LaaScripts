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
from LaaScripts.Src.Python2.Utils import panel_utils


class ViewportManager(object):

    def __init__(self):
        pass

    def toggle_xray(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.XRAY)
        info.show_info(msg)

    def toggle_wireframe(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.WIREFRAME)
        info.show_info(msg)

    def toggle_default_material(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.DEF_MATERIAL)
        info.show_info(msg)

    def toggle_cameras(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.CAMERAS)
        info.show_info(msg)

    def toggle_grid(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.GRID)
        info.show_info(msg)

    def toggle_image_plane(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.IMG_PLANE)
        info.show_info(msg)

    def toggle_joints(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.JOINTS)
        info.show_info(msg)

    def toggle_lights(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.LIGHTS)
        info.show_info(msg)

    def toggle_locators(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.LOCATORS)
        info.show_info(msg)

    def toggle_handles(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.HANDLES)
        info.show_info(msg)

    def toggle_curves(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.CURVES)
        info.show_info(msg)

    def toggle_polygons(self):
        msg = panel_utils.PanelUtils.toggle_viewport_elements(c.POLYGONS)
        info.show_info(msg)

    def toggle_viewport_modes(self):
        pass

    def toggle_all_viewport_elements(self):
        pass
