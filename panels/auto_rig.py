from ..libs.blender_utils import get_panel, add_row_with_operator, get_pose_bone
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
    
    # row = layout.row()
    # row.prop(scene, 'mesh', text = 'mesh')
    box = layout.box()
    row = box.row()
    row.prop(scene, 'armature', text = 'Armature')

    if not scene.armature:
      return
    
    # data = scene.armature.data
    # row = layout.row()
    # row.prop_search(
    #   scene, 
    #   'def_hips', 
    #   data, 
    #   'bones', 
    #   text = 'def hips'
    # )
    
    # row = layout.row()
    # row.label(text = 'Tweak bone number:')
    box = layout.box()
    row = box.row()
    row.label(text = 'Arm')
    row.prop(scene, 'arm_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Forearm')
    row.prop(scene, 'forearm_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Leg')
    row.prop(scene, 'leg_tweak_bone_number', text = '')
    row = box.row()
    row.label(text = 'Shin')
    row.prop(scene, 'shin_tweak_bone_number', text = '')

    box = layout.box()
    row = box.row()
    row.prop(scene, 'arm_pole_normal', text = 'Arm pole normal')
    row = box.row()
    row.prop(scene, 'leg_pole_normal', text = 'Leg pole normal')

    box = layout.box()
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Foot Roll 1').type = 'side_01'
    row.prop(scene, 'side_01_head_location', text = '')
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Foot Roll 2').type = 'side_02'
    row.prop(scene, 'side_02_head_location', text = '')
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'Heel').type = 'heel'
    row.prop(scene, 'heel_location', text = '')
    row = box.row()
    row.operator(OBJECT_OT_init_location.bl_idname, text = 'tiptoe').type = 'foot_tip'
    row.prop(scene, 'foot_tip_location', text = '')
    row = layout.row()
    row.operator(OBJECT_OT_init_rig.bl_idname, text = 'Rig')
  