import maya.cmds as cmds

import ActorManager
import ProjectPath

from mutils.animation import Animation
from mutils.selectionset import SelectionSet

import os

actor = ActorManager.getActors()[0]
subActor = actor.animSubActor
pathTokenizer = subActor.getPathTokenizer()
subPath = pathTokenizer.Translate(subActor.subActorPathToken)

sceneName = os.path.splitext(os.path.basename(cmds.file(q=True, sn=True)))[0]
studioLibraryPath = os.path.join(ProjectPath.get3DFolder(), subPath, "animations", "studiolibrary")
animPath = os.path.join(studioLibraryPath, "Animations", "{}.anim".format(sceneName))
selectionSetPath = os.path.join(studioLibraryPath, "SelectionSet.set", "set.json")

selectionSet = SelectionSet.fromPath(selectionSetPath)
objects = selectionSet.objects()
objects = [obj for obj in objects if cmds.objExists(obj)]

animation = Animation.fromObjects(objects)
animation.save(animPath, time=0, bakeConnected=False)