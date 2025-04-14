from ..libs.blender_utils import (
  get_pose_bone, 
  get_pose_bones,
)

from . import add_bone_widget, init_bones_widget

def init_main_bone_widgets (bone_config, scene):
  patch_config = [
    {
      'name': 'root',
      'widget': 'Root',
      'widget_config': {
        'scale': (1, 1, 1)
      }
    },
    {
      'name': 'org_shoulder.l',
      'widget': 'Chest'
    },
    {
      'name': 'mch_finger_d_01.l',
      'widget': 'Cuboid'
    }
  ]

  init_bones_widget(patch_config, scene)
  init_bones_widget(bone_config, scene)

def init_tweak_bone_widgets (scene):
  # 以手指长度为参考
  l = get_pose_bone('def_thumb_01.l').length
  v = l / 4

  for pose_bone in get_pose_bones():
    if pose_bone.name.startswith('tweak_'):
      is_finger_tweak_bone = pose_bone.name.startswith((
        'tweak_thumb', 
        'tweak_finger', 
        'tweak_tip_thumb', 
        'tweak_tip_finger'
      ))
      add_bone_widget(
        scene, 
        pose_bone, 
        'Sphere', 
        (0, 0, 0), 
        scale = (v, v, v) if is_finger_tweak_bone else (l, l, l)
      )

def init_human_widgets (bone_config, scene):
  init_main_bone_widgets(bone_config, scene)
  init_tweak_bone_widgets(scene)
  