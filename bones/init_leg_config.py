from ..libs.blender_utils import get_edit_bone

from .init_arm_config import init_tweak_bones
from ..const import (
  mch_collection,
  fk_leg_l_collection,
  ik_leg_l_collection,
  tweak_leg_l_collection,
)

leg_tweak_bone_names = []

def init_leg_config (scene, config):
  leg_tweak_bone_names.clear()
  org_bone_names = ['org_leg.l', 'org_shin.l', 'org_foot.l']
  org_toes_bone_name = 'org_toes.l'
  org_toes_bone = get_edit_bone(org_toes_bone_name)
  if org_toes_bone:
    org_bone_names.append(org_toes_bone_name)
  no_mch_prefix_set = set([org_toes_bone_name])
  last_index = len(org_bone_names) - 1

  for index, org_bone_name in enumerate(org_bone_names):
    config.extend([
      {
        'name': org_bone_name.replace('org_', 'mch_switch_'),
        'source': org_bone_name,
        'collection': mch_collection,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      {
        'name': org_bone_name.replace('org_', 'fk_'),
        'source': org_bone_name,
        'collection': fk_leg_l_collection,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      {
        'name': org_bone_name.replace(
          'org_', 
          f'{ "" if org_bone_name in no_mch_prefix_set else "mch_" }ik_'
        ),
        'source': org_bone_name,
        'collection': ik_leg_l_collection if org_bone_name in no_mch_prefix_set else mch_collection,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 1
        }
      },
      {
        'name': org_bone_name.replace('org_', 'tweak_'),
        'source': org_bone_name,
        'collection': tweak_leg_l_collection,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 0.5
        }
      }
    ])

    if index > 0:
      config.append({
        'name': org_bone_name.replace('org_', 'mch_tweak_'),
        'source': org_bone_name,
        'collection': mch_collection,
        'operator': 'copy',
        'operator_config': {
          'scale_factor': 0.25
        }
      })

    if index == last_index:
      config.append({
        'name': org_bone_name.replace('org_', 'tweak_tip_'),
        'source': org_bone_name,
        'collection': tweak_leg_l_collection,
        'operator': 'extrude',
        'operator_config': {
          'head_or_tail': 'tail',
          'scale_factor': (0, 0.5, 0)
        }
      })

  config.extend([
    {
      'name': 'mch_ik_leg.l.001',
      'source': 'mch_ik_leg.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      },
      'pole_target_type': 'leg',
    },
    {
      'name': 'leg_pole.l',
      'source': 'mch_ik_leg.l.001',
      'collection': ik_leg_l_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0.3, 0)
      }
    },
    {
      'name': 'mch_parent_leg_pole.l',
      'collection': mch_collection,
      'source': 'leg_pole.l',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    {
      'name': 'vis_leg_pole.l',
      'source': 'mch_ik_leg.l',
      'collection': ik_leg_l_collection,
      'operator': 'extrude',
      'operator_config': {
        'target': 'leg_pole.l',
        'head_or_tail': 'tail',
        'target_head_or_tail': 'tail'
      }
    },
    {
      'name': 'mch_ik_fk_leg_pole.l',
      'source': 'leg_pole.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.25
      }
    },
    # foot ctrl
    {
      'name': 'mch_foot_roll.l',
      'source': 'org_foot.l',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 1, 0)
      },
    },
    {
      'name': 'ik_foot.l',
      'source': 'mch_foot_roll.l',
      'collection': ik_leg_l_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      },
    },
    {
      'name': 'mch_ik_fk_foot.l',
      'source': 'ik_foot.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    {
      'name': 'mch_parent_ik_foot.l',
      'source': 'ik_foot.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    {
      'name': 'mch_roll_side_01.l',
      'source': 'mch_foot_roll.l',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0.5, 0, 0)
      },
    },
    {
      'name': 'mch_roll_side_02.l',
      'source': 'mch_roll_side_01.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      },
    },
    {
      'name': 'mch_foot_heel.l',
      'source': 'mch_foot_roll.l',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0, 0.5)
      },
    },
    {
      'name': 'foot_heel.l',
      'source': 'mch_foot_heel.l',
      'collection': ik_leg_l_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      },
    },
  ])

  if org_toes_bone:
    config.append({
      'name': 'mch_ik_toes.l',
      'source': 'ik_toes.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      },
    })

  init_tweak_bones(scene, 'leg', leg_tweak_bone_names)
  for tweak_bone_name in leg_tweak_bone_names:
    config.append({
      'name': tweak_bone_name.replace('org_', 'tweak_'),
      'source': tweak_bone_name,
      'collection': leg_tweak_bone_names,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    })

  # twist bones
  config.extend([
    {
      'name': 'mch_leg.l',
      'source': 'org_leg.l',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, 0.25)
      }
    },
    {
      'name': 'mch_int_leg.l',
      'source': 'mch_leg.l',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5
      }
    },
    {
      'name': 'mch_twist_leg.l',
      'source': 'org_leg.l',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, -0.25)
      }
    }
  ])

  return config
