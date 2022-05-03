from PySide2 import QtWidgets as wdg
from PySide2 import QtGui as gui
from PySide2 import QtCore as cor

# =============================================================================
# MAYA CONTROLS CONSTANTS
# =============================================================================
TIME_CONTROL = "$gPlayBackSlider"
SHELF = "$gShelfTopLevel"
STATUS_LINE = "$gStatusLine"
ATTRIBUTE_EDITOR = "$gAttributeEditorWindowName"
CHANNELS_BOX = "$gChannelBoxName"
TOOLBOX = "$gToolBox"
COMMAND_LINE = "$gCommandLine"
RANGE_SLIDER = "$gTimeRangeSlider"
HELP_LINE = "$gHelpLineForm"

# =============================================================================
# LISTS
# =============================================================================
EMPTY_LIST = []

# =============================================================================
# PLAYBACK
# =============================================================================
FRAMES, TYPES = 'frames', 'types'
KEY, BREAKDOWN, INBETWEEN, ALL = 0, 1, 2, 3
MARKER_TYPE_NAMES = {KEY: 'Key', BREAKDOWN: 'Breakdown', INBETWEEN: 'Inbetween'}
INDEX, FRAME, TYPE = 0, 1, 2
RANGE, COLOR = 0, 1
TIMEOUT = 150
SECTION_RANGES, SECTION_COLORS = 'ranges', 'colors'

# =============================================================================
# COLORS
# =============================================================================
DARK, MEDIUM, LIGHT = 0, 1, 2
RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, DARK_GREY, LIGHT_GREY = 0, 1, 2, 3, 4, 5, 6, 7, 8
COLORS = {
    RED: {
        DARK: gui.QColor('#FF3B3B'),
        MEDIUM: gui.QColor('#FF5C5C'),
        LIGHT: gui.QColor('#FF8080')
    },
    ORANGE: {
        DARK: gui.QColor('#FE8801'),
        MEDIUM: gui.QColor('#FDAC41'),
        LIGHT: gui.QColor('#FCCC76')
    },
    YELLOW: {
        DARK: gui.QColor('#FFCB00'),
        MEDIUM: gui.QColor('#FEDD4B'),
        LIGHT: gui.QColor('#FEED73')
    },
    GREEN: {
        DARK: gui.QColor('#05C270'),
        MEDIUM: gui.QColor('#39DA8A'),
        LIGHT: gui.QColor('#57EBA3')
    },
    CYAN: {
        DARK: gui.QColor('#00CFDD'),
        MEDIUM: gui.QColor('#74E0E6'),
        LIGHT: gui.QColor('#A9EFF3')
    },
    BLUE: {
        DARK: gui.QColor('#0063F8'),
        MEDIUM: gui.QColor('#5B8DEE'),
        LIGHT: gui.QColor('#9DBFF8')
    },
    PURPLE: {
        DARK: gui.QColor('#6500CD'),
        MEDIUM: gui.QColor('#AC5CD9'),
        LIGHT: gui.QColor('#DEA5E8')
    },
    DARK_GREY: {
        DARK: gui.QColor('#28293D'),
        MEDIUM: gui.QColor('#555870'),
        LIGHT: gui.QColor('#9090A7')
    },
    LIGHT_GREY: {
        DARK: gui.QColor('#EBEAEF'),
        MEDIUM: gui.QColor('#F2F2F4'),
        LIGHT: gui.QColor('#FAFAFC')
    }
}

# =============================================================================
# KEYFRAMES
# =============================================================================
NEXT, PREVIOUS, FIRST, LAST = 'next', 'previous', 'first', 'last'

# =============================================================================
# INFO UTILS CONSTANTS
# =============================================================================
INFO_HEIGHT, INFO_WIDTH, INFO_X_OFFSET, INFO_Y_OFFSET = 38, 360, 90, 378
MODEL_PANEL, GRAPH_EDITOR, SCRIPT_EDITOR = 'modelPanel', 'graphEditor', 'scriptEditor'

# =============================================================================
# USER DATA CONSTANTS
# =============================================================================
INFO_ENABLED = 'info_enabled'
WARNINGS_ENABLED = 'warnings_enabled'
PLAYBACK_MODE = 'playback_mode'
LOOP, STOP, PASS, EXPAND = 'loop', 'stop', 'pass', 'expand'
TIME_INCREMENT = 'time_increment'

# =============================================================================
# NAVIGATION
# =============================================================================
MOVE, ROTATE, SCALE = 'Move', 'Rotate', 'Scale'
LOCAL, WORLD, NORMAL, GIMBAL, PARENT, COMPONENT = 'Local', 'World', 'Normal', 'Gimbal', 'Parent', 'Component'
TX, TY, TZ, RX, RY, RZ, SX, SY, SZ = 'tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz'
TRS_XYZ = ['tx', 'ty', 'tz']
ROT_XYZ = ['rx', 'ry', 'rz']
SCL_XYZ = ['sx', 'sy', 'sz']
NAME, INDEX = 0, 1

# =============================================================================
# TIMELINE
# =============================================================================
ANIMATION, PLAYBACK = 0, 1
ALL_RANGE, BEFORE_CURRENT_TIME, AFTER_CURRENT_TIME = 0, 1, 2
START_TIME, END_TIME = 0, 1
NEXT, PREVIOUS, FIRST, LAST = 'next', 'previous', 'first', 'last'

# =============================================================================
# NODES
# =============================================================================
VERSION = 'LaaScripts v1.0.0'
ICON = 'icon'

LAA_SCRIPTS_NODE = 'LaaScripts'

NAVIGATION_NODE = 'LaaScripts|Navigation'
KEYFRAMING_NODE = 'LaaScripts|Keyframing'
TRANSFORM_NODE = 'LaaScripts|Transform'
SELECTION_NODE = 'LaaScripts|Selection'
CONTROLS_SELECTOR_NODE = 'LaaScripts|Selection|ControlsSelector'
VIEWPORT_NODE = 'LaaScripts|Viewport'
PLAYBACK_NODE = 'LaaScripts|Playback'
FRAME_MARKER_NODE = 'LaaScripts|Playback|FrameMarker'
TIMELINE_SECTION_NODE = 'LaaScripts|Playback|TimelineSection'

VERSION_ATTR = 'version'
ICON_ATTR = 'icon'
PARENT_ATTR = 'parent'

KEY_MARKERS_ATTR = 'key_markers'
FRAME_MARKERS_ATTR = 'frame_markers'
TIMELINE_SECTION_ATTR = 'timeline_section'

