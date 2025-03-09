from ..libs.blender_utils import get_pose_bone, get_active_object, set_mode
from .init_torso import init_torso
from .init_arm import init_arm
from .init_leg import init_leg

def add_driver (name, index, config):
  pose_bone = get_pose_bone(name)
  constraint = pose_bone.constraints[index]
  prop = config['name']
  type = config['type']
  vars = config['vars']

  if constraint.type == 'ARMATURE':
    targets = pose_bone.constraints[0].targets
    expression = config.get('expression')

    for index, target in enumerate(targets):
      target.driver_remove(prop)
      driver = target.driver_add(prop).driver
      driver.type = type
      
      for var in vars:
        name = var['name']
        _targets = var['targets']

        for i, __target in enumerate(_targets):
          id_type = __target['id_type']
          data_path = __target['data_path']
          _var = driver.variables.new()
          _var.name = name
          ___target = _var.targets[i]
          ___target.id_type = id_type
          ___target.id = get_active_object()
          ___target.data_path = data_path

        if expression:
          driver.expression = expression[index]
        else:
          driver.expression = f'{ name } == { index }'
  else:
    constraint.driver_remove(prop)
    driver = constraint.driver_add(prop).driver
    driver.type = type
    
    for var in vars:
      name = var['name']
      targets = var['targets']
      _var = driver.variables.new()
      _var.name = name

      for index, target in enumerate(targets):
        id_type = target['id_type']
        data_path = target['data_path']
        _target = _var.targets[index]
        _target.id_type = id_type
        _target.id = get_active_object()
        _target.data_path = data_path

def init_drivers ():

  torso_config = init_torso()
  arm_config = init_arm()
  leg_config = init_leg()
  configs = [torso_config, arm_config, leg_config]
  # 可能会导致未知的问题，比如另一边的驱动器必须打开再关闭才生效
  set_mode('POSE')

  for config in configs:
    for item in config:
      name = item['name']
      index = item['index']
      config = item['config']

      add_driver(name, index, config)
