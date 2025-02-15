from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.rename_by_increasing import OBJECT_OT_rename_by_increasing

class VIEW3D_PT_rename_by_increasing (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Rename By Increasing"
  bl_idname = "VIEW3D_PT_rename_by_increasing"

  def draw(self, context):
    layout = self.layout
    add_row_with_operator(layout, OBJECT_OT_rename_by_increasing.bl_idname, 'Rename by increasing')
