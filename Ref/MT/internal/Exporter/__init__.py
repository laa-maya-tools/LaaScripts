import maya.cmds as cmds
import maya.mel as mel

import os, subprocess, shutil

import ProjectPath
import P4.Tools as P4Tools
import Utils.Maya as MayaUtils
import Utils.Maya.AnimLayers as AnimLayersUtils

# ------------------------------------
# | Constants                        |
# ------------------------------------

EXPORTER_CHANGELIST_DESCRIPTION = "EXPORTER"
EXPORTER_COMPILER_PATH = os.path.join(ProjectPath.getMSFrameworkFolder(), "AssetCompilerIDE.exe")
EXPORTER_COMPILER_BATCHFILE_PATH = os.path.join(ProjectPath.getMSFrameworkFolder(), "BatchExport.cmpjob")

EXPORTER_OUTPUT_FORMATS = ["fmd", "ftx", "fsk", "fvb", "fcl", "fts"," ftp", "fsh", "fsn"]

class ExportFileType(object):
    def __init__(self, outputFormat, fileExtension, fileExtensionConverted=None):
        self.outputFormat = outputFormat
        self.fileExtension = fileExtension
        self.fileExtensionConverted = fileExtensionConverted
        
    def getOutputString(self):
        outputString = ""
        for format in EXPORTER_OUTPUT_FORMATS:
            outputString += self.getOutputStringForFormat(format)
        return outputString
        
    def getOutputStringForFormat(self, outputFormat):
        return "output_{}={};".format(outputFormat, "true" if outputFormat == self.outputFormat else "false")


EXPORTER_ANIMATION_FILE_TYPE = ExportFileType("fsk", "fskb", "cskla")
EXPORTER_CAMERA_FILE_TYPE = ExportFileType("fsn", "fsnb", "ccam")

# ------------------------------------
# | Asset Compiling                  |
# ------------------------------------

def compileAssetFiles(filePaths, wait=True, raiseExceptions=True):
    try:
        batchExportFile = open(EXPORTER_COMPILER_BATCHFILE_PATH, "w") 
        
        batchExportFile.write("<CompileTasks>\n")
        for filePath in filePaths:
            batchExportFile.write("\t<Task Type=\"COMPILE_FILE\" Platforms=\"WIN|NX\" File=\"{}\" ForceCompile=\"true\" AutoImport=\"true\"/>\n".format(filePath))
        batchExportFile.write("</CompileTasks>\n")

    finally:
        batchExportFile.close()

    process = subprocess.Popen("{} \"{}\" -nogui".format(EXPORTER_COMPILER_PATH, EXPORTER_COMPILER_BATCHFILE_PATH), cwd=ProjectPath.getMSFrameworkFolder())
    if wait:
        stdout, stderr = process.communicate()
        if raiseExceptions and process.returncode != 0:
            raise RuntimeError(stderr)

# ------------------------------------
# | Animation Export                 |
# ------------------------------------
# Animations require an special treatment, converting them to cskla format before.
EXPORTER_ANIMATION_CONVERSION_INTERMEDIATE_FOLDER = "Export"
EXPORTER_ANIMATION_CONVERTER_PATH = os.path.join(ProjectPath.getMSFrameworkFolder(), "IFNWtoCTRNW.exe")

class AnimationExportStruct(object):
    def __init__(self, rootNode, animationName, exportFolder, rangeStart, rangeEnd, loop, animLayers=None, callback=None):
        if not rootNode:
            raise AssertionError("No nodes to export!")
        
        self.rootNode = rootNode
        self.animationName = animationName
        self.exportFolder = exportFolder
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd
        self.loop = loop
        self.animLayers = animLayers
        self.callback = callback

    def getFolderPath(self, intermediateFolder=None):
        if intermediateFolder == None:
            return self.exportFolder
        else:
            path = os.path.normpath(self.exportFolder)
            assetFolderIndex = path.lower().find("\\assets\\")
            return os.path.join(path[:assetFolderIndex], intermediateFolder, path[assetFolderIndex + 1:])

    def getFilePath(self, extension, intermediateFolder=None):
        path = self.getFolderPath(intermediateFolder=intermediateFolder)
        return os.path.join(path, "{}.{}".format(self.animationName, extension))
    
    def applyAnimLayers(self):
        if self.animLayers != None:
            # The Base Animation Layer must be always enabled
            baseLayer = AnimLayersUtils.getBaseLayer()
            if baseLayer != None and baseLayer not in self.animLayers:
                self.animLayers = self.animLayers + [baseLayer]
            
            AnimLayersUtils.setEnabledAnimLayers(self.animLayers)

EXPORTER_CAMERA_ATTRIBUTES_TO_CONNECT = [
    "focalLength", 
    "nearClipPlane", 
    "farClipPlane", 
    "horizontalFilmAperture",
    "verticalFilmAperture"
    ]

