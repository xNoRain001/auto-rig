from ..libs.blender_utils import (
  copy_bone_,
  extrude_bone_
)

from ..bone_patch import bone_patchs

def init_bones (config, scene = None):
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
