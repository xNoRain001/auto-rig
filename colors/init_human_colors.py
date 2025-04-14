from collections import defaultdict

from . import init_bones_color
from ..const import (
  root_collection,
  fk_arm_l_collection,
  ik_arm_l_collection,
  tweak_arm_l_collection,
  fk_arm_r_collection,
  ik_arm_r_collection,
  tweak_arm_r_collection,
  torso_collection,
  tweak_hand_l_collection,
  tweak_hand_r_collection,
  fk_leg_l_collection,
  ik_leg_l_collection,
  tweak_leg_l_collection,
  fk_leg_r_collection,
  ik_leg_r_collection,
  tweak_leg_r_collection,
  torso_collection,
  fk_torso_collection,
  tweak_torso_collection,
  props_collection,
  hand_l_collection,
  hand_r_collection
)

def gen_color_map (scene):
  torso_color = scene.torso_color
  fk_ik_l_color = scene.fk_ik_l_color
  fk_ik_r_color = scene.fk_ik_r_color
  tweak_color = scene.tweak_color
  color_map = defaultdict(list)
  color_map[tweak_color].extend([
    tweak_leg_r_collection,
    tweak_leg_l_collection,
    tweak_hand_l_collection,
    tweak_hand_r_collection,
    tweak_arm_l_collection,
    tweak_arm_r_collection,
    tweak_torso_collection
  ])
  color_map[fk_ik_l_color].extend([
    fk_arm_l_collection,
    fk_leg_l_collection,
    ik_arm_l_collection,
    ik_leg_l_collection,
    hand_l_collection
  ])
  color_map[fk_ik_r_color].extend([
    fk_arm_r_collection,
    fk_leg_r_collection,
    ik_arm_r_collection,
    ik_leg_r_collection,
    hand_r_collection
  ])
  color_map[torso_color].extend([
    torso_collection,
    fk_torso_collection,
    root_collection,
    props_collection
  ])

  return color_map

def init_human_color (scene):
  init_bones_color(gen_color_map(scene))
