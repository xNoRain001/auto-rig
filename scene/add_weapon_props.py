import json
from ..libs.blender_utils import (
  get_context, 
  get_pose_bone, 
  update_view,
  add_timer,
  get_props,
  get_types
)
from ..const import weapon_custom_prop_prefix

def get_world_matrix (armature, pose_bone):
  world_matrix = armature.matrix_world @ pose_bone.matrix
  arm_eval = armature.evaluated_get(get_context().view_layer.depsgraph)
  return arm_eval.matrix_world.inverted() @ world_matrix

def getter (prop):
  def _getter (self):
    return self.get(prop)

  return _getter

def weapon_parent_setter (prop, weapon_name):
  def _setter (self, value):
    old_value = getattr(self, prop)

    if old_value == value:
      return
   
    context = get_context()
    weapon = get_pose_bone(weapon_name)
    armature = context.scene.armature
    world_matrix = get_world_matrix(armature, weapon)
    self[prop] = value

    def cb ():
      weapon.matrix = world_matrix

    add_timer(cb, 0.1)

  return _setter

def weapon_to_master_setter (prop, weapon_name):
  def _setter (self, value):
    old_value = getattr(self, prop)

    if old_value == value:
      return
   
    context = get_context()
    armature = context.scene.armature
    weapon = get_pose_bone(weapon_name)
    weapon_master = get_pose_bone(weapon_name + '_master')
    world_matrix = get_world_matrix(armature, weapon)
    self[prop] = value

    def cb ():
      weapon_master.matrix = world_matrix
      update_view()
      weapon.matrix = world_matrix

    add_timer(cb, 0.1)

  return _setter

def weapon_master_parent_setter (prop, weapon_name):
  def _setter (self, value):
    old_value = getattr(self, prop)

    if old_value == value:
      return
   
    context = get_context()
    weapon_master = get_pose_bone(weapon_name + '_master')
    armature = context.scene.armature
    world_matrix = get_world_matrix(armature, weapon_master)
    self[prop] = value

    def cb ():
      weapon_master.matrix = world_matrix

    add_timer(cb, 0.1)

  return _setter

def init_items (parents):
  items = []
    
  for index, parent in enumerate(parents):
    # 标识符需要为字符串
    items.append((str(index), parent, ''))

  return items

def get_parents (prop):
  props_bone = get_pose_bone('props')
  return json.loads(props_bone.id_properties_ui(prop).as_dict()['description'])

def add_weapon_props (new_weapons = None):
  props_bone = get_pose_bone('props')
  # weapon_props 有值，说明是追加，没有值，说明是初始化
  weapons = new_weapons or json.loads(props_bone.get('weapons', '[]'))
  PoseBone = get_types('PoseBone')
  EnumProperty = get_props('EnumProperty')
  BoolProperty = get_props('BoolProperty')

  for weapon in weapons:
    prefix = weapon_custom_prop_prefix + weapon
    weapon_parent = f'{ prefix }_parent'
    weapon_to_master = f'{ prefix }_to_master'
    weapon_master_parent = f'{ prefix }_master_parent'
    weapon_parents = get_parents(weapon_parent)
    weapon_master_parents = get_parents(weapon_master_parent)
    setattr(
      PoseBone, 
      weapon_parent, 
      EnumProperty(
        items = init_items(weapon_parents), 
        get = getter(weapon_parent),
        set = weapon_parent_setter(weapon_parent, weapon)
      )
    )
    setattr(
      PoseBone, 
      weapon_to_master, 
      BoolProperty(
        get = getter(weapon_to_master),
        set = weapon_to_master_setter(weapon_to_master, weapon)
      )
    )
    setattr(
      PoseBone, 
      weapon_master_parent, 
      EnumProperty(
        items = init_items(weapon_master_parents),
        get = getter(weapon_master_parent),
        set = weapon_master_parent_setter(weapon_master_parent, weapon)
      )
    )
