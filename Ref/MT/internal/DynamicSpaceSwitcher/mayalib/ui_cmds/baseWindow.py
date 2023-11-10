import maya.cmds as cmds

class BaseWindow(object):
    
    WINDOW_NAME = "BaseWindow"
    WINDOW_TITLE = "Base Window"
    WIDTH = 300
    HEIGHT = 600    
    SCROLLABLE = True

    def __init__(self):
        self.createUI()
        
    def createUI(self):
        if (cmds.window(self.WINDOW_NAME, exists=True)):
            cmds.deleteUI(self.WINDOW_NAME)
        
        # Window    
        self.window = cmds.window(self.WINDOW_NAME, title=self.WINDOW_TITLE, width=self.WIDTH, height=self.HEIGHT,
                        sizeable=True, minimizeButton=True, maximizeButton=True)
        cmds.window(self.window, edit=True, width=self.WIDTH, height=self.HEIGHT)    
        
        # Main Layout
        self.mainLayout = cmds.columnLayout("mainLayout", width=self.WIDTH)    
        self.contentLayout = self.mainLayout
        
        if self.SCROLLABLE:
            self.scrollLayout = cmds.scrollLayout("scrollLayout", width=self.WIDTH, height=self.HEIGHT, parent=self.mainLayout)
            self.contentLayout = cmds.columnLayout("contentLayout", width=self.WIDTH - 16, parent=self.scrollLayout)
        
        self.createCustomUI()
        
        cmds.showWindow(self.window)    

    def createCustomUI(self):
        print("BaseWindow.createCustomUI Sobreescribe esta funcion en las clases hijas")


