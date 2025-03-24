from ..libs.blender_utils import get_panel, get_active_object
from ..operators.bone_wiggle import OBJECT_OT_bone_wiggle
from ..const import bl_category
from ..operators import OBJECT_OT_rig_weapon
from .custom_props import show_panel

class VIEW3D_PT_extra_rig (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Extra Rig"
  bl_idname = "VIEW3D_PT_extra_rig"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    scene = context.scene
    layout = self.layout

    box = layout.box()
    row = box.row()
    row.label(text = 'Custom prop')
    row.prop(scene, 'wiggle_prop', text = '')
    row = box.row()
    row.label(text = 'Influence ')
    row.prop(scene, 'wiggle_influence', text = '')
    row = box.row()
    row.operator(OBJECT_OT_bone_wiggle.bl_idname, text = 'Bone Wiggle')

    box = layout.box()
    row = box.row()
    row.label(text = 'Armature ')
    row.prop(scene, 'armature', text = '')

    row = box.row()
    row.label(text = 'Weapon')
    armature = get_active_object()
    data = armature.data
    row.prop_search(scene, 'weapon', data, 'bones', text = '')
    row = box.row()
    row.operator(OBJECT_OT_rig_weapon.bl_idname, text = 'Rig Weapon')
