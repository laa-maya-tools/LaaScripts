# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: smart_manipulator.py
-----------------------------------------------------------------------------
This module adds new functionality to the default maya's manipulator.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2020 | Python 2
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Python3.Constants import constants as c
from LaaScripts.Src.Python3.Utils import info_utils as info
from LaaScripts.Src.Python3.Utils.navigation_utils import NavigationUtils


class SmartManipulator(object):

    def __init__(self):
        self._transform_modes = {
            c.MOVE: [[c.LOCAL, 0], [c.WORLD, 1]],
            c.ROTATE: [[c.LOCAL, 0], [c.WORLD, 1], [c.GIMBAL, 2]],
            c.SCALE: [[c.LOCAL, 0], [c.WORLD, 2]]
        }

        self._transform_attrs = {
            c.MOVE: [c.TX, c.TY, c.TZ],
            c.ROTATE: [c.RX, c.RY, c.RZ],
            c.SCALE: [c.SX, c.SY, c.SZ]
        }

    def switch_translate_manipulator(self):
        """
        Switch the translate manipulator coordinate system between local and world.
        """
        current_mode = NavigationUtils.get_current_move_mode()
        NavigationUtils.reset_rotate_mode(self._transform_modes[c.ROTATE][-1][c.INDEX])
        NavigationUtils.reset_scale_mode(self._transform_modes[c.SCALE][-1][c.INDEX])
        cmd.setToolTo(c.MOVE)

        for i, mode in enumerate(self._transform_modes[c.MOVE]):

            if not current_mode == self._transform_modes[c.MOVE][-1][c.INDEX]:
                if current_mode == self._transform_modes[c.MOVE][i][c.INDEX]:
                    NavigationUtils.set_current_move_mode(self._transform_modes[c.MOVE][i + 1][c.INDEX])
                    info.show_info('W: {0}'.format(self._transform_modes[c.MOVE][i+1][c.NAME]))
                    NavigationUtils.fix_translate_marking_menu()
                    return

        NavigationUtils.set_current_move_mode(self._transform_modes[c.MOVE][0][c.INDEX])
        info.show_info('W: {0}'.format(self._transform_modes[c.MOVE][0][c.NAME]))
        NavigationUtils.fix_translate_marking_menu()

    def switch_rotate_manipulator(self):
        """
        Switch the rotate manipulator coordinate system between local, world and gimbal.
        """
        current_mode = NavigationUtils.get_current_rotate_mode()
        NavigationUtils.reset_move_mode(self._transform_modes[c.MOVE][-1][c.INDEX])
        NavigationUtils.reset_scale_mode(self._transform_modes[c.SCALE][-1][c.INDEX])
        cmd.setToolTo(c.ROTATE)

        for i, mode in enumerate(self._transform_modes[c.ROTATE]):

            if not current_mode == self._transform_modes[c.ROTATE][-1][c.INDEX]:
                if current_mode == self._transform_modes[c.ROTATE][i][c.INDEX]:
                    NavigationUtils.set_current_rotate_mode(self._transform_modes[c.ROTATE][i + 1][c.INDEX])
                    info.show_info('E: {0}'.format(self._transform_modes[c.ROTATE][i+1][c.NAME]))
                    NavigationUtils.fix_rotate_marking_menu()
                    return

        NavigationUtils.set_current_rotate_mode(self._transform_modes[c.ROTATE][0][c.INDEX])
        info.show_info('E: {0}'.format(self._transform_modes[c.ROTATE][0][c.NAME]))
        NavigationUtils.fix_rotate_marking_menu()

    def switch_scale_manipulator(self):
        """
        Switch the scale manipulator coordinate system between local and world.
        """
        current_mode = NavigationUtils.get_current_scale_mode()
        NavigationUtils.reset_move_mode(self._transform_modes[c.MOVE][-1][c.INDEX])
        NavigationUtils.reset_rotate_mode(self._transform_modes[c.SCALE][-1][c.INDEX])
        cmd.setToolTo(c.SCALE)

        for i, mode in enumerate(self._transform_modes[c.SCALE]):

            if not current_mode == self._transform_modes[c.SCALE][-1][c.INDEX]:
                if current_mode == self._transform_modes[c.SCALE][i][c.INDEX]:
                    NavigationUtils.set_current_scale_mode(self._transform_modes[c.SCALE][i + 1][c.INDEX])
                    info.show_info('R: {0}'.format(self._transform_modes[c.SCALE][i+1][c.NAME]))
                    NavigationUtils.fix_scale_marking_menu()
                    return

        NavigationUtils.set_current_scale_mode(self._transform_modes[c.SCALE][0][c.INDEX])
        info.show_info('R: {0}'.format(self._transform_modes[c.SCALE][0][c.NAME]))
        NavigationUtils.fix_scale_marking_menu()



