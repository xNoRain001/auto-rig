from ..const import custom_props_config
from ..libs.blender_utils import get_panel, add_row_with_operator, get_pose_bone

class Custom_Props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Custom Props"
  bl_idname = "_PT_Custom_Props_PT_"
  # bl_parent_id = bl_idname 指定父面板，属性分类时可以用到

  def draw(self, context):
    bone = get_pose_bone('props')

    if not bone:
      return
    
    # 0.7 表示 label 内容占 70%
    factor = 0.7
    # box 会给一个黑色的背景
    box = self.layout.box()
    col = box.column(align = True)

    custom_props = custom_props_config.keys()
    
    for custom_prop in custom_props:
      split = col.row().split(align = True, factor = factor)
      row_label = split.row(align = True)
      row_label.label(text = custom_prop)
      row_prop = split.row(align = True)
      row_prop.prop(bone, f'["{ custom_prop }"]', text = '')
