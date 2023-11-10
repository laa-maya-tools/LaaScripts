# Autodesk help:
# https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/Maya-DataExchange/files/GUID-335F2172-DD4D-4D79-B969-55238C08F2EF-htm.html

import os
import maya.cmds as cmds
#import maya.mel as mel
#from pymel.core import mel

# ---------------------------------------------------------
# ------------------------ Classes ------------------------

# ----------- FBX SETTINGS AVAILABLE -----------
# As extracted from: cmds.FBXProperties()
class FBXSettings():
    class Import():
        class IncludeGrp():
            mergeMode = "Import|IncludeGrp|MergeMode"
            class MergeMode():
                kAdd            = "Add"
                kAddAndUpdate   = "Add and update animation"
                kUpdate         = "Update animation"
            
            class Geometry():
                unlockNormals   = "Import|IncludeGrp|Geometry|UnlockNormals"
                hardEdges       = "Import|IncludeGrp|Geometry|HardEdges"
                blindData       = "Import|IncludeGrp|Geometry|BlindData"
            
            class Animation():
                animation   = "Import|IncludeGrp|Animation"
                curveFilter = "Import|IncludeGrp|Animation|CurveFilter"
                samplingRateSelector    = "Import|IncludeGrp|Animation|SamplingPanel|SamplingRateSelector"
                curveFilterSamplingRate = "Import|IncludeGrp|Animation|SamplingPanel|CurveFilterSamplingRate"
                constraint              = "Import|IncludeGrp|Animation|ConstraintsGrp|Constraint"
                characterType           = "Import|IncludeGrp|Animation|ConstraintsGrp|Constraint"
                class SamplingRateSelector():
                    kScene  = "Scene"
                    kFile   = "File"
                    kCustom = "Custom"
                class CharacterType():
                    kNone       = "None"
                    kHumanIK    = "HumanIK"
                    
                
                class ExtraOptions():
                    take                = "Import|IncludeGrp|Animation|ExtraGrp|Take"
                    timeLine            = "Import|IncludeGrp|Animation|ExtraGrp|TimeLine"
                    bakeAnimationLayers = "Import|IncludeGrp|Animation|ExtraGrp|BakeAnimationLayers"
                    markers             = "Import|IncludeGrp|Animation|ExtraGrp|Markers"
                    quaternion          = "Import|IncludeGrp|Animation|ExtraGrp|Quaternion"
                    protectDrivenKeys   = "Import|IncludeGrp|Animation|ExtraGrp|ProtectDrivenKeys"
                    deformNullsAsJoints = "Import|IncludeGrp|Animation|ExtraGrp|DeformNullsAsJoints"
                    nullsToPivot        = "Import|IncludeGrp|Animation|ExtraGrp|NullsToPivot"
                    pointCache          = "Import|IncludeGrp|Animation|ExtraGrp|PointCache"
                    class Quaternion():
                        kRetainQuaternionInterpolation = "Retain Quaternion Interpolation"
                        kSetAsEulerInterpolation = "Set As Euler Interpolation"
                        kResampleAsEulerInterpolation = "Resample As Euler Interpolation" 
                
                class Deformation():
                    deformation             = "Import|IncludeGrp|Animation|Deformation"
                    skins                   = "Import|IncludeGrp|Animation|Deformation|Skins"
                    shape                   = "Import|IncludeGrp|Animation|Deformation|Shape"
                    ForceWeightNormalize    = "Import|IncludeGrp|Animation|Deformation|ForceWeightNormalize"
                
            class Cameras():
                cameras = "Import|IncludeGrp|CameraGrp|Camera"
                
            class Lights():
                lights = "Import|IncludeGrp|LightGrp|Light"
                
            class Audio():
                audio = "Import|IncludeGrp|Audio"
        
        class AdvancedOptions():
            class Units():
                dynamicScaleConversion  = "Import|AdvOptGrp|UnitsGrp|DynamicScaleConversion"
                unitsSelector           = "Import|AdvOptGrp|UnitsGrp|UnitsSelector"
                class UnitsSelector():
                    kMillimeters = "Millimeters"
                    kCentimeters = "Centimeters"
                    kDecimeters = "Decimeters"
                    kMeters = "Meters"
                    kKilometers = "Kilometers"
                    kInches = "Inches"
                    kFeet = "Feet"
                    kYards = "Yards"
                    kMiles = "Miles"
            
            class AxisConversion():
                axisConversion  = "Import|AdvOptGrp|AxisConvGrp|AxisConversion"
                upAxis          = "Import|AdvOptGrp|AxisConvGrp|UpAxis"
                class UpAxis():
                    kY = "Y"
                    kZ = "Z"
            
            class UI():
                ShowWarningsManager = "Import|AdvOptGrp|UI|ShowWarningsManager"
                generateLogData     = "Import|AdvOptGrp|UI|GenerateLogData"
            
            class FileFormat():
                class Obj():
                    referenceNode = "Import|AdvOptGrp|FileFormat|Obj|ReferenceNode"
                
                class Max3DS():
                    referenceNode   = "Import|AdvOptGrp|FileFormat|Max_3ds|ReferenceNode"
                    texture         = "Import|AdvOptGrp|FileFormat|Max_3ds|Texture"
                    material        = "Import|AdvOptGrp|FileFormat|Max_3ds|Material"
                    animation       = "Import|AdvOptGrp|FileFormat|Max_3ds|Animation"
                    mesh            = "Import|AdvOptGrp|FileFormat|Max_3ds|Mesh"
                    light           = "Import|AdvOptGrp|FileFormat|Max_3ds|Light"
                    camera          = "Import|AdvOptGrp|FileFormat|Max_3ds|Camera"
                    ambientLight    = "Import|AdvOptGrp|FileFormat|Max_3ds|AmbientLight"
                    rescaling       = "Import|AdvOptGrp|FileFormat|Max_3ds|Rescaling"
                    filter          = "Import|AdvOptGrp|FileFormat|Max_3ds|Filter"
                    smoothgroup     = "Import|AdvOptGrp|FileFormat|Max_3ds|Smoothgroup"
                
                class MotionBase():
                    MotionFrameCount                = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionFrameCount"
                    MotionFrameRate                 = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionFrameRate"
                    MotionActorPrefix               = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionActorPrefix"
                    MotionRenameDuplicateNames      = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionRenameDuplicateNames"
                    MotionExactZeroAsOccluded       = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionExactZeroAsOccluded"
                    MotionSetOccludedToLastValidPos = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionSetOccludedToLastValidPos"
                    MotionAsOpticalSegments         = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionAsOpticalSegments"
                    MotionASFSceneOwned             = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionASFSceneOwned"
                    MotionUpAxisUsedInFile          = "Import|AdvOptGrp|FileFormat|Motion_Base|MotionUpAxisUsedInFile"
                
                class Biovision_BVH():
                    motionCreateReferenceNode = "Import|AdvOptGrp|FileFormat|Biovision_BVH|MotionCreateReferenceNode"
                
                class MotionAnalysis_HTR():
                    motionCreateReferenceNode   = "Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionCreateReferenceNode"
                    motionBaseTInOffset         = "Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionBaseTInOffset"
                    motionBaseRInPrerotation    = "Import|AdvOptGrp|FileFormat|MotionAnalysis_HTR|MotionBaseRInPrerotation"
                
                class Acclaim_ASF():
                    motionCreateReferenceNode   = "Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionCreateReferenceNode"
                    motionDummyNodes            = "Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionDummyNodes"
                    motionLimits                = "Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionLimits"
                    motionBaseTInOffset         = "Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionBaseTInOffset"
                    motionBaseRInPrerotation    = "Import|AdvOptGrp|FileFormat|Acclaim_ASF|MotionBaseRInPrerotation"
                
                class Acclaim_AMC():
                    motionCreateReferenceNode   = "Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionCreateReferenceNode"
                    motionDummyNodes            = "Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionDummyNodes"
                    motionLimits                = "Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionLimits"
                    motionBaseTInOffset         = "Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionBaseTInOffset"
                    motionBaseRInPrerotation    = "Import|AdvOptGrp|FileFormat|Acclaim_AMC|MotionBaseRInPrerotation"
            
            class Dxf():
                weldVertices        = "Import|AdvOptGrp|Dxf|WeldVertices"
                objectDerivation    = "Import|AdvOptGrp|Dxf|ObjectDerivation"
                referenceNode       = "Import|AdvOptGrp|Dxf|ReferenceNode"
                class ObjectDerivation():
                    kLayer  = "By layer"
                    kEntity = "By entity"
                    kBlock  = "By block"
    
    
    class Export():
        class Include():
            class Geometry():
                smoothingGroups =       "Export|IncludeGrp|Geometry|SmoothingGroups"
                splitPerVertexNormals = "Export|IncludeGrp|Geometry|expHardEdges"
                tangentsandBinormals =  "Export|IncludeGrp|Geometry|TangentsandBinormals"
                smoothMesh =            "Export|IncludeGrp|Geometry|SmoothMesh"
                selectionSets =         "Export|IncludeGrp|Geometry|SelectionSet"
                convertToNullObjects =  "Export|IncludeGrp|Geometry|BlindData"
                animationOnly =         "Export|IncludeGrp|Geometry|AnimationOnly"
                preserveInstances =     "Export|IncludeGrp|Geometry|Instances"
                referencedAssetsContent = "Export|IncludeGrp|Geometry|ContainerObjects"
                triangulate =           "Export|IncludeGrp|Geometry|Triangulate"
                convertNURBSSurfaceTo ="Export|IncludeGrp|Geometry|GeometryNurbsSurfaceAs"
                class ConvertNURBSSurfaceTo():
                    kNurbs = "NURBS"
                    kInteractiveDisplayMesh = "Interactive Display Mesh"
                    kSoftwareRenderMesh = "Software Render Mesh"
            
            class Animation():
                animation = "Export|IncludeGrp|Animation"
                
                class ExtraOptions():
                    useSceneName =                  "Export|IncludeGrp|Animation|ExtraGrp|UseSceneName"
                    removeSingleKey =               "Export|IncludeGrp|Animation|ExtraGrp|RemoveSingleKey"
                    quaternionInterpolationMode =   "Export|IncludeGrp|Animation|ExtraGrp|Quaternion"
                    class QuaternionInterpolationMode():
                        kRetainQuaternionInterpolation = "Retain Quaternion Interpolation"
                        kSetAsEulerInterpolation = "Set As Euler Interpolation"
                        kResampleAsEulerInterpolation = "Resample As Euler Interpolation" 
                        
                
                class BakeAnimation():
                    bakeAnimation = "Export|IncludeGrp|Animation|BakeComplexAnimation"
                    start =         "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStart"
                    end =           "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameEnd"
                    step =          "Export|IncludeGrp|Animation|BakeComplexAnimation|BakeFrameStep"
                    resampleAll =   "Export|IncludeGrp|Animation|BakeComplexAnimation|ResampleAnimationCurves"
                    hideAnimationBakedWarning =   "Export|IncludeGrp|Animation|BakeComplexAnimation|HideComplexAnimationBakedWarning"
                
                class DeformedModels():
                    deformedModels ="Export|IncludeGrp|Animation|Deformation"
                    skins =         "Export|IncludeGrp|Animation|Deformation|Skins"
                    blendShapes =   "Export|IncludeGrp|Animation|Deformation|Shape"
                    class BlendShapeOptions():
                        shapeAttribute =    "Export|IncludeGrp|Animation|Deformation|ShapeAttributes"
                        attributeValues =   "Export|IncludeGrp|Animation|Deformation|ShapeAttributes|ShapeAttributesValues"
                        class AttributeValues():
                            kRelative = "Relative"
                            kAbsolute  = "Absolute" 
                
                class CurveFilters():
                    curveFilters = "Export|IncludeGrp|Animation|CurveFilter"
                    class ConstantKeyReducer():
                        constantKeyReducer =    "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed"
                        translationPrecision =  "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedTPrec"
                        rotationPrecision =     "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedRPrec"
                        scalingPrecision =      "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedSPrec"
                        otherPrecision =        "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|CurveFilterCstKeyRedOPrec"
                        autoTangentsOnly =      "Export|IncludeGrp|Animation|CurveFilter|CurveFilterApplyCstKeyRed|AutoTangentsOnly"
                
                class GeometryCacheFiles():
                    geometryCacheFiles = "Export|IncludeGrp|Animation|PointCache"
                
                class Constraints():
                    constraints =           "Export|IncludeGrp|Animation|ConstraintsGrp|Constraint"
                    skeletonDefinitions =   "Export|IncludeGrp|Animation|ConstraintsGrp|Character"
            
            class Cameras():
                cameras = "Export|IncludeGrp|CameraGrp|Camera"
            
            class Lights():
                lights = "Export|IncludeGrp|LightGrp|Light"
            
            class Audio():
                audio = "Export|IncludeGrp|Audio"
            
            class EmbedMedia():
                embedMedia = "Export|IncludeGrp|EmbedTextureGrp|EmbedTexture"
            
            class BindPose():
                bindPose = "Export|IncludeGrp|BindPose"
            
            class PivotToNulls():
                pivotToNulls = "Export|IncludeGrp|PivotToNulls"
            
            class BypassRrsInheritance():
                bypassRrsInheritance = "Export|IncludeGrp|BypassRrsInheritance"
            
            class Connections():
                includeChildren =   "Export|IncludeGrp|InputConnectionsGrp|IncludeChildren"
                inputConnections =  "Export|IncludeGrp|InputConnectionsGrp|InputConnections"
        
        class AdvancedOptions():
            class Units():
                automatic =             "Export|AdvOptGrp|UnitsGrp|DynamicScaleConversion"
                fileUnitsConvertedTo =  "Export|AdvOptGrp|UnitsGrp|UnitsSelector"
                class FileUnitsConvertedTo():
                    kMillimeters = "Millimeters"
                    kCentimeters = "Centimeters"
                    kDecimeters = "Decimeters"
                    kMeters = "Meters"
                    kKilometers = "Kilometers"
                    kInches = "Inches"
                    kFeet = "Feet"
                    kYards = "Yards"
                    kMiles = "Miles"
            
            class AxisConversion():
                upAxis = "Export|AdvOptGrp|AxisConvGrp|UpAxis"
                class UpAxis():
                    kY = "Y"
                    kZ = "Z"
            
            class UI():
                showWarningManager =    "Export|AdvOptGrp|UI|ShowWarningsManager"
                generateLogData =       "Export|AdvOptGrp|UI|GenerateLogData"
            
            class FileFormat():
                class Obj():
                    triangulate = "Export|AdvOptGrp|FileFormat|Obj|Triangulate"
                    deformation = "Export|AdvOptGrp|FileFormat|Obj|Deformation"
                
                class MotionBase():
                    motionFrameCount =          "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameCount"
                    motionFromGlobalPosition =  "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFromGlobalPosition"
                    motionFrameRate =           "Export|AdvOptGrp|FileFormat|Motion_Base|MotionFrameRate"
                    motionGapsAsValidData =     "Export|AdvOptGrp|FileFormat|Motion_Base|MotionGapsAsValidData"
                    motionC3DRealFormat =       "Export|AdvOptGrp|FileFormat|Motion_Base|MotionC3DRealFormat"
                    motionASFSceneOwned =       "Export|AdvOptGrp|FileFormat|Motion_Base|MotionASFSceneOwned"
                
                class Biovision_BVH():
                    motionTranslation = "Export|AdvOptGrp|FileFormat|Biovision_BVH|MotionTranslation"
                
                class AcclaimASF():
                    motionTranslation = "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionTranslation"
                    motionFrameRateUsed = "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRateUsed"
                    motionFrameRange = "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionFrameRange"
                    motionWriteDefaultAsBaseTR = "Export|AdvOptGrp|FileFormat|Acclaim_ASF|MotionWriteDefaultAsBaseTR"
                    motionTranslation = "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionTranslation"
                    motionFrameRateUsed = "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionFrameRateUsed"
                    motionWriteDefaultAsBaseTR = "Export|AdvOptGrp|FileFormat|Acclaim_AMC|MotionWriteDefaultAsBaseTR"
            
            class FBXFileFormat():
                fileType =  "Export|AdvOptGrp|Fbx|AsciiFbx"
                version =   "Export|AdvOptGrp|Fbx|ExportFileVersion"
                class FileType():
                    kBinary = "Binary"
                    kASCII = "ASCII"
                class Version():
                    kFBX202000 = "FBX202000"
                    kFBX201900 = "FBX201900"
                    kFBX201800 = "FBX201800"
                    kFBX201600 = "FBX201600"
                    kFBX201400 = "FBX201400"
                    kFBX201300 = "FBX201300"
                    kFBX201200 = "FBX201200"
                    kFBX201100 = "FBX201100"
                    kFBX201000 = "FBX201000"
                    kFBX200900 = "FBX200900"
                    kFBX200611 = "FBX200611"
            
            class Dxf():
                deformation = "Export|AdvOptGrp|Dxf|Deformation"
                triangulate = "Export|AdvOptGrp|Dxf|Triangulate"
            
            class Collada():
                trinagulate =   "Export|AdvOptGrp|Collada|Triangulate"
                singleMatrix =  "Export|AdvOptGrp|Collada|SingleMatrix"
                frameRate =     "Export|AdvOptGrp|Collada|FrameRate"

