from ..libs.blender_utils import get_types, add_scene_custom_prop

def add_bow ():
  add_scene_custom_prop(
    'bow_armature', 
    'Pointer', 
    type = get_types('Object'),
    poll = lambda self, o: o.type == 'ARMATURE'
  )
  add_scene_custom_prop(
    'bowstring_max_distance', 
    'Float', 
    min = 0, 
    default = 0.15
  )
  add_scene_custom_prop(
    'bow_limb_max_angle', 
    'Float', 
    min = 0, 
    max = 90, 
    default = 30
  )
  add_scene_custom_prop('bow_root', 'String')
  add_scene_custom_prop('bowstring', 'String')
  add_scene_custom_prop('bow_limb', 'String')
  add_scene_custom_prop('bow_limb_upper', 'String')
  add_scene_custom_prop('bow_limb_lower', 'String')
