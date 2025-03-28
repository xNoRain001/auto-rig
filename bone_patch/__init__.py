from .pole_target import pole_target
from .fix_location import fix_location
from .switch_direction import switch_direction
from .move import move
from .roll import roll
from .add_custom_props import add_custom_props
from .cal_roll import cal_roll

bone_patchs = {
  'mch_ik_arm.l.001': pole_target,
  'mch_ik_leg.l.001': pole_target,
  'mch_foot_roll.l': [cal_roll, fix_location],
  'mch_foot_heel.l': cal_roll,
  'ik_foot.l': fix_location,
  'mch_roll_side_01.l': [cal_roll, fix_location, roll],
  'mch_roll_side_02.l': [switch_direction, roll],
  'foot_heel.l': [cal_roll, move],
  'props': add_custom_props,
  'mch_ik_toes.l': cal_roll
}
