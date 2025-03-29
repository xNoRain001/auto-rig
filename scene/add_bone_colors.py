from ..libs.blender_utils import (
  add_scene_custom_prop, 
  get_types, 
  get_pose_bones,
  get_bone_collections,
  get_active_object
)

from ..hooks import init_bone_colors

def update_color (self, context):
  init_bone_colors(context.scene)

def add_bone_colors ():
  items = []
  enum_items = get_types('BoneColor').bl_rna.properties['palette'].enum_items

  for index, enum_item in enumerate(enum_items):
    name = enum_item.name
    identifier = enum_item.identifier
    icon = enum_item.icon
    items.append((identifier, name, '', icon, index))

  add_scene_custom_prop(
    'torso_color', 
    'Enum',
    items[4][0], 
    items = items,
    update = update_color
  )
  add_scene_custom_prop(
    'fk_ik_l_color', 
    'Enum',
    items[1][0], 
    items = items,
    update = update_color
  )
  add_scene_custom_prop(
    'fk_ik_r_color', 
    'Enum',
    items[3][0], 
    items = items,
    update = update_color
  )
  add_scene_custom_prop(
    'tweak_color', 
    'Enum',
    items[9][0], 
    items = items,
    update = update_color
  )
