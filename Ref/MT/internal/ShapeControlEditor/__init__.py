from ShapeControlEditor.shapeControlEditor import ShapeControlEditorWin

def show():
    global shapeControlEditorWin
    try:
        if shapeControlEditorWin.isVisible():
            shapeControlEditorWin.close()
    except NameError:
        pass
    shapeControlEditorWin = ShapeControlEditorWin()
    shapeControlEditorWin.show()