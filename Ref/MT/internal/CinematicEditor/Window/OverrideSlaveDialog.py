from PySide2 import QtWidgets

import CinematicEditor.MasterSlave as MasterSlave
    
from QtCustomWidgets.UIFileWidget import UIFileWidget

from Utils.Maya.UndoContext import clearUndo

class OverrideSlaveDialog(QtWidgets.QDialog):

    def __init__(self, masterSlaveFile : MasterSlave.MasterSlaveFile, parent=None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        
        # UI Loading
        uiFileWidget = UIFileWidget(r"CinematicEditor/Window/ui/OverrideSlaveDialog.ui")
        self.ui = uiFileWidget.ui
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(uiFileWidget)
        self.setLayout(layout)
        
        self.masterSlaveFile = masterSlaveFile

        # Window Configuration
        self.setWindowTitle("Override Slave")
        
        # Signals
        self.ui.slavesList.itemSelectionChanged.connect(self.refreshOwnedShotsList)
        self.ui.overrideButton.clicked.connect(self.onOverrideButtonPressed)
        self.ui.cancelButton.clicked.connect(self.reject)
        
    def displayMessageOnList(self, message):
        self.ui.slavesList.clear()
        self.ui.slavesList.addItem(message)
        
    def refresh(self):
        self.refreshSlavesList()
        self.refreshOwnedShotsList()
        
    def refreshSlavesList(self):
        slaveIDs = self.masterSlaveFile.getSlaveIDs()
        slaveIDs.remove(self.masterSlaveFile.cutscene.masterSlaveID)
        if len(slaveIDs) == 0:
            self.displayMessageOnList("<There are no other slaves for this cutscene>")
            return
        
        items = ["ID {}".format(slaveID) for slaveID in slaveIDs]
        
        self.ui.slavesList.clear()
        self.ui.slavesList.addItems(items)
        
    def refreshOwnedShotsList(self):
        selectedSlaves = self.getSelectedSlaves()
        ownedShots = []
        for slave in selectedSlaves:
            ownedShots += self.masterSlaveFile.getOwnedShots(id=slave)
            
        items = [shot.shotName for shot in ownedShots]
        
        self.ui.ownedShotsList.clear()
        self.ui.ownedShotsList.addItems(items)
        
    def getSelectedSlaves(self):
        items = self.ui.slavesList.selectedItems()
        ids = [int(item.text().split(" ")[-1]) for item in items]
        return ids
    
    def onOverrideButtonPressed(self):
        selectedSlaves = self.getSelectedSlaves()
        if len(selectedSlaves) == 0:
            QtWidgets.QMessageBox.warning(self, "Override Slave", "Please select another Slave to override.")
            return
        
        message = "Overriding a Slave means taking the place of that Slave.\n\
* You will be able to modify the overriden slave's shots.\n\
* Any delegated shot you have already claimed will remain unchanged.\n\n\
This process cannot be undone, are you sure you want to override this Slave?\n\n\
WARNING: This option should be used to create new versions of a Slave and not to take their delegated Shots. The previous Slave file will still be able to modify the Shots so there might be conflicts, proceed with extreme caution!"
        result = QtWidgets.QMessageBox.question(self, "Override Slave", message)
        if result != QtWidgets.QMessageBox.Yes:
            return
        
        self.masterSlaveFile.overrideSlave(selectedSlaves[0])
        clearUndo()
                        
        self.accept()

    def showEvent(self, e):
        self.refresh()
