from ..libs.blender_utils import add_scene_custom_prop

def add_dynamic_parent ():
  add_scene_custom_prop('dynamic_parent_bone', 'String', 'mch_parent_ik_hand.l')
  add_scene_custom_prop('selected_target', 'Int')
  add_scene_custom_prop('target_prop', 'String')
