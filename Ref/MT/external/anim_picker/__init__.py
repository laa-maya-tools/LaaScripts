from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from . import gui
from . import version

__version__ = version.__version__

import shiboken2

# =============================================================================
# Load user interface function
# =============================================================================

instance = None

def load(edit=False, dockable=False, unique=True, *args, **kwargs):
    global instance
    if unique and instance and shiboken2.isValid(instance) and instance.isVisible():
        instance.close()
    
    instance = gui.load(edit=edit, dockable=dockable)
    
    return instance
