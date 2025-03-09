from ..libs.blender_utils import add_scene_custom_prop

def add_foot_ctrl ():
  # , 
  common = { 'size': 3, 'subtype': 'COORDINATES', 'precision': 5 }
  # 如果名字叫做 side_01_head_location 只会显示 x，非常奇怪的问题
  add_scene_custom_prop(
    'side_01_head_location_', 
    'FloatVector', 
    # default = (0.03, -0.06, 0.00528),
    default = (0.0293, -0.0587, 0.0053),
    **common
  )
  add_scene_custom_prop('side_02_head_location', 'FloatVector', default = (0.08, -0.05, 0.00673), **common)
  add_scene_custom_prop('heel_location', 'FloatVector', default = (0.04, 0.04, 0.00562), **common)
  add_scene_custom_prop('foot_tip_location', 'FloatVector', default = (0.06, -0.13, 0.0062), **common)
  