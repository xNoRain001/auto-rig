from collections import defaultdict

from . import init_bones_color
from ..const import bow_collection

def gen_color_map (scene):
  bow_color = scene.bow_color
  color_map = defaultdict(list)
  color_map[bow_color].append(bow_collection)

  return color_map

def init_bow_color (scene):
  init_bones_color(gen_color_map(scene))
