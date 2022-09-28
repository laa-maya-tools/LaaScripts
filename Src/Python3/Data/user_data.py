"""
=============================================================================
MODULE: user_data.py
-----------------------------------------------------------------------------
This class is responsible for showing info to the user. This module must
be used by the trigger module, SHOULD NOT BE USED DIRECTLY.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2019 | Python 2
=============================================================================
"""
import json
import os

USER_PATH = r"{0}".format(os.path.expanduser("~"))
FILE_PATH = USER_PATH + '/Documents/maya/scripts/LaaScripts_Data/user_data.json'


class UserData(object):

    @staticmethod
    def read_user_data():
        try:
            with open(FILE_PATH, 'r') as f:
                data = json.load(f)
            return data
        except IOError as error:
            print(error)

    @staticmethod
    def store_user_data(data):
        try:
            with open(FILE_PATH, 'w') as json_file:
                json.dump(data, json_file)
        except IOError as error:
            print(error)





