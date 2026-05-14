import maya.cmds as cmd

from LaaScripts.Src.constants import constants as c
from LaaScripts.Src.utils.scene import info_utils as info

_MAYA_CAT_PREFIX = 'Custom Scripts.Laa '


class HotkeyManager(object):

    # ------------------------------------------------------------------
    # Naming helpers
    # ------------------------------------------------------------------

    @staticmethod
    def to_runtime_name(method_name):
        """'go_to_next_frame' -> 'LaaGoToNextFrame'"""
        return 'Laa' + ''.join(w.capitalize() for w in method_name.split('_'))

    @staticmethod
    def to_name_command(method_name):
        return HotkeyManager.to_runtime_name(method_name) + 'NameCommand'

    @staticmethod
    def to_display_name(method_name):
        """'go_to_next_frame' -> 'Go To Next Frame'"""
        return ' '.join(w.capitalize() for w in method_name.split('_'))

    # ------------------------------------------------------------------
    # Hotkey string parsing / formatting
    # ------------------------------------------------------------------

    @staticmethod
    def parse_hotkey_string(s):
        """'Ctrl+Alt+X' -> {'key':'x','ctrl':True,'alt':True,'shift':False}"""
        if not s:
            return None
        parts = s.split('+')
        return {
            'key':   parts[-1].lower(),
            'ctrl':  'Ctrl'  in parts,
            'alt':   'Alt'   in parts,
            'shift': 'Shift' in parts,
        }

    @staticmethod
    def format_hotkey(info):
        """{'key':'x','ctrl':True,...} -> 'Ctrl+X'"""
        if not info:
            return ''
        parts = []
        if info.get('ctrl'):  parts.append('Ctrl')
        if info.get('alt'):   parts.append('Alt')
        if info.get('shift'): parts.append('Shift')
        parts.append(info['key'].upper())
        return '+'.join(parts)

    # ------------------------------------------------------------------
    # Command catalogue
    # ------------------------------------------------------------------

    @staticmethod
    def get_all_commands():
        """Returns list of dicts sorted by (category, display_name)."""
        result = []
        for method, data in c.COMMANDS.items():
            result.append({
                'method':          method,
                'display':         HotkeyManager.to_display_name(method),
                'category':        data[c.CATEGORY],
                'default_hotkey':  data[c.HOTKEY],
            })
        return sorted(result, key=lambda x: (x['category'], x['display']))

    @staticmethod
    def get_categories():
        return sorted({data[c.CATEGORY] for data in c.COMMANDS.values()})

    # ------------------------------------------------------------------
    # Maya hotkey query / conflict detection
    # ------------------------------------------------------------------

    @staticmethod
    def get_name_command_for_key(key, ctrl=False, alt=False, shift=False):
        """Returns the nameCommand currently bound to this key combo, or ''."""
        try:
            return cmd.hotkey(keyShortcut=key, q=True, name=True,
                              ctl=ctrl, alt=alt, sht=shift) or ''
        except Exception:
            return ''

    @staticmethod
    def is_laa_command(name_cmd):
        return name_cmd.startswith('Laa') or name_cmd.startswith('laa_')

    @staticmethod
    def check_conflict(key, ctrl=False, alt=False, shift=False):
        """Returns (has_conflict, current_nameCommand).
        has_conflict is True only when the key is bound to a non-LaaScripts command.
        """
        current = HotkeyManager.get_name_command_for_key(key, ctrl, alt, shift)
        if not current or HotkeyManager.is_laa_command(current):
            return False, current
        return True, current

    # ------------------------------------------------------------------
    # Runtime / name command registration
    # ------------------------------------------------------------------

    @staticmethod
    def _ensure_runtime_command(method_name):
        runtime = HotkeyManager.to_runtime_name(method_name)
        if not cmd.runTimeCommand(runtime, q=True, exists=True):
            category = c.COMMANDS[method_name][c.CATEGORY]
            cmd.runTimeCommand(
                runtime,
                annotation=runtime,
                commandLanguage='python',
                category=_MAYA_CAT_PREFIX + category,
                command=c.OBJECT_NAME.TRIGGER_COMMAND.format(method_name),
            )
        return runtime

    @staticmethod
    def _ensure_name_command(method_name):
        runtime  = HotkeyManager._ensure_runtime_command(method_name)
        name_cmd = HotkeyManager.to_name_command(method_name)
        cmd.nameCommand(name_cmd, annotation=name_cmd,
                        command=runtime, sourceType='mel')
        return name_cmd

    # ------------------------------------------------------------------
    # Hotkey assignment / removal
    # ------------------------------------------------------------------

    @staticmethod
    def assign_hotkey(method_name, key, ctrl=False, alt=False, shift=False):
        name_cmd = HotkeyManager._ensure_name_command(method_name)
        cmd.hotkey(keyShortcut=key, name=name_cmd, ctl=ctrl, alt=alt, sht=shift)

    @staticmethod
    def remove_hotkey(key, ctrl=False, alt=False, shift=False):
        cmd.hotkey(keyShortcut=key, name='', releaseName='',
                   ctl=ctrl, alt=alt, sht=shift)

    # ------------------------------------------------------------------
    # Hotkey set management
    # ------------------------------------------------------------------

    @staticmethod
    def get_all_hotkey_sets():
        return cmd.hotkeySet(q=True, hotkeySetArray=True) or []

    @staticmethod
    def get_current_hotkey_set():
        return cmd.hotkeySet(q=True, current=True)

    @staticmethod
    def set_current_hotkey_set(name):
        try:
            cmd.hotkeySet(name, e=True, current=True)
            info.show_info('HOTKEY SET: {0}'.format(name))
            return True, ''
        except Exception as e:
            return False, str(e)

    @staticmethod
    def create_hotkey_set(name, source='Maya_Default'):
        if name in HotkeyManager.get_all_hotkey_sets():
            return False, 'Hotkey set "{0}" already exists.'.format(name)
        try:
            cmd.hotkeySet(name, source=source, current=True)
            return True, ''
        except Exception as e:
            return False, str(e)

    @staticmethod
    def delete_hotkey_set(name):
        if name == 'Maya_Default':
            return False, 'Cannot delete the Maya_Default hotkey set.'
        try:
            cmd.hotkeySet(name, e=True, delete=True)
            return True, ''
        except Exception as e:
            return False, str(e)

    @staticmethod
    def toggle_hotkey_sets():
        hotkey_sets = HotkeyManager.get_all_hotkey_sets()
        if len(hotkey_sets) == 1:
            info.show_info(hotkey_sets[0])
            return
        current = HotkeyManager.get_current_hotkey_set()
        if current == hotkey_sets[-1]:
            HotkeyManager.set_current_hotkey_set(hotkey_sets[0])
            return
        for i, hs in enumerate(hotkey_sets):
            if current == hs:
                HotkeyManager.set_current_hotkey_set(hotkey_sets[i + 1])
                return
