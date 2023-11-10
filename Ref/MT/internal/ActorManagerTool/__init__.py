from ActorManagerTool.ActorManagerWindow import ActorManagerWindow

def show():
    global actorManagerWindow
    try:
        if actorManagerWindow.isVisible():
            actorManagerWindow.close()
    except NameError:
        pass
    actorManagerWindow = ActorManagerWindow()
    actorManagerWindow.show()