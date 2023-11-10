from P4 import P4, P4Exception

import subprocess
import os, stat

# -----------------------------------
# | General Perforce Functions      |
# -----------------------------------

# Connection singleton, to avoid creating multiple connections
_connectionInstance = None

def getConnection(forceNew=False):
    global _connectionInstance
    if forceNew or _connectionInstance == None:
        _connectionInstance = P4()
        _connectionInstance.encoding = "iso8859-1"
    return _connectionInstance

# Perforce commands always return arrays, checks if the output is an empty array.
# They sometimes also return an array with an empty dictionary, so checks that as well.
def isValidP4Output(p4Output):
    return p4Output != [] and p4Output != [{}]

# Auxiliar function to check if a file's state is "Move".
# Moved files have two parts: the "add" file (with the new name) and the "delete" file (with the old name)
def isActionMove(action, add=False, delete=False):
    return (add and action == "move/add") or (delete and action == "move/delete")

# Auxiliar function to check if a file's state is "Add".
def isActionAdd(action, includeMarkedForMove=True):
    return action == "add" or (includeMarkedForMove and isActionMove(action, add=True))

# Auxiliar function to check if a file's state is "Delete".
def isActionDelete(action, includeMarkedForMove=True):
    return action == "delete" or (includeMarkedForMove and isActionMove(action, delete=True))

# Auxiliar function to check if a file's state is "Edit".
def isActionEdit(action, includeMarkedForAdd=True, includeMarkForDelete=True, includeMarkedForMove=True):
    return action == "edit" or (includeMarkedForAdd and isActionAdd(action, includeMarkedForMove=includeMarkedForMove)) or (includeMarkForDelete and isActionDelete(action, includeMarkedForMove=includeMarkedForMove))


# -----------------------------------
# | P4Changelist                    |
# -----------------------------------
# | Wraps a Perforce changelist.    |
# -----------------------------------

class P4Changelist(object):

    # -----------------------------------
    # | General wrapper methods         |
    # -----------------------------------

    def __init__(self, changelistNumber):
        self.changelistNumber = changelistNumber

    def __eq__(self, other):
        if issubclass(type(other), P4Changelist):
            return self.changelistNumber == other.changelistNumber
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.changelistNumber)

    # -----------------------------------
    # | Static methods                  |
    # -----------------------------------

    # Creates a new changelist with the provided description and returns a P4Changelist instance.
    # A new changelist will be created even if there is already a changelist with the same description.
    @staticmethod
    def createChangelist(description):
        connection = getConnection()
        with connection.connect():
            result = connection.save_change({'Change': 'new', 'Description': description})[0]
            changelistNumber = int(result.split(" ")[1])    # The result says "Changelist X created", so we split it and pick the second element to retrieve the changelist number (X).
            return P4Changelist(changelistNumber)

    # Returns a P4Changelist wrapper for the default changelist.
    @staticmethod
    def getDefaultChangelist():
        return P4Changelist("default")

    # Returns the changelist with the provided description as a P4Changelist instance.
    # If such a changelist doesn't exist and the "createIfNotExists" flag is set to True, a new one will be created and returned.
    @staticmethod
    def getChangelistByDescription(description, client=None, createIfNotExists=False):
        if not description.endswith("\n"):
            description += "\n"
            
        descriptionLower = description.lower()
        if descriptionLower == "default\n":
            return "default"

        connection = getConnection()
        with connection.connect():
            if client == None:
                client = connection.client
                
            client = client.lower()
                
            changelists = [changelist["change"] for changelist in connection.run("changes", "--me", "-s", "pending")]
            if len(changelists) > 0:
                changelistDescriptions = connection.run("describe", changelists)
                for changelistDescription in changelistDescriptions:
                    if changelistDescription["client"].lower() == client and changelistDescription["desc"].lower() == descriptionLower:
                        return P4Changelist(changelistDescription["change"])

        if createIfNotExists:
            return P4Changelist.createChangelist(description)
        else:
            return None

    # -----------------------------------
    # | General methods                 |
    # -----------------------------------

    # Quick access to the connection for the class instances.
    @property
    def connection(self):
        return getConnection()

    # Checks if a changelist is valid. In order for a changelist to be valid it must:
    # * It's changelist number must exist on Perforce.
    # * The changelist must be pending (not submitted).
    # * The changelist must be owned by this user.
    def isValidChangelist(self):
        if self.changelistNumber == None:
            return False
        if self.changelistNumber == "default":
            return True

        with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
            changelistInfo = self.connection.run("describe", self.changelistNumber)
            if not isValidP4Output(changelistInfo):
                return False

            changelistInfo = changelistInfo[0]
            return changelistInfo["status"].lower() == "pending" and changelistInfo["user"].lower() == self.connection.user.lower() and changelistInfo["client"].lower() == self.connection.client.lower()

    # -----------------------------------
    # | Changelist methods              |
    # -----------------------------------

    # Gets the description of the changelist.
    # TODO: Refactor to property if modification is needed.
    def getChangelistDescription(self):
        if self.isValidChangelist():
            with self.connection.connect():
                return self.connection.run("describe", self.changelistNumber)[0]["desc"]
        else:
            raise P4Exception("Error: Unable to retrieve changelist description - The changelist {} is not valid.".format(self.changelistNumber))


