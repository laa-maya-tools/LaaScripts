import maya.cmds as cmds

import AnimTools.CopyPasteWorld as CopyPasteWorld

#---------------------------------
#|      Transform Commands       |
#---------------------------------

class TransformCommands():
    
    @staticmethod
    def copySelectedNodesWorldTransform(relative=False):
        selection = CopyPasteWorld.getSelectedTransforms()
        animRange = CopyPasteWorld.getSelectedAnimRange()
        bake = animRange and animRange[0] == animRange[1]
        
        copiedTransforms = CopyPasteWorld.copyWorldTransform(selection, animRange=animRange, bake=bake, relative=relative)
        CopyPasteWorld.storeCopiedTransfromsOnFile(copiedTransforms)
        
    @staticmethod
    def pasteSelectedNodesWorldTransform(relative=False):
        copiedTransforms = CopyPasteWorld.loadCopiedTransfromsFromFile()
        selection = CopyPasteWorld.getSelectedTransforms()
        remaps = dict({(selection[0], obj) for obj in copiedTransforms}) if len(copiedTransforms) <=2 and len(selection) == (2 if relative else 1) and selection[0] not in copiedTransforms else None
        start = cmds.currentTime(q=True)
        
        CopyPasteWorld.pasteWorldTransform(copiedTransforms, nodes=selection, remaps=remaps, start=start, relative=relative)

    @staticmethod
    def registerCommands():
        cmds.runTimeCommand("CopyWorldTransform", cat="MSE Commands.Transform", i="Commands\CopyWorldTransform.png", ann="Copies the selected nodes' World Transform in order to paste it later. If multiple nodes are copied, the transform will be pasted on the same node (if selected). If only one node is copied, that transform will be pasted on all the selected nodes, regardless of name.", c="import CustomCommands.AnimToolsCommands as AnimToolsCommands; AnimToolsCommands.TransformCommands.copySelectedNodesWorldTransform()", default=True)
        cmds.runTimeCommand("PasteWorldTransform", cat="MSE Commands.Transform", i="Commands\PasteWorldTransform.png", ann="Pastes the copied World Transform on the selected nodes. If multiple nodes were copied, the transform will be pasted on the same node (if selected). If only one node was copied, that transform will be pasted on all the selected nodes, regardless of name.", c="import CustomCommands.AnimToolsCommands as AnimToolsCommands; AnimToolsCommands.TransformCommands.pasteSelectedNodesWorldTransform()", default=True)
        cmds.runTimeCommand("CopyWorldTransformRelative", cat="MSE Commands.Transform", i="Commands\CopyWorldTransformRelative.png", ann="Copies the firstly selected nodes' World Transform relative to the last one selected in order to paste it later. If multiple nodes are copied, the transform will be pasted on the same node (if selected). If only one node is copied, that transform will be pasted on all the selected nodes, regardless of name.", c="import CustomCommands.AnimToolsCommands as AnimToolsCommands; AnimToolsCommands.TransformCommands.copySelectedNodesWorldTransform(relative=True)", default=True)
        cmds.runTimeCommand("PasteWorldTransformRelative", cat="MSE Commands.Transform", i="Commands\PasteWorldTransformRelative.png", ann="Pastes the copied World Transform on the firstly selected nodes relative to the last one selected. If multiple nodes were copied, the transform will be pasted on the same node (if selected). If only one node was copied, that transform will be pasted on all the selected nodes, regardless of name.", c="import CustomCommands.AnimToolsCommands as AnimToolsCommands; AnimToolsCommands.TransformCommands.pasteSelectedNodesWorldTransform(relative=True)", default=True)


#---------------------------------
#|           Commands            |
#---------------------------------

def register():
    TransformCommands.registerCommands()
