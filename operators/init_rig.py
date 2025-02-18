from ..const import custom_props_config
from ..scene import set_rotation_mode
from ..libs.blender_utils import (
  set_mode,
  select_bone,
  deselect,
  get_edit_bone,
  extrude_bone,
  get_pose_bone,
  add_stretch_to_constraint,
  copy_bone,
  set_parent,
  add_copy_location_constraints,
  add_copy_scale_constraints,
  add_copy_rotation_constraints,
  add_damped_track_constraints,
  add_ik_constraints,
  add_limit_rotation_constraints,
  add_copy_transforms_constraints,
  add_armature_constraints,
  symmetrize_bones,
  get_context,
  get_armature,
  get_ops,
  get_operator,
  get_active_object,
  get_edit_bones,
  duplicate,
  def_add_copy_transforms,
  active_object_,
  report_warning,
  get_object_,
  select_bone_head,
  select_bone_tail,
  snap_cursor,
  snap_selected_to_cursor
)

def gen_tweak_tip_bone (bone, tweak_bones, mch_switch_bones):
  name = bone.name.replace('org_', 'tweak_tip_')
  tweak_tip_bone = extrude_bone(
    bone, 
    'tail', 
    (0, bone.length / 2, 0), 
    use_connect = False,
    name = name,
    parent = mch_switch_bones[-1],
    parent_connect = False
  )
  tweak_bones.append(tweak_tip_bone)
  leg_or_arm_bone_names.append(name)

def org_bone_add_stretch_to (bones, tweak_bones):
  for index, bone in enumerate(bones):
    add_stretch_to_constraint(bone, tweak_bones[index + 1])

def get_leg_or_arm_bones (type):
  leg_or_arm_bones = []
  template = []
  inner_leg_or_arm_bones = []

  if type == 'leg':
    template.extend([
      'org_leg_01.l', 'org_leg_02.l', 'org_leg_03.l', 'org_leg_04.l',
      'org_shin_01.l', 'org_shin_02.l', 'org_shin_03.l', 'org_shin_04.l'
    ])
    leg_or_arm_bone_names.extend(['org_leg.l', 'org_shin.l', 'org_foot.l'])
    org_toes= get_edit_bone('org_toes.l')

    if org_toes: 
      leg_or_arm_bone_names.append('org_toes.l')
  else:
    template.extend([
      'org_arm_01.l', 'org_arm_02.l', 'org_arm_03.l', 'org_arm_04.l',
      'org_forearm_01.l', 'org_forearm_02.l', 'org_forearm_03.l', 'org_forearm_04.l'
    ])
    leg_or_arm_bone_names.extend(['org_arm.l', 'org_forearm.l', 'org_hand.l'])

  for leg_or_arm_bone_name in leg_or_arm_bone_names:
    leg_or_arm_bones.append(get_edit_bone(leg_or_arm_bone_name))

  for inner_leg_or_arm_bone_name in template:
    bone = get_edit_bone(inner_leg_or_arm_bone_name)

    if bone:
      inner_leg_or_arm_bones.append(bone)
      leg_or_arm_bone_names.append(bone.name)
  
  return [leg_or_arm_bones, inner_leg_or_arm_bones]

def set_ik_stretch (ik_bones) :
   get_pose_bone(ik_bones[0]).ik_stretch = 0.01
   get_pose_bone(ik_bones[1]).ik_stretch = 0.01

def gen_mch_twist_bone (leg_or_arm_bone, type):
  new_bone_length = leg_or_arm_bone.length / 4
  name_suffix = 'leg' if type == 'leg' else 'arm'

  mch_leg_or_arm = extrude_bone(
    leg_or_arm_bone, 'head', 
    (0, 0, new_bone_length), 
    name = f'mch_{ name_suffix }.l'
  )
  mch_int_leg_or_arm = copy_bone(
    mch_leg_or_arm, 
    f'mch_int_{ name_suffix }.l', 
    0.5, 
    get_edit_bone('root'), 
    False
  )
  mch_twist_leg_or_arm = extrude_bone(
    leg_or_arm_bone, 
    'head', 
    (0, 0, -new_bone_length), 
    name = f'mch_twist_{ name_suffix }.l'
  )
  select_bone(mch_twist_leg_or_arm)
  get_context().active_object.data.edit_bones.active = leg_or_arm_bone
  get_armature().align()
  deselect()
  set_parent(mch_twist_leg_or_arm, mch_leg_or_arm, False)

  leg_or_arm_bone_names.extend([
    mch_leg_or_arm.name,
    mch_int_leg_or_arm.name,
    mch_twist_leg_or_arm.name
  ])

  return [mch_int_leg_or_arm, mch_twist_leg_or_arm]

def gen_ik_and_fk_bones (
  bone, 
  mch_switch_bones, 
  tweak_bones, 
  fk_bones, 
  ik_bones
):
  org_bone_name = bone.name
  mch_switch_bone_name = org_bone_name.replace('org_', 'mch_switch_')
  mch_switch_bone = copy_bone(bone, mch_switch_bone_name, 1)
  fk_bone_name = org_bone_name.replace('org_', 'fk_')
  fk_bone = copy_bone(bone, fk_bone_name, 1)

  add_mch_prefix = True
  if (
    org_bone_name.startswith('org_toes') or
    org_bone_name.startswith('org_hand')
  ):
    add_mch_prefix = False

  ik_bone_name = org_bone_name.replace('org_', f"{ 'mch_' if add_mch_prefix else '' }" + 'ik_')
  ik_bone = copy_bone(bone, ik_bone_name, 1)
  tweak_bone_name = org_bone_name.replace('org_', 'tweak_')
  tweak_bone = copy_bone(bone, tweak_bone_name, 0.5, mch_switch_bone, False)
  set_parent(bone, tweak_bone, False)
  mch_switch_bones.append(mch_switch_bone)
  tweak_bones.append(tweak_bone)
  fk_bones.append(fk_bone)
  ik_bones.append(ik_bone)

  leg_or_arm_bone_names.extend([
    mch_switch_bone.name,
    fk_bone.name,
    ik_bone.name,
    tweak_bone.name
  ])

