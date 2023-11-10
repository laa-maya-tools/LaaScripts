from PySide2 import QtCore, QtGui, QtWidgets

class CollapsibleHeader(QtWidgets.QFrame):
    
    COLLAPSED_PIXMAP = QtGui.QPixmap(":teRightArrow.png")
    EXPANDED_PIXMAP = QtGui.QPixmap(":teDownArrow.png")
    
    clicked = QtCore.Signal()
    
    def __init__(self, text, showCheckBox, checked, parent=None):
        super(CollapsibleHeader, self).__init__(parent)
        
        self.setAutoFillBackground(True)
        self.setBackgroundColor(None)
        
        self.iconLabel = QtWidgets.QLabel()
        self.iconLabel.setFixedWidth(self.COLLAPSED_PIXMAP.width())
        
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setChecked(checked)
        self.checkBox.setVisible(showCheckBox)
        
        self.textLabel = QtWidgets.QLabel()
        self.textLabel.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        self.mainLayout.setContentsMargins(4, 4, 4, 4)
        self.mainLayout.addWidget(self.iconLabel)
        self.mainLayout.addWidget(self.checkBox)
        self.mainLayout.addWidget(self.textLabel)
        self.mainLayout.addStretch()
        
        self.setText(text)
        self.setExpanded(False)
        
    def setText(self, text):
        self.textLabel.setText("<b>{0}</b>".format(text))
        
    def setBackgroundColor(self, color):
        if not color:
            color = QtWidgets.QPushButton().palette().color(QtGui.QPalette.Button)
        
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, color)
        self.setPalette(palette)
        
    def isExpanded(self):
        return self._expanded
        
    def setExpanded(self, expanded):
        self._expanded = expanded
        
        if(self._expanded):
            self.iconLabel.setPixmap(self.EXPANDED_PIXMAP)
        else:
            self.iconLabel.setPixmap(self.COLLAPSED_PIXMAP)
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()  # pylint: disable=E1101
            return True
        else:
            event.ignore()
            return False
    
class CollapsiblePanel(QtWidgets.QWidget):
    
    def __init__(self, text, parent=None, showCheckBox=False, checked=True, mainWindow : QtWidgets.QDialog = None):
        super(CollapsiblePanel, self).__init__(parent)
        
        self.mainWindow = mainWindow
        
        self.headerWidget = CollapsibleHeader(text, showCheckBox, checked)
        self.headerWidget.clicked.connect(self.onHeaderClicked)
        
        self.bodyWidget = QtWidgets.QWidget()
        
        self.bodyLayout = QtWidgets.QVBoxLayout(self.bodyWidget)
        self.bodyLayout.setContentsMargins(4, 2, 4, 2)
        self.bodyLayout.setSpacing(3)
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.headerWidget)
        self.main_layout.addWidget(self.bodyWidget)
        
        self.widgetHeight = None
        self.setExpanded(False, resizeWindow=False)
        
    def addWidget(self, widget):
        self.bodyLayout.addWidget(widget)
        
    def addLayout(self, layout):
        self.bodyLayout.addLayout(layout)
              
    def isExpanded(self):
        return self.headerWidget.isExpanded()
    
    def setExpanded(self, expanded, resizeWindow=True):
        wasExpanded = self.isExpanded()
        
        self.headerWidget.setExpanded(expanded)
        self.bodyWidget.setVisible(expanded)
        
        if self.mainWindow and resizeWindow:
            if self.widgetHeight == None:
                if wasExpanded:
                    self.widgetHeight = self.bodyWidget.height() + 6
                else:
                    return
            
            windowHeight = self.mainWindow.height()
            if expanded:
                windowHeight += self.widgetHeight
            else:
                windowHeight -= self.widgetHeight
            self.mainWindow.setFixedHeight(windowHeight)
    
    def isChecked(self):
        return self.headerWidget.checkBox.isChecked()
    
    def setChecked(self, checked):
        return self.headerWidget.checkBox.setChecked(checked)
        
    def setHeaderBackgroundColor(self, color):
        self.headerWidget.setBackgroundColor(color)
        
    def setBodyBackgroundColor(self, color):
        palette = self.bodyWidget.palette()
        palette.setColor(QtGui.QPalette.Window, color)
        self.bodyWidget.setPalette(palette)
        self.bodyWidget.setAutoFillBackground(True)
        
    def onHeaderClicked(self):
        self.setExpanded(not self.headerWidget.isExpanded())
      