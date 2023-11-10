import maya.cmds as cmds
import maya.mel as mel

class OptionBoxWindow():
    
    loaded = False
    
    @classmethod
    def isLoaded(cls):
        return cls.loaded
    
    @classmethod
    def setLoaded(cls, loaded):
        cls.loaded = loaded
    
    @classmethod
    def createAndShow(cls):
        cls().show()
    
    def __init__(self, title, applyText):
        self.layout = mel.eval("getOptionBox();")   # Procedure not available on cmds
        
        window = mel.eval("$temp = $gOptionBox")
        saveMenuItem = mel.eval("$temp = $gOptionBoxEditMenuSaveItem")
        resetMenuItem = mel.eval("$temp = $gOptionBoxEditMenuResetItem")
        applyButton = mel.eval("$temp = $gOptionBoxApplyBtn")
        applyAndCloseButton = mel.eval("$temp = $gOptionBoxApplyAndCloseBtn")
        
        cmds.window(window, e=True, closeCommand=self.onClose)
        cmds.menuItem(saveMenuItem, e=True, command=self.saveOptions)
        cmds.menuItem(resetMenuItem, e=True, command=self.resetOptions)
        cmds.button(applyButton, e=True, command=self.apply)
        cmds.button(applyAndCloseButton, e=True, command=self.applyAndClose)
        
        if title != None:
            cmds.window(window, e=True, title=title)
        if applyText != None:
            cmds.button(applyAndCloseButton, e=True, label=applyText)
            
        cmds.setParent(self.layout)
        self.onCreateUI()
        self.applyOptions()
            
    def show(self):
        mel.eval("showOptionBox();")    # Procedure not available on cmds
        self.onShow()
        
    def close(self):
        mel.eval("hideOptionBox();")    # Procedure not available on cmds
        # onClose is called by the window's closeCommand
        
    def applyOptions(self, *args):
        if not self.isLoaded():
            self.loadOptions()
        else:
            self.onApplyOptions()
    
    def saveOptions(self, *args):
        self.onSaveOptions()
    
    def loadOptions(self, *args):
        self.onLoadOptions()
        self.setLoaded(True)
        self.applyOptions()
    
    def resetOptions(self, *args):
        self.onResetOptions()
        self.loadOptions()
        
    def applyAndClose(self, *args):
        self.apply()
        self.close()
        
    def apply(self, *args):
        self.onApply()
    
    def onCreateUI(self):
        pass
    
    def onShow(self):
        pass
    
    def onClose(self):
        pass
    
    def onApplyOptions(self):
        pass
    
    def onSaveOptions(self):
        pass
    
    def onLoadOptions(self):
        pass
    
    def onResetOptions(self):
        pass
    
    def onApply(self):
        pass

