from ..const import bl_category
from ..libs.blender_utils import (
  get_panel, add_row_with_operator, get_pose_bone, get_active_object,
  get_object_
)

not_visible = [
  'mmd_bone',
  'leg_fk_to_ik_l',
  'leg_fk_to_ik_r',
  'arm_fk_to_ik_l',
  'arm_fk_to_ik_r'
]

class VIEW3D_PT_custom_props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Custom Props"
  bl_idname = "VIEW3D_PT_custom_props"

  def draw(self, context):
    armature_name = context.scene.armature_name
    armature = get_object_(armature_name)

    if armature:
      bone = armature.pose.bones.get('props')

      if not bone:
        return
            
      # 给一个黑色的背景
      box = self.layout.box()
      col = box.column()
      for prop_name in bone.keys():
        if prop_name not in not_visible:
          row = col.row()
          row.label(text = prop_name)
          row.prop(bone, f'["{ prop_name }"]', text = '')

        
      