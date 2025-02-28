from ..libs.blender_utils import get_panel, add_row_with_operator, get_selected_bone, get_selected_pose_bone
from ..operators.wiggle import OBJECT_OT_wiggle
from ..const import bl_category

class VIEW3D_PT_wiggle (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Wiggle"
  bl_idname = "VIEW3D_PT_wiggle"

  def draw(self, context):
    scene = context.scene
    layout = self.layout
    row = layout.row()
    row.prop(scene, 'wiggle_prop', text = '')
    row.prop(scene, 'wiggle_influence', text = '')

    # get_selected_bone()
    # get_selected_pose_bone()

    if scene.wiggle_prop:
      row = layout.row()
      row.operator(OBJECT_OT_wiggle.bl_idname, text = 'Wiggle')
