from ..libs.blender_utils import get_operator, get_pose_bone, get_object_

class OBJECT_OT_add_target (get_operator()):
  bl_idname = "object.add_target"
  bl_label = "Add Target"
  # TODO: 将 tagets 作为参数传递过来
  # targets: get_props().CollectionProperty()

  def execute(self, context):
    scene = context.scene
    armature_name = scene.armature_name
    constraints = get_pose_bone(scene.armature_bone).constraints

    for constraint in constraints:
      if constraint.type == 'ARMATURE':
        targets = constraint.targets
        target = targets.new()
        armature = get_object_(armature_name)
        target.target = armature
        type = 'l'
     
        for target in targets:
          target.driver_remove("weight")
          fcurve = target.driver_add("weight")
          driver = fcurve.driver
          driver.type = 'SCRIPTED'
          var = driver.variables.new()
          var.name = f'leg_ik_parent.{ type }'.replace('.', '_')
          var.targets[0].id_type = 'OBJECT'
          var.targets[0].id = armature
          var.targets[0].data_path = f'pose.bones["props"]["leg_ik_parent.{ type }"]'
          driver.expression = f'{ var.name } == 2'

    return {'FINISHED'}
