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

        CharacterInfo.update_characters_list_info()

    def switch_active_char(self):
        """
        Switch the active character in the scene and store its value in a node.
        :return: True if a character is set.
        :rtype: bool
        """
        char_list = CharacterInfo.get_characters_list_info()
        if char_list[0] == c.EMPTY_STRING:
            info.show_info('No Character in the scene')
            return False

        active_char = CharacterInfo.get_active_char_info()
        if active_char == c.EMPTY_STRING or active_char == char_list[-1]:
            active_char = char_list[0]
            self.update_active_char_info(active_char)
            return True

        for i, char in enumerate(char_list):
            if active_char == char:
                active_char = char_list[i + 1]
                self.update_active_char_info(active_char)
                return True

        return False

    def toggle_active_char_picker(self):
        char_list = CharacterInfo.get_characters_list_info()
        if char_list[0] == c.EMPTY_STRING:
            info.show_info('No Character in the scene')
            return False

        active_char = CharacterInfo.get_active_char_info()
        if active_char == c.EMPTY_STRING:
            active_char = char_list[0]
            self.update_active_char_info(active_char)

        char_nsp = active_char.split(c.DATA_SEPARATOR)[0]
        costume_nsp = active_char.split(c.DATA_SEPARATOR)[1]

        picker_mode = CharacterInfo.get_picker_mode_info()
        if picker_mode == c.BODY:
            picker_mode = c.FACE
        elif picker_mode == c.FACE:
            picker_mode = c.BOTH
        else:
            picker_mode = c.BODY

        self.load_picker(char_nsp, costume_nsp, picker_mode)
        SceneData.save_scene_data(c.CHAR_INFO_NODE, c.PICKER_MODE_ATTR, picker_mode)
        info.show_info('Picker Mode: {0}'.format(picker_mode.upper()))

    @staticmethod
    def update_picker_mode_info(picker_mode):
        SceneData.save_scene_data(c.CHAR_INFO_NODE, c.PICKER_MODE_ATTR, picker_mode)

    @staticmethod
    def update_characters_list_info():
        """
        Store all the character's info in a node.
        """
        pickers = {
            c.SOURCE_PICKERS: [],
            c.TARGET_PICKERS: []
        }
        chars_list = c.EMPTY_STRING
        chars_namespaces = CharacterInfo.get_all_chars_namespaces()
        for nsp in chars_namespaces:
            costume = CharacterInfo.get_attached_costume(nsp)
            color = CharacterInfo.get_char_color(nsp)
            if costume is None:
                pickers[c.SOURCE_PICKERS].append('{0}'.format('pop'))
            else:
                costume_name = c.COSTUMES[costume.split(c.PREFIX_SEPARATOR)[2]]
                pickers[c.SOURCE_PICKERS].append('{0}{1}'.format('pop', costume_name))
            pickers[c.TARGET_PICKERS].append('{0}#{1}'.format(nsp, costume))

            if chars_list == c.EMPTY_STRING:
                chars_list = '{0}#{1}#{2}'.format(nsp, costume, color)
            else:
                chars_list = '{0};{1}#{2}#{3}'.format(chars_list, nsp, costume, color)

        CharacterInfo.refresh_pickers(pickers[c.SOURCE_PICKERS], pickers[c.TARGET_PICKERS])
        SceneData.save_scene_data(c.CHAR_INFO_NODE, c.CHARS_LIST_ATTR, chars_list)

    def update_active_char_info(self, active_char):
        nsp = active_char.split(c.DATA_SEPARATOR)[0]
        color = active_char.split(c.DATA_SEPARATOR)[-1]
        costume_namespace = active_char.split(c.DATA_SEPARATOR)[1]
        picker_mode = CharacterInfo.get_picker_mode_info()

        if costume_namespace == c.NONE:
            SceneData.save_scene_data(c.CHAR_INFO_NODE, c.ACTIVE_CHAR_ATTR, active_char)
            info.show_info('ACTIVE CHAR:  Pop [ {0} ]'.format(color.upper()))
            self.load_picker(nsp, c.NONE, picker_mode)
            return

        costume_name = c.COSTUMES[costume_namespace.split(c.PREFIX_SEPARATOR)[2]]
        SceneData.save_scene_data(c.CHAR_INFO_NODE, c.ACTIVE_CHAR_ATTR, active_char)
        self.load_picker(nsp, costume_namespace, picker_mode)
        info.show_info('ACTIVE CHAR:  Pop {0} [ {1} ]'.format(costume_name, color.upper()))

    def load_picker(self, char_nsp, prop_nsp=None, mode=c.BODY, add_picker=False):
        """
        Load a DwPicker file.
        :param str char_nsp: Pop Namespace
        :param str prop_nsp: Costume Namespace
        :param mode: Body/Face Picker
        :param add_picker: Add Picker if True
        """
        local_path = CharacterInfo.get_local_path()
        if not add_picker:
            self.picker.clear()

        if mode == c.BOTH:
            if prop_nsp is None:
                picker_body_file = r'{0}/{1}#None#{2}.json'.format(local_path, char_nsp, c.BODY)
                picker_face_file = r'{0}/{1}#None#{2}.json'.format(local_path, char_nsp, c.FACE)
            else:
                picker_body_file = r'{0}/{1}#{2}#{3}.json'.format(local_path, char_nsp, prop_nsp, c.BODY)
                picker_face_file = r'{0}/{1}#{2}#{3}.json'.format(local_path, char_nsp, prop_nsp, c.FACE)
            self.picker.add_picker_from_file(picker_body_file)
            self.picker.add_picker_from_file(picker_face_file)
        else:
            if prop_nsp is None:
                picker_file = r'{0}/{1}#None#{2}.json'.format(local_path, char_nsp, mode)
            else:
                picker_file = r'{0}/{1}#{2}#{3}.json'.format(local_path, char_nsp, prop_nsp, mode)
            self.picker.add_picker_from_file(picker_file)

    @staticmethod
    def get_characters_list_info():
        chars_list = SceneData.load_scene_data(c.CHAR_INFO_NODE, c.CHARS_LIST_ATTR).split(c.LIST_SEPARATOR)
        return chars_list

    @staticmethod
    def get_active_char_info():
        active_char = SceneData.load_scene_data(c.CHAR_INFO_NODE, c.ACTIVE_CHAR_ATTR)
        return active_char

    @staticmethod
    def get_picker_mode_info():
        picker_mode = SceneData.load_scene_data(c.CHAR_INFO_NODE, c.PICKER_MODE_ATTR)
        return picker_mode

    @staticmethod
    def get_all_scene_namespaces():
        namespaces = []

        for nsp in cmd.namespaceInfo(lon=True):
            if nsp not in c.EXCLUDED_NAMESPACES:
                namespaces.append(nsp)

        return namespaces

    @staticmethod
    def get_all_chars_namespaces():
        scene_namespaces = CharacterInfo.get_all_scene_namespaces()
        namespaces = []

        for nsp in scene_namespaces:
            char = nsp.split(c.PREFIX_SEPARATOR)[1]
            prop = nsp.split(c.PREFIX_SEPARATOR)[2]
            if not char.startswith(c.PR) and not prop.startswith(c.PR):
                namespaces.append(nsp)

        return namespaces

    @staticmethod
    def get_all_costumes_namespaces():
        scene_namespaces = CharacterInfo.get_all_scene_namespaces()
        namespaces = []

        for nsp in scene_namespaces:
            prop = nsp.split(c.PREFIX_SEPARATOR)[2]
            if prop.startswith(c.PR) and prop in c.COSTUMES:
                namespaces.append(prop)

        return namespaces

    @staticmethod
    def get_char_color(namespace):
        color_attr = '{0}:{1}.{2}'.format(namespace, c.MAIN_CTRL, c.COLOR_ATTR)
        return c.COLORS[cmd.getAttr(color_attr)]

    @staticmethod
    def get_attached_costume(namespace):
        color_attr = '{0}:{1}.{2}'.format(namespace, c.MAIN_CTRL, c.COLOR_ATTR)
        connection = cmd.listConnections(color_attr, d=True, s=False)[-1]
        costume_nsp = connection.split(':')[0]
        formatted_str = costume_nsp.split('_')
        costume_prefix = '{0}_{1}_{2}'.format(formatted_str[0], formatted_str[1], formatted_str[2])

        if not costume_prefix == namespace:
            return costume_nsp
        return None

    @staticmethod
    def refresh_pickers(source_pickers, target_pickers):
        local_path = CharacterInfo.get_local_path()
        CharacterInfo.create_dir(local_path)

        for i, target_picker in enumerate(target_pickers):
            source_body_picker = r'{0}/{1}_body.json'.format(c.PICKERS_PATH, source_pickers[i])
            target_body_picker = r'{0}/{1}#body.json'.format(local_path, target_picker)
            source_face_picker = r'{0}/{1}_face.json'.format(c.PICKERS_PATH, source_pickers[i])
            target_face_picker = r'{0}/{1}#face.json'.format(local_path, target_picker)

            CharacterInfo.copy_file(source_body_picker, target_body_picker)
            CharacterInfo.copy_file(source_face_picker, target_face_picker)

            # ----- Replace Namespace -----
            new_char_nsp = target_picker.split(c.DATA_SEPARATOR)[0]
            new_costume_nsp = target_picker.split(c.DATA_SEPARATOR)[1]
            base_costume_nsp = new_costume_nsp[:-1] + '1'

            CharacterInfo.replace_text_in_file(target_body_picker, 'lea_ch0015_1', new_char_nsp)
            CharacterInfo.replace_text_in_file(target_face_picker, 'lea_ch0015_1', new_char_nsp)
            CharacterInfo.replace_text_in_file(target_body_picker, base_costume_nsp, new_costume_nsp)
            CharacterInfo.replace_text_in_file(target_face_picker, base_costume_nsp, new_costume_nsp)

    @staticmethod
    def get_local_path():
        scene_full_name = cmd.file(query=True, sn=True)
        scene_name_ext = scene_full_name.split('/')[-1]
        local_path = scene_full_name.replace(scene_name_ext, c.LOCAL_FOLDER)
        return local_path

    @staticmethod
    def copy_file(source_file, destiny_file):
        shutil.copy(source_file, destiny_file)

    @staticmethod
    def create_dir(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    @staticmethod
    def replace_text_in_file(file, old_text, new_text):
        fin = open(file, "rt")
        data = fin.read()
        data = data.replace(old_text, new_text)
        fin.close()
        fin = open(file, "wt")
        fin.write(data)
        fin.close()


if __name__ == "__main__":
    _char_info = CharacterInfo()
    _char_info.switch_active_char()
    # print(CharacterInfo.get_all_chars_namespaces())