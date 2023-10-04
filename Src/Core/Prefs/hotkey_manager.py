# =============================================================================
# SCRIPT: Hotkey Manager v1.0
# AUTHOR: Leandro Adeodato
# -----------------------------------------------------------------------------
# Loops through all hotkey sets.
# =============================================================================
import maya.cmds as cmd
from LaaScripts.Src.Python3.Utils import info_utils as info


class HotkeyManager(object):

    @staticmethod
    def update_hotkeys():
        print('update')

    def get_current_hotkey_set(self):
        """
        Get the current hotkey set.
        :return: Current hotkey name.
        :rtype: str
        """
        return cmd.hotkeySet(q=True, current=True)

    def set_current_hotkey_set(self, hotkey_set):
        """
        Set the current hotkey set.
        :param str hotkey_set: Hotkey set name.
        """
        try:
            cmd.hotkeySet(hotkey_set, e=True, current=True)
            info.show_info('HOTKEY SET: {0}'.format(hotkey_set))
        except:
            print('{0} hotkey set doesn`t exist.'.format(hotkey_set))

    def list_all_hotkey_sets(self):
        """
        List all existing hotkey sets.
        :return: All hotkey sets.
        :rtype: list of str
        """
        return cmd.hotkeySet(q=True, hotkeySetArray=True)

    def toggle_hotkey_sets(self):
        """
        Loop through all existing hotkey sets.
        """
        hotkey_sets = self.list_all_hotkey_sets()
        if len(hotkey_sets) == 1:
            info.show_info(hotkey_sets[0])
            return

        current_hotkey_set = self.get_current_hotkey_set()
        if current_hotkey_set == hotkey_sets[-1]:
            self.set_current_hotkey_set(hotkey_sets[0])
            return

        for i, hotkey_set in enumerate(hotkey_sets):
            if current_hotkey_set == hotkey_set:
                self.set_current_hotkey_set(hotkey_sets[i+1])
                return


if __name__ == '__main__':
    HotkeyManager.update_hotkeys()