def gen_mch_tweak_bones (tweak_bones, mch_tweak_bones):
  for index, tweak_bone in enumerate(tweak_bones):
     if index > 0:
      mch_tweak_bone_name = tweak_bone.name.replace('tweak_', 'mch_tweak_')
      mch_tweak_bone = copy_bone(
        tweak_bone, 
        mch_tweak_bone_name, 
        0.5
      )
      set_parent(tweak_bone, mch_tweak_bone, False)
      mch_tweak_bones.append(mch_tweak_bone)
      leg_or_arm_bone_names.append(mch_tweak_bone_name)

def connect_bones (
  mch_int_leg_or_arm, 
  mch_twist_leg_or_arm, 
  ik_bones, 
  fk_bones, 
  mch_switch_bones, 
  tweak_bones,
  mch_ik_parent_bone,
  type
):
  set_parent(tweak_bones[0], mch_twist_leg_or_arm, False)

  for index, value in enumerate(mch_switch_bones):
    if index == 0:
       set_parent(value, mch_int_leg_or_arm, False)
       set_parent(ik_bones[0], mch_int_leg_or_arm, False)
       set_parent(fk_bones[0], mch_int_leg_or_arm, False)
    else:
       set_parent(value, mch_switch_bones[index - 1], True)
       set_parent(ik_bones[index], ik_bones[index - 1], True)
       set_parent(fk_bones[index], fk_bones[index - 1], True)

  if type == 'arm':
    set_parent(ik_bones[2], mch_ik_parent_bone, False)

def gen_foot_roll (mch_ik_foot, fk_foot, scene):
  bone = get_edit_bone('org_foot.l')
  mch_foot_roll_bone = extrude_bone(
    bone, 
    'tail', 
    (0, bone.length, 0), 
    name = 'mch_foot_roll.l',
    clear_parent = True,
    roll = True
  )


  heel_location = scene.heel_location
  select_bone_tail(mch_foot_roll_bone)
  snap_cursor(heel_location)
  snap_selected_to_cursor()
  deselect()
 
  foot_bone = copy_bone(mch_foot_roll_bone, 'ik_foot.l', clear_parent = True)
  foot_tip_location = scene.foot_tip_location
  select_bone_head(foot_bone)
  snap_cursor(foot_tip_location)
  snap_selected_to_cursor()
  deselect()
  # select_bone_tail(foot_bone)
  # snap_cursor(heel_location)
  # snap_selected_to_cursor()
  mch_parent_foot = copy_bone(foot_bone, 'mch_parent_ik_foot.l', 0.5, clear_parent = True)
  set_parent(foot_bone, mch_parent_foot, False)
  # TODO: ??? 这根骨头是做什么的
  # mch_ik_fk_foot_bone = copy_bone(
  #   foot_bone, 
  #   f'mch_ik_fk_{ foot_bone.name }', 
  #   0.25, 
  #   fk_foot, 
  #   False
  # )
  set_parent(mch_ik_foot, mch_foot_roll_bone, False)
  deselect()
  mch_roll_side_bone1 = extrude_bone(
    mch_foot_roll_bone, 
    'tail', 
    (mch_foot_roll_bone.length / 2, 0, 0), 
    name = 'mch_roll_side_01.l',
    parent = foot_bone,
    parent_connect = False,
    roll = True,
    roll_type = 'GLOBAL_POS_Y'
  )

  mch_roll_side_bone2 = copy_bone(mch_roll_side_bone1, 'mch_roll_side_02.l', 1)
  select_bone(mch_roll_side_bone2)
  get_armature().switch_direction()
  set_parent(mch_roll_side_bone2, mch_roll_side_bone1, False)
  deselect()
  select_bone(mch_roll_side_bone1)
  ops = get_ops()
  ops.transform.transform(mode = 'BONE_ROLL', value = (3.14159, 0, 0, 0))
  deselect()

  mch_foot_heel_bone = extrude_bone(
    mch_foot_roll_bone, 
    'tail', 
    (0, 0, mch_foot_roll_bone.length / 2), 
    name = 'mch_foot_heel.l',
    parent = mch_roll_side_bone2,
    parent_connect = False,
    roll = True
  )
  set_parent(mch_foot_roll_bone, mch_foot_heel_bone, False)

  foot_heel_bone = copy_bone(
    mch_foot_heel_bone, 
    'foot_heel.l', 
    1, 
    parent = foot_bone, 
    use_connect = False,
    roll = True
  )
  select_bone(foot_heel_bone)
  ops.transform.translate(value = (0, 0.1, 0))
  deselect()


  side_01_head_location = scene.side_01_head_location
  side_02_head_location = scene.side_02_head_location
  select_bone_head(mch_roll_side_bone1)
  select_bone_tail(mch_roll_side_bone2)
  snap_cursor(side_01_head_location)
  snap_selected_to_cursor()
  select_bone_head(mch_roll_side_bone2)
  select_bone_tail(mch_roll_side_bone1)
  snap_cursor(side_02_head_location)
  snap_selected_to_cursor()
  deselect()


  mch_foot_roll_bone_name = mch_foot_roll_bone.name
  mch_foot_heel_bone_name = mch_foot_heel_bone.name
  foot_heel_bone_name = foot_heel_bone.name
  mch_roll_side_bone1_name = mch_roll_side_bone1.name
  mch_roll_side_bone2_name = mch_roll_side_bone2.name
  mch_parent_foot_name = mch_parent_foot.name

  leg_or_arm_bone_names.extend([
    mch_foot_roll_bone_name,
    foot_bone.name,
    mch_roll_side_bone1_name,
    mch_roll_side_bone2_name,
    mch_foot_heel_bone_name,
    foot_heel_bone_name,
    mch_parent_foot_name,
    # mch_ik_fk_foot_bone.name
  ])

  return [
    mch_foot_roll_bone_name, 
    mch_foot_heel_bone_name,
    foot_heel_bone_name,
    mch_roll_side_bone1_name,
    mch_roll_side_bone2_name,
    mch_parent_foot_name
  ]

def bones_to_bone_names (bones):
  bone_names = []

  for bone in bones:
    bone_names.append(bone.name)

  return bone_names

