def common_stretch_config (org_bone_names, config):
  last_index = len(org_bone_names) - 1

  for index, org_bone_name in enumerate(org_bone_names):
    if index == last_index:
      target_bone_name = org_bone_name.replace('org_', 'tweak_tip_')
    else:
      target_bone_name = org_bone_names[index + 1].replace('org_', 'tweak_') 

    config.append({
      'name': org_bone_name,
      'target': target_bone_name,
      'type': 'STRETCH_TO'
    })

def init_torso ():
  common = {
    'influence': 0.5,
    'target_space': 'LOCAL', 
    'owner_space': 'LOCAL'
  }

  config = [
    {
      'name': 'mch_spine_02_pivot',
      'target': 'fk_spine_01',
      'type': 'COPY_TRANSFORMS',
      'config': {
        'influence': 0.5
      }
    },
    {
      'name': 'mch_fk_chest',
      'target': 'chest',
      'type': 'COPY_TRANSFORMS',
      'config': common
    },
    {
      'name': 'mch_fk_spine_02',
      'target': 'chest',
      'type': 'COPY_TRANSFORMS',
      'config': common
    },
    {
      'name': 'mch_fk_spine_01',
      'target': 'hips',
      'type': 'COPY_TRANSFORMS',
      'config': common
    },
    {
      'name': 'mch_fk_hips.',
      'target': 'hips',
      'type': 'COPY_TRANSFORMS',
      'config': common
    },
    {
      'name': 'mch_int_neck',
      'target': 'mch_neck',
      'type': 'COPY_LOCATION'
    },
    {
      'name': 'mch_int_neck',
      'target': 'mch_neck',
      'type': 'COPY_SCALE'
    },
    {
      'name': 'mch_int_neck',
      'target': 'mch_neck',
      'type': 'COPY_ROTATION',
    },
    {
      'name': 'mch_int_head',
      'target': 'mch_head',
      'type': 'COPY_LOCATION',
    },
    {
      'name': 'mch_int_head',
      'target': 'mch_head',
      'type': 'COPY_SCALE',
    },
    {
      'name': 'mch_int_head',
      'target': 'mch_head',
      'type': 'COPY_ROTATION',
    },
  ]
  
  org_bone_names = [
    'org_hips',
    'org_spine_01',
    'org_spine_02',
    'org_chest',
    'org_neck',
    'org_head'
  ]

  common_stretch_config(org_bone_names, config)
  config[-1]['target'] = 'tweak_top_head'

  return config
