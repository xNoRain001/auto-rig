from ..libs.blender_utils import get_panel, is_pose_mode
from ..operators.clear_bone_widget import OBJECT_OT_clear_bone_widget
from ..operators.clear_unused_widget import OBJECT_OT_clear_unused_bone_widget
from ..operators.reset_transform import OBJECT_OT_reset_transform
from ..const import bl_category

class VIEW3D_PT_bone_widget (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Bone Widget"
  bl_idname = "VIEW3D_PT_bone_widget"

  @classmethod
  def poll(cls, context):
    return is_pose_mode()

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    # row = layout.row()
    # row.prop(scene, 'scale', text = '缩放(%)')
    # row = layout.row()
    # row.prop(scene, 'translation', text = '移动(%)')
    # row = layout.row()
    # row.prop(scene, 'rotation', text = '旋转')
    # row = layout.row()
    box = layout.box()
    row = box.row()
    # row.prop(scene, 'show_wire', text = '线框')
    # row = box.row()
    row.label(text = 'Wire width')
    row.prop(scene, 'wire_width', text = '')
    row = box.row()
    row.label(text = 'Shape ')
    row.prop(scene, 'shape', text = '')
    row = box.row()
    row.operator(OBJECT_OT_clear_bone_widget.bl_idname, text = '清除选中骨骼的自定义形状')
    row = box.row()
    row.operator(OBJECT_OT_clear_unused_bone_widget.bl_idname, text = '清空未使用的 WGT')
 