from ..libs.blender_utils import (
  extrude_bone_, 
  copy_bone_,
  delete_bones,
  get_edit_bone,
)

from .init_parent import init_parent
from ..bone_patch import bone_patchs
from .init_org_bones import init_org_bones
from .init_arm_config import init_arm_config
from .init_leg_config import init_leg_config
from .init_hand_config import init_hand_config
from .init_torso_config import init_torso_config
from .init_props_config import init_props_config

def delete_tmp_bones ():
  delete_bones([get_edit_bone('mch_ik_arm.l.001'), get_edit_bone('mch_ik_leg.l.001')])

def _init_bones (config, scene = None):
  for bone_config in config:
    name = bone_config['name']
    source = bone_config['source']
    operator = bone_config['operator']
    operator_config = bone_config['operator_config']
    scale_factor = operator_config.get('scale_factor')

    if operator == 'extrude':
      target = operator_config.get('target')
      target_head_or_tail = operator_config.get('target_head_or_tail')
      head_or_tail = operator_config['head_or_tail']
      
      extrude_bone_(name, source, head_or_tail, scale_factor, target, target_head_or_tail)
    else:
      copy_bone_(name, source, scale_factor)

    if name in bone_patchs:
      cbs = bone_patchs[name]

      if isinstance(cbs, list):
        for cb in cbs:
          cb(scene, bone_config)
      else:
        cbs(scene, bone_config)

def init_bones (scene):
  init_org_bones()
  config = init_hand_config()
  config = init_arm_config(scene, config)
  config = init_torso_config(config)
  config = init_props_config(config)
  config = init_leg_config(scene, config)
  _init_bones(config, scene)
  init_parent()
  delete_tmp_bones()

  return config
