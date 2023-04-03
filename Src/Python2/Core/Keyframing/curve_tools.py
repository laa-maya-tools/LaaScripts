import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Python2.Constants import constants as c
from LaaScripts.Src.Python2.Utils import info_utils as info


class CurveTools(object):

    def __init__(self):
        print('curve')

    def set_smart_key(self):
        mel.eval('ackSliceCurves;')
        info.show_info('Smart Key Set')

    def delete_redundant(self):
        mel.eval('ackDeleteRedundant;')
        info.show_info('Redundant Keys Deleted')

    def push_keys(self):
        mel.eval('ackPushPull "push";')
        info.show_info('Keys Pushed')

    def pull_keys(self):
        mel.eval('ackPushPull "pull";')
        info.show_info('Keys Pulled')

    def zero_out_keys(self):
        mel.eval('ackZeroOutKeys;')
        info.show_info('Keys set to Zero')

    def snap_to_buffer(self):
        mel.eval('ackConvergeBuffer "snap";')
        info.show_info('Snap to Buffer')

    def converge_to_buffer(self):
        mel.eval('ackConvergeBuffer "toward"')
        info.show_info('Towards Buffer')

    def diverge_from_buffer(self):
        mel.eval('ackConvergeBuffer "away"')
        info.show_info('Away from Buffer')


if __name__ == '__main__':
    ct = CurveTools()
    ct.zero_out_keys()
