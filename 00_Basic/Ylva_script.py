import maya.cmds as mc

def createOffset(obj):
    groupOff = mc.group(em=True, name=obj + '_offset_CONS')
    mc.delete(mc.parentConstraint(obj, groupOff))
    groupPadre = mc.listRelatives(obj, parent=True)
    mc.parent(groupOff, groupPadre)
    mc.setAttr(groupOff + '.sx', 1)
    mc.setAttr(groupOff + '.sy', 1)
    mc.setAttr(groupOff + '.sz', 1)
    mc.setAttr(groupOff + '.rx', 0)
    mc.setAttr(groupOff + '.ry', 0)
    mc.setAttr(groupOff + '.rz', 0)
    mc.parent(obj, groupOff)
    return groupOff

# hips
mc.parentConstraint('Hips', createOffset('CN_Upperbody_CTRL'), mo=True)

# Spine
mc.orientConstraint('Spine', createOffset('CN_Spine_FK1_CTRL'), mo=True)
mc.orientConstraint('Spine1', createOffset('CN_Spine_FK2_CTRL'), mo=True)
mc.parentConstraint('Spine2', createOffset('CN_Chest_CTRL'), mo=True)

# Neck
mc.orientConstraint('Neck', createOffset('CN_Neck_JNT_ctrl'), mo=True)

# Head
mc.orientConstraint('Head', createOffset('Head_CTRL'), mo=True)

# Shoulders
mc.parentConstraint('LeftShoulder', createOffset('L_Clavicle_JNT_CTRL'), mo=True)
mc.parentConstraint('RightShoulder', createOffset('R_Clavicle_JNT_CTRL'), mo=True)

# Arms
mc.orientConstraint('LeftArm', createOffset('L_Shoulder_FK_CTRL'), mo=True)
mc.orientConstraint('RightArm', createOffset('R_Shoulder_FK_CTRL'), mo=True)

mc.orientConstraint('LeftForeArm', createOffset('L_Elbow_FK_CTRL'), mo=True)
mc.orientConstraint('RightForeArm', createOffset('R_Elbow_FK_CTRL'), mo=True)

mc.orientConstraint('LeftHand', createOffset('L_Hand_FK_CTRL'), mo=True)
mc.orientConstraint('RightHand', createOffset('R_Hand_FK_CTRL'), mo=True)

# Legs
mc.parentConstraint('LeftUpLeg', createOffset('L_Hip_FK_CTRL'), mo=True)
mc.parentConstraint('RightUpLeg', createOffset('R_Hip_FK_CTRL'), mo=True)

mc.orientConstraint('LeftLeg', createOffset('L_Knee_FK_CTRL'), mo=True)
mc.orientConstraint('RightLeg', createOffset('R_Knee_FK_CTRL'), mo=True)

mc.orientConstraint('LeftForeFoot', createOffset('L_Foot_FK_CTRL'), mo=True)
mc.orientConstraint('RightForeFoot', createOffset('R_Foot_FK_CTRL'), mo=True)

mc.orientConstraint('LeftToeBase', createOffset('L_Toe_JNT'), mo=True)
mc.orientConstraint('RightToeBase', createOffset('R_Toe_JNT'), mo=True)

# # hips
# mc.orientConstraint('Hips', 'CN_Upperbody_CTRL', mo=True)
#
# # Spine
# mc.orientConstraint('Spine', 'CN_Spine_FK1_CTRL', mo=True)
# mc.orientConstraint('Spine1', 'CN_Spine_FK2_CTRL', mo=True)
# mc.orientConstraint('Spine2', 'CN_Chest_CTRL', mo=True)
#
# # Neck
# mc.orientConstraint('Neck', 'CN_Neck_JNT_ctrl', mo=True)
#
# # Head
# mc.orientConstraint('Head', 'Head_CTRL', mo=True)
#
# # Shoulders
# mc.orientConstraint('LeftShoulder', 'L_Clavicle_JNT_CTRL', mo=True)
# mc.orientConstraint('RightShoulder', 'R_Clavicle_JNT_CTRL', mo=True)
#
# # Arms
# mc.orientConstraint('LeftArm', 'L_Shoulder_FK_CTRL', mo=True)
# mc.orientConstraint('RightArm', 'R_Shoulder_FK_CTRL', mo=True)
#
# mc.orientConstraint('LeftForeArm', 'L_Elbow_FK_CTRL', mo=True)
# mc.orientConstraint('RightForeArm', 'R_Elbow_FK_CTRL', mo=True)
#
# mc.orientConstraint('LeftHand', 'L_Hand_FK_CTRL', mo=True)
# mc.orientConstraint('RightHand', 'R_Hand_FK_CTRL', mo=True)
#
# # Legs
# mc.orientConstraint('LeftUpLeg', 'L_Hip_FK_CTRL', mo=True)
# mc.orientConstraint('RightUpLeg', 'R_Hip_FK_CTRL', mo=True)
#
# mc.orientConstraint('LeftLeg', 'L_Knee_FK_CTRL', mo=True)
# mc.orientConstraint('RightLeg', 'R_Knee_FK_CTRL', mo=True)
#
# mc.orientConstraint('LeftFoot', 'L_Foot_FK_CTRL', mo=True)
# mc.orientConstraint('RightFoot', 'R_Foot_FK_CTRL', mo=True)
#
# mc.orientConstraint('LeftToeBase', 'L_Toe_JNT', mo=True)
# mc.orientConstraint('RightToeBase', 'R_Toe_JNT', mo=True)