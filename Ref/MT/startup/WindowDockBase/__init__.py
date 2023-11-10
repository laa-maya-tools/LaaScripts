import pymel.core       as pm
import maya.OpenMayaUI  as omui
import os
import ProjectPath

from PySide2                    import QtWidgets, QtUiTools
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from Utils.Python.Versions      import long


# Maya Bug introduced in 2018: Global holds all widgets restored from maya preferences so that qt doesnt garbage collect them if they aren't currently visible (ex: in a docked tab that isn't the currently displayed tab).
try:
    _RestoredWidgets += []
except:
    _RestoredWidgets = []

# Docking Manager class that is in charge of everything neccesary for:
# - Docking Widgets
# - Restoring Widgets when Maya is closed and reopened (with 'restoreFromClose' parameter in the "showWindow" method)
class UIDockManager(MayaQWidgetDockableMixin, QtWidgets.QWidget):
    # Override in SubClasses
    MObjName    = None
    
    def __init__(self, mayaObjName, uiFilePath, **kwargs):
        super(UIDockManager, self).__init__(**kwargs)
        self.mayaObjName = mayaObjName
        self.setObjectName(mayaObjName)
        self.ui = QtUiTools.QUiLoader().load(os.path.join(ProjectPath.getToolsFolder(), uiFilePath))
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.ui) 
    
    # Not a classmethod anymore
    #@classmethod
    def showWindow(self, dockable=True, restoreFromClose=False, debug=False):
        '''
        Call to re-show or initiate the UI.
        :param bool debug: Set to True to re-initialize an existing UI.
        '''        
        if pm.workspaceControl(self.mayaObjName + 'WorkspaceControl', ex=True):     # Test if tool is already open
            if debug:                                                               # Used to bypass saved dock preferences in maya workspaces. Useful for testing without restarting maya
                pm.deleteUI(self.mayaObjName + 'WorkspaceControl')                  # Deletes existing UI
                #Instance.__init__()                                                # Init new dock manager
                self.showWindow()                                                   # Rerun THIS show() to create new UI. (the else below)
            pm.workspaceControl(self.mayaObjName + 'WorkspaceControl', edit=True, restore=True) # Shows UI
        else:
            if restoreFromClose:
                # Show widget and attach uiScript for restoring widget from maya close using class_name and module_name to define path to restoreFromClose classmethod.
                self.show(dockable=dockable, uiScript='import {0}\n{0}.{1}.restoreFromClose()'.format(self.__module__, self.__class__.__name__))
            else:
                self.show(dockable=dockable)
    
    @classmethod
    def restoreFromClose(cls):
        '''
        Called by Maya from the preferences when starting a new session to restore last session's ui.
        '''
        Instance = cls()                                            # Init dock manager (it creates mixin widget)
        RestoredControl = omui.MQtUtil.getCurrentParent()           # Get the current maya control that the mixin widget should parent to
        MixinPtr = omui.MQtUtil.findControl(Instance.mayaObjName)   # Find the widget created above as a maya control (aka a maya class)
        _RestoredWidgets.append(Instance)                           # Hold on to Instance so qt doesnt garbage collect it
        omui.MQtUtil.addWidgetToMayaLayout(long(MixinPtr), long(RestoredControl))   # Add mixin widget to container UI