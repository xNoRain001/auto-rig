from ..libs.blender_utils import get_panel, add_row_with_operator, add_row, add_scene_custom_prop

class Soft_Body (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "Item"
  bl_label = "Soft Body"
  bl_idname = "_PT_Soft_Body_PT_"

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    add_row(layout, scene, 'friction', '摩擦')
    add_row(layout, scene, 'mass', '质量')
    add_row(layout, scene, 'goal_min', '强度最小值')
    add_row_with_operator(layout, 'object.soft_body', '添加软体物理')

add_scene_custom_prop('friction', 'Float', 10, '')
add_scene_custom_prop('mass', 'Float', 0.1, '')
add_scene_custom_prop('goal_min', 'Float', 0.4, '')
add_scene_custom_prop('friction', 'Float', 10, '')
