from ..libs.blender_utils import add_scene_custom_prop, get_selected_pose_bones

def on_update (self, context):
  pose_bones = get_selected_pose_bones() or []
  show_wire = self.show_wire
  
  for pose_bone in pose_bones:
    if pose_bone.custom_shape:
      pose_bone.bone.show_wire = show_wire

def add_show_wire ():
  add_scene_custom_prop('show_wire', 'Bool', True, update = on_update)
