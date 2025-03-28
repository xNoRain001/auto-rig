from ..libs.blender_utils import select_bone, get_edit_bone, get_ops, deselect_bones

def move (scene, config):
  deselect_bones()
  bone_name = config['name']
  bone = get_edit_bone(bone_name)
  select_bone(bone)
  get_ops().transform.translate(value = (0, 0.1, 0))
  deselect_bones()
