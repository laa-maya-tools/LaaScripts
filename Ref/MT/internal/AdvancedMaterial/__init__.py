import maya.cmds as cmds
import maya.mel as mel

import mtoa.utils;

import RelativeReferences.lib.Utils as RelativeReferencesUtils

from Utils.Maya.UndoContext import UndoContext

def areDefalutLightsCreated():
    return cmds.objExists("KeyLight")   # We only check the KeyLight for simplicity

def createDefaultLights(unique=True, adjustLambert=True):
    with UndoContext("Create Default Lights"):
        if not unique or not cmds.objExists("KeyLight"):
            keyLightShape = cmds.directionalLight(name="KeyLight", intensity=5)
            keyLightTransform = cmds.listRelatives(keyLightShape, parent=True)[0]
            cmds.setAttr("{}.overrideEnabled".format(keyLightTransform), True)
            cmds.setAttr("{}.overrideDisplayType".format(keyLightTransform), 2)
            cmds.setAttr("{}.rotate".format(keyLightTransform), -60, 25, -15)
        
        if not unique or not cmds.objExists("FillLight"):
            fillLightShape = cmds.directionalLight(name="FillLight", intensity=1)
            fillLightTransform = cmds.listRelatives(fillLightShape, parent=True)[0]
            cmds.setAttr("{}.overrideEnabled".format(fillLightTransform), True)
            cmds.setAttr("{}.overrideDisplayType".format(fillLightTransform), 2)
            cmds.setAttr("{}.rotate".format(fillLightTransform), -10, -50, 0)
        
        if not unique or not cmds.objExists("BounceLight"):
            bounceLightShape = cmds.directionalLight(name="BounceLight", intensity=0.25)
            bounceLightTransform = cmds.listRelatives(bounceLightShape, parent=True)[0]
            cmds.setAttr("{}.overrideEnabled".format(bounceLightTransform), True)
            cmds.setAttr("{}.overrideDisplayType".format(bounceLightTransform), 2)
            cmds.setAttr("{}.rotate".format(bounceLightTransform), 90, 0, 0)
        
        if not unique or not cmds.objExists("AmbientLight"):
            ambientLightShape, ambientLightTransform = mtoa.utils.createLocator("aiSkyDomeLight", asLight=True)
            cmds.setAttr("{}.intensity".format(ambientLightShape), 0.5)
            cmds.setAttr("{}.skyRadius".format(ambientLightShape), 0)
            ambientLightTransform = cmds.rename(ambientLightTransform, "AmbientLight")
            cmds.setAttr("{}.overrideEnabled".format(ambientLightTransform), True)
            cmds.setAttr("{}.overrideDisplayType".format(ambientLightTransform), 2)
            
        if adjustLambert:
            adjustDefaultLambertMaterial()

def adjustDefaultLambertMaterial():
    if cmds.objExists("lambert1"):
        with UndoContext("Adjust Default Lambert Material"):
            cmds.setAttr("lambert1.color", 0.3, 0.3, 0.3, type="double3")
        
    else:
        cmds.warning("Default material [lambert1] not found!")

def upgradeSelectedMeshesMaterials(selection=None, relativizeTexturePath=True):
    if selection == None:
        selection = cmds.ls(selection=True)
    selectedMeshes = cmds.ls(selection, dag=True, shapes=True, type="mesh")
    if selectedMeshes:
        with UndoContext("Upgrade Selected Meshes Materials"):
            for mesh in selectedMeshes:
                upgradeMeshMaterial(mesh, relativizeTexturePath=relativizeTexturePath)
    else:
        cmds.warning("No meshes selected!")

def upgradeMeshMaterial(mesh, relativizeTexturePath=True):
    shadingEngines = cmds.listConnections(mesh, type="shadingEngine")
    if shadingEngines:
        with UndoContext("Upgrade Mesh Material"):
            for shadingEngine in shadingEngines:
                upgradeShadingEngineMaterial(shadingEngine, relativizeTexturePath=relativizeTexturePath)
    else:
        cmds.warning("Mesh [{}] has no ShadingEngine!".format(mesh))

def upgradeShadingEngineMaterial(shadingEngine, relativizeTexturePath=True):
    materials = cmds.listConnections("{}.surfaceShader".format(shadingEngine))
    if materials:
        with UndoContext("Upgrade ShadingEngine Material"):
            for material in materials:
                upgradeMaterial(material, relativizeTexturePath=relativizeTexturePath)
    else:
        cmds.warning("ShadingEngine [{}] has no material!".format(shadingEngine))

         
