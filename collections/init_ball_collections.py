from ..const import (
  org_collection,
  ball_collection,
  ball_def_collection,
)
from . import (
  move_bones_to_collection, 
  update_collections_visibility,
  move_def_and_org_bones_to_collection
)

def extend_collection_config (bone_config, scene):
  root = scene.ball_root
  deformation = scene.deformation
  bone_config.extend([
    {
      'name': root,
      'collection': ball_collection
    },
    {
      'name': deformation,
      'collection': ball_def_collection
    }
  ])

def init_ball_collections (bone_config, scene):
  move_def_and_org_bones_to_collection(ball_def_collection, org_collection)
  extend_collection_config(bone_config, scene)
  move_bones_to_collection(bone_config)
  update_collections_visibility(set([ball_collection]))
