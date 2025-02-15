from ..const import custom_props_config
from ..libs.blender_utils import (
  get_panel, add_row_with_operator, get_pose_bone, get_active_object,
  get_object_
)

class VIEW3D_PT_custom_props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Custom Props"
  bl_idname = "VIEW3D_PT_custom_props"

  def draw(self, context):
    armature_name = context.scene.armature_name
    armature = get_object_(armature_name)
    bone = armature.pose.bones.get('props')

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
      # row_label = split.row(align = True)
      # row_label.label(text = custom_prop)
      row_prop = split.row(align = True)
      row_prop.prop(bone, f'["{ custom_prop }"]', text = custom_prop)
