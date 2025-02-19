from ..libs.blender_utils import (
  get_operator, get_selected_bone, get_edit_bone, copy_bone, set_parent,
  set_mode, get_pose_bone, add_armature_constraints, add_copy_transforms_constraints,
  get_active_object
)
from .init_rig import add_custom_props

def gen_custom_props_config (weapon_name):
  custom_props_config =[
    {
      'prop_name': f'{ weapon_name }_parent',
      'config': {
        'min': 0,
        'max': 2,
        'description': '0-root | 1-hand.l | 2-hand.r',
        'default': 0
      },
      'is_visible': True
    },
    {
      'prop_name': f'{ weapon_name }_to_master',
      'config': {
        'default': False
      },
      'is_visible': True
    },
    {
      'prop_name': f'{ weapon_name }_master_parent',
      'config': {
        'min': 0,
        'max': 1,
        'description': '0-root | 1-torso',
        'default': 0
      },
      'is_visible': True
    }
  ]

  return custom_props_config

def rig_weapon (weapon_bone):
  weapon = weapon_bone.name
  custom_props_config = gen_custom_props_config(weapon)
  add_custom_props(custom_props_config)
  
  mch_parent_weapon = copy_bone(weapon_bone, f'mch_parent_{ weapon }', 0.5, clear_parent = True)
  mch_parent_weapon_to_master = copy_bone(weapon_bone, f'mch_parent_{ weapon }_to_master', 0.5, clear_parent = True)
  weapon_master = copy_bone(weapon_bone, f'{ weapon }_master', 1.5, clear_parent = True)
  mch_parent_weapon_master = copy_bone(weapon_master, f'mch_parent_{ weapon }_master', 0.5, clear_parent = True)
  mch_parent_ik_hand_l = get_edit_bone('mch_parent_ik_hand.l')
  mch_parent_ik_to_master_l = copy_bone(mch_parent_ik_hand_l, 'mch_parent_ik_to_master.l', parent = weapon_master, use_connect = False)
  mch_parent_ik_hand_r = get_edit_bone('mch_parent_ik_hand.r')
  mch_parent_ik_to_master_r = copy_bone(mch_parent_ik_hand_r, 'mch_parent_ik_to_master.r', parent = weapon_master, use_connect = False)
  set_parent(weapon_bone, mch_parent_weapon, use_connect = False)
  set_parent(mch_parent_weapon_to_master, weapon_master, use_connect = False)
  set_parent(weapon_master, mch_parent_weapon_master, use_connect = False)
  mch_parent_weapon_name = mch_parent_weapon.name
  mch_parent_weapon_master_name = mch_parent_weapon_master.name
  mch_parent_ik_hand_l_name = mch_parent_ik_hand_l.name
  mch_parent_ik_hand_r_name = mch_parent_ik_hand_r.name
  mch_parent_ik_to_master_l_name = mch_parent_ik_to_master_l.name
  mch_parent_ik_to_master_r_name = mch_parent_ik_to_master_r.name

  set_mode('POSE')
  constraints = get_pose_bone(mch_parent_ik_to_master_l_name).constraints
  while len(constraints):
    constraints.remove(constraints[0])
  constraints = get_pose_bone(mch_parent_ik_to_master_r_name).constraints
  while len(constraints):
    constraints.remove(constraints[0])

  add_armature_constraints(mch_parent_weapon_master_name, ['root', 'torso'])
  add_armature_constraints(mch_parent_weapon_name, ['root', 'org_hand.l', 'org_hand.r'])
  add_copy_transforms_constraints(mch_parent_weapon_name, f'mch_parent_{ weapon }_to_master')
  add_copy_transforms_constraints(mch_parent_ik_hand_l_name, 'mch_parent_ik_to_master.l')
  add_copy_transforms_constraints(mch_parent_ik_hand_r_name, 'mch_parent_ik_to_master.r')

  pose_bone = get_pose_bone(mch_parent_ik_hand_l_name)
  constraint = pose_bone.constraints[-1]
  constraint.driver_remove("influence")
  fcurve = constraint.driver_add("influence")
  driver = fcurve.driver
  driver.type = 'AVERAGE'
  var = driver.variables.new()
  var.name = f'{ weapon }_to_master'
  var.targets[0].id_type = 'OBJECT'
  var.targets[0].id = get_active_object()
  var.targets[0].data_path = f'pose.bones["props"]["{ weapon }_to_master"]'

  pose_bone = get_pose_bone(mch_parent_ik_hand_r_name)
  constraint = pose_bone.constraints[-1]
  constraint.driver_remove("influence")
  fcurve = constraint.driver_add("influence")
  driver = fcurve.driver
  driver.type = 'AVERAGE'
  var = driver.variables.new()
  var.name = f'{ weapon }_to_master'
  var.targets[0].id_type = 'OBJECT'
  var.targets[0].id = get_active_object()
  var.targets[0].data_path = f'pose.bones["props"]["{ weapon }_to_master"]'

  pose_bone = get_pose_bone(mch_parent_weapon_master_name)
  targets = pose_bone.constraints[0].targets

  for index, target in enumerate(targets):
    target.driver_remove("weight")
    fcurve = target.driver_add("weight")
    driver = fcurve.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name = 'master_parent'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = get_active_object()
    var.targets[0].data_path = f'pose.bones["props"]["{ weapon }_master_parent"]'
    driver.expression = f'{ var.name } == { index }'

  pose_bone = get_pose_bone(mch_parent_weapon_name)
  targets = pose_bone.constraints[0].targets

  for index, target in enumerate(targets):
    target.driver_remove("weight")
    fcurve = target.driver_add("weight")
    driver = fcurve.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name = f'{ weapon }_parent'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = get_active_object()
    var.targets[0].data_path = f'pose.bones["props"]["{ weapon }_parent"]'
    driver.expression = f'{ var.name } == { index }'

  constraint = pose_bone.constraints[-1]
  constraint.driver_remove("influence")
  fcurve = constraint.driver_add("influence")
  driver = fcurve.driver
  driver.type = 'AVERAGE'
  var = driver.variables.new()
  var.name = f'{ weapon }_to_master'
  var.targets[0].id_type = 'OBJECT'
  var.targets[0].id = get_active_object()
  var.targets[0].data_path = f'pose.bones["props"]["{ weapon }_to_master"]'

class OBJECT_OT_rig_weapon (get_operator()):
  bl_idname = "object.rig_weapon"
  bl_label = "Rig Weapon"

  def execute(self, context):
    weapon_bone = get_selected_bone()
    rig_weapon(weapon_bone)

    return {'FINISHED'}
