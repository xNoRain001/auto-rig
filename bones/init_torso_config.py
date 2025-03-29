from ..const import (
  mch_collection,
  torso_collection,
  fk_torso_collection,
  tweak_torso_collection,
)

def init_torso_config (config):
  config.extend([
    # fk_bones
    {
      'name': 'torso',
      'source': 'org_spine_02',
      'collection': torso_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 3, 0)
      },
    },
    {
      'name': 'chest',
      'source': 'torso',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.9,
      },
    },
    {
      'name': 'hips',
      'source': 'torso',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.8,
      },
    },
    {
      'name': 'fk_spine_01',
      'source': 'org_spine_02',
      'collection': fk_torso_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, 1)
      },
    },
    {
      'name': 'fk_hips',
      'source': 'org_hips',
      'collection': fk_torso_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0, 1)
      },
    },
    {
      'name': 'fk_spine_02',
      'source': 'org_spine_02',
      'collection': fk_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
    },
    {
      'name': 'fk_chest',
      'source': 'org_chest',
      'collection': fk_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
    },
    {
      'name': 'neck',
      'source': 'org_neck',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
    },
    {
      'name': 'head',
      'source': 'org_head',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
    },
    # tweak bones
    {
      'name': 'tweak_hips',
      'source': 'org_hips',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_spine_01',
      'source': 'org_spine_01',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_spine_02',
      'source': 'org_spine_02',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_chest',
      'source': 'org_chest',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_neck',
      'source': 'org_neck',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_head',
      'source': 'org_head',
      'collection': tweak_torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_top_head',
      'source': 'org_head',
      'collection': tweak_torso_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0, 0.25),
      }
    },
    # mch bones
    {
      'name': 'mch_neck',
      'source': 'neck',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_int_neck',
      'source': 'mch_neck',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'mch_head',
      'source': 'head',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_int_head',
      'source': 'mch_head',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'mch_fk_chest',
      'source': 'fk_chest',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_spine_02',
      'source': 'fk_spine_02',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_spine_01',
      'source': 'fk_spine_01',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_hips',
      'source': 'fk_hips',
      'collection': mch_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_spine_02_pivot',
      'source': 'fk_spine_01',
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
  ])

  return config
