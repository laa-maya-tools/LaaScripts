# coding: utf-8

import maya.api.OpenMaya as OpenMaya
import maya.api.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaRender as OpenMayaRender

import maya.cmds as cmds

import AnimSystems.IKManipulator as ManipulatorCommon
from AnimSystems.IKManipulator import IKManipulatorController
from AnimSystems.IKManipulator import FKManipulatorController
from RigManager.IKFKChain import IKFKChain

import Utils.OpenMaya.ApiUndo as ApiUndo
import Utils.OpenMaya.Geometry as GeometryUtils
import Utils.OpenMaya as OpenMayaUtils
import Utils.Maya as MayaUtils
import Utils.Python.Math as MathUtils
import NodeID

import sys
import math

# Maya API 2.Functions required to use
def maya_useNewAPI():
    pass


def getNodeWorldRotation(nodePath):
    matrix = OpenMaya.MTransformationMatrix(nodePath.inclusiveMatrix())
    return matrix.rotation(asQuaternion=True)

def getNodeWorldTranslation(nodePath):
    matrix = OpenMaya.MTransformationMatrix(nodePath.inclusiveMatrix())
    return OpenMaya.MPoint(matrix.translation(OpenMaya.MSpace.kWorld))

def getCameraZoomRatio(cameraPath, targetPoint, viewportWidth=1200): # The size of the controls depend on the viewport width. All metrics have been taken on a 1200 px viewport.
    cameraFn = OpenMaya.MFnDependencyNode(cameraPath.node())
    isOrtho = cameraFn.findPlug("orthographic", False).asBool()
    if isOrtho:
        orthoWidth = cameraFn.findPlug("orthographicWidth", False).asFloat()
        zoomRatio = math.ldexp(orthoWidth, 3) * 0.0035
    else:
        matrix = OpenMaya.MTransformationMatrix(cameraPath.inclusiveMatrix())
        cameraPosition = OpenMaya.MPoint(matrix.translation(OpenMaya.MSpace.kWorld))
        cameraDirection = OpenMaya.MVector(0, 0, -1).rotateBy(matrix.rotation(asQuaternion=True))
        projection = cameraPosition + ((targetPoint - cameraPosition) * cameraDirection) * cameraDirection
        
        cameraFov = cameraFn.findPlug("focalLength", False).asFloat()
        horizontalFilmAperture = cameraFn.findPlug("horizontalFilmAperture", False).asFloat()
        apertureRatio = horizontalFilmAperture / 1.5   # Calculations have been made with a 1.5 aspect ratio
        zoomRatio = projection.distanceTo(cameraPosition) * apertureRatio / cameraFov
        
    zoomRatio *= 1200.0 / viewportWidth
    
    return zoomRatio

def worldToView(view, point):
    x, y, clipped = view.worldToView(OpenMaya.MPoint(point))
    return OpenMaya.MPoint(x, y, 0)


