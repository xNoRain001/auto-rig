from ..libs.blender_utils import get_panel

from ..operators import OBJECT_OT_retarget_to_mixamo
from ..const import bl_category

class VIEW3D_PT_retarget_to_mixamo (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Retarget To Mixamo"
  bl_idname = "VIEW3D_PT_retarget_to_mixamo"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    box = layout.box()
    
    row = box.row()
    row.label(text = 'Armature ')
    row.prop(scene, 'armature', text = '')
    row = box.row()
    row.label(text = 'Retarget Armature ')
    row.prop(scene, 'retarget_armature', text = '')

    if not scene.armature or not scene.retarget_armature:
      return
    
    row = box.row()
    row.operator(OBJECT_OT_retarget_to_mixamo.bl_idname, text = 'Retarget')
    