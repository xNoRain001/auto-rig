from ..libs.blender_utils import add_scene_custom_prop, get_object_

def set_rotation_mode (armature, mode):
  # TODO: 替换为 get_pose_bones 
  bones = armature.pose.bones

  for bone in bones:
    bone.rotation_mode = mode

def on_update (self, context):
  armature_name = context.scene.armature_name
  mode = self.rotation_mode

  set_rotation_mode(get_object_(armature_name), mode)

def add_rotation_mode ():
  add_scene_custom_prop(
    'rotation_mode', 
    'Enum', 
    'XYZ', 
    items = [
      ('QUATERNION', "QUATERNION", ""),
      ('XYZ', "XYZ", ""),
    ],
    update = on_update
  )