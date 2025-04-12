from ..libs.blender_utils import get_panel

from ..const import bl_category
from ..operators import OBJECT_OT_rig_bow

class VIEW3D_PT_rig_bow (get_panel()):
  bl_label = 'Rig Bow'
  bl_region_type = 'UI'
  bl_space_type = 'VIEW_3D'
  bl_category = bl_category
  bl_idname = 'VIEW3D_PT_rig_bow'

  # @classmethod
  # def poll(cls, context):
  #   return show_panel_in_pose_mode()

  def draw(self, context):
    layout = self.layout
    scene = context.scene

    box = layout.box()
    row = box.row()
    row.label(text = 'Armature ')
    row.prop(scene, 'bow_armature', text = '')

    if not scene.bow_armature:
      return
    
    row = box.row()
    row.label(text = 'Bowstring max distance ')
    row.prop(scene, 'bowstring_max_distance', text = '')
    row = box.row()
    row.label(text = 'Bow limb max angle ')
    row.prop(scene, 'bow_limb_max_angle', text = '')
    row = box.row()
    row.operator(OBJECT_OT_rig_bow.bl_idname, text = 'Rig bow')
