from ..libs.blender_utils import get_types, add_scene_custom_prop

def add_ball ():
  add_scene_custom_prop(
    'ball_armature', 
    'Pointer', 
    type = get_types('Object'),
    poll = lambda self, o: o.type == 'ARMATURE'
  )
  add_scene_custom_prop('ball_root', 'String', '')
  add_scene_custom_prop('deformation', 'String', '')
