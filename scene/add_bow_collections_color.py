from ..libs.blender_utils import add_scene_custom_prop

from ..colors.init_bow_colors import init_bow_color
from .add_human_collections_color import get_palettes

def update_color (self, context):
  init_bow_color(context.scene)

def add_bow_collections_color ():
  palettes = get_palettes()
  add_scene_custom_prop(
    'bow_color', 
    'Enum',
    palettes[9][0], 
    items = palettes,
    update = update_color
  )
