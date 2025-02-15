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
    
    # 给一个黑色的背景
    box = self.layout.box()
    col = box.column()
    custom_props = custom_props_config.keys()
    
    for custom_prop in custom_props:
      row = col.row()
      row.label(text = custom_prop)
      row.prop(bone, f'["{ custom_prop }"]', text = '')
