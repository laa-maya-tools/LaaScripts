import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window as CinematicEditorUtils
import CinematicEditor.Window.CinematicEditorConfiguration as CEConfiguration
import ExporterWindow
import ScreenDrawer.CinematicGuides as CinematicGuides

from Utils.Maya.RepeatCommand import RepeatCommand
from CustomCommands.CommonCommands import TimeChangeRepeat

import Utils.Maya as MayaUtils

#---------------------------------
#|          Functions            |
#---------------------------------

def frameCurrentShot():
    if CinematicEditorUtils.isVisible():
        currentShot = CinematicEditorUtils.instance.cinematicEditorTimeline.getCurrentShot()
        if currentShot:
            currentShot.applyAnimRange(goTo=currentShot.goToClamp)

def frameSelectedShots():
    if CinematicEditorUtils.isVisible():
        selectedShots = CinematicEditorUtils.instance.shotTable.getSelectedShots()
        if selectedShots:
            selectedShots[0].getCutscene().frameShots(selectedShots)

def frameAllShots():
    if CinematicEditorUtils.isVisible():
        cutscene = CinematicEditor.getCutscene(createIfNotExists=False)
        if cutscene:
            cutscene.frameAllShots()
            
def toggleAutoFrameShots():
    if CinematicEditorUtils.isVisible():
        CEConfiguration.AUTO_FRAME_ENABLED_OPTIONVAR.value = not CEConfiguration.AUTO_FRAME_ENABLED_OPTIONVAR.value

def playCutscene():
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.togglePlayback(fromTheBeginning=False)
    
def goToNextCinematicFrame(count, repeating):
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.goToNextCinematicFrame(count)
    
def goToPreviousCinematicFrame(count, repeating):
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.goToPreviousCinematicFrame(count)
    
nextCutsceneFrameRepeatCommand = RepeatCommand(goToNextCinematicFrame, startTime=TimeChangeRepeat.repeatStartTime, toggleRate=MayaUtils.getFrameRate())
previousCutsceneFrameRepeatCommand = RepeatCommand(goToPreviousCinematicFrame, startTime=TimeChangeRepeat.repeatStartTime, toggleRate=MayaUtils.getFrameRate())

def nextShot():
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.goToNextShot()
    
def previousShot():
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.goToPreviousShot()
        
def toggleRules():
    CinematicGuides.CINEMATIC_GUIDES_ENABLED_OPTIONVAR.value = not CinematicGuides.CINEMATIC_GUIDES_ENABLED_OPTIONVAR.value
    
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.refreshCinematicGuides()
    if ExporterWindow.isVisible():
        ExporterWindow.instance.refreshCurrentTab()
        
    cmds.refresh(force=True)
    
def switchRules():
    modes = CinematicGuides.CinematicGuides.Modes.getKeys()
    index = modes.index(CinematicGuides.CINEMATIC_GUIDES_MODE_OPTIONVAR.value)
    CinematicGuides.CINEMATIC_GUIDES_MODE_OPTIONVAR.value = modes[(index + 1) % len(modes)]
    
    if CinematicEditorUtils.isVisible():
        CinematicEditorUtils.instance.cinematicEditorTimeline.refreshCinematicGuides()
    if ExporterWindow.isVisible():
        ExporterWindow.instance.refreshCurrentTab()
        
    cmds.refresh(force=True)
    
def getCurrentCamera():
    if CinematicEditorUtils.isVisible():
        currentShot = CinematicEditorUtils.instance.cinematicEditorTimeline.getCurrentShot()
        if currentShot:
            camera = currentShot.camera
            if camera:
                return camera
    
    # Fallback to select the current viewport's camera
    viewport = cmds.playblast(activeEditor=True)
    if viewport:
        camera = cmds.modelEditor(viewport, q=True, camera=True)
        if cmds.nodeType(camera) == "camera":
            camera = cmds.listRelatives(camera, parent=True)[0]
    return camera
    
def selectCurrentCamera():
    camera = getCurrentCamera()
    if camera:
        cmds.select(camera)
    
def toggleCameraRotateInPlace():
    camera = getCurrentCamera()
    if camera:
        CinematicEditorUtils.setCameraPivotInPlaceMode(camera, not CinematicEditorUtils.isCameraPivotInPlaceMode(camera))
    
def toggleCameraFrustrums():
    CEConfiguration.CAMERA_FRUSTRUMS_ENABLED_OPTIONVAR.value = not CEConfiguration.CAMERA_FRUSTRUMS_ENABLED_OPTIONVAR.value
    
    cmds.refresh(force=True)

#---------------------------------
#|           Commands            |
#---------------------------------

