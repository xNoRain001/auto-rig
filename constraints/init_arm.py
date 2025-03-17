from ..libs.blender_utils import get_edit_bone
from .init_torso import common_stretch_config
from ..bones.init_arm import arm_tweak_bone_names

def init_arm ():
  config = []
  org_bone_names = ['org_arm.l', 'org_forearm.l', 'org_hand.l']

  # COPY_ROTATION 要在 STRETCH_TO 之前
  influence_list = [0.1, 0.3, 0.7, 1, 0.1, 0.3, 0.7, 1]
  for index, org_bone_name in enumerate(arm_tweak_bone_names):
    if org_bone_name.startswith('org_arm_'):
      prefix = 'mch_switch_arm.l'
    else:
      prefix = 'mch_switch_forearm.l'

    config.append({
      'name': org_bone_name,
      'target': prefix,
      'type': 'COPY_ROTATION',
      'config': {
        'influence': influence_list[index]
      }
    })

  common_stretch_config(org_bone_names, config)
  common_stretch_config(arm_tweak_bone_names, config)
  config[-1]['target'] = 'tweak_hand.l'

  config.extend([
    {
      'name': 'vis_arm_pole.l',
      'target': 'arm_pole.l',
      'type': 'STRETCH_TO',
      'config': {
        'head_tail': 1
      }
    },
    {
      'name': 'mch_parent_arm_pole.l',
      # 这个约束的 target 是一个列表
      'target': ['root', 'torso', 'org_spine_01', 'chest', 'head'],
      'type': 'ARMATURE',
    },
    {
      'name': 'mch_parent_ik_hand.l',
      'target': ['root', 'torso', 'org_spine_01', 'chest', 'head'],
      'type': 'ARMATURE',
    },
    # 解决拉伸缩放问题
    {
      'name': 'mch_tweak_forearm.l',
      'target': 'root',
      'type': 'COPY_SCALE',
    },
    {
      'name': 'mch_tweak_hand.l',
      'target': 'root',
      'type': 'COPY_SCALE',
    },
    # twist
    {
      'name': 'mch_int_arm.l',
      'target': 'mch_arm.l',
      'type': 'COPY_LOCATION',
    },
    {
      'name': 'mch_int_arm.l',
      'target': 'mch_arm.l',
      'type': 'COPY_ROTATION',
    },
    {
      'name': 'mch_twist_arm.l',
      'target': 'mch_switch_arm.l',
      'type': 'COPY_LOCATION',
    },
    {
      'name': 'mch_twist_arm.l',
      'target': 'mch_switch_arm.l',
      'type': 'DAMPED_TRACK',
      'config': {
        'head_tail': 1
      }
    },
    # ik
    {
      'name': 'mch_ik_forearm.l',
      'target': 'ik_hand.l',
      'type': 'IK',
      'config': {
        'chain_count': 2,
        'pole_subtarget': 'arm_pole.l'
      }
    },
  ])

  list = ['mch_switch_arm.l', 'mch_switch_forearm.l', 'mch_switch_hand.l']
  list2 = ['fk_arm.l', 'fk_forearm.l', 'fk_hand.l']
  list3 = ['mch_ik_arm.l', 'mch_ik_forearm.l', 'ik_hand.l']

  for index, item in enumerate(list):
    config.extend([
      {
        'name': item,
        'target': list2[index],
        'type': 'COPY_TRANSFORMS',
      },
      {
        'name': item,
        'target': list3[index],
        'type': 'COPY_TRANSFORMS',
      }
    ])

  # TODO:
  # def set_ik_stretch (ik_bones) :
  #  get_pose_bone(ik_bones[0]).ik_stretch = 0.01
  #  get_pose_bone(ik_bones[1]).ik_stretch = 0.01

  return config
