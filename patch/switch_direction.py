from ..libs.blender_utils import select_bone, get_armature, get_edit_bone, deselect_bones

def switch_direction (scene, config):
  deselect_bones()
  bone_name = config['name']
  bone = get_edit_bone(bone_name)
  select_bone(bone)
  get_armature().switch_direction()
  deselect_bones()