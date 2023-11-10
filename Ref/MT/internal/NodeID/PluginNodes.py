
class PluginNode(object):
    @property
    def nodeName(self):
        raise NotImplementedError

    @property
    def nodeID(self):
        raise NotImplementedError

    @staticmethod
    def creator():
        raise NotImplementedError
    @staticmethod
    def initializer():
        raise NotImplementedError


import sys

def registerNodes(mplugin, nodeList):
    for node in nodeList:
        try:
            mplugin.registerNode(node.nodeName, node.nodeID, node.creator, node.initializer)
        except Exception:    
            sys.stderr.write("Failed to register node: " + node.nodeName)
            raise

# uninitialize the script plug-in
def unregisterNodes(mplugin, nodeList):
    for node in nodeList:
        try:
            mplugin.deregisterNode(node.nodeID)
        except Exception:
            sys.stderr.write("Failed to unregister node: " + node.nodeName)    
            raise