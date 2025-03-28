def init_arm_config (config):
  sides = ['l', 'r']

  for side in sides:
    common = {
      'name': 'weight',
      'type': 'SCRIPTED',
      'vars': [
        {
          'name': f'arm_ik_parent_{ side }',
          'targets': [
            {
              'id_type': 'OBJECT',
              'data_path': f'pose.bones["props"]["arm_ik_parent_{ side }"]'
            }
          ]
        }
      ]
    }
    config.extend([
      {
        'name': f'mch_parent_ik_hand.{ side }',
        'index': 0,
        'config': common
      },
      {
        'name': f'mch_parent_arm_pole.{ side }',
        'index': 0,
        'config': common
      },
    ])

    list = [f'mch_switch_arm.{ side }', f'mch_switch_forearm.{ side }', f'mch_switch_hand.{ side }']

    for item in list:
      config.append({
        'name': item,
        'index': -1,
        'config': {
          'name': 'influence',
          'type': 'AVERAGE',
          'vars': [
            {
              'name': f'arm_fk_to_ik_{ side }',
              'targets': [
                {
                  'id_type': 'OBJECT',
                  'data_path': f'pose.bones["props"]["arm_fk_to_ik_{ side }"]'
                }
              ]
            }
          ]
        }
      })

  return config
