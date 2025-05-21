def common_stretch_config (org_bone_names, config):
  last_index = len(org_bone_names) - 1

  for index, org_bone_name in enumerate(org_bone_names):
    if index == last_index:
      target_bone_name = org_bone_name.replace('org_', 'tweak_tip_')
    else:
      target_bone_name = org_bone_names[index + 1].replace('org_', 'tweak_') 

    config.append({
      'name': org_bone_name,
      'type': 'STRETCH_TO',
      'config': {
        'subtarget': target_bone_name,
      }
    })

def init_torso_config ():
  config = [
    {
      'name': 'mch_int_neck',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_neck',
      }
    },
    {
      'name': 'mch_int_neck',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'mch_neck',
      }
    },
    {
      'name': 'mch_int_neck',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'mch_neck',
      }
    },
    {
      'name': 'mch_int_head',
      'type': 'COPY_LOCATION',
      'config': {
        'subtarget': 'mch_head',
      }
    },
    {
      'name': 'mch_int_head',
      'type': 'COPY_SCALE',
      'config': {
        'subtarget': 'mch_head',
      }
    },
    {
      'name': 'mch_int_head',
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': 'mch_head',
      }
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
  config[-1]['config']['subtarget'] = 'tweak_top_head'

  return config
