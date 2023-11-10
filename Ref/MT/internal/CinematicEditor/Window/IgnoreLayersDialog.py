from PySide2 import QtWidgets, QtGui

import maya.cmds as cmds

import CinematicEditor
import CinematicEditor.Window as CinematicEditorUtils
    
from QtCustomWidgets.UIFileWidget import UIFileWidget

from Utils.Maya.UndoContext import UndoContext

class IgnoreLayersDialog(QtWidgets.QDialog):

    def __init__(self, cutscene, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        
        # UI Loading
        uiFileWidget = UIFileWidget(r"CinematicEditor/Window/ui/IgnoreLayersDialog.ui")
        self.ui = uiFileWidget.ui
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(uiFileWidget)
        self.setLayout(layout)
        
        self.cutscene = cutscene

        # Window Configuration
        self.setWindowTitle("Layers to Export")
        
        # Widget Configuration
        self.ui.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        # Signals
        self.ui.byShotCheckBox.toggled.connect(self.onByShotCheckBoxToggled)
        self.ui.okButton.clicked.connect(self.onOkButtonPressed)
        self.ui.cancelButton.clicked.connect(self.reject)
        
    def displayMessageOnTable(self, message):
            self.ui.table.setRowCount(1)
            self.ui.table.setColumnCount(1)
            self.ui.table.verticalHeader().setVisible(False)
            self.ui.table.horizontalHeader().setVisible(False)
            self.ui.table.setItem(0, 0, QtWidgets.QTableWidgetItem(message))
        
    def refreshTable(self, checkAllshotsTheSame=False):
        if self.cutscene == None:
            self.displayMessageOnTable("<There are no shots on the scene>") # This should display "there is no cutscene on the scene", but to the user this message is more
            return
        
        shots = self.cutscene.getShots()
        if len(shots) == 0:
            self.displayMessageOnTable("<There are no shots on the scene>")
            return
        
        layers = cmds.ls(type="animLayer") or []
        rootLayer = cmds.animLayer(q=True, root=True)
        if rootLayer in layers:
            layers.remove(rootLayer)
        if len(layers) == 0:
            self.displayMessageOnTable("<There are no layers on the scene>")
            return
        
        if checkAllshotsTheSame:
            allShotsTheSame = True
            layersOnFirstShot = set(shots[0].getShotLayers())
            for shot in shots:
                differences = layersOnFirstShot.symmetric_difference(shot.getShotLayers())
                if len(differences) != 0:
                    allShotsTheSame = False
                    break
                
            signalsBlocked = self.ui.byShotCheckBox.blockSignals(True)
            self.ui.byShotCheckBox.setChecked(not allShotsTheSame)
            self.ui.byShotCheckBox.blockSignals(signalsBlocked)
            
        
        self.ui.table.setRowCount(len(layers))
        self.ui.table.setVerticalHeaderLabels(layers)
        self.ui.table.verticalHeader().setVisible(True)
        
        if self.byShot():
            self.ui.table.setColumnCount(len(shots))
            self.ui.table.horizontalHeader().setVisible(True)
            self.ui.table.setHorizontalHeaderLabels([shot.shotName for shot in shots])
        else:
            self.ui.table.setColumnCount(1)
            self.ui.table.horizontalHeader().setVisible(False)
        
        for j in range(self.ui.table.columnCount()):
            shotLayers = shots[j].getShotLayers()
            for i , layer in enumerate(layers):
                container = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.setContentsMargins(4, 4, 4, 4)
                container.setLayout(layout)
                self.ui.table.setCellWidget(i, j, container)
                
                checkButton = QtWidgets.QToolButton()
                checkButton.setCheckable(True)
                checkButton.setChecked(layer in shotLayers)
                checkButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                checkButton.setAutoFillBackground(True)
                layout.addWidget(checkButton)
                
                if self.byShot():
                    color = CinematicEditorUtils.tupleAsColor(shots[j].color)
                    backgroundColor = QtGui.QColor.fromHsl(color.hue(), color.saturation(), color.value() / 3)
                    
                    palette = checkButton.palette()
                    palette.setColor(palette.Highlight, color)
                    palette.setColor(palette.Window, backgroundColor)
                    palette.setColor(palette.Button, backgroundColor)
                    checkButton.setPalette(palette)

    def byShot(self):
        return self.ui.byShotCheckBox.isChecked()

    def onByShotCheckBoxToggled(self):
        self.refreshTable()

    def onOkButtonPressed(self):
        with UndoContext("Set Layers to Export"):
            shots = self.cutscene.getShots()
            for j in range(self.ui.table.columnCount()):
                affectedShots = [shots[j]] if self.byShot() else self.cutscene.getShots()
                for i in range(self.ui.table.rowCount()):
                    layer = self.ui.table.verticalHeaderItem(i).text()
                    for shot in affectedShots:
                        if self.ui.table.cellWidget(i, j).layout().itemAt(0).widget().isChecked():
                            shot.addLayer(layer)
                        else:
                            shot.removeLayer(layer)
                        
        self.accept()

    def showEvent(self, e):
        self.refreshTable(checkAllshotsTheSame=True)

if __name__ == "__main__":
    IgnoreLayersDialog(CinematicEditor.getCutscene(createIfNotExists=True)).exec_()