class IKManipulator(OpenMayaUI.MPxManipulatorNode):
    
    class ConnectedChain(object):
        
        class Undoer(object):
        
            def __init__(self, chain, affectEndRotation):
                chain.storeCurrentState()
                
                self.limbADagPath = chain.limbADagPath
                self.limbBDagPath = chain.limbBDagPath
                self.previousLimbARotation = chain.initialLimbALocalRotation
                self.previousLimbBRotation = chain.initialLimbBWorldRotation
                self.currentLimbARotation = chain.currentLimbALocalRotation
                self.currentLimbBRotation = chain.currentLimbBWorldRotation
                
                self.affectEndRotation = affectEndRotation
                if self.affectEndRotation:
                    self.limbCDagPath = chain.limbCDagPath
                    self.previousLimbCRotation = chain.initialLimbCLocalRotation
                    self.currentLimbCRotation = chain.currentLimbCLocalRotation
                    
                self.limbCuadrupedDagPath = chain.limbCuadrupedDagPath
                if self.limbCuadrupedDagPath:
                    self.previousLimbCuadrupedRotation = chain.initialLimbCuadrupedWorldRotation
                    self.currentLimbCuadrupedRotation = chain.currentLimbCuadrupedWorldRotation
                
            def undoIt(self):
                limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
                limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
                limbATransformFn.setRotation(self.previousLimbARotation, OpenMaya.MSpace.kTransform)
                limbBTransformFn.setRotation(self.previousLimbBRotation, OpenMaya.MSpace.kWorld)
                
                if self.limbCuadrupedDagPath:
                    limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.limbCuadrupedDagPath)
                    limbCuadrupedTransformFn.setRotation(self.previousLimbCuadrupedRotation, OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                    limbCTransformFn.setRotation(self.previousLimbCRotation, OpenMaya.MSpace.kTransform)
                    
            def redoIt(self):
                limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
                limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
                limbATransformFn.setRotation(self.currentLimbARotation, OpenMaya.MSpace.kTransform)
                limbBTransformFn.setRotation(self.currentLimbBRotation, OpenMaya.MSpace.kWorld)
    
                if self.limbCuadrupedDagPath:
                    limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.limbCuadrupedDagPath)
                    limbCuadrupedTransformFn.setRotation(self.currentLimbCuadrupedRotation, OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                    limbCTransformFn.setRotation(self.currentLimbCRotation, OpenMaya.MSpace.kTransform)
                    
    
        def __init__(self, rigChain):
            self.rigChain = rigChain
            
            self.limbADagPath = OpenMayaUtils.asDagPath(rigChain.fkLimbA)
            self.limbBDagPath = OpenMayaUtils.asDagPath(rigChain.fkLimbB)
            self.limbCDagPath = OpenMayaUtils.asDagPath(rigChain.fkLimbC)
            
            limbCuadruped = rigChain.fkLimbCuadruped
            self.limbCuadrupedDagPath = OpenMayaUtils.asDagPath(limbCuadruped) if limbCuadruped else None
            
            self.planarAxis = rigChain.fkPlanarAxis
            
            self.initialLimbALocalRotation = None
            self.initialLimbCLocalRotation = None
            self.currentLimbALocalRotation = None
            self.currentLimbCLocalRotation = None
        
            self.initialLimbAWorldTranslation = None
            self.initialLimbAWorldRotation = None
            self.initialLimbBWorldTranslation = None
            self.initialLimbBWorldRotation = None
            self.initialLimbCWorldTranslation = None
            self.initialLimbCWorldRotation = None
            self.initialLimbCuadrupedWorldTranslation = None
            self.initialLimbCuadrupedWorldRotation = None
            self.initialBaseWorldTranslation = None
            self.initialBaseWorldRotation = None
            
            self.currentLimbAWorldTranslation = None
            self.currentLimbAWorldRotation = None
            self.currentLimbBWorldTranslation = None
            self.currentLimbBWorldRotation = None
            self.currentLimbCWorldTranslation = None
            self.currentLimbCWorldRotation = None
            self.currentLimbCuadrupedWorldTranslation = None
            self.currentLimbCuadrupedWorldRotation = None
            self.currentBaseWorldTranslation = None
            self.currentBaseWorldRotation = None
            
        def __eq__(self, other):
            if issubclass(type(other), IKManipulator.ConnectedChain):
                return self.rigChain == other.rigChain
            return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
    
        def getPlanarAxisFromChain(self):
            return IKFKChain.getEnumAxis(self.planarAxis)
        
        def getUndoer(self):
            return self.Undoer(self, IKManipulatorController.isAffectEndRotation())
        
        def getHandlesToHide(self):
            handlesToHide = IKManipulator.HIDE_NO_HANDLES
            if not self.limbCuadrupedDagPath:
                handlesToHide |= IKManipulator.HIDE_CUADRUPED_HANDLES
            return handlesToHide
        
        def moveToPosition(self, position, useCachedData=False, rotateEnd=True):
            if not useCachedData:
                self.storeInitialState()
            
            if self.limbCuadrupedDagPath:
                AtoC_dir = (self.initialLimbCWorldTranslation - self.initialLimbAWorldTranslation).normal()
                AtoM_dir = (position - self.initialLimbAWorldTranslation).normal()
                extraAxis = (AtoC_dir ^ AtoM_dir).normal()
                extraAngle = math.acos(MathUtils.clamp(AtoC_dir * AtoM_dir, -1, 1))
                extraRotation = OpenMaya.MQuaternion(extraAngle, extraAxis)
                
                planarAxis = self.getPlanarAxisFromChain().rotateBy(self.initialLimbAWorldRotation)
                newPlanarAxis = planarAxis.rotateBy(extraRotation)
                normalRotation = OpenMaya.MQuaternion(planarAxis, newPlanarAxis)
                
                C = self.initialLimbCuadrupedWorldTranslation
                M = position - (self.initialLimbCWorldTranslation - self.initialLimbCuadrupedWorldTranslation).rotateBy(normalRotation)
                
            else:
                C = self.initialLimbCWorldTranslation
                M = position
            
            AtoM = M - self.initialLimbAWorldTranslation
            AtoC = C - self.initialLimbAWorldTranslation
            AtoB = self.initialLimbBWorldTranslation - self.initialLimbAWorldTranslation
            BtoC = C - self.initialLimbBWorldTranslation
            AtoM_dist = AtoM.length()
            AtoC_dist = AtoC.length()
            AtoB_dist = AtoB.length()
            BtoC_dist = BtoC.length()
            AtoM_dir = AtoM / AtoM_dist
            AtoC_dir = AtoC / AtoC_dist
            AtoB_dir = AtoB / AtoB_dist
            
            AtoM_dist = MathUtils.clamp(AtoM_dist, 0.01, AtoB_dist + BtoC_dist)
            
            currentPlanarAngle = math.acos(MathUtils.clamp(AtoC_dir * AtoB_dir, -1, 1))
            newPlanarAngle = math.acos(MathUtils.clamp((AtoB_dist * AtoB_dist + AtoM_dist * AtoM_dist - BtoC_dist * BtoC_dist) / (2 * AtoB_dist * AtoM_dist), -1, 1))
            elbowAngle = math.acos(MathUtils.clamp((AtoB_dist * AtoB_dist + BtoC_dist * BtoC_dist - AtoM_dist * AtoM_dist) / (2 * AtoB_dist * BtoC_dist), -1, 1))
            extraAngle = math.acos(MathUtils.clamp(AtoC_dir * AtoM_dir, -1, 1))
            
            planarAxis = self.getPlanarAxisFromChain().rotateBy(self.initialLimbAWorldRotation)
            extraAxis = (AtoC_dir ^ AtoM_dir).normal()
            planarRotation = OpenMaya.MQuaternion(newPlanarAngle - currentPlanarAngle, planarAxis)
            extraRotation = OpenMaya.MQuaternion(extraAngle, extraAxis)
            elbowRotation = OpenMaya.MQuaternion(elbowAngle - math.pi, planarAxis.rotateBy(self.initialLimbBWorldRotation.inverse()))
            totalRotation = self.initialLimbAWorldRotation * (planarRotation * extraRotation)
            
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbATransformFn.setRotation(self.initialLimbALocalRotation, OpenMaya.MSpace.kTransform)
            limbATransformFn.rotateBy(planarRotation, OpenMaya.MSpace.kWorld)
            limbATransformFn.rotateBy(extraRotation, OpenMaya.MSpace.kWorld)
            
            limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
            limbBTransformFn.setRotation(elbowRotation * totalRotation, OpenMaya.MSpace.kWorld)
            
            if self.limbCuadrupedDagPath:
                newPlanarAxis = planarAxis.rotateBy(extraRotation)
                normalRotation = OpenMaya.MQuaternion(planarAxis, newPlanarAxis)
                
                limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.limbCuadrupedDagPath)
                limbCuadrupedTransformFn.setRotation(self.initialLimbCuadrupedWorldRotation, OpenMaya.MSpace.kWorld)
                limbCuadrupedTransformFn.rotateBy(normalRotation, OpenMaya.MSpace.kWorld)
            
            if IKManipulatorController.isAffectEndRotation() and rotateEnd:
                limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                currentRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
                limbCTransformFn.rotateBy((currentRotation.inverse() * self.initialLimbCWorldRotation), OpenMaya.MSpace.kWorld)
            
        def moveOffset(self, offset, useCachedData=False, rotateEnd=True):
            if not useCachedData:
                self.storeInitialState()
                
            offset = OpenMaya.MVector(offset)
            position = self.initialLimbCWorldTranslation + offset.rotateBy(self.getTargetRotation(useInitial=True))
            self.moveToPosition(position, useCachedData=True, rotateEnd=rotateEnd)

        def getTargetPosition(self, useInitial=False):
            return self.initialLimbCWorldTranslation if useInitial else self.currentLimbCWorldTranslation
        
        def getTargetRotation(self, useInitial=False):
            limbCWorldTranslation = self.initialLimbCWorldTranslation if useInitial else self.currentLimbCWorldTranslation
            limbCWorldRotation = self.initialLimbCWorldRotation if useInitial else self.currentLimbCWorldRotation
            #limbBWorldTranslation = self.initialLimbBWorldTranslation if useCached else self.currentLimbBWorldTranslation
            limbBWorldRotation = self.initialLimbBWorldRotation if useInitial else self.currentLimbBWorldRotation
            limbAWorldTranslation = self.initialLimbAWorldTranslation if useInitial else self.currentLimbAWorldTranslation
            limbAWorldRotation = self.initialLimbAWorldRotation if useInitial else self.currentLimbAWorldRotation
            #baseWorldTranslation = self.initialBaseWorldTranslation if useCached else self.currentBaseWorldTranslation
            baseWorldRotation = self.initialBaseWorldRotation if useInitial else self.currentBaseWorldRotation
            
            rotationMode = IKManipulatorController.getTransformMode()
            if rotationMode == "World":
                return OpenMaya.MQuaternion.kIdentity
            elif rotationMode == "Object":
                return limbCWorldRotation
            elif rotationMode == "Parent":
                return limbBWorldRotation
            elif rotationMode == "Base":
                return baseWorldRotation
            elif rotationMode == "Axis":
                planarAxis = self.getPlanarAxisFromChain()
                axis = OpenMaya.MVector(0, -1, 0) if self.planarAxis != 1 else OpenMaya.MVector(-1, 0, 0)
                d = (limbCWorldTranslation - limbAWorldTranslation).normal()
                r = planarAxis.rotateBy(limbAWorldRotation)
                q = OpenMaya.MQuaternion(axis, d)
                return q * OpenMaya.MQuaternion(planarAxis.rotateBy(q), r)
            else:
                return OpenMaya.MQuaternion.kIdentity
        
        def storeInitialState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.initialLimbALocalRotation = limbATransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            self.initialLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            self.initialLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.initialLimbBWorldTranslation = OpenMaya.MPoint(limbBTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbBWorldRotation = limbBTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.initialLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbCWorldRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            if self.limbCuadrupedDagPath:
                limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.limbCuadrupedDagPath)
                self.initialLimbCuadrupedWorldTranslation = OpenMaya.MPoint(limbCuadrupedTransformFn.translation(OpenMaya.MSpace.kWorld))
                self.initialLimbCuadrupedWorldRotation = limbCuadrupedTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)

            parentMatrix = OpenMaya.MTransformationMatrix(self.limbADagPath.exclusiveMatrix())
            self.initialBaseWorldTranslation = OpenMaya.MPoint(parentMatrix.translation(OpenMaya.MSpace.kWorld))
            self.initialBaseWorldRotation = parentMatrix.rotation(asQuaternion=True)
        
        def storeCurrentState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.currentLimbALocalRotation = limbATransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            self.currentLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            self.currentLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.currentLimbBWorldTranslation = OpenMaya.MPoint(limbBTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbBWorldRotation = limbBTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.currentLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbCWorldRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)

            if self.limbCuadrupedDagPath:
                limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.limbCuadrupedDagPath)
                self.currentLimbCuadrupedWorldTranslation = OpenMaya.MPoint(limbCuadrupedTransformFn.translation(OpenMaya.MSpace.kWorld))
                self.currentLimbCuadrupedWorldRotation = limbCuadrupedTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)

            parentMatrix = OpenMaya.MTransformationMatrix(self.limbADagPath.exclusiveMatrix())
            self.currentBaseWorldTranslation = OpenMaya.MPoint(parentMatrix.translation(OpenMaya.MSpace.kWorld))
            self.currentBaseWorldRotation = parentMatrix.rotation(asQuaternion=True)
    
    
    class ConnectedNormalNode(object):
        
        class Undoer(object):
        
            def __init__(self, node):
                node.storeCurrentState()
                
                self.nodeDagPath = node.dagPath
                self.previousNodeTranslation = OpenMaya.MVector(node.initialWorldTranslation)
                self.currentNodeTranslation = OpenMaya.MVector(node.currentWorldTranslation)
                
            def undoIt(self):
                transformFn = OpenMaya.MFnTransform(self.nodeDagPath)
                transformFn.setTranslation(self.previousNodeTranslation, OpenMaya.MSpace.kWorld)
                
            def redoIt(self):
                transformFn = OpenMaya.MFnTransform(self.nodeDagPath)
                transformFn.setTranslation(self.currentNodeTranslation, OpenMaya.MSpace.kWorld)
    
    
        def __init__(self, node):
            self.dagPath = OpenMayaUtils.asDagPath(node)
            
            self.initialWorldTranslation = None
            self.initialWorldRotation = None
            self.initialParentWorldTranslation = None
            self.initialParentWorldRotation = None
            
            self.currentWorldTranslation = None
            self.currentWorldRotation = None
            self.currentParentWorldTranslation = None
            self.currentParentWorldRotation = None
            
        def __eq__(self, other):
            if issubclass(type(other), IKManipulator.ConnectedNormalNode):            
                return self.dagPath == other.dagPath
            return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def getUndoer(self):
            return self.Undoer(self)
        
        def getHandlesToHide(self):
            handlesToHide = IKManipulator.HIDE_SWIVEL_HANDLES | IKManipulator.HIDE_CUADRUPED_HANDLES
            
            transformMode = IKManipulatorController.getTransformMode()
            shouldHide = transformMode == "Parent" or transformMode == "Base"
            
            if shouldHide:
                nodeFn = OpenMaya.MFnDependencyNode(self.dagPath.node())
                translateXPlug = nodeFn.findPlug("translateX", False)
                translateYPlug = nodeFn.findPlug("translateY", False)
                translateZPlug = nodeFn.findPlug("translateZ", False)
                
                if translateXPlug.isNull or translateXPlug.isLocked:
                    handlesToHide |= IKManipulator.HIDE_TRANSLATE_X_HANDLE
                if translateYPlug.isNull or translateYPlug.isLocked:
                    handlesToHide |= IKManipulator.HIDE_TRANSLATE_Y_HANDLE
                if translateZPlug.isNull or translateZPlug.isLocked:
                    handlesToHide |= IKManipulator.HIDE_TRANSLATE_Z_HANDLE
            
            return handlesToHide
        
        def moveToPosition(self, position, useCachedData=False, rotateEnd=True):
            if not useCachedData:
                self.storeInitialState()
                
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            transformFn.setTranslation(OpenMaya.MVector(position), OpenMaya.MSpace.kWorld)
            
        def moveOffset(self, offset, useCachedData=False, rotateEnd=True):
            if not useCachedData:
                self.storeInitialState()
            
            offset = OpenMaya.MVector(offset)
            position = self.initialWorldTranslation + offset.rotateBy(self.getTargetRotation(useInitial=True))
            self.moveToPosition(position, useCachedData=True)
        
        def getTargetPosition(self, useInitial=False):
            return self.initialWorldTranslation if useInitial else self.currentWorldTranslation
        
        def getTargetRotation(self, useInitial=False):
            rotation =  self.initialWorldRotation if useInitial else self.currentWorldRotation
            parentRotation =  self.initialParentWorldRotation if useInitial else self.currentParentWorldRotation
            
            rotationMode = IKManipulatorController.getTransformMode()
            if rotationMode == "World" or rotationMode == "Axis":
                return OpenMaya.MQuaternion.kIdentity
            elif rotationMode == "Object":
                return rotation
            elif rotationMode == "Parent" or rotationMode == "Base":
                return parentRotation
            else:
                return OpenMaya.MQuaternion.kIdentity
        
        def storeInitialState(self):
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            self.initialWorldTranslation = OpenMaya.MPoint(transformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialWorldRotation = transformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            parentMatrix = OpenMaya.MTransformationMatrix(self.dagPath.exclusiveMatrix())
            self.initialParentWorldTranslation = OpenMaya.MPoint(parentMatrix.translation(OpenMaya.MSpace.kWorld))
            self.initialParentWorldRotation = parentMatrix.rotation(asQuaternion=True)
            
        def storeCurrentState(self):
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            self.currentWorldTranslation = OpenMaya.MPoint(transformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentWorldRotation = transformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            parentMatrix = OpenMaya.MTransformationMatrix(self.dagPath.exclusiveMatrix())
            self.currentParentWorldTranslation = OpenMaya.MPoint(parentMatrix.translation(OpenMaya.MSpace.kWorld))
            self.currentParentWorldRotation = parentMatrix.rotation(asQuaternion=True)
    
    
    nodeName = "ikManip"
    
    HIDE_NO_HANDLES = 0
    HIDE_SWIVEL_HANDLES = 1
    HIDE_CUADRUPED_HANDLES = 2
    HIDE_TRANSLATE_X_HANDLE = 4
    HIDE_TRANSLATE_Y_HANDLE = 8
    HIDE_TRANSLATE_Z_HANDLE = 16
    HIDE_ROTATE_HANDLES = HIDE_SWIVEL_HANDLES | HIDE_CUADRUPED_HANDLES
    HIDE_TRANSLATE_HANDLES = HIDE_TRANSLATE_X_HANDLE | HIDE_TRANSLATE_Y_HANDLE | HIDE_TRANSLATE_Z_HANDLE
    
    @staticmethod
    def creator():
        return IKManipulator()
    
    @staticmethod
    def initialize():
        pass
    
    def __init__(self):
        OpenMayaUI.MPxManipulatorNode.__init__(self)
        
        self.connectedItems = []
        
        self.targetToDraw = None
        
        self.xAxisHandle = None
        self.yAxisHandle = None
        self.zAxisHandle = None
        self.xPlaneHandle = None
        self.yPlaneHandle = None
        self.zPlaneHandle = None
        self.viewHandle = None
        self.swivelAngleHandle = None
        self.cuadrupedAngleHandle = None
        
        self.zoomRatio = None
        self.cameraRotation = None
        self.view = None
        
        self.clickedPosition = None
        self.newClickedPosition = None
    
    def connectToDependNode(self, node):
        dependencyNodeFn = OpenMaya.MFnDependencyNode(node)
        messagePlug = dependencyNodeFn.findPlug("message", False)
        connections = messagePlug.connectedTo(False, True)
        isChain = False
        for connection in connections:
            if OpenMaya.MFnDependencyNode(connection.node()).typeName == IKFKChain._Type:
                rigChain = IKFKChain(connection.node())
                if connection.partialName(useLongNames=True).startswith("fkLimb"):
                    conn = IKManipulator.ConnectedChain(rigChain)
                    if conn not in self.connectedItems:
                        self.connectedItems.append(conn)
                    isChain = True
        if not isChain:
            self.connectedItems.append(IKManipulator.ConnectedNormalNode(node))
    
    def getTargetToDraw(self):
        if len(self.connectedItems) > 0:
            return self.connectedItems[-1]
        else:
            return None
    
    def moveToPosition(self, position, useCachedData=False):
        for item in self.connectedItems:
            item.moveToPosition(position, useCachedData=useCachedData)
    
    def moveOffset(self, offset, useCachedData=False):
        for item in self.connectedItems:
            item.moveOffset(offset, useCachedData=useCachedData)
    
    def preDrawUI(self, view):
        self.targetToDraw = self.getTargetToDraw()
        if self.targetToDraw != None:
            self.targetToDraw.storeCurrentState()
            self.zoomRatio = getCameraZoomRatio(view.getCamera(), self.targetToDraw.getTargetPosition(), viewportWidth=view.portWidth())
            self.cameraRotation = getNodeWorldRotation(view.getCamera())
            self.view = view
    
    def drawUI(self, drawManager, frameContext):
        if self.targetToDraw == None:
            return
        
        targetPosition = self.targetToDraw.getTargetPosition()
        initialPosition = self.targetToDraw.getTargetPosition(useInitial=True)
        targetRotation = self.targetToDraw.getTargetRotation(useInitial=(self.clickedPosition is not None and not IKManipulatorController.isUpdateWhileMoving()))
        
        handlesToHide = self.targetToDraw.getHandlesToHide()
        if self.clickedPosition is not None:
            activeHandle = self.glActiveName()
            if activeHandle == self.swivelAngleHandle:
                handlesToHide |= self.HIDE_TRANSLATE_HANDLES | self.HIDE_CUADRUPED_HANDLES
            elif activeHandle == self.cuadrupedAngleHandle:
                handlesToHide |= self.HIDE_TRANSLATE_HANDLES | self.HIDE_SWIVEL_HANDLES
            else:
                handlesToHide |= self.HIDE_ROTATE_HANDLES
        
        handle = self.glFirstHandle()
        self.xAxisHandle = handle
        if not (handlesToHide & self.HIDE_TRANSLATE_X_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle, self.xColor())
            self.drawArrow(drawManager, targetPosition, targetRotation, OpenMaya.MVector(1, 0, 0))
            drawManager.endDrawable()
        
        handle += 1
        self.yAxisHandle = handle
        if not (handlesToHide & self.HIDE_TRANSLATE_Y_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle, self.yColor())
            self.drawArrow(drawManager, targetPosition, targetRotation, OpenMaya.MVector(0, 1, 0))
            drawManager.endDrawable()
        
        handle += 1
        self.zAxisHandle = handle
        if not (handlesToHide & self.HIDE_TRANSLATE_Z_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle, self.zColor())
            self.drawArrow(drawManager, targetPosition, targetRotation, OpenMaya.MVector(0, 0, 1))
            drawManager.endDrawable()
        
        handle += 1
        self.xPlaneHandle = handle
        if not (handlesToHide & (self.HIDE_TRANSLATE_Y_HANDLE | self.HIDE_TRANSLATE_Z_HANDLE)):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  self.xColor())
            self.drawPlane(drawManager, targetPosition, targetRotation, OpenMaya.MVector(0, 1, 0), OpenMaya.MVector(0, 0, 1))
            drawManager.endDrawable()
        
        handle += 1
        self.yPlaneHandle = handle
        if not (handlesToHide & (self.HIDE_TRANSLATE_Z_HANDLE | self.HIDE_TRANSLATE_X_HANDLE)):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  self.yColor())
            self.drawPlane(drawManager, targetPosition, targetRotation, OpenMaya.MVector(0, 0, 1), OpenMaya.MVector(1, 0, 0))
            drawManager.endDrawable()
        
        handle += 1
        self.zPlaneHandle = handle
        if not (handlesToHide & (self.HIDE_TRANSLATE_X_HANDLE | self.HIDE_TRANSLATE_Y_HANDLE)):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  self.zColor())
            self.drawPlane(drawManager, targetPosition, targetRotation, OpenMaya.MVector(1, 0, 0), OpenMaya.MVector(0, 1, 0))
            drawManager.endDrawable()
        
        handle += 1
        self.viewHandle = handle
        if (handlesToHide & self.HIDE_TRANSLATE_HANDLES) != self.HIDE_TRANSLATE_HANDLES:
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  self.mainColor())
            self.drawViewPlane(drawManager, targetPosition, self.cameraRotation)
            drawManager.endDrawable()
        
        handle += 1
        self.swivelAngleHandle = handle
        if not (handlesToHide & self.HIDE_SWIVEL_HANDLES):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  10)   # Color Nº10 is Magenta
            axis = (targetPosition - self.targetToDraw.currentLimbAWorldTranslation).normal()
            normal = self.targetToDraw.getPlanarAxisFromChain().rotateBy(self.targetToDraw.currentLimbAWorldRotation)
            arrowDirection = (normal ^ axis).normal()
            radius = self.drawRotationCircle(drawManager, targetPosition, axis, arrowDirection=arrowDirection)
            drawManager.endDrawable()
            
            if IKManipulatorController.isDrawAxis():
                drawManager.beginDrawable()
                drawManager.setColor(OpenMaya.MColor((0.5, 0.5, 0.5, 0.5)))
                drawManager.setLineStyle(drawManager.kShortDashed)
                drawManager.line(targetPosition, self.targetToDraw.currentBaseWorldTranslation)
                drawManager.endDrawable()
        
        handle += 1
        self.cuadrupedAngleHandle = handle
        if not (handlesToHide & self.HIDE_CUADRUPED_HANDLES):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.setHandleColor(drawManager, handle,  19)   # Color Nº19 is Cyan
            axis = self.targetToDraw.getPlanarAxisFromChain().rotateBy(self.targetToDraw.currentLimbAWorldRotation)
            radius = self.drawRotationCircle(drawManager, targetPosition, axis)
            drawManager.endDrawable()
        
        if self.clickedPosition is not None:
            targetView = worldToView(self.view, targetPosition)
            
            if not (handlesToHide & self.HIDE_TRANSLATE_HANDLES):
                initialView = worldToView(self.view, initialPosition)
                
                drawManager.beginDrawable()
                drawManager.setColor(OpenMaya.MColor((0.5, 0.5, 0.5, 0.5)))
                drawManager.line2d(initialView, targetView)
                drawManager.rect2d(initialView, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                drawManager.endDrawable()
                
            if (handlesToHide & self.HIDE_ROTATE_HANDLES) != self.HIDE_ROTATE_HANDLES:
                clickedView = worldToView(self.view, targetPosition + radius * (self.clickedPosition - initialPosition).normal())
                
                drawManager.beginDrawable()
                drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                drawManager.line2d(targetView, clickedView)
                drawManager.rect2d(clickedView, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                drawManager.endDrawable()
                
        if self.newClickedPosition is not None:
            if (handlesToHide & self.HIDE_ROTATE_HANDLES) != self.HIDE_ROTATE_HANDLES:
                targetView = worldToView(self.view, targetPosition)
                
                clickedDir = (self.clickedPosition - initialPosition).normal()
                newClickedDir = (self.newClickedPosition - initialPosition).normal()
                
                if IKManipulatorController.isAlternativeRotateMode():
                    start = clickedView
                    end = worldToView(self.view, self.newClickedPosition + OpenMaya.MVector(targetPosition) - initialPosition)
                    
                    if activeHandle == self.swivelAngleHandle:
                        initialRotation = self.targetToDraw.initialLimbAWorldRotation
                        currentRotation = self.targetToDraw.currentLimbAWorldRotation
                    elif activeHandle == self.cuadrupedAngleHandle:
                        initialRotation = self.targetToDraw.initialLimbCuadrupedWorldRotation
                        currentRotation = self.targetToDraw.currentLimbCuadrupedWorldRotation
                      
                    newDir = clickedDir.rotateBy(initialRotation.inverse() * currentRotation)  
                    newDirPos = worldToView(self.view, targetPosition + radius * newDir)
                    
                    drawManager.beginDrawable()
                    drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                    drawManager.line2d(targetView, newDirPos)
                    drawManager.rect2d(newDirPos, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 0, 0.25)))
                    drawManager.arc(targetPosition, clickedDir, newDir, clickedDir ^ newDir, radius * 0.5, filled=True)
                    drawManager.endDrawable()
                    
                else:
                    start = targetView
                    end = worldToView(self.view, targetPosition + radius * (self.newClickedPosition - initialPosition).normal())
                    
                    drawManager.beginDrawable()
                    drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 0, 0.25)))
                    drawManager.arc(targetPosition, clickedDir, newClickedDir, clickedDir ^ newClickedDir, radius * 0.5, filled=True)
                    drawManager.endDrawable()
                
                drawManager.beginDrawable()
                drawManager.setColor(OpenMaya.MColor((1, 1, 1, 1)))
                drawManager.line2d(start, end)
                drawManager.rect2d(end, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                drawManager.endDrawable()
    
    def drawArrow(self, drawManager, origin, rotation, direction):
        direction = direction.rotateBy(rotation)
        
        lineLength = 1.80 * self.zoomRatio * OpenMayaUI.MFnManip3D.globalSize()
        coneRadius = 0.36 * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
        coneLength = 2.00 * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
        end = origin + lineLength * direction
        
        drawManager.line(origin, end)
        drawManager.cone(end, direction, coneRadius, coneLength, True)
    
    def drawPlane(self, drawManager, origin, rotation, axis1, axis2):
        axis1 = axis1.rotateBy(rotation)
        axis2 = axis2.rotateBy(rotation)
            
        normal = axis1 ^ axis2
        offset = 1.35 * self.zoomRatio * OpenMayaUI.MFnManip3D.globalSize()
        size = 0.75 * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
        
        drawManager.rect(origin + offset * (axis1 + axis2), axis1, normal, size, size, True)
    
    def drawViewPlane(self, drawManager, origin, cameraRotation, size=0.9):
        normal = OpenMaya.MVector(0, 0, 1).rotateBy(cameraRotation)
        up = OpenMaya.MVector(0, 1, 0).rotateBy(cameraRotation)
        size = size * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
        
        drawManager.rect(origin, up, normal, size, size, False)
    
    def drawRotationCircle(self, drawManager, origin, axis, arrowDirection=None):
        radius = IKManipulatorController.getRotateDisplayRadius() * self.zoomRatio * OpenMayaUI.MFnManip3D.globalSize()
        
        drawManager.setLineWidth(OpenMayaUI.MFnManip3D.lineSize())
        drawManager.circle(origin, axis, radius, False)
        
        if arrowDirection:
            coneRadius = 0.18 * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
            coneLength = 1.00 * self.zoomRatio * OpenMayaUI.MFnManip3D.handleSize() * 0.01
            end = origin + arrowDirection * radius
            
            drawManager.setLineStyle(drawManager.kShortDashed)
            drawManager.line(origin, origin + arrowDirection * radius)
            drawManager.cone(end - arrowDirection * coneLength, arrowDirection, coneRadius, coneLength, True)
        
        return radius
    
    def getClickedPosition(self, rayOrigin, rayDirection, origin, rotation, view):
        activeHandle = self.glActiveName()
        if activeHandle == self.xAxisHandle:
            return GeometryUtils.rayIntersectionOnLine(rayOrigin, rayDirection, origin, OpenMaya.MVector(1, 0, 0).rotateBy(rotation))[0]
        elif activeHandle == self.yAxisHandle:
            return GeometryUtils.rayIntersectionOnLine(rayOrigin, rayDirection, origin, OpenMaya.MVector(0, 1, 0).rotateBy(rotation))[0]
        elif activeHandle == self.zAxisHandle:
            return GeometryUtils.rayIntersectionOnLine(rayOrigin, rayDirection, origin, OpenMaya.MVector(0, 0, 1).rotateBy(rotation))[0]
        elif activeHandle == self.xPlaneHandle:
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, OpenMaya.MVector(1, 0, 0).rotateBy(rotation))[0]
        elif activeHandle == self.yPlaneHandle:
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, OpenMaya.MVector(0, 1, 0).rotateBy(rotation))[0]
        elif activeHandle == self.zPlaneHandle:
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, OpenMaya.MVector(0, 0, 1).rotateBy(rotation))[0]
        elif activeHandle == self.viewHandle:
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, OpenMaya.MVector(0, 0, 1).rotateBy(getNodeWorldRotation(view.getCamera())))[0]
        elif activeHandle == self.swivelAngleHandle:
            axis = (origin - self.targetToDraw.initialLimbAWorldTranslation).normal()
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, axis)[0]
        elif activeHandle == self.cuadrupedAngleHandle:
            axis = self.targetToDraw.getPlanarAxisFromChain().rotateBy(self.targetToDraw.currentLimbAWorldRotation)
            return GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, axis)[0]
    
    def doPress(self, view):
        if self.targetToDraw == None:
            return
        
        for item in self.connectedItems:
            item.storeInitialState()
        
        targetPosition = self.targetToDraw.getTargetPosition(useInitial=True)
        targetRotation = self.targetToDraw.getTargetRotation(useInitial=(not IKManipulatorController.isUpdateWhileMoving()))
        
        rayOrigin, rayDirection = self.mouseRayWorld()
        self.clickedPosition = self.getClickedPosition(rayOrigin, rayDirection, targetPosition, targetRotation, view)
    
    def doDrag(self, view):
        if self.targetToDraw == None:
            return
        
        targetPosition = self.targetToDraw.getTargetPosition(useInitial=True)
        targetRotation = self.targetToDraw.getTargetRotation(useInitial=(not IKManipulatorController.isUpdateWhileMoving()))
        
        rayOrigin, rayDirection = self.mouseRayWorld()
        self.newClickedPosition = self.getClickedPosition(rayOrigin, rayDirection, targetPosition, targetRotation, view)
        
        activeHandle = self.glActiveName()
        if activeHandle == self.swivelAngleHandle or activeHandle == self.cuadrupedAngleHandle:
            startDirection = (self.clickedPosition - targetPosition).normal()
            endDirection = (self.newClickedPosition - targetPosition).normal()
            axis = startDirection ^ endDirection
            
            if IKManipulatorController.isAlternativeRotateMode():
                perpendicular = (axis ^ startDirection).normal()
                self.newClickedPosition = GeometryUtils.rayIntersectionOnLine(rayOrigin, rayDirection, self.clickedPosition, perpendicular)[0]
                zoomRatio = getCameraZoomRatio(view.getCamera(), targetPosition, viewportWidth=view.portWidth())
                distance = IKManipulatorController.getAlternativeRotateModeSensibility() * (self.newClickedPosition - self.clickedPosition) * perpendicular / zoomRatio    # Since we are using distance units to apply an angle, we use the camera zoom ratio to be more consistent
                rotation = OpenMaya.MQuaternion(distance, axis)
            else:
                rotation = OpenMaya.MQuaternion(endDirection.angle(startDirection), axis)
            
            if activeHandle == self.swivelAngleHandle:
                limbATransformFn = OpenMaya.MFnTransform(self.targetToDraw.limbADagPath)
                limbATransformFn.setRotation(self.targetToDraw.initialLimbALocalRotation, OpenMaya.MSpace.kTransform)
                limbATransformFn.rotateBy(rotation, OpenMaya.MSpace.kWorld)
            
            elif activeHandle == self.cuadrupedAngleHandle:
                distance = self.targetToDraw.initialLimbCWorldTranslation - self.targetToDraw.initialLimbCuadrupedWorldTranslation
                offset = distance - distance.rotateBy(rotation)
                self.targetToDraw.moveOffset(offset, useCachedData=True, rotateEnd=False)
        
                limbCuadrupedTransformFn = OpenMaya.MFnTransform(self.targetToDraw.limbCuadrupedDagPath)
                limbCuadrupedTransformFn.setRotation(self.targetToDraw.initialLimbCuadrupedWorldRotation, OpenMaya.MSpace.kWorld)
                limbCuadrupedTransformFn.rotateBy(rotation, OpenMaya.MSpace.kWorld)
                
            if IKManipulatorController.isAffectEndRotation():
                limbCTransformFn = OpenMaya.MFnTransform(self.targetToDraw.limbCDagPath)
                currentRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
                limbCTransformFn.rotateBy((currentRotation.inverse() * self.targetToDraw.initialLimbCWorldRotation), OpenMaya.MSpace.kWorld)
            
        else:
            offset = (self.newClickedPosition - self.clickedPosition).rotateBy(self.targetToDraw.getTargetRotation(useInitial=True).inverse())
            self.moveOffset(offset, useCachedData=True)
    
    def doRelease(self, view):
        if self.targetToDraw == None:
            return
        
        undoers = []
        for item in self.connectedItems:
            undoers.append(item.getUndoer())
            
        ApiUndo.UndoOverwrite(undoers).commit()
        
        self.clickedPosition = None
        self.newClickedPosition = None


