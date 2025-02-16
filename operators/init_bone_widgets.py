from ..libs.blender_utils import (
  get_pose_bone, get_pose_bones, get_context, get_bone_widget, get_operator,
  active_object_, get_object_, set_mode, get_data
)
from math import radians

def add_bone_widget (
  pose_bone,
  **kwargs
):
  prop = 'shape'
  shape = kwargs[prop]
  del kwargs[prop]
  pose_bone.bone.select = True
  # get_data().window_managers["WinMan"].widget_list = shape
  get_context().scene.widget_list = shape
  get_bone_widget().create_widget(**kwargs)
  pose_bone.bone.select = False

def gen_shape_map ():
  rotation = (radians(90), radians(0), radians(0))
  shape_map = {
    'root': { 'shape': 'Root 1' },
    'props': { 'shape': 'Gear Complex', 'rotation': rotation },
    'head': { 'shape': 'Circle', 'slide': 1 },
    'neck': { 'shape': 'Circle', 'slide': 0.5 },
    'torso': { 'shape': 'Cube' },
    'chest': { 'shape': 'Chest', 'rotation': rotation },
    'hips': { 'shape': 'Chest', 'rotation': rotation },
    'fk_arm.l': { 'shape': 'FK Limb 2' },
    'ik_hand.l': { 'shape': 'Cube' },
    'arm_pole.l': { 'shape': 'Sphere' },
    'vis_arm_pole.l': { 'shape': 'Line' },
    'thumb_01.l': { 'shape': 'Cube', 'global_size': 0.2, 'slide': 0.5 },
    'ik_foot.l': { 'shape': 'Cube', 'slide': 0.5 },
    'foot_heel.l': { 'shape': 'Roll 1', 'global_size': 0.5, 'slide': 0.5 },
    'ik_toes.l': { 'shape': 'Roll 3', 'global_size': 0.5, 'slide': 0.5 }
  }
  # 相同配置
  config = {
    'arm_pole.l': ['leg_pole.l'],
    'vis_arm_pole.l': ['vis_leg_pole.l'],
    'thumb_01.l': [
      'thumb_02.l', 'thumb_03.l', 
      'finger_a_01.l', 'finger_a_02.l', 'finger_a_03.l',
      'finger_b_01.l', 'finger_b_02.l', 'finger_b_03.l',
      'finger_c_01.l', 'finger_c_02.l', 'finger_c_03.l',
      'finger_d_01.l', 'finger_d_02.l', 'finger_d_03.l'
    ],
    'fk_arm.l': [
      'fk_forearm.l', 'fk_hand.l', 
      'fk_leg.l', 'fk_shin.l', 'fk_foot.l', 'fk_toes.l'
    ]
  }

  for key, value in config.items():
    for item in value:
      shape_map[item] = shape_map[key]

  return shape_map

def init_bone_widget (armature_name):
  active_object_(get_object_(armature_name))
  set_mode('POSE')
  shape_map = gen_shape_map()

  for bone_name, config in shape_map.items():
    pose_bone = get_pose_bone(bone_name)

    if pose_bone:
      add_bone_widget(pose_bone, **config)

  for pose_bone in get_pose_bones():
    if pose_bone.name.startswith('tweak_'):
      add_bone_widget(pose_bone, **{ 'shape': 'Sphere' })

  # bone widget 插件 bug，只能手动对称
  # bpy.ops.pose.select_all(action='SELECT')
  # bonewidget.symmetrize_shape()
  # bpy.ops.pose.select_all(action='DESELECT')

class OBJECT_OT_init_bone_widgets (get_operator()):
  bl_idname = 'object.init_bone_widget'
  bl_label = 'Init Bone Widget'

  def execute(self, context):
    armature_name = context.scene.armature_name
    init_bone_widget(armature_name)

    return {'FINISHED'}