def mch_tweak_bone_add_copy_scale (mch_tweak_bone_names):
  for mch_tweak_bone_name in mch_tweak_bone_names:
    add_copy_scale_constraints(mch_tweak_bone_name, 'root')

def mch_int_leg_or_arm_bone_add_constraints (tyoe):
  add_copy_location_constraints(f'mch_int_{ tyoe }.l', f'mch_{ tyoe }.l')
  add_copy_rotation_constraints(f'mch_int_{ tyoe }.l', f'mch_{ tyoe }.l')
  
def mch_twist_bone_add_constraints (type):
  suffix = 'leg' if type == 'leg' else 'arm'
  add_copy_location_constraints(f'mch_twist_{ suffix }.l', f'mch_switch_{ suffix }.l')
  add_damped_track_constraints(f'mch_twist_{ suffix }.l', f'mch_switch_{ suffix }.l', head_tail = 1)

def ik_bone_add_ik (ik_bone_names, pole_subtarget):
  add_ik_constraints(ik_bone_names[1], ik_bone_names[2], 2, pole_subtarget)
  set_ik_stretch(ik_bone_names)

def foot_roll_add_constraints (
  mch_foot_roll_bone_name, 
  mch_foot_heel_bone_name, 
  foot_heel_bone_name, 
  mch_roll_side_bone1_name, 
  mch_roll_side_bone2_name
):
  add_copy_rotation_constraints(mch_foot_heel_bone_name, foot_heel_bone_name, use_y = False, use_z = False, owner_space = 'LOCAL', target_space = 'LOCAL')
  add_limit_rotation_constraints(mch_foot_heel_bone_name, use_limit_x = True, min_x = -180, max_x = 0, use_legacy_behavior = True, owner_space = 'LOCAL')
  add_copy_rotation_constraints(mch_foot_roll_bone_name, foot_heel_bone_name, use_y = False, use_z = False, owner_space = 'LOCAL', target_space = 'LOCAL')
  add_limit_rotation_constraints(mch_foot_roll_bone_name, use_limit_x = True, min_x = 0, max_x = 180, use_legacy_behavior = True, owner_space = 'LOCAL')
  add_copy_rotation_constraints(mch_roll_side_bone1_name, foot_heel_bone_name, use_x = False, use_y = False, owner_space = 'LOCAL', target_space = 'LOCAL')
  add_limit_rotation_constraints(mch_roll_side_bone1_name, use_limit_z = True, min_z = 0, max_z = 180, use_legacy_behavior = True, owner_space = 'LOCAL')
  add_copy_rotation_constraints(mch_roll_side_bone2_name, foot_heel_bone_name, use_x = False, use_y = False, owner_space = 'LOCAL', target_space = 'LOCAL')
  add_limit_rotation_constraints(mch_roll_side_bone2_name, use_limit_z = True, min_z = -180, max_z = 0, use_legacy_behavior = True, owner_space = 'LOCAL')

def mch_switch_bone_add_constraints(
  mch_switch_bone_names, 
  fk_bone_names, 
  ik_bone_names
):
  for index, value in enumerate(mch_switch_bone_names):
    add_copy_transforms_constraints(value, fk_bone_names[index])
    add_copy_transforms_constraints(value, ik_bone_names[index])

def mch_switch_bone_add_driver (mch_switch_bone_names, type, direction):
  set_mode('POSE')
  name_prefix = 'leg' if type == 'leg' else 'arm'

  for mch_switch_bone_name in mch_switch_bone_names:
    mch_switch_bone_name = mch_switch_bone_name.replace('.l', f'.{ direction }')
    pose_bone = get_pose_bone(mch_switch_bone_name)
    constraint = pose_bone.constraints[-1]
    constraint.driver_remove("influence")
    fcurve = constraint.driver_add("influence")
    driver = fcurve.driver
    driver.type = 'AVERAGE'
    var = driver.variables.new()
    var.name = f'{ name_prefix }_fk_to_ik.{ direction }'.replace('.', '_')
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = get_active_object()
    var.targets[0].data_path = f'pose.bones["props"]["{ name_prefix }_fk_to_ik.{ direction }"]'

def mch_ik_toes_add_copy_rotation (bone, target):
  add_copy_rotation_constraints(
    bone, 
    target, 
    target_space = 'LOCAL', 
    owner_space = 'LOCAL',
    use_x = True,
    use_y = False,
    use_z = False
  )

def gen_mch_ik_toes(ik_toes, ik_foot):
  mch_ik_toes_bone = copy_bone(ik_toes, 'mch_ik_toes.l', 0.5, ik_foot, roll = True)
  set_parent(ik_toes, mch_ik_toes_bone, False)
  leg_or_arm_bone_names.append(mch_ik_toes_bone.name)

def gen_leg_or_arm_pole_bone (ik_leg_or_arm, type, fk_leg_or_arm, scene):
  name_suffix = 'leg' if type == 'leg' else 'arm'
  tmp = copy_bone(ik_leg_or_arm, scale_factor = 1)
  select_bone(tmp)
  normal = scene.leg_pole_normal if type == 'leg' else scene.arm_pole_normal
  flag = 1 if len(normal) == 1 else -1
  direction = normal if len(normal) == 1 else normal[1]
  if direction == 'X':
    get_ops().transform.translate(value = (0.5 * flag, 0, 0), orient_type = 'NORMAL')
  else:
    get_ops().transform.translate(value = (0, 0, 0.5 * flag), orient_type = 'NORMAL')

  deselect()
  mch_parent_leg_or_arm_pole = extrude_bone(tmp, 'tail', (0, 0.05 if type == 'leg' else -0.05, 0), name = f'mch_parent_{ name_suffix }_pole.l', clear_parent = True)
  leg_or_arm_pole_bone = copy_bone(mch_parent_leg_or_arm_pole, f'{ name_suffix }_pole.l', 2, mch_parent_leg_or_arm_pole, use_connect = False)
  vis_leg_or_arm_pole = extrude_bone(
    ik_leg_or_arm, 
    'tail', 
    leg_or_arm_pole_bone, 
    'tail', 
    name = f'vis_{ name_suffix }_pole.l'
  )
  select_bone(tmp)
  get_armature().delete()

  mch_ik_fk_leg_or_arm_pole_bone = copy_bone(
    leg_or_arm_pole_bone, 
    f'mch_ik_fk_{ leg_or_arm_pole_bone.name }',
    0.25,
    fk_leg_or_arm,
    False
  )

  leg_or_arm_bone_names.extend([
    mch_parent_leg_or_arm_pole.name, 
    leg_or_arm_pole_bone.name, 
    vis_leg_or_arm_pole.name,
    mch_ik_fk_leg_or_arm_pole_bone.name
  ])

  return [
    leg_or_arm_pole_bone.name, 
    vis_leg_or_arm_pole.name, 
    mch_parent_leg_or_arm_pole.name
  ]
  
