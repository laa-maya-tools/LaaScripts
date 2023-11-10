import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as OpenMayaAnim

import sys
import inspect

import NodeID

# Keep track of instances to get around script limitation with proxy classes of base pointers that actually point to derived classes
kTrackingDictionary = {}

class AdditiveTransformationMatrix(OpenMayaMPx.MPxTransformationMatrix):

    def __init__(self):
        OpenMayaMPx.MPxTransformationMatrix.__init__(self)
        kTrackingDictionary[OpenMayaMPx.asHashable(self)] = self
        
        self.additivePositionX = 0.0
        self.additivePositionY = 0.0
        self.additivePositionZ = 0.0

        self.additiveRotationX = 0.0
        self.additiveRotationY = 0.0
        self.additiveRotationZ = 0.0

        self.additiveScaleX = 1.0
        self.additiveScaleY = 1.0
        self.additiveScaleZ = 1.0
                
    def __del__(self):
        del kTrackingDictionary[OpenMayaMPx.asHashable(self)]
        
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(AdditiveTransformationMatrix())
    
    def setAdditivePositionX(self,val):
        self.additivePositionX = val
    
    def setAdditivePositionY(self,val):
        self.additivePositionY = val
    
    def setAdditivePositionZ(self,val):
        self.additivePositionZ = val

    def setAdditiveRotationX(self,val):
        self.additiveRotationX = val

    def setAdditiveRotationY(self,val):
        self.additiveRotationY = val

    def setAdditiveRotationZ(self,val):
        self.additiveRotationZ = val

    def setAdditiveScaleX(self,val):
        self.additiveScaleX = val

    def setAdditiveScaleY(self,val):
        self.additiveScaleY = val

    def setAdditiveScaleZ(self,val):
        self.additiveScaleZ = val
            
    def asMatrix(self,percent=None):
        if percent == None:
            matrix = OpenMayaMPx.MPxTransformationMatrix.asMatrix(self)
            tm = OpenMaya.MTransformationMatrix(matrix)

            try:
                tm.addTranslation(OpenMaya.MVector(self.additivePositionX, self.additivePositionY, self.additivePositionZ), OpenMaya.MSpace.kTransform)

                rotation = OpenMaya.MEulerRotation(self.additiveRotationX, self.additiveRotationY, self.additiveRotationZ, self.rotationOrder()).asQuaternion()
                tm.addRotationQuaternion(rotation.x, rotation.y, rotation.z, rotation.w, OpenMaya.MSpace.kObject)

                scaleUtil = OpenMaya.MScriptUtil()
                scaleUtil.createFromList([self.additiveScaleX, self.additiveScaleY, self.additiveScaleZ], 3)
                tm.addScale(scaleUtil.asDoublePtr(), OpenMaya.MSpace.kObject)

            except Exception as ex:
                print(ex)
                
            return tm.asMatrix()

        else:
            tm = OpenMayaMPx.MPxTransformationMatrix(self)

            try:
                tm.addTranslation(OpenMaya.MVector(self.additivePositionX, self.additivePositionY, self.additivePositionZ), OpenMaya.MSpace.kTransform)
                
                trans = tm.translation()
                rotatePivotTrans = tm.rotatePivot()
                scalePivotTrans = tm.scalePivotTranslation()
                trans = trans * percent
                rotatePivotTrans = rotatePivotTrans * percent
                scalePivotTrans = scalePivotTrans * percent
                tm.translateTo(trans)
                tm.setRotatePivot(rotatePivotTrans)
                tm.setScalePivotTranslation(scalePivotTrans)

                rotation = OpenMaya.MEulerRotation(self.additiveRotationX, self.additiveRotationY, self.additiveRotationZ, self.rotationOrder()).asQuaternion()
                tm.addRotationQuaternion(rotation.x, rotation.y, rotation.z, rotation.w, OpenMaya.MSpace.kObject)

                eulerRotate = tm.eulerRotation()
                tm.rotateTo(eulerRotate * percent, OpenMaya.MSpace.kTransform)
                
                scaleUtil = OpenMaya.MScriptUtil()
                scaleUtil.createFromList(self.additiveScale, 3)
                tm.addScale(scaleUtil.asDoublePtr(), OpenMaya.MSpace.kObject)
                
                s = self.scale(OpenMaya.MSpace.kTransform)
                s.x = 1.0 + (s.x - 1.0) * percent
                s.y = 1.0 + (s.y - 1.0) * percent
                s.z = 1.0 + (s.z - 1.0) * percent
                tm.scaleTo(s, OpenMaya.MSpace.kTransform)

            except Exception as ex:
                print(ex)

            return tm.asMatrix()
        
    def setRotatePivot(self, point, space, balance):
        rot = OpenMaya.MEulerRotation(self.additiveRotationX, self.additiveRotationY, self.additiveRotationZ, self.rotationOrder())
        point = OpenMaya.MPoint(OpenMaya.MVector(point).rotateBy(rot))
        super(AdditiveTransformationMatrix, self).setRotatePivot(point, space, balance)

    def rotatePivot(self, space):
        point = super(AdditiveTransformationMatrix, self).rotatePivot(space)
        rot = OpenMaya.MEulerRotation(self.additiveRotationX, self.additiveRotationY, self.additiveRotationZ, self.rotationOrder())
        point = OpenMaya.MPoint(OpenMaya.MVector(point).rotateBy(rot.inverse()))
        return point
                
