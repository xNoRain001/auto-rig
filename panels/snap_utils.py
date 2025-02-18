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
    armature_name = context.scene.armature_name
    armature = get_object_(armature_name)

    if armature:
      collections_all = armature.data.collections_all

      layout = self.layout
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname, 
        text = 'fk_arm.l',
        depress = collections_all['arm_fk.l'].is_visible
      ).param = 'fk-arm-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_arm.r',
        depress = collections_all['arm_fk.r'].is_visible
      ).param = 'fk-arm-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_arm.l',
        depress = collections_all['arm_ik.l'].is_visible
      ).param = 'ik-arm-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_arm.r',
        depress = collections_all['arm_ik.r'].is_visible
      ).param = 'ik-arm-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_leg.l',
        depress = collections_all['leg_fk.l'].is_visible
      ).param = 'fk-leg-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'fk_leg.r',
        depress = collections_all['leg_fk.l'].is_visible
      ).param = 'fk-leg-r'
      row = layout.row()
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_leg.l',
        depress = collections_all['leg_ik.l'].is_visible
      ).param = 'ik-leg-l'
      row.operator(
        OBJECT_OT_snap_utils.bl_idname,
        text = 'ik_leg.r',
        depress = collections_all['leg_ik.r'].is_visible
      ).param = 'ik-leg-r'
