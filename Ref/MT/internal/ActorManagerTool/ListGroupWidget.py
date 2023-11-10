
import QtCustomWidgets.UIFileWidget     as UIFileWidget

from ActorManagerTool.ListItemPartsWidget import ListItemPartsWidget

from PySide2                    import QtWidgets, QtCore, QtGui
from PySide2.QtCore             import Signal


class ListGroupWidget(UIFileWidget.UIFileWidget):
    itemSelectionChanged        = Signal()
    addClicked                  = Signal()
    deleteClicked               = Signal()
    duplicateClicked            = Signal()
    selectClicked               = Signal()
    refreshClicked              = Signal()
    lstDataItemDoubleClicked    = Signal(QtWidgets.QListWidgetItem)
    selectIcon      = QtGui.QImage(":/selectModel.png").copy(0, 0, 26, 26) #CropUnusedSpace
    addIcon         = QtGui.QImage(":/p-add.png")
    deleteIcon      = QtGui.QImage(":/delete.png")
    refreshIcon     = QtGui.QImage(":/refresh.png").copy(1, 1, 18, 18)
    duplicateIcon   = QtGui.QImage(":/duplicateReference.png")
    
    def __init__(self, title, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/ListGroup.ui", parent=parent)
        
        self.ui.gbx_main.setTitle(title)
        
        self.ui.lst_Data.itemDoubleClicked.connect(self.lst_Data_ItemDoubleClicked)
        self.ui.lst_Data.itemSelectionChanged.connect(self.lst_Data_SelectionChanged)
        self.ui.btn_Add.clicked.connect(self.btn_Add_Clicked)
        self.ui.btn_Delete.clicked.connect(self.btn_Delete_Clicked)
        self.ui.btn_Duplicate.clicked.connect(self.btn_Duplicate_Clicked)
        self.ui.btn_Refresh.clicked.connect(self.btn_Refresh_Clicked)
        self.ui.btn_Select.clicked.connect(self.btn_Select_Clicked)
        
        self.ui.btn_Add.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(ListGroupWidget.addIcon)))
        self.ui.btn_Delete.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(ListGroupWidget.deleteIcon)))
        self.ui.btn_Duplicate.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(ListGroupWidget.duplicateIcon)))
        self.ui.btn_Select.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(ListGroupWidget.selectIcon)))
        self.ui.btn_Refresh.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(ListGroupWidget.refreshIcon)))
    
    def LoadData(self, dataArray):
        self.ClearData()
        self.AppendData(dataArray)
    
    def AppendData(self, dataArray):
        for obj in dataArray:
            item = QtWidgets.QListWidgetItem('', self.ui.lst_Data)
            item.setSizeHint(QtCore.QSize(1, 20))
            self.ui.lst_Data.setItemWidget(item, ListItemPartsWidget(obj.getNamespace(), obj.name, obj))
    
    def ClearData(self):
        self.__data = []
        self.ui.lst_Data.clear()
    
    def selectedItems(self):
        return self.ui.lst_Data.selectedItems()
    
    def selectedItemsData(self):
        result = []
        for itm in self.selectedItems():
            wdgt = self.ui.lst_Data.itemWidget(itm)
            result.append(wdgt.itemData)
        return result
    
    def getItemData(self, item):
        wdgt = self.ui.lst_Data.itemWidget(item)
        return wdgt.itemData
    
    def getItemWidget(self, item):
        wdgt = self.ui.lst_Data.itemWidget(item)
        return wdgt
    
    def selectByName(self, name):
        for i in range(self.ui.lst_Data.count()):
            item = self.ui.lst_Data.item(i)
            if (self.getItemData(item).name == name):
                self.ui.lst_Data.setItemSelected(item, True)
                break
    
    def SetAddEnabled(self, value):
        self.ui.btn_Add.setEnabled(value)
    
    def SetDeleteEnabled(self, value):
        self.ui.btn_Delete.setEnabled(value)
    
    def SetSelectEnabled(self, value):
        self.ui.btn_Select.setEnabled(value)
    
    def SetRefreshVisible(self, value):
        self.ui.btn_Refresh.setVisible(value)
    
    def SetDuplicateEnabled(self, value):
        self.ui.btn_Duplicate.setEnabled(value)
    
    def SetDuplicateVisible(self, value):
        self.ui.btn_Duplicate.setVisible(value)
    
    def SetUIStatus(self, status):
        if (status <= 0): #Disabled All
            self.ui.btn_Add.setEnabled(False)
            self.ui.btn_Delete.setEnabled(False)
            self.ui.btn_Select.setEnabled(False)
            self.ui.btn_Duplicate.setEnabled(False)
        elif (status == 1): #Add Only
            self.ui.btn_Add.setEnabled(True)
            self.ui.btn_Delete.setEnabled(False)
            self.ui.btn_Select.setEnabled(False)
            self.ui.btn_Duplicate.setEnabled(False)
        elif (status == 2): #Enabled All
            self.ui.btn_Add.setEnabled(True)
            self.ui.btn_Delete.setEnabled(True)
            self.ui.btn_Select.setEnabled(True)
            self.ui.btn_Duplicate.setEnabled(True)
        elif (status == 3): #Delete and Select Only
            self.ui.btn_Add.setEnabled(False)
            self.ui.btn_Delete.setEnabled(True)
            self.ui.btn_Select.setEnabled(True)
            self.ui.btn_Duplicate.setEnabled(False)
    
    # ******************************************************
    # *********************** EVENTS ***********************
    # ******************************************************       
    def lst_Data_SelectionChanged(self):
        self.itemSelectionChanged.emit()
    
    def btn_Add_Clicked(self):
        self.addClicked.emit()
    
    def btn_Delete_Clicked(self):
        self.deleteClicked.emit()
    
    def btn_Duplicate_Clicked(self):
        self.duplicateClicked.emit()
    
    def btn_Select_Clicked(self):
        self.selectClicked.emit()
    
    def btn_Refresh_Clicked(self):
        self.refreshClicked.emit()
    
    def lst_Data_ItemDoubleClicked(self, item):
        self.lstDataItemDoubleClicked.emit(item)