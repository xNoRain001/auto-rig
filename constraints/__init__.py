from .init_torso import init_torso
from .init_hand import init_hand
from .init_arm import init_arm
from .init_leg import init_leg
from ..libs.blender_utils import (
  set_mode,
  add_copy_transforms_constraints,
  add_copy_location_constraints,
  add_copy_scale_constraints,
  add_copy_rotation_constraints,
  add_stretch_to_constraint,
  add_armature_constraints,
  add_damped_track_constraints,
  add_ik_constraints,
  add_limit_rotation_constraints,
  get_pose_bones
)

strategies = {
  'IK': add_ik_constraints,
  'ARMATURE': add_armature_constraints,
  'STRETCH_TO': add_stretch_to_constraint,
  'COPY_SCALE': add_copy_scale_constraints,
  'DAMPED_TRACK': add_damped_track_constraints,
  'COPY_LOCATION': add_copy_location_constraints,
  'COPY_ROTATION': add_copy_rotation_constraints,
  'LIMIT_ROTATION': add_limit_rotation_constraints,
  'COPY_TRANSFORMS': add_copy_transforms_constraints
}

def def_bone_add_copy_transforms (armature = None):
  set_mode('POSE')
  pose_bones = get_pose_bones()
  
  for pose_bone in pose_bones:
    name = pose_bone.name

    if name.startswith('def_'):
      # TODO: 不一定存在
      org_name = name.replace('def_', 'org_')
      constraints = pose_bone.constraints

      # org_constraints = get_pose_bone(org_name).constraints
      # while len(org_constraints):
      #   org_constraints.remove(org_constraints[0])

      # 清空骨骼的所有约束
      while len(constraints):
        constraints.remove(constraints[0])

      # 如果里面才进入 POSE，每一次循环都会切换模式，性能非常差，推测相同模式之间切换
      # 也会造成性能影响
      # tip: transforms 约束不进入 POSE 也能添加
      add_copy_transforms_constraints(name, org_name, target = armature)

def init_constraints ():
  torso_config = init_torso()
  hand_config = init_hand()
  arm_config = init_arm()
  leg_config = init_leg()
  set_mode('POSE')

  def_bone_add_copy_transforms()

  configs = [torso_config, hand_config, arm_config, leg_config]

  for config in configs:
    for item in config:
      name = item['name']
      target = item['target']
      type = item['type']
      config = item.get('config') or {}

      if type == 'LIMIT_ROTATION':
        strategies[type](name, **config)
      else:
        # if type == 'COPY_LOCATION':
        #   print(name)
        strategies[type](name, target, **config)