def vis_leg_or_arm_pole_add_stretch_to (bone, target):
  add_stretch_to_constraint (bone, target, 1)

def mch_parent_leg_or_arm_pole_add_driver (name, type, direction):
  set_mode('POSE')

  name_prefix = 'leg' if type == 'leg' else 'arm'
  bone_name = name.replace('.l', f'.{ direction }')
  pose_bone = get_pose_bone(bone_name)
  targets = pose_bone.constraints[0].targets

  for index, target in enumerate(targets):
    target.driver_remove("weight")
    fcurve = target.driver_add("weight")
    driver = fcurve.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name = f'{ name_prefix }_ik_parent.{ direction }'.replace('.', '_')
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = get_active_object()
    var.targets[0].data_path = f'pose.bones["props"]["{ name_prefix }_ik_parent.{ direction }"]'
    driver.expression = f'{ var.name } == { index }'

def mch_parent_foot_add_driver (name, type):
  set_mode('POSE')

  bone_name = name.replace('.l', f'.{ type }')
  pose_bone = get_pose_bone(bone_name)
  targets = pose_bone.constraints[0].targets
  drivers = []

  for target in targets:
    target.driver_remove("weight")
    fcurve = target.driver_add("weight")
    driver = fcurve.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name = f'leg_ik_parent.{ type }'.replace('.', '_')
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = get_active_object()
    var.targets[0].data_path = f'pose.bones["props"]["leg_ik_parent.{ type }"]'
    drivers.append(driver)
  
  drivers[0].expression = f'{ var.name } == 0 or { var.name } == 1'
  drivers[1].expression = f'{ var.name } == 2'

def gen_inner_tweak_bone (
  inner_leg_or_arm_bones,
  leg_or_arm_bone,
  shin_or_forearm_bone,
  inner_tweak_bones
):
  for bone in inner_leg_or_arm_bones:
    name = bone.name
    parent = leg_or_arm_bone if name.startswith('org_leg') or name.startswith('org_arm') else shin_or_forearm_bone
    tweak_bone = copy_bone(bone, name.replace('org_', 'tweak_'), 0.5, parent, False)
    set_parent(bone, tweak_bone, False)
    inner_tweak_bones.append(tweak_bone)
    leg_or_arm_bone_names.append(tweak_bone.name)
    
def inner_bone_add_stretch_to (inner_leg_or_arm_bone_names, inner_tweak_bone_names):
  for index, name in enumerate(inner_leg_or_arm_bone_names):
    add_stretch_to_constraint(name, inner_tweak_bone_names[index + 1])

def inner_bone_add_copy_rotation (
  inner_leg_or_arm_bone_names,
  mch_swith_leg_or_arm_name,
  org_foot_or_hand_name
):
  for bone_name in inner_leg_or_arm_bone_names:
    if bone_name == 'org_arm_01.l' or bone_name == 'org_leg_01.l':
      add_copy_rotation_constraints(bone_name, mch_swith_leg_or_arm_name, influence = 0.1)
    if bone_name == 'org_arm_02.l' or bone_name == 'org_leg_02.l':
      add_copy_rotation_constraints(bone_name, mch_swith_leg_or_arm_name, influence = 0.3)
    if bone_name == 'org_arm_03.l' or bone_name == 'org_leg_03.l':
      add_copy_rotation_constraints(bone_name, mch_swith_leg_or_arm_name, influence = 0.7)
    if bone_name == 'org_arm_04.l' or bone_name == 'org_leg_04.l':
      add_copy_rotation_constraints(bone_name, mch_swith_leg_or_arm_name)
    if bone_name == 'org_forearm_01.l' or bone_name == 'org_shin_01.l':
      add_copy_rotation_constraints(bone_name, org_foot_or_hand_name, influence = 0.1)
    if bone_name == 'org_forearm_02.l' or bone_name == 'org_shin_02.l':
      add_copy_rotation_constraints(bone_name, org_foot_or_hand_name, influence = 0.3)
    if bone_name == 'org_forearm_03.l' or bone_name == 'org_shin_03.l':
      add_copy_rotation_constraints(bone_name, org_foot_or_hand_name, influence = 0.7)
    if bone_name == 'org_forearm_04.l' or bone_name == 'org_shin_04.l':
      add_copy_rotation_constraints(bone_name, org_foot_or_hand_name)
  
leg_or_arm_bone_names = []

def gen_mch_ik_parent_bone (ik_foot_or_hand):
  bone_name = f'mch_parent_{ ik_foot_or_hand.name }'
  mch_ik_parent_bone = copy_bone(ik_foot_or_hand, bone_name, 0.5, clear_parent = True)
  leg_or_arm_bone_names.append(bone_name)

  return mch_ik_parent_bone

def gen_tweak_tip_finger_bone (org_bone, tweak_bone, stretch_to_target_list):
  name = org_bone.name.replace('org_', 'tweak_tip_')
  tweak_tip_bone = extrude_bone(
    org_bone, 
    'tail', 
    (0, org_bone.length / 2, 0), 
    use_connect = False,
    name = name,
    parent = tweak_bone.parent,
    parent_connect = False
  )

  stretch_to_target_list.append(name)
  leg_or_arm_bone_names.append(name)

