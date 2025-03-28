from ..libs.blender_utils import get_edit_bone, select_bone, get_ops, deselect_bones

def roll (scene, config):
  deselect_bones()
  bone_name = config['name']
  bone = get_edit_bone(bone_name)

  if bone_name == 'mch_roll_side_01.l':
    value = (3.14159, 0, 0, 0)
  else:
    value = (0, 0, 0, 0)

  select_bone(bone)
  get_ops().transform.transform(mode = 'BONE_ROLL', value = value)
  deselect_bones()
