import maya.cmds as cmds
import ControllerTagManager.Window.ControllerTagManagerWindow as mw

def show():
    global controllerTagManagerWindow
    try:
        if controllerTagManagerWindow.isVisible():
            controllerTagManagerWindow.close()
    except NameError:
        pass
    controllerTagManagerWindow = mw.ControllerTagManagerWindow()
    controllerTagManagerWindow.show()
