import tempfile, os
import maya.cmds                        as cmds
import maya.mel                         as mel
import WindowDockBase                   as wdBase
import Utils.Maya.MayaFBX               as MayaFBX
import MaxMeshToMaya.LockedNormalsToHS  as HS

from importlib import reload
reload(HS)

from PySide2                        import QtGui, QtWidgets, QtCore
from Utils.Python.FileExplorer      import ShowFileExplorer


class MaxToMayaWindow(wdBase.UIDockManager):
    tempFolder = os.path.join( tempfile.gettempdir(), "SendToMaya")
    
    def __init__(self, parent=None):
        super(MaxToMayaWindow, self).__init__("MaxToMaya", r"MaxMeshToMaya/Window/ui/MainWindow.ui")
        self.setWindowTitle('Max to Maya')
        self.workingFolder = MaxToMayaWindow.tempFolder
        self.optionsVisible = False
        self.upArrowPixmap      = QtGui.QIcon(":/arrowUp.png").pixmap(QtCore.QSize(12,12))
        self.downArrowPixmap    = QtGui.QIcon(":/arrowDown.png").pixmap(QtCore.QSize(12,12))
        
        self.ui.led_Folder.setText(self.tempFolder)
        self.ui.btn_Options.setIcon(self.upArrowPixmap)
        self.ui.btn_OpenFolder.setIcon(QtGui.QIcon(":/arrowRight.png"))
        self.ui.btn_Refresh.setIcon(QtGui.QIcon(":/refresh.png"))
        
        #---------- Signals
        self.ui.btn_BrowseFolder.clicked.connect(self.btn_BrowseFolder_clicked)
        self.ui.btn_OpenFolder.clicked.connect(self.btn_OpenFolder_Clicked)
        self.ui.btn_Import.clicked.connect(self.btn_Import_Clicked)
        self.ui.btn_DeleteAll.clicked.connect(self.btn_DeleteAll_Clicked)
        self.ui.btn_DeleteSelected.clicked.connect(self.btn_DeleteSelected_Clicked)
        self.ui.btn_Refresh.clicked.connect(self.btn_Refresh_Clicked)
        self.ui.btn_Options.clicked.connect(self.btn_Options_clicked)
        
        #---------- Initialization
        self.LoadFolderFBXs(self.workingFolder)
        self.CheckOptionsVisible()
    
    def IsDeformableObject(self, node):
        rels = cmds.listRelatives(node, path=True, shapes=True)
        defRels = cmds.ls(rels, type='deformableShape')
        if (len(defRels) > 0):
            return True
        return False
    
    def LoadFolderFBXs(self, path):
        self.ui.lst_Files.clear()
        if (os.path.isdir(path)):
            files = [f for f in os.listdir(path) if (os.path.isfile(os.path.join(path, f)) and f.lower().endswith(".fbx"))]
            for file in files:
                self.ui.lst_Files.addItem(os.path.splitext(file)[0])
    
    def ShowMessage(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.exec()
    
    def DeleteFile(self, fileName):
        try:
            os.remove(os.path.join(self.ui.led_Folder.text(), "{}.fbx".format(fileName)))
        except:
            self.ShowMessage("Could not delete file: {}".format(fileName))
    
    def CleanUserAttributes(self, node):
        userDefAttrs = cmds.listAttr(node, userDefined=True)
        if (userDefAttrs):
            for attr in cmds.listAttr(node, userDefined=True):
                cmds.deleteAttr("{}.{}".format(node, attr))
    
    def FlipYZAxes(self, node):
        #If it has a parent, then unparent before flipping axes and then reparent later.
        #We use Temporal parent nodes in order to not let maya change any name of the unparented nodes.
        tempParentA = cmds.group(empty=True)
        tempParentB = cmds.group(empty=True)
        parent = cmds.listRelatives(node, parent=True, path=True)
        if (parent):
            node = cmds.parent(node, tempParentA)
        children = cmds.listRelatives(node, children=True, noIntermediate=True, type="transform", path=True)
        if (children):
            for i in range(len(children)):
                children[i] = cmds.parent(children[i], tempParentB)
        
        rot = cmds.xform(node, q=True, rotation=True)
        cmds.xform(node, rotation=[-90,0,0])
        cmds.makeIdentity(node, apply=True, rotate=1, n=0, pn=1)
        rot[0] += 90
        cmds.xform(node, rotation=rot)
        # If we flip the Axes we want the internal vertex data to be clean, and as we
        #can't manually reset its '.vrts' data, the only way as today is to put a 
        #deformar and clean history...
        if (self.IsDeformableObject(node)):
            cmds.lattice(node, dv=(2, 2, 2), oc=True)
            cmds.bakePartialHistory(node, preCache=True)
        
        if (parent):
            node = cmds.parent(node, parent[0])
        if (children):
            for i in range(len(children)):
                children[i] = cmds.parent(children[i], node)
        cmds.delete([tempParentA, tempParentB])
    
    def RecalculateEdges(self, node):
        uiItem = HS.ProgressUI()
        uiItem.show()
        HS.SGtoHS(node, uiItem)
        uiItem.deleteUI()
    
    def CheckOptionsVisible(self):
        if (self.optionsVisible):
            self.ui.wdg_OptionsContent.setHidden(False)
            self.ui.btn_Options.setIcon(self.downArrowPixmap)
        else:
            self.ui.wdg_OptionsContent.setHidden(True)
            self.ui.btn_Options.setIcon(self.upArrowPixmap)
    
    # -----------------------------------------
    # ------------------ Slots ----------------
    # -----------------------------------------
    def btn_Options_clicked(self):
        self.optionsVisible = not self.optionsVisible
        self.CheckOptionsVisible()
    
    def btn_BrowseFolder_clicked(self):        
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Export Folder", self.workingFolder, QtWidgets.QFileDialog.ShowDirsOnly)
        if (path != ""):
            self.workingFolder = path
            self.ui.led_Folder.setText(path)
            self.LoadFolderFBXs(self.workingFolder)
    
    def btn_OpenFolder_Clicked(self):
        ShowFileExplorer(self.ui.led_Folder.text())
    
    def btn_Import_Clicked(self):
        selItems = self.ui.lst_Files.selectedItems()
        if (selItems):
            MaxImportPreset = MayaFBX.FBXImportPreset({
                MayaFBX.FBXSettings.Import.IncludeGrp.Geometry.unlockNormals : 1,
                MayaFBX.FBXSettings.Import.AdvancedOptions.AxisConversion.axisConversion : 1,
            })
            
            #Force Edges option and Lock Normals: Must import with normals locked
            if (self.ui.chk_ForceEdges.isChecked() or self.ui.chk_LockNormals.isChecked()):
                MaxImportPreset.SetProperty(MayaFBX.FBXSettings.Import.IncludeGrp.Geometry.unlockNormals, 0)
            
            MayaFBX.LoadPreset(MaxImportPreset, verbose=True)
            
            allNewNodes = []
            for item in selItems:
                current = cmds.ls(dag=True, transforms=True, long=True)
                MayaFBX.ImportFBX(os.path.join(self.ui.led_Folder.text(), "{}.fbx".format(item.text())))
                updated = cmds.ls(dag=True, transforms=True, long=True)
                new = [x for x in updated if x not in current]
                allNewNodes += new
                for node in new:
                    # Clean attributes created on import
                    if (self.ui.chk_CleanAttributes.isChecked()):
                        self.CleanUserAttributes(node)
                    # Flip Z-Y Axes
                    if (self.ui.chk_FlipAxis.isChecked()):
                        self.FlipYZAxes(node)
                    # Force Edges: Racalculate Hard and Soft Edges
                    if (self.ui.chk_ForceEdges.isChecked()):
                        self.RecalculateEdges(node)
            
            if (allNewNodes):
                cmds.select(allNewNodes)
            
            # In order to not have duplicated shading networks (and duplicated materials), we use
            # an option of the "cleanUpScene" Maya integrated Tool, wich seems to be only
            # available with mel, and only works if evaluated deferred:
            cmds.evalDeferred("mel.eval('removeDuplicateShadingNetworks 0')")
    
    def btn_DeleteAll_Clicked(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setText("Do you really want to Delete All files?")
        msgBox.setWindowTitle("Delete All")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        if (not msgBox.exec_() == QtWidgets.QMessageBox.Ok):
            return
        
        for i in range(self.ui.lst_Files.count()):
            item = self.ui.lst_Files.item(i)
            self.DeleteFile(item.text())
        
        self.LoadFolderFBXs(self.workingFolder)
    
    def btn_DeleteSelected_Clicked(self):
        selItems = self.ui.lst_Files.selectedItems()
        if (selItems):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Question)
            msgBox.setText("Do you really want to Delete the Selected files?")
            msgBox.setWindowTitle("Delete Selected")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if (not msgBox.exec_() == QtWidgets.QMessageBox.Ok):
                return
            
            for item in selItems:
                self.DeleteFile(item.text())
            
            self.LoadFolderFBXs(self.workingFolder)
    
    def btn_Refresh_Clicked(self):
        self.LoadFolderFBXs(self.workingFolder)

if __name__ == '__main__':
    try:
        if maxToMayaWindow.isVisible():
            maxToMayaWindow.close()
    except NameError:
        pass
    maxToMayaWindow = MaxToMayaWindow()
    maxToMayaWindow.showWindow(debug=True)