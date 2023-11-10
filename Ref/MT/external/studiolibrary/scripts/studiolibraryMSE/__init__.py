import ActorManager

import studiolibrary

import maya.cmds as cmds

import os
import collections

sceneOpenedScriptJob = None

def getActorLibraryPaths(actors):
    libraryPaths = {}
    for actor in actors:
        animSubActor = actor.animSubActor
        animPath = animSubActor.getPathTokenizer(branch="{3D}").Translate(animSubActor.animPath)
        libraryPaths[actor.name] = studiolibrary.normPath(os.path.join(animPath, "studiolibrary"))
    return libraryPaths

def getLocalLibraryPath():
    return studiolibrary.normPath(os.path.join(os.environ["MAYA_APP_DIR"], "studiolibrary"))

def getLibraryPaths(addSceneLibraries=True, addLocalLibrary=True):
    libraryPaths = collections.OrderedDict()
    if addSceneLibraries:
        actorLibraryPaths = getActorLibraryPaths(ActorManager.getActors())
        for path in actorLibraryPaths.values():
            if not os.path.exists(path):
                os.makedirs(path)
        libraryPaths.update(actorLibraryPaths)
    if addLocalLibrary:
        localLibraryPath = getLocalLibraryPath()
        if not os.path.exists(localLibraryPath):
            os.makedirs(localLibraryPath)
        libraryPaths["Local"] = localLibraryPath
    return libraryPaths

def open(addSceneLibraries=True, addLocalLibrary=True):
    libraryWindow = onSceneOpened(show=True, addSceneLibraries=addSceneLibraries, addLocalLibrary=addLocalLibrary)
    
    cmds.scriptJob(e=("SceneOpened", onSceneOpened), parent=libraryWindow.objectName(), replacePrevious=True)
    
def onSceneOpened(show=False, addSceneLibraries=True, addLocalLibrary=True):
    libraryPaths = getLibraryPaths(addSceneLibraries=addSceneLibraries, addLocalLibrary=addLocalLibrary)
    libraryWindow = studiolibrary.main(paths=libraryPaths, show=show)
    libraryWindow.sync()
    return libraryWindow
