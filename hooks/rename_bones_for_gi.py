from ..libs.blender_utils import get_edit_bones

def rename_bones_for_gi ():
  name_map = {
    'Bip001': 'root',
    '+PelvisTwist CF A01': 'def_hips',
    'Bip001 Spine': 'def_spine_01',
    'Bip001 Spine1': 'def_spine_02',
    'Bip001 Spine2': 'def_chest',
    'Bip001 L Clavicle': 'def_shoulder.l',
    'Bip001 Neck': 'def_neck',
    'Bip001 Head': 'def_head', 
    'Bip001 L UpperArm': 'def_arm.l',
    '+UpperArmTwist L A01': 'def_arm_01.l',
    '+UpperArmTwist L A02': 'def_arm_02.l',
    'Bip001 L Forearm': 'def_forearm.l',
    '+ForeArmTwistS L A01': 'def_forearm_01.l',
    '+ForeArmTwistS L A02': 'def_forearm_02.l',
    'Bip001 L Hand': 'def_hand.l',
    'Bip001 L Finger0': 'def_thumb_01.l',
    'Bip001 L Finger01': 'def_thumb_02.l',
    'Bip001 L Finger02': 'def_thumb_03.l',
    'DMZ L 01': 'def_thumb_01.l',
    'DMZ L 02': 'def_thumb_02.l',
    'DMZ L 03': 'def_thumb_03.l',
    'Bip001 L Finger1': 'def_finger_a_01.l',
    'Bip001 L Finger11': 'def_finger_a_02.l',
    'Bip001 L Finger12': 'def_finger_a_03.l',
    'Bip001 L Finger2': 'def_finger_b_01.l',
    'Bip001 L Finger21': 'def_finger_b_02.l',
    'Bip001 L Finger22': 'def_finger_b_03.l',
    'Bip001 L Finger3': 'def_finger_c_01.l',
    'Bip001 L Finger31': 'def_finger_c_02.l',
    'Bip001 L Finger32': 'def_finger_c_03.l',
    'Bip001 L Finger4': 'def_finger_d_01.l',
    'Bip001 L Finger41': 'def_finger_d_02.l',
    'Bip001 L Finger42': 'def_finger_d_03.l',
    'Bip001 L Thigh': 'def_leg.l',
    'Bip001 L Calf': 'def_shin.l',
    'Bip001 L Foot': 'def_foot.l',
    'Bip001 L Toe0': 'def_toes.l',
    # '+EyeBone L A01': 'def_eye.l', 
    # '+Breast L A01': 'def_breast.l',
  } 

  bones = get_edit_bones()

  for bone in bones:
    bone_name = bone.name

    if bone_name in name_map:
      new_name = name_map[bone_name]
      bone.name = new_name

      if ' L ' in bone_name:
        mirror_name = bone_name.replace(' L ', ' R ')
        bones[mirror_name].name = new_name.replace('.l', '.r')
        