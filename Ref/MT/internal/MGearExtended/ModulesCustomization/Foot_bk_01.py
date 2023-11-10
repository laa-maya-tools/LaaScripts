import maya.cmds                  as cmds
import MGearExtended.PostProUtils as PostP

# utils
def getToeControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'fk0', checkSet)

def getToeReverseControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'bk1', checkSet)

def getHeelControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'heel', checkSet)

def getRollControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'roll', checkSet)

def getTipControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'bk0', checkSet)

def getFootprintControl(moduleName, side, checkSet=True):
    return PostP.getControl(moduleName, side, 'tip', checkSet)

def getControlsByFilter(moduleName, side, checkSet=True, toe=True, toeReverse=True, heel=True, roll=True, tip=True, footprint=True):
    result = []
    if toe: result.append( getToeControl(moduleName, side, checkSet) )
    if toeReverse: result.append( getToeReverseControl(moduleName, side, checkSet) )
    if heel: result.append( getHeelControl(moduleName, side, checkSet) )
    if roll: result.append( getRollControl(moduleName, side, checkSet) )
    if tip: result.append( getTipControl(moduleName, side, checkSet) )
    if footprint: result.append( getFootprintControl(moduleName, side, checkSet) )
    return [member for member in result if member]

def getAllControls(moduleName, side, checkSet=True):
    return getControlsByFilter(moduleName, side, checkSet)
