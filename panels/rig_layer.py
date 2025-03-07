from ..libs.blender_utils import (
  get_active_object, get_bone_collections, get_panel, get_collection,
  get_object_, active_object_
)
from ..const import bl_category

group = {
  'visible': [
    ['root'],
    ['torso', 'torso_fk', 'tweak_torso'],
    ['arm_fk.l', 'arm_fk.r'],
    ['arm_ik.l', 'arm_ik.r'],
    ['tweak_arm.l', 'tweak_arm.r'],
    ['hand.l', 'hand.r'],
    ['tweak_hand.l', 'tweak_hand.r'],
    ['leg_fk.l', 'leg_fk.r'],
    ['leg_ik.l', 'leg_ik.r'],
    ['tweak_leg.l', 'tweak_leg.r']
  ],
  'not_visible': [
    ['def'],
    ['org'],
    ['mch'],
    ['props']
  ]
}

class VIEW3D_PT_rig_layer (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Rig Layer"
  bl_idname = "VIEW3D_PT_rig_layer"

  def draw(self, context):
    col = self.layout.column()
    armature = context.scene.armature

    if armature:
      collections_all = armature.data.collections_all

      for collection_group in group['visible']:
        row = col.row()

        for collection_name in collection_group:
          if collection_name in collections_all:
            collection = collections_all[collection_name]

            if collection:
              row.prop(
                collections_all[collection_name], 
                'is_visible', 
                toggle = True, 
                text = collection_name
              )
