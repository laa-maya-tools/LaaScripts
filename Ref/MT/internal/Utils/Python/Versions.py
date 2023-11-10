import sys

long = long if int(sys.version[0]) <= 2 else int

basestring = basestring if int(sys.version[0]) <= 2 else str