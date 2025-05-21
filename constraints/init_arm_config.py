import re
from ..libs.blender_utils import get_edit_bone

from .init_torso_config import common_stretch_config
from ..bones.init_arm_config import arm_tweak_bone_names

def get_last_number (string):
  numbers = re.findall(r'\d+', string)
  return int(numbers[-1]) if numbers else None

def init_arm_config (scene, config):
  org_bone_names = ['org_arm.l', 'org_forearm.l', 'org_hand.l']

  # COPY_ROTATION 要在 STRETCH_TO 之前
  for index, org_bone_name in enumerate(arm_tweak_bone_names):
    i = get_last_number(org_bone_name)
    is_arm = org_bone_name.startswith('org_arm_')

    if is_arm:
      prefix = 'mch_switch_arm.l'
    else:
      prefix = 'mch_switch_forearm.l'

    config.append({
      'name': org_bone_name,
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': prefix,
        'influence': getattr(scene, f'{ "arm" if is_arm else "forearm" }_influence_{ i - 1 }')
      }
    })

  common_stretch_config(org_bone_names, config)
  common_stretch_config(arm_tweak_bone_names, config)
  config[-1]['config']['subtarget'] = 'tweak_hand.l'

  config.extend([
    {
      'name': 'vis_arm_pole.l',
      'type': 'STRETCH_TO',
      'config': {
        'subtarget': 'arm_pole.l',
        'head_tail': 1
      }
    },
    {
      'name': 'mch_parent_arm_pole.l',
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'cog', 'org_spine_01', 'chest', 'head'],
      }
    },
    {
      'name': 'mch_parent_ik_hand.l',
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'cog', 'org_spine_01', 'chest', 'head'],
      }
    },
    # 解决拉伸缩放问题
    {
      'name': 'mch_tweak_forearm.l',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'root',
      }
    },
    {
      'name': 'mch_tweak_hand.l',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'root',
      }
    },
    # twist
    {
      'name': 'mch_int_arm.l',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_arm.l',
      }
    },
    {
      'name': 'mch_int_arm.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'mch_arm.l',
      }
    },
    {
      'name': 'mch_twist_arm.l',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_switch_arm.l',
      }
    },
    {
      'name': 'mch_twist_arm.l',
      'type': 'DAMPED_TRACK',
      'config': {
        'subtarget': 'mch_switch_arm.l',
        'head_tail': 1
      }
    },
    # ik
    {
      'name': 'mch_ik_forearm.l',
      'type': 'IK',
      'config': {
        'subtarget': 'ik_hand.l',
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
        'type': 'COPY_TRANSFORMS',
        'config': {
          'subtarget': list2[index],
        }
      },
      {
        'name': item,
        'type': 'COPY_TRANSFORMS',
        'config': {
          'subtarget': list3[index],
        }
      }
    ])

  return config
