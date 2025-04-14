from ..libs.blender_utils import add_scene_custom_prop

from ..colors.init_ball_colors import init_ball_color
from .add_human_collections_color import get_palettes

def update_color (self, context):
  init_ball_color(context.scene)

def add_ball_collections_color ():
  palettes = get_palettes()
  add_scene_custom_prop(
    'ball_color', 
    'Enum',
    palettes[9][0], 
    items = palettes,
    update = update_color
  )
