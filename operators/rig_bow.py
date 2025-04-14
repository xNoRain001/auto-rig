from ..libs.blender_utils import (
  set_mode,
  select_bone,
  get_edit_bone,
  get_operator,
  get_edit_bones,
  active_object_,
  report_warning,
  symmetrize_bones_,
  deselect_bones
)

from ..bones_roll import init_bones_roll
from ..constraints import init_bone_constraints
from ..bones.init_bow_bones import init_bow_bones
from ..bones_roll.bow_roll_map import init_bow_roll
from ..collections.init_bow_collections import init_bow_collections
from ..constraints.init_bow_constraints import init_bow_constraints_config

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
  passing = True
  checkers = [
    check_armature, 
    check_bone_name
  ]
  params = [
    [self, armature],
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

class OBJECT_OT_rig_bow (get_operator()):
  bl_idname = 'object.rig_bow'
  bl_label = 'Rig Bow'

  def execute(self, context):
    scene = context.scene
    armature = scene.bow_armature
    active_object_(armature)
    set_mode('EDIT')
    init_bones_roll(init_bow_roll())
    bow_config = init_bow_bones(scene)
    init_bone_constraints(init_bow_constraints_config())
    init_bow_collections(bow_config)

    return {'FINISHED'}
