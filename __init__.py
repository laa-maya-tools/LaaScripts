# Fixes an error with the channelbox
import maya.cmds as cmd

cmd.optionVar(intValue=('containerSelRootsInOutliner', True))
cmd.optionVar(intValue=('containerChanBoxMaxWithTemplate', 10))
cmd.optionVar(intValue=('containerChanBoxMaxNoTemplate', 10))
cmd.optionVar(intValue=('containerFlatViewCap', 10))
