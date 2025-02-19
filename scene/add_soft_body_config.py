from ..libs.blender_utils import add_scene_custom_prop

def add_soft_body_config ():
  add_scene_custom_prop('friction', 'Float', 10)
  add_scene_custom_prop('mass', 'Float', 0.1)
  add_scene_custom_prop('goal_min', 'Float', 0.4)
  add_scene_custom_prop('friction', 'Float', 10)
  