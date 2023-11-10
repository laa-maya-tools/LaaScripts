from RelativeReferences.MainWindow import RelativeReferencesWindow

def show():
    global relRefsWindow
    try:
        if relRefsWindow.isVisible():
            relRefsWindow.close()
    except NameError:
        pass
    relRefsWindow = RelativeReferencesWindow()
    relRefsWindow.show()