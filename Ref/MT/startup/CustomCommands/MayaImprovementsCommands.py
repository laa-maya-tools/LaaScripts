import maya.cmds as cmds

def register():
    cmds.runTimeCommand("SetKeyFiltered", cat="MSE Commands.Maya Improvements", ann="Set Key on the filtered animation curves from the MayaImprovements tool.", c="import TimeSlider; timeSliderSelectionList = cmds.timeControl(TimeSlider.defaultTimeSlider, q=True, mainListConnection=True); maya.mel.eval(\"performSetKeyframeArgList 1 {{\\\"0\\\", \\\"{}\\\"}};\".format(timeSliderSelectionList))", default=True)
