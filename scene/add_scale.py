from ..libs.blender_utils import add_scene_custom_prop, get_selected_pose_bones
from ..const import default_scale

def on_update (self, context):
  pose_bones = get_selected_pose_bones() or []
  sx, sy, sz = self.scale
  
  for pose_bone in pose_bones:
    custom_shape = pose_bone.custom_shape

    if custom_shape:
      osx, osy, osz = pose_bone.custom_shape_scale_xyz
      xyz = (osx * sx * 0.01, osy * sy * 0.01, osz * sz * 0.01)
      pose_bone.custom_shape_scale_xyz = xyz

def add_scale ():
  add_scene_custom_prop(
    'scale', 
    'IntVector', 
    subtype = 'XYZ', 
    size = 3,
    default = default_scale,
    update = on_update
  )
