from PySide2 import QtWidgets, QtCore

class Completer(QtWidgets.QCompleter):
    def __init__(self, *args, **kwargs):
        super(Completer, self).__init__(*args, **kwargs)
        
        self.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.setWrapAround(False)
    
    # Add texts instead of replace
    def pathFromIndex(self, index):
        path = QtWidgets.QCompleter.pathFromIndex(self, index)
        lst = str(self.widget().text()).split('{')
        if len(lst) > 1:
            for x in range(1,len(lst)):
                lst[x] = '{' + lst[x]
            path = '%s{%s}' % (''.join(lst[:-1]), path)
        return path
    
    def splitPath(self, path):
        path = str(path.split('{')[-1]).lstrip(' ')
        return [path]