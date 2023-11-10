import mgear
import maya.cmds as cmds
import mgear.core.anim_utils as anu
from mgear.core import transform


def ikFkMatch_with_namespace(namespace,
                             ikfk_attr,
                             ui_host,
                             fks,
                             ik,
                             upv,
                             ik_rot=None,
                             key=None,
                             toggleAttr=True):
    """Switch IK/FK with matching functionality

    This function is meant to work with 2 joint limbs.
    i.e: human legs or arms

    Args:
        namespace (str): Rig name space
        ikfk_attr (str): Blend ik fk attribute name
        ui_host (str): Ui host name
        fks ([str]): List of fk controls names
        ik (str): Ik control name
        upv (str): Up vector control name
        ikRot (None, str): optional. Name of the Ik Rotation control
        key (None, bool): optional. Whether we do an snap with animation
    """

    # returns a pymel node on the given name
    def _get_node(name):
        # type: (str) -> pm.nodetypes.Transform
        name = anu.stripNamespace(name)
        if namespace:
            node = anu.getNode(":".join([namespace, name]))
        else:
            node = anu.getNode(name)

        if not node:
            mgear.log("Can't find object : {0}".format(name), mgear.sev_error)

        return node

    # returns matching node
    def _get_mth(name):
        # type: (str) -> pm.nodetypes.Transform
        tmp = name.split("_")
        tmp[-1] = "mth"
        return _get_node("_".join(tmp))

    # get things ready
    fk_ctrls = [_get_node(x) for x in fks]
    fk_targets = [_get_mth(x) for x in fks]
    ik_ctrl = _get_node(ik)
    ik_target = _get_mth(ik)
    upv_ctrl = _get_node(upv)

    if ik_rot:
        ik_rot_node = _get_node(ik_rot)
        ik_rot_target = _get_mth(ik_rot)

    ui_node = _get_node(ui_host)
    o_attr = ui_node.attr(ikfk_attr)
    val = o_attr.get()

    # sets keyframes before snapping
    if key:
        _all_controls = []
        _all_controls.extend(fk_ctrls)
        _all_controls.extend([ik_ctrl, upv_ctrl, ui_node])
        if ik_rot:
            _all_controls.extend([ik_rot_node])
        [cmds.setKeyframe("{}".format(elem),
                          time=(cmds.currentTime(query=True) - 1.0))
         for elem in _all_controls]

    # if is IKw then snap FK
    if val == 1.0:

        for target, ctl in zip(fk_targets, fk_ctrls):
            transform.matchWorldTransform(target, ctl)
        
        
        '''#If it is a leg, then set the foot tip as the ik roll
        nme = fks[0]
        if (nme.find('leg') >= 0):
            footTipName = nme.replace('leg', 'foot')
            idx = nme.index('_fk')
            footTipName = footTipName[:idx+4] + '0' + footTipName[idx+5:]
            
            footTipNode = _get_node(footTipName)
            rollCtlNode = _get_node(footTipName.replace('fk0', 'roll'))
            
            print(footTipName)
            print(rollCtlNode)
            
            rollZAttr = rollCtlNode.attr('rotateZ')
            rollZVal = rollZAttr.get()
            rollZAttr.set(0)
            footTipZRotAttr = footTipNode.attr('rotateZ')
            footTipZRotAttr.set(-rollZVal)'''
            
        
        if (toggleAttr):
            o_attr.set(0.0)

    # if is FKw then sanp IK
    elif val == 0.0:
        transform.matchWorldTransform(ik_target, ik_ctrl)
        if ik_rot:
            transform.matchWorldTransform(ik_rot_target, ik_rot_node)

        transform.matchWorldTransform(fk_targets[1], upv_ctrl)
        # calculates new pole vector position
        start_end = (fk_targets[-1].getTranslation(space="world") -
                     fk_targets[0].getTranslation(space="world"))
        start_mid = (fk_targets[1].getTranslation(space="world") -
                     fk_targets[0].getTranslation(space="world"))

        dot_p = start_mid * start_end
        proj = float(dot_p) / float(start_end.length())
        proj_vector = start_end.normal() * proj
        arrow_vector = start_mid - proj_vector
        arrow_vector *= start_end.normal().length()
        final_vector = (arrow_vector +
                        fk_targets[1].getTranslation(space="world"))
        upv_ctrl.setTranslation(final_vector, space="world")

        # sets blend attribute new value
        if (toggleAttr):
            o_attr.set(1.0)
        roll_att = ui_node.attr(ikfk_attr.replace("blend", "roll"))
        roll_att.set(0.0)

    # sets keyframes
    if key:
        [cmds.setKeyframe("{}".format(elem),
                          time=(cmds.currentTime(query=True)))
         for elem in _all_controls]


