from ..libs.blender_utils import get_pose_bone, set_mode, update_view, get_pose_bones

custom_props_config = [
  {
    'prop_name': 'head_follow',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'neck_follow',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'leg_fk_to_ik_l',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'leg_fk_to_ik_r',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'leg_ik_parent_l',
    'config': {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    }
  },
  {
    'prop_name': 'leg_ik_parent_r',
    'config': {
      'min': 0,
      'max': 2,
      'description': '0-root | 1-foot | 2-torso',
      'default': 1
    }
  },
  {
    'prop_name': 'arm_fk_to_ik_l',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'arm_fk_to_ik_r',
    'config': {
      'default': True
    }
  },
  {
    'prop_name': 'arm_ik_parent_l',
    'config': {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    }
  },
  {
    'prop_name': 'arm_ik_parent_r',
    'config': {
      'min': 0,
      'max': 4,
      'description': '0-root | 1-torso | 2-org_spine_01 | 3-org_chest | 4-org_head',
      'default': 0
    }
  }
]

def _add_custom_props (custom_props_config):
  # 获取 pose bones，如果之前没有切换到 POSE模式，必须先切换一次，之后获取不用切换
  # 到 POSE 也能获取到
  set_mode('POSE')
  pose_bone = get_pose_bone('props')

  for item in custom_props_config:
    prop_name = item['prop_name']
    config = item['config']
    # 创建属性
    pose_bone[prop_name] = config['default']
    _config = { k: v for k, v in config.items() if k != 'default' }

    # 创建属性后才有 ui
    if len(_config.keys()):
      ui = pose_bone.id_properties_ui(prop_name)
      # 更新默认配置
      ui.update(**_config)

  pose_bone['initialized'] = True
  set_mode('EDIT')

def add_custom_props (scene, config):
  _add_custom_props(custom_props_config)
  