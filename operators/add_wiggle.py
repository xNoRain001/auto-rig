from ..libs.blender_utils import (
  get_operator, 
  get_selected_bones,
  copy_bone,
  add_stretch_to_constraint,
  add_damped_track_constraints,
  add_copy_transforms_constraints,
  set_mode,
  get_pose_bone,
  get_active_object,
  add_limit_rotation_constraints,
  get_edit_bone,
  get_mode,
  report_warning,
  is_pose_mode,
  get_selected_pose_bones,
)
from .init_rig import add_custom_props, gen_org_bones, def_bone_add_copy_transforms

def gen_tweak_bone (org_bone):
  tweak_bone_name = org_bone.name.replace('org_', 'tweak_')
  tweak_bone = copy_bone(org_bone, tweak_bone_name, 0.25, use_connect = False)
  org_bone.parent = tweak_bone

  return tweak_bone

def gen_fk_bone (tweak_bone):
  fk_bone_name = tweak_bone.name.replace('tweak_', '')
  fk_bone = copy_bone(tweak_bone, fk_bone_name, 2, use_connect = False)
  tweak_bone.parent = fk_bone

  return fk_bone

def gen_mch_bone (fk_bone):
  mch_bone_name = 'mch_' + fk_bone.name
  mch_bone = copy_bone(fk_bone, mch_bone_name, 0.5, use_connect = False)
  fk_bone.parent = mch_bone

  return mch_bone

def gen_mch_int_bone (mch_bone):
  mch_int_bone_name = mch_bone.name.replace('mch_', 'mch_int_')
  mch_int_bone = copy_bone(mch_bone, mch_int_bone_name, 0.5, use_connect = False)
  mch_bone.parent = mch_int_bone

  return mch_int_bone

def gen_phy_bone (mch_int_bone):
  phy_bone_name = mch_int_bone.name.replace('mch_int_', 'phy_')
  phy_bone = copy_bone(mch_int_bone, phy_bone_name, 3, use_connect = False)

  return phy_bone

def get_bone_names ():
  # 可能在 POSE 模式下选中骨骼
  set_mode('EDIT')
  bones = get_selected_bones()
  bone_names = []

  for bone in bones:
    bone_names.append(bone.name)

  for bone_name in bone_names:
    if bone_name.startswith('def_'):
      gen_org_bones()
      def_bone_add_copy_transforms()

      break

  for index, bone_name in enumerate(bone_names):
    if bone_name.startswith('def_'):
      bone_names[index] = bone_name.replace('def_', 'org_')

  return bone_names

def auto_fk (bone_name, parent, phy_bone_parent, stretch_bone_names, phy_bone_names, transforms_bone_names):
  set_mode('EDIT')
  bone = get_edit_bone(bone_name)
  tweak_bone = gen_tweak_bone(bone)
  fk_bone = gen_fk_bone(tweak_bone)
  mch_bone = gen_mch_bone(fk_bone)
  mch_int_bone = gen_mch_int_bone(mch_bone)
  phy_bone = gen_phy_bone(mch_int_bone)
  
  # 上一个 fk bone
  if parent:
    mch_int_bone.parent = parent
    stretch_bone_names.append([
      # org bone
      parent.children[0].children[0].name, 
      tweak_bone.name
    ])
    transforms_bone_names.append([
      mch_bone.name,
      parent.name
    ])

  phy_bone_name = phy_bone.name
  phy_bone_names.append(phy_bone_name)

  # 上一个 phy bone
  if phy_bone_parent:
    phy_bone.parent = phy_bone_parent

  children = bone.children
  if len(children):
    auto_fk(children[0].name, fk_bone, phy_bone, stretch_bone_names, phy_bone_names, transforms_bone_names)

def add_driver (pose_bone_name, wiggle_prop):
  pose_bone = get_pose_bone(pose_bone_name)
  constraints = pose_bone.constraints
  
  for constraint in constraints:
    if constraint.type == 'DAMPED_TRACK':
      constraint.driver_remove("influence")
      driver = constraint.driver_add("influence").driver
      driver.type = 'AVERAGE'
      var = driver.variables.new()
      var.name = wiggle_prop
      target = var.targets[0]
      target.id_type = 'OBJECT'
      target.id = get_active_object()
      target.data_path = f'pose.bones["props"]["{ wiggle_prop }"]'

