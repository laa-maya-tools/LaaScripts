"""
=============================================================================
MODULE: user_data.py
-----------------------------------------------------------------------------
This class is responsible for showing info to the user. This module must
be used by the trigger module, SHOULD NOT BE USED DIRECTLY.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2/3
=============================================================================
"""
import json
import os

from LaaScripts.Src.Constants import constants as c


class UserData(object):

    def __init__(self):
        self.user_data = {}

        if not UserData.dir_exists(c.PATH.LAASCRIPTS_DATA_DIR):
            UserData.create_dir(c.PATH.LAASCRIPTS_DATA_DIR)

        if UserData.file_exists(c.PATH.USER_DATA_FILE):
            self.user_data = UserData.read_user_data(c.PATH.USER_DATA_FILE)
        else:
            self.user_data = UserData.get_default_user_data()
            UserData.store_user_data(self.user_data, c.PATH.USER_DATA_FILE)

    @staticmethod
    def file_exists(file):
        return True if os.path.isfile(file) else False

    @staticmethod
    def dir_exists(dir):
        return True if os.path.exists(dir) else False

    @staticmethod
    def create_dir(dir):
        os.makedirs(dir)

    @staticmethod
    def get_default_user_data():
        user_data = {
            c.USER_DATA.INFO_ENABLED: True,
            c.USER_DATA.WARNINGS_ENABLED: True,
            c.USER_DATA.PLAYBACK_MODE: "loop",
            c.USER_DATA.TIME_INCREMENT: 1
        }
        return user_data

    @staticmethod
    def read_user_data(file):
        try:
            with open(file, 'r') as f:
                user_data = json.load(f)
            return user_data
        except IOError as error:
            print('READING: {0}'.format(error))

    @staticmethod
    def store_user_data(user_data, file):
        try:
            with open(file, 'w+') as json_file:
                json.dump(user_data, json_file)
        except IOError as error:
            print('WRITING: {0}'.format(error))
