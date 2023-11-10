import os
import QtCustomWidgets.UIFileWidget as UIFileWidget

from PySide2        import QtCore, QtWidgets
from ProjectPath    import PathTokenizer, Tokens

from Utils.Maya.UndoContext         import UndoContext
from Utils.Python.IndexedList       import IndexedList
from Utils.Python.FileExplorer      import ShowFileExplorer
from QtCustomWidgets.CurlyCompleter import Completer

class SubActorExportWidget(UIFileWidget.UIFileWidget):
    __overridePathToken = "OverridePath"
    __defaultExpPathConfig = "{{{}}}\\{{{}}}\\{{{}}}\\models".format(Tokens.TGameActors, Tokens.TActorType, Tokens.TActorName)
    __defaultExpNameConfig = "{{{}}}_{{{}}}".format(Tokens.TActorName, Tokens.TSubActorName)
    
    def __init__(self, subActor, parent=None, branch=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ExporterActor/ui/SubActorExportWidget.ui", parent=parent)
        
        self.__subActorObj = subActor
        self.__enabled = True
        self.__overriddenPath = False
        self.__preOverriddenOriginalPath = None
        self.__parentInst = parent
        self.__expPathTemplate = "{}\\{}{}"
        self.__fileTypes = None
        custDict = {
            Tokens.TSubActorPath        : subActor.subActorPathToken,
            Tokens.TSubActorExportPath  : subActor.exportPath,
            #Tokens.TSubActorModelPath   : subActor.modelPath,
            #Tokens.TSubActorAnimPath    : subActor.animPath,
            Tokens.TSubActorName        : subActor.name,
            Tokens.TActorName   : self.GetActorName(),
            Tokens.TActorType   : self.GetActorType(),
            Tokens.TBranch      : branch
        }
        
        self.tokenizer = PathTokenizer(custDict)
        self.currentFocusWidget = None
        self.PreviousFocusWidget = None
        
        # ********* Name
        self.ui.ckb_SubActor.setText(subActor.name)
        
        # ********* Export Path Text
        self.ui.led_ExpPath.setText(subActor.modelPath if (subActor.modelPath != None and subActor.modelPath != '') else SubActorExportWidget.__defaultExpPathConfig)
        
        # ********* Export Path Name
        self.ui.led_ExpName.setText(subActor.modelName if (subActor.modelName != None and subActor.modelName != '') else SubActorExportWidget.__defaultExpNameConfig)
        
        # ********* Type/s
        self.__fileTypes = IndexedList(subActor.getFileTypes())
        self.ui.cbx_FileExtension.addItems(self.__fileTypes.values())
        self.ui.cbx_FileExtension.setCurrentIndex(self.__fileTypes.positionofIndex(subActor.modelFileType))
        
        # ********* Full Translated Export Path
        pth = self.GetExportPath()
        self.ui.led_ResultPath.setText(pth)
        
        # ********* Tokens Completer
        keys = self.tokenizer.GetFullDictionary().keys()
        keys = sorted(keys)
        completer = Completer(keys, None)
        self.ui.led_ExpPath.setCompleter(completer)
        self.ui.led_ExpName.setCompleter(completer)
        self.ui.led_ExpPath.installEventFilter(self)
        self.ui.led_ExpName.installEventFilter(self)
        self.ui.led_ExpPath.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.led_ExpName.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.led_ResultPath.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        
        # ********* Events Connections
        self.ui.led_ExpPath.textChanged.connect(self.led_ExpPath_TextChanged)
        self.ui.led_ExpName.textChanged.connect(self.led_ExpName_TextChanged)
        self.ui.led_ExpPath.editingFinished.connect(self.led_ExpPath_editingFinished)
        self.ui.led_ExpName.editingFinished.connect(self.led_ExpName_editingFinished)
        self.ui.ckb_SubActor.stateChanged.connect(self.ckb_SubActor_StateChanged)
        self.ui.cbx_FileExtension.currentIndexChanged.connect(self.cbx_FileExtension_CurrentIndexChanged)
        self.ui.btn_ExpPath.clicked.connect(self.btn_ExpPath_Clicked)
        self.ui.led_ExpPath.customContextMenuRequested.connect(self.__GenerateContextMenu)
        self.ui.led_ExpName.customContextMenuRequested.connect(self.__GenerateContextMenu)
        self.ui.led_ResultPath.customContextMenuRequested.connect(self.__led_ResultPath_customContextMenuRequested)
        
        # ********* Actions
        self.TranslateAction    = QtWidgets.QAction("Translate", None)
        self.TokenizeAction     = QtWidgets.QAction("Tokenize", None)
        self.OpenPathAction     = QtWidgets.QAction("Open in File Browser", None)
        self.TranslateAction.triggered.connect(self.TranslateAction_Triggered)
        self.TokenizeAction.triggered.connect(self.TokenizeAction_Triggered)
        self.OpenPathAction.triggered.connect(self.OpenPathAction_Triggered)
    
    def eventFilter(self, object, event):
        if event.type()== QtCore.QEvent.FocusIn:
            self.currentFocusWidget = object
        return False
    
    def __GenerateContextMenu(self, location):
        menu = self.ui.led_ExpPath.createStandardContextMenu()
        menu.addSeparator()
        menu.addAction(self.TranslateAction)
        menu.addAction(self.TokenizeAction)
        menu.popup(self.currentFocusWidget.mapToGlobal(location))
    
    def __led_ResultPath_customContextMenuRequested(self, location):
        menu = self.ui.led_ResultPath.createStandardContextMenu()
        menu.addSeparator()
        menu.addAction(self.OpenPathAction)
        menu.popup(self.ui.led_ResultPath.mapToGlobal(location))
    
    def GetActorName(self):
        return self.__parentInst.ui.gbx_Actor.title()
    
    def GetActorType(self):
        return self.__parentInst.ui.cbx_Type.currentText()
    
    def GetExportPath(self, translated=True):
        result = self.__expPathTemplate.format(self.ui.led_ExpPath.text(), self.ui.led_ExpName.text(), self.ui.cbx_FileExtension.currentText())
        
        if (translated):
            result = self.tokenizer.Translate(result)
        
        return result
    
    def GetExportFileType(self):
        return self.ui.cbx_FileExtension.currentText()
    
    def GetASCIIMode(self):
        return (self.ui.ckb_Ascii.isVisible() and self.ui.ckb_Ascii.isChecked())
    
    def SetBranch(self, val):
        self.tokenizer.Update({Tokens.TBranch : val})
        self.UpdateExpPath()
    
    def UpdateTokenizer(self):
        newDict = {
            "ActorName" : self.GetActorName(),
            "ActorType" : self.GetActorType()
        }
        self.tokenizer.Update(newDict)
    
    def UpdateExpPath(self):
        pth = self.GetExportPath()
        self.ui.led_ResultPath.setText(pth)
    
    def setEnabled(self, val):
        self.__enabled = val
        if (not self.__overriddenPath):
            self.ui.led_ExpPath.setEnabled(self.__enabled)
            self.ui.btn_ExpPath.setEnabled(self.__enabled)
        self.ui.led_ExpName.setEnabled(self.__enabled)
        self.ui.cbx_FileExtension.setEnabled(self.__enabled)
        self.ui.led_ResultPath.setEnabled(self.__enabled)
    
    def setPathOverride(self, overridePath):
        if (not self.__overriddenPath):
            self.__preOverriddenOriginalPath = self.ui.led_ExpPath.text()
        
        self.tokenizer.Update({SubActorExportWidget.__overridePathToken: overridePath})
        
        if (overridePath == None):
            self.ui.led_ExpPath.setEnabled(self.__enabled)
            self.ui.btn_ExpPath.setEnabled(self.__enabled)
            self.ui.led_ExpPath.setText(self.__preOverriddenOriginalPath)
            self.__preOverriddenOriginalPath = None
            self.__overriddenPath = False
        else:
            self.ui.led_ExpPath.setEnabled(False)
            self.ui.btn_ExpPath.setEnabled(False)
            self.ui.led_ExpPath.setText("{{{}}}".format(SubActorExportWidget.__overridePathToken))
            self.__overriddenPath = True
    
    def GetSubactorObj(self):
        return self.__subActorObj
    
    def IsChecked(self):
        return self.ui.ckb_SubActor.isChecked()
    
    # ******************************************************
    # *********************** EVENTS ***********************
    # ******************************************************
    def led_ExpPath_TextChanged(self, txt):
        self.UpdateExpPath()
    
    def led_ExpPath_editingFinished(self):
        newValue = self.ui.led_ExpPath.text()
        if (self.__subActorObj.modelPath != newValue):
            with UndoContext("Set Export Path"):
                self.__subActorObj.modelPath = self.ui.led_ExpPath.text()
    
    def led_ExpName_TextChanged(self, txt):
        self.UpdateExpPath()
    
    def led_ExpName_editingFinished(self):
        newValue = self.ui.led_ExpName.text()
        if (self.__subActorObj.modelName != newValue):
            with UndoContext("Set Export Name"):
                self.__subActorObj.modelName = self.ui.led_ExpName.text()
    
    def cbx_FileExtension_CurrentIndexChanged(self, idx):
        self.__subActorObj.modelFileType = (self.__fileTypes.indexOfPosition(idx))
        self.UpdateExpPath()
        if (idx == 0):
            self.ui.ckb_Ascii.setHidden(False)
        else:
            self.ui.ckb_Ascii.setHidden(True)
    
    def ckb_SubActor_StateChanged(self, arg):
        self.setEnabled(False) if (arg == 0) else self.setEnabled(True)
    
    def btn_ExpPath_Clicked(self):
        dir = os.path.dirname(self.GetExportPath())
        
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Export Folder", dir, QtWidgets.QFileDialog.ShowDirsOnly)
        if (fileName != ""):
            self.ui.led_ExpPath.setText(self.tokenizer.Tokenize(fileName))
    
    def TranslateAction_Triggered(self):
        currentText = self.currentFocusWidget.text()
        self.currentFocusWidget.setText(self.tokenizer.Translate(currentText))
    
    def TokenizeAction_Triggered(self):
        currentText = self.currentFocusWidget.text()
        self.currentFocusWidget.setText(self.tokenizer.Tokenize(currentText))
    
    def OpenPathAction_Triggered(self):
        path = self.ui.led_ResultPath.text()
        ShowFileExplorer(path)
        """path = os.path.normpath(path)
        
        if ("." in path):
            if (os.path.isfile(path)):
                print(path)
                explorer = subprocess.Popen(['explorer', '/select,', path])
                return
            else:
                path = GetFurthestExistingFolder(os.path.split(path)[0])
        
        print(path)
        subprocess.Popen(['explorer', path])"""