def offsetConstraintWithNode(constraint, node, target):
    productNode = cmds.createNode("vectorProduct")
    cmds.setAttr("{}.operation".format(productNode), 4) # Point X Matrix Mode
    cmds.connectAttr("{}.worldInverseMatrix".format(node), "{}.matrix".format(productNode), f=True)
    cmds.connectAttr("{}.constraintTranslate".format(constraint), "{}.input1".format(productNode), f=True)
    cmds.connectAttr("{}.outputX".format(productNode), "{}.translateX".format(target), f=True)
    cmds.connectAttr("{}.outputY".format(productNode), "{}.translateY".format(target), f=True)
    cmds.connectAttr("{}.outputZ".format(productNode), "{}.translateZ".format(target), f=True)

def simplifyParentConstraint(constraint, node, targetIndex):
    attrs = cmds.listAttr("{}.target[{}]".format(constraint, targetIndex))
    attrs = ["{}.{}".format(constraint, attr) for attr in attrs]
    connections = cmds.listConnections(attrs, c=True, p=True, s=True, d=False)
    for i in range(0, len(connections), 2):
        cmds.disconnectAttr(connections[i+1], connections[i])
    cmds.connectAttr("{}.worldMatrix".format(node), "{}.target[{}].targetParentMatrix".format(constraint, targetIndex))
    
def createExportCamera(camera, parent=None, name=None):
    if name != None:
        if name != camera and cmds.objExists(name):
            raise NameError("Unable to rename camera {} to {}, the name is already in use.".format(camera, name))
    else:
        name = camera
    
    oldCamera = MayaUtils.renameCamera(camera, "{}_old".format(camera), autoRenameDuplicated=True)
    
    exportCamera = cmds.camera()[0]
    exportCamera = MayaUtils.renameCamera(exportCamera, name)
    mel.eval("cameraMakeNode 2 \"{}\";".format(exportCamera))
    
    lookAtNode = MayaUtils.getCameraLookAtNode(exportCamera)
    targetNode = MayaUtils.getLookAtTargetNode(lookAtNode)
    
    cameraConstraint = cmds.pointConstraint(oldCamera, exportCamera, maintainOffset=False)[0]
    cmds.connectAttr("{}.worldMatrix[0]".format(targetNode), "{}.worldUpMatrix".format(lookAtNode))
    cmds.setAttr("{}.worldUpType".format(lookAtNode), 2)    # Camera Aim Mode to Object Rotation Up, done the last since it gets reset when some attributes are changed
    
    targetConstraint = cmds.parentConstraint(oldCamera, targetNode, maintainOffset=False)[0]
    simplifyParentConstraint(targetConstraint, oldCamera, 0)    # Parent Constraint's won't account for the Camera Noise, fix this
    cmds.setAttr("{}.target[0].targetOffsetTranslateZ".format(targetConstraint), -500)
    
    if parent != None:
        # Cameras are exported on World Coordinates. This creates a setup so the export camera's world transform is the original one's relative to the parent's.
        offsetConstraintWithNode(cameraConstraint, parent, exportCamera)
        offsetConstraintWithNode(targetConstraint, parent, targetNode)
    
    oldCameraShape = cmds.listRelatives(oldCamera, children=True, type="camera")[0]
    exportCameraShape = cmds.listRelatives(exportCamera, children=True, type="camera")[0]
    for attr in EXPORTER_CAMERA_ATTRIBUTES_TO_CONNECT:
        cmds.connectAttr("{}.{}".format(oldCameraShape, attr), "{}.{}".format(exportCameraShape, attr))
    
    return oldCamera, exportCamera

def deleteExportCamera(oldCamera, exportCamera, originalCameraName=None):
    if originalCameraName == None:
        originalCameraName = exportCamera
    MayaUtils.deleteCamera(exportCamera, deleteUp=False)    # The Up will be connected to the old camera, we don't want to delete it
    MayaUtils.renameCamera(oldCamera, originalCameraName)

def convertAnimationFile(filePath, fileType=EXPORTER_ANIMATION_FILE_TYPE, checkout=True, changelist=EXPORTER_CHANGELIST_DESCRIPTION, wait=True, raiseExceptions=True):
    if not filePath.endswith(fileType.fileExtension):
        raise RuntimeError("Animation file doesn't have the right extension ({}): {}".format(fileType.fileExtension, filePath))

    newFilePath = filePath[:-len(fileType.fileExtension)] + fileType.fileExtensionConverted
    if checkout:
        exporterChangelist = P4Tools.P4Changelist.getChangelistByDescription(changelist, createIfNotExists=True)
        p4File = P4Tools.P4File(newFilePath)
        p4File.smartCheckout(changelist=exporterChangelist)

    dir, file = os.path.split(filePath)
    command = "{} -i \"{}\"".format(EXPORTER_ANIMATION_CONVERTER_PATH, file)
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    process = subprocess.Popen(command, cwd=dir, startupinfo=startupinfo)  # This startupinfo will prevent a window to pop up when converting
    if wait:
        stdout, stderr = process.communicate()
        if raiseExceptions and process.returncode != 0:
            raise RuntimeError(process.returncode, stderr)

    return newFilePath

