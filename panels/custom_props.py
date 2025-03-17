from ..const import bl_category, weapon_custom_prop_prefix
from ..libs.blender_utils import get_panel, get_pose_bone

i = len(weapon_custom_prop_prefix)
not_visible = set([
  'mmd_bone',
  'leg_fk_to_ik_l',
  'leg_fk_to_ik_r',
  'arm_fk_to_ik_l',
  'arm_fk_to_ik_r',
  'weapons'
])

def show_panel (context):
  armature = context.scene.armature

  if armature:
    bone = get_pose_bone('props', armature)

    if bone:
      return True
    
  return False

class VIEW3D_PT_custom_props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Custom Properties "
  bl_idname = "VIEW3D_PT_custom_props"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    scene = context.scene
    armature = scene.armature
    bone = get_pose_bone('props', armature)
    # 黑色的背景
    box = self.layout.box()

    for prop_name in bone.keys():
      if prop_name in not_visible:
        continue
      
      if prop_name.startswith(weapon_custom_prop_prefix):
        if hasattr(scene, prop_name):
          row = box.row()
          row.label(text = prop_name[i:])
          row.prop(scene, prop_name, text = '')
      else:
        row = box.row()
        row.label(text = prop_name)
        row.prop(bone, f'["{ prop_name }"]', text = '')
