from ..libs.blender_utils import add_scene_custom_prop

def add_dynamic_parent ():
  # for test
  # add_scene_custom_prop('dynamic_parent_bone', 'String', 'mch_parent_ik_hand.l')
  add_scene_custom_prop('dynamic_parent_bone', 'String', '')
  # 用于 UL List 中 active_propname
  add_scene_custom_prop('placeholder_prop', 'Int')
  add_scene_custom_prop('var_name', 'String', 'leg_ik_parent_l')
  add_scene_custom_prop('data_path', 'String', 'pose.bones["props"]["leg_ik_parent.l"]')
