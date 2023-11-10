# encoding: utf-8

from PySide2 import QtCore, QtWidgets

import maya.cmds as cmds

class QPickButton(QtWidgets.QPushButton):

    # Por las limitaciones de tener que usar strings para llamar comandos, necesitamos métodos estáticos para recoger los callbacks.
    # Se utiliza una variable estática para identificar qué objeto está usando el comando y llamar a sus eventos adecuadamente.
    _pickCommandTarget = None

    @staticmethod
    def _pickCallback():
        if QPickButton._pickCommandTarget != None:
            temp = QPickButton._pickCommandTarget
            QPickButton._pickCommandTarget = None
            temp._onPicked()
    
    @staticmethod
    def _abortCallback():
        if QPickButton._pickCommandTarget != None:
            temp = QPickButton._pickCommandTarget
            QPickButton._pickCommandTarget = None
            temp._onAbort()

    ### Señales ###

    # objectPicked: Señal disparada cuando se selecciona un objeto con el botón. También se dispara si se establece manualmente o se borra el objeto seleccionado.
    objectPicked = QtCore.Signal(str)

    ### Opciones del Pick Button ###
    # autoUpdateText: Cambia el texto del botón al nombre del objeto seleccionado automáticamente
    # autoUpdateToolTip : Cambia el tooltip del botón al nombre completo del objeto seleccionado automáticamente
    # rightClickClear: Permite borrar el objeto guardado haciendo click derecho en el botón
    def __init__(self, text="...", autoUpdateText=True, autoUpdateToolTip=True, rightClickClear=True):
        QtWidgets.QPushButton.__init__(self, text)
        self.defaultText = text
        self.defaultToolTip = ""

        self.setCheckable(True)
        self.setAutoRepeat(False)

        self.toggled.connect(self._onToggled)

        self._pickCommand = None
        self._pickedObject = None

        self._updateText = autoUpdateText
        self._updateToolTip = autoUpdateToolTip
        self._rightClickClear = rightClickClear

    ### Métodos de utilidad ###
    def getNodeNameFromPath(self, nodePath):
        return nodePath.split("|")[-1]

    ### Overrides ###
    # Se han sobrescrito los métodos setText y setTooltip para guardar el valor pasado a los mismos.
    # Este valor se utiliza como valor por defecto cuando se borra el objeto guardado cuando las opciones autoUpdateText o autoUpdateToolTip están activadas
    # Al cambiar el texto o tooltip automaticamente al seleccionar un objeto, QPickButton siempre llamará a los métodos setText y setTooltip de su clase base.
    # Así, solo se sobrescriben los valores por defecto de estos campos cuando el usuario los cambia manualmente.

    def setText(self, text):
        QtWidgets.QPushButton.setText(self, text)
        self.defaultText = text

    def setToolTip(self, toolTip):
        QtWidgets.QPushButton.setToolTip(self, toolTip)
        self.defaultToolTip = toolTip

    ### Propiedades ###

    def setAutoUpdateText(self, val):
        self._updateText = val
        if self._updateText and self._pickedObject != None:
            QtWidgets.QPushButton.setText(self, self.getNodeNameFromPath(self._pickedObject))

    def getAutoUpdateText(self):
        return self._updateText

    def setAutoUpdateToolTip(self, val):
        self._updateToolTip = val
        if self._updateToolTip and self._pickedObject != None:
            QtWidgets.QPushButton.setToolTip(self, self._pickedObject)

    def getAutoUpdateToolTip(self):
        return self._updateToolTip

    def setRightClickClear(self, val):
        self._rightClickClear = val
        
    def getRightClickClear(self):
        return self._rightClickClear

    def setPickedObject(self, obj):
        self._pickedObject = obj

        if self._updateText:
            if obj != None:
                QtWidgets.QPushButton.setText(self, self.getNodeNameFromPath(self._pickedObject))
            else:
                QtWidgets.QPushButton.setText(self, self.defaultText)

        if self._updateToolTip:
            if obj != None:
                QtWidgets.QPushButton.setToolTip(self, self._pickedObject)
            else:
                QtWidgets.QPushButton.setToolTip(self, self.defaultToolTip)

        self.objectPicked.emit(self._pickedObject)

    def clearPickedObject(self):
        self.setPickedObject(None)

    def getPickedObject(self):
        return self._pickedObject
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            if self._rightClickClear:
                self.clearPickedObject()
        elif event.button() == QtCore.Qt.MiddleButton:
            cmds.select(self.getPickedObject())
            
        super().mousePressEvent(event)

    ### Eventos privados ###
    # Funcionalidad propia del PickButton, no deben ser utilizados por el usuario.
    # _onPicked y _onAbort son los métodos llamados por el comando de selección cuando se selecciona u aborta la operación respectivamente.

    def _pick(self):
        QPickButton._pickCommandTarget = self
        self._pickCommand = cmds.pickContext(pc="from QtCustomWidgets.PickButton import QPickButton; QPickButton._pickCallback()", ac="from QtCustomWidgets.PickButton import QPickButton; QPickButton._abortCallback()")
        cmds.setToolTo(self._pickCommand)

    def _onToggled(self, checked):
        if checked:
            if self._pickCommand == None:
                if QPickButton._pickCommandTarget != None:
                    cmds.AbortCurrentTool()
                cmds.evalDeferred(self._pick)
            else:
                raise AssertionError("Attempted to run a _pickCommand while another one is already running.")
        else:
            cmds.AbortCurrentTool()

    def _onPicked(self):
        if self._pickCommand == None:
            raise AssertionError("OnPicked called while the pick command wasn't running.")

        temp = cmds.pickContext(self._pickCommand, q=True, sl=True)
        if temp == None:
            raise AssertionError("OnPicked called when no object was picked.")

        self.setPickedObject(temp)

        self._pickCommand = None
        self.setChecked(False)

    def _onAbort(self):
        if self._pickCommand == None:
            raise AssertionError("OnAbort called while the pick command wasn't running.")

        self._pickCommand = None
        self.setChecked(False)
