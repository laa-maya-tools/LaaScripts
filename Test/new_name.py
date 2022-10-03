import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace, switch_namespace

picker = dwpicker.current()
current_namespace = detect_picker_namespace(picker.shapes)


def change_namespace(namespace):
    for shape in picker.shapes:
        if not shape.targets():
            continue
        targets = [switch_namespace(t, namespace) for t in shape.targets()]
        shape.options['action.targets'] = targets

    # self.data_changed_from_picker(picker)


change_namespace('rocky_2')