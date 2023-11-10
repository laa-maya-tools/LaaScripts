#-----------------------
#|      MSE INIT       |
#-----------------------
# Initializes the modules on the startup folder.
# The order in which they are loaded is relevant since they may depend on each other.

import logging
import traceback

import maya.cmds as cmds

def init():
  # On batch mode, some modules won't need to be opened
  batch = cmds.about(batch=True)
  
  # Note: Modules' initializations are surrounded by a try/catch clause so an error on one of them will not prevent the other ones from loading.

  # Configures the environment variables so the other modules can use them
  try:
    import ConfigureEnv
    ConfigureEnv.init()
  except:
    traceback.print_exc()
    logging.error("An error occurred while initializing Environment Variables, see the log for more information.")

  # Opens the necessary command ports for external applications to send code into Maya
  if not batch:
    try:
      import OpenCommandPort
      OpenCommandPort.init()
    except:
      traceback.print_exc()
      logging.error("An error occurred while initializing Command Ports, see the log for more information.")

  # Loads the commands for the custom tools
  if not batch:
    try:
      import CustomCommands
      CustomCommands.init()
    except:
      traceback.print_exc()
      logging.error("An error occurred while initializing Custom Commands, see the log for more information.")

  # Loads the P4 Extra tools
  try:
    import P4.Extra
    P4.Extra.init()
  except:
    traceback.print_exc()
    logging.error("An error occurred while initializing P4 Extra Tools, see the log for more information.")
  
  # Loads Auto-Update system
  if not batch:
    try:
      import AutoUpdate
      AutoUpdate.init()
    except:
      traceback.print_exc()
      logging.error("An error occurred while initializing Auto-Updater, see the log for more information.")

  # Starts the Nintendo Tools
  try:
    import NintendoStartup
    NintendoStartup.init()
  except:
    traceback.print_exc()
    logging.error("An error occurred while initializing Nintendo Startup, see the log for more information.")

  # Loads the custom menus
  if not batch:
    try:
      import CustomMenu
      CustomMenu.init()
    except:
      traceback.print_exc()
      logging.error("An error occurred while initializing Custom Menus, see the log for more information.")
