from ..libs.blender_utils import get_operator, get_ops, get_selected_pose_bones
from ..const import default_translation, default_rotation, default_scale

class OBJECT_OT_reset_transform (get_operator()):
  bl_idname = "object.reset_transform"
  bl_label = "Reset Transform"

  def execute(self, context):
    scene = context.scene
    scene.translation = default_translation
    scene.scale = default_scale
    scene.rotation = default_rotation

    return {'FINISHED'}
