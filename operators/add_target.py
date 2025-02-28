from ..libs.blender_utils import get_operator, get_pose_bone, get_object_

def get_var_name (armature, pose_bone):
  var_name = None

  for fcurve in armature.animation_data.drivers:
    if fcurve.data_path.startswith(f'pose.bones["{ pose_bone.name }"]'):
      var = fcurve.driver.variables[0]
      var_name = var.name
      
      break

  return var_name

class OBJECT_OT_add_target (get_operator()):
  bl_idname = "object.add_target"
  bl_label = "Add Target"
  # TODO: 将 tagets 作为参数传递过来
  # targets: get_props().CollectionProperty()

  def execute(self, context):
    scene = context.scene
    armature_name = scene.armature_name
    var_name = scene.var_name
    data_path = scene.data_path
    armature = get_object_(armature_name)
    pose_bone = get_pose_bone(scene.dynamic_parent_bone)
    constraints = pose_bone.constraints

    for constraint in constraints:
      if constraint.type == 'ARMATURE':
        targets = constraint.targets
        target = targets.new()
        target.target = armature
        target.driver_remove("weight")
        fcurve = target.driver_add("weight")
        driver = fcurve.driver
        driver.type = 'SCRIPTED'
        var = driver.variables.new()
        var.name = var_name
        var.targets[0].id_type = 'OBJECT'
        var.targets[0].id = armature
        var.targets[0].data_path = data_path
        driver.expression = f'{ var_name } == '

        # prop = get_pose_bone('prop')
        # ui = prop.id_properties_ui(var_name)
        # ui.update({ 'max': len(driver.variables) - 1 })

    return {'FINISHED'}