def gen_fk_chain (
  org_bones, 
  parent, 
  rotation_owner_list, 
  rotation_target_list,
  stretch_to_owner_list,
  stretch_to_target_list,
  mch_bone_names
):
  for org_bone in org_bones:
    org_bone_name = org_bone.name
    mch_bone = copy_bone(org_bone, org_bone_name.replace('org_', 'mch_'), 0.25, parent)
    fk_bone = copy_bone(org_bone, org_bone_name.replace('org_', ''), 1, mch_bone, False)
    tweak_bone = copy_bone(org_bone, org_bone_name.replace('org_', 'tweak_'), 0.5, fk_bone, False)
    set_parent(org_bone, tweak_bone, False)
    
    stretch_to_owner_list.append(org_bone_name)

    if parent:
      stretch_to_target_list.append(tweak_bone.name)
    else:
      mch_bone_names.append(mch_bone.name)

    if org_bone_name.endswith('_03.l'):
      rotation_owner_list.append(mch_bone.name)
      rotation_target_list.append(parent.name)

    children = org_bone.children
    leg_or_arm_bone_names.extend([
      org_bone_name,
      mch_bone.name,
      fk_bone.name,
      tweak_bone.name
    ])

    if len(children):
      gen_fk_chain(
        children, 
        fk_bone, 
        rotation_owner_list, 
        rotation_target_list,
        stretch_to_owner_list,
        stretch_to_target_list,
        mch_bone_names
      )
    else:
      gen_tweak_tip_finger_bone(org_bone, tweak_bone, stretch_to_target_list)

def finger_add_copy_rotation (rotation_owner_list, rotation_target_list):
  for index, bone_name in enumerate(rotation_owner_list):
    add_copy_rotation_constraints(
      bone_name, 
      rotation_target_list[index],
      target_space = 'LOCAL',
      owner_space = 'LOCAL'
    )

def finger_add_stretch_to(stretch_to_owner_list, stretch_to_target_list):
  for index, bone_name in enumerate(stretch_to_owner_list):
    add_stretch_to_constraint(bone_name, stretch_to_target_list[index])

def finger_master_add_copy_rotation (mch_bone_names):
  target = mch_bone_names[-1]
  add_copy_rotation_constraints(
    mch_bone_names[2], 
    target,
    target_space = 'LOCAL',
    owner_space = 'LOCAL',
    influence = 0.25
  )
  add_copy_rotation_constraints(
    mch_bone_names[3], 
    target,
    target_space = 'LOCAL',
    owner_space = 'LOCAL',
    influence = 0.6
  )

def gen_torso_fk_bone (org_bones):
  org_hips = org_bones[0]
  org_spine_01 = org_bones[1]
  org_spine_02 = org_bones[2]
  org_chest = org_bones[3]
  org_neck = org_bones[4]
  org_head = org_bones[5]

  torso = extrude_bone(
    org_spine_02, 
    'head', 
    (0, org_spine_02.length * 2, 0),
    name = 'torso',
    parent = get_edit_bone('root'),
    parent_connect = False
  )
  chest = copy_bone(torso, 'chest', 0.75, torso, False)
  hips = copy_bone(torso, 'hips', 0.5, torso, False)

  fk_spine_01 = extrude_bone(
    org_spine_02, 
    'head', 
    (0, 0, org_spine_02.length), 
    parent = hips,
    parent_connect = False,
    name = 'fk_spine_01'
  )
  select_bone(fk_spine_01)
  get_active_object().data.edit_bones.active = org_spine_01
  get_armature().align()
  deselect()

  fk_hips = extrude_bone(
    org_hips, 
    'tail', 
    (0, 0, org_hips.length), 
    name = 'fk_hips', 
    parent = fk_spine_01,
    parent_connect = False
  )
  select_bone(fk_hips)
  get_active_object().data.edit_bones.active = org_hips
  get_armature().align()
  deselect()

  fk_spine_02 = copy_bone(
    org_spine_02, 
    'fk_spine_02', 
    1, 
    parent = chest,
    use_connect = False
  )
  fk_chest = copy_bone(
    org_chest, 
    'fk_chest', 
    1, 
    parent = fk_spine_02,
    use_connect = False
  )
  neck = copy_bone(
    org_neck, 
    'neck', 
    1, 
    parent = fk_chest,
    use_connect = False
  )
  head = copy_bone(
    org_head, 
    'head', 
    1, 
    parent = neck,
    use_connect = False
  )

  return [
    fk_hips,
    fk_spine_01,
    fk_spine_02,
    fk_chest,
    neck,
    head,
    chest,
    hips,
    torso
  ]

def torso_follow_add_driver (mch_int_neck_name, mch_int_head_name):
  bone = get_pose_bone(mch_int_neck_name)
  constraint = bone.constraints[-1]
  constraint.driver_remove("influence")
  fcurve = constraint.driver_add("influence")
  driver = fcurve.driver
  driver.type = 'AVERAGE'
  var = driver.variables.new()
  var.name = 'neck_follow'
  var.targets[0].id_type = 'OBJECT'
  var.targets[0].id = get_active_object()
  var.targets[0].data_path = 'pose.bones["props"]["neck_follow"]'

  bone = get_pose_bone(mch_int_head_name)
  constraint = bone.constraints[-1]
  constraint.driver_remove("influence")
  fcurve = constraint.driver_add("influence")
  driver = fcurve.driver
  driver.type = 'AVERAGE'
  var = driver.variables.new()
  var.name = 'head_follow'
  var.targets[0].id_type = 'OBJECT'
  var.targets[0].id = get_active_object()
  var.targets[0].data_path = 'pose.bones["props"]["head_follow"]'

