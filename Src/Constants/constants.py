import os
from dataclasses import dataclass
from collections import namedtuple

from PySide2 import QtCore as cor
from PySide2 import QtGui as gui
from PySide2 import QtWidgets as wdg

__APP_NAME__ = 'LaaScripts'
__APP_VERSION__ = '1.0.0'


# =============================================================================
# PAGES
# =============================================================================
@dataclass
class _Pages:
    # ----- STRINGS -----
    DEFAULT: int = 0
    CTRL: int = 1
    ALT: int = 2
    SHIFT: int = 3


PAGE = _Pages()


# =============================================================================
# STRINGS CONSTANTS
# =============================================================================
@dataclass
class _String:
    # ----- STRINGS -----
    EMPTY: str = ''
    SPACE: str = ' '
    NO_SPACE: str = ''
    SEPARATOR: str = '#'


STRING = _String()


# =============================================================================
# STRINGS CONSTANTS
# =============================================================================
@dataclass
class _Separator:
    # ----- STRINGS -----
    MAIN: str = '#'
    SECOND: str = ';'


SEPARATOR = _Separator()

# =============================================================================
# LISTS CONSTANTS
# =============================================================================
EMPTY_LIST = []


# =============================================================================
# NAVIGATION CONSTANTS
# =============================================================================
@dataclass
class _Navigation:
    # ----- IDS -----
    NAME: int = 0
    INDEX: int = 1
    # ----- MODES -----
    MOVE: str = 'Move'
    ROTATE: str = 'Rotate'
    SCALE: str = 'Scale'
    ALL: str = 'All'
    # ----- COORD SYSTEMS -----
    LOCAL: str = 'Local'
    WORLD: str = 'World'
    NORMAL: str = 'Normal'
    GIMBAL: str = 'Gimbal'
    PARENT: str = 'Parent'
    COMPONENT: str = 'Component'
    # ----- AXIS -----
    TX: str = 'tx'
    TY: str = 'ty'
    TZ: str = 'tz'
    RX: str = 'rx'
    RY: str = 'ry'
    RZ: str = 'rz'
    SX: str = 'sx'
    SY: str = 'sy'
    SZ: str = 'sz'
    # ----- COORD SYSTEMS -----
    TRS_XYZ: tuple = ('tx', 'ty', 'tz')
    ROT_XYZ: tuple = ('rx', 'ry', 'rz')
    SCL_XYZ: tuple = ('sx', 'sy', 'sz')


NAVIGATION = _Navigation()


# =============================================================================
# SECTIONS IDS
# =============================================================================
@dataclass
class _SectionInfo:
    # ----- MAIN SECTIONS -----
    MAIN: int = 0
    DEFAULT: int = 1
    CTRL: int = 2
    ALT: int = 3
    SHIFT: int = 4
    # ----- SECTIONS -----
    LOGO: int = 0
    EMPTY: int = 1
    PREFS: int = 2
    NAVIGATION: int = 3
    KEYFRAMING: int = 4
    SELECTION: int = 5
    TRANSFORM: int = 6
    VIEWPORT: int = 7
    PLAYBACK: int = 8
    # ----- SECTIONS OBJECT NAMES -----
    LOGO_SECTION: str = 'LogoSection'
    INACTIVE_SECTION: str = 'InactiveSection'
    ACTIVE_SECTION: str = 'ActiveSection'


SECTION_INFO = _SectionInfo()


# =============================================================================
# TIMELINE CONSTANTS
# =============================================================================
@dataclass
class _Timeline:
    # ----- IDS -----
    ANIMATION: int = 0
    PLAYBACK: int = 1
    # ----- MODES -----
    ALL_RANGE: int = 0
    BEFORE_CURRENT_TIME: int = 1
    AFTER_CURRENT_TIME: int = 2
    # ----- RANGE SLIDER -----
    START_TIME: int = 0
    END_TIME: int = 1
    # ----- KEYS -----
    NEXT: str = 'next'
    PREVIOUS: str = 'previous'
    FIRST: str = 'first'
    LAST: str = 'last'


TIMELINE = _Timeline()


# =============================================================================
# BLENDING CONSTANTS
# =============================================================================
@dataclass
class _TweenerMode:
    # ----- MODES -----
    TWEEN_MACHINE: int = 0
    BLEND_TO_NEIGHBORS: int = 1
    BLEND_TO_EASE: int = 2
    TWEEN_TO_RESET: int = 3


TWEENER_MODE = _TweenerMode()


# =============================================================================
# PLAYBACK CONSTANTS
# =============================================================================
@dataclass
class _Playback:
    # ----- MARKER IDS -----
    RANGE: int = 0
    COLOR: int = 1
    INDEX: int = 0
    FRAME: int = 1
    TYPE: int = 2
    # ----- MARKER TYPES -----
    KEY: int = 0
    BREAKDOWN: int = 1
    INBETWEEN: int = 2
    ALL: int = 3
    # ----- MARKER NAMES -----
    FRAMES: str = 'frames'
    TYPES: str = 'types'
    MARKER_TYPE_NAMES: tuple = ('KEY', 'BREAKDOWN', 'INBETWEEN')

    # ----- SECTION NAMES -----
    SECTION_RANGES: str = 'ranges'
    SECTION_COLORS: str = 'colors'


PLAYBACK = _Playback()


# =============================================================================
# NODES CONSTANTS
# =============================================================================
@dataclass
class _Nodes:
    # ----- NODES DESCRIPTIONS -----
    VERSION: str = '{0} v{1}'.format(__APP_NAME__, __APP_VERSION__)
    ICON: str = 'icon'
    # ----- NODES ATTRIBUTES -----
    VERSION_ATTR: str = 'version'
    ICON_ATTR: str = 'icon'
    PARENT_ATTR: str = 'parent'
    KEY_MARKERS_ATTR: str = 'key_markers'
    FRAME_MARKERS_ATTR: str = 'frame_markers'
    TIMELINE_SECTION_ATTR: str = 'timeline_section'
    ACTIVE_CHAR_ATTR: str = 'active_char'
    CTRLS_LIST_ATTR: str = 'ctrls_list'

    # ----- NODES PATHS -----
    LAASCRIPTS_NODE: str = __APP_NAME__
    PREFS_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Prefs')
    NAVIGATION_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Navigation')
    SELECTION_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Selection')
    CHAR_INFO_NODE: str = '{0}|{1}'.format(SELECTION_NODE, 'CharInfo')
    CTRLS_NODE: str = '{0}|{1}'.format(SELECTION_NODE, 'Ctrls')
    UPPERBODY_NODE: str = '{0}|{1}'.format(CTRLS_NODE, 'UpperBody')
    CONTROLS_SELECTOR_NODE: str = '{0}|{1}'.format(SELECTION_NODE, 'ControlsSelector')
    TRANSFORM_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Transform')
    VIEWPORT_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Viewport')
    PLAYBACK_NODE: str = '{0}|{1}'.format(LAASCRIPTS_NODE, 'Playback')
    FRAME_MARKER_NODE: str = '{0}|{1}'.format(PLAYBACK_NODE, 'FrameMarker')
    TIMELINE_SECTION_NODE: str = '{0}|{1}'.format(PLAYBACK_NODE, 'TimelineSection')


NODES = _Nodes()


# =============================================================================
# NAMESPACES CONSTANTS
# =============================================================================
@dataclass
class _Namespaces:
    # ----- BODY CTRLS -----
    EXCLUDED: tuple = ('UI', 'shared')


NAMESPACES = _Namespaces()


