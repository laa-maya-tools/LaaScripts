import CinematicEditor.Cutscene as Cutscene

from Utils.Maya.UndoContext import UndoContext

# ------------------------------------
# | Cutscene Methods                 |
# ------------------------------------

def getCutscene(createIfNotExists=False):
    cutscenes = Cutscene.Cutscene.getInstances()
    if len(cutscenes) == 0:
        if createIfNotExists:
            with UndoContext("Create Cutscene"):
                cutscene = Cutscene.Cutscene().create()
                cutscene.createCutsceneRoot()
                return cutscene
        else:
            return None
    else:
        return cutscenes[0]
