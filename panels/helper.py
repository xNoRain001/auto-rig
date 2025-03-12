from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.reload_addon import OBJECT_OT_reload_addon
from ..const import bl_category
from ..operators import (
  OBJECT_OT_init_bone_collection, 
  OBJECT_OT_rig_weapon, 
  OBJECT_OT_init_def_bones,
  OBJECT_OT_refresh_weapon
)

class VIEW3D_PT_helper (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Helper"
  bl_idname = "VIEW3D_PT_helper"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    row = layout.row()
    row.prop(scene, 'torso_color', text = 'Torso Bones Color')
    row = layout.row()
    row.prop(scene, 'fk_ik_l_color', text = 'Left Bones Color')
    row = layout.row()
    row.prop(scene, 'fk_ik_r_color', text = 'Right Bone Color')
    row = layout.row()
    row.prop(scene, 'tweak_color', text = 'Tweak Bones Color')
    row = layout.row()
    row.prop(scene, 'rotation_mode', text = 'Rotation mode')
    row = layout.row()
    row.prop(scene, 'line_width', text = 'Line width')
    row = layout.row()
    row.operator(OBJECT_OT_init_bone_collection.bl_idname, text = 'Assign Collection')
    row = layout.row()
    row.operator(OBJECT_OT_rig_weapon.bl_idname, text = 'Rig Weapon')
    row = layout.row()
    row.operator(OBJECT_OT_init_def_bones.bl_idname, text = 'Init Def Bones')
    row = layout.row()
    row.operator(OBJECT_OT_refresh_weapon.bl_idname, text = 'Refresh Weapon')
