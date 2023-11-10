from CreateSkinProxy.createSkinProxy import CreateSkinProxyWin

def show():
    global createSkinProxyWin
    try:
        if createSkinProxyWin.isVisible():
            createSkinProxyWin.close()
    except NameError:
        pass
    createSkinProxyWin = CreateSkinProxyWin()
    createSkinProxyWin.show()