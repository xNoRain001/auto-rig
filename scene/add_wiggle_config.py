from ..libs.blender_utils import add_scene_custom_prop

def add_wiggle_config ():
  add_scene_custom_prop('wiggle_prop', 'String', '')
  add_scene_custom_prop('wiggle_influence', 'Float', 0.5, min = 0, max = 1)
