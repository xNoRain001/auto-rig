from ..libs.blender_utils import get_operator, get_selected_pose_bones

class OBJECT_OT_clear_bone_widget (get_operator()):
  bl_idname = "object.clear_bone_widget"
  bl_label = "Clear Bone Widget"

  def execute(self, context):
    pose_bones = get_selected_pose_bones() or []

    for pose_bone in pose_bones:
      widget = pose_bone.custom_shape

      if widget:
        pose_bone.custom_shape = None

    return {'FINISHED'}
