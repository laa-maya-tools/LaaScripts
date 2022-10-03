import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace, switch_namespace

picker = dwpicker.current()
current_namespace = detect_picker_namespace(picker.shapes)


def get_namespaces():
    ctrls_list = cmd.ls('rocky_*:x_main_000_ctrl')
    return [nsp_list.split(':')[0] for nsp_list in ctrls_list]


def change_namespace(namespace):
    for shape in picker.shapes:
        if not shape.targets():
            continue
        targets = [switch_namespace(t, namespace) for t in shape.targets()]
        shape.options['action.targets'] = targets


all_namespaces = get_namespaces()
if len(all_namespaces) > 1:
    for i, namespace in enumerate(all_namespaces):
        if current_namespace == all_namespaces[-1]:
            change_namespace(all_namespaces[0])
            break
        elif current_namespace == namespace:
            change_namespace(all_namespaces[i+1])
            break
