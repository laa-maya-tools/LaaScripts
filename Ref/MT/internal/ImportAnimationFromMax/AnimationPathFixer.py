import Batcher

import maya.cmds as cmds

import ActorManager
import Exporter
import ProjectPath
import P4.Tools as P4Tools

import xml.etree.ElementTree as XML

import os
import math

import logging
logger = logging.getLogger(__name__)

class AnimationPathFixerBatch(Batcher.BatcherUI):
    
    def onGetWindowTitle(self):
        return "Anim Preset Path Fixer"
    
    def onGetFileFilters(self):
        return ["FSKA Files (*.fska)"]
    
    def onBeforeProcess(self):
        self.filesOpened = []
        return True
    
    def onPerformBatchProcess(self, filePath):
        xmlDoc = XML.parse(filePath)
        mayaFile = xmlDoc.getroot().find("file_info").find("create").get("src_path")
        if mayaFile in self.filesOpened:
            logger.info("File {} already fixed, skipped.".format(mayaFile))
            return
        
        self.filesOpened.append(mayaFile)
        
        # Checks if the animation file exists.
        if not os.path.isfile(mayaFile):
            raise FileNotFoundError("Couldn't find the specified Animation File! {}".format(mayaFile))

        # Opens the animation file.
        # If the flag from the preparation process is set, skips this step.
        logger.info("Opening Maya File: {}".format(mayaFile))
        cmds.file(mayaFile, o=True, force=True)
    
        # Exports the animations
        pathsToCompile = []
        actors = ActorManager.getActors()
        for actor in actors:
            logger.info("Exporting {} Animations...".format(actor.getNamespace()))
            animPresets = actor.getAnimPresets()
            digitCount = int(math.floor(math.log10(len(animPresets)))) + 1
            for i, animPreset in enumerate(animPresets):
                # Fixes the path
                logger.info("[{}/{}] Fixing path for {}...".format(str(i+1).zfill(digitCount), len(animPresets), animPreset.getConcatenatedName()))
                animPreset.path = ""
                
                # Exports the animation
                logger.info("[{}/{}] Exporting {}...".format(str(i+1).zfill(digitCount), len(animPresets), animPreset.getConcatenatedName()))
                exportedFilePaths = animPreset.export(checkout=True, convert=True, compile=False)
                pathsToCompile += exportedFilePaths

        # Compiles the animations
        if len(pathsToCompile) > 0:
            logger.info("Compiling Animations...".format(actor.getNamespace()))
            Exporter.compileAssetFiles(pathsToCompile)
            
        # Saves the file
        logger.info("Saving Maya file...".format(actor.getNamespace()))
        P4Tools.P4File(mayaFile).smartCheckout()
        cmds.file(save=True, type="mayaBinary")


def showBatchWindow():
    global animBatchPathFixerWindow
    try:
        if animBatchPathFixerWindow.isVisible():
            animBatchPathFixerWindow.close()
    except NameError:
        pass
    animBatchPathFixerWindow = AnimationPathFixerBatch()
    animBatchPathFixerWindow.show()

if __name__ == "__main__":
    showBatchWindow()