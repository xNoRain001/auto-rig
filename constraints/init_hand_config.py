from ..libs.blender_utils import get_edit_bone, get_bone_chain_names
from .init_torso_config import common_stretch_config
from ..bones.init_hand_config import org_bone_names

def init_hand_config (config):
  common = {
    'target_space': 'LOCAL',
    'owner_space': 'LOCAL',
  }
  org_master_bone_names = [
    'org_thumb_01.l',
    'org_finger_a_01.l',
    'org_finger_b_01.l',
    'org_finger_c_01.l',
    'org_finger_d_01.l',
  ]

  for _org_bone_names in org_bone_names:
    common_stretch_config(_org_bone_names, config)

    for index, org_bone_name in enumerate(_org_bone_names):
      if org_bone_name.endswith('_03.l'):
        config.append({
          'name': org_bone_name.replace('org_', 'mch_'),
          'type': 'COPY_ROTATION',
          'config': {
            'subtarget': _org_bone_names[index - 1].replace('org_', ''), # fk
            **common
          }
        })

  target = org_master_bone_names[-1].replace('org_', 'mch_')
  config.extend([
    {
      'name': org_master_bone_names[2].replace('org_', 'mch_'),
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': target,
        'influence': 0.25,
        **common
      }
    },
    {
      'name': org_master_bone_names[3].replace('org_', 'mch_'),
      'type': 'COPY_ROTATION',
      'config': {
        'subtarget': target,
        'influence': 0.6,
        **common
      }
    }
  ])

  return config
