from ..libs.blender_utils import get_panel
from ..operators.snap_utils import OBJECT_OT_snap_utils

class VIEW3D_PT_snap_utils (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Snap Utils"
  bl_idname = "VIEW3D_PT_snap_utils"

  def draw(self, context):
    layout = self.layout
    row = layout.row()
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'fk_arm.l').param = 'fk-arm-l'
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'fk_arm.r').param = 'fk-arm-r'
    row = layout.row()
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'ik_arm.l').param = 'ik-arm-l'
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'ik_arm.r').param = 'ik-arm-r'
    row = layout.row()
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'fk_leg.l').param = 'fk-leg-l'
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'fk_leg.r').param = 'fk-leg-r'
    row = layout.row()
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'ik_leg.l').param = 'ik-leg-l'
    row.operator(OBJECT_OT_snap_utils.bl_idname, text = 'ik_leg.r').param = 'ik-leg-r'
