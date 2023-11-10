from PySide2 import QtGui, QtWidgets, QtCore

import QtCustomWidgets.UIFileWidget as UIFileWidget
import ProjectPath

import ExporterWindow.AnimationTab as AnimationTab

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import maya.cmds as cmds

import os

class UIConfigurationOptions():
    WINDOW_GEOMETRY         = "EXPORT_UI_WINDOW_GEOMETRY"
    EXPORT_DIR_PATHS        = "EXPORT_UI_EXPORT_DIR_PATHS"
    EXPORT_DIR_INDEX        = "EXPORT_UI_EXPORT_DIR_INDEX"
    ACTIVE_TAB_INDEX        = "EXPORT_UI_ACTIVE_TAB_INDEX"
    LOG_DIVIDER_POSITION    = "EXPORT_UI_LOG_DIVIDER_POSITION"


class ExporterWindow(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    
    # ------------------------------------
    # | Constructor                      |
    # ------------------------------------

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ExporterWindow/ui/ExporterWindow.ui", parent=parent)

        # Window Configuration
        self.setWindowTitle("NX Exporter")
        self.setWindowIcon(QtGui.QIcon(os.path.join(ProjectPath.getIconsFolder(), r"ExporterWindow\ExporterIcon.png")))

        # Creates the different tabs
        self.animationTab = AnimationTab.AnimationTab(self)
        self.tabs = [self.animationTab]

        for tab in self.tabs:
            self.ui.Tab_Exporter.addTab(tab, tab.getTabName())

        # Callbacks
        self.fileNewScriptJob = None
        self.fileOpenScriptJob = None
        self.undoScriptJob = None
        self.redoScriptJob = None
        self.timeUnitChangedScriptJob = None

        # Attributes
        self.exporting = False
        self.exportCancelled = False

        # Signals
        self.ui.Tab_Exporter.currentChanged.connect(self.refreshTabByIndex)
        self.ui.CBx_ExportRoot.currentTextChanged.connect(self.onExportRootChanged)
        self.ui.Btn_AddExportRoot.released.connect(self.browseExportRoot)
        self.ui.Btn_RemoveExportRoot.released.connect(self.removeCurrentExportRoot)
        self.ui.Btn_ClearExportRoots.released.connect(self.clearExportRoots)
        self.ui.Spt_LogSplitter.splitterMoved.connect(self.resizeEvent)
        self.ui.Btn_CancelExport.released.connect(self.cancelExport)
        self.ui.Btn_ClearLog.released.connect(self.clearLog)

    def registerCallbacks(self):
        self.quitApplicationScriptJob = cmds.scriptJob(e=["quitApplication", self.close])
        self.fileNewScriptJob = cmds.scriptJob(e=["PreFileNew", self.close])
        self.fileOpenScriptJob = cmds.scriptJob(e=["SceneOpened", self.onSceneOpened])
        self.undoScriptJob = cmds.scriptJob(e=["Undo", self.onUndo])
        self.redoScriptJob = cmds.scriptJob(e=["Redo", self.onUndo])
        self.timeUnitChangedScriptJob = cmds.scriptJob(e=["timeUnitChanged", self.onTimeUnitChanged])

    def deregisterCallbacks(self):
        cmds.scriptJob(k=self.quitApplicationScriptJob)
        cmds.scriptJob(k=self.fileNewScriptJob)
        cmds.scriptJob(k=self.fileOpenScriptJob)
        cmds.scriptJob(k=self.undoScriptJob)
        cmds.scriptJob(k=self.redoScriptJob)
        cmds.scriptJob(k=self.timeUnitChangedScriptJob)

    def loadUIConfiguration(self):
        if cmds.optionVar(exists=UIConfigurationOptions.WINDOW_GEOMETRY):
            geometry = cmds.optionVar(q=UIConfigurationOptions.WINDOW_GEOMETRY)
            if type(geometry) == list:
                self.move(int(geometry[0]), int(geometry[1]))
                self.resize(int(geometry[2]), int(geometry[3]))
                
                if not QtGui.QGuiApplication.instance().desktop().geometry().intersects(self.geometry()):
                    self.move(0, 0)

        if cmds.optionVar(exists=UIConfigurationOptions.EXPORT_DIR_PATHS):
            paths = cmds.optionVar(q=UIConfigurationOptions.EXPORT_DIR_PATHS)
            if type(paths) == list:
                self.setExportRoots(paths)

        if cmds.optionVar(exists=UIConfigurationOptions.EXPORT_DIR_INDEX):
            self.ui.CBx_ExportRoot.setCurrentIndex(cmds.optionVar(q=UIConfigurationOptions.EXPORT_DIR_INDEX))

        if cmds.optionVar(exists=UIConfigurationOptions.ACTIVE_TAB_INDEX):
            self.ui.Tab_Exporter.setCurrentIndex(cmds.optionVar(q=UIConfigurationOptions.ACTIVE_TAB_INDEX))

        if cmds.optionVar(exists=UIConfigurationOptions.LOG_DIVIDER_POSITION):
            sizes = cmds.optionVar(q=UIConfigurationOptions.LOG_DIVIDER_POSITION)
            if type(sizes) == list:
                self.ui.Spt_LogSplitter.setSizes(sizes)

        for tab in self.tabs:
            tab.loadUIConfiguration()

    def saveUIConfiguration(self):
        cmds.optionVar(ca=UIConfigurationOptions.WINDOW_GEOMETRY)
        cmds.optionVar(iva=(UIConfigurationOptions.WINDOW_GEOMETRY, self.x()))
        cmds.optionVar(iva=(UIConfigurationOptions.WINDOW_GEOMETRY, self.y()))
        cmds.optionVar(iva=(UIConfigurationOptions.WINDOW_GEOMETRY, self.width()))
        cmds.optionVar(iva=(UIConfigurationOptions.WINDOW_GEOMETRY, self.height()))

        cmds.optionVar(ca=UIConfigurationOptions.EXPORT_DIR_PATHS)
        for customExportRoot in self.getExportRoots(customOnly=True):
            cmds.optionVar(sva=(UIConfigurationOptions.EXPORT_DIR_PATHS, customExportRoot))
        
        cmds.optionVar(iv=(UIConfigurationOptions.EXPORT_DIR_INDEX, self.ui.CBx_ExportRoot.currentIndex()))
        
        cmds.optionVar(iv=(UIConfigurationOptions.ACTIVE_TAB_INDEX, self.ui.Tab_Exporter.currentIndex()))
        
        cmds.optionVar(ca=UIConfigurationOptions.LOG_DIVIDER_POSITION)
        for size in self.ui.Spt_LogSplitter.sizes():
            cmds.optionVar(iva=(UIConfigurationOptions.LOG_DIVIDER_POSITION, size))
        
        for tab in self.tabs:
            tab.saveUIConfiguration()

    def onSceneOpened(self):
        currentTab = self.getCurrentTab()
        
        relevantTab = None
        if currentTab.isRelevant():
            relevantTab = currentTab
        else:
            for tab in self.tabs:
                if tab.isRelevant():
                    relevantTab = tab
                    break
                
        if relevantTab != None:
            self.setCurrentTab(relevantTab)
            relevantTab.refreshTab()
        else:
            self.close()
            
    def onTimeUnitChanged(self):
        self.refreshCurrentTab()
    
    def onUndo(self):
        self.getCurrentTab().onUndo()

    # ------------------------------------
    # | Generic Methods                  |
    # ------------------------------------

    def getPathTokenizer(self, pathTokenizer=None):
        if not pathTokenizer:
            pathTokenizer = ProjectPath.PathTokenizer()
        pathTokenizer.Update({ ProjectPath.Tokens.TPrjBranch : self.getSelectedExportRoot() })
        return pathTokenizer

    def tokenizeExportRoot(self, path):
        exportRoots = self.getExportRoots()
        for exportRoot in exportRoots:
            exportRoot = exportRoot.lower()
            if path.startswith(exportRoot):
                return path.replace(exportRoot, "{{{}}}".format(ProjectPath.Tokens.TPrjBranch))
        return path # No matching export root, returns the path without changes

    # ------------------------------------
    # | Tab Methods                      |
    # ------------------------------------

    def refreshTabByIndex(self, tabIndex):
        self.getTabByIndex(tabIndex).refreshTab()

    def refreshCurrentTab(self):
        self.refreshTabByIndex(self.ui.Tab_Exporter.currentIndex())

    def getTabByIndex(self, tabIndex):
        return self.tabs[tabIndex]

    def getCurrentTab(self):
        return self.getTabByIndex(self.ui.Tab_Exporter.currentIndex())
    
    def setCurrentTab(self, tab):
        self.ui.Tab_Exporter.setCurrentIndex(self.tabs.index(tab))

    # ------------------------------------
    # | Export Methods                   |
    # ------------------------------------

    def startExport(self, expandLog=True):
        self.ui.Btn_CancelExport.setEnabled(True)
        self.ui.Btn_ClearLog.setEnabled(False)

        self.exporting = True
        self.exportCancelled = False

        if expandLog:
            self.setExportLogExpanded(True)

    def endExport(self, contractLog=True):
        self.ui.Btn_CancelExport.setEnabled(False)
        self.ui.Btn_ClearLog.setEnabled(True)

        self.exporting = False
        self.exportCancelled = False
        
        if contractLog:
            QtCore.QCoreApplication.processEvents() # We need to process the event before minimizing the log becouse some mouse clicks can be passed to the hidden tab instead of the log
            self.setExportLogExpanded(False)

    def cancelExport(self, ask=True):
        if self.isExporting():
            if not ask or QtWidgets.QMessageBox.question(self, "Cancel Export", "Are you sure you want to cancel the current export?") == QtWidgets.QMessageBox.StandardButton.Yes:
                self.exportCancelled = True

    def isExporting(self):
        return self.exporting

    def isExportCancelled(self):
        return self.exportCancelled

    # ------------------------------------
    # | Export Root Methods              |
    # ------------------------------------

    def setExportRoots(self, customExportRoots):
        currentExportRoot = self.getSelectedExportRoot()

        self.ui.CBx_ExportRoot.clear()
        self.addExportRoot(ProjectPath.getGameFolder())
        self.ui.CBx_ExportRoot.setCurrentIndex(0)

        for customExportRoot in customExportRoots:
            self.addExportRoot(customExportRoot)
            if customExportRoot == currentExportRoot:
                self.ui.CBx_ExportRoot.setCurrentIndex(self.ui.CBx_ExportRoot.count() - 1)

    def browseExportRoot(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Browse Export Root", dir=ProjectPath.getGameFolder())
        if path != None and path != "":
            path = path.replace(os.altsep, os.sep)
            if path not in self.getExportRoots():
                self.addExportRoot(path)
            self.ui.CBx_ExportRoot.setCurrentText(path)

    def addExportRoot(self, customExportRoot):
        self.ui.CBx_ExportRoot.addItem(customExportRoot)

    def removeCurrentExportRoot(self):
        currentIndex = self.ui.CBx_ExportRoot.currentIndex()
        if currentIndex > 0:
            self.ui.CBx_ExportRoot.removeItem(currentIndex)

    def clearExportRoots(self, ask=True):
        if not ask or QtWidgets.QMessageBox.question(self, "Clear Export Roots", "Are you sure you want to clear the export roots?") == QtWidgets.QMessageBox.StandardButton.Yes:
            self.setExportRoots([])

    def getExportRoots(self, customOnly=False):
        return [self.ui.CBx_ExportRoot.itemText(i) for i in range(1 if customOnly else 0, self.ui.CBx_ExportRoot.count())]   # Starts at 1 because the first one is the default path.

    def getSelectedExportRoot(self):
        return self.ui.CBx_ExportRoot.currentText()

    def onExportRootChanged(self, exportRoot):
        self.getCurrentTab().onExportRootChanged(exportRoot)

    # ------------------------------------
    # | Log Methods                      |
    # ------------------------------------

    def writePreformatedTextToLog(self, preformatedText, newLine=True, color="white", bold=False):
        if bold:
            preformatedText = "<b style=\"margin: 0\">{}</b>".format(preformatedText)
        html = "<pre style=\"color: {}; margin: 0\">{}</pre>".format(color, preformatedText)
        self.writeHtmlTextToLog(html, newLine=newLine)

    def writeHtmlTextToLog(self, html, newLine=True):
        self.ui.Txt_LogBox.moveCursor(QtGui.QTextCursor.End)
        self.ui.Txt_LogBox.insertHtml(html)
        if newLine:
            self.ui.Txt_LogBox.insertPlainText("\n")
        self.ui.Txt_LogBox.moveCursor(QtGui.QTextCursor.End)

    def clearLog(self, ask=True):
        if not ask or QtWidgets.QMessageBox.question(self, "Clear Log", "Are you sure you want to clear the log?") == QtWidgets.QMessageBox.StandardButton.Yes:
            self.ui.Txt_LogBox.setText("")

    def getLog(self):
        return self.ui.Txt_LogBox.text()

    def setExportLogExpanded(self, expanded, scrollToEnd=True):
        self.ui.Tab_Exporter.setVisible(not expanded)
        self.ui.Frm_Common.setVisible(not expanded)
        if scrollToEnd:
            scrollBar = self.ui.Txt_LogBox.verticalScrollBar()
            scrollBar.setValue(scrollBar.maximum())

    # ------------------------------------
    # | Widget Events                    |
    # ------------------------------------

    def showEvent(self, event):
        # Callbacks
        self.registerCallbacks()

        # Initialices the export root list. This will be needed if there is no custom export roots to load.
        self.setExportRoots([])

        # Store defaults
        defaultTabIndex = self.ui.Tab_Exporter.currentIndex()
        defaultLayerPanelVisibility = self.animationTab.isLayerPanelVisible()

        # Load UI configuration
        self.loadUIConfiguration()

        # The initialization will automatically call events to refresh itself when we load the UI configuration.
        # However, it will not be called if there is no configuration to load or if the values loaded are the same as the default ones.
        # In both cases, the values will remain the default ones, so refresh manually in those cases.
        if self.ui.Tab_Exporter.currentIndex() == defaultTabIndex:
            self.refreshTabByIndex(defaultTabIndex)
        if self.animationTab.isLayerPanelVisible() == defaultLayerPanelVisibility:
            self.animationTab.showLayerPanel(defaultLayerPanelVisibility)

    def closeEvent(self, event):
        if self.isExporting():
            # If there is an exportation in progress, asks to cancel it instead of closing the window
            self.cancelExport()
            event.ignore()
        else:
            # Callbacks
            cmds.evalDeferred(self.deregisterCallbacks)

            # Saves UI configuration
            self.saveUIConfiguration()

    def resizeEvent(self, event):
        self.getCurrentTab().resizeEvent(event)
    
instance = None    

def show():
    global instance
    if isVisible():
        instance.close()
        
    instance = ExporterWindow()
    instance.show()
    
def isVisible():
    global instance
    return instance != None and instance.isVisible()

if __name__ == '__main__':
    show()