def upgradeMaterial(material, relativizeTexturePath=True):
    with UndoContext("Upgrade Material"):
        if cmds.nodeType(material) != "standardSurface":
            standardMaterial = mel.eval('createRenderNodeCB -asShader "surfaceShader" standardSurface "";')  # This mel procedure will handle the creation of the material node
            
            colorPlug = cmds.listConnections("{}.color".format(material), plugs=True)
            colorPlug = colorPlug[0] if colorPlug else None
            normalPlug = cmds.listConnections("{}.normalCamera".format(material), plugs=True)
            normalPlug = normalPlug[0] if normalPlug else None
            
            if colorPlug:
                cmds.connectAttr(colorPlug, "{}.baseColor".format(standardMaterial), force=True)
            if normalPlug:
                cmds.connectAttr(normalPlug, "{}.normalCamera".format(standardMaterial), force=True)
            
            shadingEngines = cmds.listConnections("{}.outColor".format(material), type="shadingEngine")
            for shadingEngine in shadingEngines:
                cmds.connectAttr("{}.outColor".format(standardMaterial), "{}.surfaceShader".format(shadingEngine), force=True)

            cmds.delete(material)
            material = cmds.rename(standardMaterial, material)
            
        else:
            colorPlug = cmds.listConnections("{}.baseColor".format(material), plugs=True)
            colorPlug = colorPlug[0] if colorPlug else None
            normalPlug = cmds.listConnections("{}.normalCamera".format(material), plugs=True)
            normalPlug = normalPlug[0] if normalPlug else None
        
        # Disconnect anything from the Specular Weight attribute (previous versions connected something but that's not needed anymore, so we undo this connection)
        specularPlug = "{}.specular".format(material)
        specularConnections = cmds.listConnections(specularPlug, plugs=True) or []
        for connection in specularConnections:
            cmds.disconnectAttr(connection, specularPlug)
        
        if normalPlug:
            normalBumpNode = normalPlug.split(".")[0]
            normalTextureNode = cmds.listConnections("{}.bumpValue".format(normalBumpNode))
            normalTextureNode = normalTextureNode[0] if normalTextureNode else None
            if normalTextureNode:
                normalTextureAttr = "{}.fileTextureName".format(normalTextureNode)
                normalTexture = cmds.getAttr(normalTextureAttr)
                if relativizeTexturePath and RelativeReferencesUtils.IsProjectPath(normalTexture):
                    normalTexture = RelativeReferencesUtils.RelativizePath(normalTexture)
                    cmds.setAttr(normalTextureAttr, normalTexture, type="string")
                    
                cmds.setAttr("{}.colorSpace".format(normalTextureNode), "Raw", type="string")
            
            else:
                cmds.warning("Material [{}] has no Normal Texture".format(material))
                    
        if colorPlug:
            colorTextureNode = colorPlug.split(".")[0]
            colorTextureAttr = "{}.fileTextureName".format(colorTextureNode)
            colorTexture = cmds.getAttr(colorTextureAttr)
            if relativizeTexturePath and RelativeReferencesUtils.IsProjectPath(colorTexture):
                colorTexture = RelativeReferencesUtils.RelativizePath(colorTexture)
                cmds.setAttr(colorTextureAttr, colorTexture, type="string")
            
            dataTexture = colorTexture.replace("_bc.", "_at.")
            dataNode = mel.eval('createRenderNodeCB -as2DTexture "" file "";')  # This mel procedure will handle the creation of the texture node
            cmds.setAttr("{}.fileTextureName".format(dataNode), dataTexture, type="string")
            cmds.setAttr("{}.colorSpace".format(dataNode), "Raw", type="string")
            
            cmds.connectAttr("{}.outColorR".format(dataNode), "{}.base".format(material), force=True)
            cmds.connectAttr("{}.outColorG".format(dataNode), "{}.diffuseRoughness".format(material), force=True)
            cmds.connectAttr("{}.outColorG".format(dataNode), "{}.specularRoughness".format(material), force=True)
            cmds.connectAttr("{}.outColorB".format(dataNode), "{}.metalness".format(material), force=True)
            
            cmds.connectAttr(colorPlug, "{}.emissionColor".format(material), force=True)
            cmds.connectAttr("{}.outAlpha".format(colorTextureNode), "{}.emission".format(material), force=True)

        else:
            cmds.warning("Material [{}] has no Color Texture!".format(material))
