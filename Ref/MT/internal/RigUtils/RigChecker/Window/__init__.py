import maya.cmds as cmds
import RigUtils.RigChecker.Window.RigCheckerWindow as mw

def show():
    global rigCheckerWindow
    try:
        if rigCheckerWindow.isVisible():
            rigCheckerWindow.close()
    except NameError:
        pass
    rigCheckerWindow = mw.RigCheckerWindow()
    rigCheckerWindow.show()
