from ..const import props_collection

def init_props_config (config):
  config.append({
    'name': 'props',
    'source': 'org_head',
    'collection': props_collection,
    'operator': 'extrude',
    'operator_config': {
      'head_or_tail': 'tail',
      'scale_factor': (0, 0, 1)
    }
  })

  return config
