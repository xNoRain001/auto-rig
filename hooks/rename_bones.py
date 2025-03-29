from ..libs.blender_utils import get_pose_bone

def rename_bones ():
  get_pose_bone('org_shoulder.l').name = 'shoulder.l'
  get_pose_bone('org_shoulder.r').name = 'shoulder.r'
  get_pose_bone('mch_finger_d_01.l').name = 'palm.l'
  get_pose_bone('mch_finger_d_01.r').name = 'palm.r'
