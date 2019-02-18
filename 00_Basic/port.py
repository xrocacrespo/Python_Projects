import maya.cmds as cmds
if not cmds.commandPort(':8290', q=True):
    cmds.commandPort(n=':8290')