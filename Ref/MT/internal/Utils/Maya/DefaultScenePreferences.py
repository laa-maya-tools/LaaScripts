import maya.cmds as cmds

def SetDefaultScenePreferences():
    # https://download.autodesk.com/global/docs/maya2012/en_us/Commands/optionVar.html
    # Global preferences (in case thay are not set yet):
    cmds.optionVar(stringValue=("workingUnitTimeDefault", "ntsc"))
    cmds.optionVar(fv=("gridSize", 100))
    cmds.optionVar(fv=("gridSpacing", 10))
    cmds.optionVar(fv=("gridDivisions", 1))
    
    # Current File:
    # Set Grid Size (1m front, 1m back, 1m left & 1m Right) in divisions of 10 cms
    # This preference is saved when closing Maya
    cmds.grid(size=100, spacing=10, divisions=1)
    # Set FrameRate to 30FPS
    cmds.currentUnit(time="ntsc")
    # Set Viewport transparency algorithm to Alpha Cut
    # This preference is always scene dependent (it seems it can't bet set globally)
    cmds.setAttr("hardwareRenderingGlobals.transparencyAlgorithm", 5)