# -----------------------------------
# | P4File                          |
# -----------------------------------
# | Wraps a file, allowing to       |
# | manage it easily on Perforce.   |
# -----------------------------------

class P4File(object):

    # -----------------------------------
    # | General wrapper methods         |
    # -----------------------------------

    def __init__(self, file):
        self.file = file

    def __eq__(self, other):
        if isinstance(other, P4File):
            return self.file == other.file
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.file)

    # -----------------------------------
    # | General methods                 |
    # -----------------------------------

    # Quick access to the connection for the class instances.
    @property
    def connection(self):
        return getConnection()

    # Returns a field of information from the file on Perforce.
    def getFileInfo(self, field):
        with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
            fileStats = self.connection.run("fstat", "-T", field, self.file)
            if isValidP4Output(fileStats):
                return fileStats[0][field]
            else:
                return None

    # Returns a field of information from the file's revision on Perforce.
    def getRevisionInfo(self, field, onlyLastRevision=True):
        with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
            if onlyLastRevision:
                fileStats = self.connection.run("filelog", "-l", "-m", 1, field, self.file)
            else:
                fileStats = self.connection.run("filelog", "-l", field, self.file)
            if isValidP4Output(fileStats):
                if onlyLastRevision:
                    return fileStats[0][field][0]
                else:
                    return fileStats[0][field]
            else:
                return None

    # -----------------------------------
    # | Local file methods              |
    # -----------------------------------

    # Wheter or not does the file exists locally.
    def doesLocalFileExist(self):
        return os.path.isfile(self.file)

    # Deletes the local file. If the force flag is set, deletes it even if it's read only.
    # NOTE: Be aware that doing this won't notify Perforce about the file's deletion, so it will still think it is locally downloaded.
    def deleteLocalFile(self, force=True):
        if self.doesLocalFileExist():
            if force:
                self.setLocalFileReadOnly(False)
            os.remove(self.file)

    # Creates an empty file with the specified path. If the flag force is set, replaces the existing one.
    def createLocalEmptyFile(self, force=True):
        if force or not self.doesLocalFileExist():
            folder = os.path.dirname(self.file)
            if not os.path.isdir(folder):
                os.makedirs(folder)
            open(self.file, "a").close()

    # Gets the file's read only state.
    def isLocalFileReadOnly(self):
        permissions = stat.S_IMODE(os.stat(self.file).st_mode)
        return (permissions & stat.S_IWUSR) == 0

    # Changes the file's read only state.
    def setLocalFileReadOnly(self, readOnly):
        permissions = stat.S_IMODE(os.stat(self.file).st_mode)
        if readOnly:
            permissions |= stat.S_IWUSR
        else:
            permissions &= ~stat.S_IWUSR
        os.chmod(self.file, 0o777 ^ permissions)

    # -----------------------------------
    # | Perforce file methods           |
    # -----------------------------------

    # Revision Methods ------------------
    
    # Checks if the file is under the perforce path.
    def isFileUnderPerforcePath(self):
        with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
            result = self.connection.run("info")[0]
            if "clientRoot" not in result:
                return False
            clientRoot = os.path.abspath(result["clientRoot"]).lower()
            absPath = os.path.abspath(self.file).lower()
            return absPath.startswith(clientRoot)

    # Checks if the file is in depot.
    def isFileInDepot(self):
        if self.isFileUnderPerforcePath():
            with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
                return self.connection.run("files", "-e", self.file) != []
        else:
            raise P4Exception("Error: Unable to check if file is in depot {} - File not under perforce path.".format(self.file))

    # Get the file's have revision.
    # A file not downloaded to workspace will return 0, while a non existing file in depot will raise an exception.
    def getFileRevision(self):
        with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
            fileStats = self.connection.run("fstat", "-T", "haveRev", self.file)
            if isValidP4Output(fileStats):
                fileStats = fileStats[0]
                if "haveRev" in fileStats:
                    return int(fileStats["haveRev"])
                else:
                    return 0    # File not on workspace
            else:
                raise P4Exception("Error: Unable to get revision for file {} - File not in depot.".format(self.file))

    # Checks if the file is up to date with the depot's head revision.
    # A file not downloaded to workspace will return False, while a non existing file in depot will raise an exception.
    def isFileLastRevision(self):
        with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
            fileStats = self.connection.run("fstat", "-T", "headRev,haveRev", self.file)
            if isValidP4Output(fileStats):
                fileStats = fileStats[0]
                if "haveRev" in fileStats:
                    return fileStats["headRev"] == fileStats["haveRev"]
                else:
                    return False    # File not on workspace
            else:
                raise P4Exception("Error: Unable to check latest revision for file {} - File not in depot.".format(self.file))

    # Downloads the latest revision of the file from depot.
    # As Perforce normally works, doing this will not override the current file if it's checked out.
    def syncFile(self):
        if self.isFileInDepot():
            with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
                self.connection.run("sync", self.file)
        else:
            # We use the isFileInDepot method to know if the file is in depot.
            # We cannot directly use the "sync" command to know that since it will also return a null output if the file is already updated.
            raise P4Exception("Error: Unable to sync file {} - File not in depot.".format(self.file))

    # Changelist Methods ----------------

    # Returns the changelist the file is checked out on.
    # If the file is not checked out, a None value will be returned.
    def getFileChangelist(self):
        return P4Changelist(self.getFileInfo("change"))

    # Moves the file to the specified changelist.
    # Raises an exception if the changelist is not valid or if the file is not checked out (NOTE: It won't chek out the file!).
    def setFileChangelist(self, changelist):
        if not self.isFileCheckedOut():
            raise P4Exception("Error: Unable to set the changelist for file {} - The file is not checked out.".format(self.file))

        if changelist == None:
            changelist = P4Changelist.getDefaultChangelist()

        if not changelist.isValidChangelist():
            raise P4Exception("Error: Unable to set the changelist for file {} - The provided changelist {} is not valid.".format(self.file, changelist.changelistNumber))

        with self.connection.connect():
            self.connection.run("reopen", "-c", changelist.changelistNumber, self.file)

    # When a file is marked for move, returns the name of the file before it was moved.
    def getFileNameBeforeMove(self):
        if self.isFileMarkedForMove(add=False, delete=True):
            return self.file
        elif self.isFileMarkedForMove(add=True, delete=False):
            return self.getFileInfo("movedFile")
        else:
            raise P4Exception("Error: Unable to get the file name befor being moved for file {} - The file is not marked for move.".format(self.file))
    
    # When a file is marked for move, returns the name of the file after it was moved.
    def getFileNameAfterMove(self):
        if self.isFileMarkedForMove(add=True, delete=False):
            return self.file
        elif self.isFileMarkedForMove(add=False, delete=True):
            return self.getFileInfo("movedFile")
        else:
            raise P4Exception("Error: Unable to get the file name befor being moved for file {} - The file is not marked for move.".format(self.file))
    
    # State Methods ---------------------

    # Wether or not a file is marked for move.
    # Used the "add" and "delete" flags to check for the specific move state of the file:
    # The "add" file (with the new name) and the "delete" file (with the old name)
    def isFileMarkedForMove(self, add=False, delete=False):
        return isActionMove(self.getFileInfo("action"), add=add, delete=delete)

    # Wether or not a file is marked for add.
    # Returns True also if the flag "includeMarkedForMove" is set and the file is marked for move.
    def isFileMarkedForAdd(self, includeMarkedForMove=True):
        return isActionAdd(self.getFileInfo("action"), includeMarkedForMove=includeMarkedForMove)

    # Wether or not a file is marked for delete.
    # Returns True also if the flag "includeMarkedForMove" is set and the file is marked for move.
    def isFileMarkedForDelete(self, includeMarkedForMove=True):
        return isActionDelete(self.getFileInfo("action"), includeMarkedForMove=includeMarkedForMove)

    # Wether or not a file is checked out.
    # Returns True also if the flag "includeMarkedForAdd" is set and the file is marked for add.
    # Returns True also if the flag "includeMarkForDelete" is set and the file is marked for delete.
    # Returns True also if the flag "includeMarkedForMove" is set and the file is marked for move.
    def isFileCheckedOut(self, includeMarkedForAdd=True, includeMarkForDelete=True, includeMarkedForMove=True):
        return isActionEdit(self.getFileInfo("action"), includeMarkedForAdd=includeMarkedForAdd, includeMarkForDelete=includeMarkForDelete, includeMarkedForMove=includeMarkedForMove)
    
    # Marks a file for add.
    # If a changelist is not provided, the action will be added to the default changelist.
    # If the file is already marked for add and the "moveChangelist" flag is set, the add action will be moved to the provided changelist.
    # NOTE: This method won't raise an exception if the file is already marked for add, but will raise one if the file is already in depot.
    def markFileForAdd(self, changelist=None, moveChangelist=False):
        if self.isFileInDepot():
            raise P4Exception("Error: Unable to mark file for add {} - File already in depot.".format(self.file))

        if self.isFileMarkedForAdd():
            if moveChangelist and changelist != None and changelist != self.getFileChangelist():
                self.setFileChangelist(changelist)
        else:
            if not self.doesLocalFileExist():
                raise P4Exception("Error: Unable to mark file for add {} - File does not exist.".format(self.file))

            if changelist == None:
                changelist = P4Changelist.getDefaultChangelist()

            if not changelist.isValidChangelist():
                raise P4Exception("Error: Unable to mark file for add {} - The provided changelist {} is not valid.".format(self.file, changelist.changelistNumber))

            #with self.connection.connect():
            #    self.connection.run("add", "-c", changelist.changelistNumber, self.file)
            
            # There is a bug with the "add" command on P4Python. It fails to set the correct file type when marking files for add.
            # In order to avoid it we directly use the command line to mark files for add.
            subprocess.Popen(["p4", "add", "-c", str(changelist.changelistNumber), self.file])

    # Marks a file for delete.
    # If a changelist is not provided, the action will be added to the default changelist.
    # If the file is already marked for delete and the "moveChangelist" flag is set, the delete action will be moved to the provided changelist.
    # If the file is not in depot and the "deleteLocalIfNotInDepot" flag is set, the local file will be deleted. If the flag is not set, an exception will be raised. 
    # NOTE: This method won't raise an exception if the file is already marked for delete, but will raise one if the file is already checked out.
    def markFileForDelete(self, changelist=None, moveChangelist=False, revertIfCheckedOut=True, deleteLocalIfNotInDepot=False):
        if self.isFileMarkedForAdd():
            if revertIfCheckedOut:
                self.revertFile()
                self.deleteLocalFile()
                return
            else:
                raise P4Exception("Error: Unable to mark file for delete {} - File is already marked for add.".format(self.file))
            
        if not self.isFileInDepot():
            if deleteLocalIfNotInDepot:
                self.deleteLocalFile()
                return
            else:
                raise P4Exception("Error: Unable to mark file for delete {} - File not in depot.".format(self.file))

        if self.isFileMarkedForDelete():
            if moveChangelist and changelist != None and changelist != self.getFileChangelist():
                self.setFileChangelist(changelist)
        else:
            if changelist == None:
                changelist = P4Changelist.getDefaultChangelist()

            if self.isFileCheckedOut():
                if revertIfCheckedOut:
                    self.revertFile()
                else:
                    raise P4Exception("Error: Unable to mark file for delete {} - File is already checked out.".format(self.file))

            if not changelist.isValidChangelist():
                raise P4Exception("Error: Unable to mark file for delete {} - The provided changelist {} is not valid.".format(self.file, changelist.changelistNumber))

            if not self.doesLocalFileExist():    # We need the file to exist locally in order to mark it for delete. It will be deleted again when the "delete" command is run.
                self.syncFile()
            with self.connection.connect():
                self.connection.run("delete", "-c", changelist.changelistNumber, self.file)

    # Renames a file, marking it for move.
    # This is a shortcut function to move files only changing their names (not their folders).
    def renameFile(self, newName, changelist=None, moveChangelist=False):
        path, file = os.path.split(self.file)
        newPath = os.path.join(path, newName)
        self.moveFile(newPath, changelist=changelist, moveChangelist=moveChangelist)
    
    # Moves a file to a new path, also renaming it.
    # Marked for delete files cannot be moved.
    def moveFile(self, newPath, changelist=None, moveChangelist=False):
        if self.isFileMarkedForDelete(includeMarkedForMove=False):
            raise P4Exception("Error: Unable to rename file {} - The provided file is already marked for delete.".format(self.file))

        if changelist == None:
            changelist = P4Changelist.getDefaultChangelist()
        
        if not self.isFileCheckedOut():
            self.checkoutFile(changelist=changelist, addIfNotInDepot=True)
        elif moveChangelist and changelist != None and changelist != self.getFileChangelist():
            self.setFileChangelist(changelist)
            
        if os.path.normpath(newPath) != os.path.normpath(self.file):
            other = P4File(newPath)
            if other.isFileInDepot():
                raise P4Exception("Error: Unable to rename file {} - The new name {} already exists on Depot.".format(self.file, newPath))
                
            with self.connection.connect():
                self.connection.run("rename", "-c", changelist.changelistNumber, self.file, newPath)
            
            self.file = newPath
    
    # Reverts a file.
    # Only checked out files, marked for add files and marked for delete files can be reverted.
    def revertFile(self, onlyUnchanged=False):
        if self.isFileCheckedOut():
            fileMarkedForMove = self.isFileMarkedForMove(add=True, delete=False)
            if fileMarkedForMove:
                oldFileName = self.getFileNameBeforeMove()
            
            with self.connection.connect():
                if onlyUnchanged:
                    self.connection.run("revert", self.file, "-a")
                else:
                    self.connection.run("revert", self.file)
                
            if fileMarkedForMove:
                self.file = oldFileName
                self.file = self.getFileInfo("clientFile")
        else:
            raise P4Exception("Error: Unable to revert file {} - File not checked out.".format(self.file))

    # Checks out a file.
    # If a changelist is not provided, the action will be added to the default changelist.
    # If the file is already checked out, marked for add or marked for delete and the "moveChangelist" flag is set, the action will be moved to the provided changelist.
    # If the "updateFileToLastRevision" flag is set, the lastest version of the file will be downloaded prior to it being checked out. Regardless of the flag, the file will also be updated if it wasn't downloaded at all.
    # If the file was not in depot and the "addIfNotInDepot" flag is set, the flag will be marked for add instead. If the flag is not set, an exception will be raised.
    def checkoutFile(self, changelist=None, moveChangelist=False, updateFileToLastRevision=False, addIfNotInDepot=False):
        if not self.isFileInDepot():
            if addIfNotInDepot:
                self.markFileForAdd(changelist=changelist, moveChangelist=moveChangelist)
                return
            else:
                raise P4Exception("Error: Unable to checkout file {} - File not in depot.".format(self.file))

        if self.isFileCheckedOut():
            if moveChangelist and changelist != None and changelist != self.getFileChangelist():
                self.setFileChangelist(changelist)
        else:
            if changelist == None:
                changelist = P4Changelist.getDefaultChangelist()

            if not changelist.isValidChangelist():
                raise P4Exception("Error: Unable to checkout file {} - The provided changelist {} is not valid.".format(self.file, changelist.changelistNumber))

            if updateFileToLastRevision or not self.doesLocalFileExist():    # We need the file to exist locally in order to checkout it.
                self.syncFile()

            with self.connection.connect():
                self.connection.run("edit", "-c", changelist.changelistNumber, self.file)

    # Checks out a file if it is on depot or marks it for add if it's not.
    # While marking for add, this methods will also create an empty file if it doesn't exist already. If it does exist, it will remove it's read only flag.
    def smartCheckout(self, changelist=None, moveChangelist=False, updateFileToLastRevision=False, keepEmptyFile=True):
        if self.isFileInDepot():
            if self.isFileMarkedForDelete():
                self.revertFile()
            self.checkoutFile(changelist=changelist, moveChangelist=moveChangelist, updateFileToLastRevision=updateFileToLastRevision)
        else:
            localFileExists = self.doesLocalFileExist()
            if localFileExists:
                self.setLocalFileReadOnly(False)
            else:
                self.createLocalEmptyFile()
            self.markFileForAdd(changelist=changelist, moveChangelist=moveChangelist)
            if not localFileExists and not keepEmptyFile:
                self.deleteLocalFile()


