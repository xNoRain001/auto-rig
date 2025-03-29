from ..libs.blender_utils import get_panel

from ..const import bl_category
from ..operators.add_soft_body import OBJECT_OT_add_soft_body
from .custom_props import show_panel_in_edit_and_pose_mode

class VIEW3D_PT_soft_body (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Soft Body"
  bl_idname = "VIEW3D_PT_soft_body"

  # @classmethod
  # def poll(cls, context):
  #   return show_panel_in_edit_and_pose_mode()

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    box = layout.box()
    row = box.row()
    row.label(text = '摩擦')
    row.prop(scene, 'friction', text = '')
    row = box.row()
    row.label(text = '质量')
    row.prop(scene, 'mass', text = '')
    row = box.row()
    row.label(text = '强度最小值')
    row.prop(scene, 'goal_min', text = '')
    row = box.row()
    row.operator(OBJECT_OT_add_soft_body.bl_idname, text = '添加软体物理')
