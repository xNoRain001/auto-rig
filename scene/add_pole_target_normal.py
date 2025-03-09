from ..libs.blender_utils import add_scene_custom_prop
  
def add_pole_target_normal ():
  items = [
    ('X', "X", ""),
    ('-X', "-X", ""),
    ('Z', "Z", ""),
    ('-Z', "-Z", ""),
  ]
  add_scene_custom_prop(
    'arm_pole_normal', 
    'Enum', 
    '-X', 
    items = items
  )
  add_scene_custom_prop(
    'leg_pole_normal', 
    'Enum', 
    'X', 
    items = items
  )