# ----------- GENERAL PRESET CLASS -----------
class FBXPreset():
    def __init__(self, baseDict={}):
        self.__Dict = baseDict
    
    def SetProperties(self, dict):
        for (k,v) in dict.items():
            self.SetProperty(k,v)
    
    def SetProperty(self, key, val):
        if (key in self.__Dict.keys()):
            self.__Dict[key] = val
        else:
            raise Exception("Key not found: {}".format(key))
    
    def GetProperty(self, key):
        if (key in self.__Dict.keys()):
            return self.__Dict[key]
        else:
            raise Exception("Key not found: {}".format(key))
    
    def Keys(self):
        return self.__Dict.keys()
    
    def PrintValues(self):
        for k in self.__Dict.keys():
            print("{} = {}".format(k, self.__Dict[k]))

# ----------- IMPORT PRESET CLASS -----------
class FBXImportPreset(FBXPreset):
    def __init__(self, inDict=None):
        super().__init__({
            FBXSettings.Import.IncludeGrp.mergeMode : FBXSettings.Import.IncludeGrp.MergeMode.kAdd,
            
            FBXSettings.Import.IncludeGrp.Geometry.unlockNormals : 0,
            FBXSettings.Import.IncludeGrp.Geometry.hardEdges : 0,
            FBXSettings.Import.IncludeGrp.Geometry.blindData : 0,
            
            FBXSettings.Import.IncludeGrp.Animation.animation : 0,
            FBXSettings.Import.IncludeGrp.Animation.curveFilter : 0,
            FBXSettings.Import.IncludeGrp.Animation.samplingRateSelector : FBXSettings.Import.IncludeGrp.Animation.SamplingRateSelector.kScene,
            FBXSettings.Import.IncludeGrp.Animation.curveFilterSamplingRate : 30.0,
            FBXSettings.Import.IncludeGrp.Animation.constraint : 0,
            FBXSettings.Import.IncludeGrp.Animation.characterType : FBXSettings.Import.IncludeGrp.Animation.CharacterType.kHumanIK,
            
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.take : "No Animation",
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.timeLine : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.bakeAnimationLayers : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.markers : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.quaternion : FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.Quaternion.kRetainQuaternionInterpolation,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.protectDrivenKeys : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.deformNullsAsJoints : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.nullsToPivot : 0,
            FBXSettings.Import.IncludeGrp.Animation.ExtraOptions.pointCache : 0,
            
            FBXSettings.Import.IncludeGrp.Animation.Deformation.deformation : 0,
            FBXSettings.Import.IncludeGrp.Animation.Deformation.skins : 0,
            FBXSettings.Import.IncludeGrp.Animation.Deformation.shape : 0,
            FBXSettings.Import.IncludeGrp.Animation.Deformation.ForceWeightNormalize : 0,
            
            FBXSettings.Import.IncludeGrp.Cameras.cameras : 0,
            FBXSettings.Import.IncludeGrp.Lights.lights : 0,
            FBXSettings.Import.IncludeGrp.Audio.audio : 0,
            
            FBXSettings.Import.AdvancedOptions.Units.dynamicScaleConversion : 0,
            FBXSettings.Import.AdvancedOptions.Units.unitsSelector : FBXSettings.Import.AdvancedOptions.Units.UnitsSelector.kCentimeters,
            
            FBXSettings.Import.AdvancedOptions.AxisConversion.axisConversion : 0,
            FBXSettings.Import.AdvancedOptions.AxisConversion.upAxis : FBXSettings.Import.AdvancedOptions.AxisConversion.UpAxis.kY,
            
            FBXSettings.Import.AdvancedOptions.UI.ShowWarningsManager : 0,
            FBXSettings.Import.AdvancedOptions.UI.generateLogData : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.Obj.referenceNode : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.referenceNode : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.texture : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.material : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.animation : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.mesh : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.light : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.camera : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.ambientLight : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.rescaling : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.filter : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Max3DS.smoothgroup : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionFrameCount : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionFrameRate : 0.0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionActorPrefix : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionRenameDuplicateNames : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionExactZeroAsOccluded : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionSetOccludedToLastValidPos : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionAsOpticalSegments : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionASFSceneOwned : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionBase.MotionUpAxisUsedInFile : 3,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.Biovision_BVH.motionCreateReferenceNode : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionAnalysis_HTR.motionCreateReferenceNode : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionAnalysis_HTR.motionBaseTInOffset : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.MotionAnalysis_HTR.motionBaseRInPrerotation : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_ASF.motionCreateReferenceNode : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_ASF.motionDummyNodes : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_ASF.motionLimits : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_ASF.motionBaseTInOffset : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_ASF.motionBaseRInPrerotation : 0,
            
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_AMC.motionCreateReferenceNode : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_AMC.motionDummyNodes : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_AMC.motionLimits : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_AMC.motionBaseTInOffset : 0,
            FBXSettings.Import.AdvancedOptions.FileFormat.Acclaim_AMC.motionBaseRInPrerotation : 0,
            
            FBXSettings.Import.AdvancedOptions.Dxf.weldVertices : 0,
            FBXSettings.Import.AdvancedOptions.Dxf.objectDerivation : FBXSettings.Import.AdvancedOptions.Dxf.ObjectDerivation.kLayer,
            FBXSettings.Import.AdvancedOptions.Dxf.referenceNode : 0
        })
        
        if (inDict):
            self.SetProperties(inDict)

