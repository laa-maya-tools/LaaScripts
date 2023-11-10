import QtCustomWidgets.UIFileWidget as UIFileWidget

class ExporterWindowTab(UIFileWidget.UIFileWidget):

    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------

    def __init__(self, uiFilePath, exporterWindow):
        UIFileWidget.UIFileWidget.__init__(self, uiFilePath, parent=exporterWindow)
        self.exporterWindow = exporterWindow

    # ------------------------------------
    # | Override Methods                 |
    # ------------------------------------
    
    def isRelevant(self):
        return True

    def refreshTab(self):
        pass

    def getTabName(self):
        return ""

    def onExportRootChanged(self, exportRoot):
        pass

    def loadUIConfiguration(self):
        pass

    def saveUIConfiguration(self):
        pass

    def resizeEvent(self, event):
        pass
    
    def onUndo(self):
        pass