from ..libs.blender_utils import get_types, add_scene_custom_prop

from ..colors.init_human_colors import init_human_color

def get_palettes ():
  palettes = []
  enum_items = get_types('BoneColor').bl_rna.properties['palette'].enum_items

  for index, enum_item in enumerate(enum_items):
    name = enum_item.name
    identifier = enum_item.identifier
    icon = enum_item.icon
    palettes.append((identifier, name, '', icon, index))

  return palettes

def update_color (self, context):
  init_human_color(context.scene)

def add_human_collections_color ():
  palettes = get_palettes()
  add_scene_custom_prop(
    'torso_color', 
    'Enum',
    palettes[4][0], 
    items = palettes,
    update = update_color
  )
  add_scene_custom_prop(
    'fk_ik_l_color', 
    'Enum',
    palettes[1][0], 
    items = palettes,
    update = update_color
  )
  add_scene_custom_prop(
    'fk_ik_r_color', 
    'Enum',
    palettes[3][0], 
    items = palettes,
    update = update_color
  )
  add_scene_custom_prop(
    'tweak_color', 
    'Enum',
    palettes[9][0], 
    items = palettes,
    update = update_color
  )
