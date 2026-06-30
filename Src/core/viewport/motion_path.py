# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: motion_path.py
-----------------------------------------------------------------------------
Draws a motion trail on the viewport showing the selected object's animation
path. A small sphere marks every frame and a larger sphere highlights each
keyframe, connected by a degree-1 NURBS backbone curve.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2022+ | Python 3
=============================================================================
"""
import maya.cmds as cmd  # type: ignore[import]

from LaaScripts.Src.utils.scene import info_utils as info
from LaaScripts.Src.utils.animation.timeline_utils import TimelineUtils
from LaaScripts.Src.utils.scene.selection_utils import SelectionUtils


# -----------------------------------------------------------------------------
# TRAIL IDENTITY
# -----------------------------------------------------------------------------
TRAIL_GROUP = 'LaaMotionTrail_Grp'
TRAIL_CURVE = 'LaaMotionTrail_Crv'
FRAME_MARKER_GROUP = 'LaaMotionTrail_FrameMarkers_Grp'
KEYFRAME_MARKER_GROUP = 'LaaMotionTrail_KeyframeMarkers_Grp'

FRAME_SHADER = 'LaaMotionTrail_FrameShader'
KEYFRAME_SHADER = 'LaaMotionTrail_KeyframeShader'
FRAME_TEMPLATE = 'LaaMotionTrail_FrameTemplate'
KEYFRAME_TEMPLATE = 'LaaMotionTrail_KeyframeTemplate'

TRAIL_COLOR = 6                          # Maya override color index (6 = blue)
FRAME_COLOR = (0.0, 0.40, 0.87)         # RGB blue for frame markers
KEYFRAME_COLOR = (1.0, 0.82, 0.09)      # RGB amber for keyframe markers

FRAME_RADIUS = 0.10                      # Small sphere for every frame
KEYFRAME_RADIUS = 0.35                   # Larger sphere for keyframes


class MotionPath(object):
    """
    Draws a motion trail in the viewport showing the animation path of the
    selected object.

    Every frame gets a small sphere marker; keyframes receive a larger,
    differently-colored sphere. A degree-1 NURBS curve runs through all
    positions as a visual backbone.

    Usage:
        mp = MotionPath()
        mp.toggle_trail()   # toggle on/off
    """

    def __init__(self):
        self._enabled = False
        self._target = None
        self._job_id = None

    # -------------------------------------------------------------------------
    # PUBLIC API
    # -------------------------------------------------------------------------
    def create_trail(self):
        """
        Creates a motion trail for the selected object.
        """
        selection = SelectionUtils.list_selected_objects()
        if not selection:
            info.show_info('No Object Selected', warning=True)
            return

        self._target = selection[0]
        self._enabled = True
        self._build_trail()
        self._register_callback()
        info.show_info('Motion Trail Created')

    def remove_trail(self):
        """
        Removes the motion trail from the viewport.
        """
        self._unregister_callback()
        self._delete_trail_nodes()
        self._enabled = False
        self._target = None
        info.show_info('Motion Trail Removed')

    def toggle_trail(self):
        """
        Toggles the motion trail on or off.
        """
        if self._enabled:
            self.remove_trail()
        else:
            self.create_trail()

    # -------------------------------------------------------------------------
    # TRAIL BUILDING
    # -------------------------------------------------------------------------
    def _build_trail(self):
        """
        Orchestrates the full trail build: sample positions, create the
        backbone curve, then place frame and keyframe markers.
        """
        playback_range = TimelineUtils.get_playback_range()
        start, end = int(playback_range[0]), int(playback_range[1])

        positions = self._sample_world_positions(start, end)
        if not positions:
            info.show_info('Could Not Sample Positions', warning=True)
            return

        key_times = self._get_keyframe_times()
        keyframe_indices = {
            t - start for t in key_times if start <= t <= end
        }

        self._create_trail_curve(positions)
        self._create_frame_markers(positions, start, keyframe_indices)
        self._create_keyframe_markers(key_times, keyframe_indices)

    def _sample_world_positions(self, start, end):
        """
        Samples the world position of the target object at every frame
        in the given range without changing the current time.

        :param int start: Start frame.
        :param int end: End frame.
        :return: List of [x, y, z] world-space positions.
        :rtype: list
        """
        positions = []
        for frame in range(start, end + 1):
            pos = cmd.getAttr(self._target + '.worldMatrix', time=frame)
            positions.append([pos[12], pos[13], pos[14]])
        return positions

    def _get_keyframe_times(self):
        """
        Returns the sorted unique keyframe times for the target object.

        :return: List of keyframe times.
        :rtype: list
        """
        key_times = cmd.keyframe(self._target, q=True, timeChange=True) or []
        return sorted(set(int(t) for t in key_times))

    # -------------------------------------------------------------------------
    # CURVE
    # -------------------------------------------------------------------------
    def _create_trail_curve(self, positions):
        """
        Creates a degree-1 NURBS curve through all sampled positions as
        the visual backbone of the trail.

        :param list positions: List of world-space positions.
        """
        self._delete_trail_nodes()

        if not cmd.objExists(TRAIL_GROUP):
            cmd.group(em=True, n=TRAIL_GROUP)
        cmd.setAttr(TRAIL_GROUP + '.hiddenInOutliner', 1)

        curve = cmd.curve(p=positions, degree=1, n=TRAIL_CURVE)
        cmd.parent(curve, TRAIL_GROUP)

        cmd.setAttr(curve + '.overrideEnabled', 1)
        cmd.setAttr(curve + '.overrideColor', TRAIL_COLOR)
        cmd.setAttr(curve + '.lineWidth', 2.0)

        # Reference display on the curve only — keeps it non-selectable.
        # Marker groups stay in normal rendering so their shaders show.
        self._set_reference_display(curve)

    # -------------------------------------------------------------------------
    # FRAME MARKERS (every frame — small sphere)
    # -------------------------------------------------------------------------
    def _create_frame_markers(self, positions, start_frame, keyframe_indices):
        """
        Places a small sphere marker at every frame position.
        Keyframe positions are skipped here (handled separately with larger
        markers). Uses instanced duplication so all markers share a single
        shape node.

        :param list positions: List of [x, y, z] positions.
        :param int start_frame: The frame number of the first position.
        :param set keyframe_indices: Indices of positions that are keyframes.
        """
        if not cmd.objExists(FRAME_MARKER_GROUP):
            cmd.group(em=True, n=FRAME_MARKER_GROUP)
        cmd.parent(FRAME_MARKER_GROUP, TRAIL_GROUP)
        cmd.setAttr(FRAME_MARKER_GROUP + '.hiddenInOutliner', 1)

        shader = self._get_or_create_shader(FRAME_SHADER, FRAME_COLOR)
        template = self._get_or_create_template(
            FRAME_TEMPLATE, FRAME_RADIUS, TRAIL_GROUP
        )

        for i, pos in enumerate(positions):
            if i in keyframe_indices:
                continue  # keyframes get their own larger marker

            frame_num = start_frame + i
            marker = cmd.duplicate(
                template,
                n='LaaMotionTrail_F_{0}'.format(frame_num),
                instanceLeaf=True,
            )[0]
            cmd.xform(marker, ws=True, t=pos)
            cmd.parent(marker, FRAME_MARKER_GROUP)
            self._assign_shader(marker, shader)

    # -------------------------------------------------------------------------
    # KEYFRAME MARKERS (keyframes only — large sphere)
    # -------------------------------------------------------------------------
    def _create_keyframe_markers(self, key_times, keyframe_indices):
        """
        Places a larger sphere marker at each keyframe position.
        Uses instanced duplication for efficiency.

        :param list key_times: List of keyframe times.
        :param set keyframe_indices: Set of position indices that are keyframes
            (unused here; kept for symmetry).
        """
        if not key_times:
            return

        if not cmd.objExists(KEYFRAME_MARKER_GROUP):
            cmd.group(em=True, n=KEYFRAME_MARKER_GROUP)
        cmd.parent(KEYFRAME_MARKER_GROUP, TRAIL_GROUP)
        cmd.setAttr(KEYFRAME_MARKER_GROUP + '.hiddenInOutliner', 1)

        shader = self._get_or_create_shader(KEYFRAME_SHADER, KEYFRAME_COLOR)
        template = self._get_or_create_template(
            KEYFRAME_TEMPLATE, KEYFRAME_RADIUS, TRAIL_GROUP
        )

        for t in key_times:
            pos = cmd.getAttr(self._target + '.worldMatrix', time=t)
            marker = cmd.duplicate(
                template,
                n='LaaMotionTrail_KF_{0}'.format(int(t)),
                instanceLeaf=True,
            )[0]
            cmd.xform(marker, ws=True, t=[pos[12], pos[13], pos[14]])
            cmd.parent(marker, KEYFRAME_MARKER_GROUP)
            self._assign_shader(marker, shader)

    # -------------------------------------------------------------------------
    # SHADER & TEMPLATE HELPERS
    # -------------------------------------------------------------------------
    @staticmethod
    def _get_or_create_shader(name, color):
        """
        Returns (and creates if needed) a Lambert shader with its shading group.

        :param str name: Shader node name.
        :param tuple color: (R, G, B) float values.
        :return: Shader name.
        :rtype: str
        """
        if cmd.objExists(name):
            return name

        shader = cmd.shadingNode('lambert', asShader=True, n=name)
        cmd.setAttr(shader + '.color', *color, type='double3')
        cmd.setAttr(shader + '.diffuse', 0.8)
        cmd.setAttr(shader + '.ambientColor', 0.3, 0.3, 0.3, type='double3')

        # Create a shading group so the shader is ready to assign
        sg = cmd.sets(
            renderable=True, noSurfaceShader=True, empty=True,
            name=name + 'SG',
        )
        cmd.connectAttr(shader + '.outColor', sg + '.surfaceShader', force=True)
        return shader

    @staticmethod
    def _assign_shader(obj, shader):
        """
        Assigns a shader to an object via its shading group.

        :param str obj: Object name.
        :param str shader: Shader name.
        """
        sg = shader + 'SG'
        if cmd.objExists(sg):
            cmd.sets(obj, edit=True, forceElement=sg)

    @staticmethod
    def _get_or_create_template(name, radius, parent):
        """
        Returns (and creates if needed) a hidden template sphere used as the
        source for instanced duplication.

        :param str name: Template node name.
        :param float radius: Sphere radius.
        :param str parent: Parent group name.
        :return: Template transform name.
        :rtype: str
        """
        if cmd.objExists(name):
            return name

        template = cmd.sphere(n=name, r=radius, ch=False)[0]
        cmd.parent(template, parent)
        cmd.setAttr(template + '.visibility', 0)
        return template

    @staticmethod
    def _set_reference_display(node):
        """
        Sets the node to reference display type: fully shaded and visible,
        but non-selectable and non-renderable.

        :param str node: Node name.
        """
        cmd.setAttr(node + '.overrideEnabled', 1)
        cmd.setAttr(node + '.overrideDisplayType', 2)  # 2 = reference

    # -------------------------------------------------------------------------
    # TRAIL CLEANUP
    # -------------------------------------------------------------------------
    def _delete_trail_nodes(self):
        """
        Removes all trail geometry from the scene.
        """
        for node in (TRAIL_GROUP,):
            if cmd.objExists(node):
                cmd.delete(node)

    # -------------------------------------------------------------------------
    # CALLBACK MANAGEMENT
    # -------------------------------------------------------------------------
    def _register_callback(self):
        """
        Registers a scriptJob to rebuild the trail when the playback range
        changes.
        """
        self._unregister_callback()

        self._job_id = cmd.scriptJob(
            event=['playbackRangeChanged', self._on_range_changed],
            killWithScene=False,
        )

    def _unregister_callback(self):
        """
        Removes the scriptJob if it exists.
        """
        if self._job_id is not None:
            if cmd.scriptJob(exists=self._job_id):
                cmd.scriptJob(kill=self._job_id, force=True)
            self._job_id = None

    def _on_range_changed(self):
        """
        Callback: rebuilds the trail when the playback range is modified.
        """
        if not self._enabled or self._target is None:
            return
        if not cmd.objExists(self._target):
            self.remove_trail()
            return
        self._build_trail()
