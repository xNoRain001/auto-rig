from ..libs.blender_utils import (
  get_pose_bone, 
  select_pose_bone,
  deselect_pose_bone
)

def chest_patch ():
  get_pose_bone('chest').custom_shape_translation[2] = \
    get_pose_bone('org_spine_02').length + get_pose_bone('chest').length / 2

def hips_patch ():
  get_pose_bone('hips').custom_shape_translation[2] = \
    (get_pose_bone('org_spine_01').length + get_pose_bone('hips').length) * -1
  
def palm_patch ():
  get_pose_bone('mch_finger_d_01.l').custom_shape_scale_xyz[0] = \
    get_pose_bone('mch_finger_d_01.l').custom_shape_scale_xyz[0] * 2

bone_widget_patchs = {
  'chest': chest_patch,
  'hips': hips_patch,
  'mch_finger_d_01.l': palm_patch
}

def add_bone_widget (
  scene,
  bone_name,
  shape,
  translation = None,
  rotation = None,
  scale = None
):
  pose_bone = get_pose_bone(bone_name)
  select_pose_bone(pose_bone)
  scene.shape = shape

  if translation:
    scene.translation = translation

  if rotation:
    scene.rotation = rotation

  if scale:
    scene.scale = scale

  deselect_pose_bone(pose_bone)

def init_bones_widget (bone_config, scene):
  for config in bone_config:
    bone_name = config['name']
    widget = config.get('widget')

    if widget:
      widget_config = config.get('widget_config') or {}
      add_bone_widget(scene, bone_name, widget, **widget_config)

    if bone_name in bone_widget_patchs:
      bone_widget_patchs[bone_name]()