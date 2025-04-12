from . import init_bones
from ..parent import init_bones_parent
from .init_org_bones import init_org_bones
from .init_bow_config import init_bow_config
from ..parent.init_bow_parent import init_bow_parent_config

def init_bow_bones (scene):
  config = init_bow_config(scene)
  init_org_bones()
  init_bones(config, scene)
  init_bones_parent(init_bow_parent_config())

  return config
