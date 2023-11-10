import QtCustomWidgets.CollapsiblePanel as CollapsiblePanel

class AnimWidgetPanel(CollapsiblePanel.CollapsiblePanel):
    
    def __init__(self, group, animationTab, parent=None, contextMenuCallback=None):
        CollapsiblePanel.CollapsiblePanel.__init__(self, group, parent=parent)
        
        self.group = group
        self.animationTab = animationTab
        self.contextMenuCallback = contextMenuCallback
        
        self.main_layout.setSpacing(3)
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
    
    def getAnimWidgets(self):
        animWidgetsLayout = self.bodyLayout.layout()
        animWidgets = []
        for i in range(animWidgetsLayout.count()):
            widget = animWidgetsLayout.itemAt(i).widget()
            if type(widget) == AnimWidgetPanel:
                animWidgets += widget.getAnimWidgets()
            else:
                animWidgets.append(widget)
        return animWidgets
    
    def contextMenuEvent(self, event):
        self.contextMenuCallback(self.group, self, event)
    