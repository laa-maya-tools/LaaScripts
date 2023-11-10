import QtCustomWidgets.UIFileWidget         as UIFileWidget
import RelativeReferences.lib.Utils  as Utils
import ProjectPath

from PySide2                                import QtCore, QtWidgets
from maya.app.general.mayaMixin             import MayaQWidgetBaseMixin
from RelativeReferences.lib.Classes  import Colors

class Status:
    isInvalid   = 0
    isRelative  = 1
    isProject   = 2
    
class ListItemWidget(UIFileWidget.UIFileWidget):
    pathChanged = QtCore.Signal()
    
    def __init__(self, refName, namespace, refPath, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"RelativeReferences/ui/ListItemWidget.ui", parent=parent)
        self.status = None
        self.referenceNode = refName
        self.ui.lbl_RefName.setText(refName)
        self.ui.lbl_Namespace.setText(namespace)
        self.ui.lbl_RefPath.setText(refPath)
        
        self.ui.btn_Edit.clicked.connect(self.btn_Edit_Clicked)
    
    def SetStatus(self, status):
        self.status = status
        self.ui.chb_Selected.setEnabled(False)
        self.ui.chb_Selected.setVisible(False)
        if status != None:
            if status == Status.isInvalid:
                self.ui.tbt_Status.setStyleSheet(Colors.redColorStyle)
            elif status == Status.isProject:
                self.ui.tbt_Status.setStyleSheet(Colors.orangeColorStyle)
                self.ui.chb_Selected.setEnabled(True)
                self.ui.chb_Selected.setVisible(True)
            elif status == Status.isRelative:
                self.ui.tbt_Status.setStyleSheet(Colors.greenColorStyle)
        else:
            self.ui.tbt_Status.setStyleSheet(Colors.invisibleColorStyle)
    
    def SetCheckStatus(self, value):
        if self.ui.chb_Selected.isEnabled():
            if value:
                self.ui.chb_Selected.setCheckState(QtCore.Qt.Checked)
            else:
                self.ui.chb_Selected.setCheckState(QtCore.Qt.Unchecked)
    
    def IsChecked(self):
        if self.ui.chb_Selected.isEnabled():
            return self.ui.chb_Selected.isChecked()
        else:
            return False
    
    def btn_Edit_Clicked(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Select Origin File", ProjectPath.getProjectFolder(), "Maya Files (*.ma *.mb)")
        if (fileName != ""):
            fName = fileName[0]
            if Utils.IsProjectPath(fileName[0]):
                fName = Utils.RelativizePath(fName)
            else:
                QtWidgets.QMessageBox.warning(self, "Invalid File", "The selected file is not under current project path.\nNothing will be done.")
                return
            Utils.SetReferenceFilePath(self.referenceNode, fName)
            self.pathChanged.emit()