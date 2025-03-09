from ..libs.blender_utils import add_scene_custom_prop

def add_line_width ():
  add_scene_custom_prop('line_width', 'Float', 1.0, min = 1.0)
