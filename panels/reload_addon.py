from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.reload_addon import OBJECT_OT_reload_addon
from ..const import bl_category

class VIEW3D_PT_reload_addon (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Reload Addon"
  bl_idname = "VIEW3D_PT_reload_auto_rig_addon"

  def draw(self, context):
    layout = self.layout
    add_row_with_operator(layout, OBJECT_OT_reload_addon.bl_idname, 'Reload Auto Rig Addon')
