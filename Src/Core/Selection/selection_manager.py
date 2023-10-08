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
import maya.cmds as cmd

import LaaScripts.Src.Utils.info_utils as info
from LaaScripts.Core.Selection.character_info import CharacterInfo


class SelectionManager(object):

    def __init__(self):
        pass

    def next_upperbody_ctrl(self):
        char_info = CharacterInfo.get_active_char_info()
        char_nsp = char_info.split('#')[0]

        upperbody_ctrls = [char_nsp + ':x_rootX000_CTRL',
                           char_nsp + ':x_spineX000_CTRL',
                           char_nsp + ':x_spineX001_CTRL',
                           char_nsp + ':x_spineX002_CTRL',
                           char_nsp + ':x_spineX003_CTRL',
                           char_nsp + ':x_spineX004_CTRL',
                           char_nsp + ':x_neckX000_CTRL',
                           char_nsp + ':x_headX000_CTRL']

        upperbody_huds = [char_nsp + ' | COG',
                          char_nsp + ' | SPINE',
                          char_nsp + ' | NECK',
                          char_nsp + ' | HEAD']

        selected_ctrls = cmd.ls(sl=True)

        if len(selected_ctrls) != 0:
            if selected_ctrls[0] == upperbody_ctrls[0]:
                cmd.select(upperbody_ctrls[1], upperbody_ctrls[2], upperbody_ctrls[3], upperbody_ctrls[4],
                           upperbody_ctrls[5])
                info.show_info(upperbody_huds[1])
                return
            elif selected_ctrls[0] == upperbody_ctrls[1] or selected_ctrls[
                0] == upperbody_ctrls[2] or selected_ctrls[
                0] == upperbody_ctrls[3] or selected_ctrls[
                0] == upperbody_ctrls[4] or selected_ctrls[
                0] == upperbody_ctrls[5]:
                cmd.select(upperbody_ctrls[6])
                info.show_info(upperbody_huds[2])
                return
            elif selected_ctrls[0] == upperbody_ctrls[6]:
                cmd.select(upperbody_ctrls[7])
                info.show_info(upperbody_huds[3])
                return
            else:
                cmd.select(upperbody_ctrls[0])
                info.show_info(upperbody_huds[0])
                return
        else:
            cmd.select(upperbody_ctrls[0])
            info.show_info(upperbody_huds[0])
            return

    def next_lf_arm_ctrl(self):
        char_info = CharacterInfo.get_active_char_info()
        char_nsp = char_info.split('#')[0]

        lf_arm_ctrls = [char_nsp + ':l_upperarmFKX000_CTRL',
                        char_nsp + ':l_forearmFKX000_CTRL',
                        char_nsp + ':l_handFKX000_CTRL',
                        char_nsp + ':l_armIKX000_CTRL',
                        char_nsp + ':l_armPoleVectorX000_CTRL',
                        char_nsp + ':l_clavicleX000_CTRL']

        lf_arm_huds = [char_nsp + ' | LF FK ARM',
                       char_nsp + ' | LF FK ELBOW',
                       char_nsp + ' | LF FK WRIST',
                       char_nsp + ' | LF IK ARM',
                       char_nsp + ' | LF IK ELBOW',
                       char_nsp + ' | LF SHOULDER']

        lf_arm_switch = cmd.getAttr(char_nsp + ':l_armSwitchX000_CTRL.switch_IKFK')

        selected_ctrls = cmd.ls(sl=True)

        # ===== LF FK ARM CONTROLS =====
        if not lf_arm_switch:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == lf_arm_ctrls[0]:
                    cmd.select(lf_arm_ctrls[1])
                    info.show_info(lf_arm_huds[1])
                    return
                elif selected_ctrls[0] == lf_arm_ctrls[1]:
                    cmd.select(lf_arm_ctrls[2])
                    info.show_info(lf_arm_huds[2])
                    return
                elif selected_ctrls[0] == lf_arm_ctrls[2]:
                    cmd.select(lf_arm_ctrls[5])
                    info.show_info(lf_arm_huds[5])
                    return
                else:
                    cmd.select(lf_arm_ctrls[0])
                    info.show_info(lf_arm_huds[0])
                    return
            else:
                cmd.select(lf_arm_ctrls[0])
                info.show_info(lf_arm_huds[0])
                return

        # ===== LF IK ARM CONTROLS =====
        else:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == lf_arm_ctrls[3]:
                    cmd.select(lf_arm_ctrls[4])
                    info.show_info(lf_arm_huds[4])
                    return
                elif selected_ctrls[0] == lf_arm_ctrls[4]:
                    cmd.select(lf_arm_ctrls[5])
                    info.show_info(lf_arm_huds[5])
                    return
                else:
                    cmd.select(lf_arm_ctrls[3])
                    info.show_info(lf_arm_huds[3])
                    return
            else:
                cmd.select(lf_arm_ctrls[3])
                info.show_info(lf_arm_huds[3])
                return

    def next_rt_arm_ctrl(self):
        char_info = CharacterInfo.get_active_char_info()
        char_nsp = char_info.split('#')[0]

        rt_arm_ctrls = [char_nsp + ':r_upperarmFKX000_CTRL',
                        char_nsp + ':r_forearmFKX000_CTRL',
                        char_nsp + ':r_handFKX000_CTRL',
                        char_nsp + ':r_armIKX000_CTRL',
                        char_nsp + ':r_armPoleVectorX000_CTRL',
                        char_nsp + ':r_clavicleX000_CTRL']

        rt_arm_huds = [char_nsp + ' | RT FK ARM',
                       char_nsp + ' | RT FK ELBOW',
                       char_nsp + ' | RT FK WRIST',
                       char_nsp + ' | RT IK ARM',
                       char_nsp + ' | RT IK ELBOW',
                       char_nsp + ' | RT SHOULDER']

        rt_arm_switch = cmd.getAttr(char_nsp + ':r_armSwitchX000_CTRL.switch_IKFK')

        selected_ctrls = cmd.ls(sl=True)

        # ===== RT FK ARM CONTROLS =====
        if not rt_arm_switch:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == rt_arm_ctrls[0]:
                    cmd.select(rt_arm_ctrls[1])
                    info.show_info(rt_arm_huds[1])
                    return
                elif selected_ctrls[0] == rt_arm_ctrls[1]:
                    cmd.select(rt_arm_ctrls[2])
                    info.show_info(rt_arm_huds[2])
                    return
                elif selected_ctrls[0] == rt_arm_ctrls[2]:
                    cmd.select(rt_arm_ctrls[5])
                    info.show_info(rt_arm_huds[5])
                    return
                else:
                    cmd.select(rt_arm_ctrls[0])
                    info.show_info(rt_arm_huds[0])
                    return
            else:
                cmd.select(rt_arm_ctrls[0])
                info.show_info(rt_arm_huds[0])
                return

        # ===== LF IK ARM CONTROLS =====
        else:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == rt_arm_ctrls[3]:
                    cmd.select(rt_arm_ctrls[4])
                    info.show_info(rt_arm_huds[4])
                    return
                elif selected_ctrls[0] == rt_arm_ctrls[4]:
                    cmd.select(rt_arm_ctrls[5])
                    info.show_info(rt_arm_huds[5])
                    return
                else:
                    cmd.select(rt_arm_ctrls[3])
                    info.show_info(rt_arm_huds[3])
                    return
            else:
                cmd.select(rt_arm_ctrls[3])
                info.show_info(rt_arm_huds[3])
                return

    def next_lf_leg_ctrl(self):
        char_info = CharacterInfo.get_active_char_info()
        char_nsp = char_info.split('#')[0]

        lf_leg_ctrls = [char_nsp + ':l_footMainIKX000_CTRL',
                        char_nsp + ':l_legPoleVectorX000_CTRL',
                        char_nsp + ':l_auxPelvisX000_CTRL',
                        char_nsp + ':l_footToeIKX000_CTRL',
                        char_nsp + ':l_thighFKX000_CTRL',
                        char_nsp + ':l_calfFKX000_CTRL',
                        char_nsp + ':l_footMainFKX000_CTRL',
                        char_nsp + ':l_footToeFKX000_CTRL']

        lf_leg_huds = [char_nsp + ' | LF IK FOOT',
                       char_nsp + ' | LF IK PV',
                       char_nsp + ' | LF IK TOE',
                       char_nsp + ' | LF IK ROOT',
                       char_nsp + ' | LF FK THIGH',
                       char_nsp + ' | LF FK KNEE',
                       char_nsp + ' | LF FK FOOT',
                       char_nsp + ' | LF FK TOE']

        lf_leg_switch = cmd.getAttr(char_nsp + ':l_legSwitchX000_CTRL.switch_IKFK')

        selected_ctrls = cmd.ls(sl=True)

        # ===== LF FK LEG CONTROLS =====
        if not lf_leg_switch:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == lf_leg_ctrls[0]:
                    cmd.select(lf_leg_ctrls[1])
                    info.show_info(lf_leg_huds[1])
                    return
                elif selected_ctrls[0] == lf_leg_ctrls[1]:
                    cmd.select(lf_leg_ctrls[2])
                    info.show_info(lf_leg_huds[2])
                    return
                elif selected_ctrls[0] == lf_leg_ctrls[2]:
                    cmd.select(lf_leg_ctrls[3])
                    info.show_info(lf_leg_huds[3])
                    return
                else:
                    cmd.select(lf_leg_ctrls[0])
                    info.show_info(lf_leg_huds[0])
                    return
            else:
                cmd.select(lf_leg_ctrls[0])
                info.show_info(lf_leg_huds[0])
                return

        # ===== LF IK LEG CONTROLS =====
        else:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == lf_leg_ctrls[4]:
                    cmd.select(lf_leg_ctrls[5])
                    info.show_info(lf_leg_huds[5])
                    return
                elif selected_ctrls[0] == lf_leg_ctrls[5]:
                    cmd.select(lf_leg_ctrls[6])
                    info.show_info(lf_leg_huds[6])
                    return
                elif selected_ctrls[0] == lf_leg_ctrls[6]:
                    cmd.select(lf_leg_ctrls[7])
                    info.show_info(lf_leg_huds[7])
                    return
                else:
                    cmd.select(lf_leg_ctrls[4])
                    info.show_info(lf_leg_huds[4])
                    return
            else:
                cmd.select(lf_leg_ctrls[4])
                info.show_info(lf_leg_huds[4])
                return

    def next_rt_leg_ctrl(self):
        char_info = CharacterInfo.get_active_char_info()
        char_nsp = char_info.split('#')[0]

        rt_leg_ctrls = [char_nsp + ':r_footMainIKX000_CTRL',
                        char_nsp + ':r_legPoleVectorX000_CTRL',
                        char_nsp + ':r_auxPelvisX000_CTRL',
                        char_nsp + ':r_footToeIKX000_CTRL',
                        char_nsp + ':r_thighFKX000_CTRL',
                        char_nsp + ':r_calfFKX000_CTRL',
                        char_nsp + ':r_footMainFKX000_CTRL',
                        char_nsp + ':r_footToeFKX000_CTRL']

        rt_leg_huds = [char_nsp + ' | RT IK FOOT',
                       char_nsp + ' | RT IK PV',
                       char_nsp + ' | RT IK TOE',
                       char_nsp + ' | RT IK ROOT',
                       char_nsp + ' | RT FK THIGH',
                       char_nsp + ' | RT FK KNEE',
                       char_nsp + ' | RT FK FOOT',
                       char_nsp + ' | RT FK TOE']

        rt_leg_switch = cmd.getAttr(char_nsp + ':r_legSwitchX000_CTRL.switch_IKFK')

        selected_ctrls = cmd.ls(sl=True)

        # ===== RT FK LEG CONTROLS =====
        if not rt_leg_switch:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == rt_leg_ctrls[0]:
                    cmd.select(rt_leg_ctrls[1])
                    info.show_info(rt_leg_huds[1])
                    return
                elif selected_ctrls[0] == rt_leg_ctrls[1]:
                    cmd.select(rt_leg_ctrls[2])
                    info.show_info(rt_leg_huds[2])
                    return
                elif selected_ctrls[0] == rt_leg_ctrls[2]:
                    cmd.select(rt_leg_ctrls[3])
                    info.show_info(rt_leg_huds[3])
                    return
                else:
                    cmd.select(rt_leg_ctrls[0])
                    info.show_info(rt_leg_huds[0])
                    return
            else:
                cmd.select(rt_leg_ctrls[0])
                info.show_info(rt_leg_huds[0])
                return

        # ===== RT IK LEG CONTROLS =====
        else:
            if len(selected_ctrls) == 1:
                if selected_ctrls[0] == rt_leg_ctrls[4]:
                    cmd.select(rt_leg_ctrls[5])
                    info.show_info(rt_leg_huds[5])
                    return
                elif selected_ctrls[0] == rt_leg_ctrls[5]:
                    cmd.select(rt_leg_ctrls[6])
                    info.show_info(rt_leg_huds[6])
                    return
                elif selected_ctrls[0] == rt_leg_ctrls[6]:
                    cmd.select(rt_leg_ctrls[7])
                    info.show_info(rt_leg_huds[7])
                    return
                else:
                    cmd.select(rt_leg_ctrls[4])
                    info.show_info(rt_leg_huds[4])
                    return
            else:
                cmd.select(rt_leg_ctrls[4])
                info.show_info(rt_leg_huds[4])
                return


if __name__ == "__main__":
    _selection_manager = SelectionManager()
    _selection_manager.next_rt_leg_ctrl()