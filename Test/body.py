import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace

picker = dwpicker.current()
namespace = detect_picker_namespace(picker.shapes)
if cmd.getAttr('{0}:x_bodyX000_GEO.visibility'.format(namespace)):
    cmd.setAttr('{0}:x_bodyX000_GEO.visibility'.format(namespace), 0)
else:
    cmd.setAttr('{0}:x_bodyX000_GEO.visibility'.format(namespace), 1)

