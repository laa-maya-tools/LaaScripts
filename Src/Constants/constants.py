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
# PLAYBACK
# =============================================================================
FRAMES, TYPES = 'frames', 'types'
KEY, BREAKDOWN, INBETWEEN, ALL = 0, 1, 2, 3
MARKER_TYPE_NAMES = {KEY: 'Key', BREAKDOWN: 'Breakdown', INBETWEEN: 'Inbetween'}
INDEX, FRAME, TYPE = 0, 1, 2

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

VERSION_ATTR = 'version'
ICON_ATTR = 'icon'
PARENT_ATTR = 'parent'

KEY_MARKERS_ATTR = 'key_markers'
FRAME_MARKERS_ATTR = 'frame_markers'

