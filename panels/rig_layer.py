from ..const import group
from ..libs.blender_utils import get_active_object, get_bone_collections, get_panel, get_collection

class VIEW3D_PT_rig_layer (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Rig Layer"
  bl_idname = "VIEW3D_PT_rig_layer"

  def draw(self, context):
    col = self.layout.column()
    armature = get_active_object()

    if armature.type == 'ARMATURE':
      collections = get_bone_collections(armature)

      for collection_group in group['use_in_rig_ui']:
        row = col.row()

        for collcetion_name in collection_group:
          collection = get_collection(collcetion_name)

          if collection:
            row.prop(
              collections[collcetion_name], 
              'is_visible', 
              toggle = True, 
              text = collcetion_name
            )
