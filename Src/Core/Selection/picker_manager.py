"""
=============================================================================
MODULE: info_utils.py
-----------------------------------------------------------------------------
This class is responsible for showing info and warnings to the user.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import os
import maya.cmds as cmd
import shutil

import LaaScripts.Src.Utils.info_utils as info
from LaaScripts.Src.Data.scene_data import SceneData
from LaaScripts.Src.Core.Selection.character_info import CharacterInfo
from LaaScripts.Src.Constants import constants as c


class PickerManager(object):

    def __init__(self):
        self.picker = dwpicker._dwpicker
        self.picker.show()

        PickerManager.refresh_pickers()

    @staticmethod
    def refresh_pickers():
        chars_list = SceneData.load_scene_data(c.CHAR_INFO_NODE, c.CHARS_LIST_ATTR)
        print
        chars_list

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
    # PickerManager.refresh_pickers()
    _char_info = CharacterInfo()
    _char_info.switch_active_char()
