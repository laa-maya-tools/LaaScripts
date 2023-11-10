import CheckSkinInfluences.Window.MainWindow as mw

def show():
    global checkSkinInfluencesWindow
    try:
        if checkSkinInfluencesWindow.isVisible():
            checkSkinInfluencesWindow.close()
    except NameError:
        pass
    checkSkinInfluencesWindow = mw.CheckSkinInfluencesWindow()
    checkSkinInfluencesWindow.showWindow()