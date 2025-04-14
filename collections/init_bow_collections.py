from ..const import (
  def_collection,
  org_collection,
  bow_mch_collection,
  bow_root_collection
)
from . import (
  move_bones_to_collection, 
  update_collections_visibility,
  move_def_and_org_bones_to_collection
)

def init_bow_collections (bone_config):
  move_def_and_org_bones_to_collection(def_collection, org_collection)
  move_bones_to_collection(bone_config)
  update_collections_visibility(set())
