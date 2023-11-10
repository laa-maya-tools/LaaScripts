class TabWidgetBase(object):
    def __init__(self):
        self.currentActor = None
        self.currentSubActor = None
    
    # -------------------------------------------------
    # -------------- Data Load Handling ---------------
    # -------------------------------------------------
    def setCurrentActor(self, act):
        self.currentActor = act
    
    def setCurrentSubActor(self, subAct):
        self.currentSubActor = subAct
    
    def loadCurrentActorData(self):
        raise NotImplementedError
    
    def loadCurrentSubActorData(self):
        raise NotImplementedError
    
    def clearUI(self):
        raise NotImplementedError