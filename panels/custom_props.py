from ..const import bl_category, weapon_custom_prop_prefix, identifier
from ..libs.blender_utils import (
  get_panel, 
  is_pose_mode,
  get_pose_bone, 
  get_active_object
)

i = len(weapon_custom_prop_prefix)
not_visible = set([
  'mmd_bone',
  'leg_fk_to_ik_l',
  'leg_fk_to_ik_r',
  'arm_fk_to_ik_l',
  'arm_fk_to_ik_r',
  'weapons'
])

def show_panel_in_edit_and_pose_mode ():
  armature = get_active_object()

  return (
    armature and
    armature.type == 'ARMATURE' and
    identifier in armature
  )

def show_panel_in_pose_mode ():
  # 在 pose 模式下时，激活的对象一定是 ARMATURE，只需要检查 identifier
  return is_pose_mode() and identifier in get_active_object()

class VIEW3D_PT_custom_props (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Custom Properties "
  bl_idname = "VIEW3D_PT_custom_props"

  @classmethod
  def poll(cls, context):
    return show_panel_in_pose_mode()

  def draw(self, context):
    scene = context.scene
    bone = get_pose_bone('props')
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

    # row = box.row()
    # row.label(text = 'arm ik stretch')
    # row.prop(get_pose_bone('mch_ik_arm.l'), 'ik_stretch', text = '')
