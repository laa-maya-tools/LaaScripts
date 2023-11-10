import Batcher

import maya.cmds as cmds

import ActorManager
import Exporter

from Utils.Maya.UndoContext import AutoUndo
import Utils.Maya.AnimLayers as AnimLayerUtils

import os
import math

import logging
logger = logging.getLogger(__name__)

class AnimBatchExporter(Batcher.BatcherUI):
    
    def onGetWindowTitle(self):
        return "Anim Batch Exporter"

    def onPerformBatchProcess(self, filePath):
        # Checks if the animation file exists.
        if not os.path.isfile(filePath):
            raise FileNotFoundError("Couldn't find the specified Maya File! {}".format(filePath))

        # Opens the animation file.
        # If the flag from the preparation process is set, skips this step.
        logger.info("Opening Maya File...")
        cmds.file(filePath, o=True, force=True)

        # Exports the animations
        pathsToCompile = []
        actors = ActorManager.getActors()
        for actor in actors:
            logger.info("Exporting {} Animations...".format(actor.getNamespace()))
            animPresets = actor.getAnimPresets()
            if animPresets:
                digitCount = int(math.floor(math.log10(len(animPresets)))) + 1
                mirrorAnimPresets = []
                for i, animPreset in enumerate(animPresets):
                    logger.info("[{}/{}] Exporting {}...".format(str(i+1).zfill(digitCount), len(animPresets), animPreset.getConcatenatedName().format(left="left", right="right")))
                    
                    exportedFilePaths = animPreset.export(checkout=True, convert=True, compile=False, exportMirror=False)
                    
                    if animPreset.mirror:
                        mirrorAnimPresets.append(animPreset)
                    
                    pathsToCompile += exportedFilePaths
                    
                if mirrorAnimPresets:
                    with AutoUndo():
                        logger.info("Mirroring actor {}...".format(actor.getNamespace()))
                        
                        AnimLayerUtils.setEnabledAnimLayers(actor.getAnimLayers()) # mirrorAnimation will mirror only enabled layers
                        actor.rig.mirrorAnimation()
                        
                        digitCount = int(math.floor(math.log10(len(mirrorAnimPresets)))) + 1
                        for i, animPreset in enumerate(mirrorAnimPresets):
                            nameParts = animPreset.getNameParts()
                            for j in range(len(nameParts)):
                                nameParts[j] = nameParts[j].format(left="right", right="left")
                            animPreset.setNameParts(nameParts)
                            
                            logger.info("[{}/{}] Exporting mirror {}...".format(str(i+1).zfill(digitCount), len(mirrorAnimPresets), animPreset.getConcatenatedName()))
                    
                            exportedFilePaths = animPreset.export(checkout=True, convert=True, compile=False, exportMirror=False)
                            
                            pathsToCompile += exportedFilePaths
                        
                        logger.info("Undoing Mirror...")
                    
            else:
                logger.warning("Actor {} has no animations to export!".format(actor.getNamespace()))

        # Compiles de animations
        if len(pathsToCompile) > 0:
            logger.info("Compiling Animations...".format(actor.getNamespace()))
            Exporter.compileAssetFiles(pathsToCompile)


def showBatchWindow():
    global animBatchExporterWindow
    try:
        if animBatchExporterWindow.isVisible():
            animBatchExporterWindow.close()
    except NameError:
        pass
    animBatchExporterWindow = AnimBatchExporter()
    animBatchExporterWindow.show()

if __name__ == "__main__":
    showBatchWindow()