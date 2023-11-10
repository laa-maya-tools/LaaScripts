import maya.cmds as cmds

class UndoContext(object):

    def __init__(self, contextName):
        self.contextName = contextName

    def __enter__(self):
        cmds.undoInfo(openChunk=True, chunkName=self.contextName)

    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        cmds.undoInfo(closeChunk=True)


class UndoOff(object):
    
    def __init__(self):
        self.wasUndoEnabled = None

    def __enter__(self):
        self.wasUndoEnabled = cmds.undoInfo(q=True, swf=True)
        cmds.undoInfo(swf=False)

    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        cmds.undoInfo(swf=self.wasUndoEnabled)


class AutoUndo(object):

    def __init__(self):
        self.wasUndoEnabled = None

    def __enter__(self):
        # Needs to enable Undo in case it wasn't
        self.wasUndoEnabled = cmds.undoInfo(q=True, swf=True)
        cmds.undoInfo(swf=True)
        
        # Opens a chunk to undo it on exit
        cmds.undoInfo(openChunk=True, chunkName="AUTO_UNDO")

    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        # Closes the chunk and undoes it
        cmds.undoInfo(closeChunk=True)
        cmds.undo()
        
        # Restore the Undo state
        cmds.undoInfo(swf=self.wasUndoEnabled)

def clearUndo():
    cmds.flushUndo()
