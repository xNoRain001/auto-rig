from ..libs.blender_utils import add_scene_custom_prop

def add_tweak_bone_number ():
  add_scene_custom_prop('arm_tweak_bone_number', 'Int', default = 2, min = 0)
  add_scene_custom_prop('forearm_tweak_bone_number', 'Int', default = 0, min = 0)
  add_scene_custom_prop('leg_tweak_bone_number', 'Int', default = 0, min = 0)
  add_scene_custom_prop('shin_tweak_bone_number', 'Int', default = 0, min = 0)
