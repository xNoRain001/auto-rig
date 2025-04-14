from ..libs.blender_utils import get_bone_collections, get_pose_bones

def init_bones_color (color_map):
  pose_bones = get_pose_bones()
  bone_collections = get_bone_collections()

  for color, collection_names in color_map.items():
    for collection_name in collection_names:
      for bone in bone_collections[collection_name].bones:
        pose_bones[bone.name].color.palette = color
