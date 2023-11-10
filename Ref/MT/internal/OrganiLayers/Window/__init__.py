import OrganiLayers.Window.MainWindow as mw

def show():
    global organiLayersWindow
    try:
        if organiLayersWindow.isVisible():
            organiLayersWindow.close()
    except NameError:
        pass
    organiLayersWindow = mw.OrganiLayersWindow()
    organiLayersWindow.showWindow(restoreFromClose=True)