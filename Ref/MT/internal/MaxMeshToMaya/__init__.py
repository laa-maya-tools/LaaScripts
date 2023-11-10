import MaxMeshToMaya.LockedNormalsToHS  as HS
import Utils.Maya.MayaBridge            as Bridge

def ConvertLockedNormalsToHardSoftEdges():
    selection = Bridge.getSelectedDAGNodes()
    for node in selection:
        try:
            uiItem = HS.ProgressUI()
            uiItem.show()
            HS.SGtoHS(node, uiItem)
            uiItem.deleteUI()
        except Exception as e:
            Bridge.printError("Error converting Mesh '{}': {}".format(node, e))