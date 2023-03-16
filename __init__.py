# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: __init__.py
-----------------------------------------------------------------------------
Loads the trigger module depending on the python version.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2/3
=============================================================================
"""
import sys

PYTHON2, PYTHON3 = 27, 37


def get_python_version():
    """
    Gets the python version.
    :return: Python version.
    :rtype: Str
    """
    python_version = int("%s%s" % (sys.version_info[0], sys.version_info[1]))
    return python_version


if get_python_version() == PYTHON2:
    from LaaScripts.Src.Python2 import trigger
elif get_python_version() == PYTHON3:
    from LaaScripts.Src.Python3 import trigger



