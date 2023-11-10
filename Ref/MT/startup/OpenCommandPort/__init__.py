#-----------------------
#|  OPEN COMMAND PORT  |
#-----------------------
# Opens the command ports necessary for other programs to send code into Maya.

import maya.cmds as cmds

def init():
    try:
        cmds.commandPort(name=":7001", close=True)
    except:
        pass
    try:
        cmds.commandPort(name=":7002", close=True)
    except:
        pass

    cmds.commandPort(name=":7001", sourceType="mel")
    cmds.commandPort(name=":7002", sourceType="python")