import maya.cmds as cmds

import OrganiLayers.OrganiItem as OrganiItem
import OrganiLayers.Window as OrganiLayersWindow

from Utils.Maya.UndoContext import UndoContext

def isVisible(obj):
    organiItems = OrganiItem.OrganiItemWrapper.getConnectedWrappers([obj])
    if organiItems:
        return organiItems.pop().visibility
    else:
        return cmds.getAttr("{}.visibility".format(obj))

def setVisible(obj, visible):
    organiItems = OrganiItem.OrganiItemWrapper.getConnectedWrappers([obj])
    if organiItems:
        organiItems.pop().visibility = visible
    else:
        return cmds.setAttr("{}.visibility".format(obj), visible)

def toggleSelectedObjectsVisibility():
    selection = cmds.ls(selection=True)
    if selection:
        with UndoContext("Toggle Visibility"):
            shouldBeVisible = not isVisible(selection[0])
            for obj in selection:
                setVisible(obj, shouldBeVisible)
                
def toggleSelectedObjectsLayersVisibility():
    selection = cmds.ls(selection=True)
    if selection:
        organiItems = OrganiItem.OrganiItemWrapper.getConnectedWrappers(selection)
        selectionLayers = []
        for organiItem in organiItems:
            selectionLayers.append(organiItem.parentLayer)
        if selectionLayers:
            with UndoContext("Toggle Visibility"):
                shouldBeVisible = not selectionLayers[0].visibility
                for layer in selectionLayers:
                    layer.visibility = shouldBeVisible


def register():
    cmds.runTimeCommand("ToggleVisibility", cat="MSE Commands.OrganiLayers", ann="Toggles the visibility of the selected controls, hiding them if they are visible and unhiding them otherwise. If multiple objects are selected, only the visibility of the first selected object will be used to determine wether to hide or show the nodes (so they end up with the same visibility). If the nodes are registered on an OrganiLayer, they will be hidden there. otherwise they will be hidden normally.", c="import CustomCommands.OrganiLayersCommands as OrganiLayersCommands; OrganiLayersCommands.toggleSelectedObjectsVisibility()", default=True)
    cmds.runTimeCommand("ToggleLayerVisibility", cat="MSE Commands.OrganiLayers", ann="Toggles the visibility of the layers containing the selected controls, hiding them if they are visible and unhiding them otherwise. If multiple layers are selected this way, only the visibility of the first one will be used to determine wether to hide or show the others (so they end up with the same visibility).", c="import CustomCommands.OrganiLayersCommands as OrganiLayersCommands; OrganiLayersCommands.toggleSelectedObjectsLayersVisibility()", default=True)
