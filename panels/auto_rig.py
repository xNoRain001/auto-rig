from ..libs.blender_utils import get_panel, add_row_with_operator

class Auto_Rig (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Auto Rig"
  bl_idname = "_PT_Auto_Rig_PT_"

  def draw(self, context):
    layout = self.layout
    add_row_with_operator(layout, 'object.init_rig', '绑定（请检查骨骼命名和轴向）')
    add_row_with_operator(layout, 'object.init_bone_collection', '分配集合')
    add_row_with_operator(layout, 'object.init_bone_widget', '自定义骨骼')
