from ..libs.blender_utils import get_operator, get_pose_bone, get_props

class OBJECT_OT_remove_target (get_operator()):
  bl_idname = "object.remove_target"
  bl_label = "Remove Target"
  index: get_props().IntProperty()

  def execute(self, context):
    scene = context.scene
    constraints = get_pose_bone(scene.dynamic_parent_bone).constraints

    for constraint in constraints:
      if constraint.type == 'ARMATURE':
        targets = constraint.targets
        target = targets[self.index]
        # 需要清空驱动器，否则驱动器仍在，控制台会出警告
        target.driver_remove("weight")
        targets.remove(target)

    return {'FINISHED'}
