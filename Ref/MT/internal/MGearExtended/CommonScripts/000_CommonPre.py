import pymel.core as pm

import RigUtils.Core        as RigCore
import RigUtils.Transforms  as RigTransforms
import OrganiLayers

# This Script is in charge of:
# - Deleting all constraints of the DC_Root hierarchy [Disabled]
# - Cleaning all the Controller Tags
# - Clean all OrganiLayers
# - Setting nice (-180 / 180) orientations for the export skeleton joints that may have weird values

# Clean Skeleton Constraints
# RigCore.DeleteConstraints("DC_Root", True)

# Clean Tags
tags = pm.ls(type="controller")
if (tags):
    pm.delete(tags)

# Clean OrganiLayers Nodes
OrganiLayers.CleanAllNodesInScene()

# Clean Skeleton rotations
# (When creating orient constraints with maintain offset ON Maya can add
# a full rotation each time and that rotation adds up on the bone transforms)
print("\n############## Setting nice joint orient values ##############")
if (pm.objExists("DC_Root")):
    totalChanged = RigTransforms.SetNiceOrient(pm.PyNode("DC_Root"), recursive=True, verbose=True)
    print("Total orientations changed: {}".format(totalChanged))
    print("##############  ##############\n")

# Final Print
print("*********************** Common Pre Finalized!!! ***********************")