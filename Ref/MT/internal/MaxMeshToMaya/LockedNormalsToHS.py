"""
Author: Buliarca Cristian
Version: 1.0.1


Modified By: Jose Carlos Ramirez Sanchez
- Standalone Logic and UI
- Added capacity to find invalid vertices
- Minimal Refactoring
- Usage with UI:

import MaxMeshToMaya.LockedNormalsToHS as HS

for item in cmds.ls(sl=True):
    uiItem = HS.ProgressUI()
    uiItem.show()
    HS.SGtoHS(item, uiItem)
    uiItem.deleteUI()
"""

import maya.cmds as cmds
import math

class mbVector() :
    """provides 3D vector functionality simmilar to Maya"""
    x, y, z = 0.0, 0.0, 0.0
    
    def __init__( self, *initValues ) :
        if len( initValues ) == 1 :
            self.x = initValues[ 0 ][ 0 ]
            self.y = initValues[ 0 ][ 1 ]
            self.z = initValues[ 0 ][ 2 ]
        else :
            self.x = initValues[ 0 ]
            self.y = initValues[ 1 ]
            self.z = initValues[ 2 ]
    
    def __add__( self, other )	:
        return mbVector( [ self.x + other.x, self.y + other.y, self.z + other.z ] )
    
    def __sub__( self, other )	:
        return mbVector( [ self.x - other.x, self.y - other.y, self.z - other.z ] )
        
    def __mul__( self, scalar ) :
        return mbVector( [ self.x * scalar, self.y * scalar, self.z * scalar ] )
    
    def mag( self ) :
        return math.sqrt( self.x*self.x + self.y*self.y + self.z*self.z )
    
    def __repr__( self ) :
        return ( "<< " + str( math.floor( self.x * 100.0 + 0.49) / 100.0 ) + ", " + str( math.floor( self.y * 100.0 + 0.49 ) / 100.0 ) + ", " + str( math.floor( self.z * 100.0 + 0.49 ) / 100.0 ) + " >>" )

class ProgressUI():
    def __init__(self):
        self.window = cmds.window(title="Converting locked normals to Soft\Hard Edges")
        cmds.columnLayout(adjustableColumn=True)
        self.windowText = cmds.text( label='  Step 1 of 2  ', align='center' )
        self.progressBar = cmds.progressBar(maxValue=10, width=400, isInterruptable = True)
    
    def show(self):
        cmds.showWindow(self.window)
    
    def progress(self, step1):
        if(cmds.window(self.window, q=True, ex = True) ):
            cmds.progressBar(self.progressBar, edit=True, progress=step1+1)
    
    def setMaxVal(self, val):
        if(cmds.window(self.window, q=True, ex = True) ):
            if val ==0:
                val = 1
            cmds.progressBar(self.progressBar, edit=True, maxValue=val)
    
    def deleteUI(self):
        if(cmds.window(self.window, q=True, ex = True) ):
            cmds.deleteUI( self.window, window=True )
    
    def changeMessageTo(self, newText):
        if(cmds.window(self.window, q=True, ex = True) ):
            cmds.text(self.windowText, edit=True, label = newText)

def compareVFNormal(vert):
    def remove_values_from_list(the_list, val):
        for ii in range(the_list.count(val)):
            the_list.remove(val)
    
    obj = vert.split(".")
    nrVtx = obj[1].split("[")
    nrVtx = nrVtx[1].strip("]")
    edg = []
    vfInfo = cmds.polyInfo( vert, vf=True )
    vfList = []
    vfIList = vfInfo[0].split(' ')
    
    remove_values_from_list(vfIList, "")
    remove_values_from_list(vfIList, "\n")
    vfIList.pop(0)
    vfIList.pop(0)
    for i in range(len(vfIList)):
        fInf = vfIList[i].strip()
        vfList.append(obj[0]+".vtxFace["+nrVtx+"]["+fInf+"]")
    if (vfList):
        vfN = cmds.polyNormalPerVertex(vfList[-1],query=True, xyz=True )
        vfOldV = mbVector(vfN[0],vfN[1],vfN[2])
        for j in range(len(vfList)):
            vfN1 = cmds.polyNormalPerVertex(vfList[j], query=True, xyz=True )
            vfNewV = mbVector(vfN1[0],vfN1[1],vfN1[2])
            compV = vfOldV - vfNewV
            if compV.mag() != 0:
                hEdge = cmds.polyListComponentConversion(vfList[j], te= True)
                edg.append(hEdge[0])
            vfOldV = vfNewV
    else:
        cmds.warning("Invalid Vertex: {}".format(str(vert)))
    return edg

def SGtoHS(obj, UI=None):
    nrVtx = cmds.polyEvaluate(obj, v=True)
    if (type(nrVtx) == int):
        if (UI):
            UI.changeMessageTo('  Recalculating: ' + str(obj))
            UI.setMaxVal(nrVtx + 1)
        hardEdg = []
        
        for i in range(nrVtx):
            currVert = obj+".vtx["+str(i)+"]"
            cmpV = compareVFNormal(currVert)
            #hardEdg = mbJoin(hardEdg,cmpV)
            hardEdg = hardEdg + cmpV
            if (UI):
                UI.progress(i)
        
        cmds.polyNormalPerVertex (obj, ufn = True)
        cmds.polySoftEdge (obj, a=180)
            
        if len(hardEdg) != 0:
            cmds.select(hardEdg, r=True)
            cmds.polySoftEdge(a=0)
        
        if (UI):
            UI.progress(nrVtx + 1)
    else:
        print("Object '{}' is not a poligonal Object. Won't force any edge.".format(obj))