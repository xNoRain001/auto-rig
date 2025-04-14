from ..const import (
  def_collection,
  org_collection,
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
from . import (
  move_bones_to_collection, 
  update_collections_visibility,
  move_def_and_org_bones_to_collection
)

def extend_collection_config (bone_config):
  bone_config.extend([
    {
      'name': 'root',
      'collection': root_collection
    },
    {
      'name': 'org_shoulder.l',
      'collection': torso_collection
    },
    {
      'name': 'org_shoulder.r',
      'collection': torso_collection
    },
    {
      'name': 'mch_finger_d_01.l',
      'collection': hand_l_collection
    },
    {
      'name': 'mch_finger_d_01.r',
      'collection': hand_r_collection
    }
  ])

def init_human_collections (bone_config):
  move_def_and_org_bones_to_collection(def_collection, org_collection)
  extend_collection_config(bone_config)
  move_bones_to_collection(bone_config)
  update_collections_visibility(set([
    root_collection,
    torso_collection,
    ik_arm_l_collection,
    ik_arm_r_collection,
    hand_l_collection,
    hand_r_collection,
    ik_leg_l_collection,
    ik_leg_r_collection
  ]))
