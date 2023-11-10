import maya.cmds as cmds

import AnimSystems.IKManipulator as IKManipulator

def currentContextManipulator():
    context = cmds.currentCtx()
    if context:
        return cmds.contextInfo(context, c=True)
    else:
        return None
    
def manipulatorCommand(context):
    contextClass = cmds.contextInfo(context, c=True)
    if contextClass == "manipMove":
        return cmds.manipMoveContext
    elif contextClass == "manipRotate":
        return cmds.manipRotateContext
    elif contextClass == "manipScale":
        return cmds.manipScaleContext
    else:
        return None

def displayPrompt(message):
    cmds.inViewMessage(message=message, fade=True, fadeStayTime=1200, fadeOutTime=300, position="topCenter")

def displayValuePrompt(label, value):
    displayPrompt("{} - <b style=\"color: rgb(255, 255, 0)\">{}</b>".format(label, value))


class ManipulatorModes():
    
    # These are Maya's Manipulator Modes
    moveManipulatorModes = ["Object", "Parent", "World", "Normal", "Along Rotation Axis", "Along Live Object Axis", "Custom", None, None, None, "Component"]
    rotateManipulatorModes = ["Object", "World", "Gimbal", None, None, None, None, None, None, None, "Component"]
    scaleManipulatorModes = moveManipulatorModes    # Position and scale use the same modes

    @classmethod
    def moveContextManipulatorModeIndex(cls, manipulateContext="Move"):
        return cmds.manipMoveContext(manipulateContext, q=True, mode=True)

    @classmethod
    def moveContextManipulatorMode(cls, manipulateContext="Move"):
        return cls.moveManipulatorModes[cls.moveContextManipulatorModeIndex(manipulateContext=manipulateContext)]

    @classmethod
    def setMoveContextManipulatorModeIndex(cls, manipulatorModeIndex, manipulateContext="Move", showPrompt=False):
        cmds.manipMoveContext(manipulateContext, e=True, mode=manipulatorModeIndex)
        if showPrompt:
            displayValuePrompt("Move", cls.moveManipulatorModes[manipulatorModeIndex])

    @classmethod
    def setMoveContextManipulatorMode(cls, manipulatorMode, manipulateContext="Move", showPrompt=False):
        if manipulatorMode in cls.moveManipulatorModes:
            cls.setMoveContextManipulatorModeIndex(cls.moveManipulatorModes.index(manipulatorMode), manipulateContext=manipulateContext, showPrompt=showPrompt)
            return True
        else:
            return False

    @classmethod
    def rotateContextManipulatorModeIndex(cls, manipulateContext="Rotate"):
        return cmds.manipRotateContext(manipulateContext, q=True, mode=True)

    @classmethod
    def rotateContextManipulatorMode(cls, manipulateContext="Rotate"):
        return cls.rotateManipulatorModes[cls.rotateContextManipulatorModeIndex(manipulateContext=manipulateContext)]

    @classmethod
    def setRotateContextManipulatorModeIndex(cls, manipulatorModeIndex, manipulateContext="Rotate", showPrompt=False):
        cmds.manipRotateContext(manipulateContext, e=True, mode=manipulatorModeIndex)
        if showPrompt:
            displayValuePrompt("Rotate", cls.rotateManipulatorModes[manipulatorModeIndex])

    @classmethod
    def setRotateContextManipulatorMode(cls, manipulatorMode, manipulateContext="Rotate", showPrompt=False):
        if manipulatorMode in cls.rotateManipulatorModes:
            cls.setRotateContextManipulatorModeIndex(cls.rotateManipulatorModes.index(manipulatorMode), manipulateContext=manipulateContext, showPrompt=showPrompt)
            return True
        else:
            return False

    @classmethod
    def scaleContextManipulatorModeIndex(cls, manipulateContext="Scale"):
        return cmds.manipScaleContext(manipulateContext, q=True, mode=True)

    @classmethod
    def scaleContextManipulatorMode(cls, manipulateContext="Scale"):
        return cls.scaleManipulatorModes[cls.scaleContextManipulatorModeIndex(manipulateContext=manipulateContext)]

    @classmethod
    def setScaleContextManipulatorModeIndex(cls, manipulatorModeIndex, manipulateContext="Scale", showPrompt=False):
        cmds.manipScaleContext(manipulateContext, e=True, mode=manipulatorModeIndex)
        if showPrompt:
            displayValuePrompt("Scale", cls.scaleManipulatorModes[manipulatorModeIndex])

    @classmethod
    def setScaleContextManipulatorMode(cls, manipulatorMode, manipulateContext="Scale", showPrompt=False):
        if manipulatorMode in cls.scaleManipulatorModes:
            cls.setScaleContextManipulatorModeIndex(cls.scaleManipulatorModes.index(manipulatorMode), manipulateContext=manipulateContext, showPrompt=showPrompt)
            return True
        else:
            return False

    @classmethod
    def currentContextManipulatorModeIndex(cls):
        context = cmds.currentCtx()
        contextClass = cmds.contextInfo(context, c=True)

        if contextClass == "manipMove":
            return cls.moveContextManipulatorModeIndex(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == "manipRotate":
            return cls.rotateContextManipulatorModeIndex(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == "manipScale":
            return cls.scaleContextManipulatorModeIndex(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == IKManipulator.IKManipulatorController.CONTEXT_CLASS:
            return IKManipulator.IKManipulatorController.getTransformModeIndex()
        elif contextClass == IKManipulator.FKManipulatorController.CONTEXT_CLASS:
            return IKManipulator.FKManipulatorController.getTransformModeIndex()
        else:
            return None

    @classmethod
    def currentContextManipulatorMode(cls):
        context = cmds.currentCtx()
        contextClass = cmds.contextInfo(context, c=True)

        if contextClass == "manipMove":
            return cls.moveContextManipulatorMode(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == "manipRotate":
            return cls.rotateContextManipulatorMode(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == "manipScale":
            return cls.scaleContextManipulatorMode(manipulateContext=cmds.superCtx(context, q=True))
        elif contextClass == IKManipulator.IKManipulatorController.CONTEXT_CLASS:
            return IKManipulator.IKManipulatorController.getTransformMode()
        elif contextClass == IKManipulator.FKManipulatorController.CONTEXT_CLASS:
            return IKManipulator.FKManipulatorController.getTransformMode()
        else:
            return None

    @classmethod
    def setCurrentContextManipulatorModeIndex(cls, manipulatorModeIndex, showPrompt=False):
        context = cmds.currentCtx()
        contextClass = cmds.contextInfo(context, c=True)

        if contextClass == "manipMove":
            cls.setMoveContextManipulatorModeIndex(manipulatorModeIndex, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == "manipRotate":
            cls.setRotateContextManipulatorModeIndex(manipulatorModeIndex, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == "manipScale":
            cls.setScaleContextManipulatorModeIndex(manipulatorModeIndex, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == IKManipulator.IKManipulatorController.CONTEXT_CLASS:
            val = IKManipulator.IKManipulatorController.setTransformModeIndex(manipulatorModeIndex)
            if showPrompt:
                displayValuePrompt("IK Manipulator", IKManipulator.IKManipulatorController.TRANSFORM_MODES[manipulatorModeIndex])
            return val
        elif contextClass == IKManipulator.FKManipulatorController.CONTEXT_CLASS:
            val = IKManipulator.FKManipulatorController.setTransformModeIndex(manipulatorModeIndex)
            if showPrompt:
                displayValuePrompt("FK Manipulator", IKManipulator.FKManipulatorController.TRANSFORM_MODES[manipulatorModeIndex])
            return val
        
    @classmethod
    def setCurrentContextManipulatorMode(cls, manipulatorMode, showPrompt=False):
        context = cmds.currentCtx()
        contextClass = cmds.contextInfo(context, c=True)

        if contextClass == "manipMove":
            return cls.setMoveContextManipulatorMode(manipulatorMode, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == "manipRotate":
            return cls.setRotateContextManipulatorMode(manipulatorMode, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == "manipScale":
            return cls.setScaleContextManipulatorMode(manipulatorMode, manipulateContext=cmds.superCtx(context, q=True), showPrompt=showPrompt)
        elif contextClass == IKManipulator.IKManipulatorController.CONTEXT_CLASS:
            val = IKManipulator.IKManipulatorController.setTransformMode(manipulatorMode)
            if showPrompt:
                displayValuePrompt("IK Manipulator", manipulatorMode)
            return val
        elif contextClass == IKManipulator.FKManipulatorController.CONTEXT_CLASS:
            val = IKManipulator.FKManipulatorController.setTransformMode(manipulatorMode)
            if showPrompt:
                displayValuePrompt("FK Manipulator", manipulatorMode)
            return val
        else:
            return False


class Snap():
    
    @staticmethod
    def getCurrentSnapState():
        context = cmds.currentCtx()
        contextCommand = manipulatorCommand(context)
        
        if contextCommand:
            superCtx = cmds.superCtx(context, q=True)
            return contextCommand(superCtx, q=True, snap=True)
        else:
            return None
        
    @staticmethod
    def getCurrentSnapValue():
        context = cmds.currentCtx()
        contextCommand = manipulatorCommand(context)
        
        if contextCommand:
            superCtx = cmds.superCtx(context, q=True)
            return contextCommand(superCtx, q=True, snapValue=True)
        else:
            return None
        
    @staticmethod
    def setCurrentSnapState(state, showMessage=True):
        context = cmds.currentCtx()
        contextCommand = manipulatorCommand(context)
        
        if contextCommand:
            superCtx = cmds.superCtx(context, q=True)
            contextCommand(superCtx, e=True, snap=state)
            
            if showMessage:
                displayValuePrompt("Snap", "On ({})</b>".format(contextCommand(superCtx, q=True, snapValue=True)) if state else "Off")
        
    @staticmethod
    def setCurrentSnapValue(value, showMessage=True):
        context = cmds.currentCtx()
        contextCommand = manipulatorCommand(context)
        
        if contextCommand:
            superCtx = cmds.superCtx(context, q=True)
            contextCommand(superCtx, e=True, snapValue=value)
            
            if showMessage:
                displayValuePrompt("Snap", value)
        
