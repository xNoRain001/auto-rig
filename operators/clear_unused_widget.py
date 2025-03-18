from ..const import wgt_collection_name
from ..libs.blender_utils import (
  get_operator, get_pose_bones, get_collection, get_data
)

class OBJECT_OT_clear_unused_bone_widget (get_operator()):
  bl_idname = "object.clear_unused_bone_widget"
  bl_label = "Clear Unused Bone Widget"

  def execute(self, context):
    pose_bones = get_pose_bones()
    used_widgets = set()

    for pose_bone in pose_bones:
      custom_shape = pose_bone.custom_shape

      if custom_shape:
        used_widgets.add(custom_shape)

    collection = get_collection(wgt_collection_name)
    widgets = collection.objects

    for widget in widgets:
      if widget not in used_widgets:
        get_data().objects.remove(widget)

    return {'FINISHED'}
