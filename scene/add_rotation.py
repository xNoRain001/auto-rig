from ..libs.blender_utils import add_scene_custom_prop, get_selected_pose_bones
from ..const import default_rotation

def on_update (self, context):
  pose_bones = get_selected_pose_bones() or []
  
  for pose_bone in pose_bones:
    custom_shape = pose_bone.custom_shape

    if custom_shape:
      pass

def add_rotation ():
  add_scene_custom_prop(
    'rotation', 
    'FloatVector', 
    subtype = 'EULER', 
    size = 3,
    default = default_rotation,
    update = on_update
  )
  