def ikFkMatch(model, ikfk_attr, ui_host, fks, ik, upv, ik_rot=None, key=None):
    """Switch IK/FK with matching functionality

    This function is meant to work with 2 joint limbs.
    i.e: human legs or arms

    Args:
        model (PyNode): Rig top transform node
        ikfk_attr (str): Blend ik fk attribute name
        ui_host (str): Ui host name
        fks ([str]): List of fk controls names
        ik (str): Ik control name
        upv (str): Up vector control name
        ikRot (None, str): optional. Name of the Ik Rotation control
        key (None, bool): optional. Whether we do an snap with animation
    """
    # gets namespace
    current_namespace = anu.getNamespace(model)

    ikFkMatch_with_namespace(current_namespace,
                             ikfk_attr,
                             ui_host,
                             fks,
                             ik,
                             upv,
                             ik_rot=ik_rot,
                             key=key)


def fkMatchIk(model, ikfk_attr, ui_host, fks, ik, upv, ik_rot=None, key=None):
    current_namespace = anu.getNamespace(model)
    ikFkMatch_with_namespace(current_namespace,
                             ikfk_attr,
                             ui_host,
                             fks,
                             ik,
                             upv,
                             ik_rot=ik_rot,
                             key=key,
                             toggleAttr=False)


def ikMatchFk(model, ikfk_attr, ui_host, fks, ik, upv, ik_rot=None, key=None):
    current_namespace = anu.getNamespace(model)
    ikFkMatch_with_namespace(current_namespace,
                             ikfk_attr,
                             ui_host,
                             fks,
                             ik,
                             upv,
                             ik_rot=ik_rot,
                             key=key,
                             toggleAttr=False)

def ikFkMatchSelection(selection=None):
    if selection == None:
        selection = cmds.ls(selection=True) or []
    
    selectedLimbs = {}
    for selectedNode in selection:        
        namespaceSplit = selectedNode.split(":")
        namespace = ":".join(namespaceSplit[:-1])
        nodeName = namespaceSplit[-1]
        if len(nodeName) < 5:   # Necessary: 3 characters for the limb, a _ symbol and L/R for the side
            continue
        
        limb = nodeName[:3]
        if limb != "arm" and limb != "leg":
            continue
        
        limbSplit = nodeName.split("_")
        if len(limbSplit) < 2:  # The first element should be the limb, the second contains the side (L or R followed by a number, picks the first character)
            continue
        side = limbSplit[1][0]
        if side != "L" and side != "R":
            continue
        
        if (limb, side) in selectedLimbs:
            continue
            
        switchAttribute = "{}_blend".format(limb)
        switchControl = "{}:{}UI_{}0_ctl".format(namespace, limb, side)
        ikControl = "{}:{}_{}0_ik_ctl".format(namespace, limb, side)
        ikUpVectorControl = "{}:{}_{}0_upv_ctl".format(namespace, limb, side)
        fkControls = ["{}:{}_{}0_fk{}_ctl".format(namespace, limb, side, i) for i in range(3)]
        
        selectedLimbs[(limb, side)] = (selectedNode, switchAttribute, switchControl, fkControls, ikControl, ikUpVectorControl)
    
    for limb in selectedLimbs.values():
        ikFkMatch(limb[0], limb[1], limb[2], limb[3], limb[4], limb[5])


if (__name__ == "__main__"):
    #NameSpace
    namesp = "Samus:"

    #Body Part:
    #bodyPart = 'arm'
    bodyPart = 'leg'

    #Side:
    side = 'R' #-Right Arm
    #side = 'L' #-Left Arm

    #Nodes:
    character_root = "{}rig".format(namesp)
    switch_control = "{}{}UI_{}0_ctl".format(namesp, bodyPart, side)
    switch_attribute = "{}_blend".format(bodyPart)
    ik_control = "{}{}_{}0_ik_ctl".format(namesp, bodyPart, side)
    ik_upvector_control = "{}{}_{}0_upv_ctl".format(namesp, bodyPart, side)
    fk_controls = ("{}{}_{}0_fk0_ctl".format(namesp, bodyPart, side),
                    "{}{}_{}0_fk1_ctl".format(namesp, bodyPart, side),
                    "{}{}_{}0_fk2_ctl".format(namesp, bodyPart, side))

    #IKFK Match:
    ikMatchFk(character_root, switch_attribute, switch_control, fk_controls, ik_control, ik_upvector_control)