def torso_follow (
  head, neck, fk_chest, fk_spine_02, chest, hips, torso,
  fk_spine_01, fk_hips
  ):
  mch_neck = extrude_bone(
    neck, 
    'head', 
    (0, neck.length / 2, 0), 
    name = 'mch_neck', 
    parent = fk_chest, 
    parent_connect = False
  )
  mch_int_neck = copy_bone(
    mch_neck, 
    'mch_int_neck', 
    0.5, 
    get_edit_bone('root'), 
    False
  )
  set_parent(neck, mch_int_neck, False)

  mch_head = extrude_bone(
    head, 
    'head', 
    (0, head.length / 2, 0), 
    name = 'mch_head', 
    parent = neck, 
    parent_connect = False
  )
  mch_int_head = copy_bone(
    mch_head, 
    'mch_int_head', 
    0.5, 
    get_edit_bone('root'), 
    False
  )
  set_parent(head, mch_int_head, False)

  mch_chest_fk = extrude_bone(
    fk_chest, 
    'head', 
    (0, fk_chest.length / 2, 0), 
    name = 'mch_fk_chest', 
    parent = fk_spine_02, 
    parent_connect = False
  )
  set_parent(fk_chest, mch_chest_fk, False)
  mch_spine_02_fk = extrude_bone(
    fk_spine_02, 
    'head', 
    (0, fk_spine_02.length / 2, 0), 
    name = 'mch_fk_spine_02', 
    parent = torso, 
    parent_connect = False
  )
  set_parent(fk_spine_02, mch_spine_02_fk, False)
  mch_spine_01_fk = extrude_bone(
    fk_spine_01, 
    'head', 
    (0, fk_spine_01.length / 2, 0), 
    name = 'mch_fk_spine_01', 
    parent = torso, 
    parent_connect = False
  )
  set_parent(fk_spine_01, mch_spine_01_fk, False)
  mch_hips_fk = extrude_bone(
    fk_hips, 
    'head', 
    (0, fk_hips.length / 2, 0), 
    name = 'mch_fk_hips', 
    parent = fk_spine_01, 
    parent_connect = False
  )
  set_parent(fk_hips, mch_hips_fk, False)

  mch_spine_02_pivot = copy_bone(fk_spine_01, 'mch_spine_02_pivot', 0.5, fk_spine_02, False)
  tweak_spine_02 = get_edit_bone('tweak_spine_02')
  set_parent(tweak_spine_02, mch_spine_02_pivot, False)

  mch_neck_name = mch_neck.name
  mch_int_neck_name = mch_int_neck.name
  mch_head_name = mch_head.name
  mch_int_head_name = mch_int_head.name
  mch_chest_fk_name = mch_chest_fk.name
  mch_spine_02_fk_name = mch_spine_02_fk.name
  mch_spine_01_fk_name = mch_spine_01_fk.name
  mch_hips_fk_name = mch_hips_fk.name
  chest_name = chest.name
  hips_name = hips.name
  fk_spine_01_name = fk_spine_01.name
  mch_spine_02_pivot_name = mch_spine_02_pivot.name

  set_mode('POSE')
  add_copy_transforms_constraints(mch_spine_02_pivot_name, fk_spine_01_name, influence = 0.5)
  add_copy_transforms_constraints(mch_chest_fk_name, chest_name, target_space = 'LOCAL', owner_space = 'LOCAL', influence = 0.5)
  add_copy_transforms_constraints(mch_spine_02_fk_name, chest_name, target_space = 'LOCAL', owner_space = 'LOCAL', influence = 0.5)
  add_copy_transforms_constraints(mch_spine_01_fk_name, hips_name, target_space = 'LOCAL', owner_space = 'LOCAL', influence = 0.5)
  add_copy_transforms_constraints(mch_hips_fk_name, hips_name, target_space = 'LOCAL', owner_space = 'LOCAL', influence = 0.5)

  add_copy_location_constraints(mch_int_neck_name, mch_neck_name)
  add_copy_scale_constraints(mch_int_neck_name, mch_neck_name)
  add_copy_rotation_constraints(mch_int_neck_name, mch_neck_name)
  add_copy_location_constraints(mch_int_head_name, mch_head_name)
  add_copy_scale_constraints(mch_int_head_name, mch_head_name)
  add_copy_rotation_constraints(mch_int_head_name, mch_head_name)
  torso_follow_add_driver(mch_int_neck_name, mch_int_head_name)

def torso_stretch_to (org_bone_names, tweak_bone_names):
  for index, org_bone_name in enumerate(org_bone_names):
    add_stretch_to_constraint(org_bone_name, tweak_bone_names[index + 1])

def gen_org_bones ():
  def select_def_bones (edit_bones):
    for edit_bone in edit_bones:
      name = edit_bone.name

      if name.startswith('def_'):
        # 隐藏的骨骼也会被选中
        select_bone(edit_bone)

  def rename_org_bones (edit_bones):
    for edit_bone in edit_bones:
      if edit_bone.select:
        edit_bone.name = (
          edit_bone.name
            .replace('def_', 'org_')
            .replace('.001', '')
        )
  
  deselect()
  edit_bones = get_edit_bones()
  select_def_bones(edit_bones)
  # 隐藏的骨骼不会被复制
  duplicate()
  rename_org_bones(edit_bones)
  deselect()

def gen_prop_bone ():
  props_bone = get_edit_bone('props')

  if not props_bone:
    head = get_edit_bone('org_head')
    extrude_bone(
      head, 
      'tail', 
      (0, 0, head.length), 
      name = 'props',
      parent = get_edit_bone('root'), 
      parent_connect = False
    )

def add_custom_props ():
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
      ui.update(**_config)