def clear_list (stretch_bone_names, phy_bone_names, transforms_bone_names):
  stretch_bone_names.clear()
  phy_bone_names.clear()
  transforms_bone_names.clear()

def add_constraints (wiggle_prop, wiggle_influence, stretch_bone_names, phy_bone_names, transforms_bone_names):
  set_mode('POSE')
  last_index = len(phy_bone_names) - 1
 
  for index, phy_bone_name in enumerate(phy_bone_names):
    if index != last_index:
      add_damped_track_constraints(
        phy_bone_name, 
        phy_bone_names[index + 1], 
        influence = wiggle_influence
      )
      add_driver(phy_bone_name, wiggle_prop)
      add_limit_rotation_constraints(
        phy_bone_name, 
        owner_space = 'LOCAL', 
        use_limit_z = True,
        min_z = -180,
        max_z = 0
      )
    
    mch_int_bone_name = phy_bone_name.replace('phy_', 'mch_int_')
    add_copy_transforms_constraints(
      mch_int_bone_name, 
      phy_bone_name, 
      target_space = 'LOCAL', 
      owner_space = 'LOCAL'
    )
    
    # org_bone_name = phy_bone_name.replace('phy_', 'org_')
    # tweak_bone_name = phy_bone_name.replace('phy_', 'mch_')
  for item in stretch_bone_names:
    add_stretch_to_constraint(item[0], item[1])

  for item in transforms_bone_names:
    add_copy_transforms_constraints(
      item[0], 
      item[1], 
      target_space = 'LOCAL', 
      owner_space = 'LOCAL'
    )

  clear_list(stretch_bone_names, phy_bone_names, transforms_bone_names)

def check_wiggle_prop (self, wiggle_prop):
  passing = True

  if not wiggle_prop:
    passing = False
    report_warning(self, '控制摆动强度的自定义属性不能为空')

  return passing

def check_selected_bones (self):
  passing = True
  selected_bones = get_selected_pose_bones() if is_pose_mode() else get_selected_bones()

  # OBJECT 模式下 selected_bones 为 None
  if not selected_bones or not len(selected_bones):
    passing = False
    report_warning(self, '没有选中骨骼')
  else:
    for selected_bone in selected_bones:
      if not selected_bone.name.startswith(('def_', 'org_')):
        passing = False
        report_warning(self, '选中的骨骼中存在名称不以 def_ 或 org_ 开头的骨骼')

        break

  return passing

def run_checker (
  self,
  wiggle_prop
):
  passing = True
  checkers = [
    check_wiggle_prop, 
    check_selected_bones
  ]
  params = [
    [self, wiggle_prop],
    [self]
  ]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

def add_wiggle (wiggle_prop, wiggle_influence):
  mode = get_mode()
  # 最后需要添加约束，所以保存名称
  bone_names = get_bone_names()
  stretch_bone_names = []
  phy_bone_names = []
  transforms_bone_names = []

  for bone_name in bone_names:
    # fk bone 的父级是 mch bone，mch bone 的父级是 mch int bone,
    # 每一个 mch int bone 复制对应的 phy bone 的变换，
    # 当 phy bone 变换时，所有骨骼都会有相同的变换
    # mch int bone 的父级是上一个 fk bone，mch bone 复制上一个 fk_bone 的变换，
    # 当 fk bone 变换时，其他 fk bone 也会变换并且带有过渡效果
    auto_fk(bone_name, None, None, stretch_bone_names, phy_bone_names, transforms_bone_names)
    add_constraints(wiggle_prop, wiggle_influence, stretch_bone_names, phy_bone_names, transforms_bone_names)

  # 还原回最开始时的模式
  set_mode(mode)

class OBJECT_OT_add_wiggle (get_operator()):
  bl_idname = "object.add_wiggle"
  bl_label = "Add Wiggle"

  def execute(self, context):
    scene = context.scene
    wiggle_prop = scene.wiggle_prop
    passing = run_checker(
      self, 
      wiggle_prop
    )

    if passing:
      wiggle_influence = scene.wiggle_influence
      add_custom_props([{
        'prop_name': wiggle_prop,
        'config': {
          'min': 0,
          'max': 1,
          'default': wiggle_influence
        }
      }])
      add_wiggle(wiggle_prop, wiggle_influence)

    return {'FINISHED'}
