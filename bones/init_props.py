def init_props ():
  return [
    {
      'name': 'props',
      'source': 'org_head',
      'operator': 'extrude',
      'operator_config': {
        'head_or_tail': 'tail',
        'scale_factor': (0, 0, 1)
      }
    }
  ]
