from ..libs.blender_utils import get_operator, get_pose_bone

class OBJECT_OT_remove_target (get_operator()):
  bl_idname = "object.remove_target"
  bl_label = "Remove Target"

  def execute(self, context):
    scene = context.scene
    armature_name = scene.armature_name
    selected_target = scene.selected_target
    constraints = get_pose_bone(scene.armature_bone).constraints

    for constraint in constraints:
      if constraint.type == 'ARMATURE':
        print(selected_target)
        # targets = constraint.targets
        # target = targets.new()
        # armature = get_object_(armature_name)
        # target.target = armature
       

    return {'FINISHED'}
