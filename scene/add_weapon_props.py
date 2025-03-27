import json
from ..libs.blender_utils import (
  get_context, 
  get_pose_bone, 
  update_view,
  add_scene_custom_prop,
  get_current_frame,
  set_current_frame,
  get_active_object,
  insert_whole_character
)

from ..const import weapon_custom_prop_prefix

def get_world_matrix (armature, pose_bone):
  world_matrix = armature.matrix_world @ pose_bone.matrix
  arm_eval = armature.evaluated_get(get_context().view_layer.depsgraph)

  return arm_eval.matrix_world.inverted() @ world_matrix

def get_offset_matrix (armature, pose_bone):
  m1 = armature.matrix_world @ pose_bone.bone.matrix_local
  m2 = armature.matrix_world @ pose_bone.matrix

  return m2 - m1

def prev_frame_insert_whole_character ():
  frame = get_current_frame()
  set_current_frame(frame - 1)
  insert_whole_character()
  set_current_frame(frame)
  update_view()

def update_weapon_parent (prop, weapon_name, default):
  old_value = default

  def update (self, context):
    nonlocal old_value
    value = self[prop]

    if old_value == value:
      return
    
    props_bone = get_pose_bone('props')
    armature = get_active_object()
    weapon = get_pose_bone(weapon_name)
    mch_parent_weapon = get_pose_bone('mch_parent_' + weapon_name)
    prev_frame_insert_whole_character()
    world_matrix = get_world_matrix(armature, weapon)
    self[prop] = props_bone[prop] = value
    mch_parent_weapon.matrix = world_matrix
    update_view()
    weapon.matrix = world_matrix
    insert_whole_character()
    old_value = value

  return update

def update_weapon_to_master (prop, weapon_name, default):
  old_value = default

  def update (self, context):
    nonlocal old_value
    # TODO: self[prop] 的值为什么是数字 0 或 1
    value = bool(self[prop])

    if old_value == value:
      return
    
    armature = get_active_object()
    weapon = get_pose_bone(weapon_name)
    weapon_master = get_pose_bone(weapon_name + '_master')
    ik_hand_l = get_pose_bone('ik_hand.l')
    ik_hand_r = get_pose_bone('ik_hand.r')
    world_matrix = get_world_matrix(armature, weapon)
    _world_matrix = get_world_matrix(armature, ik_hand_l)
    __world_matrix = get_world_matrix(armature, ik_hand_r)
    props_bone = get_pose_bone('props')
    prev_frame_insert_whole_character()
    self[prop] = props_bone[prop] = value
    weapon_master.matrix = world_matrix
    update_view()
    ik_hand_l.matrix = _world_matrix
    ik_hand_r.matrix = __world_matrix
    update_view()
    weapon.matrix = world_matrix
    insert_whole_character()
    old_value = value

  return update

def update_weapon_master_parent (prop, weapon_name, default):
  old_value = default

  def update (self, context):
    nonlocal old_value
    value = self[prop]

    if old_value == value:
      return
    
    weapon_master = get_pose_bone(weapon_name + '_master')
    armature = get_active_object()
    world_matrix = get_world_matrix(armature, weapon_master)
    props_bone = get_pose_bone('props')
    prev_frame_insert_whole_character()
    self[prop] = props_bone[prop] = value
    weapon_master.matrix = world_matrix
    update_view()
    weapon_master.matrix = world_matrix
    insert_whole_character()
    old_value = value

  return update

def init_items (parents):
  items = []
    
  for parent in parents:
    items.append((parent, parent, ''))

  return items

def get_parents (prop):
  props_bone = get_pose_bone('props')
  return json.loads(props_bone.id_properties_ui(prop).as_dict()['description'])

# weapon_props 有值 -> 追加
# weapon_props 没有值 -> 初始化
def add_weapon_props (new_weapons = None):
  props_bone = get_pose_bone('props')
  weapons = new_weapons or json.loads(props_bone.get('weapons', '[]'))

  for weapon in weapons:
    prefix = weapon_custom_prop_prefix + weapon
    weapon_parent = f'{ prefix }_parent'
    weapon_to_master = f'{ prefix }_to_master'
    weapon_master_parent = f'{ prefix }_master_parent'
    weapon_parents = get_parents(weapon_parent)
    weapon_master_parents = get_parents(weapon_master_parent)
    weapon_parent_default = props_bone[weapon_parent]
    weapon_to_master_default = props_bone[weapon_to_master]
    weapon_master_parent_default = props_bone[weapon_master_parent]

    add_scene_custom_prop(
      weapon_parent, 
      'Enum', 
      default = weapon_parent_default,
      items = init_items(weapon_parents), 
      update = update_weapon_parent(
        weapon_parent, 
        weapon,
        weapon_parent_default
      )
    )
    add_scene_custom_prop(
      weapon_to_master, 
      'Bool',  
      default = weapon_to_master_default,
      update = update_weapon_to_master(
        weapon_to_master, 
        weapon,
        weapon_to_master_default
      )
    )
    add_scene_custom_prop(
      weapon_master_parent, 
      'Enum', 
      default = weapon_master_parent_default,
      items = init_items(weapon_master_parents),
      update = update_weapon_master_parent(
        weapon_master_parent, 
        weapon,
        weapon_master_parent_default
      )
    )
