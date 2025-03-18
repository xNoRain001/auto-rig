from ..libs.blender_utils import (
  set_mode,
  add_scene_custom_prop, 
  get_selected_pose_bones,
)

def on_update (self, context):
  set_mode('POSE')
  pose_bones = get_selected_pose_bones()

  if not pose_bones:
    return

  wire_width = self.wire_width
  
  for pose_bone in pose_bones:
    if pose_bone.custom_shape:
      pose_bone.custom_shape_wire_width = wire_width

def add_wire_width ():
  add_scene_custom_prop('wire_width', 'Float', 2.5, update = on_update)
