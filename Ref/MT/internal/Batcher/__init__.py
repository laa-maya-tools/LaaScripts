# coding: utf-8

from PySide2 import QtCore, QtWidgets, QtGui

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import QtCustomWidgets.UIFileWidget as UIFileWidget

import os
import math
import time
import logging
import traceback
import functools
import subprocess

class CancelledException(Exception):
    pass


class BatchLogHandler(logging.FileHandler):
    
    def __init__(self, batcher, logFile, **kwargs):
        self.batcher = batcher
        self.logFile = logFile

        if logFile != None:
            logging.FileHandler.__init__(self, logFile, **kwargs)
            self.close()
        else:
            logging.Handler.__init__(self, **kwargs)

        self.formatter = logging.Formatter("%(filepath)s [%(levelname)s]: %(message)s")

    def emit(self, record):
        try: 
            if self.logFile != None:
                record.filepath = str(os.path.basename(self.batcher.currentFileBeingProcessed.filePath)) if self.batcher.currentFileBeingProcessed != None else "GLOBAL"
                super(BatchLogHandler, self).emit(record)

            msg = record.getMessage()
            color = record.__dict__["color"] if "color" in record.__dict__ else None
            if record.levelno >= logging.ERROR:
                if record.exc_info != None:
                    exceptionType, exceptionValue, exceptionTraceback = record.exc_info
                    exceptionInfo = traceback.format_exception(exceptionType, exceptionValue, exceptionTraceback)
                else:
                    exceptionInfo = None
                self.batcher.logError(msg, exceptionInfo=exceptionInfo, color=color)
            elif record.levelno >= logging.WARNING:
                self.batcher.logWarning(msg, color=color)
            elif record.levelno >= logging.INFO:
                self.batcher.logInfo(msg, color=color)

        except CancelledException:
            raise

        except: 
            self.handleError(record)

    def close(self):
        if self.logFile != None:
            logging.FileHandler.close(self)
        else:
            logging.Handler.close(self)


