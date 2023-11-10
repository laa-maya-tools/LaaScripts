import pymel.core as pm

import RigUtils.MultiConfigLoader   as RigCfg
import RigUtils.Transforms          as RigTransforms
import ControllerTagManager as ctm

# This Script is in charge of:
# - Setting mGear joints visibility to false
# - Setting the controls visibility on playback for mGear
# - Setting nice (-180 / 180) orientations for the export skeleton orient constraints that may have weird values
# - Import Default configurations (like KeyingGroups, OrganiLayers, CustomTags...)
# - Clean any selection

# Visibility Options
pm.setAttr('rig.ctl_vis_on_playback', 0)
pm.setAttr('rig.jnt_vis', 0)

# Clean/set nice orient values on orient constraints
if (pm.objExists("DC_Root")):
    skeletonOrientCnss = RigTransforms.GetHierarchyConstraints(pm.PyNode("DC_Root"), orient=True)
    print("\n############## Setting nice orient offset values ##############")
    for orientCns in skeletonOrientCnss:
        RigTransforms.SetOrientConstraintNiceOffsets(orientCns, verbose=True)
    print("##############  ##############\n")

# Import Config Files
pm.evalDeferred("import RigUtils.MultiConfigLoader as RigCfg\nRigCfg.ImportFileDefaultConfigs()")

# Clean invalid Controller Tags (mGear may crash if it finds one without any node set as controller)
invalidControllerTags = ctm.GetInvalidTags()
pm.delete(invalidControllerTags)

# Clear Selection
pm.select(cl=True)

# Final Print
print("*********************** Common Post Finalized!!! ***********************")