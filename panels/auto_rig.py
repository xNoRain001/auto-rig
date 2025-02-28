from ..libs.blender_utils import get_panel, add_row_with_operator
from ..operators.init_rig import OBJECT_OT_init_rig
from ..operators.init_bone_collections import OBJECT_OT_init_bone_collection
from ..operators.init_bone_widgets import OBJECT_OT_init_bone_widgets
from ..operators.init_location import OBJECT_OT_init_location
from ..operators.rig_weapon import OBJECT_OT_rig_weapon
from ..const import bl_category

class VIEW3D_PT_auto_rig (get_panel()):
  bl_label = "Auto Rig"
  bl_idname = "VIEW3D_PT_auto_rig"
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    row = layout.row()
    row.prop(scene, 'torso_color', text = 'Torso Color')
    row = layout.row()
    row.prop(scene, 'fk_ik_l_color', text = 'L Ctrl Color')
    row = layout.row()
    row.prop(scene, 'fk_ik_r_color', text = 'R Ctrl Color')
    row = layout.row()
    row.prop(scene, 'tweak_color', text = 'Tweak Color')
    row = layout.row()
    row.prop(scene, 'mesh_name', text = 'mesh name')
    row = layout.row()
    row.prop(scene, 'armature_name', text = 'armature name')
    row = layout.row()
    row.prop(scene, 'rotation_mode', text = 'rotation mode')
    row = layout.row()
    row.prop(scene, 'arm_pole_normal', text = 'arm pole normal')
    row = layout.row()
    row.prop(scene, 'leg_pole_normal', text = 'leg pole normal')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Roll 1').type = 'side_01'
    row.prop(scene, 'side_01_head_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Roll 2').type = 'side_02'
    row.prop(scene, 'side_02_head_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Heel').type = 'heel'
    row.prop(scene, 'heel_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Foot tip').type = 'foot_tip'
    row.prop(scene, 'foot_tip_location', text = '')
    add_row_with_operator(layout, OBJECT_OT_init_rig.bl_idname, 'Rig Body')
    add_row_with_operator(layout, OBJECT_OT_init_bone_widgets.bl_idname, 'Custom Bone')
    add_row_with_operator(layout, OBJECT_OT_init_bone_collection.bl_idname, 'Assign Collection')
    add_row_with_operator(layout, OBJECT_OT_rig_weapon.bl_idname, 'Rig Weapon')
