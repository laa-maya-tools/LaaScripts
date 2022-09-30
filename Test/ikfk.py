import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace

picker = dwpicker.current()
namespace = detect_picker_namespace(picker.shapes)
if cmd.getAttr('{0}:r_legSwitch_000_ctrl.fk_ik'.format(namespace)):
    cmd.setAttr('{0}:r_legSwitch_000_ctrl.fk_ik'.format(namespace), 0)
else:
    cmd.setAttr('{0}:r_legSwitch_000_ctrl.fk_ik'.format(namespace), 1)
