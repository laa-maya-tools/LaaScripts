"""
=============================================================================
MODULE: timeline_utils.py
-----------------------------------------------------------------------------
This class contains a tone of helper methods to get/set timeline keyframing
data.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2017+ | Python 2.7
=============================================================================
"""
import maya.cmds as cmd
import maya.mel as mel

from .widget_utils import WidgetUtils
from ..Constants import constants as c
reload(c)


class LayersUtils(object):

    @staticmethod
    def create_new_anim_layer(layer):
        try:
            layer_name = cmd.animLayer(layer, mute=False, solo=False, override=True, passthrough=False, lock=False)
            return layer_name
        except:
            cmd.warning('Could not create {0} layer'.format(layer))

    @staticmethod
    def delete_selected_anim_layers():
        if not KeyframingUtils.any_user_layer_exists():
            return
        selected_layers = KeyframingUtils.get_selected_anim_layers()
        for layer in selected_layers:
            cmd.delete(layer)

    @staticmethod
    def set_active_anim_layer(layer):
        all_layers = KeyframingUtils.list_all_anim_layers()
        inactive_layers = list(all_layers)
        inactive_layers.remove(layer)

        try:
            KeyframingUtils.lock_anim_layers(inactive_layers)
            KeyframingUtils.select_anim_layers(inactive_layers, False)
            KeyframingUtils.lock_anim_layers([layer], False)
            KeyframingUtils.select_anim_layers([layer])
        except:
            print('{0} does not exist'.format(layer))


    @staticmethod
    def get_base_anim_layer():
        return cmd.animLayer(q=True, root=True)

    @staticmethod
    def list_all_anim_layers():
        return cmd.ls(type='animLayer')

    @staticmethod
    def list_all_user_layers():
        return cmd.ls(type='animLayer')[1:]

    @staticmethod
    def select_anim_layers(layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return
        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, selected=state)
            except:
                print('{0} does not exist'.format(layer))

    @staticmethod
    def select_top_anim_layer():
        user_layers = KeyframingUtils.list_all_user_layers()

        if len(user_layers) >= 1:
            top_layer = KeyframingUtils.list_all_user_layers()[-1]
        else:
            top_layer = KeyframingUtils.get_base_anim_layer()

        KeyframingUtils.set_active_anim_layer(top_layer)
        # cmd.animLayer(top_layer, edit=True, selected=True)

    @staticmethod
    def is_anim_layer_selected(layer):
        try:
            return cmd.animLayer(layer, query=True, selected=True)
        except:
            print('{0} does not exist'.format(layer))

    @staticmethod
    def any_user_layer_exists():
        user_layers = KeyframingUtils.list_all_user_layers()
        if user_layers:
            return True
        return False

    @staticmethod
    def get_selected_anim_layers():
        layers = KeyframingUtils.list_all_anim_layers()
        selected_layers = []
        for layer in layers:
            if KeyframingUtils.is_anim_layer_selected(layer):
                selected_layers.append(layer)

        print(selected_layers)
        return selected_layers

    @staticmethod
    def set_anim_layers_color(layers, color):
        all_layers = KeyframingUtils.list_all_anim_layers()
        selected_layers = KeyframingUtils.get_selected_anim_layers()

        try:
            cmd.setAttr("{0}.ghostColor", color)
        except:
            print('{0} does not exist'.format(layers))

    @staticmethod
    def lock_anim_layers(layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, lock=state)
            except:
                print('{0} does not exist'.format(layer))

    @staticmethod
    def solo_anim_layers(layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, solo=state)
            except:
                print('{0} does not exist'.format(layer))

    @staticmethod
    def mute_anim_layers(layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, mute=state)
            except:
                print('{0} does not exist'.format(layer))

    @staticmethod
    def add_objects_to_layer(layer):
        try:
            cmd.animLayer(layer, edit=True, addSelectedObjects=True)
        except:
            cmd.warning('Could not add objects to layer.')


