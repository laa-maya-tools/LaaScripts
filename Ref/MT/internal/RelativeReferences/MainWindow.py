import RelativeReferences.lib.Utils as Utils
import functools

import QtCustomWidgets.UIFileWidget  as UIFileWidget
import RelativeReferences.ListItem   as ListItem
import ProjectPath

from PySide2                        import QtCore, QtWidgets
from maya.app.general.mayaMixin     import MayaQWidgetBaseMixin
from RelativeReferences.lib.Classes import Colors

class PathWidget(QtWidgets.QWidget):
    class Status:
        isInvalid   = 0
        isRelative  = 1
        isProject   = 2
    
    def __init__(self, path, pathStatus, parent=None):
        super().__init__(parent)
        self.lbl = QtWidgets.QLabel(path)
        
        self.statusDisplay = QtWidgets.QToolButton()
        self.statusDisplay.setMaximumWidth(5)
        self.statusDisplay.setAutoRaise(True)
        
        if (pathStatus == PathWidget.Status.isInvalid):
            self.statusDisplay.setStyleSheet(Colors.redColorStyle)
        elif (pathStatus == PathWidget.Status.isRelative):
            self.statusDisplay.setStyleSheet(Colors.greenColorStyle)
        elif (pathStatus == PathWidget.Status.isProject):
            self.statusDisplay.setStyleSheet(Colors.orangeColorStyle)
        
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(0,1,0,1)
        self.layout().addWidget(self.statusDisplay)
        self.layout().addWidget(self.lbl)

