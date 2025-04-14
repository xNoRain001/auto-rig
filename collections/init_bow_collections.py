from ..const import def_collection, org_collection, bow_collection
from . import (
  move_bones_to_collection, 
  update_collections_visibility,
  move_def_and_org_bones_to_collection
)

def extend_collection_config (bone_config, scene):
  root = scene.bow_root
  bowstring = scene.bowstring
  bone_config.extend([
    {
      'name': root,
      'collection': bow_collection
    },
    {
      'name': bowstring.replace('def_', 'org_'),
      'collection': bow_collection
    }
  ])

def init_bow_collections (bone_config, scene):
  move_def_and_org_bones_to_collection(def_collection, org_collection)
  extend_collection_config(bone_config, scene)
  move_bones_to_collection(bone_config)
  update_collections_visibility(set([bow_collection]))
