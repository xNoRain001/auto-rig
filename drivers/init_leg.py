from ..libs.blender_utils import get_edit_bone

def init_leg ():
  sides = ['l', 'r']
  config = []

  for side in sides:
    common = {
      'name': 'weight',
      'type': 'SCRIPTED',
      'vars': [
        {
          'name': f'leg_ik_parent_{ side }',
          'targets': [
            {
              'id_type': 'OBJECT',
              'data_path': f'pose.bones["props"]["leg_ik_parent_{ side }"]'
            }
          ]
        }
      ]
    }
    config.extend([
      {
        'name': f'mch_parent_ik_foot.{ side }',
        'index': 0,
        'config': {
          'expression': [
            f'leg_ik_parent_{ side } == 0 or leg_ik_parent_{ side } == 1',
            f'leg_ik_parent_{ side } == 2'
          ],
          **common
        }
      },
      {
        'name': f'mch_parent_leg_pole.{ side }',
        'index': 0,
        'config': common
      },
    ])

    list = [f'mch_switch_leg.{ side }', f'mch_switch_shin.{ side }', f'mch_switch_foot.{ side }']
    org_toes_bone_name = f'org_toes.{ side }'

    if get_edit_bone(org_toes_bone_name):
      list.append(org_toes_bone_name.replace('org_', 'mch_switch_'))

    for item in list:
      config.append({
        'name': item,
        'index': -1,
        'config': {
          'name': 'influence',
          'type': 'AVERAGE',
          'vars': [
            {
              'name': f'leg_fk_to_ik_{ side }',
              'targets': [
                {
                  'id_type': 'OBJECT',
                  'data_path': f'pose.bones["props"]["leg_fk_to_ik_{ side }"]'
                }
              ]
            }
          ]
        }
      })

  return config