def rig_leg_or_arm (type, scene):
  set_mode('EDIT')
  deselect()

  mch_switch_bones = []
  tweak_bones = []
  mch_tweak_bones = []
  fk_bones = []
  ik_bones = []
  leg_or_arm_bones, inner_leg_or_arm_bones = get_leg_or_arm_bones(type)
  inner_tweak_bones = []

  if len(inner_leg_or_arm_bones):
    gen_inner_tweak_bone(
      inner_leg_or_arm_bones, 
      leg_or_arm_bones[0], 
      leg_or_arm_bones[1],
      inner_tweak_bones
    )
  
  mch_int_leg_or_arm, mch_twist_leg_or_arm = gen_mch_twist_bone(
    leg_or_arm_bones[0], 
    type
  )

  for leg_or_arm_bone in leg_or_arm_bones:
    gen_ik_and_fk_bones(
      leg_or_arm_bone, 
      mch_switch_bones, 
      tweak_bones, 
      fk_bones, 
      ik_bones
    )

  # 因为 tweak_leg 不需要 mch_tweak_leg 处理缩放，因此不放入循环里
  gen_mch_tweak_bones(tweak_bones, mch_tweak_bones)
  gen_tweak_tip_bone(leg_or_arm_bones[-1], tweak_bones, mch_switch_bones)
  set_mode('EDIT')
  (
    leg_or_arm_pole_bone_name, 
    vis_leg_or_arm_pole_name, 
    mch_parent_leg_or_arm_pole_name
  ) = gen_leg_or_arm_pole_bone(
    ik_bones[0], type, fk_bones[0], scene
  )
  if type == 'arm':
    mch_ik_parent_bone = gen_mch_ik_parent_bone(ik_bones[2])
    mch_ik_parent_bone_name = mch_ik_parent_bone.name
  else:
    # 脚架中会生成
    mch_ik_parent_bone = None

  connect_bones(
    mch_int_leg_or_arm, 
    mch_twist_leg_or_arm, 
    ik_bones, 
    fk_bones, 
    mch_switch_bones, 
    tweak_bones,
    mch_ik_parent_bone,
    type
  )

  bone_names = bones_to_bone_names(leg_or_arm_bones)
  tweak_bone_names = bones_to_bone_names(tweak_bones)
  mch_tweak_bone_names = bones_to_bone_names(mch_tweak_bones)
  mch_switch_bone_names = bones_to_bone_names(mch_switch_bones)
  ik_bone_names = bones_to_bone_names(ik_bones)
  fk_bone_names = bones_to_bone_names(fk_bones)
  inner_leg_or_arm_bone_names = bones_to_bone_names(inner_leg_or_arm_bones)
  inner_tweak_bone_names = bones_to_bone_names(inner_tweak_bones)
  ik_toes = ik_bone_names[-1] == 'ik_toes.l'

  if type == 'leg':
    inner_tweak_bone_names.append('tweak_foot.l')
    (
      mch_foot_roll_bone_name, 
      mch_foot_heel_bone_name, 
      foot_heel_bone_name, 
      mch_roll_side_bone1_name, 
      mch_roll_side_bone2_name, 
      mch_parent_foot_name
    ) = gen_foot_roll(ik_bones[2], fk_bones[2], scene)

    if ik_toes:
      gen_mch_ik_toes(ik_bones[-1], ik_bones[-2])
  else:
    inner_tweak_bone_names.append('tweak_hand.l')
  
  # 接下来的所有操作都在 pose mode 进行
  org_bone_add_stretch_to(bone_names, tweak_bone_names)
  vis_leg_or_arm_pole_add_stretch_to(vis_leg_or_arm_pole_name, leg_or_arm_pole_bone_name)

  if len(inner_leg_or_arm_bone_names):
    # 复制旋转要在拉伸前面
    inner_bone_add_copy_rotation(
      inner_leg_or_arm_bone_names,
      mch_switch_bone_names[0],
      leg_or_arm_bone_names[2]
    )
    inner_bone_add_stretch_to(inner_leg_or_arm_bone_names, inner_tweak_bone_names)

  if type == 'leg':
    add_armature_constraints(mch_parent_leg_or_arm_pole_name, ['root', 'ik_foot.l', 'torso'])
    add_armature_constraints(mch_parent_foot_name, ['root', 'torso'])
    mch_parent_foot_add_driver(mch_parent_foot_name, 'l')
    foot_roll_add_constraints(
      mch_foot_roll_bone_name, 
      mch_foot_heel_bone_name, 
      foot_heel_bone_name, 
      mch_roll_side_bone1_name, 
      mch_roll_side_bone2_name
    )

    if ik_toes:
      mch_ik_toes_add_copy_rotation('mch_ik_toes.l', mch_foot_roll_bone_name)
  else:
    add_armature_constraints(mch_parent_leg_or_arm_pole_name, ['root', 'torso', 'org_spine_01', 'chest', 'head'])
    add_armature_constraints(mch_ik_parent_bone_name, ['root', 'torso', 'org_spine_01', 'chest', 'head'])
    mch_parent_leg_or_arm_pole_add_driver(mch_ik_parent_bone_name, type, 'l')
    
  # TODO: fix 骨架约束必须关闭再打开才生效
  mch_parent_leg_or_arm_pole_add_driver(mch_parent_leg_or_arm_pole_name, type, 'l')
  mch_tweak_bone_add_copy_scale(mch_tweak_bone_names)
  mch_int_leg_or_arm_bone_add_constraints(type)
  mch_twist_bone_add_constraints(type)
  ik_bone_add_ik(ik_bone_names, leg_or_arm_pole_bone_name)
  mch_switch_bone_add_constraints(
    mch_switch_bone_names, 
    fk_bone_names, 
    ik_bone_names
  )
  mch_switch_bone_add_driver(mch_switch_bone_names, type, 'l')
  # 对称
  symmetrize_bones(leg_or_arm_bone_names)
  
  mch_switch_bone_add_driver(mch_switch_bone_names, type, 'r')
  mch_parent_leg_or_arm_pole_add_driver(mch_parent_leg_or_arm_pole_name, type, 'r')
  
  if type == 'leg':
    mch_parent_foot_add_driver(mch_parent_foot_name, 'r')
  else:
    mch_parent_leg_or_arm_pole_add_driver(mch_ik_parent_bone_name, type, 'r')

  leg_or_arm_bone_names.clear()

def rig_hand ():
  set_mode('EDIT')

  org_bones = [
    get_edit_bone('org_thumb_01.l'),
    get_edit_bone('org_finger_a_01.l'),
    get_edit_bone('org_finger_b_01.l'),
    get_edit_bone('org_finger_c_01.l'),
    get_edit_bone('org_finger_d_01.l'),
  ]
  rotation_owner_list = []
  rotation_target_list = []
  stretch_to_owner_list = []
  stretch_to_target_list = []
  mch_bone_names = []

  gen_fk_chain(
    org_bones, 
    None, 
    rotation_owner_list, 
    rotation_target_list,
    stretch_to_owner_list,
    stretch_to_target_list,
    mch_bone_names
  )

  finger_add_stretch_to(stretch_to_owner_list, stretch_to_target_list)
  finger_add_copy_rotation(rotation_owner_list, rotation_target_list)
  finger_master_add_copy_rotation(mch_bone_names)

  symmetrize_bones(leg_or_arm_bone_names)
  leg_or_arm_bone_names.clear()

