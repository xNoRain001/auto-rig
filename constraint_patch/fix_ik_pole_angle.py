from ..libs.blender_utils import get_pose_bone

def fix_ik_pole_angle (config):
  get_pose_bone(config['name']).constraints['IK'].pole_angle = -1.5708
