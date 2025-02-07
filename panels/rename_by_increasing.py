from ..libs.blender_utils import get_panel, add_row_with_operator

class Rename_By_Increasing (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Rename By Increasing"
  bl_idname = "_PT_Rename_By_Increasing_PT_"

  def draw(self, context):
    layout = self.layout
    add_row_with_operator(layout, 'object.rename_by_increasing', 'Rename by increasing')
