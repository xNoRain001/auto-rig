
from ..libs.blender_utils import add_scene_custom_prop, get_pose_bone

def on_update (self, context):
  # get_pose_bone(ik_bones[0]).ik_stretch = 0.01
  # get_pose_bone(ik_bones[1]).ik_stretch = 0.01
  pass


def add_armature ():
  add_scene_custom_prop('arm_ik_stretch', 'Bool')
  add_scene_custom_prop('leg_ik_stretch', 'Bool')