def rig_torso ():
  org_bone_names = [
    'org_hips',
    'org_spine_01',
    'org_spine_02',
    'org_chest',
    'org_neck',
    'org_head'
  ]
  org_bones = []

  for org_bone_name in org_bone_names:
    org_bones.append(get_edit_bone(org_bone_name))
  
  tweak_bone_names = []

  org_hips = get_edit_bone('org_hips'),
  org_spine_01 = get_edit_bone('org_spine_01'),
  org_spine_02 = get_edit_bone('org_spine_02'),
  org_chest = get_edit_bone('org_chest'),
  org_neck = get_edit_bone('org_neck'),
  org_head = get_edit_bone('org_head'),

  fk_hips, fk_spine_01, fk_spine_02, fk_chest, neck, head, chest, hips, torso = gen_torso_fk_bone(org_bones)

  for org_bone in org_bones:
    org_bone_name = org_bone.name
    tweak_bone = copy_bone(org_bone, org_bone_name.replace('org_', 'tweak_'), 0.5, clear_parent = True)
    set_parent(org_bone, tweak_bone, False)
    tweak_bone_names.append(tweak_bone.name)

    if org_bone_name == 'org_hips':
      set_parent(tweak_bone, fk_hips, False)
    elif org_bone_name == 'org_spine_01':
      set_parent(tweak_bone, fk_hips, False)
    elif org_bone_name == 'org_spine_02':
      set_parent(tweak_bone, fk_spine_01, False)
    elif org_bone_name == 'org_chest':
      set_parent(tweak_bone, fk_chest, False)
    elif org_bone_name == 'org_neck':
      set_parent(tweak_bone, neck, False)
    elif org_bone_name == 'org_head':
      set_parent(tweak_bone, head, False)

  org_head = org_bones[-1]
  tweak_top_bone = extrude_bone(
    org_head, 
    'tail', 
    (0, 0, head.length / 4), 
    name = 'tweak_top_head', 
    parent = head, 
    parent_connect = False
  )
  tweak_bone_names.append(tweak_top_bone.name)

  torso_follow(
    head, neck, fk_chest, fk_spine_02, chest, hips, torso,
    fk_spine_01, fk_hips
  )
  torso_stretch_to(org_bone_names, tweak_bone_names)

def check_foot_ctrl (
  self,
  side_01_head_location,
  side_02_head_location,
  heel_location,
  foot_tip_location
):
  passing = True

  if (
    side_01_head_location == 
    side_02_head_location == 
    heel_location == 
    foot_tip_location
  ):
    passing = False
    report_warning(self, '未设置脚部控制器位置')

  return passing

def check_bone_name (self, armature_name):
  def gen_bone_names ():
    bone_names = [
      'root',
      'def_hips', 'def_spine_01', 'def_spine_02', 'def_chest', 'def_neck',
      'def_head',
    ]
    helper = [
      'def_shoulder', 'def_arm', 'def_forearm', 'def_hand', 
      'def_thumb_01', 'def_thumb_02', 'def_thumb_03', 
      'def_finger_a_01', 'def_finger_a_02', 'def_finger_a_03', 
      'def_finger_b_01', 'def_finger_b_02', 'def_finger_b_03', 
      'def_finger_c_01', 'def_finger_c_02', 'def_finger_c_03', 
      'def_finger_d_01', 'def_finger_d_02', 'def_finger_d_03', 
      'def_leg', 'def_shin', 'def_foot', 'def_toes'
    ]
    sides = ['l', 'r']
    
    for side in sides:
      for item in helper:
        bone_names.append(f'{ item }.{ side }')

    return bone_names

  def find_error_bone_name (bone_names):
    passing = True

    for bone_name in bone_names:
      bone = get_edit_bone(bone_name)

      if not bone:
        passing = False
        report_warning(self, f'绑定失败，缺少骨骼：{ bone_name }')

        break

    return passing

  active_object_(get_object_(armature_name))
  set_mode('EDIT')
  bone_names = gen_bone_names()
  passing = find_error_bone_name(bone_names)
  return passing

def check_parent_setting (self):
  passing = True
  def_hips = get_edit_bone('def_hips')
  def_leg_l = get_edit_bone('def_leg.l')
  def_leg_r = get_edit_bone('def_leg.r')
  list = [[def_leg_l, def_hips], [def_leg_r, def_hips]]

  for item in list:
    if item[0].parent != item[1]:
      passing = False
      report_warning(self, f'{ item[0].name } parent is not { item[1].name }')

      break

  return passing

def run_checker (
  self,
  side_01_head_location,
  side_02_head_location,
  heel_location,
  foot_tip_location,
  armature_name
):
  passing = True
  checkers = [check_foot_ctrl, check_bone_name, check_parent_setting]
  params = [
    [
      self,
      side_01_head_location,
      side_02_head_location,
      heel_location,
      foot_tip_location
    ],
    [
      self,
      armature_name
    ],
    [self]
  ]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

def rename_shoulder ():
  set_mode('EDIT')
  get_edit_bone('org_shoulder.l').name = 'shoulder.l'
  get_edit_bone('org_shoulder.r').name = 'shoulder.r'

class OBJECT_OT_init_rig (get_operator()):
  bl_idname = 'object.init_rig'
  bl_label = 'Init Rig'

  def execute(self, context):
    scene = context.scene
    armature_name = scene.armature_name
    rotation_mode = scene.rotation_mode
    side_01_head_location = scene.side_01_head_location
    side_02_head_location = scene.side_02_head_location
    heel_location = scene.heel_location
    foot_tip_location = scene.foot_tip_location
    
    passing = run_checker(
      self,
      side_01_head_location,
      side_02_head_location,
      heel_location,
      foot_tip_location,
      armature_name
    )

    if passing:
      set_rotation_mode(armature_name, rotation_mode)
      gen_org_bones()
      gen_prop_bone()
      def_add_copy_transforms()
      add_custom_props()
      rig_leg_or_arm('leg', scene)
      rig_leg_or_arm('arm', scene)
      rig_hand()
      rig_torso()
      rename_shoulder()

    return {'FINISHED'}