class IKManipulatorContext(OpenMayaUI.MPxSelectionContext):

    def __init__(self):
        OpenMayaUI.MPxSelectionContext.__init__(self)
        
        self.callback = None
        
        self.manipulator = None
    
    def stringClassName(self):
        return IKManipulatorController.CONTEXT_CLASS
    
    def toolOnSetup(self, event):
        self.setTitleString("IKManipulator")
        self.setHelpString("Move a FK chain like it was IK.")
        self.setImage(IKManipulatorController.CONTEXT_IMAGE, self.kImage1)
        
        self.updateManipulators()
        self.callback = OpenMaya.MModelMessage.addCallback(OpenMaya.MModelMessage.kActiveListModified, self.updateManipulators)
    
    def toolOffCleanup(self):
        self.deleteManipulators()
        OpenMaya.MMessage.removeCallback(self.callback)
    
    def updateManipulators(self, *args):
        self.deleteManipulators()
        
        sl = OpenMaya.MGlobal.getActiveSelectionList()
        if sl.length() > 0:
            self.manipulator, manipObject = IKManipulator.newManipulator("ikManip")
            self.addManipulator(manipObject)
            
            iter = OpenMaya.MItSelectionList(sl, OpenMaya.MFn.kInvalid)
            while not iter.isDone():
                dependNode = iter.getDependNode()
                iter.next()
                
                if dependNode.isNull() or not dependNode.hasFn(OpenMaya.MFn.kTransform):
                    continue
                
                self.manipulator.connectToDependNode(dependNode)
        else:
            self.manipulator = None
                
        self.feedbackNumericalInput()
    
    def argTypeNumericalInput(self, argIndex):
        return OpenMaya.MSyntax.kDistance
    
    def processNumericalInput(self, values, flags, isAbsolute):
        # We should be implementing the feedbackNumericalInput method to update the input box with the manipulator data.
        # But it relies on the class MFeedbackLine wich is not implemented on the API 2.0 (the 1.0 version does nothing).
        # Even then, the procedure that updates the input box doesn't seem to read any data and instead it just clears the text fields.
        # So yeah, no chance :)
    
        if self.manipulator == None:
            return False
        
        undoers = []
        for item in self.manipulator.connectedItems:
            item.storeInitialState()
            values = OpenMaya.MPoint(values)
            
            if isAbsolute:
                position = item.getTargetPosition(useInitial=True)
                if self.ignoreEntry(flags, 0):
                    values.x = position.x
                if self.ignoreEntry(flags, 1):
                    values.y = position.y
                if self.ignoreEntry(flags, 2):
                    values.z = position.z
                item.moveToPosition(values, useCachedData=True)
            
            else:
                if self.ignoreEntry(flags, 0):
                    values.x = 0
                if self.ignoreEntry(flags, 1):
                    values.y = 0
                if self.ignoreEntry(flags, 2):
                    values.z = 0
                item.moveOffset(values, useCachedData=True)
            
            undoers.append(item.getUndoer())
            
        ApiUndo.UndoOverwrite(undoers).commit()
        
        return True
    
    def ignoreEntry(self, flags, index):
        # This method should be provided by Maya, but it is not implemented on the API 2.0 :)
        # We have to add it ourselves, so it might not work as expected on certain situations.
        
        # It seems that falgs 2, 3 and 4 indicate if we should ignore the X, Y and Z coordinates respectively.
        return flags[2 + index] == 1


