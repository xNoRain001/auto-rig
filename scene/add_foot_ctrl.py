from ..libs.blender_utils import add_scene_custom_prop

def add_foot_ctrl ():
  common = { 'size': 3, 'subtype': 'COORDINATES', 'precision': 5 }
  add_scene_custom_prop(
    'side_01_head_location', 
    'FloatVector', 
    default = (0.0293, -0.0587, 0.0053),
    **common
  )
  add_scene_custom_prop(
    'side_02_head_location', 
    'FloatVector', 
    default = (0.09323, -0.05679, -0.00710), 
    **common
  )
  add_scene_custom_prop(
    'heel_location', 
    'FloatVector', 
    default = (0.04542, 0.03530, -0.00628), 
    **common
  )
  add_scene_custom_prop(
    'foot_tip_location', 
    'FloatVector', 
    default = (0.06759, -0.17093, -0.00710), 
    **common
  )
  