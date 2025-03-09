from ..libs.blender_utils import select_bone, get_edit_bone, get_ops, deselect_bones

def pole_target (scene, config):
  deselect_bones()
  bone_name = config['name']
  pole_target_type = 'leg' if bone_name.endswith('_leg.l.001') else 'arm'
  select_bone(get_edit_bone(bone_name))
  normal = scene.leg_pole_normal if pole_target_type == 'leg' else scene.arm_pole_normal
  # normal 是字符串
  flag = 1 if len(normal) == 1 else -1
  direction = normal if len(normal) == 1 else normal[1]
  if direction == 'X':
    get_ops().transform.translate(value = (0.5 * flag, 0, 0), orient_type = 'NORMAL')
  else:
    get_ops().transform.translate(value = (0, 0, 0.5 * flag), orient_type = 'NORMAL')

  deselect_bones()
