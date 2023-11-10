from PySide2                    import QtWidgets

class FooterMessageWidget(QtWidgets.QWidget):
    class type():
        warning = "*WARNING*"
        error = "-ERROR-"
        info = "Info"
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(2)
        layout.setSpacing(2)
        self.setLayout(layout)