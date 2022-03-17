import maya.cmds as cmd
import maya.mel as mel
import json


class SceneData(object):

    @classmethod
    def load_scene_data(cls, key):
        data = {}
        stored_data = cmd.fileInfo(key, q=True)
        if stored_data:
            data = json.loads(stored_data[0].replace('\\"', '"'))
        return data

    @classmethod
    def store_scene_data(cls, key, value):
        encoded_data = json.dumps(value)
        cmd.fileInfo(key, encoded_data)

    @classmethod
    def create_node(cls, node_name, node_parent=None, node_type='dagContainer'):
        if not cmd.objExists(node_name):
            cmd.createNode(node_type, n=node_name, p=node_parent)

    @classmethod
    def add_node_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        if not cmd.objExists(full_attr_name):
            cmd.addAttr(node_name, longName=attr_name, dataType='string')

    @classmethod
    def get_node_attr_value(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        if not cmd.objExists(full_attr_name):
            return None
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        return cmd.getAttr(full_attr_name)

    @classmethod
    def set_node_attr_value(cls, node_name, attr_name, attr_value):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        if not cmd.objExists(full_attr_name):
            return None
        SceneData.unlock_node_attr(node_name, attr_name)
        cmd.setAttr(full_attr_name, attr_value, type='string')
        SceneData.lock_node_attr(node_name, attr_name)

    @classmethod
    def lock_node_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        cmd.setAttr(full_attr_name, lock=True)

    @classmethod
    def unlock_node_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        cmd.setAttr(full_attr_name, lock=False)


if __name__ == "__main__":
    SceneData.create_node('LaaScripts')
    # SceneData.create_node('FrameMarkers', 'LaaScripts')
    SceneData.add_node_attr('LaaScripts', 'info')
    SceneData.set_node_attr_value('LaaScripts', 'info', 'LassScripts v0.0.1')
    # print SceneData.get_node_attr_value('LaaScripts', 'info')
    # SceneData.lock_node_attr('LaaScripts', 'info')
    SceneData.lock_node_attr('LaaScripts', 'info')
    print SceneData.get_node_attr_value('LaaScripts', 'info')

    # mel.eval('setAttr -l false "LaaScripts.info";')



