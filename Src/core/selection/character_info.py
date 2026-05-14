"""
=============================================================================
MODULE: character_info.py
-----------------------------------------------------------------------------
This class manages all character's selection functionality including changing
the active character, storing character's info or loading pickers files.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import os
import maya.cmds as cmd
import shutil
import dwpicker

import LaaScripts.Src.Utils.info_utils as info
from LaaScripts.Src.Data.scene_data import SceneData
from LaaScripts.Src.Constants import constants as c


class CharacterInfo(object):

    def __init__(self):
        """
        Initialization method.
        """
        self.picker = dwpicker._dwpicker
        self.picker.show()
        info.show_info('DwPicker Loaded')

    def switch_active_char(self):
        """
        Switch the active character in the scene and store its value in a node.
        :return: True if a character is set.
        :rtype: bool
        """
        namespaces = CharacterInfo.get_all_namespaces()
        if namespaces[0] == c.STRING.EMPTY:
            info.show_info('No Character in the scene')
            return False

        active_char = CharacterInfo.get_active_char_info()
        if active_char == c.STRING.EMPTY or active_char == namespaces[-1]:
            active_char = namespaces[0]
            self.update_active_char_info(active_char)
            return True

        for i, char in enumerate(namespaces):
            if active_char == char:
                active_char = namespaces[i + 1]
                self.update_active_char_info(active_char)
                return True

        return False

    # def toggle_active_char_picker(self):
    #     namespaces = CharacterInfo.get_characters_list_info()
    #     if namespaces[0] == c.STRING.EMPTY:
    #         info.show_info('No Character in the scene')
    #         return False
    #
    #     active_char = CharacterInfo.get_active_char_info()
    #     if active_char == c.STRING.EMPTY:
    #         active_char = namespaces[0]
    #         self.update_active_char_info(active_char)
    #
    #     char_nsp = active_char.split(c.DATA_SEPARATOR)[0]
    #     costume_nsp = active_char.split(c.DATA_SEPARATOR)[1]
    #
    #     picker_mode = CharacterInfo.get_picker_mode_info()
    #     if picker_mode == c.BODY:
    #         picker_mode = c.FACE
    #     elif picker_mode == c.FACE:
    #         picker_mode = c.BOTH
    #     else:
    #         picker_mode = c.BODY
    #
    #     self.load_picker(char_nsp, costume_nsp, picker_mode)
    #     SceneData.save_scene_data(c.CHAR_INFO_NODE, c.PICKER_MODE_ATTR, picker_mode)
    #     info.show_info('Picker Mode: {0}'.format(picker_mode.upper()))

    def update_active_char_info(self, active_char):
        SceneData.save_scene_data(c.NODES.CHAR_INFO_NODE, c.NODES.ACTIVE_CHAR_ATTR, active_char)
        info.show_info('ACTIVE CHAR: {0}'.format(active_char.upper()))
        self.load_picker(active_char)

    def load_picker(self, char_nsp, add_picker=False):
        """
        Load a DwPicker file.
        :param str char_nsp: Pop Namespace
        :param add_picker: Add Picker if True
        """
        if not add_picker:
            self.picker.clear()

        picker_file = r'{0}/{1}.json'.format(c.PATH.PICKERS_DIR, char_nsp)
        self.picker.add_picker_from_file(picker_file)

    @staticmethod
    def get_active_char_info():
        active_char = SceneData.load_scene_data(c.NODES.CHAR_INFO_NODE, c.NODES.ACTIVE_CHAR_ATTR)
        return active_char

    @staticmethod
    def get_all_namespaces():
        namespaces = []

        for nsp in cmd.namespaceInfo(lon=True):
            if nsp not in c.NAMESPACES.EXCLUDED:
                namespaces.append(nsp)

        return namespaces
