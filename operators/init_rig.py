from ..scene.add_rotation_mode import set_rotation_mode
from ..libs.blender_utils import (
  set_mode,
  select_bone,
  get_edit_bone,
  symmetrize_bones,
  get_operator,
  get_edit_bones,
  active_object_,
  report_warning,
  symmetrize_bones_,
)

from ..bones import init_bones
from ..constraints import init_constraints
from ..drivers import init_drivers
# from ..operators import 

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

def check_bone_name (self):
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

  def _check_bone_name (bone_names):
    passing = True

    for bone_name in bone_names:
      bone = get_edit_bone(bone_name)

      if not bone:
        passing = False
        report_warning(self, f'绑定失败，缺少骨骼：{ bone_name }')

        break

    return passing

  bone_names = gen_bone_names()
  passing = _check_bone_name(bone_names)
  return passing

def check_parent_setting (self):
  passing = True
  parent_list = [['def_leg.l', 'def_hips'], ['def_leg.r', 'def_hips']]

  for item, parent in parent_list:
    if get_edit_bone(item).parent != get_edit_bone(parent):
      passing = False
      report_warning(self, f'{ item } parent is not { parent }')

      break

  return passing

def check_armature (self, armature):
  passing = True

  if not armature:
    passing = False
    report_warning(self, '缺少骨架')

  # 如果此时处于网格编辑模式下，必须先激活骨骼再切换到编辑模式，这样才是骨骼编辑模式
  active_object_(armature)
  set_mode('EDIT')

  return passing

def run_checker (self, context):
  scene = context.scene
  armature = scene.armature
  side_01_head_location = scene.side_01_head_location_
  side_02_head_location = scene.side_02_head_location
  heel_location = scene.heel_location
  foot_tip_location = scene.foot_tip_location
  passing = True
  checkers = [
    check_armature, 
    check_foot_ctrl, 
    check_bone_name, 
    check_parent_setting
  ]
  params = [
    [self, armature],
    [
      self,
      side_01_head_location,
      side_02_head_location,
      heel_location,
      foot_tip_location
    ],
    [self],
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

def symmetrize_bones ():
  set_mode('EDIT')
  bones = get_edit_bones()

  for bone in bones:
    if bone.name.endswith('.l'):
      select_bone(bone)

  symmetrize_bones_()
  
class OBJECT_OT_init_rig (get_operator()):
  bl_idname = 'object.init_rig'
  bl_label = 'Init Rig'

  def invoke(self, context, event):
    passing = run_checker(self, context)
  
    if passing:
      return self.execute(context)
    else:
      return {'CANCELLED'}

  def execute(self, context):
    scene = context.scene
    # TODO: 相关骨骼全部显示
    # set_rotation_mode(armature, rotation_mode)
    init_bones(scene)
    init_constraints()
    symmetrize_bones()
    init_drivers()

    return {'FINISHED'}
