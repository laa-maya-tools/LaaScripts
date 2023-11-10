from ConnectionManager.window.connectionManagerUI import ConnectionManagerWin

def show():
    global connectionManagerUI
    try:
        if connectionManagerUI.isVisible():
            connectionManagerUI.close()
    except NameError:
        pass
    connectionManagerUI = ConnectionManagerWin()
    connectionManagerUI.show()