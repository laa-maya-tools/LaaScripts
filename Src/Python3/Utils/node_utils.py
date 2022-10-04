import maya.cmds as cmd
import maya.mel as mel

from LaaScripts.Src.Python3.Constants import constants as c
reload(c)


class SceneData(object):
    _nodes = {}

    @classmethod
    def create_node(cls, node_name, node_type='dagContainer'):
        nodes = node_name.split('|')

        for i, node in enumerate(nodes):
            if not cmd.objExists(node):
                if i == 0:
                    cmd.createNode(node_type, n=node, p=None)
                else:
                    cmd.createNode(node_type, n=node, p=nodes[i-1])

    @classmethod
    def delete_node(cls, node_name):
        if cmd.objExists(node_name):
            cmd.delete(node_name)

    @classmethod
    def add_attr(cls, node_name, attr_name, attr_type='string'):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        if not cmd.objExists(full_attr_name):
            cmd.addAttr(node_name, longName=attr_name, dataType=attr_type)

    @classmethod
    def delete_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        if cmd.objExists(full_attr_name):
            cmd.deleteAttr(n=node_name, attribute=attr_name)

    @classmethod
    def set_node_attr_value(cls, node_name, attr_name, attr_value, attr_type='string'):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        SceneData.unlock_node_attr(node_name, attr_name)
        cmd.setAttr(full_attr_name, attr_value, type=attr_type)
        SceneData.lock_node_attr(node_name, attr_name)

    @classmethod
    def lock_node_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        cmd.setAttr(full_attr_name, lock=True)

    @classmethod
    def unlock_node_attr(cls, node_name, attr_name):
        full_attr_name = '{0}.{1}'.format(node_name, attr_name)
        cmd.setAttr(full_attr_name, lock=False)


    # @classmethod
    # def get_scene_data(cls, node, attr):
    #     if not cmd.objExists(node):
    #         print '{0} does not exists.'.format(node)
    #
    #     full_attr_name = '{0}.{1}'.format(node_name, attr_name)
    #     if not cmd.objExists(full_attr_name):
    #                 return None
    #             full_attr_name = '{0}.{1}'.format(node_name, attr_name)
    #             return cmd.getAttr(full_attr_name)
    #
    # @classmethod
    # def set_scene_data(cls, node, attr):
    #     if not cmd.objExists(node):
    #         print 'node'
    #
    # @classmethod
    # def get_node_attr_value(cls, node, attr):
    #     if not cmd.objExists(node):
    #         print 'node'
    #     # return None
    #     # return cmd.getAttr('{0}.{1}'.format(node, attr))
    #     # if not cmd.objExists(full_attr_name):
    #     #     return None
    #     # full_attr_name = '{0}.{1}'.format(node, attr)
    #     # return cmd.getAttr(full_attr_name)
    #
    #
    # @classmethod
    # def get_node_attr(cls, node, attr, default_value=''):
    #     return cls._nodes.setdefault(node, {attr: default_value})
    #
    # @classmethod
    # def set_node_attr(cls, node, attr, value):
    #     cls._nodes[node] = {attr: value}
#
#     @classmethod
#     def load_scene_data(cls, key):
#         data = {}
#         stored_data = cmd.fileInfo(key, q=True)
#         if stored_data:
#             data = json.loads(stored_data[0].replace('\\"', '"'))
#         return data
#
#     @classmethod
#     def store_scene_data(cls, key, value):
#         encoded_data = json.dumps(value)
#         cmd.fileInfo(key, encoded_data)
#



#
#     @classmethod
#     def add_node_attr(cls, node_name, attr_name):
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         if not cmd.objExists(full_attr_name):
#             cmd.addAttr(node_name, longName=attr_name, dataType='string')
#
#     @classmethod
#     def get_node_attr_value(cls, node_name, attr_name):
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         if not cmd.objExists(full_attr_name):
#             return None
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         return cmd.getAttr(full_attr_name)
#
#     @classmethod
#     def set_node_attr_value(cls, node_name, attr_name, attr_value):
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         if not cmd.objExists(full_attr_name):
#             return None
#         SceneData.unlock_node_attr(node_name, attr_name)
#         cmd.setAttr(full_attr_name, attr_value, type='string')
#         SceneData.lock_node_attr(node_name, attr_name)
#
#     @classmethod
#     def lock_node_attr(cls, node_name, attr_name):
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         cmd.setAttr(full_attr_name, lock=True)
#
#     @classmethod
#     def unlock_node_attr(cls, node_name, attr_name):
#         full_attr_name = '{0}.{1}'.format(node_name, attr_name)
#         cmd.setAttr(full_attr_name, lock=False)
#
if __name__ == "__main__":
    # SceneData.create_node('LaaScripts2', 'LaaScripts')
    # SceneData.create_node('LaaScripts|Playback2|FrameMarker3')
    # SceneData.add_attr('LaaScripts|Playback2', 'test2')
    SceneData.delete_attr('LaaScripts|Playback2', 'test2')
    SceneData.delete_node('LaaScripts|Viewport')
    SceneData.set_node_attr_value('LaaScripts', 'test', 'Fix2')
    # SceneData.create_node('LaaScripts')
    # # SceneData.create_node('FrameMarkers', 'LaaScripts')
    # SceneData.add_node_attr('LaaScripts', 'info')
    # SceneData.set_node_attr_value('LaaScripts', 'info', 'LassScripts v0.0.1')
    # # print SceneData.get_node_attr_value('LaaScripts', 'info')
    # # SceneData.lock_node_attr('LaaScripts', 'info')
    # SceneData.lock_node_attr('LaaScripts', 'info')
    # print SceneData.get_node_attr_value('LaaScripts', 'info')

    # mel.eval('setAttr -l false "LaaScripts.info";')

    # SceneData.set_node_attr(c.LAA_SCRIPTS_NODE, c.VERSION_ATTR, 'test')
    # print SceneData.get_node_attr(c.LAA_SCRIPTS_NODE, c.VERSION_ATTR)


    # print SceneData.get_node_attr('LaaScripts', 'version')
    # SceneData.set_node_attr('LaaScripts', 'version', '1.0.2')
    # print SceneData.get_node_attr('LaaScripts', 'version')



