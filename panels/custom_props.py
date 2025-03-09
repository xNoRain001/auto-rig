from ..const import bl_category
from ..libs.blender_utils import get_panel, get_pose_bone

not_visible = set([
  'initialized',
  'mmd_bone',
  'leg_fk_to_ik_l',
  'leg_fk_to_ik_r',
  'arm_fk_to_ik_l',
  'arm_fk_to_ik_r'
])

class VIEW3D_PT_custom_props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Custom Props"
  bl_idname = "VIEW3D_PT_custom_props"

  def draw(self, context):
    armature = context.scene.armature

    if armature:
      bone = get_pose_bone('props', armature)

      if not bone:
        return
            
      # 给一个黑色的背景
      box = self.layout.box()
     
      for prop_name in bone.keys():
        if prop_name not in not_visible:
          row = box.row()
          row.label(text = prop_name)
          row.prop(bone, f'["{ prop_name }"]', text = '')
      