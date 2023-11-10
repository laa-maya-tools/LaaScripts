import maya.OpenMaya as OpenMaya
import maya.api.OpenMaya as OpenMaya2

AdditiveTransformNodeID             = OpenMaya.MTypeId(0x80100)
AdditiveTransformationMatrixID      = OpenMaya.MTypeId(0x80101)
NoiseFloatID                        = OpenMaya2.MTypeId(0x80102)
CameraFrustrumID                    = OpenMaya2.MTypeId(0x80103)

#OrganiLayers (Organization Layers)
OrganiLayerID                       = OpenMaya.MTypeId(0x80201)
OrganiItemID                        = OpenMaya.MTypeId(0x80202)
OrganiSetID                         = OpenMaya.MTypeId(0x80203)
InheritableDrawInfoID               = OpenMaya.MTypeId(0x80210)

#ActorManager
ActorManagerActorID                 = OpenMaya2.MTypeId(0x80300)
ActorManagerSubActorID              = OpenMaya2.MTypeId(0x80301)
ActorManagerAnimPresetID            = OpenMaya2.MTypeId(0x80302)
ActorManagerCameraSetID             = OpenMaya2.MTypeId(0x80303)
ActorManagerWeightedLayerID         = OpenMaya2.MTypeId(0x80304)

#PointHelper
PointLocatorID                      = OpenMaya2.MTypeId(0x80400)

#Custom Transform Nodes
MatrixMirrorID                      = OpenMaya2.MTypeId(0x80500)
ScaleFactorID                       = OpenMaya2.MTypeId(0x80501)
LookQuaternionID                    = OpenMaya2.MTypeId(0x80502) 
MatrixRowID                         = OpenMaya2.MTypeId(0x80503) 
AngleReactionID                     = OpenMaya2.MTypeId(0x80504) 
SpaceSwitcherID                     = OpenMaya2.MTypeId(0x80505) 

#CinematicEditor
CinematicEditorCutsceneID           = OpenMaya2.MTypeId(0x80600)
CinematicEditorShotID               = OpenMaya2.MTypeId(0x80601)
CinematicEditorCutsceneActorID      = OpenMaya2.MTypeId(0x80602)

#Custom Math Nodes
TrigonometricAngleID                = OpenMaya2.MTypeId(0x80700)
TrigonometricInverseAngleID         = OpenMaya2.MTypeId(0x80701)
Angle3PointID                       = OpenMaya2.MTypeId(0x80702)
FloatMathListID                     = OpenMaya2.MTypeId(0x80703)
Point3MathListID                    = OpenMaya2.MTypeId(0x80704)

#Screen Drawer
ScreenDrawerID                      = OpenMaya2.MTypeId(0x80800)

#Custom Keying Group
CustomKeyingGroupID                 = OpenMaya2.MTypeId(0x80900)

#Custom Manipulator
IKManipulatorID                     = OpenMaya2.MTypeId(0x80A00)
FKManipulatorID                     = OpenMaya2.MTypeId(0x80A01)

#Custom Manager Nodes
NodeCollectionID                    = OpenMaya2.MTypeId(0x80B00)
CustomCollectionID                  = OpenMaya2.MTypeId(0x80B01)

#Rig Test (WIP)
RigBipedLimbFigureModeID            = OpenMaya2.MTypeId(0x80C00)
RigBipedLimbID                      = OpenMaya2.MTypeId(0x80C01)

#Rig Manager
RigManagerRigID                     = OpenMaya2.MTypeId(0x80D00)
RigManagerRigChainID                = OpenMaya2.MTypeId(0x80A02)    # Previously under another category, keeps it's ID
