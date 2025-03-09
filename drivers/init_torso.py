def init_torso ():
  config = [
    {
      'name': 'mch_int_neck',
      'index': -1,
      'config': {
        'name': 'influence',
        'type': 'AVERAGE',
        'vars': [
          {
            'name': 'neck_follow',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': 'pose.bones["props"]["neck_follow"]'
              }
            ]
          }
        ]
      }
    },
    {
      'name': 'mch_int_head',
      'index': -1,
      'config': {
        'name': 'influence',
        'type': 'AVERAGE',
        'vars': [
          {
            'name': 'head_follow',
            'targets': [
              {
                'id_type': 'OBJECT',
                'data_path': 'pose.bones["props"]["head_follow"]'
              }
            ]
          }
        ]
      }
    }
  ]

  return config