# -----------------------------------
# | P4Folder                        |
# -----------------------------------
# | Wraps a folder, allowing to     |
# | manage it easily on Perforce.   |
# -----------------------------------

class P4Folder(object):
    
    # -----------------------------------
    # | General wrapper methods         |
    # -----------------------------------

    def __init__(self, folder):
        self.folder = folder

    def __eq__(self, other):
        if isinstance(other, P4Folder):
            return self.folder == other.folder
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.folder)

    # -----------------------------------
    # | General methods                 |
    # -----------------------------------

    # Quick access to the connection for the class instances.
    @property
    def connection(self):
        return getConnection()

    # -----------------------------------
    # | Perforce folder methods         |
    # -----------------------------------
    
    # Revision Methods ------------------
    
    # Checks if the folder is under the perforce path.
    def isFolderUnderPerforcePath(self):
        with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
            result = self.connection.run("info")[0]
            if "clientRoot" not in result:
                return False
            clientRoot = os.path.abspath(result["clientRoot"]).lower()
            absPath = os.path.abspath(self.folder).lower()
            return absPath.startswith(clientRoot)
    
    # Checks if the folder is in depot.
    def isFolderInDepot(self):
        if self.isFolderUnderPerforcePath():
            with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
                return self.connection.run("dirs", self.folder) != []
        else:
            raise P4Exception("Error: Unable to check if folder is in depot {} - Folder not under perforce path.".format(self.folder))

    # Checks if the folder is up to date with the depot's head revision.
    # A folder is considered updated if all the files and subfolders it contains are updated.
    def isFolderLastRevision(self):
        if self.isFolderInDepot():
            with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
                return self.connection.run("sync", "-n", os.path.join(self.folder, "...")) == []
        else:
            raise P4Exception("Error: Unable to check latest revision for folder {} - Folder not in depot.".format(self.folder))

    # Get the folder's last changelist affecting one of it's files.
    def getFolderChangelist(self):
        if self.isFolderInDepot():
            with self.connection.at_exception_level(P4.RAISE_NONE), self.connection.connect():
                return self.connection.run("changes", "-l", "-m", 1, os.path.join(self.folder, "..."))[0]
        else:
            raise P4Exception("Error: Unable to get revision for folder {} - Folder not in depot.".format(self.folder))

    # Downloads the latest revision of all the files in the folder from depot.
    # As Perforce normally works, doing this will not override the current file if it's checked out.
    def syncFolder(self):
        if self.isFolderInDepot():
            with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
                self.connection.run("sync", os.path.join(self.folder, "..."))
        else:
            # We use the isFileInDepot method to know if the folder is in depot.
            # We cannot directly use the "sync" command to know that since it will also return a null output if the folder is already updated.
            raise P4Exception("Error: Unable to sync folder {} - Folder not in depot.".format(self.folder))

    # State Methods ---------------------

    # Wether or not some of the folder's files are checked out.
    def isFolderCheckedOut(self):
        if self.isFolderInDepot():
            with self.connection.at_exception_level(P4.RAISE_ERRORS), self.connection.connect():
                return self.connection.run("opened", os.path.join(self.folder, "...")) != []
        else:
            raise P4Exception("Error: Unable check folder {} - Folder not in depot.".format(self.folder))

    