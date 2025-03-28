from ..libs.blender_utils import get_edit_bone
from .init_arm import arm_tweak_bone_names
from .init_leg import leg_tweak_bone_names

def set_parent (bone, target, use_connect = False):
  bone.use_connect = use_connect
  bone.parent = target

def _init_parent (config):
  # TODO:
  # for tweak_bone_name in arm_tweak_bone_names:
  #   # org_arm_01.l
  #   org_bone = get_edit_bone(tweak_bone_name)

  for item in config:
    bone_name, parent_bone_name, use_connect = item
    bone = get_edit_bone(bone_name)
    parent_bone = get_edit_bone(parent_bone_name) if parent_bone_name else parent_bone_name
    
    if not bone:
      print(f'{ bone_name } 不存在')
      continue

    set_parent(bone, parent_bone, use_connect)

def init_parent ():
  # 遍历绑定完成的模型中每一个骨骼，输出它们的父级和连接状态
  config = [
    # ['def_hips', None, False],
    # ['def_spine_01', 'def_hips', False],
    # ['def_spine_02', 'def_spine_01', False],
    # ['def_chest', 'def_spine_02', False],
    # ['def_neck', 'def_chest', False],
    # ['def_head', 'def_neck', False],
    # ['def_shoulder.l', 'def_chest', False],
    # ['def_arm.l', 'def_shoulder.l', False],
    # ['def_forearm.l', 'def_arm.l', False],
    # ['def_hand.l', 'def_forearm.l', False],
    # ['def_thumb_01.l', 'def_hand.l', False],
    # ['def_thumb_02.l', 'def_thumb_01.l', False],
    # ['def_thumb_03.l', 'def_thumb_02.l', False],
    # ['def_finger_a_01.l', 'def_hand.l', False],
    # ['def_finger_a_02.l', 'def_finger_a_01.l', False],
    # ['def_finger_a_03.l', 'def_finger_a_02.l', False],
    # ['def_finger_b_01.l', 'def_hand.l', False],
    # ['def_finger_b_02.l', 'def_finger_b_01.l', False],
    # ['def_finger_b_03.l', 'def_finger_b_02.l', False],
    # ['def_finger_c_01.l', 'def_hand.l', False],
    # ['def_finger_c_02.l', 'def_finger_c_01.l', False],
    # ['def_finger_c_03.l', 'def_finger_c_02.l', False],
    # ['def_finger_d_01.l', 'def_hand.l', False],
    # ['def_finger_d_02.l', 'def_finger_d_01.l', False],
    # ['def_finger_d_03.l', 'def_finger_d_02.l', False],
    # ['def_forearm_01.l', 'def_forearm.l', False],
    # ['def_forearm_02.l', 'def_forearm_01.l', True],
    # ['def_forearm_03.l', 'def_forearm_02.l', True],
    # ['def_forearm_04.l', 'def_forearm_03.l', True],
    # ['def_arm_01.l', 'def_arm.l', False],
    # ['def_arm_02.l', 'def_arm_01.l', True],
    # ['def_arm_03.l', 'def_arm_02.l', True],
    # ['def_arm_04.l', 'def_arm_03.l', True],
    # ['def_leg.l', 'def_hips', False],
    # ['def_shin.l', 'def_leg.l', False],
    # ['def_foot.l', 'def_shin.l', False],
    # ['def_toes.l', 'def_foot.l', False],
    ['root', None, False],
    ['props', 'root', False],
    ['mch_int_leg.l', 'root', False],
    ['mch_switch_leg.l', 'mch_int_leg.l', False],
    ['mch_switch_shin.l', 'mch_switch_leg.l', True],
    ['mch_switch_foot.l', 'mch_switch_shin.l', True],
    ['mch_switch_toes.l', 'mch_switch_foot.l', True],
    ['mch_tweak_toes.l', 'mch_switch_toes.l', False],
    ['tweak_toes.l', 'mch_tweak_toes.l', False],
    ['org_toes.l', 'tweak_toes.l', False],
    ['tweak_tip_toes.l', 'mch_switch_toes.l', False],
    ['mch_tweak_foot.l', 'mch_switch_foot.l', False],
    ['tweak_foot.l', 'mch_tweak_foot.l', False],
    ['org_foot.l', 'tweak_foot.l', False],
    ['mch_tweak_shin.l', 'mch_switch_shin.l', False],
    ['tweak_shin.l', 'mch_tweak_shin.l', False],
    ['org_shin.l', 'tweak_shin.l', False],
    ['fk_leg.l', 'mch_int_leg.l', False],
    ['fk_shin.l', 'fk_leg.l', True],
    ['fk_foot.l', 'fk_shin.l', True],
    ['fk_toes.l', 'fk_foot.l', True],
    ['mch_ik_fk_leg_pole.l', 'fk_leg.l', False],
    ['mch_ik_leg.l', 'mch_int_leg.l', False],
    ['mch_ik_shin.l', 'mch_ik_leg.l', True],
    ['vis_leg_pole.l', 'mch_ik_leg.l', False],
    ['mch_int_arm.l', 'root', False],
    ['mch_switch_arm.l', 'mch_int_arm.l', False],
    ['mch_switch_forearm.l', 'mch_switch_arm.l', True],
    ['mch_switch_hand.l', 'mch_switch_forearm.l', True],
    ['mch_tweak_hand.l', 'mch_switch_hand.l', False],
    ['tweak_hand.l', 'mch_tweak_hand.l', False],
    ['org_hand.l', 'tweak_hand.l', False],
    ['mch_thumb_01.l', 'org_hand.l', False],
    ['thumb_01.l', 'mch_thumb_01.l', False],
    ['tweak_thumb_01.l', 'thumb_01.l', False],
    ['org_thumb_01.l', 'tweak_thumb_01.l', False],
    ['mch_thumb_02.l', 'thumb_01.l', True],
    ['thumb_02.l', 'mch_thumb_02.l', False],
    ['tweak_thumb_02.l', 'thumb_02.l', False],
    ['org_thumb_02.l', 'tweak_thumb_02.l', False],
    ['mch_thumb_03.l', 'thumb_02.l', True],
    ['thumb_03.l', 'mch_thumb_03.l', False],
    ['tweak_thumb_03.l', 'thumb_03.l', False],
    ['org_thumb_03.l', 'tweak_thumb_03.l', False],
    ['tweak_tip_thumb_03.l', 'thumb_03.l', False],
    ['mch_finger_a_01.l', 'org_hand.l', False],
    ['finger_a_01.l', 'mch_finger_a_01.l', False],
    ['tweak_finger_a_01.l', 'finger_a_01.l', False],
    ['org_finger_a_01.l', 'tweak_finger_a_01.l', False],
    ['mch_finger_a_02.l', 'finger_a_01.l', True],
    ['finger_a_02.l', 'mch_finger_a_02.l', False],
    ['tweak_finger_a_02.l', 'finger_a_02.l', False],
    ['org_finger_a_02.l', 'tweak_finger_a_02.l', False],
    ['mch_finger_a_03.l', 'finger_a_02.l', True],
    ['finger_a_03.l', 'mch_finger_a_03.l', False],
    ['tweak_finger_a_03.l', 'finger_a_03.l', False],
    ['org_finger_a_03.l', 'tweak_finger_a_03.l', False],
    ['tweak_tip_finger_a_03.l', 'finger_a_03.l', False],
    ['mch_finger_b_01.l', 'org_hand.l', False],
    ['finger_b_01.l', 'mch_finger_b_01.l', False],
    ['tweak_finger_b_01.l', 'finger_b_01.l', False],
    ['org_finger_b_01.l', 'tweak_finger_b_01.l', False],
    ['mch_finger_b_02.l', 'finger_b_01.l', True],
    ['finger_b_02.l', 'mch_finger_b_02.l', False],
    ['tweak_finger_b_02.l', 'finger_b_02.l', False],
    ['org_finger_b_02.l', 'tweak_finger_b_02.l', False],
    ['mch_finger_b_03.l', 'finger_b_02.l', True],
    ['finger_b_03.l', 'mch_finger_b_03.l', False],
    ['tweak_finger_b_03.l', 'finger_b_03.l', False],
    ['org_finger_b_03.l', 'tweak_finger_b_03.l', False],
    ['tweak_tip_finger_b_03.l', 'finger_b_03.l', False],
    ['mch_finger_c_01.l', 'org_hand.l', False],
    ['finger_c_01.l', 'mch_finger_c_01.l', False],
    ['tweak_finger_c_01.l', 'finger_c_01.l', False],
    ['org_finger_c_01.l', 'tweak_finger_c_01.l', False],
    ['mch_finger_c_02.l', 'finger_c_01.l', True],
    ['finger_c_02.l', 'mch_finger_c_02.l', False],
    ['tweak_finger_c_02.l', 'finger_c_02.l', False],
    ['org_finger_c_02.l', 'tweak_finger_c_02.l', False],
    ['mch_finger_c_03.l', 'finger_c_02.l', True],
    ['finger_c_03.l', 'mch_finger_c_03.l', False],
    ['tweak_finger_c_03.l', 'finger_c_03.l', False],
    ['org_finger_c_03.l', 'tweak_finger_c_03.l', False],
    ['tweak_tip_finger_c_03.l', 'finger_c_03.l', False],
    ['mch_finger_d_01.l', 'org_hand.l', False],
    ['finger_d_01.l', 'mch_finger_d_01.l', False],
    ['tweak_finger_d_01.l', 'finger_d_01.l', False],
    ['org_finger_d_01.l', 'tweak_finger_d_01.l', False],
    ['mch_finger_d_02.l', 'finger_d_01.l', True],
    ['finger_d_02.l', 'mch_finger_d_02.l', False],
    ['tweak_finger_d_02.l', 'finger_d_02.l', False],
    ['org_finger_d_02.l', 'tweak_finger_d_02.l', False],
    ['mch_finger_d_03.l', 'finger_d_02.l', True],
    ['finger_d_03.l', 'mch_finger_d_03.l', False],
    ['tweak_finger_d_03.l', 'finger_d_03.l', False],
    ['org_finger_d_03.l', 'tweak_finger_d_03.l', False],
    ['tweak_tip_finger_d_03.l', 'finger_d_03.l', False],
    ['tweak_tip_hand.l', 'mch_switch_hand.l', False],
    ['mch_tweak_forearm.l', 'mch_switch_forearm.l', False],
    ['tweak_forearm.l', 'mch_tweak_forearm.l', False],
    ['org_forearm.l', 'tweak_forearm.l', False],
    ['tweak_forearm_01.l', 'org_forearm.l', False],
    ['org_forearm_01.l', 'tweak_forearm_01.l', False],
    ['tweak_forearm_02.l', 'org_forearm.l', False],
    ['org_forearm_02.l', 'tweak_forearm_02.l', False],
    ['tweak_forearm_03.l', 'org_forearm.l', False],
    ['org_forearm_03.l', 'tweak_forearm_03.l', False],
    ['tweak_forearm_04.l', 'org_forearm.l', False],
    ['org_forearm_04.l', 'tweak_forearm_04.l', False],
    ['fk_arm.l', 'mch_int_arm.l', False],
    ['fk_forearm.l', 'fk_arm.l', True],
    ['fk_hand.l', 'fk_forearm.l', True],
    ['mch_ik_fk_arm_pole.l', 'fk_arm.l', False],
    ['mch_ik_arm.l', 'mch_int_arm.l', False],
    ['mch_ik_forearm.l', 'mch_ik_arm.l', True],
    ['vis_arm_pole.l', 'mch_ik_arm.l', False],
    ['torso', 'root', False],
    ['chest', 'torso', False],
    ['hips', 'torso', False],
    ['mch_fk_spine_02', 'torso', False],
    ['fk_spine_02', 'mch_fk_spine_02', False],
    ['mch_fk_chest', 'fk_spine_02', False],
    ['fk_chest', 'mch_fk_chest', False],
    ['tweak_chest', 'fk_chest', False],
    ['org_chest', 'tweak_chest', False],
    ['shoulder.l', 'org_chest', False],
    ['mch_arm.l', 'shoulder.l', False],
    ['mch_twist_arm.l', 'mch_arm.l', False],
    ['tweak_arm.l', 'mch_twist_arm.l', False],
    ['org_arm.l', 'tweak_arm.l', False],
    ['tweak_arm_01.l', 'org_arm.l', False],
    ['org_arm_01.l', 'tweak_arm_01.l', False],
    ['tweak_arm_02.l', 'org_arm.l', False],
    ['org_arm_02.l', 'tweak_arm_02.l', False],
    ['tweak_arm_03.l', 'org_arm.l', False],
    ['org_arm_03.l', 'tweak_arm_03.l', False],
    ['tweak_arm_04.l', 'org_arm.l', False],
    ['org_arm_04.l', 'tweak_arm_04.l', False],
    ['mch_neck', 'fk_chest', False],
    ['mch_spine_02_pivot', 'fk_spine_02', False],
    ['tweak_spine_02', 'mch_spine_02_pivot', False],
    ['org_spine_02', 'tweak_spine_02', False],
    ['mch_fk_spine_01', 'torso', False],
    ['fk_spine_01', 'mch_fk_spine_01', False],
    ['mch_fk_hips', 'fk_spine_01', False],
    ['fk_hips', 'mch_fk_hips', False],
    ['tweak_hips', 'fk_hips', False],
    ['org_hips', 'tweak_hips', False],
    ['mch_leg.l', 'org_hips', False],
    ['mch_twist_leg.l', 'mch_leg.l', False],
    ['tweak_leg.l', 'mch_twist_leg.l', False],
    ['org_leg.l', 'tweak_leg.l', False],
    ['tweak_spine_01', 'fk_hips', False],
    ['org_spine_01', 'tweak_spine_01', False],
    ['mch_int_neck', 'root', False],
    ['neck', 'mch_int_neck', False],
    ['tweak_neck', 'neck', False],
    ['org_neck', 'tweak_neck', False],
    ['mch_head', 'neck', False],
    ['mch_int_head', 'root', False],
    ['head', 'mch_int_head', False],
    ['tweak_head', 'head', False],
    ['org_head', 'tweak_head', False],
    ['tweak_top_head', 'head', False],
    ['mch_parent_leg_pole.l', None, False],
    ['leg_pole.l', 'mch_parent_leg_pole.l', False],
    ['mch_parent_ik_foot.l', None, False],
    ['ik_foot.l', 'mch_parent_ik_foot.l', False],
    ['mch_roll_side_01.l', 'ik_foot.l', False],
    ['mch_roll_side_02.l', 'mch_roll_side_01.l', False],
    ['mch_foot_heel.l', 'mch_roll_side_02.l', False],
    ['mch_foot_roll.l', 'mch_foot_heel.l', False],
    ['mch_ik_foot.l', 'mch_foot_roll.l', False],
    ['mch_ik_toes.l', 'mch_ik_foot.l', True],
    ['ik_toes.l', 'mch_ik_toes.l', False],
    ['foot_heel.l', 'ik_foot.l', False],
    ['mch_parent_arm_pole.l', None, False],
    ['arm_pole.l', 'mch_parent_arm_pole.l', False],
    ['mch_parent_ik_hand.l', None, False],
    ['ik_hand.l', 'mch_parent_ik_hand.l', False],
    ['mch_ik_fk_foot.l', 'fk_foot.l', False]
  ]

  _init_parent(config)