class IKManipulatorContextCommand(OpenMayaUI.MPxContextCommand):
    
    @staticmethod
    def creator():
        return IKManipulatorContextCommand()
    
    def makeObj(self):
        return IKManipulatorContext()


class FKManipulator(OpenMayaUI.MPxManipulatorNode):
    
    class ConnectedChainElbow(object):
        
        class Undoer(object):
        
            def __init__(self, chain, affectEndRotation):
                chain.storeCurrentState()
                
                self.limbCDagPath = chain.limbCDagPath
                self.poleVectorDagPath = chain.poleVectorDagPath
                self.swivelPlug = chain.swivelPlug
                
                self.swivelOutputMode = chain.rigChain.ikSwivelOutputMode
                
                self.previousLimbCTranslation = chain.initialLimbCWorldTranslation
                self.currentLimbCTranslation = chain.currentLimbCWorldTranslation
                
                self.affectEndRotation = affectEndRotation
                if self.affectEndRotation:
                    self.previousLimbCRotation = chain.initialLimbCLocalRotation
                    self.currentLimbCRotation = chain.currentLimbCLocalRotation
                
                if self.swivelOutputMode == 0:
                    self.previousPoleVectorTranslation = chain.initialPoleVectorWorldTranslation
                    self.currentPoleVectorTranslation = chain.currentPoleVectorWorldTranslation
                
                elif self.swivelOutputMode == 1:
                    self.previousSwivelAngle = chain.initialSwivelAngle
                    self.currentSwivelAngle = chain.currentSwivelAngle
                
            def undoIt(self):
                limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                limbCTransformFn.setTranslation(OpenMaya.MVector(self.previousLimbCTranslation), OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn.setRotation(self.previousLimbCRotation, OpenMaya.MSpace.kTransform)
                
                if self.swivelOutputMode == 0:
                    poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                    poleVectorTransformFn.setTranslation(OpenMaya.MVector(self.previousPoleVectorTranslation), OpenMaya.MSpace.kWorld)
                
                elif self.swivelOutputMode == 1:
                    self.swivelPlug.setMAngle(OpenMaya.MAngle(self.previousSwivelAngle, OpenMaya.MAngle.kRadians))
                    
            def redoIt(self):
                limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                limbCTransformFn.setTranslation(OpenMaya.MVector(self.currentLimbCTranslation), OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn.setRotation(self.currentLimbCRotation, OpenMaya.MSpace.kTransform)
                
                if self.swivelOutputMode == 0:
                    poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                    poleVectorTransformFn.setTranslation(OpenMaya.MVector(self.currentPoleVectorTranslation), OpenMaya.MSpace.kWorld)

                elif self.swivelOutputMode == 1:
                    self.swivelPlug.setMAngle(OpenMaya.MAngle(self.currentSwivelAngle, OpenMaya.MAngle.kRadians))


        def __init__(self, rigChain):
            self.rigChain = rigChain
            
            self.limbADagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbA)
            self.limbBDagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbB)
            self.limbCDagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbC)
            self.poleVectorDagPath = OpenMayaUtils.asDagPath(rigChain.ikPoleVector)
            self.swivelPlug = OpenMayaUtils.asMPlug(rigChain.ikSwivelPlug)
            
            self.planarAxis = rigChain.ikPlanarAxis
            
            self.initialLimbCLocalRotation = None
            self.initialLimbCWorldRotation = None
            self.currentLimbCLocalRotation = None
            self.currentLimbCWorldRotation = None
        
            self.initialLimbAWorldTranslation = None
            self.initialLimbAWorldRotation = None
            self.initialLimbBWorldTranslation = None
            self.initialLimbBWorldRotation = None
            self.initialLimbCWorldTranslation = None
            self.initialPoleVectorWorldTranslation = None
            self.initialSwivelAngle = None
            
            self.currentLimbAWorldTranslation = None
            self.currentLimbAWorldRotation = None
            self.currentLimbBWorldTranslation = None
            self.currentLimbBWorldRotation = None
            self.currentLimbCWorldTranslation = None
            self.currentPoleVectorWorldTranslation = None
            self.currentSwivelAngle = None
            
            self.accumulatedSwivelAngleForCompensation = 0
        
        def __eq__(self, other):
            if issubclass(type(other), FKManipulator.ConnectedChainElbow):
                return self.rigChain == other.rigChain
            return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def getPlanarAxisFromChain(self):
            return IKFKChain.getEnumAxis(self.planarAxis)
        
        def getForwardAxisFromChain(self):
            BtoC_dir = (self.initialLimbCWorldTranslation - self.initialLimbBWorldTranslation).normal()
            BtoC_localDir = BtoC_dir.rotateBy(self.initialLimbBWorldRotation.inverse())
            return BtoC_localDir
        
        def getUndoer(self):
            return self.Undoer(self, FKManipulatorController.isAffectEndRotation())
        
        def getHandlesToHide(self):
            transformMode = FKManipulatorController.getTransformMode()
            if transformMode == "Object":
                return FKManipulator.HIDE_ROTATE_Z_HANDLE | FKManipulator.HIDE_ROTATE_VIEW_HANDLE | FKManipulator.HIDE_ROTATE_3D_HANDLE
            else:
                return FKManipulator.HIDE_NO_HANDLES
        
        def getLimbBRotation(self, B=None, C=None, rB=None):
            if B is None:
                B = OpenMaya.MFnTransform(self.limbBDagPath).translation(OpenMaya.MSpace.kWorld)
            if C is None:
                C = OpenMaya.MFnTransform(self.limbCDagPath).translation(OpenMaya.MSpace.kWorld)
            if rB is None:
                rB = OpenMaya.MFnTransform(self.limbBDagPath).rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            planarAxis = self.getPlanarAxisFromChain().rotateBy(rB)
            BtoC_dir = (C - B).normal()
            normal = (BtoC_dir ^ planarAxis).normal()
            
            return OpenMaya.MTransformationMatrix(OpenMaya.MMatrix((
                BtoC_dir.x, BtoC_dir.y, BtoC_dir.z, 0,
                planarAxis.x, planarAxis.y, planarAxis.z, 0,
                normal.x, normal.y, normal.z, 0,
                0, 0, 0, 1
            ))).rotation(asQuaternion=True)
        
        def rotateToRotation(self, rotation, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
                
            forwardAxis = self.getForwardAxisFromChain()
            planarAxis = -self.getPlanarAxisFromChain() # I am not sure where I made a mistake, but this only works when inverting this axis
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 1:   # Right now, we only need to compensate when outputing the swivel angle
                initialPlaneNormal = planarAxis.rotateBy(self.getLimbBRotation())
            
            planarVector = forwardAxis.rotateBy(rotation * self.initialLimbAWorldRotation.inverse())
            planarProjection = planarVector - (planarVector * planarAxis) * planarAxis
            planarAngle = planarProjection.angle(forwardAxis)
            if (forwardAxis ^ planarProjection) * planarAxis <= 0:
                planarAngle = 0 if planarAngle < math.pi / 2 else math.pi - 0.01
            planarRotation = OpenMaya.MQuaternion(planarAngle, planarAxis)
            
            BtoC_length = (self.initialLimbCWorldTranslation - self.initialLimbBWorldTranslation).length()
            newDirection = forwardAxis.rotateBy(planarRotation * self.initialLimbAWorldRotation)
            newLimbCPosition = self.initialLimbBWorldTranslation + BtoC_length * newDirection
            
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            limbCTransformFn.setTranslation(OpenMaya.MVector(newLimbCPosition), OpenMaya.MSpace.kWorld)
            
            swivelVector = OpenMaya.MVector.kYaxisVector.rotateBy(rotation * self.initialLimbBWorldRotation.inverse())
            swivelProjection = swivelVector - (swivelVector * forwardAxis) * forwardAxis
            swivelAngle = swivelProjection.angle(OpenMaya.MVector.kYaxisVector)
            if (OpenMaya.MVector.kYaxisVector ^ swivelProjection) * forwardAxis < 0:
                swivelAngle = -swivelAngle
            
            if swivelOutputMode == 0:
                AtoC_dir = (self.initialLimbCWorldTranslation - self.initialLimbAWorldTranslation).normal()
                swivelRotation = OpenMaya.MQuaternion(swivelAngle, AtoC_dir)
                AtoP = self.initialPoleVectorWorldTranslation - self.initialLimbAWorldTranslation
                newPoleVectorPosition = self.initialLimbAWorldTranslation + AtoP.rotateBy(swivelRotation)
                
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                poleVectorTransformFn.setTranslation(OpenMaya.MVector(newPoleVectorPosition), OpenMaya.MSpace.kWorld)

            elif swivelOutputMode == 1:
                cmds.dgdirty(self.limbADagPath.fullPathName())  # We need to mark the node as dirty in order for the previous changes to be reflected.
                limbATransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
                AtoC_currentDir = (limbCTransformFn.translation(OpenMaya.MSpace.kWorld) - limbATransformFn.translation(OpenMaya.MSpace.kWorld)).normal()
                newPlaneNormal = planarAxis.rotateBy(self.getLimbBRotation())
                compensationAngle = newPlaneNormal.angle(initialPlaneNormal)
                if (newPlaneNormal ^ initialPlaneNormal) * AtoC_currentDir < 0:
                    compensationAngle = -compensationAngle
                self.accumulatedSwivelAngleForCompensation += compensationAngle
                
                swivelAngle += self.accumulatedSwivelAngleForCompensation
                self.swivelPlug.setMAngle(OpenMaya.MAngle(self.initialSwivelAngle + swivelAngle, OpenMaya.MAngle.kRadians))
                
            if FKManipulatorController.isAffectEndRotation():
                limbBCurrentRotation = self.getLimbBRotation()
                relRotation = self.initialLimbCWorldRotation * self.initialLimbBWorldRotation.inverse()
                limbCTransformFn.setRotation(self.initialLimbCLocalRotation, OpenMaya.MSpace.kTransform)
                limbCTransformFn.rotateBy(self.initialLimbCWorldRotation.inverse() * (relRotation * limbBCurrentRotation), OpenMaya.MSpace.kWorld)
        
        def rotateOffset(self, offset, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
            
            rotation = self.initialLimbBWorldRotation * offset
            self.rotateToRotation(rotation, useCachedData=True)
        
        def getTargetPosition(self, useInitial=False):
            return self.initialLimbBWorldTranslation if useInitial else self.currentLimbBWorldTranslation
        
        def getTargetRotation(self, useInitial=False):
            targetRotation = self.initialLimbBWorldRotation if useInitial else self.currentLimbBWorldRotation
            parentRotation =  self.initialLimbAWorldRotation if useInitial else self.currentLimbAWorldRotation
            
            rotationMode = FKManipulatorController.getTransformMode()
            if rotationMode == "World":
                return OpenMaya.MQuaternion.kIdentity
            elif rotationMode == "Object" or rotationMode == "Gimbal":
                return targetRotation
            elif rotationMode == "Parent":
                return parentRotation
            else:
                return OpenMaya.MQuaternion.kIdentity
        
        def getAxis(self, useInitial=False):
            rotation = self.getTargetRotation(useInitial=useInitial)
            return [    # There is no particular distinction for any rotation mode, not even Gimbal
                OpenMaya.MVector(1, 0, 0).rotateBy(rotation),
                OpenMaya.MVector(0, 1, 0).rotateBy(rotation),
                OpenMaya.MVector(0, 0, 1).rotateBy(rotation)
            ]
        
        def storeInitialState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.initialLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.initialLimbBWorldTranslation = OpenMaya.MPoint(limbBTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            
            self.initialLimbBWorldRotation = self.getLimbBRotation(self.initialLimbBWorldTranslation, self.initialLimbCWorldTranslation)
            
            if FKManipulatorController.isAffectEndRotation():
                self.initialLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
                self.initialLimbCWorldRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 0:
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                self.initialPoleVectorWorldTranslation = OpenMaya.MPoint(poleVectorTransformFn.translation(OpenMaya.MSpace.kWorld))
            elif swivelOutputMode == 1:
                self.initialSwivelAngle = self.swivelPlug.asMAngle().asRadians()
            
            self.accumulatedSwivelAngleForCompensation = 0
        
        def storeCurrentState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbBTransformFn = OpenMaya.MFnTransform(self.limbBDagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.currentLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.currentLimbBWorldTranslation = OpenMaya.MPoint(limbBTransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            
            self.currentLimbBWorldRotation = self.getLimbBRotation(self.currentLimbBWorldTranslation, self.currentLimbCWorldTranslation)
            
            if FKManipulatorController.isAffectEndRotation():
                self.currentLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
                self.currentLimbCWorldRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 0:
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                self.currentPoleVectorWorldTranslation = OpenMaya.MPoint(poleVectorTransformFn.translation(OpenMaya.MSpace.kWorld))
            elif swivelOutputMode == 1:
                self.currentSwivelAngle = self.swivelPlug.asMAngle().asRadians()
        
        def drawSpecialManipulationShapes(self, manipulator, drawManager):
            if manipulator.glActiveName() == manipulator.xAxisHandle:
                AtoB = self.initialLimbBWorldTranslation - self.initialLimbAWorldTranslation
                AtoC = self.initialLimbCWorldTranslation - self.initialLimbAWorldTranslation
                AtoC_dir = AtoC.normal()
                projection = GeometryUtils.vectorProjection(AtoB, AtoC_dir, normalize=False)
                
                midPoint = self.initialLimbAWorldTranslation + projection
                radius = (AtoB - projection).length()
                
                midPointView = worldToView(manipulator.view, midPoint)
                    
                if manipulator.clickedPosition is not None:
                    limbBTranslationView = worldToView(manipulator.view, self.initialLimbBWorldTranslation)
                
                    drawManager.beginDrawable()
                    drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                    drawManager.circle(midPoint, AtoC, radius, filled=False)
                    drawManager.line2d(midPointView, limbBTranslationView)
                    drawManager.rect2d(midPointView, OpenMaya.MVector(0, 1, 0), 3, 3, filled = False)
                    drawManager.rect2d(limbBTranslationView, OpenMaya.MVector(0, 1, 0), 3, 3, filled = False)
                    drawManager.endDrawable()
                
                if manipulator.newClickedPosition is not None:
                    limbBTranslationView = worldToView(manipulator.view, self.currentLimbBWorldTranslation)
                    midToB_initialDir = (self.initialLimbBWorldTranslation - midPoint).normal()
                    midToB_currentDir = (self.currentLimbBWorldTranslation - midPoint).normal()
                    
                    drawManager.beginDrawable()
                    drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                    drawManager.line2d(midPointView, limbBTranslationView)
                    drawManager.rect2d(limbBTranslationView, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 0, 0.25)))
                    drawManager.arc(midPoint, midToB_initialDir, midToB_currentDir, midToB_initialDir ^ midToB_currentDir, radius * 0.5, filled=True)
                    drawManager.endDrawable()
                    
                    if FKManipulatorController.isAlternativeRotateMode():
                        clickedView = worldToView(manipulator.view, manipulator.clickedPosition)
                        newClickedView = worldToView(manipulator.view, manipulator.newClickedPosition)
                
                        drawManager.beginDrawable()
                        drawManager.setColor(OpenMaya.MColor((1, 1, 1, 1)))
                        drawManager.line2d(clickedView, newClickedView)
                        drawManager.rect2d(clickedView, OpenMaya.MVector(0, 1, 0), 3, 3, filled = False)
                        drawManager.rect2d(newClickedView, OpenMaya.MVector(0, 1, 0), 3, 3, filled = False)
                        drawManager.endDrawable()
                
                return True
            
            else:
                return False
        
        def getSpecialClickedPosition(self, manipulator, rayOrigin, rayDirection):
            if manipulator.glActiveName() == manipulator.xAxisHandle and not FKManipulatorController.isAlternativeRotateMode():
                AtoB = self.initialLimbBWorldTranslation - self.initialLimbAWorldTranslation
                AtoC = self.initialLimbCWorldTranslation - self.initialLimbAWorldTranslation
                BtoC = self.initialLimbCWorldTranslation - self.initialLimbBWorldTranslation
                AtoC_dir = AtoC.normal()
                BtoC_dir = BtoC.normal()
                projection = GeometryUtils.vectorProjection(AtoB, AtoC_dir, normalize=False)
                offsetRotation = OpenMaya.MQuaternion(AtoC_dir, BtoC_dir)
                
                midPoint = self.initialLimbAWorldTranslation + projection
                
                clickedPosition = GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, midPoint, AtoC_dir)[0]
                clickedPosition = midPoint + manipulator.radius * (clickedPosition - midPoint).normal().rotateBy(offsetRotation)
                
                return midPoint, clickedPosition
            
            else:
                return None, None   # No special way of handling the clicked position
        
    
    class ConnectedChainShoulder(object):
        
        class Undoer(object):
        
            def __init__(self, chain, affectEndRotation):
                chain.storeCurrentState()
                
                self.limbCDagPath = chain.limbCDagPath
                self.poleVectorDagPath = chain.poleVectorDagPath
                self.swivelPlug = chain.swivelPlug
                
                self.swivelOutputMode = chain.rigChain.ikSwivelOutputMode
                
                self.previousLimbCTranslation = chain.initialLimbCWorldTranslation
                self.currentLimbCTranslation = chain.currentLimbCWorldTranslation
                
                self.affectEndRotation = affectEndRotation
                if self.affectEndRotation:
                    self.previousLimbCRotation = chain.initialLimbCLocalRotation
                    self.currentLimbCRotation = chain.currentLimbCLocalRotation
                
                if self.swivelOutputMode == 0:
                    self.previousPoleVectorTranslation = chain.initialPoleVectorWorldTranslation
                    self.currentPoleVectorTranslation = chain.currentPoleVectorWorldTranslation
                
                elif self.swivelOutputMode == 1:
                    self.previousSwivelAngle = chain.initialSwivelAngle
                    self.currentSwivelAngle = chain.currentSwivelAngle
                
            def undoIt(self):
                limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                limbCTransformFn.setTranslation(OpenMaya.MVector(self.previousLimbCTranslation), OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn.setRotation(self.previousLimbCRotation, OpenMaya.MSpace.kTransform)
                
                if self.swivelOutputMode == 0:
                    poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                    poleVectorTransformFn.setTranslation(OpenMaya.MVector(self.previousPoleVectorTranslation), OpenMaya.MSpace.kWorld)
                
                elif self.swivelOutputMode == 1:
                    self.swivelPlug.setMAngle(OpenMaya.MAngle(self.previousSwivelAngle, OpenMaya.MAngle.kRadians))
                    
            def redoIt(self):
                limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
                limbCTransformFn.setTranslation(OpenMaya.MVector(self.currentLimbCTranslation), OpenMaya.MSpace.kWorld)
                
                if self.affectEndRotation:
                    limbCTransformFn.setRotation(self.currentLimbCRotation, OpenMaya.MSpace.kTransform)
                
                if self.swivelOutputMode == 0:
                    poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                    poleVectorTransformFn.setTranslation(OpenMaya.MVector(self.currentPoleVectorTranslation), OpenMaya.MSpace.kWorld)

                elif self.swivelOutputMode == 1:
                    self.swivelPlug.setMAngle(OpenMaya.MAngle(self.currentSwivelAngle, OpenMaya.MAngle.kRadians))


        def __init__(self, rigChain):
            self.rigChain = rigChain
            
            self.limbADagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbA)
            self.limbBDagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbB)
            self.limbCDagPath = OpenMayaUtils.asDagPath(rigChain.ikLimbC)
            self.poleVectorDagPath = OpenMayaUtils.asDagPath(rigChain.ikPoleVector)
            self.swivelPlug = OpenMayaUtils.asMPlug(rigChain.ikSwivelPlug)
            
            self.planarAxis = rigChain.ikPlanarAxis
            
            self.initialLimbCLocalRotation = None
            self.currentLimbCLocalRotation = None
        
            self.initialLimbAWorldTranslation = None
            self.initialLimbAWorldRotation = None
            self.initialLimbCWorldTranslation = None
            self.initialPoleVectorWorldTranslation = None
            self.initialSwivelAngle = None
            self.initialLimbAParentRotation = None
        
            self.currentLimbAWorldTranslation = None
            self.currentLimbAWorldRotation = None
            self.currentLimbCWorldTranslation = None
            self.currentPoleVectorWorldTranslation = None
            self.currentSwivelAngle = None
            self.currentLimbAParentRotation = None
            
            self.accumulatedSwivelAngleForCompensation = 0
            
        def __eq__(self, other):
            if issubclass(type(other), FKManipulator.ConnectedChainShoulder):
                return self.rigChain == other.rigChain
            return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def getPlanarAxisFromChain(self):
            return IKFKChain.getEnumAxis(self.planarAxis)
        
        def getUndoer(self):
            return self.Undoer(self, FKManipulatorController.isAffectEndRotation())
        
        def getHandlesToHide(self):
            return FKManipulator.HIDE_NO_HANDLES
        
        def rotateToRotation(self, rotation, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
                
            offset = self.initialLimbAWorldRotation.inverse() * rotation
            self.rotateOffset(offset, useCachedData=True)
        
        def rotateOffset(self, offset, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
                
            AtoC = self.initialLimbCWorldTranslation - self.initialLimbAWorldTranslation
            newLimbCPosition = self.initialLimbAWorldTranslation + AtoC.rotateBy(offset)
            
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            limbCTransformFn.setTranslation(OpenMaya.MVector(newLimbCPosition), OpenMaya.MSpace.kWorld)
            
            if FKManipulatorController.isAffectEndRotation():
                limbCTransformFn.setRotation(self.initialLimbCLocalRotation, OpenMaya.MSpace.kTransform)
                limbCTransformFn.rotateBy(offset, OpenMaya.MSpace.kWorld)
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 0:
                AtoP = self.initialPoleVectorWorldTranslation - self.initialLimbAWorldTranslation
                newPoleVectorPosition = self.initialLimbAWorldTranslation + AtoP.rotateBy(offset)
                
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                poleVectorTransformFn.setTranslation(OpenMaya.MVector(newPoleVectorPosition), OpenMaya.MSpace.kWorld)
                
            if swivelOutputMode == 1:
                cmds.dgdirty(self.limbADagPath.fullPathName())  # We need to mark the node as dirty in order for the previous changes to be reflected.
                planarAxis = self.getPlanarAxisFromChain()
                
                limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
                newPlaneNormal = planarAxis.rotateBy(limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True))
                desiredPlanarNormal = planarAxis.rotateBy(self.initialLimbAWorldRotation * offset)
                AtoC_currentDir = (OpenMaya.MPoint(newLimbCPosition) - self.initialLimbAWorldTranslation).normal()
                
                swivelAngle = newPlaneNormal.angle(desiredPlanarNormal)
                if (newPlaneNormal ^ desiredPlanarNormal).normal() * AtoC_currentDir < 0:
                    swivelAngle *= -1
                self.accumulatedSwivelAngleForCompensation += swivelAngle
                
                self.swivelPlug.setMAngle(OpenMaya.MAngle(self.initialSwivelAngle + self.accumulatedSwivelAngleForCompensation, OpenMaya.MAngle.kRadians))
        
        def getTargetPosition(self, useInitial=False):
            return self.initialLimbAWorldTranslation if useInitial else self.currentLimbAWorldTranslation
        
        def getTargetRotation(self, useInitial=False):
            limbAWorldRotation = self.initialLimbAWorldRotation if useInitial else self.currentLimbAWorldRotation
            parentRotation =  self.initialLimbAParentRotation if useInitial else self.currentLimbAParentRotation
            
            rotationMode = FKManipulatorController.getTransformMode()
            if rotationMode == "World":
                return OpenMaya.MQuaternion.kIdentity
            elif rotationMode == "Object" or rotationMode == "Gimbal":
                return limbAWorldRotation
            elif rotationMode == "Parent":
                return parentRotation
            else:
                return OpenMaya.MQuaternion.kIdentity
        
        def getAxis(self, useInitial=False):
            rotation = self.getTargetRotation(useInitial=useInitial)
            return [    # There is no particular distinction for any rotation mode, not even Gimbal
                OpenMaya.MVector(1, 0, 0).rotateBy(rotation),
                OpenMaya.MVector(0, 1, 0).rotateBy(rotation),
                OpenMaya.MVector(0, 0, 1).rotateBy(rotation)
            ]
        
        def storeInitialState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.initialLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kTransform)
            self.initialLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            
            self.initialLimbAParentRotation = OpenMaya.MTransformationMatrix(self.limbADagPath.exclusiveMatrix()).rotation(asQuaternion=True)
            
            if FKManipulatorController.isAffectEndRotation():
                self.initialLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 0:
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                self.initialPoleVectorWorldTranslation = OpenMaya.MPoint(poleVectorTransformFn.translation(OpenMaya.MSpace.kWorld))
            elif swivelOutputMode == 1:
                self.initialSwivelAngle = self.swivelPlug.asMAngle().asRadians()
            
            self.accumulatedSwivelAngleForCompensation = 0
        
        def storeCurrentState(self):
            limbATransformFn = OpenMaya.MFnTransform(self.limbADagPath)
            limbCTransformFn = OpenMaya.MFnTransform(self.limbCDagPath)
            
            self.currentLimbAWorldTranslation = OpenMaya.MPoint(limbATransformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentLimbAWorldRotation = limbATransformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            self.currentLimbCWorldTranslation = OpenMaya.MPoint(limbCTransformFn.translation(OpenMaya.MSpace.kWorld))
            
            self.currentLimbAParentRotation = OpenMaya.MTransformationMatrix(self.limbADagPath.exclusiveMatrix()).rotation(asQuaternion=True)
            
            if FKManipulatorController.isAffectEndRotation():
                self.currentLimbCLocalRotation = limbCTransformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            swivelOutputMode = self.rigChain.ikSwivelOutputMode
            if swivelOutputMode == 0:
                poleVectorTransformFn = OpenMaya.MFnTransform(self.poleVectorDagPath)
                self.currentPoleVectorWorldTranslation = OpenMaya.MPoint(poleVectorTransformFn.translation(OpenMaya.MSpace.kWorld))
            elif swivelOutputMode == 1:
                self.currentSwivelAngle = self.swivelPlug.asMAngle().asRadians()
        
        def drawSpecialManipulationShapes(self, manipulator, drawManager):
            return False    # No special shapes to draw
        
        def getSpecialClickedPosition(self, manipulator, rayOrigin, rayDirection):
            return None, None   # No special way of handling the clicked position
        
    
    class ConnectedNormalNode(object):
        
        class Undoer(object):
        
            def __init__(self, node):
                node.storeCurrentState()
                
                self.nodeDagPath = node.dagPath
                self.previousNodeRotation = node.initialLocalRotation
                self.currentNodeRotation = node.currentLocalRotation
                
            def undoIt(self):
                transformFn = OpenMaya.MFnTransform(self.nodeDagPath)
                transformFn.setRotation(self.previousNodeRotation, OpenMaya.MSpace.kTransform)
                
            def redoIt(self):
                transformFn = OpenMaya.MFnTransform(self.nodeDagPath)
                transformFn.setRotation(self.currentNodeRotation, OpenMaya.MSpace.kTransform)


        def __init__(self, node):
            self.dagPath = OpenMayaUtils.asDagPath(node)
            
            self.initialWorldTranslation = None
            self.initialWorldRotation = None
            self.initialLocalRotation = None
            self.initialParentWorldRotation = None
            
            self.currentWorldTranslation = None
            self.currentWorldRotation = None
            self.currentLocalRotation = None
            self.currentParentWorldRotation = None
            
        def __eq__(self, other):
            if issubclass(type(other), FKManipulator.ConnectedNormalNode):            
                return self.dagPath == other.dagPath
            return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def getUndoer(self):
            return self.Undoer(self)
        
        def getHandlesToHide(self):
            handlesToHide = FKManipulator.HIDE_NO_HANDLES
            
            transformMode = FKManipulatorController.getTransformMode()
            shouldHide = transformMode == "Gimbal"
            
            if shouldHide:
                handlesToHide |= FKManipulator.HIDE_ROTATE_3D_HANDLE | FKManipulator.HIDE_ROTATE_VIEW_HANDLE
                
                nodeFn = OpenMaya.MFnDependencyNode(self.dagPath.node())
                rotateXPlug = nodeFn.findPlug("rotateX", False)
                rotateYPlug = nodeFn.findPlug("rotateY", False)
                rotateZPlug = nodeFn.findPlug("rotateZ", False)
                
                if rotateXPlug.isNull or rotateXPlug.isLocked:
                    handlesToHide |= FKManipulator.HIDE_ROTATE_X_HANDLE
                if rotateYPlug.isNull or rotateYPlug.isLocked:
                    handlesToHide |= FKManipulator.HIDE_ROTATE_Y_HANDLE
                if rotateZPlug.isNull or rotateZPlug.isLocked:
                    handlesToHide |= FKManipulator.HIDE_ROTATE_Z_HANDLE
            
            return handlesToHide
        
        def rotateToRotation(self, rotation, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
            
            offset = rotation * self.initialWorldRotation.inverse()
            self.rotateOffset(offset, useCachedData=True)
        
        def rotateOffset(self, offset, useCachedData=False):
            if not useCachedData:
                self.storeInitialState()
            
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            transformFn.setRotation(self.initialLocalRotation, OpenMaya.MSpace.kTransform)
            transformFn.rotateBy(offset, OpenMaya.MSpace.kWorld)
        
        def getTargetPosition(self, useInitial=False):
            return self.initialWorldTranslation if useInitial else self.currentWorldTranslation
        
        def getTargetRotation(self, useInitial=False):
            rotation = self.initialWorldRotation if useInitial else self.currentWorldRotation
            parentRotation = self.initialParentWorldRotation if useInitial else self.currentParentWorldRotation
            
            rotationMode = FKManipulatorController.getTransformMode()
            if rotationMode == "World":
                return OpenMaya.MQuaternion.kIdentity
            elif rotationMode == "Object" or rotationMode == "Gimbal":
                return rotation
            elif rotationMode == "Parent":
                return parentRotation
            else:
                return OpenMaya.MQuaternion.kIdentity
        
        def getAxis(self, useInitial=False):
            rotation = self.getTargetRotation(useInitial=useInitial)
            transformMode = FKManipulatorController.getTransformMode()
            if transformMode == "Gimbal":
                nodeFn = OpenMaya.MFnDependencyNode(self.dagPath.node())
                rotateOrder = nodeFn.findPlug("rotateOrder", False).asShort()
                
                euler = rotation.asEulerRotation().reorder(rotateOrder)
                axisIndices = MayaUtils.getAxisFromRotateOrder(rotateOrder)
                axis = [OpenMaya.MVector(1, 0, 0), OpenMaya.MVector(0, 1, 0), OpenMaya.MVector(0, 0, 1)]
                r1 = OpenMaya.MQuaternion(euler[axisIndices[2]], axis[axisIndices[2]])
                r2 = OpenMaya.MQuaternion(euler[axisIndices[1]], axis[axisIndices[1]])
                
                transformedAxis = [None, None, None]
                transformedAxis[axisIndices[0]] = axis[axisIndices[0]].rotateBy(r2 * r1)
                transformedAxis[axisIndices[1]] = axis[axisIndices[1]].rotateBy(r1)
                transformedAxis[axisIndices[2]] = axis[axisIndices[2]]
                return transformedAxis
            else:
                return [
                    OpenMaya.MVector(1, 0, 0).rotateBy(rotation),
                    OpenMaya.MVector(0, 1, 0).rotateBy(rotation),
                    OpenMaya.MVector(0, 0, 1).rotateBy(rotation)
                ]
        
        def storeInitialState(self):
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            self.initialWorldTranslation = OpenMaya.MPoint(transformFn.translation(OpenMaya.MSpace.kWorld))
            self.initialWorldRotation = transformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            self.initialLocalRotation = transformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            parentMatrix = OpenMaya.MTransformationMatrix(self.dagPath.exclusiveMatrix())
            self.initialParentWorldRotation = parentMatrix.rotation(asQuaternion=True)
            
        def storeCurrentState(self):
            transformFn = OpenMaya.MFnTransform(self.dagPath)
            self.currentWorldTranslation = OpenMaya.MPoint(transformFn.translation(OpenMaya.MSpace.kWorld))
            self.currentWorldRotation = transformFn.rotation(OpenMaya.MSpace.kWorld, asQuaternion=True)
            
            self.currentLocalRotation = transformFn.rotation(OpenMaya.MSpace.kTransform, asQuaternion=False)
            
            parentMatrix = OpenMaya.MTransformationMatrix(self.dagPath.exclusiveMatrix())
            self.currentParentWorldRotation = parentMatrix.rotation(asQuaternion=True)

        def drawSpecialManipulationShapes(self, manipulator, drawManager):
            return False    # No special shapes to draw
        
        def getSpecialClickedPosition(self, manipulator, rayOrigin, rayDirection):
            return None, None   # No special way of handling the clicked position
        
    
    nodeName = "fkManip"
    
    HIDE_NO_HANDLES = 0
    HIDE_ROTATE_X_HANDLE = 2
    HIDE_ROTATE_Y_HANDLE = 4
    HIDE_ROTATE_Z_HANDLE = 8
    HIDE_ROTATE_VIEW_HANDLE = 16
    HIDE_ROTATE_3D_HANDLE = 32
    HIDE_ROTATE_HANDLES = HIDE_ROTATE_X_HANDLE | HIDE_ROTATE_Y_HANDLE | HIDE_ROTATE_Z_HANDLE | HIDE_ROTATE_VIEW_HANDLE | HIDE_ROTATE_3D_HANDLE

    VIEW_HANDLE_RADIUS_FACTOR = 1.15

    @staticmethod
    def creator():
        return FKManipulator()
    
    @staticmethod
    def initialize():
        pass
    
    def __init__(self):
        OpenMayaUI.MPxManipulatorNode.__init__(self)
        
        self.connectedItems = []
        
        self.targetToDraw = None
        
        self.xAxisHandle = None
        self.yAxisHandle = None
        self.zAxisHandle = None
        self.viewHandle = None
        self.r3DHandle = None
        
        self.radius = None
        self.zoomRatio = None
        self.view = None
        self.clickedView = None
        self.cameraRotation = None
        
        self.clickedPosition = None
        self.newClickedPosition = None
    
    def connectToDependNode(self, node):
        dependencyNodeFn = OpenMaya.MFnDependencyNode(node)
        messagePlug = dependencyNodeFn.findPlug("message", False)
        connections = messagePlug.connectedTo(False, True)
        isChain = False
        for connection in connections:
            if OpenMaya.MFnDependencyNode(connection.node()).typeName == IKFKChain._Type:
                rigChain = IKFKChain(connection.node())
                if connection.partialName(useLongNames=True) == "ikLimbB":
                    conn = FKManipulator.ConnectedChainElbow(rigChain)
                    if conn not in self.connectedItems:
                        self.connectedItems.append(conn)
                    isChain = True
                elif connection.partialName(useLongNames=True) == "ikLimbA":
                    conn = FKManipulator.ConnectedChainShoulder(rigChain)
                    if conn not in self.connectedItems:
                        self.connectedItems.append(conn)
                    isChain = True
        if not isChain:
            self.connectedItems.append(FKManipulator.ConnectedNormalNode(node))
    
    def getTargetToDraw(self):
        if len(self.connectedItems) > 0:
            return self.connectedItems[-1]
        else:
            return None
    
    def rotateToRotation(self, rotation, useCachedData=False):
        for item in self.connectedItems:
            item.rotateToRotation(rotation, useCachedData=useCachedData)
    
    def rotateOffset(self, offset, target, useCachedData=False):
        axis, angle = offset.asAxisAngle()
        axis = axis.rotateBy(target.getTargetRotation(useInitial=True).inverse())
        for item in self.connectedItems:
            itemOffset = OpenMaya.MQuaternion(angle, axis.rotateBy(item.getTargetRotation(useInitial=True)))
            item.rotateOffset(itemOffset, useCachedData=useCachedData)
    
    def preDrawUI(self, view):
        self.targetToDraw = self.getTargetToDraw()
        if self.targetToDraw != None:
            self.targetToDraw.storeCurrentState()
            self.zoomRatio = getCameraZoomRatio(view.getCamera(), self.targetToDraw.getTargetPosition(), viewportWidth=view.portWidth())
            self.cameraRotation = getNodeWorldRotation(view.getCamera())
            
            if self.clickedView == None or view == self.clickedView:
                self.radius = FKManipulatorController.getRotateDisplayRadius() * self.zoomRatio * OpenMayaUI.MFnManip3D.globalSize()
                self.view = view
            
    def drawUI(self, drawManager, frameContext):
        if self.targetToDraw == None:
            return
        
        targetPosition = self.targetToDraw.getTargetPosition()
        axis = self.targetToDraw.getAxis()
        
        handlesToHide = self.targetToDraw.getHandlesToHide()
        if self.clickedPosition is not None:
            pass    # No handles need to be hidden right now
        
        handle = self.glFirstHandle()
        self.r3DHandle = handle
        draw3DHandle = not (handlesToHide & self.HIDE_ROTATE_3D_HANDLE)
        if draw3DHandle:
            if self.glActiveName() == self.r3DHandle:
                backgroundColor = OpenMaya.MColor((0, 0, 0, 0.1))
            elif self.shouldDrawHandleAsSelected(self.r3DHandle):
                backgroundColor = OpenMaya.MColor((0, 0, 0, 0.075))
            else:
                backgroundColor = OpenMaya.MColor((0, 0, 0, 0))
                
            drawManager.beginDrawable(selectability=draw3DHandle, selectionName=handle)
            drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sDormantFilledDepthPriority)
            drawManager.setColor(backgroundColor)
            drawManager.sphere(targetPosition, self.radius * 0.95, filled=True)
            drawManager.endDrawable()
            
        if handlesToHide != self.HIDE_ROTATE_HANDLES:
            drawManager.beginDrawable()
            drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sDormantWireDepthPriority)
            drawManager.setColor(OpenMaya.MColor((0, 0, 0, 0.666)))
            drawManager.setLineWidth(1)
            drawManager.circle(targetPosition, OpenMaya.MVector(0, 0, 1).rotateBy(self.cameraRotation), self.radius, filled=False)
            drawManager.endDrawable()
        
        handle += 1
        self.xAxisHandle = handle
        if not (handlesToHide & self.HIDE_ROTATE_X_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.drawRotationArc(drawManager, targetPosition, axis[0], handle, self.xColor(), self.radius, extraThick=draw3DHandle)
            drawManager.endDrawable()
        
        handle += 1
        self.yAxisHandle = handle
        if not (handlesToHide & self.HIDE_ROTATE_Y_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.drawRotationArc(drawManager, targetPosition, axis[1], handle, self.yColor(), self.radius, extraThick=draw3DHandle)
            drawManager.endDrawable()
        
        handle += 1
        self.zAxisHandle = handle
        if not (handlesToHide & self.HIDE_ROTATE_Z_HANDLE):
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.drawRotationArc(drawManager, targetPosition, axis[2], handle, self.zColor(), self.radius, extraThick=draw3DHandle)
            drawManager.endDrawable()
        
        handle += 1
        self.viewHandle = handle
        if not (handlesToHide & self.HIDE_ROTATE_VIEW_HANDLE):            
            drawManager.beginDrawable(selectability=True, selectionName=handle)
            self.drawRotationCircle(drawManager, targetPosition, OpenMaya.MVector(0, 0, 1).rotateBy(self.cameraRotation), handle, self.mainColor(), self.radius * self.VIEW_HANDLE_RADIUS_FACTOR)
            drawManager.endDrawable()
        
        if not self.targetToDraw.drawSpecialManipulationShapes(self, drawManager):
            if self.clickedPosition is not None:
                targetView = worldToView(self.view, targetPosition)
                clickedView = worldToView(self.view, self.clickedPosition)
                
                drawManager.beginDrawable()
                drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                drawManager.line2d(targetView, clickedView)
                drawManager.rect2d(clickedView, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                drawManager.endDrawable()
            
            if self.newClickedPosition is not None:
                clickedDir = (self.clickedPosition - targetPosition).normal()
                newClickedDir = (self.newClickedPosition - targetPosition).normal()
                clickedRadius = (self.radius * self.VIEW_HANDLE_RADIUS_FACTOR) if self.glActiveName() == self.viewHandle else self.radius
                
                if FKManipulatorController.isAlternativeRotateMode():
                    start = clickedView
                    end = worldToView(self.view, self.newClickedPosition)
                else:
                    start = targetView
                    end = worldToView(self.view, self.newClickedPosition)
                drawManager.beginDrawable()
                drawManager.setColor(OpenMaya.MColor((1, 1, 1, 1)))
                drawManager.line2d(start, end)
                drawManager.rect2d(end, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                drawManager.endDrawable()
                
                if FKManipulatorController.isAlternativeRotateMode():
                    initialRotation = self.targetToDraw.getTargetRotation(useInitial=True)
                    currentRotation = self.targetToDraw.getTargetRotation(useInitial=False)
                    newDir = clickedDir.rotateBy(initialRotation.inverse() * currentRotation)
                    newDirPos = worldToView(self.view, targetPosition + clickedRadius * newDir)
                    
                    drawManager.beginDrawable()
                    drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 1, 0.5)))
                    drawManager.line2d(targetView, newDirPos)
                    drawManager.rect2d(newDirPos, OpenMaya.MVector(0, 1, 0), 3, 3, False)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 0, 0.25)))
                    drawManager.arc(targetPosition, clickedDir, newDir, clickedDir ^ newDir, self.radius * 0.5, filled=True)
                    drawManager.endDrawable()
                else:
                    drawManager.beginDrawable()
                    drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sActiveWireDepthPriority)
                    drawManager.setColor(OpenMaya.MColor((1, 1, 0, 0.25)))
                    drawManager.arc(targetPosition, clickedDir, newClickedDir, clickedDir ^ newClickedDir, self.radius * 0.5, filled=True)
                    drawManager.endDrawable()
    
    def drawRotationArc(self, drawManager, origin, normal, handle, color, radius, extraThick=False):
        cameraDir = OpenMaya.MVector(0, 0, 1).rotateBy(self.cameraRotation)
        start = (cameraDir ^ normal).normal()
        
        if extraThick:
            drawManager.setColor(OpenMaya.MColor((0, 0, 0, 0)))
            drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sDormantFilledDepthPriority) 
            drawManager.cylinder(origin, normal, radius * 0.98, radius * 0.2, 32, filled=True)
        
        self.setHandleColor(drawManager, handle, color)
        drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sHiliteWireDepthPriority) 
        drawManager.setLineWidth(OpenMayaUI.MFnManip3D.lineSize())
        drawManager.arc(origin, start, -start, normal, radius, filled=False)

    def drawRotationCircle(self, drawManager, origin, normal, handle, color, radius):
        self.setHandleColor(drawManager, handle, color)
        drawManager.setDepthPriority(OpenMayaRender.MRenderItem.sHiliteWireDepthPriority) 
        drawManager.setLineWidth(OpenMayaUI.MFnManip3D.lineSize())
        drawManager.circle(origin, normal, radius, filled=False)
    
    def getHandleAxis(self, handle, view):
        if handle == self.xAxisHandle:
            return self.targetToDraw.getAxis(useInitial=True)[0]
        elif handle == self.yAxisHandle:
            return self.targetToDraw.getAxis(useInitial=True)[1]
        elif handle == self.zAxisHandle:
            return self.targetToDraw.getAxis(useInitial=True)[2]
        elif handle == self.viewHandle:
            return OpenMaya.MVector(0, 0, 1).rotateBy(getNodeWorldRotation(view.getCamera()))
        else:
            raise NotImplementedError("Unsupported handle: {}".format(handle))
    
    def getActiveAxis(self, view):
        return self.getHandleAxis(self.glActiveName(), view)
        
    def getClickedPosition(self, rayOrigin, rayDirection, origin, view):
        activeHandle = self.glActiveName()        
        if activeHandle == self.r3DHandle:
            return GeometryUtils.rayIntersectionOnSphere(rayOrigin, rayDirection, origin, self.radius)[0]
        else:
            axis = self.getActiveAxis(view)
            intersection, doesIntersect = GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, origin, axis)
            if not doesIntersect:   # If parallel to the circle, intersects with the sphere to find a proper click point
                rayOrigin = rayOrigin - GeometryUtils.vectorProjection(rayOrigin - origin, axis)
                intersection = GeometryUtils.rayIntersectionOnSphere(rayOrigin, rayDirection, origin, self.radius)[0]
            clickedRadius = self.radius * self.VIEW_HANDLE_RADIUS_FACTOR if activeHandle == self.viewHandle else self.radius
            clickedDir = (intersection - origin).normal()
            return origin + clickedRadius * clickedDir
    
    def doPress(self, view):
        if self.targetToDraw == None:
            return
        
        self.clickedView = view
        
        for item in self.connectedItems:
            item.storeInitialState()
        
        rayOrigin, rayDirection = self.mouseRayWorld()
        targetPosition, self.clickedPosition = self.targetToDraw.getSpecialClickedPosition(self, rayOrigin, rayDirection)
        if targetPosition is None:
            targetPosition = self.targetToDraw.getTargetPosition(useInitial=True)
            self.clickedPosition = self.getClickedPosition(rayOrigin, rayDirection, targetPosition, view)
    
    def doDrag(self, view):
        if self.targetToDraw == None:
            return
        
        rayOrigin, rayDirection = self.mouseRayWorld()
        targetPosition, self.newClickedPosition = self.targetToDraw.getSpecialClickedPosition(self, rayOrigin, rayDirection)
        if targetPosition is not None:
            startDirection = (self.clickedPosition - targetPosition).normal()
            endDirection = (self.newClickedPosition - targetPosition).normal()
            axis = (startDirection ^ endDirection).normal()
            rotation = OpenMaya.MQuaternion(endDirection.angle(startDirection), axis)
            
        else:
            targetPosition = self.targetToDraw.getTargetPosition(useInitial=True)
            startDirection = (self.clickedPosition - targetPosition).normal()
            
            if FKManipulatorController.isAlternativeRotateMode():
                if self.glActiveName() == self.r3DHandle:
                    self.newClickedPosition = GeometryUtils.rayIntersectionOnPlane(rayOrigin, rayDirection, self.clickedPosition, startDirection)[0]
                    perpendicular = (self.newClickedPosition - self.clickedPosition).normal()
                    axis = startDirection ^ perpendicular
                else:
                    axis = self.getActiveAxis(view)
                    perpendicular = (axis ^ startDirection).normal()
                    self.newClickedPosition = GeometryUtils.rayIntersectionOnLine(rayOrigin, rayDirection, self.clickedPosition, perpendicular)[0]
                zoomRatio = getCameraZoomRatio(view.getCamera(), targetPosition, viewportWidth=view.portWidth())
                distance = FKManipulatorController.getAlternativeRotateModeSensibility() * (self.newClickedPosition - self.clickedPosition) * perpendicular / zoomRatio    # Since we are using distance units to apply an angle, we use the camera zoom ratio to be more consistent
                rotation = OpenMaya.MQuaternion(distance, axis)
                
            else:
                self.newClickedPosition = self.getClickedPosition(rayOrigin, rayDirection, targetPosition, view)
                endDirection = (self.newClickedPosition - targetPosition).normal()
                axis = (startDirection ^ endDirection).normal()
                rotation = OpenMaya.MQuaternion(endDirection.angle(startDirection), axis)
                
        self.rotateOffset(rotation, self.targetToDraw, useCachedData=True)
    
    def doRelease(self, view):
        if self.targetToDraw == None:
            return
        
        undoers = []
        for item in self.connectedItems:
            undoers.append(item.getUndoer())
            
        ApiUndo.UndoOverwrite(undoers).commit()
        
        self.clickedView = None
        self.clickedPosition = None
        self.newClickedPosition = None


