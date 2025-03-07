from ..libs.blender_utils import get_panel, get_object_
from ..operators.snap_utils import OBJECT_OT_snap_utils
from ..const import bl_category

class VIEW3D_PT_snap_utils (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Snap Utils"
  bl_idname = "VIEW3D_PT_snap_utils"

  def draw(self, context):
    armature = context.scene.armature

    if armature:
      bone = armature.pose.bones.get('props')

      if not bone or not bone.get('initialized'):
        return
      
      arm_fK_to_ik_l = bone['arm_fk_to_ik_l']
      arm_fK_to_ik_r = bone['arm_fk_to_ik_r']
      leg_fK_to_ik_l = bone['leg_fk_to_ik_l']
      leg_fK_to_ik_r = bone['leg_fk_to_ik_r']
      
      layout = self.layout
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname, 
        text = 'fk_arm.l',
        depress = not arm_fK_to_ik_l
      ).param = 'fk-arm-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_arm.r',
        depress = not arm_fK_to_ik_r
      ).param = 'fk-arm-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_arm.l',
        depress = arm_fK_to_ik_l
      ).param = 'ik-arm-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_arm.r',
        depress = arm_fK_to_ik_r
      ).param = 'ik-arm-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_leg.l',
        depress = not leg_fK_to_ik_l
      ).param = 'fk-leg-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_leg.r',
        depress = not leg_fK_to_ik_r
      ).param = 'fk-leg-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_leg.l',
        depress = leg_fK_to_ik_l
      ).param = 'ik-leg-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_leg.r',
        depress = leg_fK_to_ik_r
      ).param = 'ik-leg-r'
