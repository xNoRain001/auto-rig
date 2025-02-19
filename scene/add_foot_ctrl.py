from ..libs.blender_utils import add_scene_custom_prop

def add_foot_ctrl ():
  common = { 'size': 3, 'subtype': 'COORDINATES' }
  add_scene_custom_prop('side_01_head_location', 'FloatVector', **common)
  add_scene_custom_prop('side_02_head_location', 'FloatVector', **common)
  add_scene_custom_prop('heel_location', 'FloatVector', **common)
  add_scene_custom_prop('foot_tip_location', 'FloatVector', **common)
  