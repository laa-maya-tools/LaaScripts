import os
import sys

_third_party = os.path.join(os.path.dirname(__file__), 'third_party', 'python')
if _third_party not in sys.path:
    sys.path.insert(0, _third_party)
