from PySide2 import QtWidgets

from CinematicEditor.Cutscene import CutsceneExportListener

import CinematicEditor.MasterSlave as MasterSlave

import ActorManager

class CinematicExportDialog(QtWidgets.QDialog, CutsceneExportListener):
    
    def __init__(self, parent, cutscene):
        super().__init__(parent)
        
        self.cutscene = cutscene
        
        self.cancelled = False
        self.shotsToExport = []
        self.stepCount = 0
        self.currentStep = 0
        
        self.setWindowTitle("Export cutscene")
        self.setMinimumWidth(400)
        
        self.setLayout(QtWidgets.QVBoxLayout())
        
        self.headerLabel = QtWidgets.QLabel()
        self.layout().addWidget(self.headerLabel)
        
        self.mainProgressGroupBox = QtWidgets.QGroupBox()
        self.mainProgressGroupBox.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.mainProgressGroupBox)
        
        self.mainProgressLabel = QtWidgets.QLabel()
        self.mainProgressGroupBox.layout().addWidget(self.mainProgressLabel)
        
        self.mainProgressBar = QtWidgets.QProgressBar()
        self.mainProgressGroupBox.layout().addWidget(self.mainProgressBar)
        
        self.secundaryProgressGroupBox = QtWidgets.QGroupBox()
        self.secundaryProgressGroupBox.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.secundaryProgressGroupBox)
        
        self.secundaryProgressLabel = QtWidgets.QLabel()
        self.secundaryProgressGroupBox.layout().addWidget(self.secundaryProgressLabel)
        
        self.secundaryProgressBar = QtWidgets.QProgressBar()
        self.secundaryProgressGroupBox.layout().addWidget(self.secundaryProgressBar)
        
        self.layout().addStretch()
        
        self.cancelExportButton = QtWidgets.QPushButton("Cancel Export")
        self.cancelExportButton.clicked.connect(self.reject)
        self.layout().addWidget(self.cancelExportButton)
        
        self.closeButton = QtWidgets.QPushButton("Close")
        self.closeButton.setVisible(False)
        self.closeButton.clicked.connect(self.accept)
        self.layout().addWidget(self.closeButton)
        
    def checkCancelled(self):
        QtWidgets.QApplication.processEvents()
        return not self.cancelled

    def showEvent(self, event):
        self.headerLabel.setText("Starting...")
        self.mainProgressGroupBox.setVisible(False)
        self.secundaryProgressGroupBox.setVisible(False)
        self.cancelExportButton.setVisible(False)
        self.closeButton.setVisible(False)
        
    def reject(self):
        if self.closeButton.isVisible():
            self.accept()
        elif not self.cancelled:
            result = QtWidgets.QMessageBox.question(self, "Cancel Export", "Are you sure you want to cancel the current export?")
            if result == QtWidgets.QMessageBox.Yes:
                self.cancelled = True
                super().reject()
        
    def export(self, shots=[], actors=[], cameras=False, structure=False, forceShots=False, forceActors=False, restoreAfterExport=True, checkout=True, convert=True, compile=True, runCharEditor=True):
        if structure:
            actorsToCheckLoaded = self.cutscene.getCutsceneActors()
        else:
            actorsToCheckLoaded = actors
        
        unloadedActors = [cutsceneActor for cutsceneActor in actorsToCheckLoaded if not ActorManager.isActorLoaded(cutsceneActor.actor)]
        if unloadedActors:
            if structure:
                message = "Unable to export: Actor references' must be loaded in order to export the cutscene's structure."
            else:
                message = "Unable to export: Actor references' must be loaded in order to export their animation."
            QtWidgets.QMessageBox.warning(self, "Export", message)
            return
        
        masterSlaveFile = MasterSlave.MasterSlaveFile(self.cutscene)
        if masterSlaveFile.exists():
            masterSlaveFile.load()
            shots = [shot for shot in shots if masterSlaveFile.ownsShot(shot)]
            shotsToUpdate = [shot for shot in self.cutscene.getShots() if masterSlaveFile.ownsShot(shot)]
        else:
            shotsToUpdate = None
        
        invalidRangeShots = []
        for shot in shots:
            if not shot.start.is_integer() or not shot.end.is_integer():
                invalidRangeShots.append(shot)
        if invalidRangeShots:
            message = "Unable to export: Shot range is not an integer number:"
            for shot in invalidRangeShots:
                message += "\n- {}".format(shot.shotName)
            QtWidgets.QMessageBox.warning(self, "Export", message)
            return
        
        conflictingRemapShots = []
        for shot in shots:
            cutsceneActors = shot.getCutsceneActors()
            cutsceneActors = [actor.remap or actor for actor in cutsceneActors if actor in actors]
            if len(cutsceneActors) != len(set(cutsceneActors)):
                conflictingRemapShots.append(shot)
        if conflictingRemapShots:
            message = "Unable to export Actor animation, conflicting Actor remaps on Shots:"
            for shot in conflictingRemapShots:
                message += "\n- {}".format(shot.shotName)
            QtWidgets.QMessageBox.warning(self, "Export", message)
            return
                
        self.show()
        return self.cutscene.export(shots=shots, actors=actors, cameras=cameras, structure=structure, forceShots=forceShots, forceActors=forceActors, shotsToUpdate=shotsToUpdate, restoreAfterExport=restoreAfterExport, checkout=checkout, convert=convert, compile=compile, runCharEditor=runCharEditor, exportListener=self)

    def onStartExport(self, shots, actors, cameras, structure, compile):
        QtWidgets.QApplication.processEvents()
        
        self.shotsToExport = shots
        
        self.currentStep = 0
        self.stepCount = 0
        if actors:
            self.stepCount += len(shots)
        if cameras:
            self.stepCount += 1
        if structure:
            self.stepCount += 1
        if (actors or cameras) and compile:
            self.stepCount += 1
        
        self.headerLabel.setText("Exporting Cutscene: {}".format(self.cutscene.getCutsceneName()))
        
        self.mainProgressGroupBox.setVisible(True)
        self.mainProgressLabel.setText("Starting...")
        self.mainProgressBar.setMaximum(self.stepCount)
        self.mainProgressBar.setValue(self.currentStep)
        
        self.secundaryProgressGroupBox.setVisible(False)
        
        self.cancelExportButton.setVisible(True)
        self.closeButton.setVisible(False)
        
        return self.checkCancelled()
        
    def onExportActor(self, actor, actorIndex, shot, shotIndex, actors):
        QtWidgets.QApplication.processEvents()
        
        self.currentStep = shotIndex + 1
        
        self.mainProgressGroupBox.setVisible(True)
        self.mainProgressLabel.setText("Exporting Shot: {} ({}/{})".format(shot.shotName, shotIndex + 1, len(self.shotsToExport)))
        self.mainProgressBar.setValue(self.currentStep)
        
        self.secundaryProgressGroupBox.setVisible(True)
        self.secundaryProgressLabel.setText("Exporting Actor: {} ({}/{})".format(actor.actor.getNamespace(), actorIndex + 1, len(actors)))
        self.secundaryProgressBar.setMaximum(len(actors))
        self.secundaryProgressBar.setValue(actorIndex + 1)
        
        return self.checkCancelled()

    def onPreExportCameras(self, shots):
        QtWidgets.QApplication.processEvents()
        
        self.currentStep += 1
        
        self.mainProgressGroupBox.setVisible(True)
        self.mainProgressLabel.setText("Exporting Cameras...")
        self.mainProgressBar.setValue(self.currentStep)
        
        self.secundaryProgressGroupBox.setVisible(True)
        self.secundaryProgressLabel.setText("")
        self.secundaryProgressBar.setMaximum(len(shots))
        self.secundaryProgressBar.setValue(0)
        
        return self.checkCancelled()

    def onExportCamera(self, camera, shot, shotIndex):
        QtWidgets.QApplication.processEvents()
        
        self.secundaryProgressGroupBox.setVisible(True)
        self.secundaryProgressLabel.setText("Exporting Shot Camera: {} - {} ({}/{})".format(shot.shotName, camera, shotIndex + 1, len(self.shotsToExport)))
        self.secundaryProgressBar.setValue(shotIndex + 1)
        
        return self.checkCancelled()

    def onCompile(self):
        QtWidgets.QApplication.processEvents()
        
        self.currentStep += 1
        
        self.mainProgressGroupBox.setVisible(True)
        self.mainProgressLabel.setText("Compiling...")
        self.mainProgressBar.setValue(self.currentStep)
        
        self.secundaryProgressGroupBox.setVisible(False)
        
        return self.checkCancelled()

    def onExportStructure(self):
        QtWidgets.QApplication.processEvents()
        
        self.currentStep += 1
        
        self.mainProgressGroupBox.setVisible(True)
        self.mainProgressLabel.setText("Exporting Structure...")
        self.mainProgressBar.setValue(self.currentStep)
        
        self.secundaryProgressGroupBox.setVisible(False)
        
        return self.checkCancelled()

    def onFinishExport(self):
        QtWidgets.QApplication.processEvents()
        
        if self.checkCancelled():
            self.headerLabel.setText("<html><p>Export Finished! <img width='12' height='12' src=':/confirm.png'/></p></html>")
            
            self.mainProgressGroupBox.setVisible(False)
            self.secundaryProgressGroupBox.setVisible(False)
            
            self.cancelExportButton.setVisible(False)
            self.closeButton.setVisible(True)
        
        return True

    def onError(self, exception):
        QtWidgets.QApplication.processEvents()
        
        self.headerLabel.setText("<html><p>Export Error! <img width='12' height='12' src=':/error.png'/></p><p style=\"color: rgb(255, 0, 0)\">{}</p></html>".format(exception))
        
        self.mainProgressGroupBox.setVisible(False)
        self.secundaryProgressGroupBox.setVisible(False)
        
        self.cancelExportButton.setVisible(False)
        self.closeButton.setVisible(True)
        
        return True
