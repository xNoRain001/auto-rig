from ..libs.blender_utils import (
  get_edit_bone, 
  calculate_roll, 
  symmetrize_bones, 
)

def init_bones_roll (config):
  bone_names = []

  for roll_type, roll_bone_names in config.items():
    for bone_name in roll_bone_names:
      bone = get_edit_bone(bone_name)
      bone_names.append(bone_name)
      calculate_roll(bone, roll_type)

  symmetrize_bones(bone_names)
