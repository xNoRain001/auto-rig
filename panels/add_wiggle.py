from ..libs.blender_utils import get_panel, add_row_with_operator, get_selected_bone, get_selected_pose_bone
from ..operators.add_wiggle import OBJECT_OT_add_wiggle
from ..const import bl_category

class VIEW3D_PT_add_wiggle (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Add Wiggle"
  bl_idname = "VIEW3D_PT_wiggle"

  def draw(self, context):
    scene = context.scene
    layout = self.layout
    row = layout.row()
    row.prop(scene, 'wiggle_prop', text = '自定义属性')
    row.prop(scene, 'wiggle_influence', text = '强度')
    row = layout.row()
    row.operator(OBJECT_OT_add_wiggle.bl_idname, text = 'Add Wiggle')
