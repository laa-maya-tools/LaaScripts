
def lock_hide_attrs(self, obj, lock=True, hide=True):
    print obj

    attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']

    for attr in attrs:
        cmds.setAttr(obj + attr, l=lock, k=hide)

def lock_hide_attr (self, obj, attr, lock=True, display=False):

    if cmds.attributeQuery(attr, node=obj, exists=True):
        cmds.setAttr(obj + '.' + attr, l=lock, k=display, cb=display)


def lock_hide_all_attrs (self, obj, lock=True, display=False):

    obj_shape = obj + 'Shape'

    # Lock/Hide All Attributes of obj
    all_attrs = cmds.listAttr(obj, se=True, sn=True)
    for attr in all_attrs:
        if cmds.attributeQuery(attr, node=obj, exists=True):
            cmds.setAttr(obj + '.' + attr, l=lock, k=display, cb=display)

    # Lock/Hide All Attributes of obj_shape
    all_attrs = cmds.listAttr(obj_shape, se=True, sn=True)
    for attr in all_attrs:
        if cmds.attributeQuery(attr, node=obj_shape, exists=True):
            cmds.setAttr(obj_shape + '.' + attr, l=lock, k=display, cb=display)


    def break_connection (self, obj, attr):

        connection = obj + attr
        print connection

        inputs = cmds.listConnections(connection, s=True, d=False, p=True)
        if inputs:
            input = inputs[0]
            cmds.disconnectAttr(input, connection)

    def get_attr_name(self, fullname):

        attr_name = fullname.split('.')[-1]
        return attr_name