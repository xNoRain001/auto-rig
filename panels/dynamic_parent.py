from ..libs.blender_utils import (
  get_panel, get_pose_bones, get_active_object, get_object_,
  get_pose_bone, get_ui_list
)
from ..const import bl_category
from ..operators import OBJECT_OT_add_target, OBJECT_OT_remove_target

class Armature_Targets (get_ui_list()):
  bl_label = "Armature Targets"
  bl_idname = "OBJECT_UL_armature_targets"

  def draw_item(
    self, 
    context, 
    layout, 
    data, 
    item, 
    icon, 
    active_data, 
    active_propname,
    index
  ):
    scene = context.scene
    armature_name = scene.armature_name
    pose = get_object_(armature_name).pose
    row = layout.row()
    row.prop_search(
      item, 
      "subtarget", 
      pose, 
      "bones", 
      text=""
    )

class VIEW3D_PT_dynamic_parent (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Dynamic Parent"
  bl_idname = "VIEW3D_PT_dynamic parent"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    armature_name = scene.armature_name
    layout.prop_search(scene, "dynamic_parent_bone", get_object_(armature_name).pose, "bones", text="")
    
    if scene.dynamic_parent_bone:
      constraints = get_pose_bone(scene.dynamic_parent_bone).constraints

      for constraint in constraints:
        if constraint.type == 'ARMATURE':
          row = layout.row()
          row.template_list("OBJECT_UL_armature_targets", "dynamic_parent", constraint, "targets", scene, 'selected_target')
          col = row.column()
          col.operator(OBJECT_OT_add_target.bl_idname, icon='ADD', text="")
          col.operator(OBJECT_OT_remove_target.bl_idname, icon='REMOVE', text="")
          break