# ----------- EXPORT PRESET CLASS -----------
class FBXExportPreset(FBXPreset):
    def __init__(self, inDict=None):
        super().__init__({
            FBXSettings.Export.Include.Geometry.smoothingGroups : 0,
            FBXSettings.Export.Include.Geometry.splitPerVertexNormals : 0,
            FBXSettings.Export.Include.Geometry.tangentsandBinormals : 0,
            FBXSettings.Export.Include.Geometry.smoothMesh : 0,
            FBXSettings.Export.Include.Geometry.selectionSets : 0,
            FBXSettings.Export.Include.Geometry.convertToNullObjects : 0,
            FBXSettings.Export.Include.Geometry.animationOnly : 0,
            FBXSettings.Export.Include.Geometry.preserveInstances : 0,
            FBXSettings.Export.Include.Geometry.referencedAssetsContent : 0,
            FBXSettings.Export.Include.Geometry.triangulate : 0,
            FBXSettings.Export.Include.Geometry.convertNURBSSurfaceTo : FBXSettings.Export.Include.Geometry.ConvertNURBSSurfaceTo.kNurbs,
            
            FBXSettings.Export.Include.Animation.animation : 0,
            FBXSettings.Export.Include.Animation.ExtraOptions.useSceneName : 0,
            FBXSettings.Export.Include.Animation.ExtraOptions.removeSingleKey : 0,
            FBXSettings.Export.Include.Animation.ExtraOptions.quaternionInterpolationMode : FBXSettings.Export.Include.Animation.ExtraOptions.QuaternionInterpolationMode.kRetainQuaternionInterpolation,
            FBXSettings.Export.Include.Animation.BakeAnimation.bakeAnimation : 0,
            FBXSettings.Export.Include.Animation.BakeAnimation.start : 1,
            FBXSettings.Export.Include.Animation.BakeAnimation.end : 200,
            FBXSettings.Export.Include.Animation.BakeAnimation.step : 1,
            FBXSettings.Export.Include.Animation.BakeAnimation.resampleAll : 0,
            FBXSettings.Export.Include.Animation.BakeAnimation.hideAnimationBakedWarning: 0,
            FBXSettings.Export.Include.Animation.DeformedModels.deformedModels : 0,
            FBXSettings.Export.Include.Animation.DeformedModels.skins : 0,
            FBXSettings.Export.Include.Animation.DeformedModels.blendShapes : 0,
            FBXSettings.Export.Include.Animation.DeformedModels.BlendShapeOptions.shapeAttribute : 0,
            FBXSettings.Export.Include.Animation.DeformedModels.BlendShapeOptions.attributeValues : FBXSettings.Export.Include.Animation.DeformedModels.BlendShapeOptions.AttributeValues.kRelative,
            FBXSettings.Export.Include.Animation.CurveFilters.curveFilters : 0,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.constantKeyReducer : 0,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.translationPrecision : 0.0001,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.rotationPrecision : 0.0090,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.scalingPrecision : 0.0040,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.otherPrecision : 0.0090,
            FBXSettings.Export.Include.Animation.CurveFilters.ConstantKeyReducer.autoTangentsOnly : 0,
            
            FBXSettings.Export.Include.Animation.GeometryCacheFiles.geometryCacheFiles : 0,
            FBXSettings.Export.Include.Animation.Constraints.constraints : 0,
            FBXSettings.Export.Include.Animation.Constraints.skeletonDefinitions : 0,
            
            FBXSettings.Export.Include.Cameras.cameras : 0,
            
            FBXSettings.Export.Include.Lights.lights : 0,
            
            FBXSettings.Export.Include.Audio.audio : 0,
            
            FBXSettings.Export.Include.EmbedMedia.embedMedia : 0,
            
            FBXSettings.Export.Include.BindPose.bindPose: 0,
            FBXSettings.Export.Include.PivotToNulls.pivotToNulls: 0,
            FBXSettings.Export.Include.BypassRrsInheritance.bypassRrsInheritance: 0,
            
            FBXSettings.Export.Include.Connections.includeChildren : 0,
            FBXSettings.Export.Include.Connections.inputConnections : 0,
            
            FBXSettings.Export.AdvancedOptions.Units.automatic : 0,
            FBXSettings.Export.AdvancedOptions.Units.fileUnitsConvertedTo : FBXSettings.Export.AdvancedOptions.Units.FileUnitsConvertedTo.kCentimeters,
            
            FBXSettings.Export.AdvancedOptions.AxisConversion.upAxis : FBXSettings.Export.AdvancedOptions.AxisConversion.UpAxis.kY,
            
            FBXSettings.Export.AdvancedOptions.UI.showWarningManager : 0,
            FBXSettings.Export.AdvancedOptions.UI.generateLogData : 0,
            
            FBXSettings.Export.AdvancedOptions.FileFormat.Obj.triangulate : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.Obj.deformation : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionFrameCount : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionFromGlobalPosition : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionFrameRate : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionGapsAsValidData : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionC3DRealFormat : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.MotionBase.motionASFSceneOwned : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.Biovision_BVH.motionTranslation : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionTranslation : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionFrameRateUsed : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionFrameRange : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionWriteDefaultAsBaseTR : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionTranslation : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionFrameRateUsed : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionFrameRange : 0,
            FBXSettings.Export.AdvancedOptions.FileFormat.AcclaimASF.motionWriteDefaultAsBaseTR : 0,
            
            FBXSettings.Export.AdvancedOptions.FBXFileFormat.fileType : FBXSettings.Export.AdvancedOptions.FBXFileFormat.FileType.kBinary,
            FBXSettings.Export.AdvancedOptions.FBXFileFormat.version : FBXSettings.Export.AdvancedOptions.FBXFileFormat.Version.kFBX202000,
            
            FBXSettings.Export.AdvancedOptions.Dxf.deformation : 0,
            FBXSettings.Export.AdvancedOptions.Dxf.triangulate : 0,
            
            FBXSettings.Export.AdvancedOptions.Collada.trinagulate : 0,
            FBXSettings.Export.AdvancedOptions.Collada.singleMatrix : 0,
            FBXSettings.Export.AdvancedOptions.Collada.frameRate : 0
        })
        
        if (inDict):
            self.SetProperties(inDict)


