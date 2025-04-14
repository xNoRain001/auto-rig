from math import radians

from ..const import ball_collection, mch_collection

def init_ball_config (scene):
  root = scene.ball_root
  deformation = scene.deformation

  config = [
    {
      'name': 'mch_squash_stretch',
      'source': deformation,
      'collection': mch_collection,
      'operator': 'copy',
      'operator_config': {
        'scale_factor': 1
      }
    },
    {
      'name': 'rotation',
      'source': root,
      'collection': ball_collection,
      'operator': 'extrude',
      'operator_config': {
        'target': deformation,
        'target_head_or_tail': 'tail',
        'head_or_tail': 'head'
      },
      'widget': 'Roll 2',
      'widget_config': {
        'scale': (1.5, 1.5, 1.5),
        'translation': (0, 0, 0),
        'rotation': (0, radians(90), 0)
      }
    },
    {
      'name': 'squash_bottom',
      'source': deformation,
      'collection': ball_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'head',
        'scale_factor': (0, 0.3, 0)
      },
      'widget': 'Circle',
      'widget_config': {
        'translation': (0, 0, 0),
        'rotation': (radians(90), 0, 0)
      }
    },
    {
      'name': 'squash_top',
      'source': deformation,
      'collection': ball_collection,
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0.3, 0)
      },
      'widget': 'Circle',
      'widget_config': {
        'translation': (0, 0, 0),
        'rotation': (radians(90), 0, 0)
      }
    },
  ]
    
  return config