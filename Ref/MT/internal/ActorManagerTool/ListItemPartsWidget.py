import QtCustomWidgets.UIFileWidget     as UIFileWidget

class ListItemPartsWidget(UIFileWidget.UIFileWidget):    
    def __init__(self, namespace, name, itemData=None, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"ActorManagerTool/ui/ListItemParts.ui", parent=parent)
        
        self.itemData = itemData
        
        self.ui.lbl_NameSpace.setText(namespace)
        self.ui.lbl_Name.setText(name)
        
        if (namespace==None):
            self.ui.lbl_NameSpace.setVisible(False)
            self.ui.lbl_Separator.setVisible(False)
    
    def setName(self, newName):
        self.ui.lbl_Name.setText(newName)