class BatchFileItem(object):

    class BatchFileItemState(object):
        def __init__(self, text, tooltip, icon):
            self.text = text
            self.tooltip = tooltip
            self.icon = icon

    STATE_PENDING = BatchFileItemState("Pending", "The file has not been processed yet.", QtGui.QIcon())
    STATE_PROCESSING = BatchFileItemState("Processing", "The file is being processed.", QtGui.QIcon(":/waitBusy.png"))
    STATE_DONE = BatchFileItemState("Done", "The file has been processed.", QtGui.QIcon(":/confirm.png"))
    STATE_DONE_WARNINGS = BatchFileItemState("Done", "The file has been processed, but warnings have occurred.", QtGui.QIcon(":/caution.png"))
    STATE_DONE_ERRORS = BatchFileItemState("Done", "The file has been processed, but errors have occurred.", QtGui.QIcon(":/RS_WarningOldCollection.png"))
    STATE_FAILED = BatchFileItemState("Failed", "An error occurred when processing the file.", QtGui.QIcon(":/error.png"))
    STATE_CANCELLED = BatchFileItemState("Cancelled", "The process was cancelled while the file was being processed.", QtGui.QIcon(":/RS_disable.png"))
    STATE_UNKNOWN = BatchFileItemState("Unknown", "An unknown error has ocurred.\nThis might be a problem with the batcher and not with the process or the file.", QtGui.QIcon(":/help.png"))

    def __init__(self, filePath, enabled=True, state=None):
        if state == None:
            state = BatchFileItem.STATE_PENDING

        self.filePath = filePath
        self.enabled = enabled
        self.state = state

        self.messageLog = []
        self.warningLog = []
        self.errorLog = []

        self.tableWidget = None
        self.pathItemWidget = None
        self.stateItemWidget = None

    def createRow(self, tableWidget, rowIndex):
        self.tableWidget = tableWidget
        
        self.pathItemWidget = QtWidgets.QTableWidgetItem(os.path.basename(self.filePath))
        self.pathItemWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)
        self.pathItemWidget.setCheckState(QtCore.Qt.Checked if self.enabled else QtCore.Qt.Unchecked)
        self.pathItemWidget.setToolTip(self.filePath + "\n\nMark the checkbox to process this file on the batch.")
        tableWidget.setItem(rowIndex, 0, self.pathItemWidget)
        
        self.stateItemWidget = QtWidgets.QTableWidgetItem()
        self.stateItemWidget.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        tableWidget.setItem(rowIndex, 1, self.stateItemWidget)

        self.pathItemWidget.setData(QtCore.Qt.UserRole, self)

        # These calls will refresh the displayed elements of the UI
        self.setState(self.state)

    def setEnabled(self, enabled):
        self.enabled = enabled
        
        signalsBlocked = self.tableWidget.blockSignals(True)
        self.pathItemWidget.setCheckState(QtCore.Qt.Checked if self.enabled else QtCore.Qt.Unchecked)
        self.tableWidget.blockSignals(signalsBlocked)

    def setState(self, state):
        self.state = state
        
        self.stateItemWidget.setText(self.state.text)
        self.stateItemWidget.setToolTip(self.state.tooltip)
        self.stateItemWidget.setIcon(self.state.icon)

    def reset(self):
        self.enabled = True

        self.setState(BatchFileItem.STATE_PENDING)

        self.clearLog()

    def clearLog(self):
        self.messageLog = []
        self.warningLog = []
        self.errorLog = []

    def processFile(self, batcher):
        try:
            timeStamp = time.time()
            self.setState(BatchFileItem.STATE_PROCESSING)

            batcher.onPerformBatchProcess(self.filePath)

            if len(self.errorLog) > 0:
                batcher.logger.info("File processed with errors! ({:.2f} s) {}".format(time.time() - timeStamp, self.filePath), extra=BatcherUI.LOG_COLOR_ERROR)
                self.setState(BatchFileItem.STATE_DONE_ERRORS)
            elif len(self.warningLog) > 0:
                batcher.logger.info("File processed with warnings! ({:.2f} s) {}".format(time.time() - timeStamp, self.filePath), extra=BatcherUI.LOG_COLOR_WARNING)
                self.setState(BatchFileItem.STATE_DONE_WARNINGS)
            else:
                batcher.logger.info("File processed successfully! ({:.2f} s) {}".format(time.time() - timeStamp, self.filePath), extra=BatcherUI.LOG_COLOR_LIGHTGREEN)
                self.setState(BatchFileItem.STATE_DONE)

            self.setEnabled(False)

        except CancelledException:
            self.setState(BatchFileItem.STATE_CANCELLED)
            raise

        except:
            batcher.logger.exception("An error occurred while processing the file: {}".format(self.filePath))
            self.setState(BatchFileItem.STATE_FAILED)


