from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import QtCustomWidgets.UIFileWidget as UIFileWidget

class DevSystemWidget(MayaQWidgetBaseMixin, UIFileWidget.UIFileWidget):
    def __init__(self, internalWidget, parent=None):
        UIFileWidget.UIFileWidget.__init__(self, r"C:\Users\dricobarral\Desktop\d_module\AutoRig\ui\DevSystemWidget.ui", parent=parent)
        #cojo el layout que quiero y le inserto el internalWidget
        self.ui.systemQVBoxLayout.addWidget(internalWidget)
        self.ui.systemQPushButton.clicked.connect(internalWidget.__do__)
        self.ui.systemQGroupBox.setTitle(internalWidget.__parentTitle__ + " Config:")

def show(QWiddget):
    global systemWidget
    try:
        if systemWidget.isVisible():
            systemWidget.close()
    except NameError:
        pass
    systemWidget = DevSystemWidget(QWiddget)
    systemWidget.show()