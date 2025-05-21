from ..libs.blender_utils import get_edit_bone
from .init_torso_config import common_stretch_config
from ..bones.init_leg_config import leg_tweak_bone_names
from .init_arm_config import get_last_number

def init_leg_config (scene, config):
  org_bone_names = ['org_leg.l', 'org_shin.l', 'org_foot.l']
  org_toes_bone_name = 'org_toes.l'
  has_toes_bone = get_edit_bone(org_toes_bone_name)
  if has_toes_bone:
    org_bone_names.append(org_toes_bone_name)
 
  # COPY_ROTATION 要在 STRETCH_TO 之前
  for index, org_bone_name in enumerate(leg_tweak_bone_names):
    i = get_last_number(org_bone_name)
    is_leg = org_bone_name.startswith('org_leg_')

    if is_leg:
      prefix = 'mch_switch_leg.l'
    else:
      prefix = 'mch_switch_shin.l'

    config.append({
      'name': org_bone_name,
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': prefix,
        'influence': getattr(scene, f'{ "leg" if is_leg else "shin" }_influence_{ i - 1 }')
      }
    })

  common_stretch_config(org_bone_names, config)
  if has_toes_bone:
    config[-1]['config']['subtarget'] = 'tweak_tip_toes.l'
  else:
    config[-1]['config']['subtarget'] = 'tweak_tip_foot.l'
  common_stretch_config(leg_tweak_bone_names, config)

  config.extend([
    {
      'name': 'vis_leg_pole.l',
      'type': 'STRETCH_TO',
      'config': {
        'subtarget': 'leg_pole.l',
        'head_tail': 1
      }
    },
    {
      'name': 'mch_parent_leg_pole.l',
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'ik_foot.l', 'cog'],
      }
    },
    {
      'name': 'mch_parent_ik_foot.l',
      'type': 'ARMATURE',
      'config': {
        'subtarget': ['root', 'cog'],
      }
    },
    # 解决拉伸缩放问题
    {
      'name': 'mch_tweak_shin.l',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'root',
      }
    },
    {
      'name': 'mch_tweak_foot.l',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'root',
      }
    },
    # twist
    {
      'name': 'mch_int_leg.l',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_leg.l',
      }
    },
    {
      'name': 'mch_int_leg.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'mch_leg.l',
      }
    },
    {
      'name': 'mch_twist_leg.l',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_switch_leg.l',
      }
    },
    {
      'name': 'mch_twist_leg.l',
      'type': 'DAMPED_TRACK',
      'config': {
        'subtarget': 'mch_switch_leg.l',
        'head_tail': 1
      }
    },
    # ik
    {
      'name': 'mch_ik_shin.l',
      'type': 'IK',
      'config': {
        'subtarget': 'mch_ik_foot.l',
        'chain_count': 2,
        'pole_subtarget': 'leg_pole.l'
      }
    },
  ])

  list = ['mch_switch_leg.l', 'mch_switch_shin.l', 'mch_switch_foot.l']
  list2 = ['fk_leg.l', 'fk_shin.l', 'fk_foot.l']
  list3 = ['mch_ik_leg.l', 'mch_ik_shin.l', 'mch_ik_foot.l']

  if has_toes_bone:
    list.append(org_toes_bone_name.replace('org_', 'mch_switch_'))
    list2.append(org_toes_bone_name.replace('org_', 'fk_'))
    list3.append(org_toes_bone_name.replace('org_', 'ik_'))

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

  # foot ctrl
  common = {
    'owner_space': 'LOCAL', 
    'target_space': 'LOCAL'
  }
  common2 = {
    'use_legacy_behavior': True, 
    'owner_space': 'LOCAL'
  }
  config.extend([
    {
      'name': 'mch_foot_heel.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'foot_heel.l',
        'use_y': False, 
        'use_z': False, 
        **common
      }
    },
    {
      'name': 'mch_foot_heel.l',
      'type': 'LIMIT_ROTATION',
      'config': {
        'use_limit_x': True, 
        'min_x': -180, 
        'max_x': 0, 
        **common2
      }
    },
    {
      'name': 'mch_foot_roll.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'foot_heel.l',
        'use_y': False, 
        'use_z': False, 
        **common
      }
    },
    {
      'name': 'mch_foot_roll.l',
      'type': 'LIMIT_ROTATION',
      'config': {
        'use_limit_x': True, 
        'min_x': 0, 
        'max_x': 180, 
        **common2
      }
    },
    {
      'name': 'mch_roll_side_01.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'foot_heel.l',
        'use_x': False, 
        'use_y': False, 
        **common
      }
    },
    {
      'name': 'mch_roll_side_01.l',
      'type': 'LIMIT_ROTATION',
      'config': {
        'use_limit_z': True, 
        'min_z': 0, 
        'max_z': 180,
        **common2
      }
    },
    {
      'name': 'mch_roll_side_02.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'foot_heel.l',
        'use_x': False, 
        'use_y': False, 
        **common
      }
    },
    {
      'name': 'mch_roll_side_02.l',
      'type': 'LIMIT_ROTATION',
      'config': {
        'use_limit_z': True, 
        'min_z': -180, 
        'max_z': 0,
        **common2
      }
    },
  ])

  if get_edit_bone('ik_toes.l'):
    config.append({
      'name': 'mch_ik_toes.l',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'mch_foot_roll.l',
        'target_space': 'LOCAL', 
        'owner_space': 'LOCAL',
        'use_x': True,
        'use_y': False,
        'use_z': False
      }
    })

  return config
