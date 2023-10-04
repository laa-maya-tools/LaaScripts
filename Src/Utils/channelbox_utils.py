"""
=============================================================================
MODULE: graph_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to manipulate the animation
curves.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel


class ChannelboxUtils(object):

    @staticmethod
    def lock_hide_attrs(obj, lock=True, hide=True):
        print(obj)

        attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']

        for attr in attrs:
            cmd.setAttr(obj + attr, l=lock, k=hide)

    @staticmethod
    def lock_hide_attr(obj, attr, lock=True, display=False):

        if cmd.attributeQuery(attr, node=obj, exists=True):
            cmd.setAttr(obj + '.' + attr, l=lock, k=display, cb=display)

    @staticmethod
    def lock_hide_all_attrs(obj, lock=True, display=False):

        obj_shape = obj + 'Shape'

        # Lock/Hide All Attributes of obj
        all_attrs = cmd.listAttr(obj, se=True, sn=True)
        for attr in all_attrs:
            if cmd.attributeQuery(attr, node=obj, exists=True):
                cmd.setAttr(obj + '.' + attr, l=lock, k=display, cb=display)

        # Lock/Hide All Attributes of obj_shape
        all_attrs = cmd.listAttr(obj_shape, se=True, sn=True)
        for attr in all_attrs:
            if cmd.attributeQuery(attr, node=obj_shape, exists=True):
                cmd.setAttr(obj_shape + '.' + attr, l=lock, k=display, cb=display)

    @staticmethod
    def break_connection(obj, attr):

        connection = obj + attr
        print(connection)

        inputs = cmd.listConnections(connection, s=True, d=False, p=True)
        if inputs:
            input = inputs[0]
            cmd.disconnectAttr(input, connection)

    def get_attr_name(self, fullname):

        attr_name = fullname.split('.')[-1]
        return attr_name
