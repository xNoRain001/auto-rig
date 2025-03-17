from ..libs.blender_utils import get_panel
from ..const import bl_category
from ..operators import (
  OBJECT_OT_init_bone_collection, 
  OBJECT_OT_init_def_bones,
  OBJECT_OT_refresh_weapon
)
from .custom_props import show_panel

class VIEW3D_PT_helper (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Helper"
  bl_idname = "VIEW3D_PT_helper"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    box = layout.box()
    row = box.row()
    row.label(text = 'Torso bones color')
    row.prop(scene, 'torso_color', text = '')
    row = box.row()
    row.label(text = 'Left bones color')
    row.prop(scene, 'fk_ik_l_color', text = '')
    row = box.row()
    row.label(text = 'Right bone color')
    row.prop(scene, 'fk_ik_r_color', text = '')
    row = box.row()
    row.label(text = 'Tweak bones Color')
    row.prop(scene, 'tweak_color', text = '')

    box = layout.box()
    row = box.row()
    row.label(text = 'Rotation mode')
    row.prop(scene, 'rotation_mode', text = '')
    row = box.row()
    row.label(text = 'Line width')
    row.prop(scene, 'line_width', text = '')
    row = box.row()
    row.operator(OBJECT_OT_init_bone_collection.bl_idname, text = 'Assign Collection')
    row = box.row()
    row.operator(OBJECT_OT_init_def_bones.bl_idname, text = 'Init Def Bones')
    row = box.row()
    row.operator(OBJECT_OT_refresh_weapon.bl_idname, text = 'Refresh Weapon')
