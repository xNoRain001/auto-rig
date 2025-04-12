from ..libs.blender_utils import (
  set_mode,
  get_pose_bones,
  add_ik_constraint,
  add_armature_constraint,
  add_transform_constraint,
  add_copy_scale_constraint,
  add_stretch_to_constraint,
  add_damped_track_constraint,
  add_copy_rotation_constraint,
  add_copy_location_constraint,
  add_limit_rotation_constraint,
  add_limit_location_constraint,
  add_copy_transforms_constraint,
)

from ..constraint_patch import constraint_patchs

constraint_map = {
  'IK': add_ik_constraint,
  'ARMATURE': add_armature_constraint,
  'TRANSFORM': add_transform_constraint,
  'STRETCH_TO': add_stretch_to_constraint,
  'COPY_SCALE': add_copy_scale_constraint,
  'DAMPED_TRACK': add_damped_track_constraint,
  'COPY_LOCATION': add_copy_location_constraint,
  'COPY_ROTATION': add_copy_rotation_constraint,
  'LIMIT_ROTATION': add_limit_rotation_constraint,
  'LIMIT_LOCATION': add_limit_location_constraint,
  'COPY_TRANSFORMS': add_copy_transforms_constraint
}

def def_bone_add_copy_transforms ():
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
      add_copy_transforms_constraint(name, org_name)

def init_bone_constraints (config):
  set_mode('POSE')

  for constraint_config in config:
    name = constraint_config['name']
    type = constraint_config['type']
    config = constraint_config.get('config')
    constraint_map[type](name, **config)

    if name in constraint_patchs:
      cbs = constraint_patchs[name]

      if isinstance(cbs, list):
        for cb in cbs:
          cb(constraint_config)
      else:
        cbs(constraint_config)
