from ..libs.blender_utils import get_bone_collections, get_panel, get_active_object

from .custom_props import show_panel
from ..const import (
  bl_category,
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
  hand_l_collection,
  hand_r_collection
)

rig_layer_rows = [
  [root_collection],
  [torso_collection, fk_torso_collection, tweak_torso_collection],
  [fk_arm_l_collection, fk_arm_r_collection],
  [ik_arm_l_collection, ik_arm_r_collection],
  [tweak_arm_l_collection, tweak_arm_r_collection],
  [hand_l_collection, hand_r_collection],
  [tweak_hand_l_collection, tweak_hand_r_collection],
  [fk_leg_l_collection, fk_leg_r_collection],
  [ik_leg_l_collection, ik_leg_r_collection],
  [tweak_leg_l_collection, tweak_leg_r_collection]
]

class VIEW3D_PT_rig_layers (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Rig Layers"
  bl_idname = "VIEW3D_PT_rig_layers"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    armature = get_active_object()
    layout = self.layout
    box = layout.box()

    bone_collections = get_bone_collections(armature)

    for collections in rig_layer_rows:
      row = box.row()

      for collection in collections:
        if collection in bone_collections:
          row.prop(
            bone_collections[collection], 
            'is_visible', 
            toggle = True, 
            text = collection
          )
