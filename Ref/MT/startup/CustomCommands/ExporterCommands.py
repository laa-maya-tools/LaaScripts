import maya.cmds as cmds

import ExporterWindow as EW

#---------------------------------
#|          Functions            |
#---------------------------------

# ---- Animation Tab ----

def frameSelectedAnimations():
    if EW.isVisible():
        animWidgets = EW.instance.animationTab.getSelectedAnimWidgets()
        EW.instance.animationTab.applyAnimationConfiguration(animWidgets, animRange=True, animLayers=False)

def frameAllAnimations():
    if EW.isVisible():
        animWidgets = EW.instance.animationTab.getAnimWidgets()
        animWidgets = [animWidget for animWidget in animWidgets if animWidget.animPreset.enabled]
        EW.instance.animationTab.applyAnimationConfiguration(animWidgets, animRange=True, animLayers=False)

#---------------------------------
#|           Commands            |
#---------------------------------

def register():
    # ---- Animation Tab ----
    cmds.runTimeCommand("FrameSelectedAnimations",  cat="MSE Commands.Exporter.Animation",    ann="Applies the animation range of the selected AnimPresets.", c="import CustomCommands.ExporterCommands as C; C.frameSelectedAnimations()", default=True)
    cmds.runTimeCommand("FrameAllAnimations",       cat="MSE Commands.Exporter.Animation",    ann="Applies the combined animation range of all the AnimPresets", c="import CustomCommands.ExporterCommands as C; C.frameAllAnimations()", default=True)
    