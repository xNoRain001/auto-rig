from ..libs.blender_utils import (
  get_panel, get_pose_bones, get_active_object, get_object_,
  get_pose_bone, get_ui_list
)
from ..const import bl_category
from ..operators import OBJECT_OT_add_target, OBJECT_OT_remove_target
from ..operators.add_target import get_var_name

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
    armature = get_object_(armature_name)
    pose = armature.pose
    pose_bone = get_pose_bone(scene.dynamic_parent_bone)
    # print()
    # pose.bones["mch_parent_ik_hand.r"].constraints["骨架"].targets[2].weight
    # print(data.name)
    fcurve = armature.animation_data.drivers.find(f'pose.bones["{ pose_bone.name }"].constraints["{ data.name }"].targets[{ index }].weight')
    
    driver = fcurve.driver
    # variable = driver.variables[0]
    row = layout.row()
    row.prop(item, 'target', text = '')
    row.prop_search(
      item, 
      "subtarget", 
      pose, 
      "bones", 
      text=""
    )
    row = layout.row()
    row.prop(driver, 'expression', text = '')
    # row.prop(item, 'weight', text = '')
    row.operator(OBJECT_OT_remove_target.bl_idname, icon = 'X', text = '').index = index

def get_drivers (armature, pose_bone):
  drivers = []

  for fcurve in armature.animation_data.drivers:
    if fcurve.data_path.startswith(f'pose.bones["{ pose_bone.name }"]'):
      drivers.append(fcurve.driver)

  return drivers

class VIEW3D_PT_dynamic_parent (get_panel()):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = bl_category
  bl_label = "Dynamic Parent"
  bl_idname = "VIEW3D_PT_dynamic parent"

  def draw(self, context):
    layout = self.layout
    scene = context.scene
    mesh_name = scene.mesh_name
    armature_name = scene.armature_name
    armature = get_object_(armature_name)

    if armature:
      layout.prop_search(scene, "dynamic_parent_bone", armature.pose, "bones", text="")
      
      if scene.dynamic_parent_bone:
        pose_bone = get_pose_bone(scene.dynamic_parent_bone)
        constraints = pose_bone.constraints

        for constraint in constraints:
          if constraint.type == 'ARMATURE':
            # var_name = get_var_name(armature, pose_bone)
            row = layout.row()
            row.prop(scene, 'var_name', text = '变量名')
            row = layout.row()
            row.prop(scene, 'data_path', text = '数据路径')
            row = layout.row()
            # drivers = get_drivers(armature, pose_bone)
            # print(dir(constraint.targets[0].weight))
            
            # row.template_list("OBJECT_UL_armature_targets", "dynamic_parent", constraint, "a", scene, 'placeholder_prop')
            # row.template_list("OBJECT_UL_armature_targets", "dynamic_parent", constraint, "targets", scene, 'placeholder_prop')
            row.template_list("OBJECT_UL_armature_targets", "dynamic_parent", constraint, "targets", scene, 'placeholder_prop')
            col = row.column()
            col.operator(OBJECT_OT_add_target.bl_idname, icon='ADD', text="")
            # col.operator(OBJECT_OT_remove_target.bl_idname, icon='REMOVE', text="")
            break
