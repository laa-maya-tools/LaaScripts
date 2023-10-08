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

from LaaShelf.Src.Constants import constants as c
from LaaShelf.Src.Utils import info_utils as info
from LaaShelf.Src.Utils.navigation_utils import NavigationUtils


class SmartManipulator(object):

    def __init__(self):
        self._transform_modes = {
            c.NAVIGATION.MOVE: [[c.NAVIGATION.LOCAL, 0], [c.NAVIGATION.WORLD, 2]],
            c.NAVIGATION.ROTATE: [[c.NAVIGATION.LOCAL, 0], [c.NAVIGATION.WORLD, 1], [c.NAVIGATION.GIMBAL, 2]],
            c.NAVIGATION.SCALE: [[c.NAVIGATION.LOCAL, 0], [c.NAVIGATION.WORLD, 2]]
        }

        self._transform_attrs = {
            c.NAVIGATION.MOVE: [c.NAVIGATION.TX, c.NAVIGATION.TY, c.NAVIGATION.TZ],
            c.NAVIGATION.ROTATE: [c.NAVIGATION.RX, c.NAVIGATION.RY, c.NAVIGATION.RZ],
            c.NAVIGATION.SCALE: [c.NAVIGATION.SX, c.NAVIGATION.SY, c.NAVIGATION.SZ]
        }

    def smart_translate_manipulator(self):
        """
        Switch the translate manipulator coordinate system between local and world.
        """
        cmd.undoInfo(stateWithoutFlush=False)
        current_mode = NavigationUtils.get_current_move_mode()
        NavigationUtils.reset_rotate_mode(self._transform_modes[c.NAVIGATION.ROTATE][-1][c.NAVIGATION.INDEX])
        NavigationUtils.reset_scale_mode(self._transform_modes[c.NAVIGATION.SCALE][-1][c.NAVIGATION.INDEX])
        cmd.setToolTo(c.NAVIGATION.MOVE)

        for i, mode in enumerate(self._transform_modes[c.NAVIGATION.MOVE]):

            if not current_mode == self._transform_modes[c.NAVIGATION.MOVE][-1][c.NAVIGATION.INDEX]:
                if current_mode == self._transform_modes[c.NAVIGATION.MOVE][i][c.NAVIGATION.INDEX]:
                    NavigationUtils.set_current_move_mode(self._transform_modes[c.NAVIGATION.MOVE][i + 1][c.NAVIGATION.INDEX])
                    info.show_info('W: {0}'.format(self._transform_modes[c.NAVIGATION.MOVE][i+1][c.NAVIGATION.NAME]))
                    cmd.undoInfo(stateWithoutFlush=True)
                    NavigationUtils.fix_translate_marking_menu()
                    return

        NavigationUtils.set_current_move_mode(self._transform_modes[c.NAVIGATION.MOVE][0][c.NAVIGATION.INDEX])
        info.show_info('W: {0}'.format(self._transform_modes[c.NAVIGATION.MOVE][0][c.NAVIGATION.NAME]))
        cmd.undoInfo(stateWithoutFlush=True)
        NavigationUtils.fix_translate_marking_menu()

    def smart_rotate_manipulator(self):
        """
        Switch the rotate manipulator coordinate system between local, world and gimbal.
        """
        cmd.undoInfo(stateWithoutFlush=False)
        current_mode = NavigationUtils.get_current_rotate_mode()
        NavigationUtils.reset_move_mode(self._transform_modes[c.NAVIGATION.MOVE][-1][c.NAVIGATION.INDEX])
        NavigationUtils.reset_scale_mode(self._transform_modes[c.NAVIGATION.SCALE][-1][c.NAVIGATION.INDEX])
        cmd.setToolTo(c.NAVIGATION.ROTATE)

        for i, mode in enumerate(self._transform_modes[c.NAVIGATION.ROTATE]):

            if not current_mode == self._transform_modes[c.NAVIGATION.ROTATE][-1][c.NAVIGATION.INDEX]:
                if current_mode == self._transform_modes[c.NAVIGATION.ROTATE][i][c.NAVIGATION.INDEX]:
                    NavigationUtils.set_current_rotate_mode(self._transform_modes[c.NAVIGATION.ROTATE][i + 1][c.NAVIGATION.INDEX])
                    info.show_info('E: {0}'.format(self._transform_modes[c.NAVIGATION.ROTATE][i + 1][c.NAVIGATION.NAME]))
                    cmd.undoInfo(stateWithoutFlush=True)
                    NavigationUtils.fix_rotate_marking_menu()
                    return

        NavigationUtils.set_current_rotate_mode(self._transform_modes[c.NAVIGATION.ROTATE][0][c.NAVIGATION.INDEX])
        info.show_info('E: {0}'.format(self._transform_modes[c.NAVIGATION.ROTATE][0][c.NAVIGATION.NAME]))
        cmd.undoInfo(stateWithoutFlush=True)
        NavigationUtils.fix_rotate_marking_menu()

    def smart_scale_manipulator(self):
        """
        Switch the scale manipulator coordinate system between local and world.
        """
        cmd.undoInfo(stateWithoutFlush=False)
        current_mode = NavigationUtils.get_current_scale_mode()
        NavigationUtils.reset_move_mode(self._transform_modes[c.NAVIGATION.MOVE][-1][c.NAVIGATION.INDEX])
        NavigationUtils.reset_rotate_mode(self._transform_modes[c.NAVIGATION.SCALE][-1][c.NAVIGATION.INDEX])
        cmd.setToolTo(c.NAVIGATION.SCALE)

        for i, mode in enumerate(self._transform_modes[c.NAVIGATION.SCALE]):

            if not current_mode == self._transform_modes[c.NAVIGATION.SCALE][-1][c.NAVIGATION.INDEX]:
                if current_mode == self._transform_modes[c.NAVIGATION.SCALE][i][c.NAVIGATION.INDEX]:
                    NavigationUtils.set_current_scale_mode(self._transform_modes[c.NAVIGATION.SCALE][i + 1][c.NAVIGATION.INDEX])
                    info.show_info('R: {0}'.format(self._transform_modes[c.NAVIGATION.SCALE][i + 1][c.NAVIGATION.NAME]))
                    cmd.undoInfo(stateWithoutFlush=True)
                    NavigationUtils.fix_scale_marking_menu()
                    return

        NavigationUtils.set_current_scale_mode(self._transform_modes[c.NAVIGATION.SCALE][0][c.NAVIGATION.INDEX])
        info.show_info('R: {0}'.format(self._transform_modes[c.NAVIGATION.SCALE][0][c.NAVIGATION.NAME]))
        cmd.undoInfo(stateWithoutFlush=True)
        NavigationUtils.fix_scale_marking_menu()
