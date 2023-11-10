# coding: utf8

#-----------------------
#|     USER SETUP      |
#-----------------------
# Delegates the initialization of the program to a file in Perforce, shared by everyone.
# Since this script will be local to each user, making it difficult to edit, it contains minimal functionalty.
# NOTE: The name of this file must be "userSetup.py", since it's the file Maya will run when booting.

# Imports
import sys
import os

import maya.cmds as cmds

# Registers the path to the startup modules.
sys.path.append(os.path.join(os.environ["P4_ROOT_FOLDER"], "GAME/Tools/MayaTools/startup"))  # TODO: Actualizar si se cambia la ubicación del código de Maya

def initialize():
    import MseInit   # We load this module late becouse we needed the path for the startup modules to be set first
    MseInit.init()

# We continue the initialization with Execute Deferred to allow Maya to load before doing any more changes
cmds.evalDeferred(initialize)