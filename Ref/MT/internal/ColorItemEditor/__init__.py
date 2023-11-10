from ColorItemEditor.colorItemEditor import ColorItemEditorWin

def show():
    global colorItemEditorWin
    try:
        if colorItemEditorWin.isVisible():
            colorItemEditorWin.close()
    except NameError:
        pass
    colorItemEditorWin = ColorItemEditorWin()
    colorItemEditorWin.show()