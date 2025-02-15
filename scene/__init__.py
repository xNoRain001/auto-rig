from ..libs.blender_utils import register_classes, unregister_classes, add_scene_custom_prop, get_object_

classes = ()

def set_rotation_mode (armature_name, mode):
  bones = get_object_(armature_name).pose.bones

  for bone in bones:
    bone.rotation_mode = mode

def on_update (self, context):
  armature_name = context.scene.armature_name
  mode = self.rotation_mode

  set_rotation_mode(armature_name, mode)

def register():
  # register_classes(classes)
  add_scene_custom_prop('mesh_name', 'String', '荧_mesh')
  add_scene_custom_prop('armature_name', 'String', '荧_arm')
  # TODO: 色盘
  add_scene_custom_prop('torso_color', 'String')
  add_scene_custom_prop('ik_fk_l_color', 'String')
  add_scene_custom_prop('ik_fk_r_color', 'String')
  add_scene_custom_prop('tweak_color', 'String')
  add_scene_custom_prop('armature_name', 'String', '荧_arm')
  add_scene_custom_prop('armature_name', 'String', '荧_arm')
  add_scene_custom_prop('friction', 'Float', 10)
  add_scene_custom_prop('mass', 'Float', 0.1)
  add_scene_custom_prop('goal_min', 'Float', 0.4)
  add_scene_custom_prop('friction', 'Float', 10)
  common = { 'size': 3, 'subtype': 'COORDINATES' }
  add_scene_custom_prop('side_01_head_location', 'FloatVector', **common)
  add_scene_custom_prop('side_02_head_location', 'FloatVector', **common)
  add_scene_custom_prop('heel_location', 'FloatVector', **common)
  add_scene_custom_prop('foot_tip_location', 'FloatVector', **common)
  add_scene_custom_prop(
    'rotation_mode', 
    'Enum', 
    'XYZ', 
    items = [
      ('QUATERNION', "QUATERNION", ""),
      ('XYZ', "XYZ", ""),
    ],
    update = on_update
  )
  add_scene_custom_prop(
    'arm_pole_normal', 
    'Enum', 
    'X', 
    items = [
      ('X', "X", ""),
      ('-X', "-X", ""),
      ('Z', "Z", ""),
      ('-Z', "-Z", ""),
    ]
  )
  add_scene_custom_prop(
    'leg_pole_normal', 
    'Enum', 
    '-Z', 
    items = [
      ('X', "X", ""),
      ('-X', "-X", ""),
      ('Z', "Z", ""),
      ('-Z', "-Z", ""),
    ]
  )

def unregister():
  # unregister_classes(classes)
  pass
