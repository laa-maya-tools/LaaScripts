import maya.cmds as cmds
import maya.mel as mel

import maya.OpenMayaUI as OpenMayaUI

from PySide2 import QtWidgets

import ProjectPath

import os
import shiboken2

from Utils.Python.Versions import long

class ManipulatorControllerCommon():
    
    TOOLBOX_LAYOUT = mel.eval("$var = $gToolBox")
    TOOLBOX_LASTTOOL_BUTTON = "lastNonSacredTool"

    CONTEXT_CLASS = None
    CONTEXT_NAME = None
    CONTEXT_TOOLBUTTON = None
    CONTEXT_TOOLTIP = None
    CONTEXT_IMAGE = None
    
    @classmethod
    def updateToolPropertiesWindow(cls):
        ctx = cmds.currentCtx()
        if cmds.contextInfo(ctx, c=True) == cls.CONTEXT_CLASS:
            mel.eval("{}Values \"{}\";".format(cls.CONTEXT_CLASS, ctx))

    @classmethod
    def loadAndGetToolButton(cls):
        # Loads the configuration scripts for the tool
        scriptBasePath = "\"" + os.path.join(ProjectPath.getToolsFolder(), "AnimSystems", "ConfigurationWindow",  "{}{}.mel") + "\";"
        scriptBasePath = scriptBasePath.replace("\\", "/")
        mel.eval("source " + scriptBasePath.format(cls.CONTEXT_CLASS, "Properties"))
        mel.eval("source " + scriptBasePath.format(cls.CONTEXT_CLASS, "Values"))
        
        # Creates the manipulator context (if it already exists, recreates it) 
        if cmds.contextInfo(cls.CONTEXT_NAME, exists=True):
            cmds.deleteUI(cls.CONTEXT_NAME, toolContext=True)
        mel.eval("{0} \"{0}\"".format(cls.CONTEXT_NAME))
        
        # Creates the tool button (if it already exists, recreates it)
        cmds.setParent(cls.TOOLBOX_LAYOUT)
        if cmds.toolButton(cls.CONTEXT_TOOLBUTTON, q=True, exists=True):
            cmds.deleteUI(cls.CONTEXT_TOOLBUTTON, control=True)
        cmds.toolButton(cls.CONTEXT_TOOLBUTTON, ann=cls.CONTEXT_TOOLTIP, tool=cls.CONTEXT_NAME, collection="toolCluster", doubleClickCommand="cmds.toolPropertyWindow()", image1=cls.CONTEXT_IMAGE, width=36, height=36)
        
        # Registers the tool as a Custom Sacred Tool
        mel.eval("registerCustomSacredTool \"{}\"".format(cls.CONTEXT_NAME))
    
        toolButton = shiboken2.wrapInstance(long(OpenMayaUI.MQtUtil.findControl(cls.CONTEXT_TOOLBUTTON)), QtWidgets.QWidget)
        return toolButton

    @classmethod
    def unload(cls):
        # Deletes the manipulator context
        if cmds.contextInfo(cls.CONTEXT_NAME, exists=True):
            cmds.deleteUI(cls.CONTEXT_NAME, toolContext=True)
            
        # Deletes the tool button
        cmds.setParent(cls.TOOLBOX_LAYOUT)
        if cmds.toolButton(cls.CONTEXT_TOOLBUTTON, q=True, exists=True):
            cmds.deleteUI(cls.CONTEXT_TOOLBUTTON, control=True)
        
        # Removes the custom tool from the sacred tools list
        mel.eval("unregisterCustomSacredTool \"{}\"".format(cls.CONTEXT_NAME))


