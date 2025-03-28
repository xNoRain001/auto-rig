from ..libs.blender_utils import (
  get_pose_bone, 
  get_pose_bones, 
  get_operator,
  set_mode, 
  select_pose_bone,
  deselect_pose_bone
)

def add_bone_widget (
  scene,
  pose_bone,
  **kwargs
):
  shape = kwargs['shape']
  translation = kwargs.get('translation')
  rotation = kwargs.get('rotation')
  scale = kwargs.get('scale')
  select_pose_bone(pose_bone)
  scene.shape = shape

  if translation:
    scene.translation = translation

  if rotation:
    scene.rotation = rotation

  if scale:
    scene.scale = scale

  deselect_pose_bone(pose_bone)

def gen_shape_map ():
  shape_map = {
    'root': { 'shape': 'Root' },
    'props': { 'shape': 'Gear Complex' },
    'head': { 'shape': 'Circle' },
    'neck': { 'shape': 'Circle' },
    'shoulder.l': { 'shape': 'Chest' },
    'torso': { 'shape': 'Cube', 'translation': (0, 0, 0) },
    'chest': { 'shape': 'Chest', 'translation': (0, 0, 0), 'rotation': (0, 0, 0) },
    'shoulder.l': { 'shape': 'Chest', 'rotation': (0, 0, 0) },
    'hips': { 'shape': 'Chest', 'translation': (0, 0, 0), 'rotation': (0, 0, 0) },
    'fk_arm.l': { 'shape': 'FK Limb 2' },
    'ik_hand.l': { 'shape': 'Cube' },
    'arm_pole.l': { 'shape': 'Sphere' },
    'vis_arm_pole.l': { 'shape': 'Line' },
    'thumb_01.l': { 'shape': 'Cube_Mini' },
    'ik_foot.l': { 'shape': 'Cuboid' },
    'foot_heel.l': { 'shape': 'Roll', 'rotation': (1.5708, 0, 1.5708) },
    'ik_toes.l': { 'shape': 'Roll', 'rotation': (3.1415, 1.5708, 0) }
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

def init_bone_widget (scene):
  set_mode('POSE')
  shape_map = gen_shape_map()

  for bone_name, config in shape_map.items():
    pose_bone = get_pose_bone(bone_name)

    if pose_bone:
      add_bone_widget(scene, pose_bone, **config)

  for pose_bone in get_pose_bones():
    if pose_bone.name.startswith('tweak_'):
      # TODO: 以手指长度为参考
      if pose_bone.name.startswith((
        'tweak_thumb', 'tweak_finger', 'tweak_tip_thumb', 'tweak_tip_finger'
      )):
        scale = (0.01, 0.01, 0.01)
      else:
        scale = (0.037, 0.037, 0.037)

      add_bone_widget(scene, pose_bone, **{ 'shape': 'Sphere', 'scale': scale })

class OBJECT_OT_init_bone_widgets (get_operator()):
  bl_idname = 'object.init_bone_widget'
  bl_label = 'Init Bone Widget'

  def execute(self, context):
    init_bone_widget(context.scene)

    return {'FINISHED'}
