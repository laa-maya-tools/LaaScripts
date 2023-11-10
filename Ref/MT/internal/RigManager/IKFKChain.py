import maya.cmds as cmds

import maya.api.OpenMaya as OpenMaya
import Utils.OpenMaya as OpenMayaUtils

from RigManager.RigChain import RigChain

from Utils.Maya.UndoContext import UndoContext
import Utils.Python.Math as MathUtils

import math

class IKFKChain(RigChain):
    
    # Static ----------------

    axisEnum = [
        ("X", OpenMaya.MVector.kXaxisVector),
        ("Y", OpenMaya.MVector.kYaxisVector),
        ("Z", OpenMaya.MVector.kZaxisVector),
        ("-X", OpenMaya.MVector.kXnegAxisVector),
        ("-Y", OpenMaya.MVector.kYnegAxisVector),
        ("-Z", OpenMaya.MVector.kZnegAxisVector)
    ]
    
    @classmethod
    def getEnumAxis(cls, index):
        return cls.axisEnum[index][1]
    
    # Wrapper ---------------
        
    _Type = "IKFKChain"
    
    # Attributes ------------
    
    _fkLimbA = "fkLimbA"
    _fkLimbB = "fkLimbB"
    _fkLimbC = "fkLimbC"
    _fkLimbCuadruped = "fkLimbCuadruped"
    _fkPlanarAxis = "fkPlanarAxis"
    
    _ikLimbA = "ikLimbA"
    _ikLimbB = "ikLimbB"
    _ikLimbC = "ikLimbC"
    _ikPlanarAxis = "ikPlanarAxis"
    _ikPoleVector = "ikPoleVector"
    _ikSwivelPlug = "ikSwivelPlug"
    _ikSwivelOutputMode = "ikSwivelOutputMode"
    
    _ikFkBlendPlug = "ikFkBlendPlug"
    _swivelCombineMode = "swivelCombineMode"
    
    _autoSnap = "autoSnap"
    
    # Properties ------------
        
    @property
    def fkLimbA(self):
        return self.getInputSingle(self._fkLimbA)
    
    @fkLimbA.setter
    def fkLimbA(self, value):
        with UndoContext("Set Chain FK Limb A"):
            self.setInputNode(self._fkLimbA, value)
        
    @property
    def fkLimbB(self):
        return self.getInputSingle(self._fkLimbB)
    
    @fkLimbB.setter
    def fkLimbB(self, value):
        with UndoContext("Set Chain FK Limb B"):
            self.setInputNode(self._fkLimbB, value)
        
    @property
    def fkLimbC(self):
        return self.getInputSingle(self._fkLimbC)
    
    @fkLimbC.setter
    def fkLimbC(self, value):
        with UndoContext("Set Chain FK Limb C"):
            self.setInputNode(self._fkLimbC, value)
        
    @property
    def fkLimbCuadruped(self):
        return self.getInputSingle(self._fkLimbCuadruped)
    
    @fkLimbCuadruped.setter
    def fkLimbCuadruped(self, value):
        with UndoContext("Set Chain FK Limb Cuadruped"):
            self.setInputNode(self._fkLimbCuadruped, value)
        
    @property
    def fkPlanarAxis(self):
        return self.getAttr(self._fkPlanarAxis)
    
    @fkPlanarAxis.setter
    def fkPlanarAxis(self, value):
        with UndoContext("Set Chain FK Planar Axis"):
            self.setNumericAttribute(self._fkPlanarAxis, value)
        
    @property
    def ikLimbA(self):
        return self.getInputSingle(self._ikLimbA)
    
    @ikLimbA.setter
    def ikLimbA(self, value):
        with UndoContext("Set Chain IK Limb A"):
            self.setInputNode(self._ikLimbA, value)
        
    @property
    def ikLimbB(self):
        return self.getInputSingle(self._ikLimbB)
    
    @ikLimbB.setter
    def ikLimbB(self, value):
        with UndoContext("Set Chain IK Limb B"):
            self.setInputNode(self._ikLimbB, value)
    
    @property
    def ikLimbC(self):
        return self.getInputSingle(self._ikLimbC)
    
    @ikLimbC.setter
    def ikLimbC(self, value):
        with UndoContext("Set Chain IK Limb C"):
            self.setInputNode(self._ikLimbC, value)
        
    @property
    def ikPlanarAxis(self):
        return self.getAttr(self._ikPlanarAxis)
    
    @ikPlanarAxis.setter
    def ikPlanarAxis(self, value):
        with UndoContext("Set Chain IK Planar Axis"):
            self.setNumericAttribute(self._ikPlanarAxis, value)
        
    @property
    def ikPoleVector(self):
        return self.getInputSingle(self._ikPoleVector)
    
    @ikPoleVector.setter
    def ikPoleVector(self, value):
        with UndoContext("Set Chain Pole Vector"):
            self.setInputNode(self._ikPoleVector, value)
        
    @property
    def ikSwivelPlug(self):
        return self.getInputSingle(self._ikSwivelPlug, plugs=True)
    
    @ikSwivelPlug.setter
    def ikSwivelPlug(self, value):
        with UndoContext("Set Chain Swivel Plug"):
            self.connect(self.getPlug(self._ikSwivelPlug), input=value)
        
    @property
    def ikSwivelOutputMode(self):
        return self.getAttr(self._ikSwivelOutputMode)
    
    @ikSwivelOutputMode.setter
    def ikSwivelOutputMode(self, value):
        with UndoContext("Set Chain Swivel Output Mode"):
            self.setNumericAttribute(self._ikSwivelOutputMode, value)
        
    @property
    def ikFkBlendPlug(self):
        return self.getInputSingle(self._ikFkBlendPlug, plugs=True)
    
    @ikFkBlendPlug.setter
    def ikFkBlendPlug(self, value):
        with UndoContext("Set Chain IK/FK Blend Plug"):
            self.connect(self.getPlug(self._ikFkBlendPlug), input=value)
    
    @property
    def swivelCombineMode(self):
        return self.getAttr(self._swivelCombineMode)
    
    @swivelCombineMode.setter
    def swivelCombineMode(self, value):
        with UndoContext("Set Chain Swivel Combine Mode"):
            self.setNumericAttribute(self._swivelCombineMode, value)
        
    @property
    def autoSnap(self):
        return self.getAttr(self._autoSnap)
    
    @autoSnap.setter
    def autoSnap(self, value):
        with UndoContext("Set Chain Auto Snap"):
            self.setNumericAttribute(self._autoSnap, value)
    
    # Methods ---------------
    
    def snapIKToFK(self, times=None):
        with UndoContext("Snap IK to FK"):
            fkLimbCTarget = self.ikLimbC.split("_")
            fkLimbCTarget[-1] = "mth"
            fkLimbCTarget = "_".join(fkLimbCTarget)
            
            fkLimbA = OpenMayaUtils.asMObject(self.fkLimbA)
            fkLimbB = OpenMayaUtils.asMObject(self.fkLimbB)
            fkLimbC = OpenMayaUtils.asMObject(fkLimbCTarget)
            ikLimbC = OpenMayaUtils.asMObject(self.ikLimbC)
            poleVector = OpenMayaUtils.asMObject(self.ikPoleVector)
            fkLimbAFn = OpenMaya.MFnDependencyNode(fkLimbA)
            fkLimbBFn = OpenMaya.MFnDependencyNode(fkLimbB)
            fkLimbCFn = OpenMaya.MFnDependencyNode(fkLimbC)
            ikLimbCFn = OpenMaya.MFnDependencyNode(ikLimbC)
            poleVectorFn = OpenMaya.MFnDependencyNode(poleVector)
            
            fkLimbAWorldMatrixPlug = fkLimbAFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            fkLimbBWorldMatrixPlug = fkLimbBFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            fkLimbCWorldMatrixPlug = fkLimbCFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            ikLimbCParentMatrixPlug = ikLimbCFn.findPlug("parentMatrix", False).elementByLogicalIndex(0)
            poleVectorWorldMatrixPlug = poleVectorFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            
            ikLimbCRotatePlug = ikLimbCFn.findPlug("rotate", False)
            ikLimbCRotateOrderPlug = ikLimbCFn.findPlug("rotateOrder", False)
            
            swivelPlug = OpenMayaUtils.asMPlug(self.ikSwivelPlug)
            
                
            if times == None:
                times = [None]
                
            if times[0] is not None:
                # Hay un bug al empezar a realizar operaciones en un frame distinto al actual.
                # Para solucionarlo lo mejor es obtener el valor de los plugs antes de todo en otro frame para forzar a Maya a borrar la cache.
                dummyContext = OpenMaya.MDGContext(OpenMaya.MTime(times[0] - 1, OpenMaya.MTime.uiUnit()))
                fkLimbAWorldMatrixPlug.asMObject(dummyContext)
                fkLimbBWorldMatrixPlug.asMObject(dummyContext)
                fkLimbCWorldMatrixPlug.asMObject(dummyContext)
                ikLimbCParentMatrixPlug.asMObject(dummyContext)
                poleVectorWorldMatrixPlug.asMObject(dummyContext)
            
            for time in times:
                if time is not None:
                    context = OpenMaya.MDGContext(OpenMaya.MTime(time, OpenMaya.MTime.uiUnit()))
                else:
                    context = OpenMaya.MDGContext.kNormal
                    time = cmds.currentTime(q=True)
                
                fkLimbCWorldMatrix = OpenMaya.MFnMatrixData(fkLimbCWorldMatrixPlug.asMObject(context)).matrix()
                ikLimbCParentMatrix = OpenMaya.MFnMatrixData(ikLimbCParentMatrixPlug.asMObject(context)).matrix()
                ikLimbCCurrentRotation = OpenMaya.MEulerRotation(ikLimbCRotatePlug.asMDataHandle(context).asDouble3())
                ikLimbCRotateOrder = ikLimbCRotateOrderPlug.asShort(context)
                
                offsetMatrix = OpenMaya.MTransformationMatrix(fkLimbCWorldMatrix * ikLimbCParentMatrix.inverse())
                offsetTranslation = offsetMatrix.translation(OpenMaya.MSpace.kTransform)
                offsetRotation = offsetMatrix.rotation(asQuaternion=False).reorder(ikLimbCRotateOrder).closestSolution(ikLimbCCurrentRotation)
                
                offsetTranslationVector = [offsetTranslation.x, offsetTranslation.y, offsetTranslation.z]
                offsetRotationVector = [offsetRotation.x, offsetRotation.y, offsetRotation.z]
                for i, coord in enumerate(["x", "y", "z"]):
                    translatePlug = "{}.t{}".format(self.ikLimbC, coord)
                    rotatePlug = "{}.r{}".format(self.ikLimbC, coord)
                    cmds.setKeyframe(translatePlug, t=time)
                    cmds.setKeyframe(rotatePlug, t=time)
                    cmds.keyframe(translatePlug, e=True, vc=offsetTranslationVector[i], t=(time, time))
                    cmds.keyframe(rotatePlug, e=True, vc=math.degrees(offsetRotationVector[i]), t=(time, time))
                
                fkLimbAWorldTransform = OpenMaya.MFnMatrixData(fkLimbAWorldMatrixPlug.asMObject(context)).transformation()
                fkLimbBWorldTransform = OpenMaya.MFnMatrixData(fkLimbBWorldMatrixPlug.asMObject(context)).transformation()
                poleVectorWorldTransform = OpenMaya.MFnMatrixData(poleVectorWorldMatrixPlug.asMObject(context)).transformation()
                
                fkLimbAWorldTranslation = fkLimbAWorldTransform.translation(OpenMaya.MSpace.kTransform)
                fkLimbCWorldTranslation = OpenMaya.MTransformationMatrix(fkLimbCWorldMatrix).translation(OpenMaya.MSpace.kTransform)
                poleVectorWorldTranslation = poleVectorWorldTransform.translation(OpenMaya.MSpace.kTransform)
                
                PtoA = fkLimbAWorldTranslation - poleVectorWorldTranslation
                PtoC = fkLimbCWorldTranslation - poleVectorWorldTranslation
                AtoC_dir = (fkLimbCWorldTranslation - fkLimbAWorldTranslation).normal()
                
                targetPlanarNormal = (PtoA ^ PtoC).normal()
                if self.swivelCombineMode == 0:
                    swivelAngle = swivelPlug.asMAngle(context).asRadians()
                    targetPlanarNormal = targetPlanarNormal.rotateBy(OpenMaya.MQuaternion(swivelAngle, AtoC_dir))
                
                fkUp = self.getEnumAxis(self.fkPlanarAxis).rotateBy(fkLimbBWorldTransform.rotation(asQuaternion=True))
                rotationAngle = targetPlanarNormal.angle(fkUp)
                rotationNormal = (targetPlanarNormal ^ fkUp).normal()
                
                if self.ikSwivelOutputMode == 0:
                    # Pole Vector Mode
                    localPoleVectorTranslation = poleVectorWorldTranslation - fkLimbCWorldTranslation
                    targetPoleVectorTranslation = fkLimbCWorldTranslation + localPoleVectorTranslation.rotateBy(OpenMaya.MQuaternion(rotationAngle, rotationNormal))
                    offsetPoleVectorTranslation = (targetPoleVectorTranslation - poleVectorWorldTranslation).rotateBy(poleVectorWorldTransform.rotation(asQuaternion=True).inverse())
                    
                    offsetPoleVectorTranslationVector = [offsetPoleVectorTranslation.x, offsetPoleVectorTranslation.y, offsetPoleVectorTranslation.z]
                    for i, coord in enumerate(["x", "y", "z"]):
                        plug = "{}.t{}".format(self.ikPoleVector, coord)
                        cmds.setKeyframe(plug, t=time)
                        cmds.keyframe(plug, e=True, vc=offsetPoleVectorTranslationVector[i], relative=True, t=(time, time))
                    
                else:
                    # Swivel Angle Mode
                    if rotationNormal * AtoC_dir < 0:
                        rotationAngle *= -1
                    
                    cmds.setKeyframe(self.ikSwivelPlug, t=time)
                    cmds.keyframe(self.ikSwivelPlug, e=True, vc=math.degrees(rotationAngle), relative=True, t=(time, time))
    
    def snapFKToIK(self, times=None):
        with UndoContext("Snap FK to IK"):
            ikLimbCTarget = self.fkLimbC.split("_")
            ikLimbCTarget[-1] = "mth"
            ikLimbCTarget = "_".join(ikLimbCTarget)
            
            fkLimbA = OpenMayaUtils.asMObject(self.fkLimbA)
            fkLimbB = OpenMayaUtils.asMObject(self.fkLimbB)
            fkLimbC = OpenMayaUtils.asMObject(self.fkLimbC)
            ikLimbC = OpenMayaUtils.asMObject(ikLimbCTarget)
            poleVector = OpenMayaUtils.asMObject(self.ikPoleVector)
            fkLimbAFn = OpenMaya.MFnDependencyNode(fkLimbA)
            fkLimbBFn = OpenMaya.MFnDependencyNode(fkLimbB)
            fkLimbCFn = OpenMaya.MFnDependencyNode(fkLimbC)
            ikLimbCFn = OpenMaya.MFnDependencyNode(ikLimbC)
            poleVectorFn = OpenMaya.MFnDependencyNode(poleVector)
            
            fkLimbAParentInverseMatrixPlug = fkLimbAFn.findPlug("parentInverseMatrix", False).elementByLogicalIndex(0)
            fkLimbCParentMatrixPlug = fkLimbCFn.findPlug("parentMatrix", False).elementByLogicalIndex(0)
            fkLimbAWorldMatrixPlug = fkLimbAFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            fkLimbBWorldMatrixPlug = fkLimbBFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            fkLimbCWorldMatrixPlug = fkLimbCFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            ikLimbCWorldMatrixPlug = ikLimbCFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            poleVectorWorldMatrixPlug = poleVectorFn.findPlug("worldMatrix", False).elementByLogicalIndex(0)
            
            swivelPlug = OpenMayaUtils.asMPlug(self.ikSwivelPlug)
            
            fkLimbARotateOrder = fkLimbAFn.findPlug("rotateOrder", False).asShort()
            fkLimbBRotateOrder = fkLimbBFn.findPlug("rotateOrder", False).asShort()
            fkLimbCRotateOrder = fkLimbCFn.findPlug("rotateOrder", False).asShort()
            
            if times == None:
                times = [None]
            
            if times[0] is not None:
                # Hay un bug al empezar a realizar operaciones en un frame distinto al actual.
                # Para solucionarlo lo mejor es obtener el valor de los plugs antes de doto en otro frame para forzar a Maya a borrar la cache.
                dummyContext = OpenMaya.MDGContext(OpenMaya.MTime(times[0] - 1, OpenMaya.MTime.uiUnit()))
                fkLimbAParentInverseMatrixPlug.asMObject(dummyContext)
                fkLimbCParentMatrixPlug.asMObject(dummyContext)
                fkLimbAWorldMatrixPlug.asMObject(dummyContext)
                fkLimbBWorldMatrixPlug.asMObject(dummyContext)
                fkLimbCWorldMatrixPlug.asMObject(dummyContext)
                ikLimbCWorldMatrixPlug.asMObject(dummyContext)
                poleVectorWorldMatrixPlug.asMObject(dummyContext)
            
            for time in times:                
                if time is not None:
                    context = OpenMaya.MDGContext(OpenMaya.MTime(time, OpenMaya.MTime.uiUnit()))
                else:
                    context = OpenMaya.MDGContext.kNormal
                    time = cmds.currentTime(q=True)
                
                fkLimbAParentInverseTransform = OpenMaya.MFnMatrixData(fkLimbAParentInverseMatrixPlug.asMObject(context)).transformation()
                fkLimbCParentTransform = OpenMaya.MFnMatrixData(fkLimbCParentMatrixPlug.asMObject(context)).transformation()
                fkLimbAWorldTransform = OpenMaya.MFnMatrixData(fkLimbAWorldMatrixPlug.asMObject(context)).transformation()
                fkLimbBWorldTransform = OpenMaya.MFnMatrixData(fkLimbBWorldMatrixPlug.asMObject(context)).transformation()
                fkLimbCWorldTransform = OpenMaya.MFnMatrixData(fkLimbCWorldMatrixPlug.asMObject(context)).transformation()
                ikLimbCWorldTransform = OpenMaya.MFnMatrixData(ikLimbCWorldMatrixPlug.asMObject(context)).transformation()
                poleVectorWorldTransform = OpenMaya.MFnMatrixData(poleVectorWorldMatrixPlug.asMObject(context)).transformation()
                
                limbAParentInverseRotation = fkLimbAParentInverseTransform.rotation(asQuaternion=True)
                limbCParentRotation = fkLimbCParentTransform.rotation(asQuaternion=True)
                limbAWorldRotation = fkLimbAWorldTransform.rotation(asQuaternion=True)
                limbTWorldRotation = ikLimbCWorldTransform.rotation(asQuaternion=True)
                
                A = OpenMaya.MPoint(fkLimbAWorldTransform.translation(OpenMaya.MSpace.kTransform))
                B = OpenMaya.MPoint(fkLimbBWorldTransform.translation(OpenMaya.MSpace.kTransform))
                C = OpenMaya.MPoint(fkLimbCWorldTransform.translation(OpenMaya.MSpace.kTransform))
                T = OpenMaya.MPoint(ikLimbCWorldTransform.translation(OpenMaya.MSpace.kTransform))
                P = OpenMaya.MPoint(poleVectorWorldTransform.translation(OpenMaya.MSpace.kTransform))
                    
                AtoB = B - A
                BtoC = C - B
                AtoC = C - A
                AtoT = T - A
                PtoA = P - A
                PtoT = P - T
                AtoB_dist = AtoB.length()
                BtoC_dist = BtoC.length()
                AtoC_dist = AtoC.length()
                AtoT_dist = AtoT.length()
                PtoA_dist = PtoA.length()
                PtoT_dist = PtoT.length()
                AtoB_dir = AtoB / AtoB_dist
                BtoC_dir = BtoC / BtoC_dist
                AtoC_dir = AtoC / AtoC_dist
                AtoT_dir = AtoT / AtoT_dist
                PtoA_dir = PtoA / PtoA_dist
                PtoT_dir = PtoT / PtoT_dist
                
                currentPlanarAngle = math.acos(MathUtils.clamp(AtoC_dir * AtoB_dir, -1, 1))
                newPlanarAngle = math.acos(MathUtils.clamp((AtoB_dist * AtoB_dist + AtoT_dist * AtoT_dist - BtoC_dist * BtoC_dist) / (2 * AtoB_dist * AtoT_dist), -1, 1))
                currentElbowAngle = math.acos(MathUtils.clamp(AtoB_dir * BtoC_dir, -1, 1))
                elbowAngle = math.acos(MathUtils.clamp((AtoB_dist * AtoB_dist + BtoC_dist * BtoC_dist - AtoT_dist * AtoT_dist) / (2 * AtoB_dist * BtoC_dist), -1, 1))
                extraAngle = math.acos(MathUtils.clamp(AtoC_dir * AtoT_dir, -1, 1))
                
                planarAxis = self.getEnumAxis(self.fkPlanarAxis)
                extraAxis = (AtoC_dir ^ AtoT_dir).normal()
                offsetElbowAngle = currentElbowAngle - (math.pi - elbowAngle)
                planarRotation = OpenMaya.MQuaternion(newPlanarAngle - currentPlanarAngle, planarAxis.rotateBy(limbAWorldRotation))
                extraRotation = OpenMaya.MQuaternion(extraAngle, extraAxis)
                elbowRotation = OpenMaya.MQuaternion(offsetElbowAngle, planarAxis)
                shoulderRotation = limbAWorldRotation * (planarRotation * extraRotation)
                
                newPlanarNormal = planarAxis.rotateBy(shoulderRotation)
                targetPlanarNormal = (PtoA_dir ^ PtoT_dir).normal()
                if self.swivelCombineMode == 0:
                    swivelAngle = swivelPlug.asMAngle(context).asRadians()
                    targetPlanarNormal = targetPlanarNormal.rotateBy(OpenMaya.MQuaternion(swivelAngle, AtoT_dir))
                twistRotation = OpenMaya.MQuaternion(newPlanarNormal, targetPlanarNormal)
                shoulderRotation = shoulderRotation * twistRotation
                
                rot1 = planarRotation * extraRotation * twistRotation
                rot2 = OpenMaya.MQuaternion(offsetElbowAngle, planarAxis.rotateBy(shoulderRotation))
                newParent = limbCParentRotation * rot1 * rot2
                handRotation = limbTWorldRotation * newParent.inverse()
                
                limbAFinalRotation = (shoulderRotation * limbAParentInverseRotation).asEulerRotation().reorder(fkLimbARotateOrder)
                limbBOffsetRotation = elbowRotation.asEulerRotation().reorder(fkLimbBRotateOrder)
                limbCFinalRotation = handRotation.asEulerRotation().reorder(fkLimbCRotateOrder)
                
                finalRotationVector = [limbAFinalRotation.x, limbAFinalRotation.y, limbAFinalRotation.z]
                for i, coord in enumerate(["x", "y", "z"]):
                    rotatePlug = "{}.r{}".format(self.fkLimbA, coord)
                    cmds.setKeyframe(rotatePlug, t=time)
                    cmds.keyframe(rotatePlug, e=True, vc=math.degrees(finalRotationVector[i]), t=(time, time))
                
                offsetRotationVector = [limbBOffsetRotation.x, limbBOffsetRotation.y, limbBOffsetRotation.z]
                for i, coord in enumerate(["x", "y", "z"]):
                    rotatePlug = "{}.r{}".format(self.fkLimbB, coord)
                    v = cmds.keyframe(rotatePlug, q=True, t=(time, time), eval=True)
                    if v:
                        cmds.setKeyframe(rotatePlug, t=time)
                        cmds.keyframe(rotatePlug, e=True, vc=(v[0] + math.degrees(offsetRotationVector[i])), t=(time, time))
                
                finalRotationVector = [limbCFinalRotation.x, limbCFinalRotation.y, limbCFinalRotation.z]
                for i, coord in enumerate(["x", "y", "z"]):
                    rotatePlug = "{}.r{}".format(self.fkLimbC, coord)
                    cmds.setKeyframe(rotatePlug, t=time)
                    cmds.keyframe(rotatePlug, e=True, vc=math.degrees(finalRotationVector[i]), t=(time, time))
