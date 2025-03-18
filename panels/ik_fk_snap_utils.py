from ..libs.blender_utils import get_panel, get_pose_bone
from ..operators.ik_fk_snap_utils import OBJECT_OT_ik_fk_snap_utils
from ..const import bl_category
from .custom_props import show_panel

class VIEW3D_PT_ik_fk_snap_utils (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "IK FK Snap Utils"
  bl_idname = "VIEW3D_PT_ik_fk_snap_utils"

  @classmethod
  def poll(cls, context):
    return show_panel(context)

  def draw(self, context):
    bone = get_pose_bone('props')
    
    arm_fK_to_ik_l = bone['arm_fk_to_ik_l']
    arm_fK_to_ik_r = bone['arm_fk_to_ik_r']
    leg_fK_to_ik_l = bone['leg_fk_to_ik_l']
    leg_fK_to_ik_r = bone['leg_fk_to_ik_r']
    
    layout = self.layout

    box = layout.box()
    row = box.row()
    bl_idname = OBJECT_OT_ik_fk_snap_utils.bl_idname
    row.operator(
      bl_idname, 
      text = 'FK Arm L',
      depress = not arm_fK_to_ik_l
    ).param = 'fk-arm-l'
    row.operator(
      bl_idname,
      text = 'FK Arm R',
      depress = not arm_fK_to_ik_r
    ).param = 'fk-arm-r'
    row = box.row()
    row.operator(
      bl_idname,
      text = 'IK Arm L',
      depress = arm_fK_to_ik_l
    ).param = 'ik-arm-l'
    row.operator(
      bl_idname,
      text = 'IK Arm R',
      depress = arm_fK_to_ik_r
    ).param = 'ik-arm-r'

    box = layout.box()
    row = box.row()
    row.operator(
      bl_idname,
      text = 'FK Leg L',
      depress = not leg_fK_to_ik_l
    ).param = 'fk-leg-l'
    row.operator(
      bl_idname,
      text = 'FK Leg R',
      depress = not leg_fK_to_ik_r
    ).param = 'fk-leg-r'
    row = box.row()
    row.operator(
      bl_idname,
      text = 'IK Leg L',
      depress = leg_fK_to_ik_l
    ).param = 'ik-leg-l'
    row.operator(
      bl_idname,
      text = 'IK Leg R',
      depress = leg_fK_to_ik_r
    ).param = 'ik-leg-r'
