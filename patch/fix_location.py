from ..libs.blender_utils import (
  snap_cursor, 
  deselect_bones, 
  select_bone_tail,
  select_bone_head,
  get_edit_bone,
  snap_selected_to_cursor
)

v_map = {
  'mch_foot_roll.l': [['tail', 'heel_location']],
  'ik_foot.l': [['head', 'foot_tip_location']],
  'mch_roll_side_01.l': [
    ['head', 'side_01_head_location_'],
    ['tail', 'side_02_head_location'],
  ]
}

def fix_location (scene, config):
  deselect_bones()
  bone_name = config['name']
  bone = get_edit_bone(bone_name)

  list = v_map[bone_name]
  for item in list:
    head_or_tail, var = item

    if head_or_tail == 'head':
      select_bone_head(bone)
    else:
      select_bone_tail(bone)

    snap_cursor(getattr(scene, var))
    snap_selected_to_cursor()
    deselect_bones()
