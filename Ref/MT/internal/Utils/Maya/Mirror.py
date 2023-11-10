from mutils.mirrortable import MirrorTable, MirrorOption, KeysOption, MirrorPlane, RE_RIGHT_SIDE, RE_LEFT_SIDE

def mirrorControls(controls, mirrorOption=MirrorOption.Swap, keysOption=KeysOption.SelectedRange, mirrorPlane=MirrorPlane.YZ):
    mirrorTable = MirrorTable.fromObjects(controls, leftSide=RE_LEFT_SIDE, rightSide=RE_RIGHT_SIDE, mirrorPlane=mirrorPlane)
    mirrorTable.load(controls, namespaces=None, option=mirrorOption, keysOption=keysOption)
