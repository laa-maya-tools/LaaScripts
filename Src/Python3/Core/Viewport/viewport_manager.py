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

from LaaScripts.Src.Python3.Constants import constants as c
from LaaScripts.Src.Python3.Utils import info_utils as info
from LaaScripts.Src.Python3.Utils import panel_utils


class ViewportManager(object):

    def __init__(self):
        pass

    def toggle_xray(self):
        ret = panel_utils.PanelUtils.toggle_viewport_elements(c.XRAY)
        info.show_info(ret)

    def toggle_wireframe(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.WIREFRAME)

    def toggle_default_material(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.DEF_MATERIAL)

    def toggle_cameras(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.CAMERAS)

    def toggle_grid(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.GRID)

    def toggle_image_plane(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.IMG_PLANE)

    def toggle_joints(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.JOINTS)

    def toggle_lights(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.LIGHTS)

    def toggle_locators(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.LOCATORS)

    def toggle_handles(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.HANDLES)

    def toggle_curves(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.CURVES)

    def toggle_polygons(self):
        panel_utils.PanelUtils.toggle_viewport_elements(c.POLYGONS)









