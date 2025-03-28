from ..libs.blender_utils import get_pose_bone, get_active_object, set_mode
from .init_torso_config import init_torso_config
from .init_arm_config import init_arm_config
from .init_leg_config import init_leg_config

def add_driver (name, index, config):
  pose_bone = get_pose_bone(name)
  constraint = pose_bone.constraints[index]
  prop = config['name']
  type = config['type']
  vars = config['vars']
  expression = config.get('expression')

  if constraint.type == 'ARMATURE':
    targets = pose_bone.constraints[0].targets

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

    if expression:
      driver.expression = expression
    
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

def _init_drivers (config):
  set_mode('POSE')

  for driver_config in config:
    name = driver_config['name']
    index = driver_config['index']
    config = driver_config['config']
    add_driver(name, index, config)

def init_drivers ():
  config = init_torso_config()
  config = init_arm_config(config)
  config = init_leg_config(config)
  _init_drivers(config)
