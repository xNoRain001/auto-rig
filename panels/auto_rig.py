from ..libs.blender_utils import get_panel, add_row_with_operator, get_pose_bone
from ..operators.auto_rig import OBJECT_OT_auto_rig
from ..operators.init_location import OBJECT_OT_init_location
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

    box = layout.box()
    row = box.row()
    row.label(text = 'Armature ')
    row.prop(scene, 'armature', text = '')

    if not scene.armature:
      return
 
    box = layout.box()
    row = box.row()
    row.label(text = 'Arm ')
    row.prop(scene, 'arm_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Forearm')
    row.prop(scene, 'forearm_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Leg ')
    row.prop(scene, 'leg_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Shin')
    row.prop(scene, 'shin_tweak_bone_number', text = '')

    box = layout.box()
    row = box.row()
    row.label(text = 'Arm pole normal')
    row.prop(scene, 'arm_pole_normal', text = '')
    row = box.row()
    row.label(text = 'Leg pole normal')
    row.prop(scene, 'leg_pole_normal', text = '')

    box = layout.box()
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Foot roll side 1').type = 'side_01'
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Foot roll side 2').type = 'side_02'
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Heel').type = 'heel'
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Tiptoe').type = 'foot_tip'
    
    row = layout.row()
    row.operator(OBJECT_OT_auto_rig.bl_idname, text = 'Rig')
  