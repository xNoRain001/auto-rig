custom_props_config = {
  'head_follow': True,
  'neck_follow': True,
  'leg_fk_to_ik.l': True,
  'leg_fk_to_ik.r': True,
  'leg_ik_parent.l': {
    'min': 0,
    'max': 2,
    'description': '0-root | 1-foot | 2-torso',
    'default': 1
  },
  'leg_ik_parent.r': {
    'min': 0,
    'max': 2,
    'description': '0-root | 1-foot | 2-torso',
    'default': 1
  },
  'arm_fk_to_ik.l': True,
  'arm_fk_to_ik.r': True,
  'arm_ik_parent.l': {
    'min': 0,
    'max': 4,
    'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
    'default': 0
  },
  'arm_ik_parent.r': {
    'min': 0,
    'max': 4,
    'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
    'default': 0
  }
}
