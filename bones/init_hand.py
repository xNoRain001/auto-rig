from ..libs.blender_utils import get_bone_chain, get_edit_bone, get_bone_chain_names

# 每根手指上的第一根骨骼
org_master_bone_names = [
  'org_thumb_01.l',
  'org_finger_a_01.l',
  'org_finger_b_01.l',
  'org_finger_c_01.l',
  'org_finger_d_01.l',
]
org_bone_names = []

def init_hand ():
  config = []

  for org_master_bone_name in org_master_bone_names:
    org_bones = get_bone_chain(get_edit_bone(org_master_bone_name))
    org_bone_names.append(get_bone_chain_names(get_edit_bone(org_master_bone_name)))
    last_index = len(org_bones) - 1

    for index, org_bone in enumerate(org_bones):
      org_bone_name = org_bone.name
  
      config.extend([
        {
          'name': org_bone_name.replace('org_', 'mch_'),
          'source': org_bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 0.25
          }
        },
        {
          'name': org_bone_name.replace('org_', ''),
          'source': org_bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 1
          }
        },
        {
          'name': org_bone_name.replace('org_', 'tweak_'),
          'source': org_bone_name,
          'operator': 'copy',
          'operator_config': {
            'scale_factor': 0.5
          }
        }
      ])

      if index == last_index:
        # tweak tip bone
        config.append({
          'name': org_bone_name.replace('org_', 'tweak_tip_'),
          'source': org_bone_name,
          'operator': 'extrude',
          'operator_config': {
            'head_or_tail': 'tail',
            'scale_factor': (0, 0.5, 0)
          }
        })

  return config
