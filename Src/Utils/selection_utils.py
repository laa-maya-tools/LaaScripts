"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to get/set timeline keyframing
data.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel
from LaaScripts.Src.Constants import constants as c
from LaaScripts.Src.Data.scene_data import SceneData


class SelectionUtils(object):

    @staticmethod
    def list_selected_objects():
        return cmd.ls(sl=True) or []

    @staticmethod
    def list_channelbox_selection():
        selected_channels = cmd.channelBox('mainChannelBox', q=True, sma=True)
        return selected_channels or []


if __name__ == '__main__':
    print(SelectionUtils.list_channelbox_selection())
