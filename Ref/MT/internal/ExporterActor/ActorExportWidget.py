import QtCustomWidgets.UIFileWidget         as UIFileWidget
import ExporterActor.SubActorExportWidget   as SubActorExportWidget

from Utils.Python.IndexedList   import IndexedList
from Utils.Maya.UndoContext     import UndoContext

class ActorExportWidget(UIFileWidget.UIFileWidget):
    __subActorLineHeight = 42
    
    def __init__(self, actor, parent=None, branch=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ExporterActor/ui/ActorExportWidget.ui", parent=parent)
        self.__actorObj = actor
        self.__actorTypes = None
        
        # ********* Name
        self.ui.gbx_Actor.setTitle(actor.name)
        
        # ********* Type/s
        self.__actorTypes = IndexedList(actor.getTypes())
        self.ui.cbx_Type.addItems(self.__actorTypes.values())
        self.ui.cbx_Type.setCurrentIndex(self.__actorTypes.positionofIndex(actor.type))
        
        # ****************** Load SubWidgets ******************
        self.subActorWidgs = self.LoadSubActors(actor.getSubActors(), branch)
        
        # ********* Events Connections
        self.ui.cbx_Type.currentIndexChanged.connect(self.cbx_Type_CurrentIndexChanged)
        self.ui.btn_AllNone.clicked.connect(self.btn_AllNone_Clicked)
    
    def LoadSubActors(self, subActorNodes=[], branch=None):
        result = []
        
        subActorsListLayout = self.ui.frm_SubActors.layout()
        for subAct in subActorNodes:
            if (subAct.isModelExportable):
                subActWidg = SubActorExportWidget.SubActorExportWidget(subAct, self, branch)
                subActorsListLayout.addWidget(subActWidg)
                result.append(subActWidg)
        
        self.ui.scr_SubActors.setFixedHeight(ActorExportWidget.__subActorLineHeight * len(result) + 2)
        return result
    
    def GetSelectedIdxs(self):
        result = []
        
        for i in range(len(self.subActorWidgs)):
            if (self.subActorWidgs[i].ui.ckb_SubActor.isChecked()):
                result.append(i)
        
        return result
    
    def setPathOverride(self, overridePath):
        for subActorWidg in self.subActorWidgs:
            subActorWidg.setPathOverride(overridePath)
    
    def updateExportPath(self, idx):
        self.subActorWidgs[idx].UpdateExpPath()
    
    def updateExportPaths(self):
        for subActorWid in self.subActorWidgs:
            subActorWid.UpdateExpPath()
    
    def GetSubactorsToExport(self):
        result = []
        for subactorWdg in self.subActorWidgs:
            if (subactorWdg.IsChecked()):
                result.append((subactorWdg.GetSubactorObj(), subactorWdg.GetExportPath(), subactorWdg.GetExportFileType(), subactorWdg.GetASCIIMode()))
        return result
    
    # ******************************************************
    # *********************** EVENTS ***********************
    # ******************************************************
    def cbx_Type_CurrentIndexChanged(self, idx):
        with UndoContext("Actor Type Changed"):
            self.__actorObj.type = (self.__actorTypes.indexOfPosition(idx))
            for subAct in self.subActorWidgs:
                subAct.UpdateTokenizer()
                subAct.UpdateExpPath()
    
    def btn_AllNone_Clicked(self):
        seldIdxs = self.GetSelectedIdxs()
        newState = False
        
        if (len(seldIdxs) != len (self.subActorWidgs)):
            newState = True
            
        for subActWidg in self.subActorWidgs:
            subActWidg.ui.ckb_SubActor.setChecked(newState)