from collections import defaultdict

from . import init_bones_color
from ..const import ball_collection

def gen_color_map (scene):
  ball_color = scene.ball_color
  color_map = defaultdict(list)
  color_map[ball_color].append(ball_collection)

  return color_map

def init_ball_color (scene):
  init_bones_color(gen_color_map(scene))