def register():
    cmds.runTimeCommand("FrameCurrentShot",             cat="MSE Commands.Cinematic Editor",    ann="Applies the animation range of the current Shot.", c="import CustomCommands.CinematicEditorCommands as C; C.frameCurrentShot()", default=True)
    cmds.runTimeCommand("FrameSelectedShots",           cat="MSE Commands.Cinematic Editor",    ann="Applies the animation range of the selected Shots.", c="import CustomCommands.CinematicEditorCommands as C; C.frameSelectedShots()", default=True)
    cmds.runTimeCommand("FrameAllShots",                cat="MSE Commands.Cinematic Editor",    ann="Applies the combined animation range of all the Shots", c="import CustomCommands.CinematicEditorCommands as C; C.frameAllShots()", default=True)
    cmds.runTimeCommand("ToggleAutoFrameShots",         cat="MSE Commands.Cinematic Editor",    ann="Toggles wether or not to apply the animation range when the current Shot is changed.", c="import CustomCommands.CinematicEditorCommands as C; C.toggleAutoFrameShots()", default=True)
    
    cmds.runTimeCommand("PlayCutscene",                 cat="MSE Commands.Cinematic Editor",    ann="Starts playing the cutscene from the current frame. If the cutscene is zoomed, the zoomed range will be played.", c="import CustomCommands.CinematicEditorCommands as C; C.playCutscene()", default=True)
    cmds.runTimeCommand("NextCutsceneFramePress",       cat="MSE Commands.Cinematic Editor",    ann="Advances to the next cutscene frame, changing shots if necessary. Hold to keep advancing. Assign this command to a key on press and NextCutsceneFrameRelease to the same key on release.", c="import CustomCommands.CinematicEditorCommands as C; C.nextCutsceneFrameRepeatCommand.onCommandPressed()", default=True)
    cmds.runTimeCommand("NextCutsceneFrameRelease",     cat="MSE Commands.Cinematic Editor",    ann="Release command for the NextCutsceneFramePress command. Assign this to the same key on release.", c="import CustomCommands.CinematicEditorCommands as C; C.nextCutsceneFrameRepeatCommand.onCommandReleased()", default=True)
    cmds.runTimeCommand("PreviousCutsceneFramePress",   cat="MSE Commands.Cinematic Editor",    ann="Rewinds to the previous cutscene frame, changing shots if necessary. Hold to keep rewinding. Assign this command to a key on press and PreviousCutsceneFrameRelease to the same key on release.", c="import CustomCommands.CinematicEditorCommands as C; C.previousCutsceneFrameRepeatCommand.onCommandPressed()", default=True)
    cmds.runTimeCommand("PreviousCutsceneFrameRelease", cat="MSE Commands.Cinematic Editor",    ann="Release command for the PreviousCutsceneFramePress command. Assign this to the same key on release.", c="import CustomCommands.CinematicEditorCommands as C; C.previousCutsceneFrameRepeatCommand.onCommandReleased()", default=True)
    cmds.runTimeCommand("NextShot",                     cat="MSE Commands.Cinematic Editor",    ann="Moves to the beginning of the next shot in the cutscene.", c="import CustomCommands.CinematicEditorCommands as C; C.nextShot()", default=True)
    cmds.runTimeCommand("PreviousShot",                 cat="MSE Commands.Cinematic Editor",    ann="Moves to the end of the previous shot in the cutscene.", c="import CustomCommands.CinematicEditorCommands as C; C.previousShot()", default=True)
    
    cmds.runTimeCommand("ToggleRules",                  cat="MSE Commands.Cinematic Editor",    ann="Enables or disables the Cinematic Guides.", c="import CustomCommands.CinematicEditorCommands as C; C.toggleRules()", default=True)
    cmds.runTimeCommand("SwitchRules",                  cat="MSE Commands.Cinematic Editor",    ann="Switches between the different Cinematic Guides modes.", c="import CustomCommands.CinematicEditorCommands as C; C.switchRules()", default=True)
    
    cmds.runTimeCommand("SelectCurrentCamera",          cat="MSE Commands.Camera",              ann="Select the current viewport's camera. If the Cinematic Editor is opened, this command will select the current Shot's camera instead.", c="import CustomCommands.CinematicEditorCommands as C; C.selectCurrentCamera()", default=True)
    cmds.runTimeCommand("ToggleCameraRotateInPlace",    cat="MSE Commands.Camera",              ann="Toggles between rotating the current camera", c="import CustomCommands.CinematicEditorCommands as C; C.toggleCameraRotateInPlace()", default=True)
    cmds.runTimeCommand("ToggleCameraFrustrums",        cat="MSE Commands.Camera",              ann="Enables or disables the camera frustrums.", c="import CustomCommands.CinematicEditorCommands as C; C.toggleCameraFrustrums()", default=True)
    