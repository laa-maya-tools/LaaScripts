import maya.cmds as cmd
import dwpicker
from dwpicker.namespace import detect_picker_namespace, switch_namespace

picker = dwpicker.current()
current_namespace = detect_picker_namespace(picker.shapes)

def get_namespaces():
    ctrls_list = cmd.ls('rocky_*:x_main_000_ctrl')
    return [nsp_list.split(':')[0] for nsp_list in ctrls_list]

all_namespaces = get_namespaces()
if len(nsp) > 1:
    for namespace in all_namespaces:
        if current_namespace != namespace:
            print(namespace)


