import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace

increment = 0.1

picker = dwpicker.current()
if picker:
    namespace = detect_picker_namespace(picker.shapes)
    upper_arm_length = cmd.getAttr('{0}:l_upperArmFK_000_ctrl.upperArm_fk_length'.format(namespace))
    lower_arm_length = cmd.getAttr('{0}:l_lowerArmFK_000_ctrl.lowerArm_fk_length'.format(namespace))

    cmd.setAttr('{0}:l_upperArmFK_000_ctrl.upperArm_fk_length'.format(namespace), upper_arm_length - increment)
    cmd.setAttr('{0}:l_lowerArmFK_000_ctrl.lowerArm_fk_length'.format(namespace), lower_arm_length - increment)
