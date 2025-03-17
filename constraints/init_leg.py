from ..libs.blender_utils import get_edit_bone
from .init_torso import common_stretch_config
from ..bones.init_leg import leg_tweak_bone_names

def init_leg ():
  config = []
  org_bone_names = ['org_leg.l', 'org_shin.l', 'org_foot.l']
  org_toes_bone_name = 'org_toes.l'
  has_toes_bone = get_edit_bone(org_toes_bone_name)
  if has_toes_bone:
    org_bone_names.append(org_toes_bone_name)
 
  # COPY_ROTATION 要在 STRETCH_TO 之前
  influence_list = [0.1, 0.3, 0.7, 1, 0.1, 0.3, 0.7, 1]
  for index, org_bone_name in enumerate(leg_tweak_bone_names):
    if org_bone_name.startswith('org_leg_'):
      prefix = 'mch_switch_leg.l'
    else:
      prefix = 'mch_switch_shin.l'

    config.append({
      'name': org_bone_name,
      'target': prefix,
      'type': 'COPY_ROTATION',
      'config': {
        'influence': influence_list[index]
      }
    })

  common_stretch_config(org_bone_names, config)
  if has_toes_bone:
    config[-1]['target'] = 'tweak_tip_toes.l'
  else:
    config[-1]['target'] = 'tweak_tip_foot.l'
  common_stretch_config(leg_tweak_bone_names, config)

  config.extend([
    {
      'name': 'vis_leg_pole.l',
      'target': 'leg_pole.l',
      'type': 'STRETCH_TO',
      'config': {
        'head_tail': 1
      }
    },
    {
      'name': 'mch_parent_leg_pole.l',
      'target': ['root', 'ik_foot.l', 'torso'],
      'type': 'ARMATURE',
    },
    {
      'name': 'mch_parent_ik_foot.l',
      'target': ['root', 'torso'],
      'type': 'ARMATURE',
    },
    # 解决拉伸缩放问题
    {
      'name': 'mch_tweak_shin.l',
      'target': 'root',
      'type': 'COPY_SCALE',
    },
    {
      'name': 'mch_tweak_foot.l',
      'target': 'root',
      'type': 'COPY_SCALE',
    },
    # twist
    {
      'name': 'mch_int_leg.l',
      'target': 'mch_leg.l',
      'type': 'COPY_LOCATION',
    },
    {
      'name': 'mch_int_leg.l',
      'target': 'mch_leg.l',
      'type': 'COPY_ROTATION',
    },
    {
      'name': 'mch_twist_leg.l',
      'target': 'mch_switch_leg.l',
      'type': 'COPY_LOCATION',
    },
    {
      'name': 'mch_twist_leg.l',
      'target': 'mch_switch_leg.l',
      'type': 'DAMPED_TRACK',
      'config': {
        'head_tail': 1
      }
    },
    # ik
    {
      'name': 'mch_ik_shin.l',
      'target': 'mch_ik_foot.l',
      'type': 'IK',
      'config': {
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
        'target': list2[index],
        'type': 'COPY_TRANSFORMS',
      },
      {
        'name': item,
        'target': list3[index],
        'type': 'COPY_TRANSFORMS',
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
      'target': 'foot_heel.l',
      'type': 'COPY_ROTATION',
      'config': {
        'use_y': False, 
        'use_z': False, 
        **common
      }
    },
    {
      'name': 'mch_foot_heel.l',
      'target': '',
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
      'target': 'foot_heel.l',
      'type': 'COPY_ROTATION',
      'config': {
        'use_y': False, 
        'use_z': False, 
        **common
      }
    },
    {
      'name': 'mch_foot_roll.l',
      'target': '',
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
      'target': 'foot_heel.l',
      'type': 'COPY_ROTATION',
      'config': {
        'use_x': False, 
        'use_y': False, 
        **common
      }
    },
    {
      'name': 'mch_roll_side_01.l',
      'target': '',
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
      'target': 'foot_heel.l',
      'type': 'COPY_ROTATION',
      'config': {
        'use_x': False, 
        'use_y': False, 
        **common
      }
    },
    {
      'name': 'mch_roll_side_02.l',
      'target': '',
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
      'target': 'mch_foot_roll.l',
      'type': 'COPY_ROTATION',
      'config': {
        'target_space': 'LOCAL', 
        'owner_space': 'LOCAL',
        'use_x': True,
        'use_y': False,
        'use_z': False
      }
    })

  return config
