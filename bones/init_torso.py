def init_torso ():
  torso_collection = 'torso'
  torso_fk_collection = 'torso_fk'
  
  return [
    # fk_bones
    {
      'name': 'torso',
      'source': 'org_spine_02',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 2, 0)
      },
      'collection': torso_collection,
    },
    {
      'name': 'chest',
      'source': 'torso',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.75,
      },
      'collection': torso_collection,
    },
    {
      'name': 'hips',
      'source': 'torso',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      },
      'collection': torso_collection,
    },
    {
      'name': 'fk_spine_01',
      'source': 'org_spine_02',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0, 1)
      },
      'collection': torso_fk_collection,
    },
    {
      'name': 'fk_hips',
      'source': 'org_hips',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0, 1)
      },
      'collection': torso_fk_collection,
    },
    {
      'name': 'fk_spine_02',
      'source': 'org_spine_02',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'collection': torso_fk_collection,
    },
    {
      'name': 'fk_chest',
      'source': 'org_chest',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'collection': torso_fk_collection,
    },
    {
      'name': 'neck',
      'source': 'org_neck',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'collection': torso_collection,
    },
    {
      'name': 'head',
      'source': 'org_head',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1,
      },
      'collection': torso_collection,
    },
    # tweak bones
    {
      'name': 'tweak_hips',
      'source': 'org_hips',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_spine_01',
      'source': 'org_spine_01',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_spine_02',
      'source': 'org_spine_02',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_chest',
      'source': 'org_chest',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_neck',
      'source': 'org_neck',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_head',
      'source': 'org_head',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'tweak_top_head',
      'source': 'org_head',
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
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_int_neck',
      'source': 'mch_neck',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'mch_head',
      'source': 'head',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_int_head',
      'source': 'mch_head',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
    {
      'name': 'mch_fk_chest',
      'source': 'fk_chest',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_spine_02',
      'source': 'fk_spine_02',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_spine_01',
      'source': 'fk_spine_01',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_fk_hips',
      'source': 'fk_hips',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.5, 0),
      }
    },
    {
      'name': 'mch_spine_02_pivot',
      'source': 'fk_spine_01',
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 0.5,
      }
    },
  ]
