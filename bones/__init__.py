from .init_arm import init_arm
from .init_hand import init_hand
from .init_torso import init_torso
from .init_leg import init_leg
from .init_props import init_props
from .init_org_bones import init_org_bones
from .init_parent import init_parent
from ..libs.blender_utils import (
  extrude_bone_, 
  copy_bone_,
  delete_bones,
  get_edit_bone,
  get_edit_bones,
  select_bone
)
from ..patch import patch_strategies

def delete_tmp_bones ():
  delete_bones([get_edit_bone('mch_ik_arm.l.001'), get_edit_bone('mch_ik_leg.l.001')])

def _init_bones (config, scene = None):
  for item in config:
    name = item['name']
    source = item['source']
    operator = item['operator']
    operator_config = item['operator_config']
    scale_factor = operator_config.get('scale_factor')

    if operator == 'extrude':
      target = operator_config.get('target')
      target_head_or_tail = operator_config.get('target_head_or_tail')
      head_or_tail = operator_config['head_or_tail']
      
      extrude_bone_(name, source, head_or_tail, scale_factor, target, target_head_or_tail)
    else:
      copy_bone_(name, source, scale_factor)

    if name in patch_strategies:
      cbs = patch_strategies[name]

      if isinstance(cbs, list):
        for cb in cbs:
          cb(scene, item)
      else:
        cbs(scene, item)

def init_bones (scene):
  init_org_bones()
  hand_config = init_hand()
  arm_config = init_arm()
  torso_config = init_torso()
  props_config = init_props()
  leg_config = init_leg()
  configs = [props_config, torso_config, hand_config, arm_config, leg_config]

  for config in configs:
    _init_bones(config, scene)
    
  init_parent()
  delete_tmp_bones()
