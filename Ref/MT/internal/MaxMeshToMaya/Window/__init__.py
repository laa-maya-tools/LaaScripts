import MaxMeshToMaya.Window.MainWindow as MaxToMayaMW

def show():
    global maxToMayaWindow
    try:
        if maxToMayaWindow.isVisible():
            maxToMayaWindow.close()
    except NameError:
        pass
    maxToMayaWindow = MaxToMayaMW.MaxToMayaWindow()
    maxToMayaWindow.showWindow(restoreFromClose=True)