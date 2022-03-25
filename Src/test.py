# toggleChannelBoxTimelineSync
import maya.cmds as cmd
import maya.mel as mel

print cmd.menuItem('cbTimelineSyncMenu', checkBox=True, query=True)


# state = (str(not cmd.menuItem('cbTimelineSyncMenu', checkBox=True, query=True))).lower()
#
# mel.eval('toggleChannelBoxTimelineSync {0};'.format(state))
# mel.eval('toggleChannelBoxGraphEdSync {0};'.format(state))
#
# state = cmd.menuItem('cbTimelineSyncMenu', checkBox=True, query=True)
#         if state:
#             # Turn Sync Off
#             mel.eval('toggleChannelBoxTimelineSync true;')
#             mel.eval('toggleChannelBoxGraphEdSync true;')
#             return True
#         else:
#             # Turn Sync On
#             mel.eval('toggleChannelBoxTimelineSync false;')
#             mel.eval('toggleChannelBoxGraphEdSync false;')
#             return False

#
# cmd.menuItem('cbTimelineSyncMenu', checkBox=True, edit=True)
# print state


        # mel.eval('toggleChannelBoxTimelineSync {0};'.format(not state))
        # mel.eval('toggleChannelBoxGraphEdSync {0};'.format(not state))
        # info.show_info('SYNC: {0}'.format(not state))