class FKManipulatorContext(OpenMayaUI.MPxSelectionContext):

    def __init__(self):
        OpenMayaUI.MPxSelectionContext.__init__(self)
        
        self.callback = None
        
        self.manipulator = None
    
    def stringClassName(self):
        return FKManipulatorController.CONTEXT_CLASS
    
    def toolOnSetup(self, event):
        self.setTitleString("FKManipulator")
        self.setHelpString("Move an IK chain like it was FK.")
        self.setImage(FKManipulatorController.CONTEXT_IMAGE, self.kImage1)
        
        self.updateManipulators()
        self.callback = OpenMaya.MModelMessage.addCallback(OpenMaya.MModelMessage.kActiveListModified, self.updateManipulators)
    
    def toolOffCleanup(self):
        self.deleteManipulators()
        OpenMaya.MMessage.removeCallback(self.callback)
    
    def updateManipulators(self, *args):
        self.deleteManipulators()
        
        sl = OpenMaya.MGlobal.getActiveSelectionList()
        if sl.length() > 0:
            self.manipulator, manipObject = FKManipulator.newManipulator("fkManip")
            self.addManipulator(manipObject)
            
            iter = OpenMaya.MItSelectionList(sl, OpenMaya.MFn.kInvalid)
            while not iter.isDone():
                dependNode = iter.getDependNode()
                iter.next()
                
                if dependNode.isNull() or not dependNode.hasFn(OpenMaya.MFn.kTransform):
                    continue
                
                self.manipulator.connectToDependNode(dependNode)
        else:
            self.manipulator = None
                
        self.feedbackNumericalInput()
    
    def argTypeNumericalInput(self, argIndex):
        return OpenMaya.MSyntax.kAngle
    
    def processNumericalInput(self, values, flags, isAbsolute):
        # We should be implementing the feedbackNumericalInput method to update the input box with the manipulator data.
        # But it relies on the class MFeedbackLine wich is not implemented on the API 2.0 (the 1.0 version does nothing).
        # Even then, the procedure that updates the input box doesn't seem to read any data and instead it just clears the text fields.
        # So yeah, no chance :)
        
        if self.manipulator == None:
            return False
        
        # NOTE: This will always apply the values in world space. This could be improved to use the current manipulation space.
        # However Mayas default rotation doesn't even do this and always works in world space so...
        
        undoers = []
        for item in self.manipulator.connectedItems:
            item.storeInitialState()
            values = OpenMaya.MEulerRotation(values)
            
            if isAbsolute:
                rotation = item.getTargetRotation(useInitial=True).asEulerRotation()
                if self.ignoreEntry(flags, 0):
                    values.x = rotation.x
                if self.ignoreEntry(flags, 1):
                    values.y = rotation.y
                if self.ignoreEntry(flags, 2):
                    values.z = rotation.z
                item.rotateToRotation(values.asQuaternion(), useCachedData=True)
            
            else:
                if self.ignoreEntry(flags, 0):
                    values.x = 0
                if self.ignoreEntry(flags, 1):
                    values.y = 0
                if self.ignoreEntry(flags, 2):
                    values.z = 0
                item.rotateOffset(values.asQuaternion(), useCachedData=True)
            
            undoers.append(item.getUndoer())
            
        ApiUndo.UndoOverwrite(undoers).commit()
        
        return True
    
    def ignoreEntry(self, flags, index):
        # This method should be provided by Maya, but it is not implemented on the API 2.0 :)
        # We have to add it ourselves, so it might not work as expected on certain situations.
        
        # It seems that falgs 2, 3 and 4 indicate if we should ignore the X, Y and Z coordinates respectively.
        return flags[2 + index] == 1