# =============================================================================
# CTRLS CONSTANTS
# =============================================================================
@dataclass
class _Ctrls:
    # ----- BODY CTRLS -----
    ALL: str = 'all_ctrls'
    BODY: str = 'body_ctrls'
    ROOT: str = 'root_ctrls'
    SPINE: str = 'spine_ctrls'
    NECK: str = 'neck_ctrls'
    HEAD: str = 'head_ctrls'

    # ----- ARM CTRLS -----
    RT_ARM: str = 'rt_arm_ctrls'
    RT_FK_ARM: str = 'rt_fk_arm_ctrls'
    RT_IK_ARM: str = 'rt_ik_arm_ctrls'
    LF_ARM: str = 'lf_arm_ctrls'
    LF_FK_ARM: str = 'lf_fk_arm_ctrls'
    LF_IK_ARM: str = 'lf_ik_arm_ctrls'

    # ----- LEG CTRLS -----
    RT_LEG: str = 'rt_leg_ctrls'
    RT_FK_LEG: str = 'rt_fk_leg_ctrls'
    RT_IK_LEG: str = 'rt_ik_leg_ctrls'
    LF_LEG: str = 'lf_leg_ctrls'
    LF_FK_LEG: str = 'lf_fk_leg_ctrls'
    LF_IK_LEG: str = 'lf_ik_leg_ctrls'

    # ----- EXTRA CTRLS -----
    ROOT_EXTRA: str = 'root_extra_ctrls'
    RT_ELBOW_EXTRA: str = 'rt_elbow_extra_ctrls'
    RT_HAND_EXTRA: str = 'rt_hand_extra_ctrls'
    RT_KNEE_EXTRA: str = 'rt_knee_extra_ctrls'
    RT_FOOT_EXTRA: str = 'rt_foot_extra_ctrls'
    LF_ELBOW_EXTRA: str = 'lf_elbow_extra_ctrls'
    LF_HAND_EXTRA: str = 'lf_hand_extra_ctrls'
    LF_KNEE_EXTRA: str = 'lf_knee_extra_ctrls'
    LF_FOOT_EXTRA: str = 'lf_foot_extra_ctrls'


CTRLS = _Ctrls()


# =============================================================================
# VIEWPORT CONSTANTS
# =============================================================================
@dataclass
class _Viewport:
    # ----- VIEWPORT ELEMENTS -----
    XRAY: str = 'xr'
    DEF_MATERIAL: str = 'udm'
    WIREFRAME: str = 'wos'
    CAMERAS: str = 'ca'
    GRID: str = 'gr'
    IMG_PLANE: str = 'ip'
    JOINTS: str = 'j'
    LIGHTS: str = 'lt'
    LOCATORS: str = 'lc'
    HANDLES: str = 'm'
    CURVES: str = 'nc'
    POLYGONS: str = 'pm'
    MODEL_PANEL: str = 'modelPanel'


VIEWPORT = _Viewport()

# =============================================================================
# PATHS CONSTANTS
# =============================================================================
_all_maya_versions = ('2017', '2018', '2019', '2020', '2021', '2022', '2023')
_user_dir = os.path.expanduser('~')
_maya_dir = r'{0}\Documents\maya'.format(_user_dir)


def list_folders_from_version(folder):
    folders_from_version = []
    for version in _all_maya_versions:
        folder_path = '{0}\{1}\{2}'.format(_maya_dir, version, folder)
        if os.path.exists(folder_path):
            folders_from_version.append(folder_path)

    return tuple(folders_from_version)


@dataclass
class _Paths:
    # ----- DIRS -----
    USER_DIR: str = _user_dir
    DATA_DIR: str = os.path.dirname(os.path.abspath(__file__))

    DATA_FOLDER: str = DATA_DIR.split(os.sep)[-1]
    ROOT_DIR: str = DATA_DIR.replace(DATA_FOLDER, STRING.EMPTY)
    ROOT_FOLDER: str = __APP_NAME__
    STYLE_DIR: str = r'{0}{1}'.format(ROOT_DIR, 'Resources\Style')
    STYLE_FILE: str = r'{0}\{1}'.format(STYLE_DIR, 'stylesheet.qss')
    # ----- FILES -----
    LAASCRIPTS_FOLDER: str = __APP_NAME__
    LAASCRIPTS_DATA_FOLDER: str = r'{0}_{1}'.format(LAASCRIPTS_FOLDER, 'Data')
    # ----- MAYA DIRS -----
    SCRIPTS_FOLDER: str = 'scripts'
    PICKERS_FOLDER: str = 'pickers'
    MODULES_FOLDER: str = 'modules'
    PREFS_FOLDER: str = 'prefs'
    ICONS_FOLDER: str = 'icons'
    SHELVES_FOLDER: str = 'shelves'
    HOTKEYS_FOLDER: str = 'hotkeys'
    MAYA_ENV_FILE_NAME: str = 'Maya.env'
    USER_DATA_FILE_NAME: str = 'user_data.json'
    # ----- OTHER DIRS -----
    MAYA_DIR: str = r'{0}\maya'.format(USER_DIR)
    SCRIPTS_DIR: str = r'{0}\{1}'.format(MAYA_DIR, SCRIPTS_FOLDER)
    MODULES_DIR: str = r'{0}\{1}'.format(MAYA_DIR, MODULES_FOLDER)
    LAASCRIPTS_DIR: str = r'{0}\{1}'.format(SCRIPTS_DIR, LAASCRIPTS_FOLDER)
    LAASCRIPTS_DATA_DIR: str = r'{0}\{1}'.format(SCRIPTS_DIR, LAASCRIPTS_DATA_FOLDER)
    PICKERS_DIR: str = r'{0}\{1}'.format(LAASCRIPTS_DATA_DIR, PICKERS_FOLDER)
    CURRENT_DIR: str = r'{0}'.format(os.path.abspath(os.getcwd()))
    PREFS_DIRS: tuple = list_folders_from_version(PREFS_FOLDER)
    ICONS_DIRS: tuple = list_folders_from_version(ICONS_FOLDER)
    SHELVES_DIRS: tuple = list_folders_from_version(SHELVES_FOLDER)
    USER_DATA_FILE: str = r'{0}\{1}'.format(LAASCRIPTS_DATA_DIR, USER_DATA_FILE_NAME)


PATH = _Paths()


# =============================================================================
# USER DATA CONSTANTS
# =============================================================================
@dataclass
class _UserData:
    # ----- DIRS -----
    USER_DIR: str = _user_dir
    DATA_DIR: str = os.path.dirname(os.path.abspath(__file__))
    INFO_ENABLED: str = 'info_enabled'
    WARNINGS_ENABLED: str = 'warnings_enabled'
    PLAYBACK_MODE: str = 'playback_mode'
    LOOP: str = 'loop'
    STOP: str = 'stop'
    PASS: str = 'pass'
    EXPAND: str = 'expand'
    TIME_INCREMENT: str = 'time_increment'
    SMART_MANIPULATOR: str = 'smart_manipulator'


USER_DATA = _UserData()


# =============================================================================
# MAYA DOCK POSITIONS CONSTANTS
# =============================================================================
@dataclass
class _DockPosition:
    # ----- IDS -----
    MAYA_TOP: int = 0
    MAYA_BOTTOM: int = 1
    TIMELINE_TOP: int = 2
    TIMELINE_BOTTOM: int = 3
    SHELF_TOP: int = 4
    SHELF_BOTTOM: int = 5
    # ----- PLACE -----
    POSITION: tuple = (
        ('top', False),
        ('bottom', False),
        ('TimeSlider', 'top'),
        ('TimeSlider', 'bottom'),
        ('Shelf', 'top'),
        ('Shelf', 'bottom')
    )


DOCK_POSITION = _DockPosition()


# =============================================================================
# SWITCH BUTTONS STATES
# =============================================================================
@dataclass
class _SwitchButtonStates:
    # ----- INDEXES -----
    UNCHECKED_INDEX: int = 0
    SELECTED_INDEX: int = 1
    CHECKED_INDEX: int = 2

    # ----- OBJECTS -----
    UNCHECKED: object = cor.Qt.Unchecked
    SELECTED: object = cor.Qt.PartiallyChecked
    CHECKED: object = cor.Qt.Checked


SWITCH_BUTTON_STATES = _SwitchButtonStates()


