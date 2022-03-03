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


class UserData(cor.QObject):

    @staticmethod
    def read_user_data():
        with open("C:\Users\leandro_laa\Documents\maya\scripts\LaaScripts_Data\user_data.json", 'r') as f:
            data = json.load(f)
        return data

    @staticmethod
    def store_user_data(data):
        with open("C:\Users\leandro_laa\Documents\maya\scripts\LaaScripts_Data\user_data.json", 'w') as json_file:
            json.dump(data, json_file)




