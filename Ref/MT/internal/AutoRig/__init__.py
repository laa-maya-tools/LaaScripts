from AutoRig.ui.AutoRigUI import AutoRigWin

def show():
    global autoRigWin
    try:
        if autoRigWin.isVisible():
            autoRigWin.close()
    except NameError:
        pass
    autoRigWin = AutoRigWin()
    autoRigWin.show()