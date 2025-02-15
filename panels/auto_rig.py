from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.init_rig import OBJECT_OT_init_rig
from ..operators.init_bone_collections import OBJECT_OT_init_bone_collection
from ..operators.init_bone_widgets import OBJECT_OT_init_bone_widgets

class VIEW3D_PT_auto_rig (get_panel()):
  bl_label = "Auto Rig"
  bl_idname = "VIEW3D_PT_auto_rig"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    row = layout.row()
    row.prop(scene, 'armature_name', text = '骨架名称')
    row = layout.row()
    row.prop(scene, 'rotation_mode', text = '旋转模式')
    row = layout.row()
    row.prop(scene, 'arm_pole_normal', text = '手臂极向方向')
    row = layout.row()
    row.prop(scene, 'leg_pole_normal', text = '腿极向方向')
    add_row_with_operator(layout, OBJECT_OT_init_rig.bl_idname, '绑定（请检查骨骼命名和轴向）')
    add_row_with_operator(layout, OBJECT_OT_init_bone_collection.bl_idname, '分配集合')
    add_row_with_operator(layout, OBJECT_OT_init_bone_widgets.bl_idname, '自定义骨骼')
