from ..libs.blender_utils import calculate_roll, get_edit_bone, deselect_bones

def cal_roll (scene, config):
  deselect_bones()
  bone_name = config['name']

  if bone_name == 'mch_roll_side_01.l':
    v = 'GLOBAL_POS_Y'
  else:
    v = 'GLOBAL_POS_Z'

  bone = get_edit_bone(bone_name)
  calculate_roll(bone, v)
  deselect_bones()
