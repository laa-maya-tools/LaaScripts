import maya.cmds as cmds

import P4.Tools as P4Tools

import os


IGNORED_FILES = "AUTO_UPDATE_IGNORED_FILES"
IGNORED_FILES_VERSIONS = "AUTO_UPDATE_IGNORED_FILES_VERSIONS"

def isFileUpToDate(file):
    p4File = P4Tools.P4File(file)
    if p4File.isFileUnderPerforcePath() and p4File.isFileInDepot():
        return p4File.isFileLastRevision()
    else:
        return True # The file is not in Perforce, return True since it doesn't need update
    
def isFolderUpToDate(folder):
    p4Folder = P4Tools.P4Folder(folder)
    if p4Folder.isFolderUnderPerforcePath() and p4Folder.isFolderInDepot():
        return p4Folder.isFolderLastRevision()
    else:
        return True # The file is not in Perforce, return True since it doesn't need update
    
def getFileRevisionDescription(file):
    p4File = P4Tools.P4File(file)
    revisionNumber = p4File.getRevisionInfo("rev")
    revisionUser = p4File.getRevisionInfo("user")
    revisionDescription = p4File.getRevisionInfo("desc")
    return "{} - [{}] {}".format(revisionNumber, revisionUser, revisionDescription)

def getFolderRevisionDescription(folder):
    p4Folder = P4Tools.P4Folder(folder)
    changelistInfo = p4Folder.getFolderChangelist()
    revisionNumber = changelistInfo["change"]
    revisionUser = changelistInfo["user"]
    revisionDescription = changelistInfo["desc"]
    return "{} - [{}] {}".format(revisionNumber, revisionUser, revisionDescription)

def saveIgnoredFileVersions(ignoredFiles, ignoredFilesVersions):
    if len(ignoredFiles) != len(ignoredFilesVersions):
        raise AssertionError("Lists of files and versions to ignore don't have the same length! ({} != {})".format(len(ignoredFiles), len(ignoredFilesVersions)))
    
    cmds.optionVar(ca=IGNORED_FILES)
    for ignoredFile in ignoredFiles:
        cmds.optionVar(sva=(IGNORED_FILES, ignoredFile))
    cmds.optionVar(ca=IGNORED_FILES_VERSIONS)
    for ignoredFileVersion in ignoredFilesVersions:
        cmds.optionVar(iva=(IGNORED_FILES_VERSIONS, ignoredFileVersion))

def clearIgnoredFileVersions():
    cmds.optionVar(ca=IGNORED_FILES)
    cmds.optionVar(ca=IGNORED_FILES_VERSIONS)

def isFileVersionIgnored(file):
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES)
    if ignoredFiles and file in ignoredFiles:
        p4File = P4Tools.P4File(file)
        revision = int(p4File.getRevisionInfo("rev", onlyLastRevision=True))
        return revision <= cmds.optionVar(q=IGNORED_FILES_VERSIONS)[ignoredFiles.index(file)]
    return False

def isFolderVersionIgnored(folder):
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES)
    if ignoredFiles and folder in ignoredFiles:
        p4Folder = P4Tools.P4Folder(folder)
        revision = int(p4Folder.getFolderChangelist()["change"])
        return revision <= cmds.optionVar(q=IGNORED_FILES_VERSIONS)[ignoredFiles.index(folder)]
    return False

def ignoreFileVersion(file):
    p4File = P4Tools.P4File(file)
    versionToIgnore = int(p4File.getRevisionInfo("rev", onlyLastRevision=True))
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES) or []
    ignoredFilesVersions = cmds.optionVar(q=IGNORED_FILES_VERSIONS) or []
    if file in ignoredFiles:
        index = ignoredFiles.index(file)
        ignoredFilesVersions[index] = versionToIgnore
    else:
        ignoredFiles.append(file)
        ignoredFilesVersions.append(versionToIgnore)
    saveIgnoredFileVersions(ignoredFiles, ignoredFilesVersions)

def ignoreFolderVersion(folder):
    p4Folder = P4Tools.P4Folder(folder)
    versionToIgnore = int(p4Folder.getFolderChangelist()["change"])
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES) or []
    ignoredFilesVersions = cmds.optionVar(q=IGNORED_FILES_VERSIONS) or []
    if folder in ignoredFiles:
        index = ignoredFiles.index(folder)
        ignoredFilesVersions[index] = versionToIgnore
    else:
        ignoredFiles.append(folder)
        ignoredFilesVersions.append(versionToIgnore)
    saveIgnoredFileVersions(ignoredFiles, ignoredFilesVersions)

def updateFile(file):
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES)
    if ignoredFiles and file in ignoredFiles:
        ignoredFilesVersions = cmds.optionVar(q=IGNORED_FILES_VERSIONS)
        index = ignoredFiles.index(file)
        ignoredFiles.pop(index)
        ignoredFilesVersions.pop(index)
        
        saveIgnoredFileVersions(ignoredFiles, ignoredFilesVersions)
    
    p4File = P4Tools.P4File(file)
    p4File.syncFile()
    if p4File.isFileCheckedOut():
        cmds.warning("File has been synced but it was checked out, please resolve any conflicts.")
    else:
        references = cmds.ls(type="reference")
        for reference in references:
            try:
                if file == cmds.referenceQuery(reference, filename=True, withoutCopyNumber=True):
                    cmds.file(loadReference=reference)
            except:
                cmds.warning("Reference node is not associated with a reference file: {}".format(reference))

def updateFolder(folder):
    ignoredFiles = cmds.optionVar(q=IGNORED_FILES)
    if ignoredFiles and folder in ignoredFiles:
        ignoredFilesVersions = cmds.optionVar(q=IGNORED_FILES_VERSIONS)
        index = ignoredFiles.index(folder)
        ignoredFiles.pop(index)
        ignoredFilesVersions.pop(index)
        
        saveIgnoredFileVersions(ignoredFiles, ignoredFilesVersions)
    
    p4Folder = P4Tools.P4Folder(folder)
    p4Folder.syncFolder()
    if p4Folder.isFolderCheckedOut():
        cmds.warning("Folder has been synced but some of it's file were checked out, please resolve any conflicts.")
    else:
        references = cmds.ls(type="reference")
        for reference in references:
            try:
                if os.path.normpath(cmds.referenceQuery(reference, filename=True, withoutCopyNumber=True)).lower().startswith(os.path.normpath(folder.lower())):
                    cmds.file(loadReference=reference)
            except:
                cmds.warning("Reference node is not associated with a reference file: {}".format(reference))
