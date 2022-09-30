import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace

default_value = 1

picker = dwpicker.current()
if picker:
    namespace = detect_picker_namespace(picker.shapes)
    cmd.setAttr('{0}:l_upperArmFK_000_ctrl.upperArm_fk_length'.format(namespace), default_value)
    cmd.setAttr('{0}:l_lowerArmFK_000_ctrl.lowerArm_fk_length'.format(namespace), default_value)
