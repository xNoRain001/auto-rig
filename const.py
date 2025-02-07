group = {
  'use_in_rig_ui': [
    ['root'],
    ['torso', 'torso_fk', 'torso_tweak'],
    ['arm_fk.l', 'arm_fk.r'],
    ['arm_ik.l', 'arm_ik.r'],
    ['arm_tweak.l', 'arm_tweak.r'],
    ['hand.l', 'hand.r'],
    ['hand_tweak.l', 'hand_tweak.r'],
    ['leg_fk.l', 'leg_fk.r'],
    ['leg_ik.l', 'leg_ik.r'],
    ['leg_tweak.l', 'leg_tweak.r']
  ],
  'unused_in_rig_ui': [
    ['def'],
    ['org'],
    ['mch'],
    ['props']
  ]
}

custom_props_config = {
  'head_follow': True,
  'neck_follow': True,
  'leg_fk_to_ik.l': True,
  'leg_fk_to_ik.r': True,
  'leg_ik_parent.l': [
    # 这个值只是用来创建属性的，会被默认值覆盖
    1, 
    # 配置项
    {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    }
  ],
  'leg_ik_parent.r': [
    1, 
    {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    }
  ],
  'arm_fk_to_ik.l': True,
  'arm_fk_to_ik.r': True,
  'arm_ik_parent.l': [
    0,
    {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    }
  ],
  'arm_ik_parent.r': [
    0,
    {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    }
  ]
}
