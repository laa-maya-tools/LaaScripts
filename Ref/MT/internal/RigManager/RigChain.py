# -*- coding: utf-8 -*-
from NodeManager import NodeWrapper

class RigChain(NodeWrapper.NodeWrapper):
    
    _rig = "rig"
    
    def __init__(self, node=None):
        super(RigChain, self).__init__(node)
    
    # Methods ---------------
    
    def getRig(self):
        import RigManager.Rig as Rig
        return self.getInputSingle(self._rig, cls=Rig.Rig)
    
    def getControls(self):
        raise NotImplementedError()
