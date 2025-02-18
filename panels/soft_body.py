from ..libs.blender_utils import get_panel, add_row_with_operator, add_row, add_scene_custom_prop
from ..operators.soft_body import OBJECT_OT_soft_body
from ..const import bl_category

class VIEW3D_PT_soft_body (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Soft Body"
  bl_idname = "VIEW3D_PT_soft_body"

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    add_row(layout, scene, 'friction', '摩擦')
    add_row(layout, scene, 'mass', '质量')
    add_row(layout, scene, 'goal_min', '强度最小值')
    add_row_with_operator(layout, OBJECT_OT_soft_body.bl_idname, '添加软体物理')
