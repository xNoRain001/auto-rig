from math import radians

from . import def_bone_add_copy_transforms

def init_bow_constraints_config ():
  config = [
    {
      'name': 'org_bowstring',
      'type': 'LIMIT_LOCATION',
      'config': {
        'owner_space': 'LOCAL',
        'use_min_x': True,
        'use_min_y': True,
        'use_min_z': True,
        'use_max_x': True,
        'use_max_y': True,
        'use_max_z': True,
        'max_y': 0.15
      }
    },
    # 由手握住，因此不会发生偏移
    # {
    #   'name': 'org_bow_limb',
    #   'type': 'COPY_LOCATION',
    #   'config': {
    #     'subtarget': 'def_bowstring',
    #     'owner_space': 'LOCAL',
    #     'target_space': 'LOCAL',
    #     'influence': 0.5
    #   }
    # },
    {
      'name': 'org_bow_limb_upper',
      'type': 'TRANSFORM',
      'config': {
        'subtarget': 'def_bowstring',
        'owner_space': 'LOCAL',
        'target_space': 'LOCAL',
        'map_to': 'ROTATION',
        'map_to_z_from': 'Y',
        'from_max_y': 0.15,
        'to_max_z_rot': radians(-30)
      }
    },
    {
      'name': 'org_bow_limb_lower',
      'type': 'TRANSFORM',
      'config': {
        'subtarget': 'def_bowstring',
        'owner_space': 'LOCAL',
        'target_space': 'LOCAL',
        'map_to': 'ROTATION',
        'map_to_z_from': 'Y',
        'from_max_y': 0.15,
        'to_max_z_rot': radians(30)
      }
    },
  ]
  
  def_bone_add_copy_transforms()

  return config
    