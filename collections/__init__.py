from ..libs.blender_utils import (
  get_edit_bone, 
  select_bone, 
  deselect_bones, 
  get_armature, 
  get_pose_bones,
  get_bone_collections,
  get_pose_bone,
  deselect_pose_bones,
  select_pose_bone,
  is_pose_mode
)

from ..const import mch_collection

def move_def_and_org_bones_to_collection (def_collection, org_collection):
  pose_bones = get_pose_bones()

  for pose_bone in pose_bones:
    bone_name = pose_bone.name

    if bone_name.startswith('org_'):
      _move_bones_to_collection(org_collection, bone_name)
    elif bone_name.startswith('def_'):
      _move_bones_to_collection(def_collection, bone_name)

def _move_bones_to_collection (collection_name, bone_names):
  _is_pose_mode = is_pose_mode()
  deselect_pose_bones() if _is_pose_mode else deselect_bones()
  bone_collections = get_bone_collections()

  if not isinstance(bone_names, list):
    bone_names = [bone_names]

  for bone_name in bone_names:
    bone = get_pose_bone(bone_name) if _is_pose_mode else get_edit_bone(bone_name)

    if bone:
      select_pose_bone(bone) if _is_pose_mode else select_bone(bone)

  if collection_name not in bone_collections:
    get_armature().move_to_collection(new_collection_name = collection_name)
  else:
    get_armature().move_to_collection(
      collection_index = bone_collections[collection_name].index
    )

  deselect_pose_bones() if _is_pose_mode else deselect_bones()

def move_bones_to_collection (bone_config):
  for config in bone_config:
    bone_name = config['name']
    collection_name = config['collection']
    _move_bones_to_collection(collection_name, bone_name)

    mirror_bone_names = bone_name.replace('.l', '.r')

    if collection_name == mch_collection:
      _move_bones_to_collection(mch_collection, mirror_bone_names)
    elif collection_name.endswith('.l'):
      mirror_collection_name = collection_name.replace('.l', '.r')
      _move_bones_to_collection(mirror_collection_name, mirror_bone_names)

def update_collections_visibility (visible_collections):
  bone_collections = get_bone_collections()

  for collection in bone_collections:
    collection_name = collection.name
    
    if collection_name not in visible_collections:
      bone_collections[collection_name].is_visible = False