class RelativeReferencesWindow(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    def __init__(self, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"RelativeReferences/ui/MainWindow.ui", parent=parent)
        self.setObjectName('ProjectRelativeReferences')
        self.setWindowTitle('Project Relative References')
        self.resize(700, 300)
        
        self.__keepSelection = []
        self.relativeRefs   = []
        self.projectRefs    = []
        self.invalidRefs    = []
        self.items          = []
        
        # ********* InfoButtons
        self.ui.tbt_RelPath.setStyleSheet(Colors.greenColorStyle)
        self.ui.tbt_PrjPath.setStyleSheet(Colors.orangeColorStyle)
        self.ui.tbt_InvalidPath.setStyleSheet(Colors.redColorStyle)
        
        # ********* Progress Bar
        self.ui.pgb_Progress.setHidden(True)
        
        # ********* Events Connections
        self.ui.btn_CheckScene.clicked.connect(self.btn_CheckScene_Clicked)
        self.ui.btn_AllNone.clicked.connect(self.btn_AllNone_Clicked)
        self.ui.btn_Convert.clicked.connect(self.btn_Convert_Clicked)
        self.ui.tree_References.itemChanged.connect(self.tree_References_itemChanged)
        self.ui.tree_References.itemSelectionChanged.connect(self.tree_References_itemSelectionChanged)
        
        #tree
        header = self.ui.tree_References.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setMinimumSectionSize(26)
        
    def GetPathStatus(self, path):
        if Utils.IsRelativePath(path):
            return PathWidget.Status.isRelative
        elif Utils.IsProjectPath(path):
            return PathWidget.Status.isProject
        else:
            return PathWidget.Status.isInvalid
    
    def clearList(self):
        self.ui.tree_References.clear()
        self.relativeRefs   = []
        self.projectRefs    = []
        self.invalidRefs    = []
    
    def LoadTreeReference(self, refData, parentItem=None):
        signalsBlocked = self.ui.tree_References.blockSignals(True)
        if (not parentItem):
            parentItem = self.ui.tree_References
        
        refInfo = Utils.GetReferencePath(refData[0])
        treeItem = QtWidgets.QTreeWidgetItem(parentItem, [refInfo[0], refInfo[1], "", ""])
        # Path Widget
        pathWdg = PathWidget(refInfo[2], self.GetPathStatus(refInfo[2]))
        self.ui.tree_References.setItemWidget(treeItem, 2, pathWdg)
        # Button Edit Widget
        btnWdg = QtWidgets.QPushButton("...")
        btnWdg.setMaximumSize(QtCore.QSize(22,16))
        btnWdg.setMinimumSize(QtCore.QSize(22,16))
        btnWdg.clicked.connect(functools.partial(self.btn_EditPath_Clicked, treeItem))
        self.ui.tree_References.setItemWidget(treeItem, 3, btnWdg)
        # Set Check Status and Color
        if Utils.IsRelativePath(refInfo[2]):
            treeItem.setFlags(treeItem.flags() & ~QtCore.Qt.ItemIsUserCheckable)
        elif Utils.IsProjectPath(refInfo[2]):
            treeItem.setCheckState(0, QtCore.Qt.Checked)
        treeItem.setTextAlignment(1, QtCore.Qt.AlignHCenter)
        
        if (len(refData)==2):
            for refChild in refData[1]:
                self.LoadTreeReference(refChild, treeItem)
        treeItem.setExpanded(True)
        self.ui.tree_References.blockSignals(signalsBlocked)
    
    def ReloadData(self):
        self.clearList()
        
        refs = Utils.GetSceneReferencesTree()
        for ref in refs:
            self.LoadTreeReference(ref)
        
        orderedRefs = Utils.TreeAsList(Utils.GetSceneReferencesTree())
        refs = [Utils.GetReferencePath(x) for x in orderedRefs]
        
        for ref in refs:
            if Utils.IsRelativePath(ref[2]):
                self.relativeRefs.append(ref[0])
            elif Utils.IsProjectPath(ref[2]):
                self.projectRefs.append(ref[0])
            else:
                self.invalidRefs.append(ref[0])
        
        if len(refs) == 0:
            self.ui.tbt_GlobalStatus.setStyleSheet(Colors.invisibleColorStyle)
        else:
            self.ui.tbt_GlobalStatus.setStyleSheet(Colors.greenColorStyle)
            if len(self.projectRefs) > 0:
                self.ui.tbt_GlobalStatus.setStyleSheet(Colors.orangeColorStyle)
            if len(self.invalidRefs) > 0:
                self.ui.tbt_GlobalStatus.setStyleSheet(Colors.redColorStyle)
    
    def GetChildren(self, item, recursive=False):
        result = []
        for i in range(item.childCount()):
            result.append(item.child(i))
            if (recursive):
                result += self.GetChildren(item.child(i), recursive)
        return result
    
    def GetAllTreeItems(self):
        return self.GetChildren(self.ui.tree_References.invisibleRootItem(), recursive=True)
    
    def GetSelectedTreeItems(self):
        return [x for x in self.GetAllTreeItems() if x.checkState(0)==QtCore.Qt.Checked]
    
    def AsertChildren(self, childItems):
        # When a "parent" reference is converted, their children could be "reversed"
        # as the original "parent" file could not have relative references. For this
        # reason, we reassure the relative children in this file keep being relative.
        for child in childItems:
            if (child.text(0) in self.relativeRefs):
                Utils.RelativizeReferencePath(child.text(0))
            self.AsertChildren(self.GetChildren(child))
    
    # Eventos
    def btn_CheckScene_Clicked(self):
        self.ui.pgb_Progress.setValue(0)
        self.ui.pgb_Progress.setHidden(True)
        self.ReloadData()
    
    def btn_EditPath_Clicked(self, treeItem):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Select Origin File", ProjectPath.getProjectFolder(), "Maya Files (*.ma *.mb)")
        if (fileName != ""):
            fName = fileName[0]
            if Utils.IsProjectPath(fileName[0]):
                fName = Utils.RelativizePath(fName)
            else:
                QtWidgets.QMessageBox.warning(self, "Invalid File", "The selected file is not under current project path.\nNothing will be done.")
                return
            Utils.SetReferenceFilePath(treeItem.text(0), fName)
            
        self.ReloadData()
    
    def btn_AllNone_Clicked(self):
        #tree
        targetStatus = QtCore.Qt.Unchecked
        if (len(self.GetSelectedTreeItems()) == 0):
            targetStatus = QtCore.Qt.Checked
        for x in self.GetAllTreeItems():
            if (x.flags() & QtCore.Qt.ItemIsUserCheckable):
                x.setCheckState(0, targetStatus)
    
    def btn_Convert_Clicked(self):
        selectedItems = self.GetSelectedTreeItems()
        numSelItems = len(selectedItems)
        
        if (numSelItems > 0):
            self.ui.pgb_Progress.setMinimum(0)
            self.ui.pgb_Progress.setMaximum(numSelItems)
            self.ui.pgb_Progress.setHidden(False)
            self.ui.pgb_Progress.setValue(0)
            
            totalModified = 0
            for item in selectedItems:
                Utils.RelativizeReferencePath(item.text(0))
                self.AsertChildren(self.GetChildren(item))
                totalModified +=1
                self.ui.pgb_Progress.setValue(totalModified)
            self.ReloadData()
    
    def tree_References_itemChanged(self, item, column):
        selection = self.ui.tree_References.selectedItems()
        if (column == 0 and item in selection):
            signalsBlocked = self.ui.tree_References.blockSignals(True)
            for selItem in selection:
                selItem.setCheckState(0, item.checkState(0))
            self.ui.tree_References.blockSignals(signalsBlocked)
            self.__keepSelection = selection
    
    def tree_References_itemSelectionChanged(self):
        if (self.__keepSelection):
            signalsBlocked = self.ui.tree_References.blockSignals(True)
            for item in self.__keepSelection:
                item.setSelected(True)
            self.__keepSelection = []
            self.ui.tree_References.blockSignals(signalsBlocked)


if __name__ == '__main__':
    try:
        if relRefsWindow.isVisible():
            relRefsWindow.close()
    except NameError:
        pass
    relRefsWindow = RelativeReferencesWindow()
    relRefsWindow.show()