from ..libs.blender_utils import get_edit_bone

def set_parent (bone, target, use_connect = False):
  bone.use_connect = use_connect
  bone.parent = target

def init_bones_parent (config):
  # TODO:
  # for tweak_bone_name in arm_tweak_bone_names:
  #   # org_arm_01.l
  #   org_bone = get_edit_bone(tweak_bone_name)

  for item in config:
    bone_name, parent_bone_name, use_connect = item
    bone = get_edit_bone(bone_name)
    parent_bone = get_edit_bone(parent_bone_name) if parent_bone_name else parent_bone_name
    
    if not bone:
      print(f'{ bone_name } 不存在')
      continue

    set_parent(bone, parent_bone, use_connect)