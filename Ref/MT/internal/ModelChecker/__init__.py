from ModelChecker.modelChecker import ModelCheckerUI

def show():
    global modelCheckerUI
    try:
        if modelCheckerUI.isVisible():
            modelCheckerUI.close()
    except NameError:
        pass
    modelCheckerUI = ModelCheckerUI()
    modelCheckerUI.show()