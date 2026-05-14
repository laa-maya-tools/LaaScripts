import maya.OpenMayaUI as mui

from LaaScripts.Src.utils.qt_compat import (
    QtWidgets as wdg, QtCore as cor, QtGui as gui, wrapInstance,
    QMB_Yes, QMB_No, Qt_UserRole, QAV_SingleSelection,
)
from LaaScripts.Src.core.prefs.hotkey_manager import HotkeyManager
from LaaScripts.Src.constants import constants as c
from LaaScripts.Src.data.user_data import UserData


class HotkeyManagerDialog(wdg.QDialog):

    def __init__(self, parent=None):
        if parent is None:
            parent = wrapInstance(int(mui.MQtUtil.mainWindow()), wdg.QWidget)
        super(HotkeyManagerDialog, self).__init__(parent)

        self._assignments = {}   # method_name -> {key, ctrl, alt, shift}
        self._selected_method = None

        self._load_assignments()
        self._build_ui()
        self._populate_table()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load_assignments(self):
        ud = UserData()
        all_sets = ud.user_data.get(c.USER_DATA.HOTKEY_ASSIGNMENTS, {})
        current_set = HotkeyManager.get_current_hotkey_set()
        self._assignments = dict(all_sets.get(current_set, {}))

    def _save_assignments(self):
        ud = UserData()
        all_sets = ud.user_data.get(c.USER_DATA.HOTKEY_ASSIGNMENTS, {})
        current_set = HotkeyManager.get_current_hotkey_set()
        all_sets[current_set] = self._assignments
        ud.user_data[c.USER_DATA.HOTKEY_ASSIGNMENTS] = all_sets
        UserData.store_user_data(ud.user_data, c.PATH.USER_DATA_FILE)

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self):
        self.setWindowTitle('LaaScripts  —  Hotkey Manager')
        self.setMinimumSize(720, 560)

        root = wdg.QVBoxLayout(self)
        root.setSpacing(8)
        root.setContentsMargins(12, 12, 12, 12)

        root.addLayout(self._build_set_bar())
        root.addLayout(self._build_filter_bar())
        root.addWidget(self._build_table())
        root.addWidget(self._build_assign_panel())
        root.addLayout(self._build_footer())

    def _build_set_bar(self):
        bar = wdg.QHBoxLayout()
        bar.addWidget(wdg.QLabel('Hotkey Set:'))

        self._set_combo = wdg.QComboBox()
        self._set_combo.setMinimumWidth(180)
        self._refresh_set_combo()
        self._set_combo.currentTextChanged.connect(self._on_set_changed)
        bar.addWidget(self._set_combo)

        new_btn = wdg.QPushButton('New')
        new_btn.setFixedWidth(64)
        new_btn.clicked.connect(self._new_hotkey_set)
        bar.addWidget(new_btn)

        del_btn = wdg.QPushButton('Delete')
        del_btn.setFixedWidth(64)
        del_btn.clicked.connect(self._delete_hotkey_set)
        bar.addWidget(del_btn)

        bar.addStretch()
        return bar

    def _build_filter_bar(self):
        bar = wdg.QHBoxLayout()

        bar.addWidget(wdg.QLabel('Category:'))
        self._cat_combo = wdg.QComboBox()
        self._cat_combo.setMinimumWidth(130)
        self._cat_combo.addItem('All')
        for cat in HotkeyManager.get_categories():
            self._cat_combo.addItem(cat)
        self._cat_combo.currentTextChanged.connect(self._apply_filter)
        bar.addWidget(self._cat_combo)

        bar.addSpacing(20)
        bar.addWidget(wdg.QLabel('Search:'))
        self._search = wdg.QLineEdit()
        self._search.setPlaceholderText('Filter commands...')
        self._search.textChanged.connect(self._apply_filter)
        bar.addWidget(self._search)

        return bar

    def _build_table(self):
        self._table = wdg.QTreeWidget()
        self._table.setColumnCount(3)
        self._table.setHeaderLabels(['Command', 'Hotkey', 'Category'])
        self._table.setColumnWidth(0, 270)
        self._table.setColumnWidth(1, 140)
        self._table.setColumnWidth(2, 120)
        self._table.setRootIsDecorated(False)
        self._table.setAlternatingRowColors(True)
        self._table.setSelectionMode(QAV_SingleSelection)
        self._table.setSortingEnabled(True)
        self._table.sortByColumn(2, cor.Qt.SortOrder.AscendingOrder
                                 if hasattr(cor.Qt, 'SortOrder')
                                 else cor.Qt.AscendingOrder)
        self._table.itemSelectionChanged.connect(self._on_selection_changed)
        return self._table

    def _build_assign_panel(self):
        group = wdg.QGroupBox('Assign Hotkey')
        layout = wdg.QVBoxLayout(group)
        layout.setSpacing(6)

        # key + modifiers row
        key_row = wdg.QHBoxLayout()
        key_row.addWidget(wdg.QLabel('Key:'))

        self._key_input = wdg.QLineEdit()
        self._key_input.setMaxLength(1)
        self._key_input.setFixedWidth(44)
        self._key_input.setPlaceholderText('?')
        key_row.addWidget(self._key_input)

        key_row.addSpacing(16)
        self._ctrl_cb  = wdg.QCheckBox('Ctrl')
        self._alt_cb   = wdg.QCheckBox('Alt')
        self._shift_cb = wdg.QCheckBox('Shift')
        key_row.addWidget(self._ctrl_cb)
        key_row.addWidget(self._alt_cb)
        key_row.addWidget(self._shift_cb)
        key_row.addStretch()
        layout.addLayout(key_row)

        # action buttons row
        btn_row = wdg.QHBoxLayout()
        self._assign_btn = wdg.QPushButton('Assign Hotkey')
        self._assign_btn.clicked.connect(self._assign_hotkey)
        self._remove_btn = wdg.QPushButton('Remove Hotkey')
        self._remove_btn.clicked.connect(self._remove_hotkey)
        btn_row.addWidget(self._assign_btn)
        btn_row.addWidget(self._remove_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        return group

    def _build_footer(self):
        footer = wdg.QHBoxLayout()
        footer.addStretch()
        close_btn = wdg.QPushButton('Close')
        close_btn.setFixedWidth(80)
        close_btn.clicked.connect(self.accept)
        footer.addWidget(close_btn)
        return footer

    # ------------------------------------------------------------------
    # Table population & filtering
    # ------------------------------------------------------------------

    _grey = gui.QColor(120, 120, 120)

    def _populate_table(self):
        self._table.clear()
        for info in HotkeyManager.get_all_commands():
            method  = info['method']
            hk_info = self._assignments.get(method)
            if hk_info:
                hk_str  = HotkeyManager.format_hotkey(hk_info)
                is_user = True
            else:
                default = HotkeyManager.parse_hotkey_string(info['default_hotkey'])
                hk_str  = HotkeyManager.format_hotkey(default) if default else ''
                is_user = False
            item = wdg.QTreeWidgetItem([info['display'], hk_str, info['category']])
            item.setData(0, Qt_UserRole, method)
            if not is_user and hk_str:
                item.setForeground(1, gui.QBrush(self._grey))
            self._table.addTopLevelItem(item)
        self._apply_filter()

    def _apply_filter(self):
        cat    = self._cat_combo.currentText()
        text   = self._search.text().lower()
        for i in range(self._table.topLevelItemCount()):
            item = self._table.topLevelItem(i)
            cat_ok  = (cat == 'All') or (item.text(2) == cat)
            text_ok = text in item.text(0).lower()
            item.setHidden(not (cat_ok and text_ok))

    def _refresh_item(self, method):
        for info in HotkeyManager.get_all_commands():
            if info['method'] != method:
                continue
            for i in range(self._table.topLevelItemCount()):
                item = self._table.topLevelItem(i)
                if item.data(0, Qt_UserRole) != method:
                    continue
                hk_info = self._assignments.get(method)
                if hk_info:
                    item.setText(1, HotkeyManager.format_hotkey(hk_info))
                    item.setForeground(1, gui.QBrush())  # default (white/theme)
                else:
                    default = HotkeyManager.parse_hotkey_string(info['default_hotkey'])
                    hk_str  = HotkeyManager.format_hotkey(default) if default else ''
                    item.setText(1, hk_str)
                    if hk_str:
                        item.setForeground(1, gui.QBrush(self._grey))
                    else:
                        item.setForeground(1, gui.QBrush())
                break
            break

    # ------------------------------------------------------------------
    # Selection
    # ------------------------------------------------------------------

    def _on_selection_changed(self):
        items = self._table.selectedItems()
        if not items:
            self._selected_method = None
            return

        self._selected_method = items[0].data(0, Qt_UserRole)
        hk_info = self._assignments.get(self._selected_method)
        if not hk_info:
            # fall back to the suggested default so the user can just hit Assign
            for cmd_info in HotkeyManager.get_all_commands():
                if cmd_info['method'] == self._selected_method:
                    hk_info = HotkeyManager.parse_hotkey_string(cmd_info['default_hotkey'])
                    break

        if hk_info:
            self._key_input.setText(hk_info['key'].upper())
            self._ctrl_cb.setChecked(hk_info.get('ctrl',  False))
            self._alt_cb.setChecked(hk_info.get('alt',   False))
            self._shift_cb.setChecked(hk_info.get('shift', False))
        else:
            self._key_input.clear()
            self._ctrl_cb.setChecked(False)
            self._alt_cb.setChecked(False)
            self._shift_cb.setChecked(False)

    # ------------------------------------------------------------------
    # Hotkey assignment / removal
    # ------------------------------------------------------------------

    def _assign_hotkey(self):
        if not self._selected_method:
            wdg.QMessageBox.warning(self, 'No Command', 'Select a command first.')
            return

        key = self._key_input.text().strip().lower()
        if not key:
            wdg.QMessageBox.warning(self, 'No Key', 'Enter a key to assign.')
            return

        ctrl  = self._ctrl_cb.isChecked()
        alt   = self._alt_cb.isChecked()
        shift = self._shift_cb.isChecked()

        has_conflict, current = HotkeyManager.check_conflict(key, ctrl, alt, shift)
        if has_conflict:
            hk_label = HotkeyManager.format_hotkey(
                {'key': key, 'ctrl': ctrl, 'alt': alt, 'shift': shift}
            )
            reply = wdg.QMessageBox.question(
                self, 'Hotkey Conflict',
                '"{0}" is already assigned to:\n\n    {1}\n\n'
                'Override it?'.format(hk_label, current),
                QMB_Yes | QMB_No,
            )
            if reply != QMB_Yes:
                return

        new_info = {'key': key, 'ctrl': ctrl, 'alt': alt, 'shift': shift}

        # clear the same key from any other command we track
        for m, info in list(self._assignments.items()):
            if info == new_info and m != self._selected_method:
                del self._assignments[m]
                self._refresh_item(m)

        HotkeyManager.assign_hotkey(self._selected_method, key, ctrl, alt, shift)
        self._assignments[self._selected_method] = new_info
        self._save_assignments()
        self._refresh_item(self._selected_method)

    def _remove_hotkey(self):
        if not self._selected_method:
            return
        hk_info = self._assignments.get(self._selected_method)
        if not hk_info:
            return

        HotkeyManager.remove_hotkey(
            hk_info['key'],
            hk_info.get('ctrl',  False),
            hk_info.get('alt',   False),
            hk_info.get('shift', False),
        )
        del self._assignments[self._selected_method]
        self._save_assignments()
        self._refresh_item(self._selected_method)

        self._key_input.clear()
        self._ctrl_cb.setChecked(False)
        self._alt_cb.setChecked(False)
        self._shift_cb.setChecked(False)

    # ------------------------------------------------------------------
    # Hotkey set management
    # ------------------------------------------------------------------

    def _refresh_set_combo(self):
        self._set_combo.blockSignals(True)
        self._set_combo.clear()
        for s in HotkeyManager.get_all_hotkey_sets():
            self._set_combo.addItem(s)
        current = HotkeyManager.get_current_hotkey_set()
        idx = self._set_combo.findText(current)
        if idx >= 0:
            self._set_combo.setCurrentIndex(idx)
        self._set_combo.blockSignals(False)

    def _on_set_changed(self, name):
        if name:
            HotkeyManager.set_current_hotkey_set(name)
            self._load_assignments()
            self._populate_table()

    def _new_hotkey_set(self):
        name, ok = wdg.QInputDialog.getText(
            self, 'New Hotkey Set', 'Name:')
        if not ok or not name.strip():
            return
        name = name.strip()

        sets = HotkeyManager.get_all_hotkey_sets()
        source, ok2 = wdg.QInputDialog.getItem(
            self, 'Base Set', 'Inherit hotkeys from:', sets, 0, False)
        if not ok2:
            source = 'Maya_Default'

        success, msg = HotkeyManager.create_hotkey_set(name, source=source)
        if success:
            self._refresh_set_combo()
            # create_hotkey_set activates the new set in Maya before the combo
            # refreshes, so currentTextChanged may not fire — call explicitly.
            self._on_set_changed(name)
        else:
            wdg.QMessageBox.warning(self, 'Error', msg)

    def _delete_hotkey_set(self):
        name = self._set_combo.currentText()
        reply = wdg.QMessageBox.question(
            self, 'Delete Hotkey Set',
            'Delete "{0}"? This cannot be undone.'.format(name),
            QMB_Yes | QMB_No,
        )
        if reply != QMB_Yes:
            return
        success, msg = HotkeyManager.delete_hotkey_set(name)
        if success:
            self._refresh_set_combo()
        else:
            wdg.QMessageBox.warning(self, 'Error', msg)
