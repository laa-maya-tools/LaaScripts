# # Fixes an error with the channelbox
# from Src.Python
# import maya.cmds as cmd
#
# cmd.optionVar(intValue=('containerSelRootsInOutliner', True))
# cmd.optionVar(intValue=('containerChanBoxMaxWithTemplate', 10))
# cmd.optionVar(intValue=('containerChanBoxMaxNoTemplate', 10))
# cmd.optionVar(intValue=('containerFlatViewCap', 10))

import maya.cmds as cmd
import sys

from LaaScripts.Src.Python3 import trigger

PYTHON2, PYTHON3 = 2, 3


def get_python_version():
    python_version = int("%s%s" % (sys.version_info[0], sys.version_info[1]))
    return python_version


def run():
    if get_python_version() == PYTHON2:
        from LaaScripts.Src.Python2 import trigger
        reload(trigger)
    elif get_python_version() == PYTHON3:
        from LaaScripts.Src.Python3 import trigger
        import importlib
        importlib.reload(trigger)
