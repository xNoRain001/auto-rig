from ..libs.blender_utils import add_scene_custom_prop

def add_tweak_bone_number ():
  add_scene_custom_prop('arm_tweak_bone_number', 'Int', default = 2, min = 0, max = 4)
  add_scene_custom_prop('forearm_tweak_bone_number', 'Int', default = 0, min = 0, max = 4)
  add_scene_custom_prop('leg_tweak_bone_number', 'Int', default = 0, min = 0, max = 4)
  add_scene_custom_prop('shin_tweak_bone_number', 'Int', default = 0, min = 0, max = 4)
  add_scene_custom_prop('arm_influence_0', 'Float', default = 0.1, min = 0, max = 1)
  add_scene_custom_prop('arm_influence_1', 'Float', default = 0.3, min = 0, max = 1)
  add_scene_custom_prop('arm_influence_2', 'Float', default = 0.7, min = 0, max = 1)
  add_scene_custom_prop('arm_influence_3', 'Float', default = 1, min = 0, max = 1)
  add_scene_custom_prop('forearm_influence_0', 'Float', default = 0.1, min = 0, max = 1)
  add_scene_custom_prop('forearm_influence_1', 'Float', default = 0.3, min = 0, max = 1)
  add_scene_custom_prop('forearm_influence_2', 'Float', default = 0.7, min = 0, max = 1)
  add_scene_custom_prop('forearm_influence_3', 'Float', default = 1, min = 0, max = 1)
  add_scene_custom_prop('leg_influence_0', 'Float', default = 0.1, min = 0, max = 1)
  add_scene_custom_prop('leg_influence_1', 'Float', default = 0.3, min = 0, max = 1)
  add_scene_custom_prop('leg_influence_2', 'Float', default = 0.7, min = 0, max = 1)
  add_scene_custom_prop('leg_influence_3', 'Float', default = 1, min = 0, max = 1)
  add_scene_custom_prop('shin_influence_0', 'Float', default = 0.1, min = 0, max = 1)
  add_scene_custom_prop('shin_influence_1', 'Float', default = 0.3, min = 0, max = 1)
  add_scene_custom_prop('shin_influence_2', 'Float', default = 0.7, min = 0, max = 1)
  add_scene_custom_prop('shin_influence_3', 'Float', default = 1, min = 0, max = 1)