def exportAnimation(rootNode, animationName, exportFolder, rangeStart, rangeEnd, loop, animLayers=None, fileType=EXPORTER_ANIMATION_FILE_TYPE, checkout=True, convert=True, compile=True):
    animExport = AnimationExportStruct(rootNode, animationName, exportFolder, rangeStart, rangeEnd, loop, animLayers=animLayers)
    exportedFiles = exportAnimationBatch([animExport], fileType=fileType, checkout=checkout, convert=convert, compile=compile)
    return exportedFiles

def exportAnimationBatch(animationExportStructs, fileType=EXPORTER_ANIMATION_FILE_TYPE, checkout=True, changelist=EXPORTER_CHANGELIST_DESCRIPTION, convert=True, compile=True):
    # Builds the export command
    melExportCommand = "NintendoExportCmd"
    melExportCommand += " -f"   # The -f flag forces to overwrite already existing files.
    
    # Options BEGIN
    melExportCommand += " -op \""

    # Animation Options
    melExportCommand += "{animationOptions}"    # This field will be filled with each animation's information.

    # Basic Options
    melExportCommand += "export_target=selection;"
    melExportCommand += "remove_namespace=true;"
    melExportCommand += fileType.getOutputString()

    # Precision Options
    melExportCommand += "bake_all_anim=false;"
    melExportCommand += "frame_precision=1;"
    melExportCommand += "compress_bone=cull;"
    melExportCommand += "tolerance_scale=0.01;"
    melExportCommand += "tolerance_rotate=0.01;"
    melExportCommand += "tolerance_translate=0.01;"
    melExportCommand += "quantize_tolerance_scale=0.01;"
    melExportCommand += "quantize_tolerance_rotate=0.01;"
    melExportCommand += "quantize_tolerance_translate=0.01;"

    # Extra Options
    melExportCommand += "magnify=1;"
    melExportCommand += "motion_mirroring=false;"

    # Default Options
    melExportCommand += "reset_root_scale=false;"
    melExportCommand += "reset_root_rotate=false;"
    melExportCommand += "reset_root_translate=false;"
    melExportCommand += "merge_anim=false;"

    # Options END
    melExportCommand += "\""

    if checkout:
        # Gets the exporter changelist
        exporterChangelist = P4Tools.P4Changelist.getChangelistByDescription(changelist, createIfNotExists=True)

    # Exports the animations
    animationPaths = []
    for animExport in animationExportStructs:
        # Runs the batch item callback
        if animExport.callback:
            if not animExport.callback():
                return None
        
        # Retrieves the export path
        exportPath = animExport.getFilePath(fileType.fileExtension, intermediateFolder=EXPORTER_ANIMATION_CONVERSION_INTERMEDIATE_FOLDER)

        # Attempts to checkout the file
        p4File = P4Tools.P4File(exportPath)
        if checkout:
            p4File.smartCheckout(changelist=exporterChangelist)
        elif p4File.doesLocalFileExist():
            p4File.setLocalFileReadOnly(False)

        # Selects the root
        cmds.select(animExport.rootNode, replace=True)

        # Completes the mel command with the animation options
        animationOptions = "output_file_name={};".format(animExport.animationName)
        animationOptions += "output_folder={};".format(os.path.dirname(exportPath).replace(os.path.sep, os.path.altsep))
        animationOptions += "frame_range=range;"
        animationOptions += "start_frame={};".format(int(animExport.rangeStart))
        animationOptions += "end_frame={};".format(int(animExport.rangeEnd))
        animationOptions += "loop_anim={};".format(str(animExport.loop).lower())
        
        # Configures the Animation Layers
        animExport.applyAnimLayers()

        # Runs the command, performing the actual export
        mel.eval(melExportCommand.format(animationOptions=animationOptions))

        # Converts the animations
        if convert:
            finalPath = animExport.getFilePath(fileType.fileExtensionConverted)

            p4File = P4Tools.P4File(finalPath)
            if checkout:
                p4File.smartCheckout(changelist=exporterChangelist)
            elif p4File.doesLocalFileExist():
                p4File.setLocalFileReadOnly(False)

            convertedPath = convertAnimationFile(exportPath, fileType=fileType, checkout=False)    # We need to move the converted file so we will manually checkout it on the final path
            
            finalDir = os.path.dirname(finalPath)
            if not os.path.isdir(finalDir):
                os.makedirs(finalDir)
            shutil.move(convertedPath, finalPath)
            
            animationPaths.append(finalPath)

        else:
            animationPaths.append(exportPath)

    # Compiles the animations
    if convert and compile: # Cannot compile the animations if they are not converted first
        compileAssetFiles(animationPaths)

    return animationPaths
