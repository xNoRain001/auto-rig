from ..const import (
  mch_collection,
  torso_collection,
  tweak_torso_collection,
)

def init_torso_config (config):
  config.extend([
    # fk_bones
    {
      'name': 'cog',
      'source': 'org_spine_02',
      'collection': torso_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 3, 0)
      },
      'widget': 'Cube',
      'widget_config': {
        'translation': (0, 0, 0)
      }
    },
    {
      'name': 'spine_01',
      'source': 'org_spine_01',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Circle',
      'widget_config': {
        'scale': (0.2, 0.2, 0.2)
      }
    },
    {
      'name': 'hips',
      'source': 'org_hips',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Chest',
      'widget_config': {
        'scale': (0.2, 0.2, 0.2)
      }
    },
    {
      'name': 'spine_02',
      'source': 'org_spine_02',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Circle',
      'widget_config': {
        'scale': (0.2, 0.2, 0.2)
      }
    },
    {
      'name': 'chest',
      'source': 'org_chest',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Circle',
      'widget_config': {
        'scale': (0.2, 0.2, 0.2)
      }
    },
    {
      'name': 'neck',
      'source': 'org_neck',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Circle'
    },
    {
      'name': 'head',
      'source': 'org_head',
      'collection': torso_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'widget': 'Circle'
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
    }
  ])

  return config
