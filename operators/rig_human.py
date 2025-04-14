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
  deselect_bones
)

from ..const import identifier
from ..drivers import init_drivers
from ..bones_roll import init_bones_roll
from ..constraints import init_bone_constraints
from ..constraints.init_human_constraints import init_human_constraints_config
from ..bones.init_human_bones import init_human_bones
from ..bones_roll.human_roll_map import init_human_roll
from ..collections.init_human_collections import init_human_collections
from ..widgets.init_human_widgets import init_human_widgets
from ..hooks import (
  rename_bones,
  init_bone_colors,
  rename_bones_for_gi
)

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

def check_armature (self, armature):
  passing = True

  # TODO: delete
  if not armature:
    passing = False
    report_warning(self, '缺少骨架')
    return passing

  # 如果此时处于网格编辑模式下，必须先激活骨骼再切换到编辑模式，这样才是骨骼编辑模式
  active_object_(armature)
  set_mode('EDIT')

  return passing

def run_checker (self, context):
  scene = context.scene
  armature = scene.armature
  side_01_head_location = scene.side_01_head_location
  side_02_head_location = scene.side_02_head_location
  heel_location = scene.heel_location
  foot_tip_location = scene.foot_tip_location
  passing = True
  checkers = [
    check_armature, 
    check_foot_ctrl, 
    check_bone_name
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
    [self]
  ]

  for index, checker in enumerate(checkers):
    passing = checker(*params[index])

    if not passing:
      passing = False

      break

  return passing

def symmetrize_bones ():
  set_mode('EDIT')
  bones = get_edit_bones()

  for bone in bones:
    if bone.name.endswith('.l'):
      select_bone(bone)

  symmetrize_bones_()
  deselect_bones()

class OBJECT_OT_rig_human (get_operator()):
  bl_idname = 'object.rig_human'
  bl_label = 'Rig Human'

  def invoke(self, context, event):
    passing = run_checker(self, context)
  
    if passing:
      return self.execute(context)
    else:
      return {'CANCELLED'}

  def execute(self, context):
    scene = context.scene
    armature = scene.armature

    rename_bones_for_gi()
    init_bones_roll(init_human_roll())
    bone_config = init_human_bones(scene)
    init_bone_constraints(init_human_constraints_config(scene))
    init_human_widgets(bone_config, scene)
    symmetrize_bones()
    init_drivers()
    init_human_collections(bone_config)
    init_bone_colors(scene)
    rename_bones()

    armature[identifier] = True

    return {'FINISHED'}
