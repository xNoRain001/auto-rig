from ..libs.blender_utils import get_edit_bones

def rename_bones_for_mixamo ():
  name_map = {
    'def_hips': 'mixamorig:Hips',
    'def_spine_01': 'mixamorig:Spine',
    'def_spine_02': 'mixamorig:Spine1',
    'def_chest': 'mixamorig:Spine2',
    'def_shoulder.l': 'mixamorig:LeftShoulder',
    'def_neck': 'mixamorig:Neck',
    'def_head': 'mixamorig:Head', 
    'def_arm.l': 'mixamorig:LeftArm',
    'def_forearm.l': 'mixamorig:LeftForeArm',
    'def_hand.l': 'mixamorig:LeftHand',
    'def_thumb_01.l': 'mixamorig:LeftHandThumb1',
    'def_thumb_02.l': 'mixamorig:LeftHandThumb2',
    'def_thumb_03.l': 'mixamorig:LeftHandThumb3',
    'def_finger_a_01.l': 'mixamorig:LeftHandIndex1',
    'def_finger_a_02.l': 'mixamorig:LeftHandIndex2',
    'def_finger_a_03.l': 'mixamorig:LeftHandIndex3',
    'def_finger_b_01.l': 'mixamorig:LeftHandMiddle1',
    'def_finger_b_02.l': 'mixamorig:LeftHandMiddle2',
    'def_finger_b_03.l': 'mixamorig:LeftHandMiddle3',
    'def_finger_c_01.l': 'mixamorig:LeftHandRing1',
    'def_finger_c_02.l': 'mixamorig:LeftHandRing2',
    'def_finger_c_03.l': 'mixamorig:LeftHandRing3',
    'def_finger_d_01.l': 'mixamorig:LeftHandPinky1',
    'def_finger_d_02.l': 'mixamorig:LeftHandPinky2',
    'def_finger_d_03.l': 'mixamorig:LeftHandPinky3',
    'def_leg.l': 'mixamorig:LeftUpLeg',
    'def_shin.l': 'mixamorig:LeftLeg',
    'def_foot.l': 'mixamorig:LeftFoot',
    'def_toes.l': 'mixamorig:LeftToeBase',
  } 

  bones = get_edit_bones()

  for bone in bones:
    bone_name = bone.name

    if bone_name in name_map:
      new_name = name_map[bone_name]
      bone.name = new_name

      if '.l' in bone_name:
        mirror_name = bone_name.replace('.l', '.r')
        bones[mirror_name].name = new_name.replace('Left', 'Right')
        