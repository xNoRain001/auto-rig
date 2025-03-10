from ..libs.blender_utils import add_scene_custom_prop, get_pose_bones

def set_rotation_mode (armature, mode):
  bones = get_pose_bones(armature)

  for bone in bones:
    bone.rotation_mode = mode

def on_update (self, context):
  armature = context.scene.armature
  mode = self.rotation_mode

  if armature:
    set_rotation_mode(armature, mode)

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
