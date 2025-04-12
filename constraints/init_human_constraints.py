from . import def_bone_add_copy_transforms
from .init_arm_config import init_arm_config
from .init_leg_config import init_leg_config
from .init_hand_config import init_hand_config
from .init_torso_config import init_torso_config

def init_human_constraints_config ():
  config = init_torso_config()
  config = init_hand_config(config)
  config = init_arm_config(config)
  config = init_leg_config(config)
  def_bone_add_copy_transforms()

  return config
    