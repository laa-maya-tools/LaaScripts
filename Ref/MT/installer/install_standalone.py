import os
import sys

# Standalone Maya Inicialization
print("Initializing Maya...")
import maya.standalone
maya.standalone.initialize(name='python')

# Runs the installation
print("Installing Plugins...")
import install
perforcePath = sys.argv[1]
fileDirectory = os.path.dirname(__file__)
install.install(fileDirectory, p4RootPath=perforcePath)

# Exits Maya
print("Exiting Maya...")
sys.exit(0)