class IKManipulatorController(ManipulatorControllerCommon):

    CONTEXT_CLASS = "IKManipulatorTool"
    CONTEXT_NAME = "IKManipulatorContext"
    CONTEXT_TOOLBUTTON = "IKManipulatorToolButton"
    CONTEXT_TOOLTIP = "This tool allows to manipulate FK chains like they were IK. It also allows normal object move manipulation."
    CONTEXT_IMAGE = "Manipulators\\IKManipulator.png"
    
    OPTIONVAR_TRANSFORM_MODE = "IKMANIPULATOR_TRANSFORM_MODE"
    OPTIONVAR_ALTERNATIVE_ROTATATE_MODE = "IKMANIPULATOR_ALTERNATIVE_ROTATATE_MODE"
    OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY = "IKMANIPULATOR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY"
    OPTIONVAR_ROTATE_DISPLAY_RADIUS = "IKMANIPULATOR_ROTATE_DISPLAY_RADIUS"
    OPTIONVAR_AFFECT_END_ROTATION = "IKMANIPULATOR_AFFECT_END_ROTATION"
    OPTIONVAR_DRAW_AXIS = "IKMANIPULATOR_DRAW_AXIS"
    OPTIONVAR_UPDATE_WHILE_MOVING = "IKMANIPULATOR_UPDATE_WHILE_MOVING"

    TRANSFORM_MODES = ["Object", "World", "Parent", "Base", "Axis"]
    
    @classmethod
    def getTransformMode(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_TRANSFORM_MODE):
            defaultValue = "World"
            cls.setTransformMode(defaultValue, refresh=False)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_TRANSFORM_MODE)

    @classmethod
    def getTransformModeIndex(cls):
        return cls.TRANSFORM_MODES.index(cls.getTransformMode())

    @classmethod
    def setTransformMode(cls, mode, refresh=True, updateToolWindow=True):
        if mode in cls.TRANSFORM_MODES:
            cmds.optionVar(sv=(cls.OPTIONVAR_TRANSFORM_MODE, mode))
            if refresh:
                cmds.refresh()
            if updateToolWindow:
                cls.updateToolPropertiesWindow()
            return True
        else:
            return False

    @classmethod
    def setTransformModeIndex(cls, modeIndex):
        cls.setTransformMode(cls.TRANSFORM_MODES[modeIndex])

    @classmethod
    def isAffectEndRotation(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_AFFECT_END_ROTATION):
            defaultValue = False
            cls.setAffectEndRotation(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_AFFECT_END_ROTATION)

    @classmethod
    def setAffectEndRotation(cls, affectEndRotation, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_AFFECT_END_ROTATION, affectEndRotation))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()
    
    @classmethod
    def isUpdateWhileMoving(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_UPDATE_WHILE_MOVING):
            defaultValue = False
            cls.setUpdateWhileMoving(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_UPDATE_WHILE_MOVING)

    @classmethod
    def setUpdateWhileMoving(cls, updateWhileMoving, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_UPDATE_WHILE_MOVING, updateWhileMoving))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def isAlternativeRotateMode(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE):
            defaultValue = False
            cls.setAlternativeRotateMode(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE)

    @classmethod
    def setAlternativeRotateMode(cls, alternativeRotateMode, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE, alternativeRotateMode))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def getAlternativeRotateModeSensibility(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY):
            defaultValue = 1.0
            cls.setAlternativeRotateModeSensibility(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY)

    @classmethod
    def setAlternativeRotateModeSensibility(cls, sensibility, updateToolWindow=True):
        cmds.optionVar(fv=(cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY, sensibility))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def getRotateDisplayRadius(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS):
            defaultValue = 1.8
            cls.setRotateDisplayRadius(defaultValue, refresh=False)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS)

    @classmethod
    def setRotateDisplayRadius(cls, displayRadius, refresh=True, updateToolWindow=True):
        cmds.optionVar(fv=(cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS, displayRadius))
        if refresh:
            cmds.refresh()
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def isDrawAxis(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_DRAW_AXIS):
            defaultValue = False
            cls.setDrawAxis(defaultValue, refresh=False)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_DRAW_AXIS)

    @classmethod
    def setDrawAxis(cls, drawAxis, refresh=True, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_DRAW_AXIS, drawAxis))
        if refresh:
            cmds.refresh()
        if updateToolWindow:
            cls.updateToolPropertiesWindow()