class AdditiveTransformNode(OpenMayaMPx.MPxTransform):

    nodeName = "AdditiveTransform"

    additivePositionXAttribute = OpenMaya.MObject()
    additivePositionYAttribute = OpenMaya.MObject()
    additivePositionZAttribute = OpenMaya.MObject()

    additiveRotationXAttribute = OpenMaya.MObject()
    additiveRotationYAttribute = OpenMaya.MObject()
    additiveRotationZAttribute = OpenMaya.MObject()

    additiveScaleXAttribute = OpenMaya.MObject()
    additiveScaleYAttribute = OpenMaya.MObject()
    additiveScaleZAttribute = OpenMaya.MObject()

    def __init__(self, transform=None):
        if transform is None:
            OpenMayaMPx.MPxTransform.__init__(self)
        else:
            OpenMayaMPx.MPxTransform.__init__(self, transform)
        
        self.additivePositionX = 0.0
        self.additivePositionY = 0.0
        self.additivePositionZ = 0.0

        self.additiveRotationX = 0.0
        self.additiveRotationY = 0.0
        self.additiveRotationZ = 0.0

        self.additiveScaleX = 1.0
        self.additiveScaleY = 1.0
        self.additiveScaleZ = 1.0

    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(AdditiveTransformNode())

    @staticmethod
    def initializer():
        unitFn = OpenMaya.MFnUnitAttribute()
        numFn = OpenMaya.MFnNumericAttribute()
        
        AdditiveTransformNode.additivePositionXAttribute = unitFn.create("additivePositionX", "apx", OpenMaya.MFnUnitAttribute.kDistance, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additivePositionXAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additivePositionXAttribute)
        
        AdditiveTransformNode.additivePositionYAttribute = unitFn.create("additivePositionY", "apy", OpenMaya.MFnUnitAttribute.kDistance, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additivePositionYAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additivePositionYAttribute)
        
        AdditiveTransformNode.additivePositionZAttribute = unitFn.create("additivePositionZ", "apz", OpenMaya.MFnUnitAttribute.kDistance, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additivePositionZAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additivePositionZAttribute)
        
        AdditiveTransformNode.additiveRotationXAttribute = unitFn.create("additiveRotationX", "arx", OpenMaya.MFnUnitAttribute.kAngle, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveRotationXAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveRotationXAttribute)
        
        AdditiveTransformNode.additiveRotationYAttribute = unitFn.create("additiveRotationY", "ary", OpenMaya.MFnUnitAttribute.kAngle, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveRotationYAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveRotationYAttribute)
        
        AdditiveTransformNode.additiveRotationZAttribute = unitFn.create("additiveRotationZ", "arz", OpenMaya.MFnUnitAttribute.kAngle, 0.0)
        unitFn.setAffectsWorldSpace(True)
        unitFn.setKeyable(True)
        unitFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveRotationZAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveRotationZAttribute)
        
        AdditiveTransformNode.additiveScaleXAttribute = numFn.create("additiveScaleX", "asx", OpenMaya.MFnNumericData.kDouble, 1.0)
        numFn.setAffectsWorldSpace(True)
        numFn.setKeyable(True)
        numFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveScaleXAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveScaleXAttribute)
        
        AdditiveTransformNode.additiveScaleYAttribute = numFn.create("additiveScaleY", "asy", OpenMaya.MFnNumericData.kDouble, 1.0)
        numFn.setAffectsWorldSpace(True)
        numFn.setKeyable(True)
        numFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveScaleYAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveScaleYAttribute)
        
        AdditiveTransformNode.additiveScaleZAttribute = numFn.create("additiveScaleZ", "asz", OpenMaya.MFnNumericData.kDouble, 1.0)
        numFn.setAffectsWorldSpace(True)
        numFn.setKeyable(True)
        numFn.setChannelBox(False)
        #unitFn.setHidden(True)
        AdditiveTransformNode.addAttribute(AdditiveTransformNode.additiveScaleZAttribute)
        AdditiveTransformNode.mustCallValidateAndSet(AdditiveTransformNode.additiveScaleZAttribute)
    
    def createTransformationMatrix(self):
        return OpenMayaMPx.asMPxPtr(AdditiveTransformationMatrix())

    def className(self):
        return AdditiveTransformNode.nodeName
        
    def getAdditiveTransformationMatrix(self):
        baseXform = self.transformationMatrixPtr()
        return kTrackingDictionary[OpenMayaMPx.asHashable(baseXform)]

    def validateAndSetValue(self, plug, handle, context):
        if not plug.isNull():
            block = self._forceCache(context)
            blockHandle = block.outputValue(plug)

            if plug == self.additivePositionXAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditivePositionX(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additivePositionYAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditivePositionY(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additivePositionZAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditivePositionZ(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveRotationXAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveRotationX(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveRotationYAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveRotationY(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveRotationZAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveRotationZ(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveScaleXAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveScaleX(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveScaleYAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveScaleY(val)

                blockHandle.setClean()
                self._dirtyMatrix()

            if plug == self.additiveScaleZAttribute:
                val = handle.asDouble()
                blockHandle.setDouble(val)

                tm = self.getAdditiveTransformationMatrix()
                if tm is not None:
                    tm.setAdditiveScaleZ(val)

                blockHandle.setClean()
                self._dirtyMatrix()

        return OpenMayaMPx.MPxTransform.validateAndSetValue(self, plug, handle, context)

    def compute(self, plug, block):
        if not plug.isNull():
            if (plug == self.matrix or plug == self.inverseMatrix or plug == self.worldMatrix or plug == self.worldInverseMatrix or	plug == self.parentMatrix or plug == self.parentInverseMatrix):
                try:
                    tm = self.getAdditiveTransformationMatrix()
                    if tm is not None:
                        handle = block.inputValue(self.additivePositionXAttribute)
                        tm.setAdditivePositionX(handle.asDouble())

                        handle = block.inputValue(self.additivePositionYAttribute)
                        tm.setAdditivePositionY(handle.asDouble())

                        handle = block.inputValue(self.additivePositionZAttribute)
                        tm.setAdditivePositionZ(handle.asDouble())
                        
                        handle = block.inputValue(self.additiveRotationXAttribute)
                        tm.setAdditiveRotationX(handle.asDouble())

                        handle = block.inputValue(self.additiveRotationYAttribute)
                        tm.setAdditiveRotationY(handle.asDouble())

                        handle = block.inputValue(self.additiveRotationZAttribute)
                        tm.setAdditiveRotationZ(handle.asDouble())

                        handle = block.inputValue(self.additiveScaleXAttribute)
                        tm.setAdditiveScaleX(handle.asDouble())

                        handle = block.inputValue(self.additiveScaleYAttribute)
                        tm.setAdditiveScaleY(handle.asDouble())

                        handle = block.inputValue(self.additiveScaleZAttribute)
                        tm.setAdditiveScaleZ(handle.asDouble())

                except Exception as ex:
                    print(ex)

        return OpenMayaMPx.MPxTransform.compute(self, plug, block)

    def computeLocalTransformation(self, xform, block):
        OpenMayaMPx.MPxTransform.computeLocalTransformation(self, xform, block)

        additivePositionX = block.inputValue(self.additivePositionXAttribute).asDouble()
        additivePositionY = block.inputValue(self.additivePositionYAttribute).asDouble()
        additivePositionZ = block.inputValue(self.additivePositionZAttribute).asDouble()
        xform.translateBy(OpenMaya.MVector(additivePositionX, additivePositionY, additivePositionZ))

        additiveRotationX = block.inputValue(self.additiveRotationXAttribute).asDouble()
        additiveRotationY = block.inputValue(self.additiveRotationYAttribute).asDouble()
        additiveRotationZ = block.inputValue(self.additiveRotationZAttribute).asDouble()
        xform.rotateBy(OpenMaya.MEulerRotation(additiveRotationX, additiveRotationY, additiveRotationZ, xform.rotationOrder()))

        additiveScaleX = block.inputValue(self.additiveScaleXAttribute).asDouble()
        additiveScaleY = block.inputValue(self.additiveScaleYAttribute).asDouble()
        additiveScaleZ = block.inputValue(self.additiveScaleZAttribute).asDouble()
        xform.scaleBy(OpenMaya.MVector(additiveScaleX, additiveScaleY, additiveScaleZ))


    def setDependentsDirty(self, dirtyPlug, plugArray):

        if dirtyPlug == self.additivePositionXAttribute or dirtyPlug == self.additivePositionYAttribute or dirtyPlug == self.additivePositionZAttribute or \
            dirtyPlug == self.additiveRotationXAttribute or dirtyPlug == self.additiveRotationYAttribute or dirtyPlug == self.additiveRotationZAttribute or \
            dirtyPlug == self.additiveScaleXAttribute or dirtyPlug == self.additiveScaleYAttribute or dirtyPlug == self.additiveScaleZAttribute:

            try:
                thisNode = self.thisMObject()
                plugArray.append(OpenMaya.MPlug(thisNode, self.matrix)) 
                plugArray.append(OpenMaya.MPlug(thisNode, self.inverseMatrix))
                plugArray.append(OpenMaya.MPlug(thisNode, self.worldMatrix)) 
                plugArray.append(OpenMaya.MPlug(thisNode, self.worldInverseMatrix))
                plugArray.append(OpenMaya.MPlug(thisNode, self.parentMatrix)) 
                plugArray.append(OpenMaya.MPlug(thisNode, self.parentInverseMatrix))

            except Exception as ex:
                print(ex)
                
        return OpenMayaMPx.MPxNode.setDependentsDirty(self, dirtyPlug, plugArray) 


# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.registerTransform(AdditiveTransformNode.nodeName, NodeID.AdditiveTransformNodeID, AdditiveTransformNode.creator, AdditiveTransformNode.initializer, AdditiveTransformationMatrix.creator, NodeID.AdditiveTransformationMatrixID)
    except:
        sys.stderr.write("Failed to register transform: " + AdditiveTransformNode.nodeName)
        raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.deregisterNode(NodeID.AdditiveTransformNodeID)
    except:
        sys.stderr.write("Failed to unregister node: " + AdditiveTransformNode.nodeName)
        raise   