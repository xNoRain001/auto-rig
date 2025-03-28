from collections import defaultdict
from ..libs.blender_utils import (
  get_edit_bone, 
  select_bone, 
  deselect_bones, 
  get_armature, 
  get_operator,
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
  fk_arm_l_collection,
  ik_arm_l_collection,
  tweak_arm_l_collection,
  fk_arm_r_collection,
  ik_arm_r_collection,
  tweak_arm_r_collection,
  torso_collection,
  tweak_hand_l_collection,
  tweak_hand_r_collection,
  fk_leg_l_collection,
  ik_leg_l_collection,
  tweak_leg_l_collection,
  fk_leg_r_collection,
  ik_leg_r_collection,
  tweak_leg_r_collection,
  torso_collection,
  fk_torso_collection,
  tweak_torso_collection,
  props_collection,
  hand_l_collection,
  hand_r_collection
)

def move_def_and_org_bone (pose_bones):
  for pose_bone in pose_bones:
    bone_name = pose_bone.name

    if bone_name.startswith('org_'):
      move_bones_to_collection(org_collection, bone_name)
    elif bone_name.startswith('def_'):
      move_bones_to_collection(def_collection, bone_name)

def gen_color_map (scene):
  torso_color = scene.torso_color
  fk_ik_l_color = scene.fk_ik_l_color
  fk_ik_r_color = scene.fk_ik_r_color
  tweak_color = scene.tweak_color
  color_map = defaultdict(list)
  color_map[tweak_color].extend([
    tweak_leg_r_collection,
    tweak_leg_l_collection,
    tweak_hand_l_collection,
    tweak_hand_r_collection,
    tweak_arm_l_collection,
    tweak_arm_r_collection,
    tweak_torso_collection
  ])
  color_map[fk_ik_l_color].extend([
    fk_arm_l_collection,
    fk_leg_l_collection,
    ik_arm_l_collection,
    ik_leg_l_collection,
    hand_l_collection
  ])
  color_map[fk_ik_r_color].extend([
    fk_arm_r_collection,
    fk_leg_r_collection,
    ik_arm_r_collection,
    ik_leg_r_collection,
    hand_r_collection
  ])
  color_map[torso_color].extend([
    torso_collection,
    fk_torso_collection,
    root_collection,
    props_collection
  ])

  return color_map

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
  move_bones_to_collection(root_collection, 'root')
  move_bones_to_collection(torso_collection, ['shoulder.l', 'shoulder.r'])

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

def update_collection_visibility (bone_collections):
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

def init_bone_colors (scene, bone_collections, pose_bones):
  color_map = gen_color_map(scene)

  for color, collection_names in color_map.items():
    for collection_name in collection_names:
      for bone in bone_collections[collection_name].bones:
        pose_bones[bone.name].color.palette = color

def init_bone_collections (scene, bone_config):
  bone_collections = get_bone_collections(scene.armature)
  pose_bones = get_pose_bones()
  move_def_and_org_bone(pose_bones)
  move_bone_to_collection(bone_config)
  init_bone_colors(scene, bone_collections, pose_bones)
  update_collection_visibility(bone_collections)

class OBJECT_OT_init_bone_collections (get_operator()):
  bl_idname = 'object.init_bone_collections'
  bl_label = 'Init Bone Collections'

  def execute(self, context):
    init_bone_collections(context.scene)

    return {'FINISHED'}