class FKManipulatorContextCommand(OpenMayaUI.MPxContextCommand):
    
    @staticmethod
    def creator():
        return FKManipulatorContextCommand()
    
    def makeObj(self):
        return FKManipulatorContext()


# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    try:
        mplugin.registerNode(IKManipulator.nodeName, NodeID.IKManipulatorID, IKManipulator.creator, IKManipulator.initialize, OpenMaya.MPxNode.kManipulatorNode)
        mplugin.registerNode(FKManipulator.nodeName, NodeID.FKManipulatorID, FKManipulator.creator, FKManipulator.initialize, OpenMaya.MPxNode.kManipulatorNode)
    except:
        sys.stderr.write("Failed to register manipulator nodes!")
        raise

    try:
        mplugin.registerContextCommand(IKManipulatorController.CONTEXT_NAME, IKManipulatorContextCommand.creator)
        mplugin.registerContextCommand(FKManipulatorController.CONTEXT_NAME, FKManipulatorContextCommand.creator)
    except:
        sys.stderr.write("Failed to register context commands!")
        raise

    try:
        ManipulatorCommon.load()
    except:
        sys.stderr.write("Failed to load the additional configuration for the IKManipulator tool.")
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMaya.MFnPlugin(mobject)

    try:
        mplugin.deregisterNode(NodeID.IKManipulatorID)
        mplugin.deregisterNode(NodeID.FKManipulatorID)
    except:
        sys.stderr.write("Failed to unregister manipulator nodes!")
        raise

    try:
        mplugin.deregisterContextCommand(IKManipulatorController.CONTEXT_NAME)
        mplugin.deregisterContextCommand(FKManipulatorController.CONTEXT_NAME)
    except:
        sys.stderr.write("Failed to unregister context commands!")
        raise

    try:
        ManipulatorCommon.unload()
    except:
        sys.stderr.write("Failed to unregister the additional configuration for the IKManipulator tool.")
        raise
