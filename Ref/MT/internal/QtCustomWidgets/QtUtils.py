from PySide2 import QtCore, QtWidgets, QtGui

# ------------------------------------
# | Block Signals                    |
# ------------------------------------
# | Custom context to easily manage  |
# | the blocking of UI signals.      |
# ------------------------------------

class BlockSignals(object):

    def __init__(self, target):
        self.target = target
        self.wereSignalsBlocked = False

    def __enter__(self):
        self.wereSignalsBlocked = self.target._signalsBlocked
        self.target._signalsBlocked = True

    def __exit__(self, type, value, traceback):
        self.target._signalsBlocked = self.wereSignalsBlocked
        
# ------------------------------------
# | QTableWidget                     |
# ------------------------------------
# | Different utility functions to   |
# | operate with QTableWidget.       |
# ------------------------------------

def setTableWidgetItemFlag(item, flag, state):
    if state:
        item.setFlags(item.flags() | flag)
    else:
        item.setFlags(item.flags() & ~flag)

def setTableWidgetItemEnabled(item, enabled):
    setTableWidgetItemFlag(item, QtCore.Qt.ItemIsEnabled, enabled)
        
# ------------------------------------
# | QListWidget                      |
# ------------------------------------
# | Different utility functions to   |
# | operate with QListWidget.        |
# ------------------------------------
    
def createListWidgetSeparatorItem(height=1):
    separatorItem = QtWidgets.QListWidgetItem()
    separatorItem.setSizeHint(QtCore.QSize(0, height))
    separatorItem.setFlags(QtCore.Qt.NoItemFlags)
    separatorItem.setBackgroundColor(QtGui.QColor.fromHsl(0, 0, 90))
    return separatorItem

# ------------------------------------
# | Colors                           |
# ------------------------------------
# | Functions related to Qt Colors.  |
# ------------------------------------

def setPaletteColor(widget, field, color):
    palette = widget.palette()
    palette.setColor(field, color)
    widget.setPalette(palette)

def restorePaletteColor(widget, field):
    defaultPalette = QtGui.QPalette()
    palette = widget.palette()
    palette.setColor(field, defaultPalette.color(field))
    widget.setPalette(palette)

# ------------------------------------
# | Menu Options                     |
# ------------------------------------
# | Custom class to easily create Qt |
# | menus.                           |
# ------------------------------------

class MenuOption():

    def __init__(self, objectName, text, enableOnMultiSelect=False, callback=None, toolTip=None, subMenus=None, checkable=False, checked=False):
        self.objectName = objectName
        self.text = text
        self.enableOnMultiSelect = enableOnMultiSelect
        self.callback = callback
        self.toolTip = toolTip
        self.subMenus = subMenus
        self.checkable = checkable
        self.checked = checked

    def addItemToMenu(self, menu, parent, multiSelection=False):
        if self.enableOnMultiSelect or not multiSelection:
            if self.subMenus == None and self.callback != None:
                action = QtWidgets.QAction(parent)
                action.setObjectName(self.objectName)
                action.setText(self.text)
                action.setToolTip(self.toolTip)
                action.setCheckable(self.checkable)
                action.setChecked(self.checked)
                action.triggered.connect(self.callback)
                menu.addAction(action)
            elif self.subMenus != None and len(self.subMenus) > 0:
                subMenu = QtWidgets.QMenu(self.text, parent)
                subMenu.setToolTipsVisible(True)
                subMenu.setToolTip(self.toolTip)
                for menuItem in self.subMenus:
                    if menuItem == None:
                        subMenu.addSeparator()
                    else:
                        menuItem.addItemToMenu(subMenu, parent)
                menu.addMenu(subMenu)


def showContextMenu(options, parent, position, multiSelection=False):
    menu = QtWidgets.QMenu(parent)
    menu.setToolTipsVisible(True)

    for option in options:
        if option == None:
            menu.addSeparator()
        else:
            option.addItemToMenu(menu, parent, multiSelection=multiSelection)

    menu.exec_(position)

# ------------------------------------
# | Select Items Dialog              |
# ------------------------------------
# | Dialog to display a generic list |
# | of strings and allow the user to |
# | select one or more of them.      |
# ------------------------------------