class FKManipulatorController(ManipulatorControllerCommon):

    CONTEXT_CLASS = "FKManipulatorTool"
    CONTEXT_NAME = "FKManipulatorContext"
    CONTEXT_TOOLBUTTON = "FKManipulatorToolButton"
    CONTEXT_TOOLTIP = "This tool allows to manipulate IK chains like they were FK. It also allows normal object rotate manipulation."
    CONTEXT_IMAGE = "Manipulators\\FKManipulator.png"
    
    OPTIONVAR_TRANSFORM_MODE = "FKMANIPULATOR_TRANSFORM_MODE"
    OPTIONVAR_ALTERNATIVE_ROTATATE_MODE = "FKMANIPULATOR_ALTERNATIVE_ROTATATE_MODE"
    OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY = "FKMANIPULATOR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY"
    OPTIONVAR_ROTATE_DISPLAY_RADIUS = "FKMANIPULATOR_ROTATE_DISPLAY_RADIUS"
    OPTIONVAR_AFFECT_END_ROTATION = "FKMANIPULATOR_AFFECT_END_ROTATION"

    TRANSFORM_MODES = ["Object", "World", "Parent", "Gimbal"]
    
    @classmethod
    def getTransformMode(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_TRANSFORM_MODE):
            defaultValue = "World"
            cls.setTransformMode(defaultValue, refresh=False)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_TRANSFORM_MODE)

    @classmethod
    def getTransformModeIndex(cls):
        return cls.TRANSFORM_MODES.index(cls.getTransformMode())

    @classmethod
    def setTransformMode(cls, mode, refresh=True, updateToolWindow=True):
        if mode in cls.TRANSFORM_MODES:
            cmds.optionVar(sv=(cls.OPTIONVAR_TRANSFORM_MODE, mode))
            if refresh:
                cmds.refresh()
            if updateToolWindow:
                cls.updateToolPropertiesWindow()
            return True
        else:
            return False

    @classmethod
    def setTransformModeIndex(cls, modeIndex):
        cls.setTransformMode(cls.TRANSFORM_MODES[modeIndex])

    @classmethod
    def isAffectEndRotation(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_AFFECT_END_ROTATION):
            defaultValue = False
            cls.setAffectEndRotation(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_AFFECT_END_ROTATION)

    @classmethod
    def setAffectEndRotation(cls, affectEndRotation, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_AFFECT_END_ROTATION, affectEndRotation))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def isAlternativeRotateMode(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE):
            defaultValue = False
            cls.setAlternativeRotateMode(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE)

    @classmethod
    def setAlternativeRotateMode(cls, alternativeRotateMode, updateToolWindow=True):
        cmds.optionVar(iv=(cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE, alternativeRotateMode))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def getAlternativeRotateModeSensibility(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY):
            defaultValue = 1.0
            cls.setAlternativeRotateModeSensibility(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY)

    @classmethod
    def setAlternativeRotateModeSensibility(cls, sensibility, updateToolWindow=True):
        cmds.optionVar(fv=(cls.OPTIONVAR_ALTERNATIVE_ROTATATE_MODE_SENSIBILITY, sensibility))
        if updateToolWindow:
            cls.updateToolPropertiesWindow()

    @classmethod
    def getRotateDisplayRadius(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS):
            defaultValue = 1.8
            cls.setRotateDisplayRadius(defaultValue, refresh=False)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS)

    @classmethod
    def setRotateDisplayRadius(cls, displayRadius, refresh=True, updateToolWindow=True):
        cmds.optionVar(fv=(cls.OPTIONVAR_ROTATE_DISPLAY_RADIUS, displayRadius))
        if refresh:
            cmds.refresh()
        if updateToolWindow:
            cls.updateToolPropertiesWindow()


def load():
    # Loads the override script to add custom sacred tools and registers it
    melOverridePath = "\"" + os.path.join(ProjectPath.getToolsFolder(), "AnimSystems", "MelOverride",  "{}.mel") + "\";"
    melOverridePath = melOverridePath.replace("\\", "/")
    mel.eval("source " + melOverridePath.format("changeToolIcon"))
    
    # Registers the manipulators and retrieves the created tool buttons.
    toolButtons = [
        IKManipulatorController.loadAndGetToolButton(),
        FKManipulatorController.loadAndGetToolButton()
    ]
    
    # We need to place the button on the right spot.
    # Mel doesn't provide a simple way to do this, so we will use QT.
    parent = toolButtons[0].parent()
    layout = parent.layout()
    items = []
    while layout.count() > 0:
        items.append(layout.takeAt(0))
    
    for toolButton in toolButtons:
        for item in items:
            if item.widget() == toolButton:
                items.remove(item)
                break
    
    for i in range(len(items)):
        if items[i].widget().objectName() == ManipulatorControllerCommon.TOOLBOX_LASTTOOL_BUTTON:
            for j in range(len(toolButtons)):
                items.insert(i - 1 + j, QtWidgets.QWidgetItem(toolButtons[j]))
            break

    for item in items:
        layout.addItem(item)

def unload():
    # Unregisters the manipulators.
    IKManipulatorController.unload()
    FKManipulatorController.unload()
