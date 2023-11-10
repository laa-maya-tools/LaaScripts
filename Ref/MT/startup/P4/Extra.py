import P4.Tools as P4Tools

import maya.cmds as cmds

import maya.api.OpenMaya as OpenMaya
import maya.OpenMaya as OpenMaya1
import P4.Tools as P4Tools

def init():
    CheckOutWhenSaving.init()

def checkoutCurrentFile(quiet=False, showSuccessMessage=False):
    currentFile = cmds.file(q=True, sn=True)
    if currentFile:
        p4File = P4Tools.P4File(currentFile)
        if p4File.isFileUnderPerforcePath():
            p4File.smartCheckout()
            if showSuccessMessage and not quiet:
                cmds.confirmDialog(title="Checkout Current File", message="The file has been checked out.\n\n{}.".format(currentFile))
        else:
            if not quiet:
                cmds.confirmDialog(title="Checkout Current File", message="Unable to check out: The file is not under the Perforce path!\n\n{}.".format(currentFile))
    else:
        if not quiet:
            cmds.confirmDialog(title="Checkout Current File", message="Unable to check out: There is no file currently opened!")


class CheckOutWhenSaving():
    
    OPTIONVAR_ENABLED = "CHECKOUTWHENSAVING_ENABLED"
    OPTIONVAR_AUTOMATIC = "CHECKOUTWHENSAVING_AUTOMATIC"
    
    beforeSaveCallback = None
    
    @classmethod
    def isEnabled(cls):
        if not cmds.optionVar(exists=cls.OPTIONVAR_ENABLED):
            defaultValue = True
            cls.setEnabled(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_ENABLED)
    
    @classmethod
    def setEnabled(cls, enabled):
        cmds.optionVar(iv=(cls.OPTIONVAR_ENABLED, enabled))
    
    @classmethod
    def isAutomatic(cls, checkParentOption=True):
        if checkParentOption and not cls.isEnabled():
            return False    # Automatic CheckOut can only be enabled when the feature itself is enabled
        
        if not cmds.optionVar(exists=cls.OPTIONVAR_AUTOMATIC):
            defaultValue = False
            cls.setAutomatic(defaultValue)
            return defaultValue
        else:
            return cmds.optionVar(q=cls.OPTIONVAR_AUTOMATIC)
    
    @classmethod
    def setAutomatic(cls, automatic):
        cmds.optionVar(iv=(cls.OPTIONVAR_AUTOMATIC, automatic))
    
    @classmethod
    def askToMarkForAdd(cls, p4File, auto):
        option_yes = "Yes"
        option_no = "No"
        option_canel = "Cancel"
        
        if auto:
            result = option_yes
        else:
            result = cmds.confirmDialog(title="Save File", message="Do you want to Mark the File for Add?", 
                        button=[option_yes, option_no, option_canel], defaultButton=option_yes, cancelButton=option_canel, dismissString=option_canel)
            
        if result == option_canel:
            return False
        elif result == option_yes:
            if p4File.doesLocalFileExist():
                p4File.setLocalFileReadOnly(False)
            else:
                p4File.createLocalEmptyFile()
            p4File.markFileForAdd()
            return True
        elif result == option_no:
            return None
    
    @classmethod
    def askToCheckOut(cls, p4File, auto):
        option_yes = "Yes"
        option_no = "No"
        option_canel = "Cancel"
        
        if auto:
            result = option_yes
        else:
            result = cmds.confirmDialog(title="Save File", message="Do you want to Checkout the File?", 
                        button=[option_yes, option_no, option_canel], defaultButton=option_yes, cancelButton=option_canel, dismissString=option_canel)
            
        if result == option_canel:
            return False
        elif result == option_yes:
            p4File.checkoutFile()
            return True
        elif result == option_no:
            return None
    
    @classmethod
    def askToSyncAndCheckOut(cls, p4File, auto):
        option_syncAndCheckout = "Sync and Checkout"
        option_checkoutWithoutSync = "Checkout without Sync"
        option_dontCheckout = "Don't Checkout"
        option_canel = "Cancel"
        
        if auto:
            result = option_checkoutWithoutSync
        else:
            result = cmds.confirmDialog(title="Save File", message="The file is not up to date to the last version on Perforce. Do you wan't to Sync it first?", 
                        button=[option_syncAndCheckout, option_checkoutWithoutSync, option_dontCheckout, option_canel], defaultButton=option_checkoutWithoutSync, cancelButton=option_canel, dismissString=option_canel)
            
        if result == option_canel:
            return False
        elif result == option_syncAndCheckout:
            p4File.syncFile()
            p4File.checkoutFile()
            return True
        elif result == option_checkoutWithoutSync:
            p4File.checkoutFile()
            return True
        elif result == option_dontCheckout:
            return None
    
    @classmethod
    def askToSetWritable(cls, p4File, auto):
        option_yes = "Yes"
        option_canel = "Cancel"
        
        if auto:
            result = option_yes
        else:
            result = cmds.confirmDialog(title="Save File", message="The file you are attempting to save is marked as Read Only. Do you want to mark it as writable?", 
                        button=[option_yes, option_canel], defaultButton=option_yes, cancelButton=option_canel, dismissString=option_canel)
            
        if result == option_canel:
            return False
        elif result == option_yes:
            p4File.setLocalFileReadOnly(False)
            return True
        
    @classmethod
    def onBeforeSave(cls, clientData):
        if cls.isEnabled():
            auto = cls.isAutomatic()
            
            fileName = OpenMaya1.MFileIO.beforeSaveFilename()   # This class is not available on the API 2.0
            p4File = P4Tools.P4File(fileName)
            
            if not p4File.doesLocalFileExist() or p4File.isLocalFileReadOnly(): # We only ask if the file didn't exist or it was marked as Read Only, so we don't keep asking for the same file.
                if p4File.isFileUnderPerforcePath():
                    if p4File.isFileInDepot():
                        if not p4File.isFileCheckedOut():
                            if p4File.isFileLastRevision():
                                result = cls.askToCheckOut(p4File, auto)
                                if result != None:
                                    return result
                            else:
                                result = cls.askToSyncAndCheckOut(p4File, auto)
                                if result != None:
                                    return result
                    else:
                        result = cls.askToMarkForAdd(p4File, False)   # We never Mark for Add automatically
                        if result != None:
                            return result
                    
            if p4File.doesLocalFileExist() and p4File.isLocalFileReadOnly():
                result = cls.askToSetWritable(p4File, auto)
                if result != None:
                    return result
        
        return True
    
    @classmethod
    def registerCallback(cls):
        cls.unregisterCallback()
        cls.beforeSaveCallback = OpenMaya.MSceneMessage.addCheckCallback(OpenMaya.MSceneMessage.kBeforeSaveCheck, cls.onBeforeSave)
    
    @classmethod
    def unregisterCallback(cls):
        if cls.beforeSaveCallback != None:
            OpenMaya.MMessage.removeCallback(cls.beforeSaveCallback)
            cls.beforeSaveCallback = None
        
    @classmethod
    def init(cls):
        cls.registerCallback()