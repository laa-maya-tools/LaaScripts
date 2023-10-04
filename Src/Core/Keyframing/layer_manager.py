# =============================================================================
# SCRIPT: Layer Manager v1.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Manages all the animation layers functionality.
# =============================================================================
import maya.cmds as cmd
from LaaScripts.Src.Python3.Utils import info_utils as info

RED, GREEN, BLUE, YELLOW, PINK, ORANGE = 12, 18, 17, 21, 19, 20


class LayerManager(object):

    def __init__(self):
        print ('initial')
        self.colors = [RED, GREEN, BLUE, YELLOW, PINK, ORANGE]

        self.all_layers = self.list_all_layers()

    def create_new_layer(self, layer):
        cmd.animLayer(layer, mute=True, solo=True, override=True, passthrough=False, lock=True)

    def merge_layer(self, bake=False):
        pass

    def get_base_layer(self):
        """
        Get the base animation layer.
        :return: base animation.
        :rtype: str
        """
        return cmd.animLayer(q=True, root=True)

    def list_all_layers(self):
        """
        List all the animation layers on the scene.
        :return: All animation layers.
        :rtype: list of str
        """
        return cmd.ls(type='animLayer')

    def list_all_user_layers(self):
        return cmd.ls(type='animLayer')[1:]


    def lock_layers(self, layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, lock=state)
            except:
                print('{0} does not exist'.format(layer))

    def solo_layers(self, layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, solo=state)
            except:
                print('{0} does not exist'.format(layer))

    def mute_layers(self, layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, mute=state)
            except:
                print('{0} does not exist'.format(layer))


    def select_layers(self, layers, state=True):
        if len(layers) == 0:
            print('Layers list is empty.')
            return

        for layer in layers:
            try:
                cmd.animLayer(layer, edit=True, selected=state)
            except:
                print('{0} does not exist'.format(layer))

    def set_active_layer(self, layer):
        all_layers = self.list_all_layers()
        inactive_layers = list(all_layers)
        inactive_layers.remove(layer)


        print(all_layers, inactive_layers)

        try:
            self.lock_layers(inactive_layers)
            self.select_layers(inactive_layers, False)
            self.lock_layers([layer], False)
            self.select_layers([layer])
        except:
            print('{0} does not exist'.format(layer))

    def is_selected(self, layer):
        try:
            return cmd.animLayer(layer, query=True, selected=True)
        except:
            print('{0} does not exist'.format(layer))

    def get_selected_layers(self):
        """
        Get all the selected layers.
        :return: All selected layers.
        :rtype: list of str
        """
        layers = self.list_all_layers()
        selected_layers = []
        for layer in layers:
            if self.is_selected(layer):
                selected_layers.append(layer)

        print(selected_layers)
        return selected_layers

    def activate_next_layer(self):
        """
        Loop through all the animation layers selecting the next one, unlocking it, and deselecting
        and locking all the inactive layers.
        """
        all_layers = self.list_all_layers()
        selected_layers = self.get_selected_layers()

        # If there is no base layer, return
        if len(all_layers) == 0:
            return

        # If there is only the base layer, we select it
        if len(all_layers) == 1:
            self.select_layers([all_layers[-1]])
            return

        if len(selected_layers) > 1:
            self.set_active_layer(all_layers[-1])
            return

        # If the last layer is selected, we select the first one
        if self.is_selected(all_layers[-1]):
            self.set_active_layer(all_layers[0])
            return

        for i, layer in enumerate(all_layers):
            if self.is_selected(layer):
                self.set_active_layer(all_layers[i+1])
                return

        self.set_active_layer(all_layers[-1])

    def set_layers_color(self, layers, color):
        all_layers = self.list_all_layers()
        selected_layers = self.get_selected_layers()

        try:
            cmd.setAttr("{0}.ghostColor", color)
        except:
            print('{0} does not exist'.format(layer))

    def activate_previous_layer(self):
        """
        Loop through all the animation layers selecting the previous one, unlocking it, and deselecting
        and locking all the inactive layers.
        """
        all_layers = self.list_all_layers()
        selected_layers = self.get_selected_layers()

        # If there is no base layer, return
        if len(all_layers) == 0:
            return

        # If there is only the base layer, we select it
        if len(all_layers) == 1:
            self.select_layers([all_layers[0]])
            return

        if len(selected_layers) > 1:
            self.set_active_layer(all_layers[0])
            return

        # If the last layer is selected, we select the first one
        if self.is_selected(all_layers[0]):
            self.set_active_layer(all_layers[-1])
            return

        for i, layer in enumerate(all_layers):
            if self.is_selected(layer):
                self.set_active_layer(all_layers[i-1])
                return

        self.set_active_layer(all_layers[0])


if __name__ == '__main__':
    lm = LayerManager()
    lm.set_layer_color()

