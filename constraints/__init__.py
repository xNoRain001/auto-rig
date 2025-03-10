from .init_torso import init_torso
from .init_hand import init_hand
from .init_arm import init_arm
from .init_leg import init_leg
from ..libs.blender_utils import (
  set_mode,
  add_copy_transforms_constraint,
  add_copy_location_constraint,
  add_copy_scale_constraint,
  add_copy_rotation_constraint,
  add_stretch_to_constraint,
  add_armature_constraint,
  add_damped_track_constraint,
  add_ik_constraint,
  add_limit_rotation_constraint,
  get_pose_bones
)

strategies = {
  'IK': add_ik_constraint,
  'ARMATURE': add_armature_constraint,
  'STRETCH_TO': add_stretch_to_constraint,
  'COPY_SCALE': add_copy_scale_constraint,
  'DAMPED_TRACK': add_damped_track_constraint,
  'COPY_LOCATION': add_copy_location_constraint,
  'COPY_ROTATION': add_copy_rotation_constraint,
  'LIMIT_ROTATION': add_limit_rotation_constraint,
  'COPY_TRANSFORMS': add_copy_transforms_constraint
}

def def_bone_add_copy_transforms (armature = None):
  set_mode('POSE')
  pose_bones = get_pose_bones()
  
  for pose_bone in pose_bones:
    name = pose_bone.name

    if name.startswith('def_'):
      org_name = name.replace('def_', 'org_')
      constraints = pose_bone.constraints

      # 清空骨骼的所有约束
      while len(constraints):
        constraints.remove(constraints[0])

      # 如果里面才进入 POSE，每一次循环都会切换模式，性能非常差，推测相同模式之间切换
      # 也会造成性能影响
      # tip: transforms 约束不进入 POSE 也能添加
      add_copy_transforms_constraint(name, org_name, target = armature)

def _init_constraints (config):
  set_mode('POSE')

  for item in config:
    name = item['name']
    target = item['target']
    type = item['type']
    config = item.get('config') or {}

    if type == 'LIMIT_ROTATION':
      strategies[type](name, **config)
    else:
      strategies[type](name, target, **config)

def init_constraints ():
  torso_config = init_torso()
  hand_config = init_hand()
  arm_config = init_arm()
  leg_config = init_leg()
  def_bone_add_copy_transforms()
  configs = [torso_config, hand_config, arm_config, leg_config]

  for config in configs:
    _init_constraints(config)
    