# =============================================================================
# OBJECT NAMES CONSTANTS
# =============================================================================
@dataclass
class _ObjectName:
    # ----- Sections -----
    LOGO_SECTION: str = 'LogoSection'
    ACTIVE_SECTION: str = 'ActiveSection'
    INACTIVE_SECTION: str = 'InactiveSection'
    # ----- Buttons -----
    BUTTON: str = 'Button'
    LAA_BUTTON: str = 'LaaButton'
    TOOL_BUTTON: str = 'ToolButton'
    OK_BUTTON: str = 'OkButton'
    CANCEL_BUTTON: str = 'CancelButton'
    TOGGLE_BUTTON: str = 'ToggleButton'
    SWITCH_BUTTON: str = 'SwitchButton'
    LOGO_BUTTON: str = 'LogoButton'
    CTRL_LOGO_BUTTON: str = 'CtrlLogoButton'
    ALT_LOGO_BUTTON: str = 'AltLogoButton'
    SHIFT_LOGO_BUTTON: str = 'ShiftLogoButton'
    TOGGLE_TEXT_BUTTON: str = 'ToggleTextButton'
    # ----- Sliders -----
    SLIDER: str = 'Slider'
    TWEENER_SLIDER: str = 'TweenerSlider'
    BLEND_TO_NEIGHBORS_SLIDER: str = 'BlendToNeighborsSlider'
    BLEND_TO_RESET_SLIDER: str = 'BlendToResetSlider'
    EASE_IN_OUT_SLIDER: str = 'EaseInOutSlider'
    HPAN_SLIDER: str = 'HPanSlider'
    VPAN_SLIDER: str = 'VPanSlider'
    ZOOM_SLIDER: str = 'ZoomSlider'
    # ----- Other Widgets -----
    COMBOBOX: str = 'ComboBox'
    SEPARATOR: str = 'Separator'
    SPACE: str = 'Space'
    LINEEDIT: str = 'LineEdit'
    DARK_LINEEDIT: str = 'DarkLineEdit'
    DARK_SEPARATOR: str = 'DarkSeparator'
    MESSAGE_BOX: str = 'MessageBox'
    # ----- DIALOG -----
    CONTENT: str = 'Content'
    DIALOG_TITLE: str = 'DialogTitle'
    DIALOG_TITLE_FRAME: str = 'DialogTitleFrame'
    LABEL: str = 'Label'
    ASSIGN_BUTTON: str = 'AssignButton'
    CLEAR_BUTTON: str = 'ClearButton'
    KEYBOARD_ICON: str = ':/_Controls/keyboard'
    # ----- OTHER -----
    SET_TANGENTS: str = 'SetTangents'
    SET_TIMELINE_HEIGHT: str = 'SetTimelineHeight'
    CHANGE_PIVOT: str = 'ChangePivot'
    GLOBAL_MODE: str = 'GlobalMode'
    IK_MOVER: str = 'IkMover'
    TRIGGER_COMMAND = 'import LaaScripts; LaaScripts.trigger.Trigger().{0}();'
    HOTKEY_SEPARATOR = '+'
    TEXT_SEPARATOR = '#'


OBJECT_NAME = _ObjectName()


# =============================================================================
# WIDGET CREATION CONSTANTS
# =============================================================================
@dataclass
class _WidgetCommand:
    # ----- Commands -----
    BUTTON: str = 'wdg.QPushButton()'
    LAA_BUTTON: str = 'lb.LaaButton()'
    SWITCH_BUTTON: str = 'lsb.LaaSwitchButton()'
    STACKED_WDG: str = 'wdg.QStackedWidget()'
    FRAME: str = 'wdg.QFrame()'
    LINEEDIT: str = 'wdg.QLineEdit()'
    SLIDER: str = 'wdg.QSlider()'
    COMBOBOX: str = 'wdg.QComboBox()'
    SEPARATOR: str = 'wdg.QFrame()'
    SPACE: str = 'wdg.QFrame()'
    H_LAYOUT: str = 'wdg.QHBoxLayout()'
    V_LAYOUT: str = 'wdg.QVBoxLayout()'


WIDGET_COMMAND = _WidgetCommand()


# =============================================================================
# WIDGET CREATION CONSTANTS
# =============================================================================
@dataclass
class _CursorType:
    # ----- Cursors -----
    SELECT: object = cor.Qt.ArrowCursor
    HAND: object = cor.Qt.PointingHandCursor
    EDIT: object = cor.Qt.IBeamCursor


CURSOR_TYPE = _CursorType()


# =============================================================================
# MAYA CONTROLS CONSTANTS
# =============================================================================
@dataclass
class _MayaControls:
    # ----- Cursors -----
    TIME_CONTROL: str = '$gPlayBackSlider'
    SHELF: str = '$gShelfTopLevel'
    STATUS_LINE: str = '$gStatusLine'
    ATTRIBUTE_EDITOR: str = '$gAttributeEditorWindowName'
    CHANNELBOX: str = '$gChannelBoxName'
    TOOLBOX: str = '$gToolBox'
    COMMAND_LINE: str = '$gCommandLine'
    RANGE_SLIDER: str = '$gTimeRangeSlider'
    HELP_LINE: str = '$gHelpLineForm'


MAYA_CONTROLS = _MayaControls()


# =============================================================================
# KEY SEQUENCER CONSTANTS
# =============================================================================
@dataclass
class _Key:
    CTRL: int = 0
    ALT: int = 1
    SHIFT: int = 2
    MAIN_KEY: int = 3
    FULL_SEQUENCE: int = 4


KEY = _Key()
KeySequence = namedtuple('KeySequence', 'ctrl alt shift key full')

# =============================================================================
# COLORS CONSTANTS
# =============================================================================
COLOR_VARIATIONS = 9
BRIGHTNESS_VARIATIONS = 3


@dataclass
class _Tone:
    DARK: int = 0
    MEDIUM: int = 1
    LIGHT: int = 2


@dataclass
class _Color:
    RED: tuple = ('#FF3B3B', '#FF5C5C', '#FF8080')
    ORANGE: tuple = ('#F18779', '#FFC4A3', '#FCCC76')
    YELLOW: tuple = ('#FFCB00', '#FEDD4B', '#FEED73')
    GREEN: tuple = ('#05C270', '#39DA8A', '#57EBA3')
    CYAN: tuple = ('#00CFDD', '#74E0E6', '#A9EFF3')
    BLUE: tuple = ('#0063F8', '#5B8DEE', '#9DBFF8')
    PURPLE: tuple = ('#6500CD', '#AC5CD9', '#DEA5E8')
    DARK_GREY: tuple = ('#333333', '#373737', '#444444')
    LIGHT_GREY: tuple = ('#777777', '#999999', '#CCCCCC')


TONE = _Tone()
COLOR = _Color()


# =============================================================================
# MESSAGE BOX IDS
# =============================================================================
@dataclass
class _Dialog:
    ERROR_DIALOG: int = 0
    WARNING_DIALOG: int = 1
    INFO_DIALOG: int = 2
    QUESTION_DIALOG: int = 3


DIALOG = _Dialog()


# =============================================================================
# TIMEOUT CONSTANTS
# =============================================================================
@dataclass
class _Timeout:
    FAST: int = 1000
    MEDIUM: int = 3000
    SLOW: int = 5000


TIMEOUT = _Timeout


# =============================================================================
# MESSAGES CONSTANTS
# =============================================================================
@dataclass
class _Message:
    color: str = COLOR.LIGHT_GREY[TONE.MEDIUM]
    background: str = COLOR.DARK_GREY[TONE.MEDIUM]
    border: str = COLOR.LIGHT_GREY[TONE.DARK]
    timeout: int = TIMEOUT.MEDIUM


warning_msg = _Message(COLOR.DARK_GREY[TONE.DARK], COLOR.ORANGE[TONE.MEDIUM], COLOR.DARK_GREY[TONE.DARK])
error_msg = _Message(COLOR.DARK_GREY[TONE.DARK], COLOR.RED[TONE.LIGHT], COLOR.DARK_GREY[TONE.DARK])
success_msg = _Message(COLOR.DARK_GREY[TONE.DARK], COLOR.GREEN[TONE.LIGHT], COLOR.DARK_GREY[TONE.DARK])
info_msg = _Message(COLOR.LIGHT_GREY[TONE.MEDIUM], COLOR.DARK_GREY[TONE.MEDIUM], COLOR.LIGHT_GREY[TONE.DARK])


# =============================================================================
# SIZE DATACLASS
# =============================================================================
@dataclass
class Size:
    width: tuple
    height: tuple
    width_policy: object
    height_policy: object


