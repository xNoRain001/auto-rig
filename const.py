custom_props_config = [
  {
    'prop_name': 'head_follow',
    'config': {
      'default': True
    },
    # Custom Props UI Panel
    'is_visible': True
  },
  {
    'prop_name': 'neck_follow',
    'config': {
      'default': True
    },
    'is_visible': True
  },
  {
    'prop_name': 'leg_fk_to_ik.l',
    'config': {
      'default': True
    },
    'is_visible': False
  },
  {
    'prop_name': 'leg_fk_to_ik.r',
    'config': {
      'default': True
    },
    'is_visible': False
  },
  {
    'prop_name': 'leg_ik_parent.l',
    'config': {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    },
    'is_visible': True
  },
  {
    'prop_name': 'leg_ik_parent.r',
    'config': {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    },
    'is_visible': True
  },

  {
    'prop_name': 'arm_fk_to_ik.l',
    'config': {
      'default': True
    },
    'is_visible': False
  },
  {
    'prop_name': 'arm_fk_to_ik.r',
    'config': {
      'default': True
    },
    'is_visible': False
  },
  {
    'prop_name': 'arm_ik_parent.l',
    'config': {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    },
    'is_visible': True
  },
  {
    'prop_name': 'arm_ik_parent.r',
    'config': {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    },
    'is_visible': True
  }
]

bl_category = 'Auto Rig'
