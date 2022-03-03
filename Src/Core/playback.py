"""
=============================================================================
MODULE: playback_tools.py
-----------------------------------------------------------------------------
Add extra functionality to Maya's playback. This module must be used by the
trigger module, SHOULD NOT BE USED DIRECTLY.
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2018 | Python 2
=============================================================================
"""
from .._Utils import info
from .._Utils import utils as utl
from .._Data import user_data as usd
from .._Constants import constants as cns

reload(info)
reload(utl)
reload(usd)
reload(cns)


class Playback(object):

    def __init__(self):
        self._utils = utl.Utils()
        self._user_data = usd.UserData().read_user_data()

    # ============================================================================= #
    # GO TO THE NEXT FRAME                                                          #
    # ============================================================================= #
    def go_to_the_next_frame(self):
        i = self._user_data[cns.TIME_INCREMENT]
        playback_start_time = self._utils.get_playback_range()[0]
        playback_end_time = self._utils.get_playback_range()[1]
        animation_end_time = self._utils.get_animation_range()[1]
        next_time = self._utils.get_current_time() + i

        if self._user_data[cns.INFO_ENABLED]:
            info.show_info('Next Frame >> {0}F'.format(int(next_time)))
        if self._user_data[cns.PLAYBACK_MODE] == cns.LOOP:
            if next_time > playback_end_time:
                next_time = playback_start_time
        elif self._user_data[cns.PLAYBACK_MODE] == cns.STOP:
            if next_time > playback_end_time:
                return
        elif self._user_data[cns.PLAYBACK_MODE] == cns.MOVE:
            if next_time > animation_end_time:
                return
            if next_time > playback_end_time:
                self._utils.set_playback_range(playback_start_time + i, playback_end_time + i)
        elif self._user_data[cns.PLAYBACK_MODE] == cns.EXPAND:
            if next_time > animation_end_time:
                return
            if next_time > playback_end_time:
                self._utils.set_playback_range(playback_start_time, playback_end_time + i)
        else:
            if self._user_data[cns.WARNINGS_ENABLED]:
                info.show_info('{0} is not a valid playback mode!'.format(self._user_data[cns.PLAYBACK_MODE].upper()), True, 2000)

        cmd.undoInfo(stateWithoutFlush=False)
        self._utils.set_current_time(next_time)
        cmd.undoInfo(stateWithoutFlush=True)