class SelectItemsDialog(QtWidgets.QDialog):

    def __init__(self, parent, title, items, labels=None, defaultSelection=None, multiSelection=True, includeNoneOption=False, okButtonText="Ok", cancelButtonText="Cancel", noItemsText="<No available items!>", noneItemText="<None>"):
        QtWidgets.QDialog.__init__(self, parent=parent)

        self.items = items
        self.labels = labels
        self.defaultSelection = defaultSelection
        self.multiSelection = multiSelection
        self.includeNoneOption = includeNoneOption
        self.noItemsText = noItemsText
        self.noneItemText = noneItemText

        self.setWindowTitle(title)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.itemList = QtWidgets.QListWidget()
        self.itemList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.itemList.itemDoubleClicked.connect(self.onItemDoubleClicked)
        layout.addWidget(self.itemList)

        buttonLayout = QtWidgets.QHBoxLayout()
        layout.addLayout(buttonLayout)
        
        buttonLayout.addStretch()

        self.okButton = QtWidgets.QPushButton(okButtonText)
        self.okButton.clicked.connect(self.accept)
        buttonLayout.addWidget(self.okButton)

        self.cancelButton = QtWidgets.QPushButton(cancelButtonText)
        self.cancelButton.clicked.connect(self.reject)
        buttonLayout.addWidget(self.cancelButton)

    def onItemDoubleClicked(self, item):
        if self.includeNoneOption or item.data(QtCore.Qt.UserRole) != None:
            self.accept()

    def showEvent(self, event):
        self.itemList.clear()
        if len(self.items) == 0 and not self.includeNoneOption:
            self.itemList.setSelectionMode(QtWidgets.QListWidget.NoSelection)
            self.okButton.setEnabled(False)
            self.itemList.addItem(QtWidgets.QListWidgetItem(self.noItemsText))
        else:
            self.itemList.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection if self.multiSelection else QtWidgets.QListWidget.SingleSelection)
            self.okButton.setEnabled(True)
            if self.includeNoneOption:
                noItem = QtWidgets.QListWidgetItem(self.noneItemText)
                self.itemList.addItem(noItem)
                self.itemList.addItem(createListWidgetSeparatorItem())

            for i, item in enumerate(self.items):
                listItem = QtWidgets.QListWidgetItem(self.labels[i] if self.labels else item)
                listItem.setData(QtCore.Qt.UserRole, item)
                listItem.setSelected(item == self.items[0])
                self.itemList.addItem(listItem)

                if self.defaultSelection != None:
                    listItem.setSelected(item in self.defaultSelection)

            if self.includeNoneOption and self.defaultSelection == None:
                noItem.setSelected(True)

    def getSelectedItems(self):
        items = self.itemList.selectedItems()
        itemData = [item.data(QtCore.Qt.UserRole) for item in items]
        if itemData == [None]:
            return []
        else:
            return itemData
        
    def run(self):
        result = self.exec_()
        if result == self.Accepted:
            return self.getSelectedItems()
        else:
            return None
        

# ------------------------------------
# | Edit Items Dialog                |
# ------------------------------------
# | Dialog to display a generic list |
# | of strings and allow the user to |
# | edit it.                         |
# ------------------------------------

class EditItemsDialog(QtWidgets.QDialog):
    
    TYPE_FLOAT = float

    def __init__(self, parent, title, items, dataType, parserFunction=None, allowAddAndRemove=True, allowReorder=True, okButtonText="Save", cancelButtonText="Cancel"):
        QtWidgets.QDialog.__init__(self, parent=parent)

        self.items = items
        self.dataType = dataType
        self.parserFunction = parserFunction if parserFunction else self.dataType
        self.allowAddAndRemove = allowAddAndRemove
        self.allowReorder = allowReorder

        self.setWindowTitle(title)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        
        upperLayout = QtWidgets.QHBoxLayout()
        layout.addLayout(upperLayout)
        
        upperLayout.addStretch()
        
        self.addItemButton = QtWidgets.QPushButton("Add")
        self.addItemButton.clicked.connect(self.addNewItem)
        upperLayout.addWidget(self.addItemButton)

        self.deleteItemsButton = QtWidgets.QPushButton("Remove")
        self.deleteItemsButton.clicked.connect(self.deleteSelectedItems)
        upperLayout.addWidget(self.deleteItemsButton)

        self.itemList = QtWidgets.QListWidget()
        self.itemList.itemChanged.connect(self.onItemEdited)
        layout.addWidget(self.itemList)

        buttonLayout = QtWidgets.QHBoxLayout()
        layout.addLayout(buttonLayout)
        
        buttonLayout.addStretch()

        self.okButton = QtWidgets.QPushButton(okButtonText)
        self.okButton.clicked.connect(self.accept)
        buttonLayout.addWidget(self.okButton)

        self.cancelButton = QtWidgets.QPushButton(cancelButtonText)
        self.cancelButton.clicked.connect(self.reject)
        buttonLayout.addWidget(self.cancelButton)

    def onItemEdited(self, item):
        try:
            item.setData(QtCore.Qt.UserRole, self.parserFunction(item.text()))
        except:
            pass
        
        item.setText(str(item.data(QtCore.Qt.UserRole)))

    def showEvent(self, event):
        self.itemList.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection if self.allowAddAndRemove else QtWidgets.QListWidget.NoSelection)
        self.itemList.setDragDropMode(QtWidgets.QListWidget.DragDrop if self.allowReorder else QtWidgets.QListWidget.NoDragDrop)
        self.itemList.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.itemList.clear()
        for item in self.items:
            self.addItem(item)
            
        self.addItemButton.setVisible(self.allowAddAndRemove)
        self.deleteItemsButton.setVisible(self.allowAddAndRemove)
            
    def addItem(self, item):
        listItem = QtWidgets.QListWidgetItem(str(item))
        listItem.setData(QtCore.Qt.UserRole, item)
        listItem.setFlags(listItem.flags() | QtCore.Qt.ItemIsEditable)
        self.itemList.addItem(listItem)
        
    def addNewItem(self):
        newItemText, result = QtWidgets.QInputDialog.getText(self, self.windowTitle(), "Add New Item")
        if result:
            try:
                self.addItem(self.parserFunction(newItemText))
            except:
                QtWidgets.QMessageBox.warning(self, "Add New Item", "Invalid Item: {}".format(newItemText))
                self.addNewItem()
    
    def deleteSelectedItems(self):
        selectedItems = self.itemList.selectedItems()
        for item in selectedItems:
            self.itemList.takeItem(self.itemList.row(item))

    def getListItems(self):
        return [self.itemList.item(i).data(QtCore.Qt.UserRole) for i in range(self.itemList.count())]
        
    def run(self):
        result = self.exec_()
        if result == self.Accepted:
            return self.getListItems()
        else:
            return None