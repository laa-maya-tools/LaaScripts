from PySide2 import QtCore, QtGui, QtWidgets

from MayaImprovements import MayaImprovement

import TimeSlider

import maya.cmds as cmds

class ClearFocusOnEnterEventFilter(QtCore.QObject):
    
    validClasses = [
        QtWidgets.QLineEdit,
        QtWidgets.QSpinBox,
        QtWidgets.QDoubleSpinBox
    ]
    
    @classmethod
    def isValidClass(cls, obj):
        for validClass in cls.validClasses:
            if isinstance(obj, validClass):
                return True
        return False
    
    @classmethod
    def isChannelBox(cls, obj):
        parent = obj.parent()
        if parent:
            parent = parent.parent()
            return parent.objectName() == TimeSlider.mainChannelBox
        return False
    
    def eventFilter(self, watched, event):
        if type(event) == QtGui.QPainter:
            # How the hell are we receiving a QPainter here???
            return False
        
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
                app = QtGui.QGuiApplication.instance()
                focusedObject = app.focusObject()
                if self.isValidClass(focusedObject):
                    cmds.evalDeferred(self.clearFocusedObject)
                    
                    if self.isChannelBox(focusedObject):
                        cmds.evalDeferred(self.deselectChannelBox)
                        return True
                        
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            # Feature para los que tenemos ratones con botones laterales :P
            app : QtGui.QGuiApplication = QtGui.QGuiApplication.instance()
            focusedObject = app.focusObject()
            if self.isValidClass(focusedObject) and not focusedObject.underMouse():
                self.clearFocusedObject()
                
            if event.button() == QtCore.Qt.ExtraButton1:
                # Mouse 4 (Back Button)
                if event.modifiers() & QtCore.Qt.AltModifier:
                    if event.modifiers() == QtCore.Qt.AltModifier | QtCore.Qt.ControlModifier:
                        cmds.TravelToAllSiblings()
                    elif event.modifiers() == QtCore.Qt.AltModifier | QtCore.Qt.ShiftModifier:
                        cmds.TravelToSiblingDownAdditive()
                    else:
                        cmds.TravelToSiblingDown()
                else:
                    if event.modifiers() == QtCore.Qt.ControlModifier:
                        cmds.TravelToAllDescendants()
                    elif event.modifiers() == QtCore.Qt.ShiftModifier:
                        cmds.TravelToChildrenAdditive()
                    else:
                        cmds.TravelToChildren()
                return True
            elif event.button() == QtCore.Qt.ExtraButton2:
                # Mouse 5 (Forward Button)
                if event.modifiers() & QtCore.Qt.AltModifier:
                    if event.modifiers() == QtCore.Qt.AltModifier | QtCore.Qt.ControlModifier:
                        cmds.TravelToAllSiblings()
                    elif event.modifiers() == QtCore.Qt.AltModifier | QtCore.Qt.ShiftModifier:
                        cmds.TravelToSiblingUpAdditive()
                    else:
                        cmds.TravelToSiblingUp()
                else:
                    if event.modifiers() == QtCore.Qt.ShiftModifier:
                        cmds.TravelToParentAdditive()
                    else:
                        cmds.TravelToParent()
                return True
            
        return False
    
    def clearFocusedObject(self):
        app = QtGui.QGuiApplication.instance()
        focusedObject = app.focusObject()
        focusedObject.clearFocus()
        
    def deselectChannelBox(self):
        cmds.channelBox(TimeSlider.mainChannelBox, e=True, select="")


class ClearFocusOnEnter(MayaImprovement):

    initialized = False
    
    eventFilter = ClearFocusOnEnterEventFilter()
    eventFilterInstalled = False
    
    quitApplicationScriptJob = None

    # Constants
    clearFocusWithEnterOptionVar = "clearFocusWithEnterEnabled"

    @classmethod
    def isClearFocusWithEnterEnabled(cls):
        if not cls.initialized:
            return False
        
        if not cmds.optionVar(exists=cls.clearFocusWithEnterOptionVar):
            default = False  # Disabled by default
            cls.setClearFocusWithEnterEnabled(default)
            return default
        
        return cmds.optionVar(q=cls.clearFocusWithEnterOptionVar)

    @classmethod
    def setClearFocusWithEnterEnabled(cls, enabled, updateOptionVar=True):
        if cls.eventFilterInstalled != enabled:
            app = QtGui.QGuiApplication.instance()
            if enabled:
                app.installEventFilter(cls.eventFilter)
                cls.eventFilterInstalled = True
            else:
                app.removeEventFilter(cls.eventFilter)
                cls.eventFilterInstalled = False
        
        if updateOptionVar:
            cmds.optionVar(iv=(cls.clearFocusWithEnterOptionVar, enabled))
            
    @classmethod
    def onQuitApplication(cls):
        # Fix para que Maya no crashee al cerrar con el ScriptEditor abierto tras haber instalado un eventFilter ¯\_(ツ)_/¯
        cmds.workspaceControl("scriptEditorPanel1Window", e=True, close=True) 

    @classmethod
    def initialize(cls):
        cls.initialized = True
        
        cls.quitApplicationScriptJob = cmds.scriptJob(e=["quitApplication", cls.onQuitApplication])

        cls.setClearFocusWithEnterEnabled(cls.isClearFocusWithEnterEnabled(), updateOptionVar=False)

    @classmethod
    def uninitialize(cls):
        cls.initialized = False
        
        cmds.scriptJob(k=cls.quitApplicationScriptJob)

        cls.setClearFocusWithEnterEnabled(False, updateOptionVar=False)
