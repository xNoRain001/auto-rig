from ..libs.blender_utils import get_panel

class Snap_Utils (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = 'Item'
  bl_label = "Snap Utils"
  bl_idname = "_PT_Snap_Utils_PT_"

  def draw(self, context):
    layout = self.layout

    col = layout.column(align=True)
    row = col.row()
    row.operator('object.snap_utils', text = 'fk_arm.l').param = 'fk-arm-l'
    row.operator('object.snap_utils', text = 'fk_arm.r').param = 'fk-arm-r'
    row = col.row()
    row.operator('object.snap_utils', text = 'ik_arm.l').param = 'ik-arm-l'
    row.operator('object.snap_utils', text = 'ik_arm.r').param = 'ik-arm-r'
    
    col = layout.column(align=True)
    row = col.row()
    row.operator('object.snap_utils', text = 'fk_leg.l').param = 'fk-leg-l'
    row.operator('object.snap_utils', text = 'fk_leg.r').param = 'fk-leg-r'
    row = col.row()
    row.operator('object.snap_utils', text = 'ik_leg.l').param = 'ik-leg-l'
    row.operator('object.snap_utils', text = 'ik_leg.r').param = 'ik-leg-r'
