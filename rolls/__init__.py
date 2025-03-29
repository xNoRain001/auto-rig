from ..libs.blender_utils import (
  set_mode,
  get_edit_bone, 
  calculate_roll, 
  symmetrize_bones, 
  get_active_object
)

def init_roll_config ():
  config = []
  roll_map = {
    'GLOBAL_NEG_Z': [
      'def_hips', 'def_spine_01', 'def_spine_02', 'def_chest', 'def_neck', 'def_head'
    ],
    'GLOBAL_POS_Y': ['def_leg.l', 'def_shin.l'],
    'GLOBAL_POS_Z': ['def_foot.l', 'def_toes.l'],
    'GLOBAL_NEG_X': [
      'def_shoulder.l', 'def_arm.l', 'def_forearm.l', 'def_hand.l',
      'def_arm_01.l', 'def_arm_02.l',
      'def_finger_a_01.l', 'def_finger_a_02.l', 'def_finger_a_03.l',
      'def_finger_b_01.l', 'def_finger_b_02.l', 'def_finger_b_03.l',
      'def_finger_c_01.l', 'def_finger_c_02.l', 'def_finger_c_03.l',
      'def_finger_d_01.l', 'def_finger_d_02.l', 'def_finger_d_03.l',
    ],
    'GLOBAL_NEG_Y': ['def_thumb_01.l', 'def_thumb_02.l', 'def_thumb_03.l']
  }

  for type, bone_names in roll_map.items():
    for bone_name in bone_names:
      config.append({
        'name': bone_name,
        'type': type
      })

  return config

def init_rolls ():
  roll_config = init_roll_config()
  bone_names = []

  for config in roll_config:
    name = config['name']
    type = config['type']
    bone = get_edit_bone(name)
    bone_names.append(name)
    calculate_roll(bone, type)

  symmetrize_bones(bone_names)
