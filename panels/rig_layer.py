from ..const import group
from ..libs.blender_utils import get_active_object, get_bone_collections, get_panel, get_collection

class Rig_Layer (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Rig Layer"
  # 首字母大写且必须包含 _PT_
  bl_idname = "_PT_Rig_Layer_PT_"

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
