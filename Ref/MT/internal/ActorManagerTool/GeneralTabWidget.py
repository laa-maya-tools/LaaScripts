import QtCustomWidgets.UIFileWidget     as UIFileWidget
import ActorManagerTool.TabWidgetBase   as TabWidgetBase
import functools

from importlib import reload
import ActorManagerTool.lib.Utils
reload(ActorManagerTool.lib.Utils)


from PySide2                        import QtCore

from ProjectPath                    import PathTokenizer, Tokens
from ActorManagerTool.lib.Utils     import ToolIcons, Defaults
from Utils.Maya.UndoContext         import UndoContext
from Utils.Python.FileExplorer      import ShowFileExplorer
from Utils.Python.IndexedList       import IndexedList
from QtCustomWidgets.QtUtils        import BlockSignals
from QtCustomWidgets.CurlyCompleter import Completer

#reload(TabWidgetBase)

class GeneralTabWidget(UIFileWidget.UIFileWidget, TabWidgetBase.TabWidgetBase):    
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/GeneralTabWidget.ui", parent=parent)
        TabWidgetBase.TabWidgetBase.__init__(self)
        self.parentWindow = parent
        self.__actorTypes = None
        self.__Defaults = [Defaults.exportPath, Defaults.subActorPath, Defaults.animsPath, Defaults.modelPath, Defaults.modelName]
        self.__exportFields = [self.ui.led_ExportPath, self.ui.led_SubActorPath, self.ui.led_AnimsPath, self.ui.led_ModelPath, self.ui.led_ModelName]
        self.__resetButtons = [self.ui.btn_ResetExpPath, self.ui.btn_ResetSubActorPath, self.ui.btn_ResetAnimsPath, self.ui.btn_RestModelPath, self.ui.btn_ResetModelName]

        custDict = {
            Tokens.TActorName :     "",
            Tokens.TSubActorName:   "",
            Tokens.TActorType :     "",
            Tokens.TBranch:         "{Game}"  #Default branch
        }
        self.tokenizer = PathTokenizer(custDict)
        
        keys = self.tokenizer.GetFullDictionary().keys()
        keys = sorted(keys)
        completer = Completer(keys, None)
        self.ui.led_ExportPath.setCompleter(completer)
        self.ui.led_SubActorPath.setCompleter(completer)
        self.ui.led_AnimsPath.setCompleter(completer)
        self.ui.led_ModelPath.setCompleter(completer)
        self.ui.led_ModelName.setCompleter(completer)
        
        self.ui.btn_ResetExpPath.setIcon(ToolIcons.resetIcon)
        self.ui.btn_ResetSubActorPath.setIcon(ToolIcons.resetIcon)
        self.ui.btn_ResetAnimsPath.setIcon(ToolIcons.resetIcon)
        self.ui.btn_RestModelPath.setIcon(ToolIcons.resetIcon)
        self.ui.btn_ResetModelName.setIcon(ToolIcons.resetIcon)
        self.ui.btn_OpenFolder.setIcon(ToolIcons.rightArrow)
        
        # ***************************** Events Connections
        self._signalsBlocked = False
        # ------------- Actor GroupBox ------------
        self.ui.cbx_ActorType.currentIndexChanged.connect(self.cbx_ActorType_CurrentIndexChanged)
        # ----------- SubActor GroupBox -----------
        self.ui.chb_IsMainSubactor.stateChanged.connect(self.chb_IsMainSubactor_stateChanged)
        self.ui.chb_IsAnimSubactor.stateChanged.connect(self.chb_IsAnimSubactor_stateChanged)
        self.ui.chb_IsModelExportable.stateChanged.connect(self.chb_IsModelExportable_stateChanged)
        # ----------- Export Paths -----------
        for i in range(len(self.__exportFields)):
            self.__exportFields[i].editingFinished.connect(functools.partial(self.led_editingFinished, i))
        
        for i in range(len(self.__resetButtons)):
            self.__resetButtons[i].clicked.connect(functools.partial(self.btn_Reset_Clicked, i))
        
        self.ui.btn_OpenFolder.clicked.connect(self.btn_OpenFolder_Clicked)
        self.ui.led_ExportPath.textChanged.connect(functools.partial(self.led_TextChanged))
        self.ui.led_SubActorPath.textChanged.connect(functools.partial(self.led_TextChanged))
    
    def loadCurrentActorData(self):
        self.checkUIStatus()
        newVals = {Tokens.TActorName: "", Tokens.TActorType: ""}
        if (self.currentActor):
            with BlockSignals(self):
                self.__actorTypes = IndexedList(self.currentActor.getTypes())
                self.ui.cbx_ActorType.addItems(self.__actorTypes.values())
                self.ui.cbx_ActorType.setCurrentIndex(self.__actorTypes.positionofIndex(self.currentActor.type))
            newVals = {Tokens.TActorName: self.currentActor.name, Tokens.TActorType: self.ui.cbx_ActorType.currentText()}
        self.tokenizer.Update(newVals)
    
    def loadCurrentSubActorData(self):
        self.checkUIStatus()
        if (self.currentSubActor):
            newVals = {Tokens.TSubActorName: self.currentSubActor.name, Tokens.TSubActorPath: self.currentSubActor.subActorPathToken}
            self.tokenizer.Update(newVals)
            with BlockSignals(self):
                self.ui.chb_IsMainSubactor.setChecked(self.currentSubActor.isMainSubActor())
                self.ui.chb_IsAnimSubactor.setChecked(self.currentSubActor.isAnimSubActor())
                self.ui.chb_IsModelExportable.setChecked(self.currentSubActor.isModelExportable)
                self.ui.led_ExportPath.setText(self.currentSubActor.exportPath)
                self.ui.led_SubActorPath.setText(self.currentSubActor.subActorPathToken)
                self.ui.led_AnimsPath.setText(self.currentSubActor.animPath)
                self.ui.led_ModelPath.setText(self.currentSubActor.modelPath)
                self.ui.led_ModelName.setText(self.currentSubActor.modelName)
                self.UpdateExpPath()
        else:
            newVals = {Tokens.TSubActorName: ""}
            self.tokenizer.Update(newVals)
    
    def clearUI(self):
        with BlockSignals(self):
            self.checkUIStatus()
            self.ui.cbx_ActorType.clear()
            self.ui.chb_IsMainSubactor.setCheckState(QtCore.Qt.Unchecked)
            self.ui.chb_IsAnimSubactor.setCheckState(QtCore.Qt.Unchecked)
            self.ui.led_ExportPath.clear()
            self.ui.led_SubActorPath.clear()
            self.ui.led_AnimsPath.clear()
            self.ui.led_ModelPath.clear()
            self.ui.led_ModelName.clear()
            self.ui.led_ResultPath.clear()
    
    def checkUIStatus(self):
        self.ui.gbx_Actor.setEnabled(False)
        self.ui.gbx_SubActor.setEnabled(False)
        self.ui.gbx_ExportInfo.setEnabled(False)
        
        if self.currentActor:
            self.ui.gbx_Actor.setEnabled(True)
        
        if self.currentSubActor:
            self.ui.gbx_SubActor.setEnabled(True)
            self.ui.gbx_ExportInfo.setEnabled(True)
    
    def UpdateExpPath(self):
        pth = self.ui.led_ExportPath.text()
        self.ui.led_ResultPath.setText(self.tokenizer.Translate(pth))
    
    # ********************************************************************************************************************
    # ****************************************************** EVENTS ******************************************************
    # ********************************************************************************************************************
    # -----------------------------------------
    # ------------- Actor GroupBox ------------
    # -----------------------------------------
    def cbx_ActorType_CurrentIndexChanged(self, idx):
        if not self._signalsBlocked:
            self.currentActor.type = (self.__actorTypes.indexOfPosition(idx))
            self.tokenizer.Update({Tokens.TActorType: self.ui.cbx_ActorType.currentText()})
            self.UpdateExpPath()
    
    # -----------------------------------------
    # ----------- SubActor GroupBox -----------
    # -----------------------------------------
    def chb_IsMainSubactor_stateChanged(self, value):
        if not self._signalsBlocked:
            value = bool(value)
            if value:
                # Set new Main SubActor
                self.currentActor.mainSubActor = self.currentSubActor
                self.parentWindow.reloadSubActorsBackgrounds()
            else:
                # Prevent the case where we uncheck a main subactor (we always want one)
                with BlockSignals(self):
                    self.ui.chb_IsMainSubactor.setCheckState(QtCore.Qt.Checked)
    
    def chb_IsAnimSubactor_stateChanged(self, value):
        if not self._signalsBlocked:
            value = bool(value)
            if value:
                # Set new Anim SubActor
                self.currentActor.animSubActor = self.currentSubActor
                self.parentWindow.reloadSubActorsBackgrounds()
            else:
                # Prevent the case where we uncheck an anim subactor (we always want one)
                with BlockSignals(self):
                    self.ui.chb_IsAnimSubactor.setCheckState(QtCore.Qt.Checked)
    
    def chb_IsModelExportable_stateChanged(self, value):
        if not self._signalsBlocked:
            if not value:
                self.currentSubActor.isModelExportable = False
            else:
                self.currentSubActor.isModelExportable = True
    
    def led_editingFinished(self, idx):
        if not self._signalsBlocked:
            field = self.__exportFields[idx]
            newValue = field.text()
            subActorProperties = ["self.currentSubActor.exportPath",
                                  "self.currentSubActor.subActorPathToken",
                                  "self.currentSubActor.animPath",
                                  "self.currentSubActor.modelPath",
                                  "self.currentSubActor.modelName"]

            currentValue = exec(subActorProperties[idx])
            if (currentValue != newValue):
                with UndoContext("Set Export Field"):
                    execLine = "{} = newValue"
                    exec(execLine.format(subActorProperties[idx]))
                    #Update SubActorPath Token
                    if (idx == 1):
                        self.tokenizer.Update({Tokens.TSubActorPath: self.currentSubActor.subActorPathToken})
    
    def btn_Reset_Clicked(self, idx):
        field = self.__exportFields[idx]
        field.setText(self.__Defaults[idx])
        self.led_editingFinished(idx)
    
    def btn_OpenFolder_Clicked(self):
        ShowFileExplorer(self.ui.led_ResultPath.text())
    
    def led_TextChanged(self, updateSubActorPath=False):
        if (updateSubActorPath):
            self.tokenizer.Update({Tokens.TSubActorPath: self.ui.led_SubActorPath.text()})
        self.UpdateExpPath()