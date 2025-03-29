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

from ..const import (
  org_collection,
  def_collection,
  mch_collection,
  root_collection,
  ik_arm_l_collection,
  ik_arm_r_collection,
  torso_collection,
  ik_leg_l_collection,
  ik_leg_r_collection,
  torso_collection,
  hand_l_collection,
  hand_r_collection
)

def move_def_and_org_bone ():
  pose_bones = get_pose_bones()

  for pose_bone in pose_bones:
    bone_name = pose_bone.name

    if bone_name.startswith('org_'):
      move_bones_to_collection(org_collection, bone_name)
    elif bone_name.startswith('def_'):
      move_bones_to_collection(def_collection, bone_name)

def move_bones_to_collection (collection_name, bone_names):
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

def move_bone_to_collection (bone_config):
  for config in bone_config:
    bone_name = config['name']
    collection_name = config['collection']
    move_bones_to_collection(collection_name, bone_name)

    mirror_bone_names = bone_name.replace('.l', '.r')

    if collection_name == mch_collection:
      move_bones_to_collection(mch_collection, mirror_bone_names)
    elif collection_name.endswith('.l'):
      mirror_collection_name = collection_name.replace('.l', '.r')
      move_bones_to_collection(mirror_collection_name, mirror_bone_names)

  move_bones_to_collection(root_collection, 'root')
  move_bones_to_collection(torso_collection, ['org_shoulder.l', 'org_shoulder.r'])
  move_bones_to_collection(hand_l_collection, 'mch_finger_d_01.l')
  move_bones_to_collection(hand_r_collection, 'mch_finger_d_01.r')

def update_collection_visibility ():
  bone_collections = get_bone_collections()
  visible = [
    root_collection,
    torso_collection,
    ik_arm_l_collection,
    ik_arm_r_collection,
    hand_l_collection,
    hand_r_collection,
    ik_leg_l_collection,
    ik_leg_r_collection
  ]

  for collection in bone_collections:
    collection_name = collection.name
    
    if collection_name not in visible:
      bone_collections[collection_name].is_visible = False

def init_bone_collections (bone_config):
  move_def_and_org_bone()
  move_bone_to_collection(bone_config)
  update_collection_visibility()