section_size = Size((40, 360), (40, 40), wdg.QSizePolicy.Expanding, wdg.QSizePolicy.Expanding)
logo_size = Size((84, 84), (40, 40), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
button_size = Size((24, 24), (24, 24), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
switch_button_size = Size((36, 36), (24, 24), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
toggle_button_size = Size((36, 36), (24, 24), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
text_button_size = Size((100, 100), (24, 24), wdg.QSizePolicy.Minimum, wdg.QSizePolicy.Minimum)
slider_size = Size((200, 200), (24, 24), wdg.QSizePolicy.Minimum, wdg.QSizePolicy.Minimum)
combobox_size = Size((60, 60), (24, 24), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
lineedit_size = Size((40, 40), (20, 20), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
separator_size = Size((2, 2), (32, 32), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)
space_size = Size((10, 10), (32, 32), wdg.QSizePolicy.Fixed, wdg.QSizePolicy.Fixed)


@dataclass
class MessageBox:
    title: str
    icon: str
    buttons: object


message_boxes = {
    DIALOG.ERROR_DIALOG: MessageBox('Error', ':/_Controls/error_message', wdg.QMessageBox.Ok),
    DIALOG.WARNING_DIALOG: MessageBox('Warning', ':/_Controls/warning_message', wdg.QMessageBox.Ok),
    DIALOG.INFO_DIALOG: MessageBox('Info', ':/_Controls/info_message', wdg.QMessageBox.Ok),
    DIALOG.QUESTION_DIALOG: MessageBox('Question', ':/_Controls/question_message',
                                       wdg.QMessageBox.Yes | wdg.QMessageBox.No)
}


# =============================================================================
# SECTION DATACLASS
# =============================================================================
@dataclass
class Section:
    object_name: str
    padding: tuple = (0, 0, 0, 0)
    spacing: int = 0
    enabled: bool = True


main_sections = {
    SECTION_INFO.MAIN: Section('MainLayout'),
    SECTION_INFO.DEFAULT: Section('DefaultLayout'),
    SECTION_INFO.CTRL: Section('CtrlLayout'),
    SECTION_INFO.ALT: Section('AltLayout'),
    SECTION_INFO.SHIFT: Section('ShiftLayout')
}

default_sections = {
    SECTION_INFO.LOGO: Section('LogoSection', (0, 0, 0, 0), 0),
    SECTION_INFO.EMPTY: Section('InactiveSection', (0, 0, 0, 0), 0),
    SECTION_INFO.PREFS: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.NAVIGATION: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.KEYFRAMING: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.SELECTION: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.TRANSFORM: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.VIEWPORT: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.PLAYBACK: Section('ActiveSection', (10, 0, 10, 0), 2, False),
}

ctrl_sections = {
    SECTION_INFO.LOGO: Section('LogoSection', (0, 0, 0, 0), 0),
    SECTION_INFO.EMPTY: Section('InactiveSection', (0, 0, 0, 0), 0),
    SECTION_INFO.PREFS: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.NAVIGATION: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.KEYFRAMING: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.SELECTION: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.TRANSFORM: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.VIEWPORT: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.PLAYBACK: Section('ActiveSection', (10, 0, 10, 0), 2, False),
}

alt_sections = {
    SECTION_INFO.LOGO: Section('LogoSection', (0, 0, 0, 0), 0),
    SECTION_INFO.EMPTY: Section('InactiveSection', (0, 0, 0, 0), 0),
    SECTION_INFO.PREFS: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.NAVIGATION: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.KEYFRAMING: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.SELECTION: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.TRANSFORM: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.VIEWPORT: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.PLAYBACK: Section('ActiveSection', (10, 0, 10, 0), 2, False),
}

shift_sections = {
    SECTION_INFO.LOGO: Section('LogoSection', (0, 0, 0, 0), 0),
    SECTION_INFO.EMPTY: Section('InactiveSection', (0, 0, 0, 0), 0),
    SECTION_INFO.PREFS: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.NAVIGATION: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.KEYFRAMING: Section('ActiveSection', (10, 0, 10, 0), 2),
    SECTION_INFO.SELECTION: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.TRANSFORM: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.VIEWPORT: Section('ActiveSection', (10, 0, 10, 0), 2, False),
    SECTION_INFO.PLAYBACK: Section('ActiveSection', (10, 0, 10, 0), 2, False),
}


# =============================================================================
# WIDGETS DATACLASS
# =============================================================================
@dataclass
class LogoButton:
    accessible_name: str = OBJECT_NAME.LOGO_BUTTON
    object_name: str = OBJECT_NAME.LOGO_BUTTON
    enabled: bool = True
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    class_name: str = OBJECT_NAME.BUTTON
    command: str = WIDGET_COMMAND.LAA_BUTTON
    default_hotkey: str = STRING.EMPTY
    size: Size = logo_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class ToolButton:
    accessible_name: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.TOOL_BUTTON
    enabled: bool = True
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    default_hotkey: str = STRING.EMPTY
    text: str = STRING.EMPTY
    class_name: str = OBJECT_NAME.BUTTON
    command: str = WIDGET_COMMAND.LAA_BUTTON
    size: Size = button_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class ToggleButton:
    accessible_name: str = STRING.EMPTY
    object_name: str = STRING.EMPTY
    enabled: bool = True
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    class_name: str = OBJECT_NAME.TOGGLE_BUTTON
    command: str = WIDGET_COMMAND.LAA_BUTTON
    default_hotkey: str = STRING.EMPTY
    size: Size = toggle_button_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class SwitchButton:
    accessible_name: str = STRING.EMPTY
    object_name: str = STRING.EMPTY
    enabled: bool = True
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    class_name: str = OBJECT_NAME.SWITCH_BUTTON
    command: str = WIDGET_COMMAND.SWITCH_BUTTON
    default_hotkey: str = STRING.EMPTY
    size: Size = switch_button_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class Slider:
    accessible_name: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.SLIDER
    enabled: bool = True
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    class_name: str = OBJECT_NAME.SLIDER
    command: str = WIDGET_COMMAND.SLIDER
    default_hotkey: str = STRING.EMPTY
    size: Size = slider_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class ComboBox:
    enabled: bool = True
    accessible_name: str = STRING.EMPTY
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.COMBOBOX
    class_name: str = OBJECT_NAME.COMBOBOX
    command: str = WIDGET_COMMAND.COMBOBOX
    default_hotkey: str = STRING.EMPTY
    size: Size = combobox_size
    cursor: object = CURSOR_TYPE.HAND
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class Space:
    accessible_name: str = STRING.EMPTY
    tooltip: str = STRING.EMPTY
    enabled: bool = True
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.SPACE
    class_name: str = OBJECT_NAME.SPACE
    command: str = WIDGET_COMMAND.SPACE
    default_hotkey: str = STRING.EMPTY
    size: Size = space_size
    cursor: object = CURSOR_TYPE.SELECT
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class Separator:
    enabled: bool = True
    accessible_name: str = STRING.EMPTY
    tooltip: str = STRING.EMPTY
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.SEPARATOR
    class_name: str = OBJECT_NAME.SEPARATOR
    command: str = WIDGET_COMMAND.SEPARATOR
    default_hotkey: str = STRING.EMPTY
    size: Size = separator_size
    cursor: object = CURSOR_TYPE.SELECT
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


@dataclass
class LineEdit:
    accessible_name: str = STRING.EMPTY
    tooltip: str = STRING.EMPTY
    enabled: bool = True
    icon: str = STRING.EMPTY
    text: str = STRING.EMPTY
    object_name: str = OBJECT_NAME.LINEEDIT
    class_name: str = OBJECT_NAME.LINEEDIT
    command: str = WIDGET_COMMAND.LINEEDIT
    default_hotkey: str = STRING.EMPTY
    size: Size = lineedit_size
    cursor: object = CURSOR_TYPE.SELECT
    parent_layout: str = WIDGET_COMMAND.H_LAYOUT


# =============================================================================
# DEFAULT WIDGETS
# =============================================================================
default_widgets = {
    SECTION_INFO.LOGO: [
        LogoButton(OBJECT_NAME.LOGO_BUTTON, OBJECT_NAME.LOGO_BUTTON)
    ],
    SECTION_INFO.EMPTY: [
        Space()
    ],
    SECTION_INFO.PREFS: [
        SwitchButton(
            'set_stepped_tangents#set_linear_tangents#set_auto_tangents',
            OBJECT_NAME.SET_TANGENTS, True, 'Set Tangents'),
        SwitchButton(
            'set_timeline_height_1x#set_timeline_height_2x#set_timeline_height_4x',
            OBJECT_NAME.SET_TIMELINE_HEIGHT, True, 'Set Timeline Height')
    ],
    SECTION_INFO.NAVIGATION: [
        ToolButton(
            'filter_translate_channels',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Translate Channels',
            ':/Navigation/filter_translate_channels'
        ),
        ToolButton(
            'filter_rotate_channels',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Rotate Channels',
            ':/Navigation/filter_rotate_channels'
        ),
        ToolButton(
            'filter_scale_channels',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Scale Channels',
            ':/Navigation/filter_scale_channels'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'smart_translate_manipulator',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Smart Translate Manipulator',
            ':/Navigation/smart_translate_manipulator'
        )
    ],
    SECTION_INFO.KEYFRAMING: [
        ToolButton(
            'push_prev_key',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Push Prev Key',
            ':/Keyframing/push_prev_key'
        ),
        ToolButton(
            'push_next_key',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Push Next Key',
            ':/Keyframing/push_next_key'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'copy_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Copy Keys',
            ':/Keyframing/copy_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'spread_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Spread Timeline Section',
            ':/Keyframing/spread_timeline_section'
        ),
        ToolButton(
            'bake_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Ones',
            ':/Keyframing/bake_on_ones'
        ),
        ToolButton(
            'rebuild_on_twos',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Rebuild on Twos',
            ':/Keyframing/rebuild_on_twos',
        ),
        ToolButton(
            'bake_on_shared_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Shared Keys',
            ':/Keyframing/bake_on_shared_keys',

        ),
        Space(), Separator(True), Space(),
        Slider(OBJECT_NAME.TWEENER_SLIDER, OBJECT_NAME.TWEENER_SLIDER, True)
    ],
    SECTION_INFO.SELECTION: [
        ToolButton(
            'select_left_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Set Blocking Preferences',
            ':/Selection/select_left_ctrl'
        ),
        ToolButton(
            'select_top_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Top Control',
            ':/Selection/select_top_ctrl'
        ),
        ToolButton(
            'select_bottom_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Bottom Control',
            ':/Selection/select_bottom_ctrl'
        ),
        ToolButton(
            'select_right_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Right Control',
            ':/Selection/select_right_ctrl'
        )
    ],
    SECTION_INFO.TRANSFORM: [
        ToggleButton(
            'global_mode',
            OBJECT_NAME.GLOBAL_MODE,
            False,
            'Global Mode'
        ),
        ToggleButton(
            'ik_mover',
            OBJECT_NAME.IK_MOVER,
            False,
            'Ik Mover'
        ),
        SwitchButton(
            'change_pivot_01#change_pivot_02#change_pivot_03',
            OBJECT_NAME.CHANGE_PIVOT,
            False,
            'Change Pivot'
        ),
        Space(), Separator(False), Space(),
        LineEdit('increment', 'increment', False),
        ToolButton(
            'increase_transform',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Increase Transform',
            ':/Transform/increase_transform'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'reset_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Reset Transforms',
            ':/Transform/reset_transforms'
        ),
        ToolButton(
            'rotate_char_base',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Rotate Character Base',
            ':/Transform/rotate_char_base'
        ),
        ToolButton(
            'snap_locator',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Snap Locator',
            ':/Transform/snap_locator'
        ),
        ToolButton(
            'copy_relationship',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Relationship',
            ':/Transform/copy_relationship'
        ),
        ToolButton(
            'copy_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Transforms',
            ':/Transform/copy_transforms'
        )
    ],
    SECTION_INFO.VIEWPORT: [
        ToolButton(
            'toggle_viewport_mode',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Viewport Mode',
            ':/Viewport/toggle_viewport_mode'
        ),
        ToolButton(
            'filter_all_objects_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Filter All Objects Visibility',
            ':/Viewport/filter_all_objects_visibility'
        ),
        ToolButton(
            'create_facial_camera',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Create Facial Camera',
            ':/Viewport/create_facial_camera'
        ),
        ToolButton(
            'toggle_image_plane_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Image Plane Visibility',
            ':/Viewport/toggle_image_plane_visibility'
        ),
        Space(), Separator(False), Space(),
        ComboBox(False),
        Slider(OBJECT_NAME.HPAN_SLIDER, OBJECT_NAME.HPAN_SLIDER, False)
    ],
    SECTION_INFO.PLAYBACK: [
        ToolButton(
            'add_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Key Marker',
            ':/Playback/add_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'prev_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Prev Key Marker',
            ':/Playback/prev_key_marker'
        ),
        ToolButton(
            'next_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Next Key Marker',
            ':/Playback/next_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'playblast_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Playblast on Ones',
            ':/Playback/playblast_on_ones'
        ),
        ToolButton(
            'play_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Play on Ones',
            ':/Playback/play_on_ones'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'add_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Timeline Section',
            ':/Playback/add_timeline_section'
        ),
        ComboBox(False)
    ]
}

# =============================================================================
# CTRL WIDGETS
# =============================================================================
ctrl_widgets = {
    SECTION_INFO.LOGO: [
        LogoButton(OBJECT_NAME.CTRL_LOGO_BUTTON, OBJECT_NAME.CTRL_LOGO_BUTTON)
    ],
    SECTION_INFO.EMPTY: [
        Space()
    ],
    SECTION_INFO.PREFS: [
        SwitchButton(
            'set_stepped_tangents#set_linear_tangents#set_auto_tangents',
            OBJECT_NAME.SET_TANGENTS, True, 'Set Tangents'),
        SwitchButton(
            'set_timeline_height_1x#set_timeline_height_2x#set_timeline_height_4x',
            OBJECT_NAME.SET_TIMELINE_HEIGHT, True, 'Set Timeline Height')
    ],
    SECTION_INFO.NAVIGATION: [
        ToolButton(
            'filter_translate_channels_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Translate Channels On Ones',
            ':/Navigation/filter_translate_channels_on_ones'
        ),
        ToolButton(
            'filter_rotate_channels_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Rotate Channels On Ones',
            ':/Navigation/filter_rotate_channels_on_ones'
        ),
        ToolButton(
            'filter_scale_channels_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter Scale Channels On Ones',
            ':/Navigation/filter_scale_channels_on_ones'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'smart_rotate_manipulator',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Smart Rotate Manipulator',
            ':/Navigation/smart_rotate_manipulator'
        )
    ],
    SECTION_INFO.KEYFRAMING: [
        ToolButton(
            'push_prev_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Push Prev Keys',
            ':/Keyframing/push_prev_keys'
        ),
        ToolButton(
            'push_next_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Push Next Keys',
            ':/Keyframing/push_next_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'cut_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Cut Keys',
            ':/Keyframing/cut_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'squeeze_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Squeeze Timeline Section',
            ':/Keyframing/squeeze_timeline_section'
        ),
        ToolButton(
            'bake_on_twos',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Twos',
            ':/Keyframing/bake_on_twos'
        ),
        ToolButton(
            'rebuild_on_fours',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Rebuild on Fours',
            ':/Keyframing/rebuild_on_fours',
        ),
        ToolButton(
            'bake_on_base_layer_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Base Layer Keys',
            ':/Keyframing/bake_on_base_layer_keys',
        ),
        Space(), Separator(True), Space(),
        Slider(OBJECT_NAME.BLEND_TO_NEIGHBORS_SLIDER, OBJECT_NAME.BLEND_TO_NEIGHBORS_SLIDER, True)
    ],
    SECTION_INFO.SELECTION: [
        ToolButton(
            'select_left_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Set Blocking Preferences',
            ':/Selection/select_left_ctrl'
        ),
        ToolButton(
            'select_top_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Top Control',
            ':/Selection/select_top_ctrl'
        ),
        ToolButton(
            'select_bottom_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Bottom Control',
            ':/Selection/select_bottom_ctrl'
        ),
        ToolButton(
            'select_right_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Right Control',
            ':/Selection/select_right_ctrl'
        )
    ],
    SECTION_INFO.TRANSFORM: [
        ToggleButton(
            'global_mode',
            OBJECT_NAME.GLOBAL_MODE,
            False,
            'Global Mode'
        ),
        ToggleButton(
            'ik_mover',
            OBJECT_NAME.IK_MOVER,
            False,
            'Ik Mover'
        ),
        SwitchButton(
            'change_pivot_01#change_pivot_02#change_pivot_03',
            OBJECT_NAME.CHANGE_PIVOT,
            False,
            'Change Pivot'
        ),
        Space(), Separator(False), Space(),
        LineEdit('increment', 'increment', False),
        ToolButton(
            'increase_transform',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Increase Transform',
            ':/Transform/increase_transform'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'reset_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Reset Transforms',
            ':/Transform/reset_transforms'
        ),
        ToolButton(
            'rotate_char_base',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Rotate Character Base',
            ':/Transform/rotate_char_base'
        ),
        ToolButton(
            'snap_locator',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Snap Locator',
            ':/Transform/snap_locator'
        ),
        ToolButton(
            'copy_relationship',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Relationship',
            ':/Transform/copy_relationship'
        ),
        ToolButton(
            'copy_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Transforms',
            ':/Transform/copy_transforms'
        )
    ],
    SECTION_INFO.VIEWPORT: [
        ToolButton(
            'toggle_viewport_mode',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Viewport Mode',
            ':/Viewport/toggle_viewport_mode'
        ),
        ToolButton(
            'filter_all_objects_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Filter All Objects Visibility',
            ':/Viewport/filter_all_objects_visibility'
        ),
        ToolButton(
            'create_facial_camera',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Create Facial Camera',
            ':/Viewport/create_facial_camera'
        ),
        ToolButton(
            'toggle_image_plane_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Image Plane Visibility',
            ':/Viewport/toggle_image_plane_visibility'
        ),
        Space(), Separator(False), Space(),
        ComboBox(False),
        Slider(OBJECT_NAME.HPAN_SLIDER, OBJECT_NAME.HPAN_SLIDER, False)
    ],
    SECTION_INFO.PLAYBACK: [
        ToolButton(
            'add_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Key Marker',
            ':/Playback/add_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'prev_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Prev Key Marker',
            ':/Playback/prev_key_marker'
        ),
        ToolButton(
            'next_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Next Key Marker',
            ':/Playback/next_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'playblast_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Playblast on Ones',
            ':/Playback/playblast_on_ones'
        ),
        ToolButton(
            'play_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Play on Ones',
            ':/Playback/play_on_ones'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'add_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Timeline Section',
            ':/Playback/add_timeline_section'
        ),
        ComboBox(False)
    ]
}

# =============================================================================
# ALT WIDGETS
# =============================================================================
alt_widgets = {
    SECTION_INFO.LOGO: [
        LogoButton(OBJECT_NAME.ALT_LOGO_BUTTON, OBJECT_NAME.ALT_LOGO_BUTTON)
    ],
    SECTION_INFO.EMPTY: [
        Space()
    ],
    SECTION_INFO.PREFS: [
        SwitchButton(
            'set_stepped_tangents#set_linear_tangents#set_auto_tangents',
            OBJECT_NAME.SET_TANGENTS, True, 'Set Tangents'),
        SwitchButton(
            'set_timeline_height_1x#set_timeline_height_2x#set_timeline_height_4x',
            OBJECT_NAME.SET_TIMELINE_HEIGHT, True, 'Set Timeline Height')
    ],
    SECTION_INFO.NAVIGATION: [
        ToolButton(
            'filter_translate_channels_on_twos', OBJECT_NAME.TOOL_BUTTON, True, 'Filter Translate Channels On Twos',
            ':/Navigation/filter_translate_channels_on_twos'
        ),
        ToolButton(
            'filter_rotate_channels_on_twos', OBJECT_NAME.TOOL_BUTTON, True, 'Filter Rotate Channels On Twos',
            ':/Navigation/filter_rotate_channels_on_twos'
        ),
        ToolButton(
            'filter_scale_channels_on_twos', OBJECT_NAME.TOOL_BUTTON, True, 'Filter Scale Channels On Twos',
            ':/Navigation/filter_scale_channels_on_twos'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'smart_scale_manipulator', OBJECT_NAME.TOOL_BUTTON, True, 'Smart Scale Manipulator',
            ':/Navigation/smart_scale_manipulator'
        )
    ],
    SECTION_INFO.KEYFRAMING: [
        ToolButton(
            'pull_prev_key',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Pull Prev Key',
            ':/Keyframing/pull_prev_key'
        ),
        ToolButton(
            'pull_next_key',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Pull Next Key',
            ':/Keyframing/pull_next_key'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'insert_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Insert Keys',
            ':/Keyframing/insert_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'crop_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Crop Timeline Section',
            ':/Keyframing/crop_timeline_section'
        ),
        ToolButton(
            'bake_on_fours',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Fours',
            ':/Keyframing/bake_on_fours'
        ),
        ToolButton(
            'rebuild_on_key_markers',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Rebuild on Key Markers',
            ':/Keyframing/rebuild_on_key_markers',
        ),
        ToolButton(
            'store_keytimes',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Store Keytimes',
            ':/Keyframing/store_keytimes',

        ),
        Space(), Separator(True), Space(),
        Slider(OBJECT_NAME.BLEND_TO_RESET_SLIDER, OBJECT_NAME.BLEND_TO_RESET_SLIDER, True)
    ],
    SECTION_INFO.SELECTION: [
        ToolButton(
            'select_left_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Set Blocking Preferences',
            ':/Selection/select_left_ctrl'
        ),
        ToolButton(
            'select_top_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Top Control',
            ':/Selection/select_top_ctrl'
        ),
        ToolButton(
            'select_bottom_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Bottom Control',
            ':/Selection/select_bottom_ctrl'
        ),
        ToolButton(
            'select_right_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Right Control',
            ':/Selection/select_right_ctrl'
        )
    ],
    SECTION_INFO.TRANSFORM: [
        ToggleButton(
            'global_mode',
            OBJECT_NAME.GLOBAL_MODE,
            False,
            'Global Mode'
        ),
        ToggleButton(
            'ik_mover',
            OBJECT_NAME.IK_MOVER,
            False,
            'Ik Mover'
        ),
        SwitchButton(
            'change_pivot_01#change_pivot_02#change_pivot_03',
            OBJECT_NAME.CHANGE_PIVOT,
            False,
            'Change Pivot'
        ),
        Space(), Separator(False), Space(),
        LineEdit('increment', 'increment', False),
        ToolButton(
            'increase_transform',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Increase Transform',
            ':/Transform/increase_transform'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'reset_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Reset Transforms',
            ':/Transform/reset_transforms'
        ),
        ToolButton(
            'rotate_char_base',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Rotate Character Base',
            ':/Transform/rotate_char_base'
        ),
        ToolButton(
            'snap_locator',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Snap Locator',
            ':/Transform/snap_locator'
        ),
        ToolButton(
            'copy_relationship',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Relationship',
            ':/Transform/copy_relationship'
        ),
        ToolButton(
            'copy_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Transforms',
            ':/Transform/copy_transforms'
        )
    ],
    SECTION_INFO.VIEWPORT: [
        ToolButton(
            'toggle_viewport_mode',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Viewport Mode',
            ':/Viewport/toggle_viewport_mode'
        ),
        ToolButton(
            'filter_all_objects_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Filter All Objects Visibility',
            ':/Viewport/filter_all_objects_visibility'
        ),
        ToolButton(
            'create_facial_camera',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Create Facial Camera',
            ':/Viewport/create_facial_camera'
        ),
        ToolButton(
            'toggle_image_plane_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Image Plane Visibility',
            ':/Viewport/toggle_image_plane_visibility'
        ),
        Space(), Separator(False), Space(),
        ComboBox(False),
        Slider(OBJECT_NAME.HPAN_SLIDER, OBJECT_NAME.HPAN_SLIDER, False)
    ],
    SECTION_INFO.PLAYBACK: [
        ToolButton(
            'add_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Key Marker',
            ':/Playback/add_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'prev_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Prev Key Marker',
            ':/Playback/prev_key_marker'
        ),
        ToolButton(
            'next_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Next Key Marker',
            ':/Playback/next_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'playblast_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Playblast on Ones',
            ':/Playback/playblast_on_ones'
        ),
        ToolButton(
            'play_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Play on Ones',
            ':/Playback/play_on_ones'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'add_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Timeline Section',
            ':/Playback/add_timeline_section'
        ),
        ComboBox(False)
    ]
}

# =============================================================================
# SHIFT WIDGETS
# =============================================================================
shift_widgets = {
    SECTION_INFO.LOGO: [
        LogoButton(OBJECT_NAME.SHIFT_LOGO_BUTTON, OBJECT_NAME.SHIFT_LOGO_BUTTON)
    ],
    SECTION_INFO.EMPTY: [
        Space()
    ],
    SECTION_INFO.PREFS: [
        SwitchButton(
            'set_stepped_tangents#set_linear_tangents#set_auto_tangents',
            OBJECT_NAME.SET_TANGENTS, True, 'Set Tangents'),
        SwitchButton(
            'set_timeline_height_1x#set_timeline_height_2x#set_timeline_height_4x',
            OBJECT_NAME.SET_TIMELINE_HEIGHT, True, 'Set Timeline Height')
    ],
    SECTION_INFO.NAVIGATION: [
        ToolButton(
            'filter_all_channels',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Filter All Channels',
            ':/Navigation/filter_all_channels'
        ),
        ToolButton(
            'clear_all_channels',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Clear All Channels',
            ':/Navigation/clear_all_channels'
        ),
        ToolButton(
            'toggle_sync_mode',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Toggle Sync Mode',
            ':/Navigation/toggle_sync_channels'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'toggle_smart_manipulator',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Toggle Smart Manipulator',
            ':/Navigation/toggle_smart_manipulator'
        )
    ],
    SECTION_INFO.KEYFRAMING: [
        ToolButton(
            'pull_prev_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Pull Prev Keys',
            ':/Keyframing/pull_prev_keys'
        ),
        ToolButton(
            'pull_next_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Pull Next Keys',
            ':/Keyframing/pull_next_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'replace_keys',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Replace Keys',
            ':/Keyframing/replace_keys'
        ),
        Space(), Separator(True), Space(),
        ToolButton(
            'even_keytimes',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Even Keytimes',
            ':/Keyframing/even_keytimes'
        ),
        ToolButton(
            'bake_on_markers',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Markers',
            ':/Keyframing/bake_on_markers'
        ),
        ToolButton(
            'rebuild_on_frame_markers',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Rebuild on Frame Markers',
            ':/Keyframing/rebuild_on_frame_markers',
        ),
        ToolButton(
            'bake_on_stored_keytimes',
            OBJECT_NAME.TOOL_BUTTON,
            True,
            'Bake on Stored Keytimes',
            ':/Keyframing/bake_on_stored_keytimes',

        ),
        Space(), Separator(True), Space(),
        Slider(OBJECT_NAME.EASE_IN_OUT_SLIDER, OBJECT_NAME.EASE_IN_OUT_SLIDER, True)
    ],
    SECTION_INFO.SELECTION: [
        ToolButton(
            'select_left_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Set Blocking Preferences',
            ':/Selection/select_left_ctrl'
        ),
        ToolButton(
            'select_top_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Top Control',
            ':/Selection/select_top_ctrl'
        ),
        ToolButton(
            'select_bottom_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Bottom Control',
            ':/Selection/select_bottom_ctrl'
        ),
        ToolButton(
            'select_right_ctrl',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Select Right Control',
            ':/Selection/select_right_ctrl'
        )
    ],
    SECTION_INFO.TRANSFORM: [
        ToggleButton(
            'global_mode',
            OBJECT_NAME.GLOBAL_MODE,
            False,
            'Global Mode'
        ),
        ToggleButton(
            'ik_mover',
            OBJECT_NAME.IK_MOVER,
            False,
            'Ik Mover'
        ),
        SwitchButton(
            'change_pivot_01#change_pivot_02#change_pivot_03',
            OBJECT_NAME.CHANGE_PIVOT,
            False,
            'Change Pivot'
        ),
        Space(), Separator(False), Space(),
        LineEdit('increment', 'increment', False),
        ToolButton(
            'increase_transform',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Increase Transform',
            ':/Transform/increase_transform'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'reset_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Reset Transforms',
            ':/Transform/reset_transforms'
        ),
        ToolButton(
            'rotate_char_base',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Rotate Character Base',
            ':/Transform/rotate_char_base'
        ),
        ToolButton(
            'snap_locator',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Snap Locator',
            ':/Transform/snap_locator'
        ),
        ToolButton(
            'copy_relationship',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Relationship',
            ':/Transform/copy_relationship'
        ),
        ToolButton(
            'copy_transforms',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Copy Transforms',
            ':/Transform/copy_transforms'
        )
    ],
    SECTION_INFO.VIEWPORT: [
        ToolButton(
            'toggle_viewport_mode',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Viewport Mode',
            ':/Viewport/toggle_viewport_mode'
        ),
        ToolButton(
            'filter_all_objects_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Filter All Objects Visibility',
            ':/Viewport/filter_all_objects_visibility'
        ),
        ToolButton(
            'create_facial_camera',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Create Facial Camera',
            ':/Viewport/create_facial_camera'
        ),
        ToolButton(
            'toggle_image_plane_visibility',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Toggle Image Plane Visibility',
            ':/Viewport/toggle_image_plane_visibility'
        ),
        Space(), Separator(False), Space(),
        ComboBox(False),
        Slider(OBJECT_NAME.HPAN_SLIDER, OBJECT_NAME.HPAN_SLIDER, False)
    ],
    SECTION_INFO.PLAYBACK: [
        ToolButton(
            'add_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Key Marker',
            ':/Playback/add_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'prev_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Prev Key Marker',
            ':/Playback/prev_key_marker'
        ),
        ToolButton(
            'next_key_marker',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Next Key Marker',
            ':/Playback/next_key_marker'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'playblast_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Playblast on Ones',
            ':/Playback/playblast_on_ones'
        ),
        ToolButton(
            'play_on_ones',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Play on Ones',
            ':/Playback/play_on_ones'
        ),
        Space(), Separator(False), Space(),
        ToolButton(
            'add_timeline_section',
            OBJECT_NAME.TOOL_BUTTON,
            False,
            'Add Timeline Section',
            ':/Playback/add_timeline_section'
        ),
        ComboBox(False)
    ]
}

# =============================================================================
# KEYBOARD CODES
# =============================================================================
keycodes = {
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9',
    65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I',
    74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R',
    83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z',
    60: '>', 39: '?', 16777264: 'F1', 16777265: 'F2', 16777266: 'F3', 16777267: 'F4',
    16777268: 'F5', 16777269: 'F6', 16777270: 'F7', 16777271: 'F8', 16777272: 'F9', 16777273: 'F10',
    16777274: 'F11', 16777275: 'F12', 32: 'SPACE', 16777235: 'UP', 16777237: 'DOWN', 16777234: 'LEFT',
    16777236: 'RIGHT',
    16777222: 'INSERT', 16777232: 'START', 16777233: 'END', 16777238: 'PGUP', 16777239: 'PGDOWN',
    47: '/', 42: '*', 45: '-', 43: '+', 44: '.'
}

invalid_keycodes = {
    16777249: 'CTRL', 16777251: 'ALT', 16777248: 'SHIFT', 16777250: 'WND', 16777217: 'TAB', 16777252: 'CAPS',
    16777220: 'ENTER', 16777216: 'ESC', 16777219: 'RETURN', 16777223: 'SUPR',
    16777254: 'BLOCK', 16777224: 'PAUSA', 16777253: 'BNUM',
    16777221: 'ENTER2', 46: 'SUPR2', 96: 'º', 161: '¡', 186: 'º'
}

# =============================================================================
# COMMANDS AND HOTKEYS
# =============================================================================
LANGUAGE = 'Python'

LOGO_CAT, PREFS_CAT, NAVIGATION_CAT, KEYFRAMING_CAT = 0, 1, 2, 3
SELECTION_CAT, TRANSFORM_CAT, VIEWPORT_CAT, PLAYBACK_CAT = 4, 5, 6, 7
CATEGORY, HOTKEY = 0, 1

CATEGORIES = {
    LOGO_CAT: 'Logo',
    PREFS_CAT: 'Prefs',
    NAVIGATION_CAT: 'Navigation',
    KEYFRAMING_CAT: 'Keyframing',
    SELECTION_CAT: 'Selection',
    TRANSFORM_CAT: 'Transform',
    VIEWPORT_CAT: 'Viewport',
    PLAYBACK_CAT: 'Playback'
}

COMMANDS = {
    # ----- LOGO -----
    'setup_user_preferences': [CATEGORIES[LOGO_CAT], 'Ctrl+Alt+Shift+U'],

    # ----- PREFS -----
    'set_stepped_tangents': [CATEGORIES[PREFS_CAT], 'W'],
    'set_linear_tangents': [CATEGORIES[PREFS_CAT], 'W'],
    'set_auto_tangents': [CATEGORIES[PREFS_CAT], 'W'],
    'set_timeline_height_1x': [CATEGORIES[PREFS_CAT], 'W'],
    'set_timeline_height_2x': [CATEGORIES[PREFS_CAT], 'W'],
    'set_timeline_height_4x': [CATEGORIES[PREFS_CAT], 'W'],
    'toggle_hotkey_sets': [CATEGORIES[PREFS_CAT], 'W'],

    # ----- NAVIGATION -----
    'smart_translate_manipulator': [CATEGORIES[NAVIGATION_CAT], 'W'],
    'smart_rotate_manipulator': [CATEGORIES[NAVIGATION_CAT], 'E'],
    'smart_scale_manipulator': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'filter_translate_channels': [CATEGORIES[NAVIGATION_CAT], 'W'],
    'filter_translate_channels_on_ones': [CATEGORIES[NAVIGATION_CAT], 'E'],
    'filter_translate_channels_on_twos': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'filter_rotate_channels': [CATEGORIES[NAVIGATION_CAT], 'W'],
    'filter_rotate_channels_on_ones': [CATEGORIES[NAVIGATION_CAT], 'E'],
    'filter_rotate_channels_on_twos': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'filter_scale_channels': [CATEGORIES[NAVIGATION_CAT], 'W'],
    'filter_scale_channels_on_ones': [CATEGORIES[NAVIGATION_CAT], 'E'],
    'filter_scale_channels_on_twos': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'filter_all_channels': [CATEGORIES[NAVIGATION_CAT], 'W'],
    'clear_all_channels': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'toggle_sync_mode': [CATEGORIES[NAVIGATION_CAT], 'R'],
    'toggle_smart_manipulator': [CATEGORIES[NAVIGATION_CAT], 'R'],

    # ----- KEYFRAMING -----
    'bake_on_base_layer_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+D'],
    'bake_on_fours': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+A'],
    'bake_on_markers': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+C'],
    'bake_on_ones': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+X'],
    'bake_on_shared_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+V'],
    'bake_on_stored_keytimes': [CATEGORIES[KEYFRAMING_CAT], ''],
    'bake_on_twos': [CATEGORIES[KEYFRAMING_CAT], ''],
    'copy_keys': [CATEGORIES[KEYFRAMING_CAT], ''],
    'crop_timeline_section': [CATEGORIES[KEYFRAMING_CAT], ''],
    'cut_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+D'],
    'even_keytimes': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+A'],
    'insert_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+C'],
    'pull_next_key': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+X'],
    'pull_next_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+V'],
    'pull_prev_key': [CATEGORIES[KEYFRAMING_CAT], ''],
    'pull_prev_keys': [CATEGORIES[KEYFRAMING_CAT], ''],
    'push_next_key': [CATEGORIES[KEYFRAMING_CAT], ''],
    'push_next_keys': [CATEGORIES[KEYFRAMING_CAT], ''],
    'push_prev_key': [CATEGORIES[KEYFRAMING_CAT], ''],
    'push_prev_keys': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+D'],
    'rebuild_on_fours': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+Shift+A'],
    'rebuild_on_frame_markers': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+C'],
    'rebuild_on_key_markers': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+X'],
    'rebuild_on_twos': [CATEGORIES[KEYFRAMING_CAT], 'Ctrl+V'],
    'replace_keys': [CATEGORIES[KEYFRAMING_CAT], ''],
    'spread_timeline_section': [CATEGORIES[KEYFRAMING_CAT], ''],
    'squeeze_timeline_section': [CATEGORIES[KEYFRAMING_CAT], ''],
    'store_keytimes': [CATEGORIES[KEYFRAMING_CAT], ''],

    # ----- VIEWPORT -----
    'toggle_xray': [CATEGORIES[VIEWPORT_CAT], 'Alt+X'],
    'toggle_wireframe': [CATEGORIES[VIEWPORT_CAT], 'Alt+W'],
    'toggle_default_material': [CATEGORIES[VIEWPORT_CAT], 'Alt+M'],
    'toggle_cameras': [CATEGORIES[VIEWPORT_CAT], ''],
    'toggle_grid': [CATEGORIES[VIEWPORT_CAT], 'Alt+G'],
    'toggle_plane': [CATEGORIES[VIEWPORT_CAT], ''],
    'toggle_lights': [CATEGORIES[VIEWPORT_CAT], ''],
    'toggle_locators': [CATEGORIES[VIEWPORT_CAT], 'Alt+L'],
    'toggle_handles': [CATEGORIES[VIEWPORT_CAT], 'Alt+H'],
    'toggle_curves': [CATEGORIES[VIEWPORT_CAT], 'Alt+C'],
    'toggle_polygons': [CATEGORIES[VIEWPORT_CAT], 'Alt+P'],

    # ----- PLAYBACK -----
    'go_to_the_next_frame': [CATEGORIES[PLAYBACK_CAT], 'X'],
    'go_to_the_prev_frame': [CATEGORIES[PLAYBACK_CAT], 'Z'],
    'next_frame_playback_press': [CATEGORIES[PLAYBACK_CAT], ''],
    'prev_frame_playback_press': [CATEGORIES[PLAYBACK_CAT], ''],
    'next_frame_playback_release': [CATEGORIES[PLAYBACK_CAT], ''],
    'prev_frame_playback_release': [CATEGORIES[PLAYBACK_CAT], ''],
    'go_to_the_next_key': [CATEGORIES[PLAYBACK_CAT], 'V'],
    'go_to_the_prev_key': [CATEGORIES[PLAYBACK_CAT], 'C'],
    'go_to_the_next_marker': [CATEGORIES[PLAYBACK_CAT], 'Ctrl+Alt+X'],
    'go_to_the_prev_marker': [CATEGORIES[PLAYBACK_CAT], 'Ctrl+Alt+Z'],
    'add_key_markers': [CATEGORIES[PLAYBACK_CAT], 'K'],
    'add_breakdown_markers': [CATEGORIES[PLAYBACK_CAT], 'J'],
    'add_inbetween_markers': [CATEGORIES[PLAYBACK_CAT], 'L'],
    'remove_frame_markers': [CATEGORIES[PLAYBACK_CAT], 'Alt+D'],
    'add_timeline_section': [CATEGORIES[PLAYBACK_CAT], ''],
    'remove_timeline_section': [CATEGORIES[PLAYBACK_CAT], '']
}


def get_category_from_name(name):
    _category = COMMANDS[name][CATEGORY]
    return 'Custom Scripts.Laa {0}'.format(_category)


def get_hotkey_from_name(name):
    return COMMANDS[name][HOTKEY]


def get_annotation_from_name(name):
    return name.title().replace('_', ' ')


def get_command_from_name(name):
    return 'import LaaScripts; LaaScripts.Trigger().{0}()'.format(name)


@dataclass
class Command:
    name: str = STRING.EMPTY
    category: str = STRING.EMPTY
    hotkey: str = STRING.EMPTY
    annotation: str = STRING.EMPTY
    command: str = STRING.EMPTY
    language: str = LANGUAGE


commands = {}

for cat in CATEGORIES.keys():
    for command_name in COMMANDS:
        category = get_category_from_name(command_name)
        hotkey = get_hotkey_from_name(command_name)
        annotation = get_annotation_from_name(command_name)
        command = get_command_from_name(command_name)
        commands[command_name] = Command(
            command_name,
            category,
            hotkey,
            annotation,
            command
        )

if __name__ == '__main__':
    print(PATH.PREFS_DIRS)
