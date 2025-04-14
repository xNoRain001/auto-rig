from . import init_bones
from ..parent import init_bones_parent
from .init_ball_config import init_ball_config
from ..parent.init_ball_parent import init_ball_parent_config

def init_ball_bones (scene):
  config = init_ball_config(scene)
  init_bones(config, scene)
  init_bones_parent(init_ball_parent_config(scene))

  return config
