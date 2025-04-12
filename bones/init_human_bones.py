from ..libs.blender_utils import delete_bones, get_edit_bone

from . import init_bones
from ..parent import init_bones_parent
from .init_org_bones import init_org_bones
from .init_arm_config import init_arm_config
from .init_leg_config import init_leg_config
from .init_hand_config import init_hand_config
from .init_torso_config import init_torso_config
from .init_props_config import init_props_config
from ..parent.init_human_parent import init_human_parent_config

def delete_tmp_bones ():
  delete_bones([get_edit_bone('mch_ik_arm.l.001'), get_edit_bone('mch_ik_leg.l.001')])

def init_human_bones (scene):
  init_org_bones()
  config = init_hand_config()
  config = init_arm_config(scene, config)
  config = init_torso_config(config)
  config = init_props_config(config)
  config = init_leg_config(scene, config)
  init_bones(config, scene)
  init_bones_parent(init_human_parent_config())
  delete_tmp_bones()

  return config