# ---------------------------------------------------------
# ----------------------- Functions -----------------------
def SetProperty(setting, value, verbose=False):
    try:
        cmds.FBXProperty(setting, "-v", value)
    except:
        if verbose:
            print("WARNING: Could not set FBX Property: {}. Input Value: {}".format(setting, value))

def GetProperty(setting):
    cmds.FBXProperty(setting, "-q")

def LoadPreset(exportPreset, verbose=False):
    for k in exportPreset.Keys():
        v = exportPreset.GetProperty(k)
        SetProperty(k, v, verbose)

def LoadExportPresetFile(filePath):
    filePath = filePath.lower()
    if (os.path.isfile(filePath) and filePath.endswith(".fbxexportpreset")):
        cmds.FBXLoadExportPresetFile('-f', filePath)
    else:
        raise Exception("FBX preset file does not exists: \n{}".format(filePath))

def ClearFBXSettings():
    #Load a Default 'empty' preset
    LoadPreset(FBXImportPreset())
    LoadPreset(FBXExportPreset())

def ImportFBX(filePath):
    cmds.FBXImport('-file', filePath)

def ExportFBX(filePath, exportObjs):
    # exportObjs is an array of nodes
    cmds.select(clear=True)
    cmds.select(exportObjs)
    filePath = filePath.replace("\\", "/")
    
    # Export command
    cmds.FBXExport('-file', filePath, '-s', True)
    
    cmds.select(clear=True)

#Export calls examples:
# for any reason, this line does not work anymore. WTF??
# Ok, the reason was: it stops working whan changing the Maya file dialog
# to the OS Native file dialog:
# https://forums.cgsociety.org/t/open-file-using-windows-native-export-file-using-maya-window/1584590
# cmds.file(filePath, force=True, type="FBX export", exportSelected=True)

# So, even this fuckery still does not work as intended, because it exports
# nodes that are not selected.
#mel.eval('FBXExport -f "{}" -s'.format(filePath))

# New try, with pymel... sigh
#mel.FBXExport(s=True, f=filePath)

# Finally, the reason why the controls were exported:
# This is neccesary because Maya suda p*llas of this configuration when
# set via FBX Settings
#cmds.FBXExportInputConnections('-v', False)
#cmds.FBXExportTriangulate("-v", True)