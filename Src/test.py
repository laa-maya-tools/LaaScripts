def list_anim_channels(selected_objects):
    if not selected_objects:
        return
    if len(selected_objects) == 1:
        anim_attrs = cmd.listAnimatable(selected_objects[0])
        return [attr.split('.')[-1] for attr in anim_attrs]

    anim_attrs = cmd.listAnimatable(selected_objects)
    anim_channels = list(set([attr.split('.')[-1] for attr in anim_attrs]))
    for object in selected_objects:
        for channel in anim_channels:
            full_attr = '{0}.{1}'.format(object, channel)
            if not cmd.objExists(full_attr):
                anim_channels.remove(channel)
    return anim_channels


    # return anim_channels
    # for attr in anim_attrs:
    #
    # anim_channels = [attr.split('.')[-1] for attr in anim_attrs]
    # return anim_channels

    # anim_attrs = cmd.listAnimatable(selected_objects)
    # anim_channels = [attr.split('.')[-1] for attr in anim_attrs]
    # return anim_channels

# def list_common_channels():
#     if not selected_objects:
#         return
#     if len(selected_objects) == 1:
#         anim_attrs = cmd.listAnimatable(selected_objects[0])
#         anim_channels = anim_attrs.en
#         return cmd.listAnimatable(selected_objects[0]) cb_channel.endswith(attr)
#
#
# import maya.cmds as cmd
# all_attrs = []
# anim_attrs = []

selected_objects = cmd.ls(sl=True)
# anim_attrs = anim_attrs + cmd.listAnimatable(selected_objects)
print list_anim_channels(selected_objects)

# selected_objects = cmd.ls(sl=True)
# for object in selected_objects:
#     all_attrs = all_attrs + '{0}.{1}'.format(object, cmd.listAttr(object))
#     anim_attrs = anim_attrs + cmd.listAnimatable(object)
#
# print all_attrs, anim_attrs


# all_channels = cmd.listAttr(selected_objects)
# cb_channels = cmd.listAnimatable(selected_objects)
#     all_attrs = cmds.listAttr(obj, se=True, sn=True)
# # intersect = list(set(all_channels) & set(cb_channels))
# # print intersect
# print all_channels


# def list_all_channels(selected_objects):
#     if not selected_objects:
#         return
#
#     channels = []
#     all_channels = cmd.listAttr(selected_objects)
#     cb_channels = cmd.listAnimatable(selected_objects)
#
#     if all_channels and cb_channels:
#         channels = [channel for channel in all_channels for cb_channel in cb_channels if cb_channel.endswith(attr)]
#
#     return list(set(channels))
#
#
# def select_common_channels(selected_objects):
#     channels = list_all_channels(selected_objects)
#     attributes = []
#
#     for object in selected_objects:
#         full_attr = '{0}.{1}'.format(object, channels)
#         if not cmd.objExists(full_attr):
#             channels.remove(full_attr)
#
#
# selected_objects = cmd.ls(sl=True)
# select_common_channels(selected_objects)


# for obj in selected_objects:
#     full_attr = '{0}.{1}'.format(obj, channel)
#     if cmd.objExists(full_attr):


#
# for obj in selected_objects:
#


    # for channel in channels:
    #     print channel
    #     full_attr = '{0}.{1}'.format(obj, channel)
    #     if cmd.objExists(full_attr):
    #         attributes.append(full_attr)
    # cmd.channelBox('mainChannelBox', e=True, select=attributes)
    # intersection = [item for item in list1 if item in list2]
#
# print set(attributes)
# # cmd.channelBox('mainChannelBox', e=True, select=attributes)