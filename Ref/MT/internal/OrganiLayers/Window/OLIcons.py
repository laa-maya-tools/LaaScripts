from PySide2                    import QtGui

class OLIcons():
    def copyPixmapWithMultipliedHSV(image, hue=1.0, saturation=1.0, value=1.0, alpha=1.0):
        newImage = QtGui.QImage(image.toImage())
        for i in range(newImage.height()):
            for j in range (newImage.width()):
                color = newImage.pixelColor(i, j)
                color.setHsv(hue * color.hue(), saturation * color.saturation(), value * color.value(), alpha * color.alpha())
                newImage.setPixelColor(i, j, color)
        result = QtGui.QPixmap()
        result.convertFromImage(newImage)
        return result
    
    pxmLayerActive      = QtGui.QPixmap(":/polyStackOrient.png")
    pxmLayerInactive    = QtGui.QPixmap(":/layerEditor.png")
    pxmVisibleOn        = QtGui.QPixmap(":/visible.png")
    pxmVisibleOff       = QtGui.QPixmap(":/settings-hide.png") #Alternative
    #pxmVisibleOff       = QtGui.QPixmap(":/hidden.png") #Original: Eye Slashed
    pxmPlaybackOn       = QtGui.QPixmap(":/play_S.png") #interactivePlayback
    pxmPlaybackOff      = QtGui.QPixmap(":/Mute_ON.png")
    pxmLodOn            = QtGui.QPixmap(":/out_subdiv.png")
    pxmLodOff           = QtGui.QPixmap(":/volumeCube.png")
    pxmShadingOn        = QtGui.QPixmap(":/cube.png")
    pxmShadingOff       = QtGui.QPixmap(":/UVTBWireFrame.png")
    pxmTexturedOn       = QtGui.QPixmap(":/textureEditorCheckered.png")
    pxmTexturedOff      = QtGui.QPixmap(":/UVEditorCheckered.png")
    pxmSnowFlake        = QtGui.QPixmap(":/UV_Freeze_Tool.png")
    pxmFrozenOn         = copyPixmapWithMultipliedHSV(pxmSnowFlake, value=1.4, saturation=0)
    pxmFrozenOff        = copyPixmapWithMultipliedHSV(pxmSnowFlake, value=0.5, saturation=0)
    pxmArrowUp          = QtGui.QPixmap(":/nudgeUp.png")
    pxmOverriden        = copyPixmapWithMultipliedHSV(pxmArrowUp, value=1, hue=0.0, saturation=1.1)
    
    # "Normal" Icons
    # Mesh, Shape, NurbsSurf, Joint, Light, Camera , Miscellaneous
    addNodesIcon        = QtGui.QIcon(":/nodeGrapherAddNodes.png")
    arrowDown           = QtGui.QIcon(":/arrowDown.png")
    arrowUp             = QtGui.QIcon(":/arrowUp.png")
    BBoxIcon            = QtGui.QIcon(pxmLodOn)
    cameraIcon          = QtGui.QIcon(":/out_camera.png")
    cubeIcon            = QtGui.QIcon(pxmShadingOn)
    curveShapeIcon      = QtGui.QIcon(":/splineTangent.png")#nurbsCurve.svg
    deleteLayerIcon     = QtGui.QIcon(":/deleteRenderPass.png")
    eyeIcon             = QtGui.QIcon(pxmVisibleOn)
    jointIcon           = QtGui.QIcon(":/kinJoint.png")
    layerActiveIcon     = QtGui.QIcon(pxmLayerActive)
    layerInactiveIcon   = QtGui.QIcon(pxmLayerInactive)
    lightAmbientIcon    = QtGui.QIcon(":/LM_ambientLight.png")
    lightSpotIcon       = QtGui.QIcon(":/LM_spotLight.png")
    locatorIcon         = QtGui.QIcon(":/locator.png")
    meshIcon            = QtGui.QIcon(":/out_polyPlane.png")
    miscellaneousIcon   = QtGui.QIcon(":/choice.svg")
    newLayerIcon        = QtGui.QIcon(":/newLayerEmpty.png")
    newLayerSelectedIcon = QtGui.QIcon(":/newLayerSelected.png")
    nurbsSurfaceIcon    = QtGui.QIcon(":/out_nurbsSurface.png")
    playbackIcon        = QtGui.QIcon(pxmPlaybackOn)
    removeNodesIcon     = QtGui.QIcon(":/nodeGrapherRemoveNodes.png")
    selectLayerIcon     = QtGui.QIcon(":/IsolateSelected.png")
    snowFlakeIcon       = QtGui.QIcon(pxmFrozenOn)
    textureIcon         = QtGui.QIcon(pxmTexturedOn)
    questionIcon        = QtGui.QIcon(":/defaultCustomLayout.png")
    wireframeIcon       = QtGui.QIcon(pxmShadingOff)
    writtenLayer        = QtGui.QIcon(pxmOverriden)
    
    # "Variant" Icons
    # Normal Vs Active  = No_hovered Vs Hovered
    # On Vs Off         = Checked Vs No_Checked
    var_visibilityIcon = QtGui.QIcon()
    var_visibilityIcon.addPixmap(pxmVisibleOn,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_visibilityIcon.addPixmap(pxmVisibleOff, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_visibilityIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_visibilityIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    
    var_hideOnPlaybackIcon = QtGui.QIcon()
    var_hideOnPlaybackIcon.addPixmap(pxmPlaybackOff,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_hideOnPlaybackIcon.addPixmap(pxmPlaybackOn, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_hideOnPlaybackIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_hideOnPlaybackIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    
    var_LodIcon = QtGui.QIcon()
    var_LodIcon.addPixmap(pxmLodOn,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_LodIcon.addPixmap(pxmLodOff, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_LodIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_LodIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    
    var_shadingIcon = QtGui.QIcon()
    var_shadingIcon.addPixmap(pxmShadingOn,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_shadingIcon.addPixmap(pxmShadingOff, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_shadingIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_shadingIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    
    var_texturedIcon = QtGui.QIcon()
    var_texturedIcon.addPixmap(pxmTexturedOn,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_texturedIcon.addPixmap(pxmTexturedOff, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_texturedIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_texturedIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    
    var_frozenIcon = QtGui.QIcon(":/UV_Freeze_Tool.png")
    var_frozenIcon.addPixmap(pxmFrozenOn,  QtGui.QIcon.Normal, QtGui.QIcon.On)  
    var_frozenIcon.addPixmap(pxmFrozenOff, QtGui.QIcon.Normal, QtGui.QIcon.Off)
    var_frozenIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.On)
    var_frozenIcon.addPixmap(pxmOverriden,  QtGui.QIcon.Disabled, QtGui.QIcon.Off)