class BatcherUI(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):

    LOG_COLOR_INFO = { "color" : "lightgray" }
    LOG_COLOR_WARNING = { "color" : "yellow" }
    LOG_COLOR_ERROR = { "color" : "#ff9999" }
    
    LOG_COLOR_WHITE = { "color" : "white" }
    LOG_COLOR_LIGHTCYAN = { "color" : "#aaddff" }
    LOG_COLOR_LIGHTGREEN = { "color" : "lightgreen" }
    LOG_COLOR_LIGHTPURPLE = { "color" : "#d080ff" }

    LOG_SEPARATOR = "═─═─═─═─═─═─═─═─═─═─═─═─"
    LOG_MESSAGE_FILE_WARNINGS_HEADER = "- Warnings in file: {}"
    LOG_MESSAGE_FILE_ERRORS_HEADER = "- Errors in file: {}"
    LOG_MESSAGE_NO_ERRORS = "No Error Messages!"
    LOG_MESSAGE_NO_WARNINGS = "No Warning Messages!"

    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
    # | Constructor                 |
    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"Batcher/Batcher.ui", parent=parent)

        self.setWindowTitle(self.onGetWindowTitle())

        # Attributes
        self.batchFiles = []

        self.currentFileBeingProcessed = None
        self.batchCancelled = False

        self.globalMessageLog = []
        self.globalWarningLog = []
        self.globalErrorLog = []

        # Logger
        logFile = self.onGetLogFilePath()
        if logFile != None:
            folder = os.path.dirname(logFile)
            if not os.path.isdir(folder):
                os.makedirs(folder)

        self.logger = logging.getLogger(self.onGetLoggerName())
        self.logger.batchLogHandler = BatchLogHandler(self, logFile)
        self.logger.handlers = [self.logger.batchLogHandler]

        # Files Table
        self.ui.filesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.filesTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        filesTableHeader = self.ui.filesTable.horizontalHeader()
        filesTableHeader.setDefaultAlignment(QtCore.Qt.AlignLeft)
        filesTableHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        filesTableHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

        self.filesTableContextMenu = QtWidgets.QMenu(self.ui.filesTable)
        self.filesTableContextMenu.addAction("Reset", self.resetSelectedBatchFileItems)
        self.filesTableContextMenu.addSeparator()
        self.filesTableContextMenu.addAction("Check", functools.partial(self.setSelectedBatchFileItemsChecked, True))
        self.filesTableContextMenu.addAction("Unheck", functools.partial(self.setSelectedBatchFileItemsChecked, False))
        self.filesTableContextMenu.addSeparator()
        self.filesTableContextMenu.addAction("Remove", self.removeSelectedBatchFileItems)

        self.ui.filesTable.customContextMenuRequested.connect(self.showFilesTableContextMenu)
        self.ui.filesTable.itemChanged.connect(self.toggleSelectedBatchFileItemsEnabled)
        self.ui.filesTable.itemSelectionChanged.connect(self.updateDisplayedLogs)

        self.ui.filesAddButton.clicked.connect(self.browseAndAddFiles)
        self.ui.filesRemoveButton.clicked.connect(self.removeSelectedBatchFileItems)

        # Log
        self.ui.openLogFileButton.clicked.connect(self.openLogFile)
        self.ui.openLogFileButton.setVisible(self.onGetLogFilePath() != None)

        # Process Buttons
        self.ui.startBatchButton.setEnabled(True)
        self.ui.cancelBatchButton.setEnabled(False)

        self.ui.startBatchButton.clicked.connect(self.startBatch)
        self.ui.cancelBatchButton.clicked.connect(self.cancelBatch)

        # Input Frame
        inputUIFile = self.onGetInputUIFilePath()
        if inputUIFile != None:
            self.inputUI = UIFileWidget.loadUIWidget(inputUIFile, self)
            self.ui.inputFrame.layout().addWidget(self.inputUI)
            self.onInitializeUI(self.inputUI)
        else:
            self.ui.inputFrame.setVisible(False)

    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
    # | Override Functions          |
    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

    # Returns the TITLE the window will have.
    def onGetWindowTitle(self):
        # By default, this method returns a plaeholder name.
        return "Batcher"

    # Returns the NAME OF THE LOGGER this batcher will use.
    # This name will be used so the batcher uses the same logger as the modules it calls.
    def onGetLoggerName(self):
        # By default, this method returns an unique name for this batcher.
        # It is recommended that this funcion returns the name of the main module the batcher calls.
        # For instance, if the batcher uses the module ExporterWindow, this function should return "ExporterWindow".
        # Then, the ExporterWindow's submodules should use logging.getLogger(__name__). This way, every logging call will notify the batcher.
        return "{}".format(self.__class__.__module__)

    # Returns the path to this batcher's LOG FILE.
    # Return NONE if you don't want to use a log file.
    def onGetLogFilePath(self):
        # By default, if this code is called from the ScriptEditor (and thus has no file associated), skips using a log file.
        if self.__class__.__module__ == "__main__":
            return None

        # By default, this method returns a path to a log file with the same name and path as the batcher's.
        import inspect
        classPath = inspect.getfile(self.__class__)
        pre, ext = os.path.splitext(classPath)
        return pre + ".log"

    # Returns a path to the CUSTOM UI FILE for this batcher.
    # The UI created by this file will be added on top of the batcher's window.
    # It's main widget should be a QWidget without any borders or frame.
    # Return NONE if you don't want to use any custom UI.
    def onGetInputUIFilePath(self):
        # By defualt, this method returns None so no custom UI is used.
        return None

    # Returns the DEFAULT PATH TO BROWSE FILES TO PROCESS on the batch.
    # Return None if you don't want any specifc default path.
    def onGetDefaultSourceFolderPath(self):
        # By default, this method returns None so no default path is used.
        return None

    # This method is used to INITIALIZE THE CUSTOM UI.
    # Use it to configure and add events to the custom UI.
    def onInitializeUI(self, inputUI):
        # By default, this method doesn't need to do anything.
        pass

    # This method is used to get the SUPPORTED FILE EXTENSIONS for thebatch to process.
    # Returns an array with each supported type (the format must be like the example below).
    def onGetFileFilters(self):
        # By default, this method returns only one type: Maya Scenes, for both the mb and ma extensions.
        # Note that the name of the type ("Maya Scene Files" in this case) can be whatever you want, the important part are the supported extensions ("*.mb *.ma").
        return ["Maya Scene Files (*.mb *.ma)"]

    # This method is EXECUTED BEFORE THE BATCH PROCESS starts.
    # Use it to initialice data or to check if the input is correctly set.
    # This method must return wheter or not the process should continue or not (True if everything is ok, False ese).
    # This method can also raise an exception. The batcher will capture and log it and then abort the process.
    def onBeforeProcess(self):
        # By default, this method returns True becouse there are no things to be done or checked.
        return True

    # This method is EXECUTED AFTER THE BATCH PROCESS ends.
    # Use it to restore data.
    # This method can also raise an exception. The batcher will capture and log it.
    def onAfterProcess(self):
        # By default, this method does nothing.
        pass

    # Main function for the batch process, PERFORMS THE ACTUAL OPERATIONS on each fle.
    # This function will be called for EVERY FILE being processed. Use self.logger to log messages during the process.
    # DO NOT ATTEMPT TO CAPTURE EXCEPTIONS HERE (unless they are intended), the batcher will automatically capture and log them.
    # If you want to produce an error, raise an Exception. The batcher will log it and continue to the next file.
    def onPerformBatchProcess(self, filePath):
        # This function MUST BE OVERRRIDEN by every batcher subclass.
        raise NotImplementedError("You must define the batch process.")

    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
    # | Files Table Methods         |
    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

    def addFiles(self, files, quiet=True):
        filesToAdd = []
        duplicatedFiles = []
        for f in files:
            if (f in filesToAdd) or (self.getBatchFileItemFromFilePath(f) != None):
                duplicatedFiles.append(f)
            else:
                filesToAdd.append(BatchFileItem(f))

        if not quiet and len(duplicatedFiles) > 0:
            result = QtWidgets.QMessageBox.warning(self, "Add Files", "Some of the files being added are already on the list. Do you want to reset them?\n\n{}".format("\n".join(duplicatedFiles)), buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Cancel:
                return
            elif result == QtWidgets.QMessageBox.Yes:
                self.removeFiles(duplicatedFiles)
                filesToAdd.extend([BatchFileItem(f) for f in duplicatedFiles])

        self.batchFiles.extend(filesToAdd)
        self.refreshFilesTable()

    def removeFiles(self, files, quiet=True):
        filesToRemove = []
        missingFiles = []
        for f in files:
            batchFileItem = f if type(f) == BatchFileItem else self.getBatchFileItemFromFilePath(f)
            if batchFileItem != None:
                if batchFileItem in self.batchFiles:
                    filesToRemove.append(batchFileItem)
                else:
                    missingFiles.append(f.filePath)
            else:
                missingFiles.append(f)

        if not quiet and len(missingFiles) > 0:
            result = QtWidgets.QMessageBox.warning(self, "Remove Files", "Some of the files being removed are not on the list, proceed?\n\n{}".format("\n".join(missingFiles)), buttons=QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Cancel:
                return

        for f in filesToRemove:
            self.batchFiles.remove(f)
        self.refreshFilesTable()

    def getBatchFileItemFromFilePath(self, filePath):
        for f in self.batchFiles:
            if os.path.normpath(f.filePath).lower() == os.path.normpath(filePath).lower():
                return f
        return None

    def getSelectedBatchFileItems(self, sortByIndex=True):
        selectedRows = self.ui.filesTable.selectionModel().selectedRows()
        selectedRows = [index.row() for index in selectedRows]
        if sortByIndex:
            selectedRows.sort()
        return [self.ui.filesTable.item(row, 0).data(QtCore.Qt.UserRole) for row in selectedRows]

    def selectBatchFileItems(self, batchFileItems):
        self.ui.filesTable.clearSelection()
        for i in range(self.ui.filesTable.rowCount()):
            item = self.ui.filesTable.item(i, 0)
            if item.data(QtCore.Qt.UserRole) in batchFileItems:
                for j in range(self.ui.filesTable.columnCount()):
                    self.ui.filesTable.item(i, j).setSelected(True)

    def refreshFilesTable(self):
        signalsBlocked = self.ui.filesTable.blockSignals(True)

        self.ui.filesTable.setRowCount(len(self.batchFiles))
        for i, f in enumerate(self.batchFiles):
            f.createRow(self.ui.filesTable, i)

        self.ui.filesTable.blockSignals(signalsBlocked)

    def browseAndAddFiles(self):
        files, selectedFilter = QtWidgets.QFileDialog.getOpenFileNames(self, caption="Select Files to apply the batch to", filter=";;".join(self.onGetFileFilters()), dir=self.onGetDefaultSourceFolderPath())
        if len(files) > 0:
            self.addFiles(files, quiet=False)

    def removeSelectedBatchFileItems(self):
        selectedItems = self.getSelectedBatchFileItems()
        self.removeFiles(selectedItems, quiet=False)

    def resetSelectedBatchFileItems(self):
        selectedItems = self.getSelectedBatchFileItems()
        for item in selectedItems:
            item.reset()

    def setSelectedBatchFileItemsChecked(self, checked):
        signalsBlocked = self.ui.filesTable.blockSignals(True)

        selectedItems = self.getSelectedBatchFileItems()
        for item in selectedItems:
            item.setEnabled(checked)

        self.ui.filesTable.blockSignals(signalsBlocked)

    def showFilesTableContextMenu(self, pos):
        selectedItem = self.ui.filesTable.itemAt(pos)
        if selectedItem is not None:
            self.filesTableContextMenu.exec_(QtGui.QCursor.pos())

    def toggleSelectedBatchFileItemsEnabled(self, changedItem):
        if changedItem.column() == 0:
            signalsBlocked = self.ui.filesTable.blockSignals(True)

            checked = changedItem.checkState() == QtCore.Qt.Checked
            selectedItems = self.getSelectedBatchFileItems()
            if changedItem.isSelected() and len(selectedItems) > 1:
                toggleAlreadyProcessed = None
                for item in selectedItems:
                    if item.state == BatchFileItem.STATE_DONE and checked == True:
                        if toggleAlreadyProcessed == None:
                            result = QtWidgets.QMessageBox.warning(self.ui.filesTable, "Toggle Enabled", "Some of the files you are about to toggle have already being processed. Do you want to reset them?", buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
                            if result == QtWidgets.QMessageBox.Cancel:
                                break
                            else:
                                toggleAlreadyProcessed = result == QtWidgets.QMessageBox.Yes
                        if toggleAlreadyProcessed:
                            item.reset()
                        else:
                            continue
                    item.setEnabled(checked)
                QtCore.QTimer.singleShot(0, functools.partial(self.selectBatchFileItems, selectedItems))
            else:
                item = changedItem.data(QtCore.Qt.UserRole)
                if item.state == BatchFileItem.STATE_DONE and checked == True:
                    result = QtWidgets.QMessageBox.warning(self.ui.filesTable, "Toggle Enabled", "The file you are about to toggle has already being processed. Do you want to reset it?", buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    if result == QtWidgets.QMessageBox.Yes:
                        item.reset()
                        item.setEnabled(checked)
                else:
                    item.setEnabled(checked)
                QtCore.QTimer.singleShot(0, functools.partial(self.selectBatchFileItems, [item]))

            self.ui.filesTable.blockSignals(signalsBlocked)

    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
    # | Log Methods                 |
    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

    def logInfo(self, string, exceptionInfo=None, color=None):
        if color == None:
            color = BatcherUI.LOG_COLOR_INFO

        self.globalMessageLog.append((string, exceptionInfo, color))
        if self.currentFileBeingProcessed != None:
            self.currentFileBeingProcessed.messageLog.append((string, exceptionInfo, color))

        self.printToMessageLog(string, color)
        if exceptionInfo != None:
            self.printToMessageLog(exceptionInfo[-1], BatcherUI.LOG_COLOR_ERROR)    # On the message log we will only show the Exception name

    def logWarning(self, string, exceptionInfo=None, color=None, logMessageAsWell=True):
        if color == None:
            color = BatcherUI.LOG_COLOR_WARNING

        if self.currentFileBeingProcessed != None:
            if len(self.currentFileBeingProcessed.warningLog) == 0:
                warningHeaderTuple = (BatcherUI.LOG_MESSAGE_FILE_WARNINGS_HEADER.format(self.currentFileBeingProcessed.filePath), None, BatcherUI.LOG_COLOR_WHITE)
                separatorTuple = (BatcherUI.LOG_SEPARATOR, None, BatcherUI.LOG_COLOR_WARNING)

                self.globalWarningLog.append(separatorTuple)
                self.currentFileBeingProcessed.warningLog.append(separatorTuple)
                self.printToWarningLog(separatorTuple[0], separatorTuple[2])

                self.globalWarningLog.append(warningHeaderTuple)
                self.currentFileBeingProcessed.warningLog.append(warningHeaderTuple)
                self.printToWarningLog(warningHeaderTuple[0], warningHeaderTuple[2])

            self.currentFileBeingProcessed.warningLog.append((string, exceptionInfo, color))
        self.globalWarningLog.append((string, exceptionInfo, color))

        self.printToWarningLog(string, color)
        if exceptionInfo != None:
            self.printToWarningLog("".join(exceptionInfo), BatcherUI.LOG_COLOR_ERROR)

        if logMessageAsWell:
            self.logInfo(string, exceptionInfo=exceptionInfo, color=color)

    def logError(self, string, exceptionInfo=None, color=None, logMessageAsWell=True):
        if color == None:
            color = BatcherUI.LOG_COLOR_ERROR

        if self.currentFileBeingProcessed != None:
            if len(self.currentFileBeingProcessed.errorLog) == 0:
                errorHeaderTuple = (BatcherUI.LOG_MESSAGE_FILE_ERRORS_HEADER.format(self.currentFileBeingProcessed.filePath), None, BatcherUI.LOG_COLOR_WHITE)
                separatorTuple = (BatcherUI.LOG_SEPARATOR, None, BatcherUI.LOG_COLOR_ERROR)

                self.globalErrorLog.append(separatorTuple)
                self.currentFileBeingProcessed.errorLog.append(separatorTuple)
                self.printToErrorLog(separatorTuple[0], separatorTuple[2])

                self.globalErrorLog.append(errorHeaderTuple)
                self.currentFileBeingProcessed.errorLog.append(errorHeaderTuple)
                self.printToErrorLog(errorHeaderTuple[0], errorHeaderTuple[2])

            self.currentFileBeingProcessed.errorLog.append((string, exceptionInfo, color))
        self.globalErrorLog.append((string, exceptionInfo, color))

        self.printToErrorLog(string, color)
        if exceptionInfo != None:
            self.printToErrorLog("".join(exceptionInfo), BatcherUI.LOG_COLOR_ERROR)

        if logMessageAsWell:
            self.logInfo(string, exceptionInfo=exceptionInfo, color=color)

    def printToMessageLog(self, string, color=None):
        if color == None:
            color = BatcherUI.LOG_COLOR_INFO
        self.printToLog(self.ui.logAllText, string, color)

    def printToWarningLog(self, string, color=None):
        if color == None:
            color = BatcherUI.LOG_COLOR_WARNING
        self.printToLog(self.ui.logWarningsText, string, color)

    def printToErrorLog(self, string, color=None):
        if color == None:
            color = BatcherUI.LOG_COLOR_ERROR
        self.printToLog(self.ui.logErrorsText, string, color)

    def printToLog(self, logWidget, string, color):
        if type(color) == dict:
            color = color["color"]
        html = "<pre style=\"color: {}; margin: 0\">{}</pre>".format(color, string)
        logWidget.moveCursor(QtGui.QTextCursor.End)
        logWidget.insertHtml(html)
        logWidget.insertPlainText("\n")
        logWidget.moveCursor(QtGui.QTextCursor.End)

        wasBatchCancelled = self.batchCancelled
        QtCore.QCoreApplication.processEvents()
        if self.batchCancelled and not wasBatchCancelled and self.currentFileBeingProcessed != None:
            raise CancelledException()

    def updateDisplayedLogs(self):
        self.ui.logAllText.clear()
        self.ui.logWarningsText.clear()
        self.ui.logErrorsText.clear()

        messageLogs = {}
        warningLogs = {}
        errorLogs = {}
        selectedItems = self.getSelectedBatchFileItems()
        if len(selectedItems) == 0:
            messageLogs[None] = self.globalMessageLog
            warningLogs[None] = self.globalWarningLog
            errorLogs[None] = self.globalErrorLog
        else:
            for item in selectedItems:
                if len(item.messageLog) > 0:
                    messageLogs[item] = item.messageLog
                if len(item.warningLog) > 0:
                    warningLogs[item] = item.warningLog
                if len(item.errorLog) > 0:
                    errorLogs[item] = item.errorLog

        for item, log in messageLogs.items():
            for message, exceptionInfo, color in log:
                self.printToLog(self.ui.logAllText, message, color)
                if exceptionInfo != None:
                    self.printToLog(self.ui.logAllText, exceptionInfo[-1], BatcherUI.LOG_COLOR_ERROR)

        if len(warningLogs) == 0:
            self.printToWarningLog(BatcherUI.LOG_MESSAGE_NO_WARNINGS, BatcherUI.LOG_COLOR_LIGHTGREEN)
        else:
            for item, log in warningLogs.items():
                for message, exceptionInfo, color in log:
                    self.printToLog(self.ui.logWarningsText, message, color)
                    if exceptionInfo != None:
                        self.printToLog(self.ui.logWarningsText, "".join(exceptionInfo), BatcherUI.LOG_COLOR_ERROR)

        if len(errorLogs) == 0:
            self.printToErrorLog(BatcherUI.LOG_MESSAGE_NO_ERRORS, BatcherUI.LOG_COLOR_LIGHTGREEN)
        else:
            for item, log in errorLogs.items():
                for message, exceptionInfo, color in log:
                    self.printToLog(self.ui.logErrorsText, message, color)
                    if exceptionInfo != None:
                        self.printToLog(self.ui.logErrorsText, "".join(exceptionInfo), BatcherUI.LOG_COLOR_ERROR)

    def clearGlobalLog(self, quiet=False):
        result = quiet or QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self, "Clear Global Log", "Are you sure you want to clear the global log?\n\nNote: The individual log for each file will be presserved.")
        if result:
            self.globalMessageLog = []
            self.globalWarningLog = []
            self.globalErrorLog = []
            self.updateDisplayedLogs()

    def closeLoggerFile(self):
        self.logger.batchLogHandler.close()

    def openLogFile(self):
        subprocess.Popen("explorer /select,\"{}\"".format(self.onGetLogFilePath()))

    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
    # | Batch Process Methods       |
    # =-=-=-=-=-=-=-=-=-=-=-=--=-=-=-

    def startBatch(self):
        self.ui.startBatchButton.setEnabled(False)
        self.ui.cancelBatchButton.setEnabled(True)
        self.ui.filesTable.setEnabled(False)
        self.ui.filesTable.clearSelection()

        try:
            self.clearGlobalLog(quiet=True)

            self.logger.info(BatcherUI.LOG_SEPARATOR, extra=BatcherUI.LOG_COLOR_LIGHTCYAN)
            self.logger.info("Batch Process Start", extra=BatcherUI.LOG_COLOR_LIGHTCYAN)
            self.logger.info(BatcherUI.LOG_SEPARATOR, extra=BatcherUI.LOG_COLOR_LIGHTCYAN)

            enabledItems = [item for item in self.batchFiles if item.enabled]
            timeStamp = time.time()
            self.batchCancelled = False

            try:
                self.logger.info("Running batch preparations...", extra=BatcherUI.LOG_COLOR_WHITE)
                prepareCorrect = self.onBeforeProcess()
                if not prepareCorrect:
                    self.logger.error("Batch preparation was unsuccessfull! Batch aborted.")
                    self.batchCancelled = True
            except:
                self.logger.exception("An Error ocurred while preparing the batch process!")
                self.batchCancelled = True
            finally:
                self.logger.info(BatcherUI.LOG_SEPARATOR, extra=BatcherUI.LOG_COLOR_WHITE)

            filesWithProblems = []
            for i, batchFileItem in enumerate(enabledItems):
                QtCore.QCoreApplication.processEvents()
                if self.batchCancelled:
                    break

                try:
                    self.currentFileBeingProcessed = batchFileItem
                    batchFileItem.clearLog()
                    
                    self.logger.info("[{1}/{2}] Processing file... {0}".format(batchFileItem.filePath, str(i+1).zfill(int(math.floor(math.log10(len(enabledItems)))) + 1), len(enabledItems)), extra=BatcherUI.LOG_COLOR_WHITE)
                    
                    self.ui.filesTable.scrollTo(self.ui.filesTable.model().index(self.batchFiles.index(batchFileItem), 0))
                    batchFileItem.processFile(self)

                    if len(batchFileItem.errorLog) > 0:
                        filesWithProblems.append(batchFileItem)

                except CancelledException:
                    break
                
                except:
                    self.logger.exception("Unexpected Exception when processing file: {}".format(batchFileItem.filePath))
                    batchFileItem.setState(BatchFileItem.STATE_UNKNOWN)
                    filesWithProblems.append(batchFileItem)

                finally:
                    self.logger.info(BatcherUI.LOG_SEPARATOR, extra=BatcherUI.LOG_COLOR_WHITE)
                    self.currentFileBeingProcessed = None

            try:
                self.logger.info("Finishing batch process...", extra=BatcherUI.LOG_COLOR_WHITE)
                self.onAfterProcess()
            except:
                self.logger.exception("An Error ocurred while finishing the batch process!")
            finally:
                self.logger.info(BatcherUI.LOG_SEPARATOR, extra=BatcherUI.LOG_COLOR_WHITE)

            if len(filesWithProblems) == 0:
                self.logger.info("Batch Process {}! ({:.2f} s)".format("Finished Successfully" if not self.batchCancelled else "Cancelled", time.time() - timeStamp), extra=BatcherUI.LOG_COLOR_LIGHTGREEN if not self.batchCancelled else BatcherUI.LOG_COLOR_LIGHTPURPLE)
            else:
                self.logger.info("Batch Process {} with Errors! ({:.2f} s)".format("Finished" if not self.batchCancelled else "Cancelled", time.time() - timeStamp), extra=BatcherUI.LOG_COLOR_ERROR)
                for batchFileItem in filesWithProblems:
                    for error, exceptionInfo, color in batchFileItem.errorLog:
                        self.logger.info(error, extra=color)
                        if exceptionInfo != None:
                            self.logger.info("".join(exceptionInfo), extra=BatcherUI.LOG_COLOR_ERROR)

            if len(self.globalWarningLog) == 0:
                self.printToWarningLog(BatcherUI.LOG_MESSAGE_NO_WARNINGS, BatcherUI.LOG_COLOR_LIGHTGREEN)
            if len(self.globalErrorLog) == 0:
                self.printToErrorLog(BatcherUI.LOG_MESSAGE_NO_ERRORS, BatcherUI.LOG_COLOR_LIGHTGREEN)
                
        except:
            self.logger.exception("The batcher produced an Unexpected Exception!")

        finally:
            self.closeLoggerFile()
            
            self.batchCancelled = False

            self.ui.startBatchButton.setEnabled(True)
            self.ui.cancelBatchButton.setEnabled(False)
            self.ui.filesTable.setEnabled(True)

    def cancelBatch(self):
        if not self.batchCancelled:
            result = QtWidgets.QMessageBox.question(self, "Stop Batch", "Are you sure you want to stop the batch? You won't need to run the batch again for the already processed files.")
            if result == QtWidgets.QMessageBox.Yes:
                self.batchCancelled = True
 

if __name__ == "__main__":
    batcherUI = BatcherUI()
    batcherUI.show()